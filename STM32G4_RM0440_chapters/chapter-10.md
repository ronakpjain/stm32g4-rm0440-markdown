# 10 System configuration controller (SYSCFG)

[← RM0440 index](../STM32G4_RM0440.md)

## 10.1 SYSCFG main features

The STM32G4 series devices feature a set of configuration registers. The main purposes of the system
configuration controller are the following:

- Remapping memory areas
- Managing the external interrupt line connection to the GPIOs
- Managing robustness feature
- Setting CCM RAM write protection and software erase
- Configuring FPU interrupts
- Enabling /disabling I2C Fast-mode Plus driving capability on some I/Os and voltage booster for
  I/Os analog switches.

## 10.2 SYSCFG registers

### 10.2.1 SYSCFG memory remap register (SYSCFG_MEMRMP)

This register is used for specific configurations on memory remap.

- **Address offset:** 0x00
- **Reset value:** 0x0000 000X (X is the memory mode selected by the BOOT0 pin and BOOT1 option bit)

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | Reserved | — | kept at reset value. |
| 30 | Reserved | — | ↳ |
| 29 | Reserved | — | ↳ |
| 28 | Reserved | — | ↳ |
| 27 | Reserved | — | ↳ |
| 26 | Reserved | — | ↳ |
| 25 | Reserved | — | ↳ |
| 24 | Reserved | — | ↳ |
| 23 | Reserved | — | ↳ |
| 22 | Reserved | — | ↳ |
| 21 | Reserved | — | ↳ |
| 20 | Reserved | — | ↳ |
| 19 | Reserved | — | ↳ |
| 18 | Reserved | — | ↳ |
| 17 | Reserved | — | ↳ |
| 16 | Reserved | — | ↳ |
| 15 | Reserved | — | ↳ |
| 14 | Reserved | — | ↳ |
| 13 | Reserved | — | ↳ |
| 12 | Reserved | — | ↳ |
| 11 | Reserved | — | ↳ |
| 10 | Reserved | — | ↳ |
| 9 | Reserved | — | ↳ |
| 8 | `FB_MODE` | rw | Flash Bank mode selection |
| 7 | Reserved | — | kept at reset value. |
| 6 | Reserved | — | ↳ |
| 5 | Reserved | — | ↳ |
| 4 | Reserved | — | ↳ |
| 3 | Reserved | — | ↳ |
| 2 | `MEM_MODE` | rw | Memory mapping selection |
| 1 | `MEM_MODE` | rw | ↳ |
| 0 | `MEM_MODE` | rw | ↳ |

**Bits 31:9 — Reserved:** kept at reset value.

**Bit 8 — `FB_MODE`:** Flash Bank mode selection

- `0`: Flash Bank 1 mapped at 0x0800 0000 (and aliased @0x0000 0000(1)) and Flash Bank 2
  mapped at 0x0804 0000 (and aliased at 0x0008 0000)
- `1`: Flash Bank2 mapped at 0x0800 0000 (and aliased @0x0000 0000(1)) and Flash Bank 1
  mapped at 0x0804 0000 (and aliased at 0x0008 0000)

**Bits 7:3 — Reserved:** kept at reset value.

**Bits 2:0 — `MEM_MODE`:** Memory mapping selection

These bits control the memory internal mapping at address 0x0000 0000. These bits are
used to select the physical remap by software and so, bypass the BOOT pin and the option
bit setting. After reset these bits take the value selected by BOOT0 pin (or option bit
nBOOT0) and BOOT1 option bit.

- `000`: Main Flash memory mapped at 0x00000000(1).
- `001`: System Flash memory mapped at 0x00000000.
- `010`: FSMC memory.
- `011`: SRAM1 mapped at 0x00000000.
- `100`: QUADSPI memory mapped at 0x0000 0000
- `101`: Reserved
- `111`: Reserved

1. When BFB2 bit is set, the system memory remains aliased at @0x0000 0000

> **Note:** When the FSMC is remapped at address 0x0000 0000, only the first two regions of Bank 1
> memory controller (Bank1 NOR/PSRAM 1 and NOR/PSRAM 2) can be remapped. In remap mode, the CPU can
> access the external memory via ICode bus instead of System bus which boosts up the performance.

### 10.2.2 SYSCFG configuration register 1 (SYSCFG_CFGR1)

- **Address offset:** 0x04
- **Reset value:** 0x7C00 0000

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | `FPU_IE[5..0]` | rw | Floating Point Unit interrupts enable bits |
| 30 | `FPU_IE[5..0]` | rw | ↳ |
| 29 | `FPU_IE[5..0]` | rw | ↳ |
| 28 | `FPU_IE[5..0]` | rw | ↳ |
| 27 | `FPU_IE[5..0]` | rw | ↳ |
| 26 | `FPU_IE[5..0]` | rw | ↳ |
| 25 | Reserved | — | kept at reset value. |
| 24 | Reserved | — | ↳ |
| 23 | `I2C4_FMP` | rw | Fast-mode Plus driving capability activation |
| 22 | `I2C3_FMP` | rw | I2C3 Fast-mode Plus driving capability activation |
| 21 | `I2C2_FMP` | rw | I2C2 Fast-mode Plus driving capability activation |
| 20 | `I2C1_FMP` | rw | I2C1 Fast-mode Plus driving capability activation |
| 19 | `I2C_PB9_FMP` | rw | Fast-mode Plus (Fm+) driving capability activation on PB9 |
| 18 | `I2C_PB8_FMP` | rw | Fast-mode Plus (Fm+) driving capability activation on PB8 |
| 17 | `I2C_PB7_FMP` | rw | Fast-mode Plus (Fm+) driving capability activation on PB7 |
| 16 | `I2C_PB6_FMP` | rw | Fast-mode Plus (Fm+) driving capability activation on PB6 |
| 15 | Reserved | — | kept at reset value. |
| 14 | Reserved | — | ↳ |
| 13 | Reserved | — | ↳ |
| 12 | Reserved | — | ↳ |
| 11 | Reserved | — | ↳ |
| 10 | Reserved | — | ↳ |
| 9 | `ANASWVDD` | rw | GPIO analog switch control voltage selection |
| 8 | `BOOSTEN` | rw | I/O analog switch voltage booster enable |
| 7 | Reserved | — | kept at reset value. |
| 6 | Reserved | — | ↳ |
| 5 | Reserved | — | ↳ |
| 4 | Reserved | — | ↳ |
| 3 | Reserved | — | ↳ |
| 2 | Reserved | — | ↳ |
| 1 | Reserved | — | ↳ |
| 0 | Reserved | — | ↳ |

**Bits 31:26 — `FPU_IE[5..0]`:** Floating Point Unit interrupts enable bits

FPU_IE[5]: Inexact interrupt enable

FPU_IE[4]: Input denormal interrupt enable

FPU_IE[3]: Overflow interrupt enable

FPU_IE[2]: underflow interrupt enable

FPU_IE[1]: Divide-by-zero interrupt enable

FPU_IE[0]: Invalid operation interrupt enable

**Bits 25:24 — Reserved:** kept at reset value.

**Bit 23 — `I2C4_FMP`:** Fast-mode Plus driving capability activation

This bit enables the Fm+ driving mode on I2C4 pins selected through AF selection bits.

- `0`: Fm+ mode is not enabled on I2C4 pins selected through AF selection bits
- `1`: Fm+ mode is enabled on I2C4 pins selected through AF selection bits.

**Bit 22 — `I2C3_FMP`:** I2C3 Fast-mode Plus driving capability activation

This bit enables the Fm+ driving mode on I2C3 pins selected through AF selection bits.

- `0`: Fm+ mode is not enabled on I2C3 pins selected through AF selection bits
- `1`: Fm+ mode is enabled on I2C3 pins selected through AF selection bits.

**Bit 21 — `I2C2_FMP`:** I2C2 Fast-mode Plus driving capability activation

This bit enables the Fm+ driving mode on I2C2 pins selected through AF selection bits.

- `0`: Fm+ mode is not enabled on I2C2 pins selected through AF selection bits
- `1`: Fm+ mode is enabled on I2C2 pins selected through AF selection bits.

**Bit 20 — `I2C1_FMP`:** I2C1 Fast-mode Plus driving capability activation

This bit enables the Fm+ driving mode on I2C1 pins selected through AF selection bits.

- `0`: Fm+ mode is not enabled on I2C1 pins selected through AF selection bits
- `1`: Fm+ mode is enabled on I2C1 pins selected through AF selection bits.

**Bit 19 — `I2C_PB9_FMP`:** Fast-mode Plus (Fm+) driving capability activation on PB9

This bit enables the Fm+ driving mode for PB9.

- `0`: PB9 pin operates in standard mode.
- `1`: Fm+ mode enabled on PB9 pin, and the Speed control is bypassed.

**Bit 18 — `I2C_PB8_FMP`:** Fast-mode Plus (Fm+) driving capability activation on PB8

This bit enables the Fm+ driving mode for PB8.

- `0`: PB8 pin operates in standard mode.
- `1`: Fm+ mode enabled on PB8 pin, and the Speed control is bypassed.

**Bit 17 — `I2C_PB7_FMP`:** Fast-mode Plus (Fm+) driving capability activation on PB7

This bit enables the Fm+ driving mode for PB7.

- `0`: PB7 pin operates in standard mode.
- `1`: Fm+ mode enabled on PB7 pin, and the Speed control is bypassed.

**Bit 16 — `I2C_PB6_FMP`:** Fast-mode Plus (Fm+) driving capability activation on PB6

This bit enables the Fm+ driving mode for PB6.

- `0`: PB6 pin operates in standard mode.
- `1`: Fm+ mode enabled on PB6 pin, and the Speed control is bypassed.

**Bits 15:10 — Reserved:** kept at reset value.

**Bit 9 — `ANASWVDD`:** GPIO analog switch control voltage selection

- `0`: I/O analog switches supplied by VDDA or booster when booster is ON
- `1`: I/O analog switches supplied by VDD.

Refer to Table 60 for bit 9 setting.

**Bit 8 — `BOOSTEN`:** I/O analog switch voltage booster enable

- `0`: I/O analog switches are supplied by VDDA voltage. This is the recommended configuration
  when using the ADC in high VDDA voltage operation.
- `1`: I/O analog switches are supplied by a dedicated voltage booster (supplied by VDD). This is
  the recommended configuration when using the ADC in low VDDA voltage operation.

**Bits 7:0 — Reserved:** kept at reset value.

Table 60 describes when the bit 9 (ANASWVDD) and the bit 8 (BOOSTEN) should be set or reset
depending on the voltage settings.

> **Note:** When FM+ mode is activated on GPIO pin, the speed configuration of the GPIO (in

GPIOx_OSPEEDR register) is ignored. Program this register only after the AF selection through the
GPIOx_AFRH or GPIOx_AFRL register.

**Table 60. BOOSTEN and ANASWVDD set/reset**

| VDD | VDDA | BOOSTEN | ANASWVDD |
| --- | --- | --- | --- |
| - | > 2.4 V | 0 | 0 |
| > 2.4 V | \< 2.4 V | 0 | 1 |
| \< 2.4 V | \< 2.4 V | 1 | 0 |

### 10.2.3 SYSCFG external interrupt configuration register 1 (SYSCFG_EXTICR1)

- **Address offset:** 0x08
- **Reset value:** 0x0000 0000

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | Reserved | — | kept at reset value. |
| 30 | Reserved | — | ↳ |
| 29 | Reserved | — | ↳ |
| 28 | Reserved | — | ↳ |
| 27 | Reserved | — | ↳ |
| 26 | Reserved | — | ↳ |
| 25 | Reserved | — | ↳ |
| 24 | Reserved | — | ↳ |
| 23 | Reserved | — | ↳ |
| 22 | Reserved | — | ↳ |
| 21 | Reserved | — | ↳ |
| 20 | Reserved | — | ↳ |
| 19 | Reserved | — | ↳ |
| 18 | Reserved | — | ↳ |
| 17 | Reserved | — | ↳ |
| 16 | Reserved | — | ↳ |
| 15 | `EXTI3[3]` | rw | EXTI 3 configuration bits |
| 14 | `EXTI3[2]` | rw | ↳ |
| 13 | `EXTI3[1]` | rw | ↳ |
| 12 | `EXTI3[0]` | rw | ↳ |
| 11 | `EXTI2[3]` | rw | EXTI 2 configuration bits |
| 10 | `EXTI2[2]` | rw | ↳ |
| 9 | `EXTI2[1]` | rw | ↳ |
| 8 | `EXTI2[0]` | rw | ↳ |
| 7 | `EXTI1[3]` | rw | EXTI 1 configuration bits |
| 6 | `EXTI1[2]` | rw | ↳ |
| 5 | `EXTI1[1]` | rw | ↳ |
| 4 | `EXTI1[0]` | rw | ↳ |
| 3 | `EXTI0[3]` | rw | EXTI 0 configuration bits |
| 2 | `EXTI0[2]` | rw | ↳ |
| 1 | `EXTI0[1]` | rw | ↳ |
| 0 | `EXTI0[0]` | rw | ↳ |

**Bits 31:16 — Reserved:** kept at reset value.

**Bits 15:12 — `EXTI3[3:0]`:** EXTI 3 configuration bits

These bits are written by software to select the source input for the EXTI3 external interrupt.

- `0000`: PA[3] pin
- `0001`: PB[3] pin
- `0010`: PC[3] pin
- `0011`: PD[3] pin
- `0100`: PE[3] pin
- `0101`: PF[3] pin
- `0110`: PG[3] pin

**Bits 11:8 — `EXTI2[3:0]`:** EXTI 2 configuration bits

These bits are written by software to select the source input for the EXTI2 external interrupt.

- `0000`: PA[2] pin
- `0001`: PB[2] pin
- `0010`: PC[2] pin
- `0011`: PD[2] pin
- `0100`: PE[2] pin
- `0101`: PF[2] pin
- `0110`: PG[2] pin

**Bits 7:4 — `EXTI1[3:0]`:** EXTI 1 configuration bits

These bits are written by software to select the source input for the EXTI1 external interrupt.

- `0000`: PA[1] pin
- `0001`: PB[1] pin
- `0010`: PC[1] pin
- `0011`: PD[1] pin
- `0100`: PE[1] pin
- `0101`: PF[1] pin
- `0110`: PG[1] pin

**Bits 3:0 — `EXTI0[3:0]`:** EXTI 0 configuration bits

These bits are written by software to select the source input for the EXTI0 external interrupt.

- `0000`: PA[0] pin
- `0001`: PB[0] pin
- `0010`: PC[0] pin
- `0011`: PD[0] pin
- `0100`: PE[0] pin
- `0101`: PF[0] pin
- `0110`: PG[0] pin

### 10.2.4 SYSCFG external interrupt configuration register 2 (SYSCFG_EXTICR2)

- **Address offset:** 0x0C
- **Reset value:** 0x0000 0000

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | Reserved | — | kept at reset value. |
| 30 | Reserved | — | ↳ |
| 29 | Reserved | — | ↳ |
| 28 | Reserved | — | ↳ |
| 27 | Reserved | — | ↳ |
| 26 | Reserved | — | ↳ |
| 25 | Reserved | — | ↳ |
| 24 | Reserved | — | ↳ |
| 23 | Reserved | — | ↳ |
| 22 | Reserved | — | ↳ |
| 21 | Reserved | — | ↳ |
| 20 | Reserved | — | ↳ |
| 19 | Reserved | — | ↳ |
| 18 | Reserved | — | ↳ |
| 17 | Reserved | — | ↳ |
| 16 | Reserved | — | ↳ |
| 15 | `EXTI7[3]` | rw | EXTI 7 configuration bits |
| 14 | `EXTI7[2]` | rw | ↳ |
| 13 | `EXTI7[1]` | rw | ↳ |
| 12 | `EXTI7[0]` | rw | ↳ |
| 11 | `EXTI6[3]` | rw | EXTI 6 configuration bits |
| 10 | `EXTI6[2]` | rw | ↳ |
| 9 | `EXTI6[1]` | rw | ↳ |
| 8 | `EXTI6[0]` | rw | ↳ |
| 7 | `EXTI5[3]` | rw | EXTI 5 configuration bits |
| 6 | `EXTI5[2]` | rw | ↳ |
| 5 | `EXTI5[1]` | rw | ↳ |
| 4 | `EXTI5[0]` | rw | ↳ |
| 3 | `EXTI4[3]` | rw | EXTI 4 configuration bits |
| 2 | `EXTI4[2]` | rw | ↳ |
| 1 | `EXTI4[1]` | rw | ↳ |
| 0 | `EXTI4[0]` | rw | ↳ |

**Bits 31:16 — Reserved:** kept at reset value.

**Bits 15:12 — `EXTI7[3:0]`:** EXTI 7 configuration bits

These bits are written by software to select the source input for the EXTI7 external interrupt.

- `0000`: PA[7] pin
- `0001`: PB[7] pin
- `0010`: PC[7] pin
- `0011`: PD[7] pin
- `0100`: PE[7] pin
- `0101`: PF[7] pin
- `0110`: PG[7] pin

**Bits 11:8 — `EXTI6[3:0]`:** EXTI 6 configuration bits

These bits are written by software to select the source input for the EXTI6 external interrupt.

- `0000`: PA[6] pin
- `0001`: PB[6] pin
- `0010`: PC[6] pin
- `0011`: PD[6] pin
- `0100`: PE[6] pin
- `0101`: PF[6] pin
- `0110`: PG[6] pin

**Bits 7:4 — `EXTI5[3:0]`:** EXTI 5 configuration bits

These bits are written by software to select the source input for the EXTI5 external interrupt.

- `0000`: PA[5] pin
- `0001`: PB[5] pin
- `0010`: PC[5] pin
- `0011`: PD[5] pin
- `0100`: PE[5] pin
- `0101`: PF[5] pin
- `0110`: PG[5] pin

**Bits 3:0 — `EXTI4[3:0]`:** EXTI 4 configuration bits

These bits are written by software to select the source input for the EXTI4 external interrupt.

- `0000`: PA[4] pin
- `0001`: PB[4] pin
- `0010`: PC[4] pin
- `0011`: PD[4] pin
- `0100`: PE[4] pin
- `0101`: PF[4] pin
- `0110`: PG[4] pin

> **Note:** Some of the I/O pins mentioned in the above register may not be available on small
> packages.

### 10.2.5 SYSCFG external interrupt configuration register 3 (SYSCFG_EXTICR3)

- **Address offset:** 0x10
- **Reset value:** 0x0000 0000

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | Reserved | — | kept at reset value. |
| 30 | Reserved | — | ↳ |
| 29 | Reserved | — | ↳ |
| 28 | Reserved | — | ↳ |
| 27 | Reserved | — | ↳ |
| 26 | Reserved | — | ↳ |
| 25 | Reserved | — | ↳ |
| 24 | Reserved | — | ↳ |
| 23 | Reserved | — | ↳ |
| 22 | Reserved | — | ↳ |
| 21 | Reserved | — | ↳ |
| 20 | Reserved | — | ↳ |
| 19 | Reserved | — | ↳ |
| 18 | Reserved | — | ↳ |
| 17 | Reserved | — | ↳ |
| 16 | Reserved | — | ↳ |
| 15 | `EXTI11[3]` | rw | EXTI 11 configuration bits |
| 14 | `EXTI11[2]` | rw | ↳ |
| 13 | `EXTI11[1]` | rw | ↳ |
| 12 | `EXTI11[0]` | rw | ↳ |
| 11 | `EXTI10[3]` | rw | EXTI 10 configuration bits |
| 10 | `EXTI10[2]` | rw | ↳ |
| 9 | `EXTI10[1]` | rw | ↳ |
| 8 | `EXTI10[0]` | rw | ↳ |
| 7 | `EXTI9[3]` | rw | EXTI 9 configuration bits |
| 6 | `EXTI9[2]` | rw | ↳ |
| 5 | `EXTI9[1]` | rw | ↳ |
| 4 | `EXTI9[0]` | rw | ↳ |
| 3 | `EXTI8[3]` | rw | EXTI 8 configuration bits |
| 2 | `EXTI8[2]` | rw | ↳ |
| 1 | `EXTI8[1]` | rw | ↳ |
| 0 | `EXTI8[0]` | rw | ↳ |

**Bits 31:16 — Reserved:** kept at reset value.

**Bits 15:12 — `EXTI11[3:0]`:** EXTI 11 configuration bits

These bits are written by software to select the source input for the EXTI11 external interrupt.

- `0000`: PA[11] pin
- `0001`: PB[11] pin
- `0010`: PC[11] pin
- `0011`: PD[11] pin
- `0100`: PE[11] pin
- `0101`: PF[11] pin

**Bits 11:8 — `EXTI10[3:0]`:** EXTI 10 configuration bits

These bits are written by software to select the source input for the EXTI10 external interrupt.

- `0000`: PA[10] pin
- `0001`: PB[10] pin
- `0010`: PC[10] pin
- `0011`: PD[10] pin
- `0100`: PE[10] pin
- `0101`: PF[10] pin
- `0110`: PG[10] pin

**Bits 7:4 — `EXTI9[3:0]`:** EXTI 9 configuration bits

These bits are written by software to select the source input for the EXTI9 external interrupt.

- `0000`: PA[9] pin
- `0001`: PB[9] pin
- `0010`: PC[9] pin
- `0011`: PD[9] pin
- `0100`: PE[9] pin
- `0101`: PF[9] pin
- `0110`: PG[9] pin

**Bits 3:0 — `EXTI8[3:0]`:** EXTI 8 configuration bits

These bits are written by software to select the source input for the EXTI8 external interrupt.

- `0000`: PA[8] pin
- `0001`: PB[8] pin
- `0010`: PC[8] pin
- `0011`: PD[8] pin
- `0100`: PE[8] pin
- `0101`: PF[8] pin
- `0110`: PG[8] pin

> **Note:** Some of the I/O pins mentioned in the above register may not be available on small
> packages.

### 10.2.6 SYSCFG external interrupt configuration register 4 (SYSCFG_EXTICR4)

- **Address offset:** 0x14
- **Reset value:** 0x0000 0000

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | Reserved | — | kept at reset value. |
| 30 | Reserved | — | ↳ |
| 29 | Reserved | — | ↳ |
| 28 | Reserved | — | ↳ |
| 27 | Reserved | — | ↳ |
| 26 | Reserved | — | ↳ |
| 25 | Reserved | — | ↳ |
| 24 | Reserved | — | ↳ |
| 23 | Reserved | — | ↳ |
| 22 | Reserved | — | ↳ |
| 21 | Reserved | — | ↳ |
| 20 | Reserved | — | ↳ |
| 19 | Reserved | — | ↳ |
| 18 | Reserved | — | ↳ |
| 17 | Reserved | — | ↳ |
| 16 | Reserved | — | ↳ |
| 15 | `EXTI15[3]` | rw | EXTI 15 configuration bits |
| 14 | `EXTI15[2]` | rw | ↳ |
| 13 | `EXTI15[1]` | rw | ↳ |
| 12 | `EXTI15[0]` | rw | ↳ |
| 11 | `EXTI14[3]` | rw | EXTI 14 configuration bits |
| 10 | `EXTI14[2]` | rw | ↳ |
| 9 | `EXTI14[1]` | rw | ↳ |
| 8 | `EXTI14[0]` | rw | ↳ |
| 7 | `EXTI13[3]` | rw | EXTI 13 configuration bits |
| 6 | `EXTI13[2]` | rw | ↳ |
| 5 | `EXTI13[1]` | rw | ↳ |
| 4 | `EXTI13[0]` | rw | ↳ |
| 3 | `EXTI12[3]` | rw | EXTI 12 configuration bits |
| 2 | `EXTI12[2]` | rw | ↳ |
| 1 | `EXTI12[1]` | rw | ↳ |
| 0 | `EXTI12[0]` | rw | ↳ |

**Bits 31:16 — Reserved:** kept at reset value.

**Bits 15:12 — `EXTI15[3:0]`:** EXTI 15 configuration bits

These bits are written by software to select the source input for the EXTI15 external
interrupt.

- `0000`: PA[15] pin
- `0001`: PB[15] pin
- `0010`: PC[15] pin
- `0011`: PD[15] pin
- `0100`: PE[15] pin
- `0101`: PF[15] pin

**Bits 11:8 — `EXTI14[3:0]`:** EXTI 14 configuration bits

These bits are written by software to select the source input for the EXTI14 external
interrupt.

- `0000`: PA[14] pin
- `0001`: PB[14] pin
- `0010`: PC[14] pin
- `0011`: PD[14] pin
- `0100`: PE[14] pin
- `0101`: PF[14] pin

**Bits 7:4 — `EXTI13[3:0]`:** EXTI 13 configuration bits

These bits are written by software to select the source input for the EXTI13 external
interrupt.

- `0000`: PA[13] pin
- `0001`: PB[13] pin
- `0010`: PC[13] pin
- `0011`: PD[13] pin
- `0100`: PE[13] pin
- `0101`: PF[13] pin

**Bits 3:0 — `EXTI12[3:0]`:** EXTI 12 configuration bits

These bits are written by software to select the source input for the EXTI12 external
interrupt.

- `0000`: PA[12] pin
- `0001`: PB[12] pin
- `0010`: PC[12] pin
- `0011`: PD[12] pin
- `0100`: PE[12] pin
- `0101`: PF[12] pin

> **Note:** Some of the I/O pins mentioned in the above register may not be available on small
> packages.

### 10.2.7 SYSCFG CCM SRAM control and status register (SYSCFG_SCSR)

- **Address offset:** 0x18

System reset value: 0x0000 0000

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | Reserved | — | kept at reset value |
| 30 | Reserved | — | ↳ |
| 29 | Reserved | — | ↳ |
| 28 | Reserved | — | ↳ |
| 27 | Reserved | — | ↳ |
| 26 | Reserved | — | ↳ |
| 25 | Reserved | — | ↳ |
| 24 | Reserved | — | ↳ |
| 23 | Reserved | — | ↳ |
| 22 | Reserved | — | ↳ |
| 21 | Reserved | — | ↳ |
| 20 | Reserved | — | ↳ |
| 19 | Reserved | — | ↳ |
| 18 | Reserved | — | ↳ |
| 17 | Reserved | — | ↳ |
| 16 | Reserved | — | ↳ |
| 15 | Reserved | — | ↳ |
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
| 4 | Reserved | — | ↳ |
| 3 | Reserved | — | ↳ |
| 2 | Reserved | — | ↳ |
| 1 | `CCMBSY` | — | CCM SRAM busy by erase operation |
| 0 | `CCMER` | — | CCM SRAM Erase |

**Bits 31:2 — Reserved:** kept at reset value

**Bit 1 — `CCMBSY`:** CCM SRAM busy by erase operation

- `0`: No CCM SRAM erase operation is on going.
- `1`: CCM SRAM erase operation is on going.

**Bit 0 — `CCMER`:** CCM SRAM Erase

Setting this bit starts a hardware CCM SRAM erase operation. This bit is automatically cleared at
the end of the CCM SRAM erase operation.

> **Note:** This bit is write-protected: setting this bit is possible only after the correct key sequence is written in the SYSCFG_SKR register.

### 10.2.8 SYSCFG configuration register 2 (SYSCFG_CFGR2)

- **Address offset:** 0x1C

System reset value: 0x0000 0000

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | Reserved | — | kept at reset value |
| 30 | Reserved | — | ↳ |
| 29 | Reserved | — | ↳ |
| 28 | Reserved | — | ↳ |
| 27 | Reserved | — | ↳ |
| 26 | Reserved | — | ↳ |
| 25 | Reserved | — | ↳ |
| 24 | Reserved | — | ↳ |
| 23 | Reserved | — | ↳ |
| 22 | Reserved | — | ↳ |
| 21 | Reserved | — | ↳ |
| 20 | Reserved | — | ↳ |
| 19 | Reserved | — | ↳ |
| 18 | Reserved | — | ↳ |
| 17 | Reserved | — | ↳ |
| 16 | Reserved | — | ↳ |
| 15 | Reserved | — | ↳ |
| 14 | Reserved | — | ↳ |
| 13 | Reserved | — | ↳ |
| 12 | Reserved | — | ↳ |
| 11 | Reserved | — | ↳ |
| 10 | Reserved | — | ↳ |
| 9 | Reserved | — | ↳ |
| 8 | `SPF` | rc_w1 | SRAM1 and CCM SRAM parity error flag |
| 7 | Reserved | — | kept at reset value |
| 6 | Reserved | — | ↳ |
| 5 | Reserved | — | ↳ |
| 4 | Reserved | — | ↳ |
| 3 | `ECCL` | rs | ECC Lock |
| 2 | `PVDL` | rs | PVD lock enable bit |
| 1 | `SPL` | rs | SRAM1 and CCM SRAM parity lock bit |
| 0 | `CLL` | rs | Cortex®-M4 LOCKUP (Hardfault) output enable bit |

**Bits 31:9 — Reserved:** kept at reset value

**Bit 8 — `SPF`:** SRAM1 and CCM SRAM parity error flag

This bit is set by hardware when an SRAM1 or CCM SRAM parity error is detected. It is cleared by
software by writing ‘1’.

- `0`: No parity error detected
- `1`: Parity error detected

**Bits 7:4 — Reserved:** kept at reset value

**Bit 3 — `ECCL`:** ECC Lock

This bit is set by software and cleared only by a system reset. It can be used to enable and lock
the Flash ECC error connection to TIM1/8/15/16/17/20 break input and hrtim_sys_flt input of HRTIM1.

- `0`: ECC error disconnected from TIM1/8/15/16/17/20 break input and hrtim_sys_flt input of HRTIM1.
- `1`: ECC error connected to TIM1/8/15/16/17/20 break input and hrtim_sys_flt input of HRTIM1.

**Bit 2 — `PVDL`:** PVD lock enable bit

This bit is set by software and cleared only by a system reset. It can be used to enable and lock
the PVD connection to TIM1/8/15/16/17/20 break input and hrtim_sys_flt input of HRTIM1., as well as
the PVDE and PLS[2:0] in the PWR_CR2 register.

- `0`: PVD interrupt disconnected from TIM1/8/15/16/17/20 break input and hrtim_sys_flt input of
  HRTIM1. PVDE and PLS[2:0] bits can be programmed by the application.
- `1`: PVD interrupt connected to TIM1/8/15/16/17/20 break input and hrtim_sys_flt input of HRTIM1,
  PVDE and PLS[2:0] bits are read only.

**Bit 1 — `SPL`:** SRAM1 and CCM SRAM parity lock bit

This bit is set by software and cleared only by a system reset. It can be used to enable and lock
the SRAM1 or CCM SRAM parity error signal connection to TIM1/8/15/16/17/20 break input and
hrtim_sys_flt input of HRTIM1.

- `0`: CCM SRAM parity error signal disconnected from TIM1/8/15/16/17/20 break input and
  hrtim_sys_flt input of HRTIM1.
- `1`: CCM SRAM parity error signal connected to TIM1/8/15/16/17/20 break input and hrtim_sys_flt
  input of HRTIM1.

**Bit 0 — `CLL`:** Cortex®-M4 LOCKUP (Hardfault) output enable bit

This bit is set by software and cleared only by a system reset. It can be used to enable and lock
the connection of Cortex®-M4 with FPU LOCKUP (Hardfault) output to TIM1/8/15/16/17/20 break input
and hrtim_sys_flt input of HRTIM1.

- `0`: Cortex®-M4 LOCKUP output disconnected from TIM1/8/15/16/17/20 break input and hrtim_sys_flt
  input of HRTIM1.
- `1`: Cortex®-M4 LOCKUP output connected to TIM1/8/15/16/17/20 break input and hrtim_sys_flt input
  of HRTIM1.

### 10.2.9 SYSCFG CCM SRAM write protection register (SYSCFG_SWPR)

- **Address offset:** 0x20

System reset value: 0x0000 0000

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | `PxWP (x = 0 to 31)` | rs | CCM SRAM page x write protection |
| 30 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 29 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 28 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 27 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 26 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 25 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 24 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 23 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 22 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 21 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 20 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 19 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 18 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 17 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 16 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 15 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 14 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 13 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 12 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 11 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 10 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 9 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 8 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 7 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 6 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 5 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 4 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 3 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 2 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 1 | `PxWP (x = 0 to 31)` | rs | ↳ |
| 0 | `PxWP (x = 0 to 31)` | rs | ↳ |

**Bits 31:0 — `PxWP (x = 0 to 31)`:** CCM SRAM page x write protection

These bits are set by software and cleared only by a system reset.

- `0`: Write protection of CCM SRAM page x is disabled.
- `1`: Write protection of CCM SRAM page x is enabled.

### 10.2.10 SYSCFG CCM SRAM key register (SYSCFG_SKR)

- **Address offset:** 0x24

System reset value: 0x0000 0000

**Register bit layout**

| Bit | Field | Access | Summary |
| ---: | --- | :---: | --- |
| 31 | Reserved | — | kept at reset value |
| 30 | Reserved | — | ↳ |
| 29 | Reserved | — | ↳ |
| 28 | Reserved | — | ↳ |
| 27 | Reserved | — | ↳ |
| 26 | Reserved | — | ↳ |
| 25 | Reserved | — | ↳ |
| 24 | Reserved | — | ↳ |
| 23 | Reserved | — | ↳ |
| 22 | Reserved | — | ↳ |
| 21 | Reserved | — | ↳ |
| 20 | Reserved | — | ↳ |
| 19 | Reserved | — | ↳ |
| 18 | Reserved | — | ↳ |
| 17 | Reserved | — | ↳ |
| 16 | Reserved | — | ↳ |
| 15 | Reserved | — | ↳ |
| 14 | Reserved | — | ↳ |
| 13 | Reserved | — | ↳ |
| 12 | Reserved | — | ↳ |
| 11 | Reserved | — | ↳ |
| 10 | Reserved | — | ↳ |
| 9 | Reserved | — | ↳ |
| 8 | Reserved | — | ↳ |
| 7 | `KEY[7]` | w | CCM SRAM write protection key for software erase |
| 6 | `KEY[6]` | w | ↳ |
| 5 | `KEY[5]` | w | ↳ |
| 4 | `KEY[4]` | w | ↳ |
| 3 | `KEY[3]` | w | ↳ |
| 2 | `KEY[2]` | w | ↳ |
| 1 | `KEY[1]` | w | ↳ |
| 0 | `KEY[0]` | w | ↳ |

**Bits 31:8 — Reserved:** kept at reset value

**Bits 7:0 — `KEY[7:0]`:** CCM SRAM write protection key for software erase

The following steps are required to unlock the write protection of the CCMER bit in the SYSCFG_SCSR
register.

1. Write "0xCA” into Key[7:0]
2. Write "0x53” into Key[7:0] Writing a wrong key reactivates the write protection.

### 10.2.11 SYSCFG register map

The following table gives the SYSCFG register map and the reset values.

**Register summary**

| Offset | Register | Reset value |
| --- | --- | --- |
| 0x00 | `SYSCFG_MEMRMP` | 0x0000 000X (X is the memory mode selected by the BOOT0 pin and BOOT1 option bit) |
| 0x04 | `SYSCFG_CFGR1` | 0x7C00 0000 |
| 0x08 | `SYSCFG_EXTICR1` | 0x0000 0000 |
| 0x0C | `SYSCFG_EXTICR2` | 0x0000 0000 |
| 0x10 | `SYSCFG_EXTICR3` | 0x0000 0000 |
| 0x14 | `SYSCFG_EXTICR4` | 0x0000 0000 |
| 0x18 | `SYSCFG_SCSR` | — |
| 0x1C | `SYSCFG_CFGR2` | — |
| 0x20 | `SYSCFG_SWPR` | — |
| 0x24 | `SYSCFG_SKR` | — |

Refer to [Section 2.2](chapter-02.md#22-memory-organization) for the register boundary addresses.
