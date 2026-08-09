#!/usr/bin/env python3
"""Build a searchable Markdown transcription of ST RM0440.

MuPDF's XHTML output is used for the document outline.  The main body is
reconstructed from MuPDF's positioned HTML output: unlike flow text, it keeps
register fields, table cells, and continuation text in visual reading order.
"""
from __future__ import annotations

import argparse
import html
import re
import subprocess
import tempfile
import textwrap
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET

NS = "{http://www.w3.org/1999/xhtml}"
TOTAL_PAGES = 2140


@dataclass
class TextBlock:
    top: float
    left: float
    line_height: float
    size: float
    bold: bool
    text: str


@dataclass(frozen=True)
class FigureSpec:
    page: int
    number: int
    occurrence: int
    top: float
    line_height: float
    title: str

    @property
    def filename(self) -> str:
        suffix = "" if self.occurrence == 1 else f"-part-{self.occurrence}"
        return f"figure-{self.number:04d}{suffix}.png"


@dataclass
class VisualRow:
    top: float
    blocks: list[TextBlock]
    text: str = ""
    space_text: str = ""
    size: float = 0.0
    left: float = 0.0
    span: float = 0.0
    line_height: float = 10.0
    bold: bool = False


def tag_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def normalize_text(text: str) -> str:
    """Normalize PDF extraction whitespace without changing meaningful text."""
    text = html.unescape(text)
    text = text.replace("\u00a0", " ").replace("\u00ad", "")
    text = text.replace("\u200b", "")
    text = re.sub(r"\s+", " ", text).strip()
    # MuPDF keeps a few words split at a visual line wrap.
    text = re.sub(r"([A-Za-z])-\s+([a-z])", r"\1-\2", text)
    # Remove extraction whitespace before ordinary punctuation, but retain the
    # intentional space before an ellipsis (``9, 10, ...``).
    text = re.sub(r"\s+([,;:!?]|\.(?!\.))", r"\1", text)
    text = re.sub(r"([.!?])(?=[A-Z][a-z])", r"\1 ", text)
    # Preserve repeated punctuation: the manual uses ``..`` and ``...`` in
    # meaningful ranges such as ``FPU_IE[5..0]`` and ``COMP1..7``.
    text = re.sub(r"([\[(])\s+", r"\1", text)
    text = re.sub(r"\s+([\])])", r"\1", text)
    text = re.sub(r"(?<=\w)_ (?=\w)", "_", text)
    return text


def plain_text(node: ET.Element) -> str:
    return normalize_text("".join(node.itertext()))


def clean_heading(text: str) -> str:
    text = normalize_text(text)
    # Contents pages use dot leaders. The main contents pages are omitted, but
    # this also makes the helper safe for headings copied from them.
    text = re.sub(r"(?:\s*\.\s*){3,}\s*\d+\s*$", "", text)
    return text.rstrip(" .")


def heading_number(text: str) -> tuple[int, ...] | None:
    # Section numbers are followed by whitespace. A word boundary also matches
    # labels such as ``4-bit``, which must not overwrite the target for
    # references to chapter 4.
    m = re.match(r"^(\d+(?:\.\d+)*)(?=\s)", text)
    if not m:
        return None
    return tuple(int(x) for x in m.group(1).split("."))


def heading_level(tag: str, text: str) -> int:
    nums = heading_number(text)
    if nums:
        # Chapter 3 -> ##; 3.7 -> ###; 3.7.1 -> ####.
        return len(nums) + 1
    if tag == "h2":
        return 2
    return 3


def slug_for(text: str, number: tuple[int, ...] | None, page: int) -> str:
    """Return the conventional GitHub-style anchor generated for a heading."""
    del number, page  # The full heading text already makes numbered headings unique.
    slug = re.sub(r"[^\w\- ]", "", text.lower(), flags=re.UNICODE)
    return slug.replace(" ", "-") or "unnumbered"


def render_inline(node: ET.Element) -> str:
    """Return inline PDF text without carrying fragile typography markup."""
    # The source uses nested bold/italic spans for typography, trademark
    # markers, and footnote markers. Keeping the underlying characters plain
    # avoids malformed Markdown such as ``Cortex**®**`` and is more searchable.
    return "".join(node.itertext())


def rendered_text(node: ET.Element) -> str:
    return normalize_text(render_inline(node))


def parse_style_number(style: str, key: str, default: float) -> float:
    match = re.search(rf"{key}:([0-9.]+)pt", style)
    return float(match.group(1)) if match else default


def parse_positioned_html(path: Path) -> dict[int, list[TextBlock]]:
    """Parse MuPDF's positioned HTML page-by-page.

    The complete HTML document has a malformed closing tag in a small number
    of pages, so each page div is parsed independently after extraction.
    """
    source = path.read_text(encoding="utf-8")
    pages: dict[int, list[TextBlock]] = {}
    page_re = re.compile(r'<div id="page(\d+)"[^>]*>(.*?)</div>', re.S)
    for match in page_re.finditer(source):
        page = int(match.group(1))
        # Positioned HTML embeds figures as non-XML ``<img>`` tags. Their
        # captions/text are in <p> blocks; strip the bitmap payloads before
        # parsing to keep extraction fast and avoid XML parser errors.
        body = re.sub(r"<img\b[^>]*>", "", match.group(2), flags=re.S)
        try:
            wrapper = ET.fromstring("<div>" + body + "</div>")
        except ET.ParseError as exc:
            raise RuntimeError(f"Could not parse positioned HTML page {page}") from exc
        blocks: list[TextBlock] = []
        for elem in list(wrapper):
            if tag_name(elem.tag) != "p":
                continue
            style = elem.attrib.get("style", "")
            if "top:" not in style or "left:" not in style:
                continue
            xml = ET.tostring(elem, encoding="unicode")
            sizes = [float(x) for x in re.findall(r"font-size:([0-9.]+)pt", xml)]
            text = plain_text(elem)
            blocks.append(
                TextBlock(
                    top=parse_style_number(style, "top", 0.0),
                    left=parse_style_number(style, "left", 0.0),
                    line_height=parse_style_number(style, "line-height", 10.0),
                    size=max(sizes or [10.0]),
                    bold="<b" in xml or "Bold" in xml,
                    text=text,
                )
            )
        pages[page] = blocks
    return pages


def is_positioned_artifact(block: TextBlock, page: int) -> bool:
    """Remove page furniture while retaining content near page edges."""
    text = block.text
    if not text:
        return True
    # Running title/header and page footer.
    if block.top < 80:
        return True
    if block.top > 730 and (
        "RM0440" in text
        # RM0440's footer denominator changes between document sections (for
        # example, chapter 31 uses ``1404/88``), so match the full page-marker
        # shape instead of assuming the PDF's physical page count.
        or re.fullmatch(r"\d{1,4}/\d{1,4}", text)
        or re.fullmatch(r"\d{1,4}", text)
        or text in {"March 2025", "www.st.com"}
    ):
        return True
    # The cover's title is represented by the generated document heading.
    if page == 1 and block.top < 180:
        return True
    return False


def is_heading_row(row: VisualRow, page: int) -> bool:
    text = row.space_text
    nums = heading_number(text)
    if row.size >= 12 and row.bold:
        if nums and nums[0] <= 50:
            # Diagram labels such as "2 ----- 4" are not headings.
            return len(nums) >= 1 and not re.search(r"[-+×<>]{3,}", text)
        if text in {"Introduction", "Related documents", "Index", "Revision history"}:
            return True
    # Index letters are emitted as unnumbered h3 elements.
    if page >= 2134 and row.size >= 12 and re.fullmatch(r"[A-Z]", text):
        return True
    return False


def is_minor_heading_row(row: VisualRow, page: int) -> bool:
    """Identify bold, unnumbered labels used as in-section subheadings."""
    text = row.space_text
    return bool(
        page >= 74
        and len(row.blocks) == 1
        and row.bold
        and 10.5 <= row.size < 13
        and 115 <= row.left <= 135
        and 1 <= len(text) <= 100
        and re.match(r"^[A-Za-z0-9]", text)
        and not re.search(r"[.!?]$", text)
        and not is_heading_row(row, page)
        and not re.match(
            r"^(?:Table|Figure|Address offset|Reset value|Access|Bits?\b|"
            r"Note|Warning|Caution|\d+[:.]|[•–—])",
            text,
        )
        and not re.search(r"(?:\.{3,}|\s\d+\s*$)", text)
    )


def combine_row_blocks(blocks: list[TextBlock], table_like: bool) -> tuple[str, str]:
    cells = [b.text for b in blocks if b.text]
    if not cells:
        return "", ""
    spaced = " ".join(cells)
    if len(cells) >= 2 and cells[0] in {"•", "–", "—"}:
        spaced = cells[0] + " " + " ".join(cells[1:])
    if table_like:
        # Pipes make register maps and table rows legible while preserving
        # every cell as searchable text. No guessed column semantics are added.
        piped = "| " + " | ".join(cells) + " |"
    else:
        piped = spaced
    return spaced, piped


def make_visual_rows(blocks: list[TextBlock], page: int) -> list[VisualRow]:
    ordered = sorted(
        (b for b in blocks if not is_positioned_artifact(b, page)),
        key=lambda b: (b.top, b.left),
    )
    rows: list[VisualRow] = []
    for block in ordered:
        if not block.text:
            continue
        if not rows or block.top - rows[-1].top > 2.0:
            rows.append(VisualRow(top=block.top, blocks=[block]))
        else:
            rows[-1].blocks.append(block)

    for row in rows:
        row.blocks.sort(key=lambda b: b.left)
        row.left = row.blocks[0].left
        row.span = row.blocks[-1].left - row.left
        row.size = max(b.size for b in row.blocks)
        row.line_height = max(b.line_height for b in row.blocks)
        row.bold = any(b.bold for b in row.blocks)
        row.space_text = combine_row_blocks(row.blocks, False)[0]
        # A wide, multi-cell visual row is a table/register/diagram row. A
        # bullet marker plus its text is deliberately not treated as a table.
        table_like = (
            len(row.blocks) >= 2
            and row.span >= 45
            and row.blocks[0].text not in {
                "•",
                "–",
                "—",
                "Note:",
                "Warning:",
                "Caution:",
            }
            and not is_heading_row(row, page)
        )
        row.text = combine_row_blocks(row.blocks, table_like)[1]
    return rows


def is_structural_start(text: str) -> bool:
    return bool(
        re.match(
            r"^(?:Address offset|Reset value|Access|Table\s+\d+\.|Figure\s+\d+\.|"
            r"Bit\s|Bits\s|[0-9]+:\s|[0-9]+\.\s|[•–—])",
            text,
        )
    )


def can_merge_rows(previous: VisualRow, current: VisualRow) -> bool:
    """Merge ordinary wrapped prose, not table cells or register rows."""
    previous_is_bullet = len(previous.blocks) == 2 and previous.blocks[0].text in {"•", "–", "—"}
    previous_is_callout = bool(previous.blocks) and previous.blocks[0].text in {
        "Note:",
        "Warning:",
        "Caution:",
    }
    footnote_wrap = bool(re.match(r"^[a-z]\.\s", previous.space_text)) and (
        current.left >= previous.left
    )
    if (
        (
            len(previous.blocks) != 1
            and not previous_is_bullet
            and not previous_is_callout
            and not footnote_wrap
        )
        or len(current.blocks) != 1
    ):
        return False
    # Body prose is 10 pt. Register descriptions and single-column table
    # cells are usually 9 pt; merge those only when they are indented text,
    # which repairs wrapped register explanations without joining bit values.
    if previous.size < 9.5 or current.size < 9.5:
        if not (previous.left >= 190 and current.left >= 190) and not footnote_wrap:
            return False
    left_delta = current.left - previous.left
    same_indent = abs(left_delta) <= 2.0
    wrapped_list = (
        left_delta >= 0
        and left_delta <= 30.0
        and previous.space_text.startswith(("•", "–", "—"))
    )
    wrapped_callout = (
        left_delta >= 0
        and left_delta <= 50.0
        and previous.space_text.startswith(("Note:", "Warning:", "Caution:"))
    )
    wrapped_numbered = (
        left_delta >= 0
        and left_delta <= 30.0
        and re.match(r"^\d+\.\s", previous.space_text) is not None
    )
    if not (same_indent or wrapped_list or wrapped_callout or wrapped_numbered or footnote_wrap):
        return False
    gap = current.top - previous.top
    if gap > max(previous.line_height, current.line_height) + 3.0:
        return False
    if is_structural_start(current.space_text):
        return False
    # A new bullet at the same indent is a new item; a wrapped continuation
    # without a marker is allowed to merge.
    if current.space_text.startswith(("•", "–", "—")):
        return False
    return True


def as_blockquote(text: str) -> str:
    match = re.match(r"^(Note|Warning|Caution):\s*(.*)$", text)
    if match:
        return f"> **{match.group(1)}:** {match.group(2)}".rstrip()
    return "> " + text


def is_pipe_row(text: str) -> bool:
    """Return whether a line is a candidate Markdown table row."""
    return text.startswith("|") and text.count("|") >= 2


def is_layout_boundary(text: str) -> bool:
    """Return whether a line clearly ends an extracted layout block."""
    return text.startswith(
        (
            "#",
            "<a ",
            "![",
            "```",
            "---",
            "> ",
            "- ",
            "  -",
            "**Table",
            "**Figure",
            "**Bit",
        )
    ) or bool(re.match(r"^(?:\d+|[a-z])\.\s", text))


def is_layout_continuation(text: str) -> bool:
    """Identify short, unclassified lines emitted from a table or diagram."""
    if not text or is_layout_boundary(text):
        return False
    if text in {"-", "--"}:
        return True
    # Ordinary prose is already merged by page_items. Remaining short lines
    # are typically wrapped table cells, register labels, or diagram labels.
    return len(text) <= 120 and not text.startswith(("Address offset:", "Reset value:", "Access:"))


def has_pipe_ahead(lines: list[str], start: int, limit: int = 4) -> bool:
    """Return whether a short layout fragment leads into a pipe row."""
    seen = 0
    for candidate in lines[start:]:
        if not candidate:
            continue
        if is_pipe_row(candidate):
            return True
        if is_layout_boundary(candidate) or not is_layout_continuation(candidate):
            return False
        seen += 1
        if seen >= limit:
            return False
    return False


def split_table_cells(text: str) -> list[str]:
    """Split a generated pipe row without changing its cell text."""
    cells = text.strip().split("|")
    if cells and cells[0].strip() == "":
        cells = cells[1:]
    if cells and cells[-1].strip() == "":
        cells = cells[:-1]
    return [cell.strip() for cell in cells]


def normalized_table_row(text: str) -> str:
    """Normalize spacing and escape literal pipes inside table cells."""
    cells = [cell.replace("|", r"\|") for cell in split_table_cells(text)]
    return "| " + " | ".join(cells) + " |"


def render_layout_blocks(lines: list[str]) -> list[str]:
    """Make extracted tables and diagrams render as intentional Markdown.

    MuPDF exposes many PDF tables as positioned text rather than semantic
    rows. A table row can therefore be followed by a short, unpiped cell
    continuation. Keeping those fragments as ordinary Markdown makes the
    document look broken. Complete, consistently shaped rows become real
    Markdown tables; ambiguous fragments are kept in compact text fences so
    their visual order and every extracted label are preserved.
    """
    rendered: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        previous_nonblank = ""
        for previous in reversed(rendered):
            if previous:
                previous_nonblank = previous
                break

        starts_layout = is_pipe_row(line) or (
            previous_nonblank.startswith(("![", "**Table"))
            and has_pipe_ahead(lines, i + 1)
            and is_layout_continuation(line)
            and re.search(r"[.!?]$", line) is None
        )
        if not starts_layout:
            rendered.append(line)
            i += 1
            continue

        values: list[str] = []
        saw_raw = False
        j = i
        while j < len(lines):
            if not lines[j]:
                j += 1
                continue
            candidate = lines[j]
            if is_pipe_row(candidate):
                values.append(candidate)
                j += 1
                continue
            if is_layout_boundary(candidate):
                break
            if not is_layout_continuation(candidate):
                break
            # A sentence ending in punctuation belongs to the surrounding
            # prose unless another pipe row immediately follows it. This
            # prevents a table from consuming the next paragraph.
            following = ""
            n = j + 1
            while n < len(lines):
                if lines[n]:
                    following = lines[n]
                    break
                n += 1
            if re.search(r"[.!?]$", candidate) and not is_pipe_row(following):
                break
            values.append(candidate)
            saw_raw = True
            j += 1

        # A lone extracted row has no header/separator pair, so it is not a
        # Markdown table. Keep it as literal layout instead of emitting raw
        # pipes that Markdown renderers interpret inconsistently.
        if len(values) == 1 and not saw_raw:
            rendered.extend(["```text", values[0], "```"])
        elif not saw_raw:
            rows = [split_table_cells(value) for value in values]
            widths = {len(row) for row in rows}
            if len(widths) == 1 and next(iter(widths), 0) <= 12:
                rendered.append(normalized_table_row(values[0]))
                rendered.append("| " + " | ".join("---" for _ in rows[0]) + " |")
                rendered.extend(normalized_table_row(value) for value in values[1:])
            else:
                rendered.extend(["```text", *values, "```"])
        else:
            rendered.extend(["```text", *values, "```"])
        i = j
    return rendered


def normalize_markdown_blocks(lines: list[str]) -> list[str]:
    """Add the blank lines required around Markdown block constructs."""
    normalized: list[str] = []
    in_fence = False

    def blank() -> None:
        if normalized and normalized[-1] != "":
            normalized.append("")

    for index, line in enumerate(lines):
        is_fence = line.lstrip().startswith("```")
        if is_fence:
            if not in_fence:
                blank()
                normalized.append(line)
                in_fence = True
            else:
                normalized.append(line)
                in_fence = False
                blank()
            continue
        if in_fence:
            normalized.append(line)
            continue

        is_heading = re.match(r"^#{1,6}\s", line) is not None
        is_table = is_pipe_row(line)
        previous_is_table = bool(normalized and is_pipe_row(normalized[-1]))
        next_is_table = index + 1 < len(lines) and is_pipe_row(lines[index + 1])

        if is_heading or (is_table and not previous_is_table):
            blank()
        normalized.append(line)
        if is_heading or (is_table and not next_is_table):
            blank()

    # PDF rows arrive as independent blocks, which otherwise turns every list
    # into a loose list with large paragraph gaps. Keep adjacent parent/child
    # items and wrapped item text in one compact Markdown list.
    compact: list[str] = []
    list_item = re.compile(r"^(?P<indent>\s*)(?P<marker>[-+*]|\d+\.)\s+")
    for index, line in enumerate(normalized):
        if line == "" and compact and index + 1 < len(normalized):
            next_line = normalized[index + 1]
            next_item = list_item.match(next_line)

            # Continue callouts and ordinary prose rows that the PDF split at
            # a page/column boundary. A soft line break renders as one
            # paragraph; blockquote continuations retain their marker.
            if (
                compact[-1].startswith("> ")
                and not re.search(r"[.!?:;]$", compact[-1])
                and re.match(r"^[a-z]", next_line)
            ):
                normalized[index + 1] = "> " + next_line
                continue
            if (
                not is_layout_boundary(compact[-1])
                and not is_pipe_row(compact[-1])
                and not re.search(r"[.!?:;]$", compact[-1])
                and re.match(r"^[a-z]", next_line)
            ):
                continue

            # Find a list marker governing the preceding contiguous lines.
            active_item: re.Match[str] | None = None
            for previous in reversed(compact):
                if previous == "":
                    break
                match = list_item.match(previous)
                if match:
                    active_item = match
                    break
                if not previous.startswith(" "):
                    break

            if active_item and next_item:
                active_indent = len(active_item.group("indent"))
                next_indent = len(next_item.group("indent"))
                if next_indent > active_indent:
                    # Nested markers align with the parent's content column;
                    # ordered markers therefore need one extra leading space.
                    content_indent = len(active_item.group(0))
                    normalized[index + 1] = " " * content_indent + next_line.lstrip()
                    continue
                previous_ordered = active_item.group("marker").endswith(".")
                next_ordered = next_item.group("marker").endswith(".")
                if previous_ordered == next_ordered:
                    if active_indent > 0 and next_indent > 0 and active_indent != next_indent:
                        normalized[index + 1] = " " * active_indent + next_line.lstrip()
                    continue

            # A lowercase fragment after an unfinished item is usually a PDF
            # page/column wrap that row merging could not recover.
            if (
                active_item
                and not re.search(r"[.!?:;]$", compact[-1])
                and re.match(r"^[a-z]", next_line)
            ):
                prefix_width = len(active_item.group(0))
                normalized[index + 1] = " " * prefix_width + next_line
                continue

        if (
            line
            and compact
            and compact[-1].startswith("> ")
            and re.match(r"^[a-z]", line)
        ):
            line = "> " + line

        if line and compact and compact[-1].startswith(" ") and not line.startswith(
            (" ", "#", ">", "|", "```", "![")
        ) and not list_item.match(line):
            active_item = None
            for previous in reversed(compact):
                if previous == "":
                    break
                match = list_item.match(previous)
                if match:
                    active_item = match
                    break
                if not previous.startswith(" "):
                    break
            if active_item:
                line = " " * len(active_item.group(0)) + line

        if line != "" or not compact or compact[-1] != "":
            compact.append(line)
    return compact


def sanitize_inline_markdown(text: str) -> str:
    """Protect technical notation and make extracted web addresses clickable."""
    sanitized: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence:
            # Long rules and leading plus signs occur in extracted formulas
            # and diagrams; escape them so they do not become headings/lists.
            if re.fullmatch(r"-{4,}", line):
                line = "\\" + line
            elif line.startswith("+ "):
                line = "\\" + line

            # Register notation such as ``HADDR[27:26](1)`` is a footnote,
            # not a Markdown link whose destination happens to be "1".
            line = re.sub(r"\[([^\]\n]+)\]\((\d+)\)", r"[\1]\\(\2)", line)
            # Preserve multiplication signs without accidentally opening an
            # emphasis span that may run across unrelated technical text.
            line = re.sub(r"(?<=\S) \* (?=\S)", r" \\* ", line)
            line = re.sub(r"(?<=\S) \+ (?=\S)", r" \\+ ", line)
            # Use ordinary Markdown links rather than angle-bracket autolinks;
            # raw angle brackets can be mistaken for HTML or tags in register
            # comparison expressions.
            line = re.sub(
                r"(?<![\[])(https?://[^\s<>()]*[A-Za-z0-9/#])",
                r"[\1](\1)",
                line,
            )
            line = re.sub(
                r"(?<![\w/<])(www\.(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}"
                r"(?:/[^\s<>()]*[A-Za-z0-9/#])?)",
                r"[\1](https://\1)",
                line,
            )
            line = line.replace("<", r"\<")
        sanitized.append(line)
    return "\n".join(sanitized)


def wrap_markdown_lines(lines: list[str], width: int = 100) -> list[str]:
    """Wrap prose and list items without touching layout-sensitive blocks."""
    wrapped: list[str] = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            wrapped.append(line)
            continue
        if in_fence or not line or is_pipe_row(line) or line.startswith(
            ("#", "<a ", "![", "**Table", "**Figure", "---", "> ")
        ):
            wrapped.append(line)
            continue

        # Navigation links should stay on one physical line. CommonMark allows
        # soft breaks in labels, but keeping the complete link together is
        # more portable across documentation renderers.
        if re.match(r"^\s*- \[[^]]+\]\(#[^)]+\)$", line):
            wrapped.append(line)
            continue

        match = re.match(r"^(?P<prefix>\s*(?:[-*+]\s+|\d+\.\s+))(?P<body>.*)$", line)
        if match:
            prefix = match.group("prefix")
            body = match.group("body")
            pieces = textwrap.wrap(
                body,
                width=max(20, width - len(prefix)),
                break_long_words=False,
                break_on_hyphens=False,
            )
            if pieces:
                wrapped.append(prefix + pieces[0])
                wrapped.extend(" " * len(prefix) + piece for piece in pieces[1:])
            else:
                wrapped.append(line)
            continue

        pieces = textwrap.wrap(
            line,
            width=width,
            break_long_words=False,
            break_on_hyphens=False,
        ) or [line]
        for piece_index, piece in enumerate(pieces):
            if piece_index and re.match(r"^\d+\.\s", piece):
                piece = re.sub(r"^(\d+)\.", r"\1\\.", piece)
            wrapped.append(piece)
    return wrapped


def repair_known_tables(lines: list[str]) -> list[str]:
    """Repair the two introductory tables whose PDF cells span many lines.

    The first product tables are especially useful as navigation aids, but
    MuPDF emits their vertically centered cells as independent positioned
    lines. These compact, source-faithful tables preserve the same values
    while making the introductory section immediately readable.
    """
    table_abbreviations = [
        "| Abbreviation | Meaning |",
        "| --- | --- |",
        "| read/write (rw) | Software can read and write to this bit. |",
        "| read-only (r) | Software can only read this bit. |",
        "| write-only (w) | Software can only write to this bit. Reading this bit returns the reset value. |",
        "| read/clear write0 (rc_w0) | Software can read as well as clear this bit by writing 0. Writing 1 has no effect on the bit value. |",
        "| read/clear write1 (rc_w1) | Software can read as well as clear this bit by writing 1. Writing 0 has no effect on the bit value. |",
        "| read/clear write (rc_w) | Software can read as well as clear this bit by writing to the register. The value written to this bit is not important. |",
        "| read/clear by read (rc_r) | Software can read this bit. Reading this bit automatically clears it to 0. Writing this bit has no effect on the bit value. |",
        "| read/set by read (rs_r) | Software can read this bit. Reading this bit automatically sets it to 1. Writing this bit has no effect on the bit value. |",
        "| read/set (rs) | Software can read as well as set this bit. Writing 0 has no effect on the bit value. |",
        "| read/write once (rwo) | Software can only write once to this bit and can also read it at any time. Only a reset can return the bit to its reset value. |",
        "| toggle (t) | The software can toggle the bit by writing 1. Writing 0 has no effect. |",
        "| read-only write trigger (rt_w1) | Software can read this bit. Writing 1 triggers an event but has no effect on the bit value. |",
        "| Reserved (Res.) | Reserved bit, must be kept at reset value. |",
    ]
    table_1 = [
        "| Memory density | Category 2 | Category 3 | Category 4 |",
        "| --- | --- | --- | --- |",
        "| 32 KBytes | STM32G431 | - | - |",
        "| 64 Kbytes | STM32G431 | - | - |",
        "| 128 Kbytes | STM32G431<br>STM32G441 (AES) | STM32G471<br>STM32G473<br>STM32G474<br>STM32G484 (AES) | - |",
        "| 256 Kbytes | - | STM32G471<br>STM32G473<br>STM32G474 | STM32G491 |",
        "| 512 Kbytes | - | STM32G471<br>STM32G473<br>STM32G474<br>STM32G483 (AES)<br>STM32G484 (AES) | STM32G491<br>STM32G4A1 (AES) |",
    ]
    table_2 = [
        "| Feature | STM32G474/<br>STM32G484 | STM32G473/<br>STM32G483 | STM32G471 | STM32G431/<br>STM32G441 | STM32G491/<br>STM32G4A1 |",
        "| --- | --- | --- | --- | --- | --- |",
        "| Flash | 512/256/128K,<br>Dual bank | 512/256/128K,<br>Dual bank | 512/256/128K,<br>Dual bank | 128/64/32K,<br>single bank | 512/256K,<br>single bank |",
        "| SRAM1 | 80K, parity check<br>on the first 32K | 80K, parity check<br>on the first 32K | 80K, parity check<br>on the first 32K | 16K, parity check<br>on the whole SRAM1 | 80K, parity check<br>on the first 32K |",
        "| SRAM2 | 16K, no parity<br>check | 16K, no parity<br>check | 16K, no parity<br>check | 6K, no parity<br>check | 16K, no parity<br>check |",
        "| CCM SRAM | 32K, parity check<br>on the whole CCM SRAM | 32K, parity check<br>on the whole CCM SRAM | 16K, parity check<br>on the whole CCM SRAM | 10K, parity check<br>on the whole CCM SRAM | 16K, parity check<br>on the whole CCM SRAM |",
        "| CRS | Yes | Yes | Yes | Yes | Yes |",
        "| DMA | 2 DMA controllers:<br>DMA1: 8 channels<br>DMA2: 8 channels | 2 DMA controllers:<br>DMA1: 8 channels<br>DMA2: 8 channels | 2 DMA controllers:<br>DMA1: 8 channels<br>DMA2: 8 channels | 2 DMA controllers:<br>DMA1: 6 channels<br>DMA2: 6 channels | 2 DMA controllers:<br>DMA1: 8 channels<br>DMA2: 8 channels |",
        "| DMAMUX | Yes | Yes | Yes | Yes | Yes |",
        "| Cordic | Yes | Yes | Yes | Yes | Yes |",
        "| FMAC | Yes | Yes | Yes | Yes | Yes |",
        "| RNG | Yes | Yes | Yes | Yes | Yes |",
        "| AES | Yes (Note) | Yes (Note) | No | Yes (Note) | Yes (Note) |",
        "| CRC | Yes | Yes | Yes | Yes | Yes |",
        "| FSMC | Yes | Yes | No | No | No |",
        "| QUADSPI | Yes | Yes | Yes | No | Yes |",
        "| ADC | 5 x ADC:<br>ADC1/2 can be used in dual mode<br>ADC3/4 can be used in dual mode<br>ADC5 usable only in single mode | 5 x ADC:<br>ADC1/2 can be used in dual mode<br>ADC3/4 can be used in dual mode<br>ADC5 usable only in single mode | 3 x ADC:<br>ADC1/2 can be used in dual mode<br>ADC3 usable only in single mode | 2 x ADC:<br>ADC1/2 can be used in dual mode | 3 x ADC:<br>ADC1/2 can be used in dual mode<br>ADC3 usable only in single mode |",
        "| DAC | 7 DAC ch:<br>DAC1_CH1/<br>DAC1_CH2/<br>DAC2_CH1: external<br>DAC3_CH1/<br>DAC3/CH2/<br>DAC4_CH1/<br>DAC4_CH2: internal | 7 DAC ch:<br>DAC1_CH1/<br>DAC1_CH2/<br>DAC2_CH1: external<br>DAC3_CH1/<br>DAC3/CH2/<br>DAC4_CH1/<br>DAC4_CH2: internal | 4 DAC ch:<br>DAC1_CH1/<br>DAC1_CH2: external<br>DAC3_CH1/<br>DAC3/CH2: internal | 4 DAC ch:<br>DAC1_CH1/<br>DAC1_CH2: external<br>DAC3_CH1/<br>DAC3/CH2: internal | 4 DAC ch:<br>DAC1_CH1/<br>DAC1_CH2: external<br>DAC3_CH1/<br>DAC3/CH2: internal |",
        "| COMP | 7 (COMP1..7) | 7 (COMP1..7) | 4 (COMP1..4) | 4 (COMP1..4) | 4 (COMP1..4) |",
        "| OPAMP | 6 (OPAMP1..6) | 6 (OPAMP1..6) | 4 (OPAMP1.2,3,6) | 3 (OPAMP1..3) | 4 (OPAMP1.2,3,6) |",
        "| VREFBUF | Yes | Yes | Yes | Yes | Yes |",
        "| HRTIM1 | Yes | No | No | No | No |",
        "| Advanced control timers (TIM1/TIM8/TIM20) | TIM1/8/20 | TIM1/8/20 | TIM1/8/20 | TIM1/8 | TIM1/8/20 |",
        "| General purpose timers (TIM2/TIM3/TIM4/TIM5) | TIM2/3/4/5 | TIM2/3/4/5 | TIM2/3/4 | TIM2/3/4 | TIM2/3/4 |",
        "| General purpose timers (TIM15/TIM16/TIM17) | TIM15/16/17 | TIM15/16/17 | TIM15/16/17 | TIM15/16/17 | TIM15/16/17 |",
        "| Basic timers (TIM6/TIM7) | TIM6/7 | TIM6/7 | TIM6/7 | TIM6/7 | TIM6/7 |",
        "| Low power timer (LPTIM1) | Yes | Yes | Yes | Yes | Yes |",
        "| Infrared interface (IRTIM) | Yes | Yes | Yes | Yes | Yes |",
        "| Independent watchdog (IWDG) | Yes | Yes | Yes | Yes | Yes |",
        "| System window watchdog (WWDG) | Yes | Yes | Yes | Yes | Yes |",
        "| RTC and TAMP | Yes | Yes | Yes | Yes | Yes |",
        "| I2C | 4 x I2C (I2C1..4) | 4 x I2C (I2C1..4) | 4 x I2C (I2C1..4) | 3 x I2C (I2C1..3) | 3 x I2C (I2C1..3) |",
        "| USART/UART | 3 x USART (USART1..3)<br>2 x UART (UART4,5) | 3 x USART (USART1..3)<br>2 x UART (UART4,5) | 3 x USART (USART1..3)<br>2 x UART (UART4,5) | 3 x USART (USART1..3)<br>1 x UART (UART4) | 3 x USART (USART1..3)<br>2 x UART (UART4,5) |",
        "| LPUART | 1 x LPUART | 1 x LPUART | 1 x LPUART | 1 x LPUART | 1 x LPUART |",
        "| SPI/I2S | 4 x SPI/2 x I2S<br>(SPI1..4 - I2S2,3) | 4 x SPI/2 x I2S<br>(SPI1..4 - I2S2,3) | 4 x SPI/2 x I2S<br>(SPI1..4 - I2S2,3) | 3 x SPI/2 x I2S<br>(SPI1..3 - I2S2,3) | 3 x SPI/2 x I2S<br>(SPI1..3 - I2S2,3) |",
        "| SAI | 1 x SAI | 1 x SAI | 1 x SAI | 1 x SAI | 1 x SAI |",
        "| FDCAN | 3 x FDCAN<br>(FDCAN1..3) | 3 x FDCAN<br>(FDCAN1..3) | 2 x FDCAN<br>(FDCAN1,2) | 1 x FDCAN<br>(FDCAN1) | 2 x FDCAN<br>(FDCAN1,2) |",
        "| USB device | 1 x USB device | 1 x USB device | 1 x USB device | 1 x USB device | 1 x USB device |",
        "| UCPD1 | 1 x UCPD | 1 x UCPD | 1 x UCPD | 1 x UCPD | 1 x UCPD |",
    ]
    replacements = {
        "The following abbreviations(b) are used in register descriptions:": (
            "a. Arm and TrustZone are registered trademarks of Arm Limited",
            table_abbreviations,
            None,
        ),
        "**Table 1. STM32G4 series memory density**": ("### 1.6 Availability of peripherals", table_1, None),
        "**Table 2. Product specific features**": (
            "## 2 System and memory overview",
            table_2,
            "> **Note:** The AES is available only on STM32G483xx, STM32G484xx, STM32G441x and STM32G4A1 devices.",
        ),
    }
    repaired: list[str] = []
    i = 0
    while i < len(lines):
        replacement = replacements.get(lines[i])
        if replacement is None:
            repaired.append(lines[i])
            i += 1
            continue
        end_marker, table, note = replacement
        end = i + 1
        while end < len(lines) and not lines[end].startswith(end_marker):
            end += 1
        if end == len(lines):
            repaired.append(lines[i])
            i += 1
            continue
        repaired.extend([lines[i], "", *table])
        if note:
            repaired.extend(["", note])
        repaired.append("")
        i = end
    return repaired


def link_section_references(text: str, section_numbers: dict[str, str]) -> str:
    """Turn prose references into links to the corresponding section."""
    # Positioned text occasionally captures a fuller heading than flow XHTML.
    # Prefer the headings actually emitted into the Markdown so every target
    # matches the renderer-generated fragment exactly.
    slug_counts: dict[str, int] = {}
    for match in re.finditer(r"^#{1,6}\s+(\d+(?:\.\d+)*)(?=\s)[^\n]*", text, re.M):
        number = match.group(1)
        heading = match.group(0).split(maxsplit=1)[1]
        base_slug = slug_for(heading, heading_number(heading), 0)
        occurrence = slug_counts.get(base_slug, 0)
        slug_counts[base_slug] = occurrence + 1
        section_numbers[number] = base_slug if occurrence == 0 else f"{base_slug}-{occurrence}"

    pattern = re.compile(r"\bSection\s+(\d+(?:\.\d+)*)\b", re.I)

    def replace(match: re.Match[str]) -> str:
        number = match.group(1)
        if number not in section_numbers:
            return match.group(0)
        # Numbered headings begin with the section number. Resolve the full
        # destination from the heading index rather than relying on raw HTML
        # anchors or a renderer-specific shorthand.
        target = section_numbers[number]
        return f"[{match.group(0)}](#{target})"

    linked: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence:
            line = pattern.sub(replace, line)
        linked.append(line)
    return "\n".join(linked)


def format_paragraph(text: str, allow_caption: bool = True) -> str:
    if not text:
        return ""
    # Replace references to the original pagination before applying list,
    # metadata, or callout formatting. Section references are linked in the
    # final document, so the remaining prose stays self-contained.
    text = re.sub(
        r"(?:\s+|^)on page(?:s)?\s+\d+(?:\s*[-–]\s*\d+)?(?:\.)?",
        " ",
        text,
        flags=re.I,
    )
    text = normalize_text(text)
    if not text or text in {".", ","}:
        return ""
    if text.startswith("•"):
        return "-" + text[1:]
    if text.startswith("–") or text.startswith("—"):
        return "  -" + text[1:]
    if re.match(r"^(Address offset|Reset value|Access):", text):
        key, value = text.split(":", 1)
        return f"- **{key}:** {value.strip()}"

    # The debug chapter uses ``Bit n = NAME: description`` (and occasionally
    # ``=`` or ``.`` between the name and description). Parse that form before
    # the usual ``Bit n NAME: description`` form so an embedded range such as
    # ``bit1:0`` cannot be mistaken for the field-name delimiter.
    assigned_bit_field = re.match(
        r"^(Bits? \d+(?::\d+)?)\s*=\s*([A-Za-z][A-Za-z0-9_\[\]:-]*)"
        r"\s*(?:=|:|\.)\s*(.*)$",
        text,
    )
    if assigned_bit_field:
        bit_range, name, description = assigned_bit_field.groups()
        return f"**{bit_range} — `{name}`:** {description}"
    bit_field = re.match(
        r"^(Bits? \d+(?::\d+)?)\s+(.+?):(?:\s+|$)(.*)$",
        text,
    )
    if bit_field:
        bit_range, name, description = bit_field.groups()
        return f"**{bit_range} — `{name.strip()}`:** {description}"
    bare_bit_field = re.fullmatch(
        r"(Bits? \d+(?::\d+)?)\s+([A-Za-z][A-Za-z0-9_]*\[\d+(?::\d+)?\])",
        text,
    )
    if bare_bit_field:
        bit_range, name = bare_bit_field.groups()
        return f"**{bit_range} — `{name}`:**"
    reserved = re.match(
        r"^(Bits? \d+(?::\d+)?)\s+Reserved,?\s*(?:must be)?\s*(.*)$",
        text,
        re.I,
    )
    if reserved:
        bit_range, description = reserved.groups()
        suffix = f" {description}" if description else ""
        return f"**{bit_range} — Reserved:**{suffix}"
    value_description = re.match(r"^([01Xx]{1,8}):\s+(.+)$", text)
    if value_description:
        value, description = value_description.groups()
        return f"- `{value}`: {description}"

    if allow_caption and re.match(r"^(Table|Figure)\s+\d+\.", text):
        return f"**{text}**"
    if text.startswith(("Note:", "Warning:", "Caution:")):
        return as_blockquote(text)
    # Cross-references to the original pagination do not belong in a
    # standalone manual; section names remain useful and searchable.
    return re.sub(r"\s+on page(?:s)?\s+\d+(?:\s*[-–]\s*\d+)?", "", text, flags=re.I)


def page_items(blocks: list[TextBlock], page: int) -> list[str]:
    rows = make_visual_rows(blocks, page)
    items: list[str] = []
    list_parent_open = False
    i = 0
    while i < len(rows):
        row = rows[i]
        if is_heading_row(row, page):
            parts = [row.space_text]
            j = i + 1
            # Chapter/section titles can wrap onto several positioned rows.
            while j < len(rows):
                nxt = rows[j]
                gap = nxt.top - rows[j - 1].top
                if (
                    nxt.size >= row.size - 0.6
                    and nxt.bold
                    and gap <= row.line_height + 3.0
                    and nxt.left >= row.left - 2.0
                    and not heading_number(nxt.space_text)
                ):
                    parts.append(nxt.space_text)
                    j += 1
                else:
                    break
            text = clean_heading(" ".join(parts))
            nums = heading_number(text)
            if page == 1:
                level = 2
            elif nums:
                level = heading_level("h2" if len(nums) == 1 else "h3", text)
            elif page >= 2134 and re.fullmatch(r"[A-Z]", text):
                level = 3
            else:
                level = 3
            items.append(f"@@HEADING@@{level}@@{text}@@{slug_for(text, nums, page)}")
            list_parent_open = False
            i = j
            continue

        if is_minor_heading_row(row, page):
            parts = [row.space_text]
            j = i + 1
            # Minor headings can wrap onto a second bold PDF row.
            while j < len(rows):
                nxt = rows[j]
                gap = nxt.top - rows[j - 1].top
                if (
                    len(nxt.blocks) == 1
                    and nxt.bold
                    and abs(nxt.size - row.size) <= 0.6
                    and abs(nxt.left - row.left) <= 2.0
                    and gap <= row.line_height + 3.0
                    and not is_heading_row(nxt, page)
                ):
                    parts.append(nxt.space_text)
                    j += 1
                else:
                    break
            text = clean_heading(" ".join(parts)).rstrip(":")
            items.append(f"@@MINOR@@{text}")
            list_parent_open = False
            i = j
            continue

        # Merge wrapped body prose before formatting it.
        merged = row
        j = i + 1
        while j < len(rows) and can_merge_rows(merged, rows[j]):
            merged_text = normalize_text(merged.space_text + " " + rows[j].space_text)
            merged = VisualRow(
                # Keep the end of the merged span so a paragraph can contain
                # more than two wrapped PDF lines. Using the first line's
                # position here made the third line look too far away and
                # prematurely stopped the merge.
                top=rows[j].top,
                blocks=[
                    TextBlock(
                        top=rows[j].top,
                        left=merged.left,
                        line_height=merged.line_height,
                        size=merged.size,
                        bold=merged.bold,
                        text=merged_text,
                    )
                ],
                text=merged_text,
                space_text=merged_text,
                size=merged.size,
                left=merged.left,
                line_height=merged.line_height,
                bold=merged.bold,
            )
            j += 1
        text = merged.text or merged.space_text
        formatted = format_paragraph(text, allow_caption=merged.bold)
        if formatted.startswith("  -"):
            if not list_parent_open:
                formatted = formatted.lstrip()
        elif re.match(r"^(?:- |\d+\.\s)", formatted):
            list_parent_open = True
        else:
            list_parent_open = False
        items.append(formatted)
        i = j
    return [item for item in items if item]


def figure_specs_from_positioned(positioned: dict[int, list[TextBlock]]) -> list[FigureSpec]:
    """Locate every numbered figure caption in positioned PDF text."""
    occurrences: dict[int, int] = {}
    specs: list[FigureSpec] = []
    for page, blocks in sorted(positioned.items()):
        if page < 74 or page == TOTAL_PAGES:
            continue
        for block in sorted(blocks, key=lambda value: (value.top, value.left)):
            match = re.match(r"^Figure\s+(\d+)\.\s*(.*)$", block.text)
            # Plain-text references such as a standalone blue "Figure 97."
            # are not captions. Actual ST captions are bold.
            if not match or not block.bold:
                continue
            number = int(match.group(1))
            occurrences[number] = occurrences.get(number, 0) + 1
            specs.append(
                FigureSpec(
                    page=page,
                    number=number,
                    occurrence=occurrences[number],
                    top=block.top,
                    line_height=block.line_height,
                    title=match.group(2),
                )
            )
    return specs


def render_figures(pdf: Path, specs: list[FigureSpec], image_dir: Path, dpi: int = 144) -> None:
    """Render and crop the actual artwork for each numbered figure.

    RM0440 diagrams are mostly vector graphics rather than embedded bitmap
    objects. Pages are therefore rasterized once, then each artwork region is
    cropped from immediately below its caption to the first substantial white
    gap. Running headers, captions, body text, and page footers are excluded.
    """
    if not specs:
        return
    try:
        import numpy as np
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("Figure cropping requires Pillow and NumPy") from exc

    image_dir.mkdir(parents=True, exist_ok=True)
    for old in image_dir.glob("page-*.png"):
        old.unlink()
    for old in image_dir.glob("figure-*.png"):
        old.unlink()

    by_page: dict[int, list[FigureSpec]] = {}
    for spec in specs:
        by_page.setdefault(spec.page, []).append(spec)

    scale = dpi / 72.0
    with tempfile.TemporaryDirectory(prefix="rm0440-figure-pages-") as temp_name:
        temp_dir = Path(temp_name)
        page_list = ",".join(str(page) for page in sorted(by_page))
        subprocess.run(
            [
                "mutool", "draw", "-q", "-r", str(dpi), "-F", "png",
                "-o", str(temp_dir / "page-%04d.png"), str(pdf), page_list,
            ],
            check=True,
        )

        for page, page_specs in by_page.items():
            with Image.open(temp_dir / f"page-{page:04d}.png") as source:
                image = source.convert("RGB")
            pixels = np.asarray(image)
            ink = np.min(pixels, axis=2) < 248
            side_margin = max(1, int(45 * scale))
            page_bottom = min(image.height, int(728 * scale))
            ordered_specs = sorted(page_specs, key=lambda value: value.top)

            for index, spec in enumerate(ordered_specs):
                start = max(0, int((spec.top + spec.line_height + 2) * scale))
                if index + 1 < len(ordered_specs):
                    limit = min(page_bottom, int((ordered_specs[index + 1].top - 2) * scale))
                else:
                    limit = page_bottom
                if limit <= start:
                    continue

                row_has_ink = ink[start:limit, side_margin : image.width - side_margin].any(axis=1)
                populated = np.flatnonzero(row_has_ink)
                if not len(populated):
                    continue
                first = int(populated[0])
                last = int(populated[-1])
                gap_limit = max(8, int(12 * scale))
                previous = first
                for row in populated[1:]:
                    row = int(row)
                    if row - previous > gap_limit:
                        last = previous
                        break
                    previous = row

                y0 = start + first
                y1 = start + last + 1
                region_ink = ink[y0:y1, side_margin : image.width - side_margin]
                ys, xs = np.nonzero(region_ink)
                if not len(xs):
                    continue
                padding = max(4, int(4 * scale))
                x0 = max(0, side_margin + int(xs.min()) - padding)
                x1 = min(image.width, side_margin + int(xs.max()) + 1 + padding)
                # Never pad upward into the caption that defines this crop.
                y0 = max(start, y0 - padding)
                y1 = min(image.height, y1 + padding)
                image.crop((x0, y0, x1, y1)).save(image_dir / spec.filename, optimize=True)


def extract_sources(pdf: Path, out: Path, split_chapters: bool = True) -> None:
    image_dir = out.with_name(out.stem + "_figures")
    with tempfile.NamedTemporaryFile(suffix=".xhtml") as xhtml_tmp, tempfile.NamedTemporaryFile(
        suffix=".html"
    ) as html_tmp:
        subprocess.run(
            ["mutool", "draw", "-q", "-F", "xhtml", "-o", xhtml_tmp.name, str(pdf), "1-2140"],
            check=True,
        )
        subprocess.run(
            ["mutool", "draw", "-q", "-F", "html", "-o", html_tmp.name, str(pdf), "1-2140"],
            check=True,
        )
        convert_xhtml(
            Path(xhtml_tmp.name),
            out,
            Path(html_tmp.name),
            pdf=pdf,
            image_dir=image_dir,
            split_chapters=split_chapters,
        )


def convert_xhtml(
    xhtml_path: Path,
    out: Path,
    html_path: Path | None = None,
    pdf: Path | None = None,
    image_dir: Path | None = None,
    split_chapters: bool = True,
) -> None:
    root = ET.parse(xhtml_path).getroot()
    pages: list[tuple[int, ET.Element]] = []
    for div in root.findall(f".//{NS}div"):
        match = re.fullmatch(r"page(\d+)", div.attrib.get("id", ""))
        if match:
            pages.append((int(match.group(1)), div))
    pages.sort()
    if not pages:
        raise RuntimeError("No MuPDF XHTML pages found")

    positioned = parse_positioned_html(html_path) if html_path else {}
    figure_specs = figure_specs_from_positioned(positioned)
    if pdf is not None and image_dir is not None:
        render_figures(pdf, figure_specs, image_dir)
    figures_by_page: dict[int, list[FigureSpec]] = {}
    for spec in figure_specs:
        figures_by_page.setdefault(spec.page, []).append(spec)

    # Collect semantic headings from flow XHTML for the generated navigation.
    headings: list[tuple[int, int, str, str, tuple[int, ...] | None]] = []
    for page, div in pages:
        if page < 74 or page == TOTAL_PAGES:
            continue
        for elem in list(div):
            name = tag_name(elem.tag)
            if name not in ("h2", "h3"):
                continue
            text = clean_heading(plain_text(elem))
            if not text or text in {"Contents", "List of tables", "List of figures"}:
                continue
            nums = heading_number(text)
            # A few diagram labels are emitted as h3 elements by MuPDF (for
            # example, ``2 ----- 4``). Real numbered h3 headings always have
            # at least a section component and belong to this manual's 1–50
            # chapter range.
            if name == "h3" and nums and (len(nums) < 2 or nums[0] > 50):
                continue
            headings.append((page, heading_level(name, text), text, slug_for(text, nums, page), nums))

    # GitHub-style renderers append -1, -2, ... to duplicate heading slugs.
    # Mirror that behavior in generated navigation links.
    slug_counts: dict[str, int] = {}
    unique_headings: list[tuple[int, int, str, str, tuple[int, ...] | None]] = []
    for page, level, text, base_slug, nums in headings:
        occurrence = slug_counts.get(base_slug, 0)
        slug_counts[base_slug] = occurrence + 1
        slug = base_slug if occurrence == 0 else f"{base_slug}-{occurrence}"
        unique_headings.append((page, level, text, slug, nums))
    headings = unique_headings

    chapters = [
        h for h in headings if h[1] == 2 and h[4] and len(h[4]) == 1
    ]
    section_numbers = {
        ".".join(str(part) for part in nums): slug
        for _page, _level, _text, slug, nums in headings
        if nums
    }
    lines: list[str] = [
        "# STM32G4 series advanced Arm®-based 32-bit MCUs — Reference manual",
        "",
        "> **Publisher:** STMicroelectronics  ",
        "> **Revision:** 9  ",
        "> **Date:** March 2025  ",
        "> **Source:** [STM32G4_RM0440.pdf](STM32G4_RM0440.pdf)  ",
        "> **Figures:** Each numbered figure is cropped to its actual artwork in the adjacent `*_figures/` directory.  ",
        "> **Formatting:** Registers and extracted tables use native Markdown tables optimized for terminal rendering.  ",
        "",
        "This standalone document provides complete information on the memory and peripherals of STM32G4 series microcontrollers. Figure captions and extracted labels remain searchable, and the associated artwork is preserved as linked images.",
        "",
        "## Contents",
        "",
    ]
    for _page, _level, text, slug, _nums in chapters:
        lines.append(f"- [{text}](#{slug})")
    lines.extend(["", "## Section index", ""])
    for _page, _level, text, slug, nums in headings:
        if nums and len(nums) <= 2:
            indent = "  " * max(0, len(nums) - 1)
            lines.append(f"{indent}- [{text}](#{slug})")
    lines.extend(["", "---", ""])

    # Emit the technical content. The generated contents/list pages and the
    # original pagination-only index are replaced by the navigation above.
    current_heading_level = 1
    for page, div in pages:
        if 2 <= page <= 73 or 2134 <= page <= 2139:
            continue
        if page in positioned:
            items = page_items(positioned[page], page)
        else:
            # Fallback for callers supplying only XHTML: retain the flow text.
            items = []
            for elem in list(div):
                name = tag_name(elem.tag)
                raw = plain_text(elem)
                if name in ("h2", "h3"):
                    text = clean_heading(raw)
                    if text and not (page == 1 and text.startswith("RM0440 Reference manual")):
                        nums = heading_number(text)
                        items.append(
                            f"@@HEADING@@{heading_level(name, text)}@@{text}@@{slug_for(text, nums, page)}"
                        )
                elif name == "p" and raw and not re.search(r"\b\d+/2140\b", raw):
                    items.append(format_paragraph(rendered_text(elem)))

        if page == 1:
            # The positioned cover title is intentionally omitted; all
            # introduction text begins below it.
            pass
        if not items:
            continue
        lines.append("")
        remaining_figures = list(figures_by_page.get(page, []))
        for item in items:
            if item.startswith("@@HEADING@@"):
                _, level, text, slug = item.split("@@", 4)[1:]
                current_heading_level = int(level)
                lines.extend([f"{'#' * current_heading_level} {text}", ""])
            elif item.startswith("@@MINOR@@"):
                text = item.removeprefix("@@MINOR@@")
                level = min(current_heading_level + 1, 6)
                lines.extend([f"{'#' * level} {text}", ""])
            else:
                lines.extend([item, ""])
                figure_match = re.match(r"^\*\*Figure\s+(\d+)\.\s*(.*?)\*\*$", item)
                if figure_match and image_dir is not None:
                    number = int(figure_match.group(1))
                    spec_index = next(
                        (index for index, spec in enumerate(remaining_figures) if spec.number == number),
                        None,
                    )
                    if spec_index is not None:
                        spec = remaining_figures.pop(spec_index)
                        figure_title = figure_match.group(2).replace("[", r"\[").replace("]", r"\]")
                        alt_text = f"Figure {number}: {figure_title}"
                        rel_image = f"{image_dir.name}/{spec.filename}"
                        lines.extend([f"![{alt_text}]({rel_image})", ""])

    # Collapse excessive blank lines introduced by independent PDF blocks,
    # then make table and diagram fragments render intentionally.
    compact: list[str] = []
    blank = False
    for line in lines:
        if line == "":
            if not blank:
                compact.append(line)
            blank = True
        else:
            compact.append(line if line.endswith("  ") else line.rstrip())
            blank = False
    compact = render_layout_blocks(compact)
    compact = repair_known_tables(compact)
    compact = wrap_markdown_lines(compact)
    compact = normalize_markdown_blocks(compact)
    standalone = "\n".join(compact).rstrip() + "\n"
    standalone = link_section_references(standalone, section_numbers)
    # PDF line wrapping can split a long URL immediately after a hyphen. Join
    # that unambiguous continuation before converting URLs into Markdown links.
    standalone = re.sub(
        r"(https?://[^\s<>()]+)-\n+(?=[A-Za-z0-9])",
        r"\1-",
        standalone,
    )
    # Known table repairs use ``<br>`` only as a source-level cell separator.
    # Replace it before escaping angle brackets; doing this afterward turned
    # ``<br>`` into the renderer-visible artifact ``\;``.
    standalone = standalone.replace("<br>", "; ")
    standalone = sanitize_inline_markdown(standalone).rstrip() + "\n"
    standalone = replace_register_maps(standalone)
    standalone = replace_register_layouts(standalone)
    standalone = replace_text_layouts(standalone)
    if split_chapters:
        write_split_manual(standalone, out)
    else:
        out.write_text(standalone, encoding="utf-8")


def replace_register_layouts(markdown: str) -> str:
    """Replace flattened register grids with semantic bit-field summaries.

    MuPDF does not expose the merged cells that associate a field name and
    access mode with a bit range. Presenting those independent rows as a table
    looks precise but is misleading. The prose immediately following a real
    register grid contains explicit ``Bits n:m — FIELD`` descriptions, which
    are reliable enough to build a useful overview. Grid-like diagrams without
    such descriptions remain verbatim text layouts instead of being mislabeled
    as registers.
    """
    lines = markdown.splitlines()
    converted: list[str] = []
    i = 0
    field_pattern = re.compile(
        r"^\*\*(Bits? \d+(?::\d+)?) — "
        r"(?:`([^`]*)`|(Reserved)):\*\*\s*(.*)$"
    )

    def register_layout(block: list[str]) -> bool:
        for line in block:
            if not is_pipe_row(line):
                continue
            cells = split_table_cells(line)
            numbers = sum(bool(re.fullmatch(r"\d{1,2}", cell)) for cell in cells)
            if len(cells) >= 8 and numbers >= 8:
                return True
        return False

    def described_fields(start: int) -> list[tuple[int, int, str, str]]:
        fields: list[tuple[int, int, str, str]] = []
        j = start
        while j < len(lines):
            line = lines[j]
            if (
                re.match(r"^#{1,6}\s", line)
                or line == "```text"
                or line.startswith("- **Address offset:**")
                or line.startswith("Flash memory address:")
            ):
                break
            match = field_pattern.match(line)
            if match:
                bits, name, reserved, description = match.groups()
                bit_text = bits.removeprefix("Bits ").removeprefix("Bit ")
                high_text, _, low_text = bit_text.partition(":")
                high = int(high_text)
                low = int(low_text or high_text)
                fields.append((max(high, low), min(high, low), name or reserved, description or "—"))
            j += 1
        return fields

    def layout_bits(block: list[str]) -> list[int]:
        bits: list[int] = []
        for line in block:
            if not is_pipe_row(line):
                continue
            cells = split_table_cells(line)
            if len(cells) >= 8 and all(re.fullmatch(r"\d{1,2}", cell) for cell in cells):
                bits.extend(int(cell) for cell in cells)
        return list(dict.fromkeys(bits))

    def layout_access(block: list[str]) -> list[str]:
        access_values = {
            "r", "w", "rw", "r/w", "ro", "wo", "rc_w0", "rc_w1",
            "rc_w", "rc_r", "rs_r", "rs", "rwo", "rt_w1", "t",
        }
        access: list[str] = []
        for line in block:
            cells = split_table_cells(line) if is_pipe_row(line) else [line.strip()]
            lowered = [cell.lower() for cell in cells if cell]
            if lowered and all(cell in access_values for cell in lowered):
                access.extend(cells)
        return access

    def table_cell(value: str) -> str:
        return re.sub(r"(?<!\\)\|", r"\\|", value).strip()

    def expanded_name(name: str, high: int, low: int, bit: int) -> str:
        if name == "Reserved":
            return "Reserved"
        indexed = re.fullmatch(r"(.+)\[(\d+):(\d+)\]", name)
        if indexed and high - low == abs(int(indexed.group(2)) - int(indexed.group(3))):
            field_high = max(int(indexed.group(2)), int(indexed.group(3)))
            field_low = min(int(indexed.group(2)), int(indexed.group(3)))
            index = field_low + (bit - low)
            return f"{indexed.group(1)}[{index}]"
        return name

    def bit_table(
        bits: list[int],
        fields: list[tuple[int, int, str, str]],
        access: list[str],
    ) -> list[str] | None:
        mapped: dict[int, tuple[str, str, bool]] = {}
        for high, low, name, description in fields:
            if any(bit in mapped for bit in range(low, high + 1)):
                return None
            for bit in range(low, high + 1):
                mapped[bit] = (expanded_name(name, high, low, bit), description, bit == high)

        named_bits = [bit for bit in bits if bit in mapped and mapped[bit][0] != "Reserved"]
        access_by_bit: dict[int, str] = {}
        if len(access) == len(bits):
            access_by_bit.update(zip(bits, access))
        elif len(access) == len(named_bits):
            access_by_bit.update(zip(named_bits, access))
        elif access and len(set(access)) == 1:
            access_by_bit.update((bit, access[0]) for bit in named_bits)

        table = [
            "**Register bit layout**",
            "",
            "| Bit | Field | Access | Summary |",
            "| ---: | --- | :---: | --- |",
        ]
        for bit in bits:
            if bit not in mapped:
                table.append(f"| {bit} | — | — | Not specified in extracted bit-field text. |")
                continue
            name, description, first = mapped[bit]
            field = name if name == "Reserved" else f"`{table_cell(name)}`"
            summary = table_cell(description) if first else "↳"
            table.append(f"| {bit} | {field} | {access_by_bit.get(bit, '—')} | {summary} |")
        return table

    while i < len(lines):
        if lines[i] != "```text":
            converted.append(lines[i])
            i += 1
            continue
        end = i + 1
        while end < len(lines) and lines[end] != "```":
            end += 1
        block = lines[i + 1 : end]
        fields = described_fields(end + 1) if end < len(lines) and register_layout(block) else []
        table = bit_table(layout_bits(block), fields, layout_access(block)) if fields else None
        if table:
            converted.extend(table)
        else:
            converted.extend(lines[i : min(end + 1, len(lines))])
        i = end + 1

    return "\n".join(converted).rstrip() + "\n"


def replace_text_layouts(markdown: str) -> str:
    """Replace remaining text fences with native Markdown structures.

    Numbered figures already have a source-page image, so duplicate extracted
    diagram labels are omitted. Ragged PDF tables become padded native tables;
    very wide tables use a compact row-per-source-row representation. Other
    formula/layout fragments become blockquotes with explicit line breaks.
    """
    lines = markdown.splitlines()
    converted: list[str] = []
    context = ""
    i = 0

    def safe(value: str) -> str:
        value = value.strip().replace("`", "'")
        value = re.sub(r"(?<!\\)\|", r"\\|", value)
        return value

    def cells(line: str) -> list[str]:
        return split_table_cells(line) if is_pipe_row(line) else [line.strip()]

    def native_table(block: list[str]) -> list[str]:
        rows = [cells(line) for line in block if line.strip()]
        width = max((len(row) for row in rows), default=1)
        if width <= 12:
            header = ["Source row", *(f"Column {index}" for index in range(1, width + 1))]
            table = [
                "| " + " | ".join(header) + " |",
                "| " + " | ".join(["---:", *("---" for _ in range(width))]) + " |",
            ]
            for number, row in enumerate(rows, 1):
                padded = [*row, *("" for _ in range(width - len(row)))]
                rendered = [f"`{safe(value)}`" if value else "" for value in padded]
                table.append(f"| {number} | " + " | ".join(rendered) + " |")
            return table

        table = ["| Source row | Extracted cells |", "| ---: | --- |"]
        for number, row in enumerate(rows, 1):
            rendered = " · ".join(f"`{safe(value)}`" for value in row if value)
            table.append(f"| {number} | {rendered or '—'} |")
        return table

    def native_quote(block: list[str]) -> list[str]:
        quote = ["> **Extracted layout**", ">"]
        for line in block:
            values = cells(line) if line.strip() else []
            rendered = " · ".join(f"`{safe(value)}`" for value in values if value)
            quote.append(f"> {rendered}  " if rendered else ">")
        return quote

    while i < len(lines):
        line = lines[i]
        if re.match(r"^(?:\*\*(?:Table|Figure)|!\[|#{1,6}\s)", line):
            context = line
        if line != "```text":
            converted.append(line)
            i += 1
            continue

        end = i + 1
        while end < len(lines) and lines[end] != "```":
            end += 1
        block = lines[i + 1 : end]
        if context.startswith(("**Figure", "![")):
            # The linked source-page render is the authoritative diagram.
            pass
        elif context.startswith("**Table"):
            converted.extend(native_table(block))
        else:
            converted.extend(native_quote(block))
        i = min(end + 1, len(lines))

    return "\n".join(converted).rstrip() + "\n"


def replace_register_maps(markdown: str) -> str:
    """Replace PDF bit-grid register maps with compact native Markdown tables.

    The source maps rely on merged cells, which Markdown cannot represent and
    MuPDF flattens into misleading text grids. Register headings and metadata
    provide a more reliable summary: one row per register with its offset,
    reset value, and access mode. Detailed bit descriptions remain immediately
    above each summary.
    """
    lines = markdown.splitlines()
    result: list[str] = []
    records: list[dict[str, str]] = []
    current_record: dict[str, str] | None = None
    heading_pattern = re.compile(r"^(#{1,6})\s+(.+)$")

    def cell(text: str | None) -> str:
        if not text:
            return "—"
        return text.replace("|", r"\|").strip()

    def fallback_records(section: list[str]) -> list[dict[str, str]]:
        """Recover simple map rows when a register heading was not extracted."""
        recovered: list[dict[str, str]] = []
        by_name: dict[str, dict[str, str]] = {}
        current: dict[str, str] | None = None
        for line in section:
            # COMP is the known manual section whose 24.6.1 heading is exposed
            # as a layout row rather than a semantic heading.
            for name in re.findall(r"\bCOMP_C\dCSR\b", line):
                current = by_name.get(name)
                if current is None:
                    current = {"name": name}
                    by_name[name] = current
                    recovered.append(current)
            offset = re.search(r"\b0x[0-9A-Fa-f]{2,8}\b", line)
            if current is not None and offset and "offset" not in current:
                current["offset"] = offset.group(0)
            if current is not None and "Reset value" in line:
                values = split_table_cells(line)
                values = [value for value in values if value != "Reset value"]
                if values:
                    current["reset"] = (
                        "0x0000 0000" if set(values) == {"0"} else " ".join(values)
                    )
        return recovered

    def summary_table(items: list[dict[str, str]]) -> list[str]:
        has_access = any(item.get("access") for item in items)
        table = ["**Register summary**", ""]
        if has_access:
            table.extend(
                [
                    "| Offset | Register | Reset value | Access |",
                    "| --- | --- | --- | --- |",
                ]
            )
        else:
            table.extend(
                [
                    "| Offset | Register | Reset value |",
                    "| --- | --- | --- |",
                ]
            )
        for item in items:
            name = cell(item.get("name"))
            row = f"| {cell(item.get('offset'))} | `{name}` | {cell(item.get('reset'))} |"
            if has_access:
                row += f" {cell(item.get('access'))} |"
            table.append(row)
        return table

    i = 0
    while i < len(lines):
        heading = heading_pattern.match(lines[i])
        if heading and "register map" in heading.group(2).lower():
            map_level = len(heading.group(1))
            end = i + 1
            while end < len(lines):
                candidate = heading_pattern.match(lines[end])
                if candidate and len(candidate.group(1)) <= map_level:
                    break
                end += 1
            section = lines[i + 1 : end]
            map_records = [record.copy() for record in records]
            if not map_records:
                map_records = fallback_records(section)

            result.append(lines[i])
            emitted = False
            in_fence = False
            for line in section:
                if line.startswith("```"):
                    in_fence = not in_fence
                    if not emitted and map_records:
                        result.extend(["", *summary_table(map_records), ""])
                        emitted = True
                    continue
                if in_fence:
                    continue
                if re.match(r"^\*\*Table\s+\d+\..*register map", line, re.I):
                    if not emitted and map_records:
                        result.extend(["", *summary_table(map_records), ""])
                        emitted = True
                    continue
                result.append(line)
            records = []
            current_record = None
            i = end
            continue

        if heading:
            if len(heading.group(1)) == 2:
                records = []
                current_record = None
            symbols = [
                symbol
                for symbol in re.findall(r"\(([A-Za-z0-9_]+)\)", heading.group(2))
                if "_" in symbol and re.match(r"^[A-Z][A-Za-z0-9_]+$", symbol)
            ]
            if symbols:
                current_record = {"name": symbols[0]}
                records.append(current_record)
        elif current_record is not None:
            metadata = re.match(
                r"^- \*\*(Address offset|Reset value|Access):\*\*\s*(.*)$",
                lines[i],
            )
            if metadata:
                key = {
                    "Address offset": "offset",
                    "Reset value": "reset",
                    "Access": "access",
                }[metadata.group(1)]
                value = metadata.group(2).strip()
                if key in current_record and value != current_record[key]:
                    current_record[key] += "; " + value
                else:
                    current_record[key] = value

        result.append(lines[i])
        i += 1

    compact: list[str] = []
    for line in result:
        if line or not compact or compact[-1]:
            compact.append(line)
    return "\n".join(compact).rstrip() + "\n"


def write_split_manual(markdown: str, out: Path) -> None:
    """Write a lightweight index and one render-friendly file per chapter."""
    lines = markdown.splitlines()
    chapter_starts: list[tuple[int, int]] = []
    for index, line in enumerate(lines):
        match = re.match(r"^## (\d+)\s+", line)
        if match:
            chapter_starts.append((index, int(match.group(1))))
    if not chapter_starts:
        raise RuntimeError("No numbered chapter headings found in generated Markdown")

    chapter_dir = out.with_name(out.stem + "_chapters")
    chapter_dir.mkdir(parents=True, exist_ok=True)
    chapter_files = {
        chapter: f"chapter-{chapter:02d}.md" for _index, chapter in chapter_starts
    }

    # Match each renderer-generated heading fragment to the chapter containing
    # it, including GitHub's numeric suffix for duplicate heading slugs.
    anchor_targets: dict[str, tuple[int | None, str]] = {}
    slug_counts: dict[str, int] = {}
    local_slug_counts: dict[int | None, dict[str, int]] = {}
    current_chapter: int | None = None
    for line in lines:
        chapter_match = re.match(r"^## (\d+)\s+", line)
        if chapter_match:
            current_chapter = int(chapter_match.group(1))
        heading_match = re.match(r"^#{1,6}\s+(.+)$", line)
        if not heading_match:
            continue
        heading = heading_match.group(1)
        base_slug = slug_for(heading, heading_number(heading), 0)
        occurrence = slug_counts.get(base_slug, 0)
        slug_counts[base_slug] = occurrence + 1
        anchor = base_slug if occurrence == 0 else f"{base_slug}-{occurrence}"

        file_counts = local_slug_counts.setdefault(current_chapter, {})
        local_occurrence = file_counts.get(base_slug, 0)
        file_counts[base_slug] = local_occurrence + 1
        local_anchor = base_slug if local_occurrence == 0 else f"{base_slug}-{local_occurrence}"
        anchor_targets[anchor] = (current_chapter, local_anchor)

    def rewrite_links(text: str, source_chapter: int | None) -> str:
        def replace(match: re.Match[str]) -> str:
            anchor = match.group(1)
            target_chapter, target_anchor = anchor_targets.get(anchor, (None, anchor))
            if target_chapter is None:
                destination = (
                    f"#{target_anchor}"
                    if source_chapter is None
                    else f"../{out.name}#{target_anchor}"
                )
            elif target_chapter == source_chapter:
                destination = f"#{target_anchor}"
            elif source_chapter is None:
                destination = (
                    f"{chapter_dir.name}/{chapter_files[target_chapter]}#{target_anchor}"
                )
            else:
                destination = f"{chapter_files[target_chapter]}#{target_anchor}"
            return f"]({destination})"

        return re.sub(r"(?<!\!)\]\(#([^)]+)\)", replace, text)

    first_chapter = chapter_starts[0][0]
    index_text = rewrite_links("\n".join(lines[:first_chapter]).rstrip(), None)
    index_text += (
        "\n\n> **Performance:** The technical content is split into chapter files so large-file "
        "Markdown renderers only process the chapter currently open.\n"
    )
    out.write_text(index_text, encoding="utf-8")

    for position, (start, chapter) in enumerate(chapter_starts):
        end = chapter_starts[position + 1][0] if position + 1 < len(chapter_starts) else len(lines)
        body = "\n".join(lines[start:end]).rstrip()
        body = rewrite_links(body, chapter)
        image_dir_name = re.escape(out.stem + "_figures")
        body = re.sub(rf"\]\({image_dir_name}/", rf"](../{out.stem}_figures/", body)

        # Each chapter is now a standalone document, so promote its heading
        # hierarchy from h2–h6 to h1–h5. Heading fragments remain unchanged.
        promoted: list[str] = []
        in_fence = False
        for line in body.splitlines():
            if line.startswith("```"):
                in_fence = not in_fence
            if not in_fence and re.match(r"^#{2,6}\s", line):
                line = line[1:]
            promoted.append(line)
        first_heading, _, remainder = "\n".join(promoted).partition("\n")
        chapter_text = (
            f"{first_heading}\n\n[← RM0440 index](../{out.name})\n\n"
            f"{remainder.strip()}\n"
        )
        (chapter_dir / chapter_files[chapter]).write_text(chapter_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--xhtml", type=Path, help="Use an existing MuPDF XHTML extraction")
    parser.add_argument("--html", type=Path, help="Use an existing MuPDF positioned HTML extraction")
    parser.add_argument(
        "--single-file",
        action="store_true",
        help="Write one large Markdown file instead of an index and per-chapter files",
    )
    args = parser.parse_args()
    if args.xhtml:
        image_dir = args.output.with_name(args.output.stem + "_figures")
        convert_xhtml(
            args.xhtml,
            args.output,
            args.html,
            pdf=args.pdf,
            image_dir=image_dir,
            split_chapters=not args.single_file,
        )
    else:
        extract_sources(args.pdf, args.output, split_chapters=not args.single_file)
    print(f"wrote {args.output} ({args.output.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
