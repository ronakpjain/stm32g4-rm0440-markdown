# 48 Device electronic signature

[← RM0440 index](../STM32G4_RM0440.md)

The device electronic signature is stored in the System memory area of the Flash memory module, and
can be read using the debug interface or by the CPU. It contains factory-programmed identification
and calibration data that allow the user firmware or other external devices to automatically match
to the characteristics of the STM32G4 series microcontroller.

## 48.1 Unique device ID register (96 bits)

The unique device identifier is ideally suited:

- for use as serial numbers (for example USB string serial numbers or other end applications)
- for use as part of the security keys in order to increase the security of code in Flash memory
  while using and combining this unique ID with software cryptographic primitives and protocols
  before programming the internal Flash memory
- to activate secure boot processes, etc.

The 96-bit unique device identifier provides a reference number which is unique for any device and
in any context. These bits cannot be altered by the user.

Base address: 0x1FFF 7590

- **Address offset:** 0x00

Read only = 0xXXXX XXXX where X is factory-programmed

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | `UID[31]` | r | X and Y coordinates on the wafer |
| 30 | `UID[30]` | r | ↳ |
| 29 | `UID[29]` | r | ↳ |
| 28 | `UID[28]` | r | ↳ |
| 27 | `UID[27]` | r | ↳ |
| 26 | `UID[26]` | r | ↳ |
| 25 | `UID[25]` | r | ↳ |
| 24 | `UID[24]` | r | ↳ |
| 23 | `UID[23]` | r | ↳ |
| 22 | `UID[22]` | r | ↳ |
| 21 | `UID[21]` | r | ↳ |
| 20 | `UID[20]` | r | ↳ |
| 19 | `UID[19]` | r | ↳ |
| 18 | `UID[18]` | r | ↳ |
| 17 | `UID[17]` | r | ↳ |
| 16 | `UID[16]` | r | ↳ |
| 15 | `UID[15]` | r | ↳ |
| 14 | `UID[14]` | r | ↳ |
| 13 | `UID[13]` | r | ↳ |
| 12 | `UID[12]` | r | ↳ |
| 11 | `UID[11]` | r | ↳ |
| 10 | `UID[10]` | r | ↳ |
| 9 | `UID[9]` | r | ↳ |
| 8 | `UID[8]` | r | ↳ |
| 7 | `UID[7]` | r | ↳ |
| 6 | `UID[6]` | r | ↳ |
| 5 | `UID[5]` | r | ↳ |
| 4 | `UID[4]` | r | ↳ |
| 3 | `UID[3]` | r | ↳ |
| 2 | `UID[2]` | r | ↳ |
| 1 | `UID[1]` | r | ↳ |
| 0 | `UID[0]` | r | ↳ |

**Bits 31:0 — `UID[31:0]`:** X and Y coordinates on the wafer

- **Address offset:** 0x04

Read only = 0xXXXX XXXX where X is factory-programmed

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | `UID[63]` | r | LOT_NUM[23:0] |
| 30 | `UID[62]` | r | ↳ |
| 29 | `UID[61]` | r | ↳ |
| 28 | `UID[60]` | r | ↳ |
| 27 | `UID[59]` | r | ↳ |
| 26 | `UID[58]` | r | ↳ |
| 25 | `UID[57]` | r | ↳ |
| 24 | `UID[56]` | r | ↳ |
| 23 | `UID[55]` | r | ↳ |
| 22 | `UID[54]` | r | ↳ |
| 21 | `UID[53]` | r | ↳ |
| 20 | `UID[52]` | r | ↳ |
| 19 | `UID[51]` | r | ↳ |
| 18 | `UID[50]` | r | ↳ |
| 17 | `UID[49]` | r | ↳ |
| 16 | `UID[48]` | r | ↳ |
| 15 | `UID[47]` | r | ↳ |
| 14 | `UID[46]` | r | ↳ |
| 13 | `UID[45]` | r | ↳ |
| 12 | `UID[44]` | r | ↳ |
| 11 | `UID[43]` | r | ↳ |
| 10 | `UID[42]` | r | ↳ |
| 9 | `UID[41]` | r | ↳ |
| 8 | `UID[40]` | r | ↳ |
| 7 | `UID[39]` | r | WAF_NUM[7:0] |
| 6 | `UID[38]` | r | ↳ |
| 5 | `UID[37]` | r | ↳ |
| 4 | `UID[36]` | r | ↳ |
| 3 | `UID[35]` | r | ↳ |
| 2 | `UID[34]` | r | ↳ |
| 1 | `UID[33]` | r | ↳ |
| 0 | `UID[32]` | r | ↳ |

**Bits 31:8 — `UID[63:40]`:** LOT_NUM[23:0]

Lot number (ASCII encoded)

**Bits 7:0 — `UID[39:32]`:** WAF_NUM[7:0]

Wafer number (8-bit unsigned number)

- **Address offset:** 0x08

Read only = 0xXXXX XXXX where X is factory-programmed

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | `UID[95]` | r | LOT_NUM[55:24] |
| 30 | `UID[94]` | r | ↳ |
| 29 | `UID[93]` | r | ↳ |
| 28 | `UID[92]` | r | ↳ |
| 27 | `UID[91]` | r | ↳ |
| 26 | `UID[90]` | r | ↳ |
| 25 | `UID[89]` | r | ↳ |
| 24 | `UID[88]` | r | ↳ |
| 23 | `UID[87]` | r | ↳ |
| 22 | `UID[86]` | r | ↳ |
| 21 | `UID[85]` | r | ↳ |
| 20 | `UID[84]` | r | ↳ |
| 19 | `UID[83]` | r | ↳ |
| 18 | `UID[82]` | r | ↳ |
| 17 | `UID[81]` | r | ↳ |
| 16 | `UID[80]` | r | ↳ |
| 15 | `UID[79]` | r | ↳ |
| 14 | `UID[78]` | r | ↳ |
| 13 | `UID[77]` | r | ↳ |
| 12 | `UID[76]` | r | ↳ |
| 11 | `UID[75]` | r | ↳ |
| 10 | `UID[74]` | r | ↳ |
| 9 | `UID[73]` | r | ↳ |
| 8 | `UID[72]` | r | ↳ |
| 7 | `UID[71]` | r | ↳ |
| 6 | `UID[70]` | r | ↳ |
| 5 | `UID[69]` | r | ↳ |
| 4 | `UID[68]` | r | ↳ |
| 3 | `UID[67]` | r | ↳ |
| 2 | `UID[66]` | r | ↳ |
| 1 | `UID[65]` | r | ↳ |
| 0 | `UID[64]` | r | ↳ |

**Bits 31:0 — `UID[95:64]`:** LOT_NUM[55:24]

Lot number (ASCII encoded)

## 48.2 Flash size data register

Base address: 0x1FFF 75E0

- **Address offset:** 0x00

Read only = 0xXXXX where X is factory-programmed

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 15 | `FLASH_SIZE[15]` | r | Flash memory size |
| 14 | `FLASH_SIZE[14]` | r | ↳ |
| 13 | `FLASH_SIZE[13]` | r | ↳ |
| 12 | `FLASH_SIZE[12]` | r | ↳ |
| 11 | `FLASH_SIZE[11]` | r | ↳ |
| 10 | `FLASH_SIZE[10]` | r | ↳ |
| 9 | `FLASH_SIZE[9]` | r | ↳ |
| 8 | `FLASH_SIZE[8]` | r | ↳ |
| 7 | `FLASH_SIZE[7]` | r | ↳ |
| 6 | `FLASH_SIZE[6]` | r | ↳ |
| 5 | `FLASH_SIZE[5]` | r | ↳ |
| 4 | `FLASH_SIZE[4]` | r | ↳ |
| 3 | `FLASH_SIZE[3]` | r | ↳ |
| 2 | `FLASH_SIZE[2]` | r | ↳ |
| 1 | `FLASH_SIZE[1]` | r | ↳ |
| 0 | `FLASH_SIZE[0]` | r | ↳ |

**Bits 15:0 — `FLASH_SIZE[15:0]`:** Flash memory size

This bitfield indicates the size of the device Flash memory expressed in Kbytes.

As an example, 0x040 corresponds to 64 Kbytes.

## 48.3 Package data register

Base address: 0x1FFF 7500

- **Address offset:** 0x00

Read only = 0xXXXX where X is factory-programmed

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 15 | Reserved | — | kept at reset value |
| 14 | Reserved | — | ↳ |
| 13 | Reserved | — | ↳ |
| 12 | Reserved | — | ↳ |
| 11 | Reserved | — | ↳ |
| 10 | Reserved | — | ↳ |
| 9 | Reserved | — | ↳ |
| 8 | Reserved | — | ↳ |
| 7 | Reserved | — | ↳ |
| 6 | Reserved | — | ↳ |
| 5 | Reserved | — | ↳ |
| 4 | `PKG[4]` | r | Package type |
| 3 | `PKG[3]` | r | ↳ |
| 2 | `PKG[2]` | r | ↳ |
| 1 | `PKG[1]` | r | ↳ |
| 0 | `PKG[0]` | r | ↳ |

**Bits 15:5 — Reserved:** kept at reset value

**Bits 4:0 — `PKG[4:0]`:** Package type

- `00000`: LQFP64
- `00001`: WLCSP64
- `00010`: LQFP100 (all devices) and LQFP80 (for category 2 devices)
- `00101`: WLCSP81 and LQFP80 (for category 3 devices)
- `00111`: LQFP128 / UFBGA121
- `01000`: UFQFPN32
- `01001`: LQFP32
- `01010`: UFQFPN48
- `01011`: LQFP48
- `01100`: WLCSP49
- `01101`: UFBGA64
- `01110`: TFBGA100
- `10001`: LQFP80 (for category 4 devices only)

Others: reserved
