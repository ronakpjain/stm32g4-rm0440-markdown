# 50 Revision history

[← RM0440 index](../STM32G4_RM0440.md)

**Table 462. Document revision history**

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `Date` | `Revision` | `Changes` |
| 2 | `06-May-2019` | `1` | `Initial release.` |
| 3 | `Document convention section` |  |  |

- Updated Table 2: Product specific features.

System architecture section

- Updated [Section 2.1](chapter-02.md#21-system-architecture): System architecture replacing FMC by FSMC.
- Updated Figure 2: Memory map replacing FMC by FSMC.

Memory organization section

- Updated Table 3: Memory map and peripheral register boundary addresses
- Updated Table 2.4: Embedded SRAM SRAM2 (mapped at address 0x2000 4000).
- Updated Table 7: Flash module - 512/256/128 KB dual bank organization (64 bits
  read width).
- Updated Table 8: Flash module - 512/256/128 KB single bank organization (128 bits
  read width).

Power control section

- Updated [Section 6.1](chapter-06.md#61-power-supplies): Power supplies.

Reset and clock control section

- Updated Figure 17: Clock tree.

Updated FMC into FSMC in:

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `10-Oct-2019` | `2` | `– Section 7.4.10: AHB3 peripheral reset register (RCC_AHB3RSTR).` |

- [Section 7.4.16](chapter-07.md#7416-ahb3-peripheral-clock-enable-registerrcc_ahb3enr): AHB3 peripheral clock enable register(RCC_AHB3ENR).
- [Section 7.4.22](chapter-07.md#7422-ahb3-peripheral-clocks-enable-in-sleep-and-stop-modes-register-rcc_ahb3smenr): AHB3 peripheral clocks enable in Sleep and Stop modes register

(RCC_AHB3SMENR).

System controller configuration section

- Updated [Section 10.2.1](chapter-10.md#1021-syscfg-memory-remap-register-syscfg_memrmp): SYSCFG memory remap register (SYSCFG_MEMRMP)
  bits[2:0] description.

Peripherals interconnect matrix section

- Updated Table 84: Interconnect 11 on-chip source FLTxSRC[1:0] = 01 column.

Nested vectored interrupt controller section

- Updated Table 100: STM32G4 series vector table.

Flexible static memory controller (FSMC) section

- Updated [Section 19](chapter-19.md#19-flexible-static-memory-controller-fsmc): Flexible static memory controller (FSMC).

CORDIC co-processor (CORDIC) section

- Updated [Section 17](chapter-17.md#17-cordic-coprocessor-cordic): CORDIC coprocessor (CORDIC).

Analog digital converter (ADC) section

- Updated [Section 21.4.33](chapter-21.md#21433-monitoring-the-internal-voltage-reference): Monitoring the internal voltage reference.
- Updated Section: Sampling time control trigger mode.

**Table 462. Document revision history (continued)**

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `Date` | `Revision` | `Changes` |
| 2 | `Digital analog converter (DAC) section` |  |  |

- Updated [Section 22](chapter-22.md#22-digital-to-analog-converter-dac): Digital-to-analog converter (DAC).

Comparator section

- Updated [Section 24.6.2](chapter-24.md#2462-comp-register-map): COMP register map.

AES hardware accelerator (AES)

- Updated [Section 27](chapter-27.md#27-aes-hardware-accelerator-aes): AES hardware accelerator (AES).

USB power delivery interface (UCPD)section

| Source row | Column 1 | Column 2 |
| ---: | --- | --- |
| 1 | `10-Oct-2019` | `2 (cont’d)` |

- Updated [Section 46](chapter-46.md#46-usb-type-cusb-power-delivery-interface-ucpd): USB Type-C®/USB Power Delivery interface (UCPD).

Debug section

- Updated [Section 47.4.2](chapter-47.md#4742-flexible-swj-dp-pin-assignment): Flexible SWJ-DP pin assignment.
- Updated [Section 47.8.3](chapter-47.md#4783-sw-dp-state-machine-reset-idle-states-id-code): SW-DP state machine (reset, idle states, ID code) ID code
  by 0x2BA01477.
- Updated Table 459: Flexible TRACE pin assignment.
- Updated Table 447: JTAG debug port data registers.

Added Category 4 devices (STM32G491, STM32G4A1) in:

- Table 1: STM32G4 series memory density.
- Table 2: Product specific features.
- [Section 2.4](chapter-02.md#24-embedded-sram): Embedded SRAM.
- [Section 2.4.1](chapter-02.md#241-parity-check): Parity check.
- Table 4: CCM SRAM organization.
- [Section 2.5](chapter-02.md#25-flash-memory-overview): Flash memory overview.
- [Section 4](chapter-04.md#4-embedded-flash-memory-flash-for-category-4-devices): Embedded flash memory (FLASH) for category 4 devices.
- Table 92: DMAMUX instantiation.

Embedded Flash memory (FLASH) section:

Updated:

- Number of wait states according to CPU clock (HCLK) frequency tables for all
  categories.
- Table 11: Option byte organization.
- Table 21: Option byte organization.

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `26-Mar-2020` | `3` | `– Section 3.4.2: Option bytes programming ‘activating dual bank mode (switching from` |

DBANK=0 to DBANK=1)’ paragraph.

- [Section 4.7.6](chapter-04.md#476-flash-control-register-flash_cr): Flash control register (FLASH_CR) PNB[7:0] bits.
- ‘User and read protection option bytes’ and [Section 4.7.8](chapter-04.md#478-flash-option-register-flash_optr): Flash option register

(FLASH_OPTR) register description adding PB4_PUPEN bit.

- [Section 5.7.14](chapter-05.md#5714-flash-register-map): FLASH register map.

Power control section:

Updated:

- Table 38: Range 1 boost mode configuration removing the lower SYSCLK limits.
- [Section 6.4.2](chapter-06.md#642-power-control-register-2-pwr_cr2): Power control register 2 (PWR_CR2) PLS[2:0] bit description.

Reset and clock control section:

Updated:

- Figure 17: Clock tree.
- Table 51: RCC register map and reset values.

Peripherals interconnect matrix section:

- Updated Table 62: STM32G4 series peripherals interconnect matrix.

**Table 462. Document revision history (continued)**

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `Date` | `Revision` | `Changes` |
| 2 | `DMA request multiplexer (DMAMUX) section:` |  |  |

- Updated [Section 13.3.2](chapter-13.md#1332-dmamux-mapping): DMAMUX mapping;

Analog digital converter section:

Updated:

- [Section 21.2](chapter-21.md#212-adc-main-features): ADC main features.
- Figure 83: ADC clock scheme.
- Figure 86: ADC3 connectivity.
- [Section 21.4.7](chapter-21.md#2147-single-ended-and-differential-input-channels): Single-ended and differential input channels.

Comparator section:

Updated Figure 168: Comparator block diagram.

Operational amplifier section:

Updated:

- Table 204: Operational amplifier possible connection.
- [Section 25.3.7](chapter-25.md#2537-calibration): Calibration procedure.
- [Section 25.3.8](chapter-25.md#2538-timer-controlled-multiplexer-mode): Timer controlled Multiplexer mode procedure.

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `26-Mar-2020` | `3 (cont’d)` | `– Section 25.5.1: OPAMP1 control/status register (OPAMP1_CSR).` |

- [Section 25.5.2](chapter-25.md#2552-opamp2-controlstatus-register-opamp2_csr): OPAMP2 control/status register (OPAMP2_CSR).
- [Section 25.5.3](chapter-25.md#2553-opamp3-controlstatus-register-opamp3_csr): OPAMP3 control/status register (OPAMP3_CSR).
- [Section 25.5.4](chapter-25.md#2554-opamp4-controlstatus-register-opamp4_csr): OPAMP4 control/status register (OPAMP4_CSR).
- [Section 25.5.5](chapter-25.md#2555-opamp5-controlstatus-register-opamp5_csr): OPAMP5 control/status register (OPAMP5_CSR).
- [Section 25.5.6](chapter-25.md#2556-opamp6-controlstatus-register-opamp6_csr): OPAMP6 control/status register (OPAMP6_CSR).

FD controller area network section:

Updated [Section 44.4.7](chapter-44.md#4447-fdcan-nominal-bit-timing-and-prescaler-register-fdcan_nbtp): FDCAN nominal bit timing and prescaler register

(FDCAN_NBTP) note.

Debug support section:

Updated:

- [Section 47.4.3](chapter-47.md#4743-internal-pull-up-and-pull-down-on-jtag-pins): Internal pull-up and pull-down on JTAG pins.
- [Section 47.6.1](chapter-47.md#4761-mcu-device-id-code): MCU device ID code.
- [Section 47.6.2](chapter-47.md#4762-boundary-scan-tap): Boundary scan TAP.

Device electronic signature section:

- Added [Section 48.3](chapter-48.md#483-package-data-register): Package data register.

**Table 462. Document revision history (continued)**

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `Date` | `Revision` | `Changes` |
| 2 | `Embedded Flash memory (FLASH) section:` |  |  |
| 3 | `Updated:` |  |  |

- Table 9: Number of wait states according to CPU clock (HCLK) frequency.
- Table 19: Number of wait states according to CPU clock (HCLK) frequency.
- Table 29: Number of wait states according to CPU clock (HCLK) frequency.
- [Section 5.4.1](chapter-05.md#541-option-bytes-description): Option bytes description ‘Securable memory area option bytes’
  paragraph.

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `14-Apr-2020` | `4` | `– Section 5.7.13: Flash securable area register (FLASH_SEC1R).` |
| 2 | `Reset and clock control (RCC) section:` |  |  |
| 3 | `Updated:` |  |  |

- [Section 7.2.4](chapter-07.md#724-pll): PLL.
- [Section 7.4.4](chapter-07.md#744-pll-configuration-register-rcc_pllcfgr): PLL configuration register (RCC_PLLCFGR) PLLN[6:0] and PLLM[3:0]
  description.

High-resolution timer (HRTIM) section:

- Updated Section 27.3.1: General description.

Memory map section:

Updated Table 3: Memory map and peripheral register boundary addresses USB SRAM
to 1 Kbyte.

Updated Figure 2: Memory map.

Embedded Flash section:

Updated for category 3 devices:

- ‘User and read protection option bytes’ register bit 29,28 name at NRST_MODE.
- ‘Securable memory area Bank 1 option bytes’ register BOOT_LOCK description
  removing caution.
- [Section 3.7.17](chapter-03.md#3717-flash-securable-area-bank1-register-flash_sec1r): Flash securable area bank1 register (FLASH_SEC1R) BOOT_LOCK
  description.

Updated for category 4 devices:

- ‘User and read protection option bytes’ register bit 29,28 name at NRST_MODE.

| Source row | Column 1 | Column 2 |
| ---: | --- | --- |
| 1 | `20-Nov-2020` | `5` |

- ‘Securable memory area option bytes’ register BOOT_LOCK description removing
  caution.
- [Section 4.7.1](chapter-04.md#471-flash-access-control-register-flash_acr): Flash access control register (FLASH_ACR) reset value.
- [Section 4.7.13](chapter-04.md#4713-flash-securable-area-register-flash_sec1r): Flash securable area register (FLASH_SEC1R) BOOT_LOCK
  description.
- [Section 4.7.14](chapter-04.md#4714-flash-register-map): FLASH register map

Updated for category 2 devices:

- ‘User and read protection option bytes’ register bit 29,28 name at NRST_MODE.
- ‘Securable memory area option bytes’ register BOOT_LOCK description removing
  caution.
- [Section 5.7.13](chapter-05.md#5713-flash-securable-area-register-flash_sec1r): Flash securable area register (FLASH_SEC1R) BOOT_LOCK
  description.

Updated ‘rw’ to ‘r’ for all option bytes.

**Table 462. Document revision history (continued)**

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `Date` | `Revision` | `Changes` |
| 2 | `Replaced ‘default’ by ‘production value’ for RDP level 0 instead of RDP level 1 in:` |  |  |

- Table 12: Flash memory read protection status.
- Figure 4: Changing the read protection (RDP) level.
- Table 22: Flash memory read protection status.
- Figure 7: Changing the read protection (RDP) level.
- Table 32: Flash memory read protection status.
- Figure 10: Changing the read protection (RDP) level.

Power control (PWR) section:

Updated [Section 6.4.22](chapter-06.md#6422-power-control-register-pwr_cr5): Power control register (PWR_CR5).

Reset and clock control (RCC) section:

Updated

- [Section 7.2.11](chapter-07.md#7211-adc-clock): ADC clock.
- [Section 7.4.19](chapter-07.md#7419-apb2-peripheral-clock-enable-register-rcc_apb2enr): APB2 peripheral clock enable register (RCC_APB2ENR) SPI4EN bit
  description.

Peripherals interconnect matrix section:

- Updated Table 75: Interconnect 2.

DMA request multiplexer (DMAMUX) section:

Updated:

- [Section 13.3.2](chapter-13.md#1332-dmamux-mapping): DMAMUX mapping.
- [Section 13.6.1](chapter-13.md#1361-dmamux-request-line-multiplexer-channel-x-configuration-register-dmamux_cxcr): DMAMUX request line multiplexer channel x configuration register

(DMAMUX_CxCR).

Nested vectored interrupt controller (NVIC) section:

| Source row | Column 1 | Column 2 |
| ---: | --- | --- |
| 1 | `20-Nov-2020` | `5 (cont’d)` |

Updated Table 100: STM32G4 series vector table.

Analog-to-digital converters (ADC) section:

Updated [Section 21.2](chapter-21.md#212-adc-main-features): ADC main features.

High-resolution timer (HRTIM) section:

Updated:

- Table 223: EExFLTR[3:0] codes depending on UDM bit setting.
- Table 224: External events features.
- Section 27.3.8: External events global conditioning.
- Section 27.3.9: External event filtering in timing units.
- Section 27.5.28: HRTIM timer x output 1 reset register (HRTIM_RSTx1R) (x = A to F).
- Section 27.5.66: HRTIM ADC trigger 1 register (HRTIM_ADC1R).
- Section 27.5.67: HRTIM ADC trigger 2 register (HRTIM_ADC2R).
- Section 27.5.68: HRTIM ADC trigger 3 register (HRTIM_ADC3R) adding note.

General-purpose timers (TIM2/TIM3/TIM4/TIM5) section:

Updated Table 302: TIM2/TIM3/TIM4/TIM5 register map and reset values.

General purpose timers (TIM15/TIM16/TIM17):

Updated:

- [Section 31.8.19](chapter-31.md#31819-timx-option-register-1-timx_or1x--16-to-17): TIMx option register 1 (TIMx_OR1)(x = 16 to 17) address offset to

0x68.

- [Section 31.8.22](chapter-31.md#31822-tim16tim17-register-map): TIM16/TIM17 register map.

Debug support (DBG) section:

- Updated [Section 47.6.1](chapter-47.md#4761-mcu-device-id-code): MCU device ID code REV_ID[15:0] bits description.

**Table 462. Document revision history (continued)**

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `Date` | `Revision` | `Changes` |
| 2 | `Embedded Flash section:` |  |  |
| 3 | `Updated:` |  |  |

- [Section 3.5.3](chapter-03.md#353-write-protection-wrp): Write protection (WRP).
- [Section 3.5.4](chapter-03.md#354-securable-memory-area): Securable memory area.
- [Section 3.7.1](chapter-03.md#371-flash-access-control-register-flash_acr): Flash access control register (FLASH_ACR) reset value
- [Section 4.5.3](chapter-04.md#453-write-protection-wrp): Write protection (WRP).
- [Section 4.5.4](chapter-04.md#454-securable-memory-area): Securable memory area.
- [Section 5.4.1](chapter-05.md#541-option-bytes-description): Option bytes description securable memory area option bytes
  paragraph.
- [Section 5.5.3](chapter-05.md#553-write-protection-wrp): Write protection (WRP).
- [Section 5.5.4](chapter-05.md#554-securable-memory-area): Securable memory area.
- [Section 5.7.1](chapter-05.md#571-flash-access-control-register-flash_acr): Flash access control register (FLASH_ACR) reset value.

Filter math accelerator (FMAC) section:

Updated [Section 18.4](chapter-18.md#184-fmac-registers): FMAC registers

| Source row | Column 1 | Column 2 |
| ---: | --- | --- |
| 1 | `08-Feb-2021` | `6` |
| 2 | `Analog digital converter section:` |  |
| 3 | `Updated:` |  |

- Table 181: ADC register map and reset values for each ADC (offset = 0x000 for
  master ADC, 0x100 for slave ADC) ADC_CFGR2 address.
- [Section 21.7.6](chapter-21.md#2176-adc-sample-time-register-1-adc_smpr1): ADC sample time register 1 (ADC_SMPR1) SMPPLUS bit.

Operational amplifier (OPAMP) section:

- Updated Table 204: Operational amplifier possible connection.

USB Type-C™ / USB Power Delivery interface (UCPD) section:

Updated:

- [Section 46.8.3](chapter-46.md#4683-ucpd-control-register-ucpd_cr): UCPD control register (UCPD_CR).
- [Section 46.8.15](chapter-46.md#46815-ucpd-register-map): UCPD register map.

Removed UCPD configuration register 3 (UCPD_CFGR3).

Debug support (DBG) section:

Updated [Section 47.4.2](chapter-47.md#4742-flexible-swj-dp-pin-assignment): Flexible SWJ-DP pin assignment removing note.

**Table 462. Document revision history (continued)**

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `Date` | `Revision` | `Changes` |
| 2 | `Updated:` |  |  |

- Related documents
- [Section 2.2](chapter-02.md#22-memory-organization): Memory organization
- Table 7: Flash module - 512/256/128 KB dual bank organization (64 bits read width)
- Table 8: Flash module - 512/256/128 KB single bank organization (128 bits read
  width)
- [Section 3](chapter-03.md#3-embedded-flash-memory-flash-for-category-3-devices): Embedded flash memory (FLASH) for category 3 devices
- [Section 3.4.1](chapter-03.md#341-option-bytes-description): Option bytes description
- [Section 3.7.5](chapter-03.md#375-flash-status-register-flash_sr): Flash status register (FLASH_SR)
- [Section 3.7.8](chapter-03.md#378-flash-option-register-flash_optr): Flash option register (FLASH_OPTR)
- [Section 4](chapter-04.md#4-embedded-flash-memory-flash-for-category-4-devices): Embedded flash memory (FLASH) for category 4 devices
- [Section 4.4.1](chapter-04.md#441-option-bytes-description): Option bytes description
- [Section 4.7.5](chapter-04.md#475-flash-status-register-flash_sr): Flash status register (FLASH_SR)
- [Section 4.7.8](chapter-04.md#478-flash-option-register-flash_optr): Flash option register (FLASH_OPTR)
- Table 18: Flash module - 256/512 Kbytes organization (64 bits read width)
- Table 28: Flash module - 32/64/128 Kbytes organization (64-bit read width)
- [Section 5](chapter-05.md#5-embedded-flash-memory-flash-for-category-2-devices): Embedded flash memory (FLASH) for category 2 devices
- [Section 5.4.1](chapter-05.md#541-option-bytes-description): Option bytes description
- [Section 5.7.5](chapter-05.md#575-flash-status-register-flash_sr): Flash status register (FLASH_SR)
- [Section 5.7.8](chapter-05.md#578-flash-option-register-flash_optr): Flash option register (FLASH_OPTR)
- [Section 6.2.3](chapter-06.md#623-peripheral-voltage-monitoring-pvm): Peripheral Voltage Monitoring (PVM)
- [Section 6.4.2](chapter-06.md#642-power-control-register-2-pwr_cr2): Power control register 2 (PWR_CR2)

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `04-Feb-2022` | `7` | `– Table 51: RCC register map and reset values` |

- [Section 9.3.15](chapter-09.md#9315-using-pb8-as-gpio): Using PB8 as GPIO
- [Section 9.4.1](chapter-09.md#941-gpio-port-mode-register-gpiox_moder-x-a-to-g): GPIO port mode register (GPIOx_MODER) (x =A to G)
- [Section 10.2.2](chapter-10.md#1022-syscfg-configuration-register-1-syscfg_cfgr1): SYSCFG configuration register 1 (SYSCFG_CFGR1)
- Table 100: STM32G4 series vector table
- [Section 18.4.7](chapter-18.md#1847-fmac-write-data-register-fmac_wdata): FMAC write data register (FMAC_WDATA)
- [Section 18.4.8](chapter-18.md#1848-fmac-read-data-register-fmac_rdata): FMAC read data register (FMAC_RDATA)
- Figure 151: DMA requests in regular simultaneous mode when MDMA = 10
- Section 24.6.1: Comparator x control and status register (COMP_CxCSR)
- [Section 24.6.2](chapter-24.md#2462-comp-register-map): COMP register map
- [Section 25.3.7](chapter-25.md#2537-calibration): Calibration
- Section 27.5.68: HRTIM ADC trigger 3 register (HRTIM_ADC3R)
- Section 27.5.81: HRTIM fault input register 4 (HRTIM_FLTINR4)
- Table 245: HRTIM register map and reset values – common functions
- [Section 42.5.9](chapter-42.md#4259-data-transmission-and-reception-procedures): Data transmission and reception procedures
- Figure 546: Transfer bus diagrams for I2C target receiver (mandatory events only)
- Table 402: CAN subsystem I/O signals
- Figure 670: Message RAM configuration
- [Section 44.4.3](chapter-44.md#4443-fdcan-data-bit-timing-and-prescaler-register-fdcan_dbtp): FDCAN data bit timing and prescaler register (FDCAN_DBTP)

Added:

- [Section 21.5](chapter-21.md#215-adc-in-low-power-mode): ADC in low-power mode
- Table 177: Effect of low-power modes on the ADC
- [Section 31.4.18](chapter-31.md#31418-6-step-pwm-generation): 6-step PWM generation

**Table 462. Document revision history (continued)**

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `Date` | `Revision` | `Changes` |
| 2 | `Updated Section 2.2.2: Memory map and register boundary addresses, Section 3.5.1:` |  |  |
| 3 | `Read protection (RDP), Section 5.7.6: Flash control register (FLASH_CR),` |  |  |
| 4 | `Section 7.4.1: Clock control register (RCC_CR), Section 7.4.20: AHB1 peripheral clocks` |  |  |
| 5 | `enable in Sleep and Stop modes register (RCC_AHB1SMENR), Section 9.3: GPIO` |  |  |
| 6 | `functional description, Section 8.7.1: CRS control register (CRS_CR), Section 12.2:` |  |  |
| 7 | `DMA main features, Section 21.4.10: Constraints when writing the ADC control bits,` |  |  |
| 8 | `Section 21.7.16: ADC injected sequence register (ADC_JSQR), Section 24.5: COMP` |  |  |
| 9 | `interrupts, Section 28.2: Main features, Section 28.3.17: Fault protection,` |  |  |
| 10 | `Section 30.5.10: TIMx capture/compare mode register 2 [alternate] (TIMx_CCMR2)(x =` |  |  |
| 11 | `2 to 5), Section 31.7.3: TIM15 slave mode control register (TIM15_SMCR),` |  |  |
| 12 | `Section 37.3.4: Clock and prescalers, note in sections 37.6.18 and 37.6.19,` |  |  |
| 13 | `Section 41.4.2: LPUART signals, Section 42.3: I2S main features, Section 42.7.1: I2S` |  |  |
| 14 | `general description, Power-down (Sleep mode), Rx handling, Standard message ID` |  |  |
| 15 | `filtering, Extended message ID filtering, and Section 44.3.7: FIFO acknowledge` |  |  |

handling.

Updated User and read protection option bytes in sections 3, 4, and 5.

Reorganized description of registers in [Section 28](chapter-28.md#28-high-resolution-timer-hrtim): High-resolution timer (HRTIM) and
in [Section 43](chapter-43.md#43-serial-audio-interface-sai): Serial audio interface (SAI).

Updated Table 11: Option byte organization, Table 31: Option byte organization,

Table 51: RCC register map and reset values, Table 55: Effect of low-power modes on

CRS, Table 100: STM32G4 series vector table, tables 166 to 169, Table 198: VREFBUF

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `12-Feb-2024` | `8` | `register map and reset values, tables in Section 28.3.2: HRTIM pins and internal` |
| 2 | `signals, Table 260: HRTIM register map and reset values – common functions,` |  |  |
| 3 | `Table 402: CAN subsystem I/O signals, Table 424: Bulk double-buffering memory` |  |  |
| 4 | `buffers usage, and Table 441: Type-C sequence (source: 3A); cable/sink connected (Rd` |  |  |

on CC1; Ra on CC2).

Added footnote to Table 5: Boot modes.

Added Table 371: USART/UART input/output pins, Table 372: USART internal
input/output signals, Table 381: LPUART input/output pins, and Table 382: LPUART
internal input/output signals.

Updated figures in [Section 20](chapter-20.md#20-quad-spi-interface-quadspi): Quad-SPI interface (QUADSPI), Figure 83: ADC clock
scheme, figures 99 to 104, Figure 156: Dual-channel DAC block diagram, Figure 171:

Standalone mode: external gain setting mode, Figure 244: Latency to external events

(counter reset and output set), Figure 245: Latency to external events (output reset on
external event), Figure 385: General-purpose timer block diagram, Figure 591: LPUART
block diagram, Figure 543: Transfer bus diagrams for I2C target transmitter (mandatory
events only), Figure 546: Transfer bus diagrams for I2C target receiver (mandatory
events only), Figure 553: Transfer bus diagrams for I2C controller transmitter

(mandatory events only), Figure 556: Transfer bus diagrams for I2C controller receiver

(mandatory events only), Figure 529: Independent watchdog block diagram,

Figure 530: Watchdog block diagram, and Figure 663: CAN subsystem..

Added [Section 49](chapter-49.md#49-important-security-notice): Important security notice.

Minor text edits across the whole document.

**Table 462. Document revision history (continued)**

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `Date` | `Revision` | `Changes` |

Rearranged sequence of sections.

Updated Introduction. [Section 3.3.1](chapter-03.md#331-flash-memory-organization): Flash memory organization, [Section 3.4.1](chapter-03.md#341-option-bytes-description): Option
bytes description, Modifying user options, Flash securable area bank1 register (FLASH_SEC1R),
[Section 3.5.4](chapter-03.md#354-securable-memory-area): Securable memory area, [Section 3.7.17](chapter-03.md#3717-flash-securable-area-bank1-register-flash_sec1r): Flash
securable area bank1 register (FLASH_SEC1R), [Section 4.4.1](chapter-04.md#441-option-bytes-description): Option bytes
description, Modifying user options, [Section 4.5.6](chapter-04.md#456-forcing-boot-from-flash-memory): Forcing boot from flash memory,

[Section 4.7.12](chapter-04.md#4712-flash-wrp-area-b-address-register-flash_wrp1br): Flash WRP area B address register (FLASH_WRP1BR),

[Section 4.7.13](chapter-04.md#4713-flash-securable-area-register-flash_sec1r): Flash securable area register (FLASH_SEC1R), [Section 5.4.1](chapter-05.md#541-option-bytes-description): Option
bytes description, [Section 5.5.6](chapter-05.md#556-forcing-boot-from-flash-memory): Forcing boot from flash memory, [Section 5.7.12](chapter-05.md#5712-flash-wrp-area-b-address-register-flash_wrp1br): Flash

WRP area B address register (FLASH_WRP1BR), [Section 5.7.13](chapter-05.md#5713-flash-securable-area-register-flash_sec1r): Flash securable area
register (FLASH_SEC1R), [Section 7.1.2](chapter-07.md#712-system-reset): System reset, [Section 7.2.7](chapter-07.md#727-system-clock-sysclk-selection): System clock

(SYSCLK) selection. [Section 9.3.2](chapter-09.md#932-io-pin-alternate-function-multiplexer-and-mapping): I/O pin alternate function multiplexer and mapping,

[Section 15.5.6](chapter-15.md#1556-pending-register-1-exti_pr1): Pending register 1 (EXTI_PR1), [Section 15.5.12](chapter-15.md#15512-pending-register-2-exti_pr2): Pending register 2

(EXTI_PR2), Auto-injection mode, Analog watchdog filter for watchdog 1, ADC
configuration register (ADC_CFGR), [Section 22.4.11](chapter-22.md#22411-dac-sawtooth-wave-generation): DAC sawtooth wave generation,

[Section 22.4.13](chapter-22.md#22413-dac-channel-buffer-calibration): DAC channel buffer calibration, [Section 22.7.23](chapter-22.md#22723-dac-sawtooth-mode-register-dac_stmodr): DAC sawtooth mode

| Source row | Column 1 | Column 2 |
| ---: | --- | --- |
| 1 | `14-Mar-2025` | `9` |
| 2 | `register (DAC_STMODR), Section 40.5.7: USART baud rate generation, and` |  |

[Section 48.3](chapter-48.md#483-package-data-register): Package data register.

Replaced SQRx and JSQRx by ADC_SQRy and ADC_JSQR registers, when referring
to registers, JSQRi and SQRi registers by JSQi and SQi bits, when referring to bits in

[Section 21](chapter-21.md#21-analog-to-digital-converters-adc): Analog-to-digital converters (ADC).

Updated Table 1: STM32G4 series memory density, Table 28: Flash module -

32/64/128 Kbytes organization (64-bit read width), Table 99: DMAMUX register map
and reset values for category 3 and 4 devices, and Table 265: Interconnect to the
tim_ti3 input multiplexer.

Added footnote to [Section 13.6.1](chapter-13.md#1361-dmamux-request-line-multiplexer-channel-x-configuration-register-dmamux_cxcr): DMAMUX request line multiplexer channel x
configuration register (DMAMUX_CxCR) and Table 98: DMAMUX register map and
reset values for category 2 devices.

Updated Figure 17: Clock tree and Figure 379: Measuring time interval between edges
on three signals.

Minor text edits across the whole document.

IMPORTANT NOTICE – READ CAREFULLY

STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections,
enhancements, modifications, and
improvements to ST products and/or to this document at any time without notice. Purchasers should
obtain the latest relevant information on

ST products before placing orders. ST products are sold pursuant to ST’s terms and conditions of
sale in place at the time of order
acknowledgment.

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes
no liability for application assistance or
the design of purchasers’ products.

No license, express or implied, to any intellectual property right is granted by ST herein.

Resale of ST products with provisions different from the information set forth herein shall void any
warranty granted by ST for such product.

ST and the ST logo are trademarks of ST. For additional information about ST trademarks, refer to
[www.st.com/trademarks](https://www.st.com/trademarks). All other
product or service names are the property of their respective owners.

Information in this document supersedes and replaces information previously supplied in any prior
versions of this document.

© 2025 STMicroelectronics – All rights reserved
