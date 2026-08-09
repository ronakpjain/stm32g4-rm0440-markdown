# 14 Nested vectored interrupt controller (NVIC)

[← RM0440 index](../STM32G4_RM0440.md)

## 14.1 NVIC main features

- 102 maskable interrupt channels (not including the sixteen Cortex®-M4 with FPU interrupt lines)
- 16 programmable priority levels (4 bits of interrupt priority are used)
- Low-latency exception and interrupt handling
- Power management control
- Implementation of system control registers

The NVIC and the processor core interface are closely coupled, which enables low latency interrupt
processing and efficient processing of late arriving interrupts.

All interrupts including the core exceptions are managed by the NVIC. For more information on
exceptions and NVIC programming, refer to the PM0214 programming manual for CortexTM-M4 products.

## 14.2 SysTick calibration value register

The SysTick calibration value is set to 0x3E8, which gives a reference time base of 1 ms with the
SysTick clock set to 125 KHz (1 MHz / 8).

## 14.3 Interrupt and exception vectors

The gray rows in Table 100 describe the vectors without specific position.

**Table 100. STM32G4 series vector table**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `Type of` |  |  |  |  |  |
| 2 | `Acronym` | `Description` | `Address` |  |  |  |
| 3 | `priority` |  |  |  |  |  |
| 4 | `Position Priority` |  |  |  |  |  |
| 5 | `-` | `-` | `-` | `-` | `Reserved` | `0x0000 0000` |
| 6 | `-` | `-3` | `Fixed` | `Reset` | `Reset` | `0x0000 0004` |
| 7 | `Non maskable interrupt. SRAM parity err + FLASH` |  |  |  |  |  |
| 8 | `-` | `-2` | `Fixed` | `NMI` | `0x0000 0008` |  |
| 9 | `ECC err + HSE CSS` |  |  |  |  |  |
| 10 | `-` | `-1` | `Fixed` | `HardFault` | `All classes of fault` | `0x0000 000C` |
| 11 | `-` | `0` | `Settable MemManage` | `Memory management` | `0x0000 0010` |  |
| 12 | `-` | `1` | `Settable BusFault` | `Pre-fetch fault, memory access fault` | `0x0000 0014` |  |
| 13 | `-` | `2` | `Settable UsageFault` | `Undefined instruction or illegal state` | `0x0000 0018` |  |
| 14 | `0x0000 001C` |  |  |  |  |  |
| 15 | `-` | `-` | `-` | `-` | `Reserved` |  |
| 16 | `-0x0000 0028` |  |  |  |  |  |
| 17 | `-` | `3` | `-` | `-` | `System service call via SWI instruction` | `0x0000 002C` |
| 18 | `-` | `4` | `-` | `-` | `Monitor` | `0x0000 0030` |
| 19 | `-` | `-` | `-` | `-` | `Reserved` | `0x0000 0034` |
| 20 | `-` | `5` | `Settable PendSV` | `Pendable request for system service` | `0x0000 0038` |  |
| 21 | `-` | `6` | `Settable SysTick` | `System tick timer` | `0x0000 003C` |  |
| 22 | `0` | `7` | `Settable WWDG` | `Window Watchdog interrupt` | `0x0000 0040` |  |
| 23 | `1` | `8` | `Settable PVD_PVM` | `PVD through EXTI line 16 interrupt` | `0x0000 0044` |  |
| 24 | `RTC/TAMP/CSS on LSE through EXTI line 19` |  |  |  |  |  |
| 25 | `2` | `9` | `Settable RTC/TAMP/CSS_LSE` | `0x0000 0048` |  |  |
| 26 | `interrupt` |  |  |  |  |  |
| 27 | `3` | `10` | `Settable RTC_WKUP` | `RTC wake-up timer through EXTI line 20 interrupt` | `0x0000 004C` |  |
| 28 | `4` | `11` | `Settable FLASH` | `Flash global interrupt` | `0x0000 0050` |  |
| 29 | `5` | `12` | `Settable RCC` | `RCC global interrupt` | `0x0000 0054` |  |
| 30 | `6` | `13` | `Settable EXTI0` | `EXTI Line0 interrupt` | `0x0000 0058` |  |
| 31 | `7` | `14` | `Settable EXTI1` | `EXTI Line1 interrupt` | `0x0000 005C` |  |
| 32 | `8` | `15` | `Settable EXTI2` | `EXTI Line2 interrupt` | `0x0000 0060` |  |
| 33 | `9` | `16` | `Settable EXTI3` | `EXTI Line3 interrupt` | `0x0000 0064` |  |
| 34 | `10` | `17` | `Settable EXTI4` | `EXTI Line4 interrupt` | `0x0000 0068` |  |
| 35 | `11` | `18` | `Settable DMA1_CH1` | `DMA1 channel 1 interrupt` | `0x0000 006C` |  |
| 36 | `12` | `19` | `Settable DMA1_CH2` | `DMA1 channel 2 interrupt` | `0x0000 0070` |  |
| 37 | `13` | `20` | `Settable DMA1_CH3` | `DMA1 channel 3 interrupt` | `0x0000 0074` |  |
| 38 | `14` | `21` | `Settable DMA1_CH4` | `DMA1 channel 4 interrupt` | `0x0000 0078` |  |

**Table 100. STM32G4 series vector table (continued)**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `Type of` |  |  |  |  |  |
| 2 | `Acronym` | `Description` | `Address` |  |  |  |
| 3 | `priority` |  |  |  |  |  |
| 4 | `Position Priority` |  |  |  |  |  |
| 5 | `15` | `22` | `Settable DMA1_CH5` | `DMA1 channel 5 interrupt` | `0x0000 007C` |  |
| 6 | `16` | `23` | `Settable DMA1_CH6` | `DMA1 channel 6 interrupt` | `0x0000 0080` |  |
| 7 | `17` | `24` | `Settable DMA1_CH7` | `DMA1 channel 7 interrupt` | `0x0000 0084` |  |
| 8 | `18` | `25` | `Settable ADC1_2` | `ADC1 and ADC2 global interrupt` | `0x0000 0088` |  |
| 9 | `19` | `26` | `Settable USB_HP` | `USB High priority interrupts` | `0x0000 008C` |  |
| 10 | `20` | `27` | `Settable USB_LP` | `USB Low priority interrupts` | `0x0000 0090` |  |
| 11 | `21` | `28` | `Settable FDCAN1_IT0` | `FDCAN1 interrupt 0` | `0x0000 0094` |  |
| 12 | `22` | `29` | `Settable FDCAN1_IT1` | `FDCAN1 interrupt1` | `0x0000 0098` |  |
| 13 | `23` | `30` | `Settable EXTI9_5` | `EXTI Line[9:5] interrupts` | `0x0000 009C` |  |
| 14 | `24` | `31` | `Settable TIM1_BRK/TIM15` | `TIM1 Break/TIM15 global interrupts` | `0x0000 00A0` |  |
| 15 | `25` | `32` | `Settable TIM1_UP/TIM16` | `TIM1 Update/TIM16 global interrupts` | `0x0000 00A4` |  |
| 16 | `TIM1_TRG_COM/` | `TIM1 trigger and commutation/TIM17` |  |  |  |  |
| 17 | `26` | `33` | `Settable` | `TIM17/TIM1_DIR/` | `interrupts/TIM1 Direction Change interrupt/TIM1` | `0x0000 00A8` |
| 18 | `TIM1_IDX` | `Index` |  |  |  |  |
| 19 | `27` | `34` | `Settable TIM1_CC` | `TIM1 capture compare interrupt` | `0x0000 00AC` |  |
| 20 | `28` | `35` | `Settable TIM2` | `TIM2 global interrupt` | `0x0000 00B0` |  |
| 21 | `29` | `36` | `Settable TIM3` | `TIM3 global interrupt` | `0x0000 00B4` |  |
| 22 | `30` | `37` | `Settable TIM4` | `TIM4 global interrupt` | `0x0000 00B8` |  |
| 23 | `31` | `38` | `Settable I2C1_EV` | `I2C1 event interrupt and EXTI line 23 interrupt` | `0x0000 00BC` |  |
| 24 | `32` | `39` | `Settable I2C1_ER` | `I2C1 error interrupt` | `0x0000 00C0` |  |
| 25 | `33` | `40` | `Settable I2C2_EV` | `I2C2 event interrupt and EXTI line 24 interrupt` | `0x0000 00C4` |  |
| 26 | `34` | `41` | `Settable I2C2_ER` | `I2C2 error interrupt` | `0x0000 00C8` |  |
| 27 | `35` | `42` | `Settable SPI1` | `SPI1 global interrupt` | `0x0000 00CC` |  |
| 28 | `36` | `43` | `Settable SPI2` | `SPI2 global interrupt` | `0x0000 00D0` |  |
| 29 | `37` | `44` | `Settable USART1` | `USART1 global interrupt and EXTI line 25` | `0x0000 00D4` |  |
| 30 | `38` | `45` | `Settable USART2` | `USART2 global interrupt and EXTI line 26` | `0x0000 00D8` |  |
| 31 | `39` | `46` | `Settable USART3` | `USART3 global interrupt and EXTI line 28` | `0x0000 00DC` |  |
| 32 | `40` | `47` | `Settable EXTI15_10` | `EXTI line[15:10] interrupts` | `0x0000 00E0` |  |
| 33 | `41` | `48` | `Settable RTC_ALARM` | `RTC alarms interrupts` | `0x0000 00E4` |  |
| 34 | `42` | `49` | `Settable USBWakeUP` | `USB wake-up from suspend (EXTI line 18)` | `0x0000 00E8` |  |
| 35 | `TIM8 Break interrupt/TIM8 Transition error/TIM8` |  |  |  |  |  |
| 36 | `43` | `50` | `Settable TIM8_BRK/TIM8_TERR` | `0x0000 00EC` |  |  |
| 37 | `/TIM8_IERR` | `Index error` |  |  |  |  |
| 38 | `44` | `51` | `Settable TIM8_UP` | `TIM8 Update interrupt` | `0x0000 00F0` |  |

**Table 100. STM32G4 series vector table (continued)**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `Type of` |  |  |  |  |
| 2 | `Acronym` | `Description` | `Address` |  |  |
| 3 | `priority` |  |  |  |  |
| 4 | `Position Priority` |  |  |  |  |
| 5 | `TIM8 trigger and commutation interrupt/TIM8` |  |  |  |  |
| 6 | `45` | `52` | `Settable TIM8_TRG_COM/TIM8` | `0x0000 00F4` |  |
| 7 | `_DIR/TIM8_IDX` | `Direction Change interrupt/TIM8 Index` |  |  |  |
| 8 | `46` | `53` | `Settable TIM8_CC` | `TIM8 capture compare interrupt` | `0x0000 00F8` |
| 9 | `47` | `54` | `Settable ADC3` | `ADC3 global interrupt` | `0x0000 00FC` |
| 10 | `48` | `55` | `Settable FSMC` | `FSMC global interrupt` | `0x0000 0100` |
| 11 | `49` | `56` | `Settable LPTIM1` | `LPTIM1 global interrupt` | `0x0000 0104` |
| 12 | `50` | `57` | `Settable TIM5` | `TIM5 global interrupt` | `0x0000 0108` |
| 13 | `51` | `58` | `Settable SPI3` | `SPI3 global interrupt` | `0x0000 010C` |
| 14 | `52` | `59` | `Settable UART4` | `UART4 global interrupt and EXTI line 34 interrupts` | `0x0000 0110` |
| 15 | `53` | `60` | `Settable UART5` | `UART5 global interrupt and EXTI line 35 interrupts` | `0x0000 0114` |
| 16 | `54` | `61` | `Settable TIM6_DACUNDER` | `TIM6 and DAC1/3 underrun global interrupts` | `0x0000 0118` |
| 17 | `55` | `62` | `Settable TIM7_DACUNDER` | `TIM7 and DAC2/4 underrun global interrupts` | `0x0000 011C` |
| 18 | `56` | `63` | `Settable DMA2_CH1` | `DMA2 channel 1 interrupt` | `0x0000 0120` |
| 19 | `57` | `64` | `Settable DMA2_CH2` | `DMA2 channel 2 interrupt` | `0x0000 0124` |
| 20 | `58` | `65` | `Settable DMA2_CH3` | `DMA2 channel 3 interrupt` | `0x0000 0128` |
| 21 | `59` | `66` | `Settable DMA2_CH4` | `DMA2 channel 4 interrupt` | `0x0000 012C` |
| 22 | `60` | `67` | `Settable DMA2_CH5` | `DMA2 channel 5 interrupt` | `0x0000 0130` |
| 23 | `61` | `68` | `Settable ADC4` | `ADC4 global interrupt` | `0x0000 0134` |
| 24 | `62` | `69` | `Settable ADC5` | `ADC5 global interrupt` | `0x0000 0138` |
| 25 | `63` | `70` | `Settable UCPD1 global interrupt` | `UCPD1 global interrupt and EXTI line 43` | `0x0000 013C` |
| 26 | `COMP1/COMP2/COMP3 through EXTI` |  |  |  |  |
| 27 | `64` | `71` | `Settable COMP1_2_3` | `0x0000 0140` |  |
| 28 | `lines 21/22/29 interrupts` |  |  |  |  |
| 29 | `COMP4/COMP5/COMP6 through EXTI` |  |  |  |  |
| 30 | `65` | `72` | `Settable COMP4_5_6` | `0x0000 0144` |  |
| 31 | `lines 30/31/32 interrupts` |  |  |  |  |
| 32 | `66` | `73` | `Settable COMP7` | `lobal interrupt COMP7 through EXTI line 33` | `0x0000 0148` |
| 33 | `67` | `74` | `Settable HRTIM_Master_IRQn` | `HRTIM master timer interrupt (hrtim_it1)` | `0x0000 014C` |
| 34 | `68` | `75` | `Settable HRTIM_TIMA_IRQn` | `HRTIM timer A interrupt (hrtim_it2)` | `0x0000 0150` |
| 35 | `69` | `76` | `Settable HRTIM_TIMB_IRQn` | `HRTIM timer B interrupt (hrtim_it3)` | `0x0000 0154` |
| 36 | `70` | `77` | `Settable HRTIM_TIMC_IRQn` | `HRTIM timer C interrupt (hrtim_it4)` | `0x0000 0158` |
| 37 | `71` | `78` | `Settable HRTIM_TIMD_IRQn` | `HRTIM timer D interrupt (hrtim_it5)` | `0x0000 015C` |
| 38 | `72` | `79` | `Settable HRTIM_TIME_IRQn` | `HRTIM timer E interrupt (hrtim_it6)` | `0x0000 0160` |
| 39 | `73` | `80` | `Settable HRTIM_TIM_FLT_IRQn` | `HRTIM fault interrupt (hrtim_it8)` | `0x0000 0164` |
| 40 | `74` | `81` | `Settable HRTIM_TIMF_IRQn` | `hrtim_it7 / HRTIM timer F interrupt` | `0x0000 0168` |
| 41 | `75` | `82` | `Settable CRS` | `CRS interrupt` | `0x0000 016C` |

**Table 100. STM32G4 series vector table (continued)**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `Type of` |  |  |  |  |
| 2 | `Acronym` | `Description` | `Address` |  |  |
| 3 | `priority` |  |  |  |  |
| 4 | `Position Priority` |  |  |  |  |
| 5 | `76` | `83` | `Settable SAI` | `SAI` | `0x0000 0170` |
| 6 | `TIM20_BRK/` |  |  |  |  |
| 7 | `TIM20 Break interrupt/TIM20 Transition` |  |  |  |  |
| 8 | `77` | `84` | `Settable` | `TIM20_TERR/` | `0x0000 0174` |
| 9 | `error/TIM20 Index error` |  |  |  |  |
| 10 | `TIM20_IERR` |  |  |  |  |
| 11 | `78` | `85` | `Settable TIM20_UP` | `TIM20 Update interrupt` | `0x0000 0178` |
| 12 | `TIM20 Trigger and commutation interrupt/TIM20` |  |  |  |  |
| 13 | `79` | `86` | `Settable TIM20_TRG_COM/` | `0x0000 017C` |  |
| 14 | `TIM20_DIR/TIM20_IDX` | `Direction Change interrupt/TIM20 Index` |  |  |  |
| 15 | `80` | `87` | `Settable TIM20_CC` | `TIM20 capture compare interrupt` | `0x0000 0180` |
| 16 | `81` | `88` | `Settable FPU` | `Floating point interrupt` | `0x0000 0184` |
| 17 | `82` | `89` | `Settable I2C4_EV` | `I2C4 event interrupt and EXTI line 42` | `0x0000_0188` |
| 18 | `83` | `90` | `Settable I2C4_ER` | `I2C4 error interrupt` | `0x0000_018C` |
| 19 | `84` | `91` | `Settable SPI4` | `SPI4 global interrupt` | `0x0000_0190` |
| 20 | `85` | `92` | `Settable AES` | `AES global interrupt` | `0x0000_0194` |
| 21 | `86` | `93` | `Settable FDCAN2_IT0` | `FDCAN2 Interrupt 0` | `0x0000_0198` |
| 22 | `87` | `94` | `Settable FDCAN2_IT1` | `FDCAN2 Interrupt 1` | `0x0000_019C` |
| 23 | `88` | `95` | `Settable FDCAN3_IT0` | `FDCAN3 Interrupt 0` | `0x0000_01A0` |
| 24 | `89` | `96` | `Settable FDCAN3_IT1` | `FDCAN3 Interrupt 0` | `0x0000_01A4` |
| 25 | `90` | `97` | `Settable RNG` | `RNG global interrupt` | `0x0000_01A8` |
| 26 | `91` | `98` | `Settable LPUART` | `LPUART global interrupt` | `0x0000_01AC` |
| 27 | `92` | `99` | `Settable I2C3_EV` | `I2C3 event and EXTI line 27 interrupts` | `0x0000_01B0` |
| 28 | `93` | `100 Settable I2C3_ER` | `I2C3 error interrupt` | `0x0000_01B4` |  |
| 29 | `94` | `101 Settable DMAMUX_OVR` | `DMAMUX overrun interrupt` | `0x0000_01B8` |  |
| 30 | `95` | `102 Settable QUADSPI` | `QUADSPI global interrupt` | `0x0000_01BC` |  |
| 31 | `96` | `103 Settable DMA1_CH8` | `DMA1 channel 8 interrupt` | `0x0000_01C0` |  |
| 32 | `97` | `104 Settable DMA2_CH6` | `DMA2 channel 6 interrupt` | `0x0000_01C4` |  |
| 33 | `98` | `105 Settable DMA2_CH7` | `DMA2 channel 7 interrupt` | `0x0000_01C8` |  |
| 34 | `99` | `106 Settable DMA2_CH8` | `DMA2 channel 8 interrupt` | `0x0000_01CC` |  |
| 35 | `100 107 Settable CORDIC` | `CORDIC interrupt` | `0x0000_01D0` |  |  |
| 36 | `101 108 Settable FMAC` | `FMAC interrupt` | `0x0000_01D4` |  |  |
