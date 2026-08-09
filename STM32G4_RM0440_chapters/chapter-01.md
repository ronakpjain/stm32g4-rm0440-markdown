# 1 Documentation conventions

[← RM0440 index](../STM32G4_RM0440.md)

## 1.1 General information

The STM32G4 series devices have an Arm®(a) Cortex®-M4 with FPU core with Arm®(a) TrustZone®.

## 1.2 List of abbreviations for registers

The following abbreviations(b) are used in register descriptions:

| Abbreviation | Meaning |
| --- | --- |
| read/write (rw) | Software can read and write to this bit. |
| read-only (r) | Software can only read this bit. |
| write-only (w) | Software can only write to this bit. Reading this bit returns the reset value. |
| read/clear write0 (rc_w0) | Software can read as well as clear this bit by writing 0. Writing 1 has no effect on the bit value. |
| read/clear write1 (rc_w1) | Software can read as well as clear this bit by writing 1. Writing 0 has no effect on the bit value. |
| read/clear write (rc_w) | Software can read as well as clear this bit by writing to the register. The value written to this bit is not important. |
| read/clear by read (rc_r) | Software can read this bit. Reading this bit automatically clears it to 0. Writing this bit has no effect on the bit value. |
| read/set by read (rs_r) | Software can read this bit. Reading this bit automatically sets it to 1. Writing this bit has no effect on the bit value. |
| read/set (rs) | Software can read as well as set this bit. Writing 0 has no effect on the bit value. |
| read/write once (rwo) | Software can only write once to this bit and can also read it at any time. Only a reset can return the bit to its reset value. |
| toggle (t) | The software can toggle the bit by writing 1. Writing 0 has no effect. |
| read-only write trigger (rt_w1) | Software can read this bit. Writing 1 triggers an event but has no effect on the bit value. |
| Reserved (Res.) | Reserved bit, must be kept at reset value. |

a. Arm and TrustZone are registered trademarks of Arm Limited (or its subsidiaries) in the US and/or
elsewhere.

b. This is an exhaustive list of all abbreviations applicable to STMicroelectronics
microcontrollers, some of them may not be used in the current document.

## 1.3 Register reset value

Bits (binary notation) or bits nibbles (hexadecimal notation) of which the reset value is undefined
are marked as X.

Bits (binary notation) or bits nibbles (hexadecimal notation) of which the reset value is unmodified
are marked as U.

## 1.4 Glossary

This section gives a brief definition of acronyms and abbreviations used in this document:

- Word: data of 32-bit length.
- Half-word: data of 16-bit length.
- Byte: data of 8-bit length.
- IAP (in-application programming): IAP is the ability to re-program the flash memory of a
  microcontroller while the user program is running.
- ICP (in-circuit programming): ICP is the ability to program the flash memory of a microcontroller
  using the JTAG protocol, the SWD protocol or the bootloader while the device is mounted on the
  user application board.
- Option bytes: device configuration bits stored in the flash memory.
- AHB: advanced high-performance bus.

## 1.5 Product category definition

Table 1 gives an overview of memory density versus product line.

The present reference manual describes the superset of features for each product category. Refer to
Table 2 for the list of features per category.

**Table 1. STM32G4 series memory density**

| Memory density | Category 2 | Category 3 | Category 4 |
| --- | --- | --- | --- |
| 32 KBytes | STM32G431 | - | - |
| 64 Kbytes | STM32G431 | - | - |
| 128 Kbytes | STM32G431; STM32G441 (AES) | STM32G471; STM32G473; STM32G474; STM32G484 (AES) | - |
| 256 Kbytes | - | STM32G471; STM32G473; STM32G474 | STM32G491 |
| 512 Kbytes | - | STM32G471; STM32G473; STM32G474; STM32G483 (AES); STM32G484 (AES) | STM32G491; STM32G4A1 (AES) |

## 1.6 Availability of peripherals

Table 2 summarizes the list of peripherals available in all the STM32G4xx products considering the
biggest package in every product.

For availability of peripherals and their number across all devices, refer to the particular device
datasheet.

**Table 2. Product specific features**

| Feature | STM32G474/; STM32G484 | STM32G473/; STM32G483 | STM32G471 | STM32G431/; STM32G441 | STM32G491/; STM32G4A1 |
| --- | --- | --- | --- | --- | --- |
| Flash | 512/256/128K,; Dual bank | 512/256/128K,; Dual bank | 512/256/128K,; Dual bank | 128/64/32K,; single bank | 512/256K,; single bank |
| SRAM1 | 80K, parity check; on the first 32K | 80K, parity check; on the first 32K | 80K, parity check; on the first 32K | 16K, parity check; on the whole SRAM1 | 80K, parity check; on the first 32K |
| SRAM2 | 16K, no parity; check | 16K, no parity; check | 16K, no parity; check | 6K, no parity; check | 16K, no parity; check |
| CCM SRAM | 32K, parity check; on the whole CCM SRAM | 32K, parity check; on the whole CCM SRAM | 16K, parity check; on the whole CCM SRAM | 10K, parity check; on the whole CCM SRAM | 16K, parity check; on the whole CCM SRAM |
| CRS | Yes | Yes | Yes | Yes | Yes |
| DMA | 2 DMA controllers:; DMA1: 8 channels; DMA2: 8 channels | 2 DMA controllers:; DMA1: 8 channels; DMA2: 8 channels | 2 DMA controllers:; DMA1: 8 channels; DMA2: 8 channels | 2 DMA controllers:; DMA1: 6 channels; DMA2: 6 channels | 2 DMA controllers:; DMA1: 8 channels; DMA2: 8 channels |
| DMAMUX | Yes | Yes | Yes | Yes | Yes |
| Cordic | Yes | Yes | Yes | Yes | Yes |
| FMAC | Yes | Yes | Yes | Yes | Yes |
| RNG | Yes | Yes | Yes | Yes | Yes |
| AES | Yes (Note) | Yes (Note) | No | Yes (Note) | Yes (Note) |
| CRC | Yes | Yes | Yes | Yes | Yes |
| FSMC | Yes | Yes | No | No | No |
| QUADSPI | Yes | Yes | Yes | No | Yes |
| ADC | 5 x ADC:; ADC1/2 can be used in dual mode; ADC3/4 can be used in dual mode; ADC5 usable only in single mode | 5 x ADC:; ADC1/2 can be used in dual mode; ADC3/4 can be used in dual mode; ADC5 usable only in single mode | 3 x ADC:; ADC1/2 can be used in dual mode; ADC3 usable only in single mode | 2 x ADC:; ADC1/2 can be used in dual mode | 3 x ADC:; ADC1/2 can be used in dual mode; ADC3 usable only in single mode |
| DAC | 7 DAC ch:; DAC1_CH1/; DAC1_CH2/; DAC2_CH1: external; DAC3_CH1/; DAC3/CH2/; DAC4_CH1/; DAC4_CH2: internal | 7 DAC ch:; DAC1_CH1/; DAC1_CH2/; DAC2_CH1: external; DAC3_CH1/; DAC3/CH2/; DAC4_CH1/; DAC4_CH2: internal | 4 DAC ch:; DAC1_CH1/; DAC1_CH2: external; DAC3_CH1/; DAC3/CH2: internal | 4 DAC ch:; DAC1_CH1/; DAC1_CH2: external; DAC3_CH1/; DAC3/CH2: internal | 4 DAC ch:; DAC1_CH1/; DAC1_CH2: external; DAC3_CH1/; DAC3/CH2: internal |
| COMP | 7 (COMP1..7) | 7 (COMP1..7) | 4 (COMP1..4) | 4 (COMP1..4) | 4 (COMP1..4) |
| OPAMP | 6 (OPAMP1..6) | 6 (OPAMP1..6) | 4 (OPAMP1.2,3,6) | 3 (OPAMP1..3) | 4 (OPAMP1.2,3,6) |
| VREFBUF | Yes | Yes | Yes | Yes | Yes |
| HRTIM1 | Yes | No | No | No | No |
| Advanced control timers (TIM1/TIM8/TIM20) | TIM1/8/20 | TIM1/8/20 | TIM1/8/20 | TIM1/8 | TIM1/8/20 |
| General purpose timers (TIM2/TIM3/TIM4/TIM5) | TIM2/3/4/5 | TIM2/3/4/5 | TIM2/3/4 | TIM2/3/4 | TIM2/3/4 |
| General purpose timers (TIM15/TIM16/TIM17) | TIM15/16/17 | TIM15/16/17 | TIM15/16/17 | TIM15/16/17 | TIM15/16/17 |
| Basic timers (TIM6/TIM7) | TIM6/7 | TIM6/7 | TIM6/7 | TIM6/7 | TIM6/7 |
| Low power timer (LPTIM1) | Yes | Yes | Yes | Yes | Yes |
| Infrared interface (IRTIM) | Yes | Yes | Yes | Yes | Yes |
| Independent watchdog (IWDG) | Yes | Yes | Yes | Yes | Yes |
| System window watchdog (WWDG) | Yes | Yes | Yes | Yes | Yes |
| RTC and TAMP | Yes | Yes | Yes | Yes | Yes |
| I2C | 4 x I2C (I2C1..4) | 4 x I2C (I2C1..4) | 4 x I2C (I2C1..4) | 3 x I2C (I2C1..3) | 3 x I2C (I2C1..3) |
| USART/UART | 3 x USART (USART1..3); 2 x UART (UART4,5) | 3 x USART (USART1..3); 2 x UART (UART4,5) | 3 x USART (USART1..3); 2 x UART (UART4,5) | 3 x USART (USART1..3); 1 x UART (UART4) | 3 x USART (USART1..3); 2 x UART (UART4,5) |
| LPUART | 1 x LPUART | 1 x LPUART | 1 x LPUART | 1 x LPUART | 1 x LPUART |
| SPI/I2S | 4 x SPI/2 x I2S; (SPI1..4 - I2S2,3) | 4 x SPI/2 x I2S; (SPI1..4 - I2S2,3) | 4 x SPI/2 x I2S; (SPI1..4 - I2S2,3) | 3 x SPI/2 x I2S; (SPI1..3 - I2S2,3) | 3 x SPI/2 x I2S; (SPI1..3 - I2S2,3) |
| SAI | 1 x SAI | 1 x SAI | 1 x SAI | 1 x SAI | 1 x SAI |
| FDCAN | 3 x FDCAN; (FDCAN1..3) | 3 x FDCAN; (FDCAN1..3) | 2 x FDCAN; (FDCAN1,2) | 1 x FDCAN; (FDCAN1) | 2 x FDCAN; (FDCAN1,2) |
| USB device | 1 x USB device | 1 x USB device | 1 x USB device | 1 x USB device | 1 x USB device |
| UCPD1 | 1 x UCPD | 1 x UCPD | 1 x UCPD | 1 x UCPD | 1 x UCPD |

> **Note:** The AES is available only on STM32G483xx, STM32G484xx, STM32G441x and STM32G4A1 devices.
