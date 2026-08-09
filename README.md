# STM32G4 RM0440 Markdown Reference

A Neovim-friendly Markdown transcription of STMicroelectronics **RM0440 Rev. 9** (March 2025), the STM32G4 series reference manual.

## Read the manual

- [Manual index and section navigation](STM32G4_RM0440.md)
- [Chapter files](STM32G4_RM0440_chapters/)
- [Source PDF](STM32G4_RM0440.pdf)

The technical content is split into 50 chapter files to keep Markdown rendering responsive. Registers use native per-bit Markdown tables, extracted tables use native Markdown structures, and all 689 numbered figures are cropped to their actual artwork rather than linked as full PDF pages.

## Regenerate

Requirements:

- Python 3.11+
- MuPDF (`mutool`)
- Pillow
- NumPy

```bash
python3 transcribe_rm0440.py STM32G4_RM0440.pdf STM32G4_RM0440.md
```

The generator extracts positioned PDF text, rebuilds headings and navigation, creates semantic register layouts, and crops vector figure regions into PNG files.

## Source and rights

RM0440 and its technical content are published by STMicroelectronics. This private repository stores the source document and a derived transcription for internal reference.
