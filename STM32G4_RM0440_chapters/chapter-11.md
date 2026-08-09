# 11 Peripherals interconnect matrix

[← RM0440 index](../STM32G4_RM0440.md)

## 11.1 Introduction

Several peripherals have direct connections between them.

This allows autonomous communication and or synchronization between peripherals, saving CPU
resources thus power supply consumption.

In addition, these hardware connections remove software latency and allow design of predictable
system.

Depending on peripherals, these interconnections can operate in Run, Sleep, Low-power run and sleep,
Stop 0 and Stop 1 modes.

## 11.2 Connection summary

**Table 62. STM32G4 series peripherals interconnect matrix(1) (2)**

| Source row | Extracted cells |
| ---: | --- |
| 1 | `Destination` |
| 2 | `Source` |
| 3 | `TIM1` · `TIM2` · `TIM3` · `TIM4` · `TIM5` · `TIM6` · `TIM7` · `TIM8` · `ADC1` · `ADC2` · `ADC3` · `ADC4` · `ADC5` · `DAC1` · `DAC2` · `DAC3` · `DAC4` · `IRTIM` |
| 4 | `TIM15` · `TIM16` · `TIM17` · `TIM20` · `HRTIM` |
| 5 | `LPTIM1` · `COMP1` · `COMP2` · `COMP3` · `COMP4` · `COMP5` · `COMP6` · `COMP7` |
| 6 | `OPAMP1` · `OPAMP2` · `OPAMP3` · `OPAMP4` · `OPAMP5` · `OPAMP6` |
| 7 | `TIM1` · `-` · `1` · `1` · `1` · `1` · `-` · `-` · `1` · `1` · `-` · `-` · `1` · `- 10` · `-` · `-` · `-` · `-` · `-` · `-` · `- 20 - 15 15 15 15 15 15 15` · `-` |
| 8 | `14 19 19 19 19 19 -` |
| 9 | `1 1` |
| 10 | `TIM2` · `1` · `-` · `-` · `-` · `-` · `1` · `1` · `-` · `-` · `1` · `- 10 19 19 19 19 19 -` · `-` · `-` · `-` · `-` · `- 20 20 20 20 15 15 15 - 15 15` · `-` · `-` |
| 11 | `2 2` |
| 12 | `1 1 1` |
| 13 | `TIM3` · `1` · `-` · `-` · `-` · `1` · `1` · `-` · `-` · `1` · `- 10 19 19 19 19 19 -` · `-` · `-` · `-` · `-` · `- 20 20 20 20 15 15 15 15 15 -` · `15` · `-` |
| 14 | `2 2 2` |
| 15 | `1 1` |
| 16 | `TIM4` · `1` · `-` · `1` · `-` · `-` · `1` · `1` · `-` · `-` · `1` · `-` · `- 19 19 19 19 19 -` · `-` · `-` · `-` · `-` · `- 20 20 20 20 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 17 | `2 2` |
| 18 | `1 1` |
| 19 | `TIM5` · `1` · `1` · `-` · `-` · `-` · `1` · `1` · `-` · `-` · `1` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 20 | `2 2` |
| 21 | `TIM6` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 10` · `-` · `-` · `-` · `-` · `- 20 20 20 20 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 22 | `13 19 19 19 19 19 -` |
| 23 | `TIM7` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 10` · `-` · `-` · `-` · `-` · `- 20 20 20 20 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 24 | `12 19 19 19 19 19 -` |
| 25 | `TIM8` · `1` · `1` · `1` · `1` · `1` · `-` · `-` · `-` · `1` · `-` · `-` · `1` · `-` · `- 19 19 19 19 19 -` · `-` · `-` · `-` · `-` · `- 20 20 - 20 15 15 15 15 15 15 15` · `-` |
| 26 | `TIM15` · `1` · `1` · `1` · `1` · `1` · `-` · `-` · `1` · `-` · `-` · `-` · `1` · `- 10 19 19 19 19 19 -` · `-` · `-` · `-` · `-` · `- 20 20 20 20 -` · `-` · `- 15 - 15 15` · `-` |
| 27 | `TIM16` · `1` · `1` · `1` · `1` · `1` · `-` · `-` · `1` · `1` · `-` · `-` · `1` · `- 12` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `16` |
| 28 | `13 19 19 -` |
| 29 | `TIM17` · `1` · `1` · `1` · `1` · `1` · `-` · `-` · `1` · `1` · `-` · `-` · `1` · `- 12` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `16` |
| 30 | `13 -` |
| 31 | `TIM20` · `1` · `1` · `1` · `1` · `1` · `-` · `-` · `1` · `1` · `-` · `-` · `1` · `-` · `- 19 19 19 19 19 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 15 15 15 15 15 15 15` · `-` |
| 32 | `LPTIM1` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 19 19 19 19 19 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 33 | `HRTIM` · `1` · `1` · `1` · `1` · `1` · `-` · `-` · `1` · `1` · `-` · `-` · `1` · `-` · `- 19 19 19 19 19 -` · `-` · `-` · `-` · `-` · `- 20 20 20 20 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 34 | `ADC1` · `2` · `-` · `2` · `-` · `-` · `-` · `-` · `2` · `-` · `-` · `-` · `-` · `- 10 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 35 | `ADC2` · `2` · `-` · `2` · `-` · `-` · `-` · `-` · `2` · `-` · `-` · `-` · `-` · `- 10 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 36 | `ADC3` · `2` · `-` · `-` · `-` · `-` · `-` · `-` · `2` · `-` · `-` · `-` · `2` · `- 10 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 37 | `ADC4` · `2` · `-` · `-` · `-` · `-` · `-` · `-` · `2` · `-` · `-` · `-` · `2` · `- 10 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 38 | `ADC5` · `2` · `-` · `-` · `-` · `-` · `-` · `-` · `2` · `-` · `-` · `-` · `2` · `- 10 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 39 | `T. Sensor` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 21 -` · `-` · `- 21 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 40 | `VBAT` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 21 - 21 - 21 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 41 | `VREFINT` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 21 - 21 21 21 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 23 23 23 23 23 23 23` · `-` |
| 42 | `OPAMP1` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 21` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 43 | `24 -` |
| 44 | `OPAMP2` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 21` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 45 | `24 -` |
| 46 | `21 21` |
| 47 | `OPAMP3` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 21` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 48 | `24 24 24 -` |
| 49 | `21` |
| 50 | `OPAMP4` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 21` · `- 21` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 51 | `24 - 24 24 -` |
| 52 | `OPAMP5` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 21` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 53 | `24 -` |

**Table 62. STM32G4 series peripherals interconnect matrix(1) (2) (continued)**

| Source row | Extracted cells |
| ---: | --- |
| 1 | `Destination` |
| 2 | `Source` |
| 3 | `TIM1` · `TIM2` · `TIM3` · `TIM4` · `TIM5` · `TIM6` · `TIM7` · `TIM8` · `ADC1` · `ADC2` · `ADC3` · `ADC4` · `ADC5` · `DAC1` · `DAC2` · `DAC3` · `DAC4` · `IRTIM` |
| 4 | `TIM15` · `TIM16` · `TIM17` · `TIM20` · `HRTIM` |
| 5 | `LPTIM1` · `COMP1` · `COMP2` · `COMP3` · `COMP4` · `COMP5` · `COMP6` · `COMP7` |
| 6 | `OPAMP1` · `OPAMP2` · `OPAMP3` · `OPAMP4` · `OPAMP5` · `OPAMP6` |
| 7 | `21` |
| 8 | `OPAMP6` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 21` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 9 | `24 24 - 21 24 -` |
| 10 | `22 22 22 22` |
| 11 | `DAC1` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 22` · `-` · `-` |
| 12 | `23 23 23 23 23 -` |
| 13 | `22` |
| 14 | `DAC2` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 22` · `-` |
| 15 | `23 23` |
| 16 | `22 22 22` |
| 17 | `DAC3` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 22` · `- 22` · `-` · `-` · `- 22` · `-` · `-` · `-` |
| 18 | `24 - 22` · `24 -` · `24 -` · `23` · `23` · `23` · `23 -` |
| 19 | `22` · `22` · `22` |
| 20 | `DAC4` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 22` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 22` · `-` |
| 21 | `24` · `24 -` · `23` · `23` · `23` |
| 22 | `HSE` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `4` · `4` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 23 | `LSE` · `-` · `2` · `-` · `-` · `4` · `-` · `-` · `-` · `4` · `4` · `4` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 24 | `HSI16` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 25 | `LSI` · `-` · `-` · `-` · `-` · `4` · `-` · `-` · `-` · `-` · `4` · `4` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 26 | `MCO` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `4` · `4` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 27 | `EXTI` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `- 19 19 19 19 19 -` · `-` · `-` · `-` · `-` · `- 20 20 20 20 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 28 | `RTC` · `-` · `-` · `-` · `-` · `4` · `-` · `-` · `-` · `-` · `4` · `4` · `- 17 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 29 | `2` · `2` · `2` · `2` |
| 30 | `2` |
| 31 | `3` · `3` · `2` · `2` · `3` · `3` · `3` |
| 32 | `3` · `3` · `3` |
| 33 | `COMP1` · `4` · `4` · `4` · `4` · `-` · `-` · `4` · `4` · `4` · `17 10` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 34 | `4` · `8` · `8` · `11 -` |
| 35 | `8` · `5` · `5` · `5` · `8` · `8` · `8` |
| 36 | `5` |
| 37 | `9` · `7` · `9` · `9` |
| 38 | `2` · `2` · `2` · `2` |
| 39 | `2` |
| 40 | `3` · `3` · `2` · `2` · `3` · `3` · `3` |
| 41 | `3` · `3` · `3` |
| 42 | `COMP2` · `4` · `4` · `4` · `4` · `-` · `-` · `4` · `5` · `4` · `17 10` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 43 | `4` · `8` · `8` · `11 -` |
| 44 | `8` · `5` · `5` · `5` · `8` · `8` · `8` |
| 45 | `5` |
| 46 | `9` · `7` · `9` · `9` |
| 47 | `2` · `2` · `2` · `2` |
| 48 | `2` |
| 49 | `3` · `3` · `2` · `2` · `3` · `3` · `3` |
| 50 | `3` · `3` · `3` |
| 51 | `COMP3` · `4` · `4` · `4` · `4` · `-` · `-` · `4` · `5` · `4` · `17 10` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 52 | `4` · `8` · `8` · `11 -` |
| 53 | `8` · `5` · `5` · `5` · `8` · `8` · `8` |
| 54 | `5` |
| 55 | `9` · `6` · `9` · `9` |
| 56 | `2` · `2` · `2` · `2` |
| 57 | `2` |
| 58 | `3` · `3` · `2` · `2` · `3` · `3` |
| 59 | `3` · `3` · `3` · `3` |
| 60 | `COMP4` · `4` · `4` · `4` · `4` · `-` · `-` · `4` · `4` · `17 10` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 61 | `4` · `8` · `8` · `8` · `11 -` |
| 62 | `8` · `5` · `5` · `5` · `8` · `8` |
| 63 | `5` |
| 64 | `9` · `6` · `9` · `9` |
| 65 | `2` |
| 66 | `2` · `2` · `2` · `2` |
| 67 | `2` · `4` · `2` · `3` · `3` |
| 68 | `3` · `3` · `3` · `3` · `3` |
| 69 | `COMP5` · `3` · `5` · `4` · `-` · `-` · `4` · `4` · `- 10` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 70 | `8` · `4` · `8` · `8` · `8` · `11 -` |
| 71 | `4` · `6` · `5` · `8` · `8` |
| 72 | `9` · `5` · `9` · `9` |

**Table 62. STM32G4 series peripherals interconnect matrix(1) (2) (continued)**

| Source row | Extracted cells |
| ---: | --- |
| 1 | `Destination` |
| 2 | `Source` |
| 3 | `TIM1` · `TIM2` · `TIM3` · `TIM4` · `TIM5` · `TIM6` · `TIM7` · `TIM8` · `ADC1` · `ADC2` · `ADC3` · `ADC4` · `ADC5` · `DAC1` · `DAC2` · `DAC3` · `DAC4` · `IRTIM` |
| 4 | `TIM15` · `TIM16` · `TIM17` · `TIM20` · `HRTIM` |
| 5 | `LPTIM1` · `COMP1` · `COMP2` · `COMP3` · `COMP4` · `COMP5` · `COMP6` · `COMP7` |
| 6 | `OPAMP1` · `OPAMP2` · `OPAMP3` · `OPAMP4` · `OPAMP5` · `OPAMP6` |
| 7 | `2` · `2` · `2` · `2` |
| 8 | `2` · `2` · `2` · `3` · `3` |
| 9 | `3` · `3` · `3` · `3` · `3` |
| 10 | `COMP6` · `3` · `4` · `4` · `-` · `-` · `5` · `5` · `- 10` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 11 | `8` · `4` · `8` · `8` · `8` · `11 -` |
| 12 | `5` · `5` · `5` · `8` · `8` |
| 13 | `9` · `5` · `9` · `9` |
| 14 | `2` · `2` · `2` · `3` · `2` |
| 15 | `2 2` |
| 16 | `3` · `2` · `3` · `3` · `4` · `3` · `3` · `3` |
| 17 | `COMP7` · `4` · `4` · `-` · `-` · `- 10` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |
| 18 | `8` · `3` · `4` · `8` · `5` · `8` · `8` · `8` · `11 -` |
| 19 | `5 5` |
| 20 | `9` · `5` · `9` · `8` · `9` |
| 21 | `SYST ERR 18 -` · `-` · `-` · `-` · `-` · `- 18 18 18 18 18 - 18 -` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` · `-` |

1. Numbers inside table link to corresponding interconnect number detailed in [Section 11.3](#113-interconnection-details):
   Interconnection details.
2. The “-” symbol in grayed cells means no interconnect.

## 11.3 Interconnection details

### 11.3.1 From timer (TIMx, HRTIM) to timer (TIMx)

**Table 63. Interconnect 1**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Timer input` | `Timer input trigger source assignment` |  |  |  |  |  |  |  |
| 2 | `trigger` |  |  |  |  |  |  |  |  |
| 3 | `signal` | `TIM1` | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM15` | `TIM20` |
| 4 | `timx_itr0` | `-` | `tim1_trgo` | `tim1_trgo` | `tim1_trgo` | `tim1_trgo` | `tim1_trgo` | `tim1_trgo` | `tim1_trgo` |
| 5 | `timx_itr1` | `tim2_trgo` | `-` | `tim2_trgo` | `tim2_trgo` | `tim2_trgo` | `tim2_trgo` | `tim2_trgo` | `tim2_trgo` |
| 6 | `timx_itr2` | `tim3_trgo` | `tim3_trgo` | `-` | `tim3_trgo` | `tim3_trgo` | `tim3_trgo` | `tim3_trgo` | `tim3_trgo` |
| 7 | `timx_itr3` | `tim4_trgo` | `tim4_trgo` | `tim4_trgo` | `-` | `tim4_trgo` | `tim4_trgo` | `tim4_trgo` | `tim4_trgo` |
| 8 | `timx_itr4` | `tim5_trgo` | `tim5_trgo` | `tim5_trgo` | `tim5_trgo` | `-` | `tim5_trgo` | `tim5_trgo` | `tim5_trgo` |
| 9 | `timx_itr5` | `tim8_trgo` | `tim8_trgo` | `tim8_trgo` | `tim8_trgo` | `tim8_trgo` | `-` | `tim8_trgo` | `tim8_trgo` |
| 10 | `timx_itr6` | `tim15_trgo` | `tim15_trgo` | `tim15_trgo` | `tim15_trgo tim15_trgo tim15_trgo -` | `tim15_trgo` |  |  |  |
| 11 | `timx_itr7` | `tim16_oc` | `tim16_oc` | `tim16_oc` | `tim16_oc` | `tim16_oc` | `tim16_oc` | `xtim16_oc` | `tim16_oc` |
| 12 | `timx_itr8` | `tim17_oc` | `tim17_oc` | `tim17_oc` | `tim17_oc` | `tim17_oc` | `tim17_oc` | `tim17_oc` | `tim17_oc` |
| 13 | `timx_itr9` | `tim20_trgo` | `tim20_trgo` | `tim20_trgo` | `tim20_trgo tim20_trgo tim20_trgo tim20_trgo -` |  |  |  |  |
| 14 | `hrtim_out_` | `hrtim_out_` | `hrtim_out_` | `hrtim_out_` | `hrtim_out_` | `hrtim_out_` | `hrtim_out_` | `hrtim_out_` |  |
| 15 | `timx_itr10` |  |  |  |  |  |  |  |  |
| 16 | `scout2` | `scout2` | `scout2` | `scout2` | `scout2` | `scout2` | `scout2` | `scout2` |  |

The HRTIM burst operation can be triggered by on chip event coming from other general purpose timer.

The burst mode controller counter can be clocked by general purpose timers as well as shown in the
Table 64.

**Table 64. Interconnect 12**

| Source row | Column 1 | Column 2 |
| ---: | --- | --- |
| 1 | `HRTIM Burst mode trigger event/ clock signal` |  |
| 2 | `HRTIM Burst mode trigger event/ clock signal` |  |
| 3 | `assignment` |  |
| 4 | `hrtim_bm_trg` | `tim7_trgo` |
| 5 | `hrtim_bm_ck1` | `tim16_oc` |
| 6 | `hrtim_bm_ck2` | `tim17_oc` |
| 7 | `hrtim_bm_ck3` | `tim7_trgo‘` |

**Table 65. Interconnect 13**

| HRTIM update enable signal | HRTIM update enable assignment |
| --- | --- |
| hrtim_upd_en1 | tim16_oc |
| hrtim_upd_en2 | tim17_oc |
| hrtim_upd_en3 | tim6_oc |

The HRTIM can be synchronized by external sources as shown in the Table 66.

**Table 66. Interconnect 14**

| HRTIM synchronization signals | HRTIM synchronization signal assignment |
| --- | --- |
| hrtim_in_sync2 | tim1_trgo |
| hrtim_in_sync3 | HRTIM_SCIN |

Some of the TIMx timers are linked together internally for timer synchronization or chaining.

When one timer is configured in Master Mode, it can reset, start, stop or clock the counter of
another timer configured in Slave Mode.

A description of the feature is provided in: [Section 29.3.30](chapter-29.md#29330-timer-synchronization): Timer synchronization.

The modes of synchronization are detailed in:

- [Section 29.3.30](chapter-29.md#29330-timer-synchronization): Timer synchronization for advanced-control timers (TIM1/TIM8/TIM20)
- [Section 30.4.23](chapter-30.md#30423-timer-synchronization): Timer synchronization for general-purpose timers (TIM2/TIM3/TIM4/TIM5)
- [Section 31.4.26](chapter-31.md#31426-timer-synchronization-tim15-only): Timer synchronization (TIM15 only) for general-purpose timer (TIM15)

#### Triggering signals

The output (from Master) is on signal TIMx_TRGO (and TIMx_TRGO2 for TIM1/TIM8/TIM20) following a
configurable timer event.

The input (to slave) is on signals TIMx_ITRx

The input and output signals for TIM1/TIM8/TIM20 are shown in Figure 296: Advanced-control timer
block diagram.

The possible master/slave connections are given in:

- Table 267: Internal trigger connection

#### Active power mode

Run, Sleep, Low-power run, Low-power sleep.

### 11.3.2 From timer (TIMx, HRTIM) and EXTI to ADC (ADCx)

**Table 67. Interconnect 19**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `ADC triggers signals assignment` |  |  |  |  |
| 2 | `ADC trigger selection` |  |  |  |  |
| 3 | `EXTSEL[4:0] or` | `ADC1/2` | `ADC3/4/5` |  |  |
| 4 | `JEXTSEL[4:0]` |  |  |  |  |
| 5 | `Regular` | `Injected` | `Regular` | `Injected` |  |
| 6 | `0` | `tim1_cc1` | `tim1_trgo` | `tim3_cc1` | `tim1_trgo` |
| 7 | `1` | `tim1_cc2` | `tim1_cc4` | `tim2_cc3` | `tim1_cc4` |
| 8 | `2` | `tim1_cc3` | `tim2_trgo` | `tim1_cc3` | `tim2_trgo` |
| 9 | `3` | `tim2_cc2` | `tim2_cc1` | `tim8_cc1` | `tim8_cc2` |
| 10 | `4` | `tim3_trgo` | `tim3_cc4` | `tim3_trgo` | `tim4_cc3` |
| 11 | `5` | `tim4_cc4` | `tim4_trgo` | `exti2` | `tim4_trgo` |
| 12 | `6` | `exti11` | `exti15` | `tim4_cc1` | `tim4_cc4` |
| 13 | `7` | `tim8_trgo` | `tim8_cc4` | `tim8_trgo` | `tim8_cc4` |
| 14 | `8` | `tim8_trgo2` | `tim1_trgo2` | `tim8_trgo2` | `tim1_trgo2` |
| 15 | `9` | `tim1_trgo` | `tim8_trgo` | `tim1_trgo` | `tim8_trgo` |
| 16 | `10` | `tim1_trgo2` | `tim8_trgo2` | `tim1_trgo2` | `tim8_trgo2` |
| 17 | `11` | `tim2_trgo` | `tim3_cc3` | `tim2_trgo` | `tim1_cc3` |
| 18 | `12` | `tim4_trgo` | `tim3_trgo` | `tim4_trgo` | `tim3_trgo` |
| 19 | `13` | `tim6_trgo` | `tim3_cc1` | `tim6_trgo` | `exti3` |
| 20 | `14` | `tim15_trgo` | `tim6_trgo` | `tim15_trgo` | `tim6_trgo` |
| 21 | `15` | `tim3_cc4` | `tim15_trgo` | `tim2_cc1` | `tim15_trgo` |
| 22 | `16` | `tim20_trgo` | `tim20_trgo` | `tim20_trgo` | `tim20_trgo` |
| 23 | `17` | `tim20_trgo2` | `tim20_trgo2` | `tim20_trgo2` | `tim20_trgo2` |
| 24 | `18` | `tim20_cc1` | `tim20_cc4` | `tim20_cc1` | `tim20_cc2` |
| 25 | `19` | `tim20_cc2` | `hrtim_adc_trg2` | `hrtim_adc_trg2` | `hrtim_adc_trg2` |

**Table 67. Interconnect 19 (continued)**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `ADC triggers signals assignment` |  |  |  |  |
| 2 | `ADC trigger selection` |  |  |  |  |
| 3 | `EXTSEL[4:0] or` | `ADC1/2` | `ADC3/4/5` |  |  |
| 4 | `JEXTSEL[4:0]` |  |  |  |  |
| 5 | `Regular` | `Injected` | `Regular` | `Injected` |  |
| 6 | `20` | `tim20_cc3` | `hrtim_adc_trg4` | `hrtim_adc_trg4` | `hrtim_adc_trg4` |
| 7 | `21` | `hrtim_adc_trg1` | `hrtim_adc_trg5` | `hrtim_adc_trg1` | `hrtim_adc_trg5` |
| 8 | `22` | `hrtim_adc_trg3` | `hrtim_adc_trg6` | `hrtim_adc_trg3` | `hrtim_adc_trg6` |
| 9 | `23` | `hrtim_adc_trg5` | `hrtim_adc_trg7` | `hrtim_adc_trg5` | `hrtim_adc_trg7` |
| 10 | `24` | `hrtim_adc_trg6` | `hrtim_adc_trg8` | `hrtim_adc_trg6` | `hrtim_adc_trg8` |
| 11 | `25` | `hrtim_adc_trg7` | `hrtim_adc_trg9` | `hrtim_adc_trg7` | `hrtim_adc_trg9` |
| 12 | `26` | `hrtim_adc_trg8` | `hrtim_adc_trg10` | `hrtim_adc_trg8` | `hrtim_adc_trg10` |
| 13 | `27` | `hrtim_adc_trg9` | `TIM16_CC1` | `hrtim_adc_trg9` | `hrtim_adc_trg1` |
| 14 | `28` | `hrtim_adc_trg10` | `-` | `hrtim_adc_trg10` | `hrtim_adc_trg3` |
| 15 | `29` | `lptim_out` | `lptim_out` | `lptim_out` | `lptim_out` |
| 16 | `30` | `tim7_trgo` | `tim7_trgo` | `tim7_trgo` | `tim7_trgo` |
| 17 | `31` | `-` | `-` | `-` | `-` |

Timers (TIMx, HRTIM) can be used to generate an ADC triggering event.

TIMx synchronization is described in: [Section 29.3.31](chapter-29.md#29331-adc-triggers): ADC triggers (TIM1/TIM8).

ADC synchronization is described in: [Section 21.4.18](chapter-21.md#21418-conversion-on-external-trigger-and-trigger-polarity-extsel-exten-jextsel-jexten): Conversion on external trigger and trigger
polarity (EXTSEL, EXTEN, JEXTSEL, JEXTEN).

#### Triggering signals

The output (from timer) is on signal TIMx_TRGO, TIMx_TRGO2 or TIMx_CCx event.

The input (to ADC) is on signal EXT[15:0], JEXT[15:0].

The connection between timers and ADC is provided in:

- Table 166: ADC1/2 - External triggers for regular channels
- Table 167: ADC1/2 - External trigger for injected channels

#### Active power mode

Run, Sleep, Low-power run, Low-power sleep.

### 11.3.3 From ADC (ADCx) to timer (TIMx, HRTIM)

See please Table 75: Interconnect 2 and Table 83.: Interconnect 10

ADCs Analog watchdogs are connected to TIM1/8/20 for digital power applications (cycle-bycycle
current regulation with ADC).

A description of the ADC analog watchdog setting is provided in: [Section 21.4.28](chapter-21.md#21428-analog-window-watchdog-awd1en-jawd1en-awd1sgl-awd1ch-awd2ch-awd3ch-awd_htx-awd_ltx-awdx): Analog window
watchdog (AWD1EN, JAWD1EN, AWD1SGL, AWD1CH, AWD2CH, AWD3CH, AWD_HTx, AWD_LTx, AWDx).

Trigger settings on the timer are provided in: [Section 29.3.6](chapter-29.md#2936-external-trigger-input): External trigger input.

#### Triggering signals

The output (from ADC) is on signals ADCn_AWDx_OUT and the input (to timer) on signal TIMx_ETR
(external trigger) or hrtim_eevx[4:1].

#### Active power mode

Run, Sleep, Low-power run, Low-power sleep.

### 11.3.4 From timer (TIMx, HRTIM) and EXTI to DAC (DACx)

**Table 68. Interconnect 20**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `DAC trigger` | `DAC triggers signals assignment` |  |  |  |  |  |  |  |
| 2 | `selection` |  |  |  |  |  |  |  |  |
| 3 | `DAC1` | `DAC2` | `DAC3` | `DAC4` |  |  |  |  |  |
| 4 | `(TSELx[3:0],` |  |  |  |  |  |  |  |  |
| 5 | `STRSTTRIG` | `Update/` | `Update/` | `Update` | `Update/` |  |  |  |  |
| 6 | `Inc` | `Inc` | `Inc` | `Inc` |  |  |  |  |  |
| 7 | `SELx[3:0])` | `reset` | `reset` | `/reset` | `reset` |  |  |  |  |
| 8 | `0` | `sw` | `-` | `sw` | `-` | `sw` | `-` | `sw` | `-` |
| 9 | `1` | `tim8_trgo` | `tim8_trgo` | `tim8_trgo` | `tim8_trgo` | `tim1_trgo` | `tim1_trgo` | `tim8_trgo` | `tim8_trgo` |
| 10 | `2` | `tim7_trgo` | `tim7_trgo` | `tim7_trgo` | `tim7_trgo` | `tim7_trgo` | `tim7_trgo` | `tim7_trgo` | `tim7_trgo` |
| 11 | `3` | `tim15_trgo` | `tim15_trgo` | `tim15_trgo` | `tim15_trgo tim15_trgo` | `tim15_trgo` | `tim15_trgo` | `tim15_trgo` |  |
| 12 | `4` | `tim2_trgo` | `tim2_trgo` | `tim2_trgo` | `tim2_trgo` | `tim2_trgo` | `tim2_trgo` | `tim2_trgo` | `tim2_trgo` |
| 13 | `5` | `tim4_trgo` | `tim4_trgo` | `tim4_trgo` | `tim4_trgo` | `tim4_trgo` | `tim4_trgo` | `tim4_trgo` | `tim4_trgo` |
| 14 | `6` | `exti9` | `exti10` | `exti9` | `exti10` | `exti9` | `exti10` | `exti9` | `exti10` |
| 15 | `7` | `tim6_trgo` | `tim6_trgo` | `tim6_trgo` | `tim6_trgo` | `tim6_trgo` | `tim6_trgo` | `tim6_trgo` | `tim6_trgo` |
| 16 | `8` | `tim3_trgo` | `tim3_trgo` | `tim3_trgo` | `tim3_trgo` | `tim3_trgo` | `tim3_trgo` | `tim3_trgo` | `tim3_trgo` |
| 17 | `hrtim_dac` | `hrtim_dac` |  |  |  |  |  |  |  |
| 18 | `hrtim_dac_` | `hrtim_step` | `hrtim_dac_` | `hrtim_step` | `hrtim_step` | `hrtim_step` |  |  |  |
| 19 | `9` | `_reset_trg` | `_reset_trg` |  |  |  |  |  |  |
| 20 | `reset_trg1` | `_trig1` | `reset_trg1` | `_trig1` | `_trig1` | `_trig1` |  |  |  |
| 21 | `1` | `1` |  |  |  |  |  |  |  |
| 22 | `hrtim_dac` |  |  |  |  |  |  |  |  |
| 23 | `hrtim_dac_` | `hrtim_step` | `hrtim_dac_` | `hrtim_step` | `hrtim_stept` | `hrtim_rst_` | `hrtim_step` |  |  |
| 24 | `10` | `_reset_trg` |  |  |  |  |  |  |  |
| 25 | `reset_trg2` | `_trig2` | `reset_trg2` | `_trig2` | `rig_2` | `_trig_2` | `_trig2` |  |  |
| 26 | `2` |  |  |  |  |  |  |  |  |
| 27 | `hrtim_dac` | `hrtim_dac` |  |  |  |  |  |  |  |
| 28 | `hrtim_dac_` | `hrtim_step` | `hrtim_dac_` | `hrtim_step` | `hrtim_step` | `hrtim_step` |  |  |  |
| 29 | `11` | `_reset_trg` | `_reset_trg` |  |  |  |  |  |  |
| 30 | `reset_trg3` | `_trig3` | `reset_trg3` | `_trig3` | `_trig3` | `_trig3` |  |  |  |
| 31 | `3` | `3` |  |  |  |  |  |  |  |

**Table 68. Interconnect 20 (continued)**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `DAC triggers signals assignment` |  |  |  |  |  |
| 2 | `DAC trigger` |  |  |  |  |  |
| 3 | `selection` |  |  |  |  |  |
| 4 | `DAC1` | `DAC2` | `DAC3` | `DAC4` |  |  |
| 5 | `(TSELx[3:0],` |  |  |  |  |  |
| 6 | `STRSTTRIG` | `Update/` | `Update/` | `Update` | `Update/` |  |
| 7 | `Inc` | `Inc` | `Inc` | `Inc` |  |  |
| 8 | `SELx[3:0])` | `reset` | `reset` | `/reset` | `reset` |  |
| 9 | `hrtim_dac` | `hrtim_dac` |  |  |  |  |
| 10 | `hrtim_dac_` | `hrtim_step` | `hrtim_dac_` | `hrtim_step` | `hrtim_step` | `hrtim_step` |
| 11 | `12` | `_reset_trg` | `_reset_trg` |  |  |  |
| 12 | `reset_trg4` | `_trig4` | `reset_trg4` | `_trig4` | `_trig4` | `_trig4` |
| 13 | `4` | `4` |  |  |  |  |
| 14 | `hrtim_dac` | `hrtim_dac` |  |  |  |  |
| 15 | `hrtim_dac_` | `hrtim_step` | `hrtim_dac_` | `hrtim_step` | `hrtim_step` | `hrtim_step` |
| 16 | `13` | `_reset_trg` | `_reset_trg` |  |  |  |
| 17 | `reset_trg5` | `_trig5` | `reset_trg5` | `_trig5` | `_trig5` | `_trig5` |
| 18 | `5` | `5` |  |  |  |  |
| 19 | `hrtim_dac` | `hrtim_dac` |  |  |  |  |
| 20 | `hrtim_dac_` | `hrtim_step` | `hrtim_dac_` | `hrtim_step` | `hrtim_step` | `hrtim_step` |
| 21 | `14` | `_reset_trg` | `_reset_trg` |  |  |  |
| 22 | `reset_trg6` | `_trig6` | `reset_trg6` | `_trig6` | `_trig6` | `_trig6` |
| 23 | `6` | `6` |  |  |  |  |
| 24 | `hrtim_dac_` | `hrtim_dac_` | `hrtim_dac` | `hrtim_dac` |  |  |
| 25 | `15` | `-` | `-` | `-` | `-` |  |
| 26 | `trg1` | `trg2` | `_trg3` | `_trg1` |  |  |

Timers (TIMx, HRTIM) and EXTI can be used as triggering event to start a DAC conversion.

#### Triggering signals

The output (from timer) is on signal TIMx_TRGO directly connected to corresponding DAC inputs.

Selection of input triggers on DAC is provided in [Section 22.4.7](chapter-22.md#2247-dac-trigger-selection): DAC trigger selection (single and
dual mode).

#### Active power mode

Run, Sleep, Low-power run, Low-power sleep.

### 11.3.5 From HSE, LSE, LSI, HSI16, MCO, RTC to timer (TIMx)

See please Table 77: Interconnect 4 and Table 75: Interconnect 2

External clocks (HSE, LSE), internal clocks (LSI, HSI16), microcontroller output clock (MCO), GPIO
and RTC wakeup interrupt can be used as input to timer (TIMx).

This allows to calibrate the HSI16 and precisely measure the LSI oscillator frequency.

When Low Speed External (LSE) oscillator is used, no additional hardware connections are required.

This feature is described in [Section 7.2.16](chapter-07.md#7216-internalexternal-clock-measurement-with-tim5tim15tim16tim17): Internal/external clock measurement with
TIM5/TIM15/TIM16/TIM17.

#### Active power mode

Run, Sleep, Low-power run, Low-power sleep.

### 11.3.6 From RTC, COMPx to low-power timer (LPTIM1)

**Table 69. Interconnect 17**

| LPTIM trigger input signal (TRIGSEL[3:0]) | LPTIM1 trigger source assignment |
| --- | --- |
| lptim1_ext_trig0 | LPTIM1_ETR |
| lptim1_ext_trig1 | rtc_alra_trg |
| lptim1_ext_trig2 | rtc_alrb_trg |
| lptim1_ext_trig3 | RTC_TAMP1 |
| lptim1_ext_trig4 | RTC_TAMP2 |
| lptim1_ext_trig5 | RTC_TAMP3 |
| lptim1_ext_trig6 | comp1_out |
| lptim1_ext_trig7 | comp2_out |
| lptim1_ext_trig8 | comp3_out |
| lptim1_ext_trig9 | comp4_out |
| lptim1_ext_trig10 | comp5_out |
| lptim1_ext_trig11 | comp6_out |
| lptim1_ext_trig12 | comp7_out |

RTC alarm A/B, RTC_TAMP1/2/3 input detection, COMPx_OUT can be used as trigger to start LPTIM
counters (LPTIM1).

#### Triggering signals

This trigger feature is described in [Section 33.4.6](chapter-33.md#3346-trigger-multiplexer): Trigger multiplexer (and following sections).

The input selection is described in Table 327: LPTIM1 external trigger connection.

#### Active power mode

Run, Sleep, Low-power run, Low-power sleep, Stop 0, Stop 1.

### 11.3.7 From timer (TIMx) to comparators (COMPx)

**Table 70. Interconnect 15**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Comparator blanking source assignment` |  |  |  |  |  |  |  |
| 2 | `Comparator blanking` |  |  |  |  |  |  |  |
| 3 | `signal BLANKSEL[2:0]` |  |  |  |  |  |  |  |
| 4 | `COMP1` | `COMP2` | `COMP3` | `COMP4` | `COMP5` | `COMP6` | `COMP7` |  |
| 5 | `1` | `tim1_oc5` | `tim1_oc5` | `tim1_oc5` | `tim3_oc4` | `tim2_oc3` | `tim8_oc5` | `tim1_oc5` |
| 6 | `2` | `tim2_oc3` | `tim2_oc3` | `tim3_oc3` | `tim8_oc5` | `tim8_oc5` | `tim2_oc4` | `tim8_oc5` |
| 7 | `3` | `tim3_oc3` | `tim3_oc3` | `tim2_oc4` | `tim15_oc1` | `tim3_oc3` | `tim15_oc2` | `tim3_oc3` |
| 8 | `4` | `tim8_oc5` | `tim8_oc5` | `tim8_oc5` | `tim1_oc5` | `tim1_oc5` | `tim1_oc5` | `tim15_oc2` |
| 9 | `5` | `tim20_oc5` | `tim20_oc5` | `tim20_oc5` | `tim20_oc5` | `tim20_oc5` | `tim20_oc5` | `tim20_oc5` |
| 10 | `6` | `tim15_oc1` | `tim15_oc1` | `tim15_oc1` | `tim15_oc1` | `tim15_oc1` | `tim15_oc1` | `tim15_oc1` |
| 11 | `7` | `tim4_oc3` | `tim4_oc3` | `tim4_oc3` | `tim4_oc3` | `tim4_oc3` | `tim4_oc3` | `tim4_oc3` |
| 12 | `Timers (TIMx) can be used as blanking window to COMPx (x = 1...7)` |  |  |  |  |  |  |  |

The blanking function is described in [Section 24.3.6](chapter-24.md#2436-comp-output-blanking): COMP output blanking.

The blanking sources are given in comparators control and status register (COMP_CxCSR) bits
BLANKSEL[2:0].

#### Triggering signals

Timer output signal TIMx_Ocx are the inputs to blanking source of COMPx.

#### Active power mode

Run, Sleep, Low-power run, Low-power sleep.

### 11.3.8 From internal analog source to ADC (ADCx), comparator (COMPx) and OPAMP (OPAMPx)

Table 71 provides the ADC channels mapping on GPIOs or internal connections to temperature sensor
(VTS), internal reference voltage VREFINT, VBAT/3 or opampxint_vout.

**Table 71. Interconnect 21**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `ADC channel source assignment` |  |  |  |  |  |
| 2 | `ADC channel` |  |  |  |  |  |
| 3 | `number` |  |  |  |  |  |
| 4 | `ADC1` | `ADC2` | `ADC3` | `ADC4` | `ADC5` |  |
| 5 | `IN0` | `-` | `-` | `-` | `-` | `-` |
| 6 | `PB1/OPAMP3` | `PA8/OPAMP5` |  |  |  |  |
| 7 | `IN1` | `PA0` | `PA0` | `PE14` |  |  |
| 8 | `_VOUT` | `_VOUT` |  |  |  |  |
| 9 | `IN2` | `PA1` | `PA1` | `PE9` | `PE15` | `PA9` |
| 10 | `PA2/OPAMP1` | `PA6/OPAMP2` | `PB12/OPAMP4` | `opamp5_int` |  |  |
| 11 | `IN3` | `PE13` |  |  |  |  |
| 12 | `_VOUT` | `_VOUT` | `_VOUT` | `_vout(1)` |  |  |
| 13 | `IN4` | `PA3` | `PA7` | `PE7` | `PB14` | `Temp sensor` |

**Table 71. Interconnect 21 (continued)**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `ADC channel source assignment` |  |  |  |  |  |
| 2 | `ADC channel` |  |  |  |  |  |
| 3 | `number` |  |  |  |  |  |
| 4 | `ADC1` | `ADC2` | `ADC3` | `ADC4` | `ADC5` |  |
| 5 | `opamp4_int` |  |  |  |  |  |
| 6 | `IN5` | `PB14` | `PC4` | `PB13` | `PB15` |  |
| 7 | `_vout(1)` |  |  |  |  |  |
| 8 | `IN6` | `PC0` | `PC0` | `PE8` | `PE8` | `PE8` |
| 9 | `IN7` | `PC1` | `PC1` | `PD10` | `PD10` | `PD10` |
| 10 | `IN8` | `PC2` | `PC2` | `PD11` | `PD11` | `PD11` |
| 11 | `IN9` | `PC3` | `PC3` | `PD12` | `PD12` | `PD12` |
| 12 | `IN10` | `PF0` | `PF1` | `PD13` | `PD13` | `PD13` |
| 13 | `PB12/OPAMP4` |  |  |  |  |  |
| 14 | `IN11` | `PC5` | `PD14` | `PD14` | `PD14` |  |
| 15 | `_VOUT` |  |  |  |  |  |
| 16 | `PB1/OPAMP3` |  |  |  |  |  |
| 17 | `IN12` | `PB2` | `PB0` | `PD8` | `PD8` |  |
| 18 | `_VOUT` |  |  |  |  |  |
| 19 | `opamp1_int` | `opamp3_int` |  |  |  |  |
| 20 | `IN13` | `PA5` | `PD9` | `PD9` |  |  |
| 21 | `_vout(1)` | `_vout(1)` |  |  |  |  |
| 22 | `PB11/OPAMP6` | `PB11/OPAMP6` |  |  |  |  |
| 23 | `IN14` | `PE10` | `PE10` | `PE10` |  |  |
| 24 | `_VOUT` | `_VOUT` |  |  |  |  |
| 25 | `IN15` | `PB0` | `PB15` | `PE11` | `PE11` | `PE11` |
| 26 | `opamp2_int` |  |  |  |  |  |
| 27 | `IN16` | `Temp sensor` | `PE12` | `PE12` | `PE12` |  |
| 28 | `_vout(1)` |  |  |  |  |  |
| 29 | `VBAT/3(2)` |  |  |  |  |  |
| 30 | `opamp6_int` |  |  |  |  |  |
| 31 | `IN17` | `VBAT/3` | `PA4` | `opamp6_int_` | `VBAT/3` |  |
| 32 | `_vout(1)` |  |  |  |  |  |
| 33 | `vout(1)(3)` |  |  |  |  |  |
| 34 | `opamp3_int` |  |  |  |  |  |
| 35 | `IN18` | `VREFINT` | `VREFINT` | `VREFINT` | `VREFINT` |  |
| 36 | `_vout(1)` |  |  |  |  |  |

1. Internal OPAMP output connected directly to ADC input only (no available externally on a pin).
2. For Category 3 devices only.
3. For Category 4 devices only.

The DAC outputs are available on GPIOs or can be internally connected to comparators and operational
amplifiers.

**Table 72. Interconnect 22**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Source` |  |  |  |  |  |  |  |
| 2 | `Destination` | `DAC1` | `DAC2` | `DAC3` | `DAC4` |  |  |  |
| 3 | `CH1` | `CH2` | `CH1` | `CH1` | `CH2` | `CH1` | `CH2` |  |
| 4 | `GPIO` | `PA4` | `PA5` | `PA6` | `-` | `-` | `-` | `-` |
| 5 | `COMP1` | `x` | `-` | `-` | `x` | `-` | `-` | `-` |
| 6 | `COMP2` | `-` | `x` | `-` | `-` | `x` | `-` | `-` |

**Table 72. Interconnect 22 (continued)**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Source` |  |  |  |  |  |  |  |
| 2 | `Destination` | `DAC1` | `DAC2` | `DAC3` | `DAC4` |  |  |  |
| 3 | `CH1` | `CH2` | `CH1` | `CH1` | `CH2` | `CH1` | `CH2` |  |
| 4 | `COMP3` | `x` | `-` | `-` | `x` | `-` | `-` | `-` |
| 5 | `COMP4` | `x` | `-` | `-` | `-` | `x` | `-` | `-` |
| 6 | `COMP5` | `-` | `x` | `-` | `-` | `-` | `x` | `-` |
| 7 | `COMP6` | `-` | `-` | `x` | `-` | `-` | `x` |  |
| 8 | `COMP7` | `-` | `-` | `x` | `-` | `-` | `x` | `-` |
| 9 | `OPAMP1` | `-` | `-` | `-` | `x` | `-` | `-` | `-` |
| 10 | `OPAMP2` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 11 | `OPAMP3` | `-` | `-` | `-` | `-` | `x` | `-` | `-` |
| 12 | `OPAMP4` | `-` | `-` | `-` | `-` | `-` | `x` | `-` |
| 13 | `OPAMP5` | `-` | `-` | `-` | `-` | `-` | `-` | `x` |
| 14 | `OPAMP6` | `-` | `-` | `-` | `x` | `-` | `-` | `-` |

**Table 73. Interconnect 23**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 | Column 10 | Column 11 | Column 12 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Comparator` | `Comparators input/output signals assignment` |  |  |  |  |  |  |  |  |  |  |
| 2 | `input/output` |  |  |  |  |  |  |  |  |  |  |  |
| 3 | `signals` | `GPIO` | `DAC output(1)` | `VREFINT scaler` |  |  |  |  |  |  |  |  |
| 4 | `INP` | `PA1` | `PB1` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 5 | `DAC1_` | `3/4` | `1/2` | `1/4` |  |  |  |  |  |  |  |  |
| 6 | `DAC3_VREF` |  |  |  |  |  |  |  |  |  |  |  |
| 7 | `COMP1` | `INM` | `PA0` | `PA4` | `-` | `-` | `-` | `CH1` | `VREF` | `VREF` | `VREF` |  |
| 8 | `CH1 INT` |  |  |  |  |  |  |  |  |  |  |  |
| 9 | `PA4` | `INT` | `INT` | `INT` |  |  |  |  |  |  |  |  |
| 10 | `OUT` | `PA0` | `PF4` | `PA6` | `PA11` | `PB8` | `-` | `-` | `-` | `-` | `-` | `-` |
| 11 | `INP` | `PA3` | `PA7` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 12 | `DAC1_` | `3/4` | `1/2` | `1/4` |  |  |  |  |  |  |  |  |
| 13 | `DAC3_VREF` |  |  |  |  |  |  |  |  |  |  |  |
| 14 | `COMP2` | `INM` | `PA2` | `PA5` | `-` | `-` | `-` | `CH2` | `VREF` | `VREF` | `VREF` |  |
| 15 | `CH2 INT` |  |  |  |  |  |  |  |  |  |  |  |
| 16 | `PA5` | `INT` | `INT` | `INT` |  |  |  |  |  |  |  |  |
| 17 | `OUT` | `PA2` | `PA7` | `PA12` | `PB9` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 18 | `INP` | `PC1` | `PA0` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 19 | `DAC1_` | `3/4` | `1/2` | `1/4` |  |  |  |  |  |  |  |  |
| 20 | `DAC3_VREF` |  |  |  |  |  |  |  |  |  |  |  |
| 21 | `COMP3` | `INM` | `PC0` | `PF1` | `-` | `-` | `-` | `CH1` | `VREF` | `VREF` | `VREF` |  |
| 22 | `CH1 INT` |  |  |  |  |  |  |  |  |  |  |  |
| 23 | `PA4` | `INT` | `INT` | `INT` |  |  |  |  |  |  |  |  |
| 24 | `OUT` | `PC2` | `PB7` | `PB15` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |

**Table 73. Interconnect 23 (continued)**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 | Column 10 | Column 11 | Column 12 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Comparator` | `Comparators input/output signals assignment` |  |  |  |  |  |  |  |  |  |  |
| 2 | `input/output` |  |  |  |  |  |  |  |  |  |  |  |
| 3 | `signals` | `GPIO` | `DAC output(1)` | `VREFINT scaler` |  |  |  |  |  |  |  |  |
| 4 | `INP` | `PB0` | `PE7` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 5 | `DAC1_` | `3/4` | `1/2` | `1/4` |  |  |  |  |  |  |  |  |
| 6 | `DAC3_VREF` |  |  |  |  |  |  |  |  |  |  |  |
| 7 | `COMP4` | `INM` | `PB2` | `PE8` | `-` | `-` | `-` | `CH1` | `VREF` | `VREF` | `VREF` |  |
| 8 | `CH2 INT` |  |  |  |  |  |  |  |  |  |  |  |
| 9 | `PA4` | `INT` | `INT` | `INT` |  |  |  |  |  |  |  |  |
| 10 | `OUT` | `PB1` | `PB6` | `PB14` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 11 | `INP` | `PD12` | `PB13` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 12 | `DAC1_` | `3/4` | `1/2` | `1/4` |  |  |  |  |  |  |  |  |
| 13 | `DAC4_VREF` |  |  |  |  |  |  |  |  |  |  |  |
| 14 | `COMP5` | `INM` | `PD13` | `PB10` | `-` | `-` | `-` | `CH2` | `VREF` | `VREF` | `VREF` |  |
| 15 | `CH1 INT` |  |  |  |  |  |  |  |  |  |  |  |
| 16 | `PA5` | `INT` | `INT` | `INT` |  |  |  |  |  |  |  |  |
| 17 | `OUT` | `PC7` | `PA9` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 18 | `INP` | `PD11` | `PB11` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 19 | `DAC2_` | `3/4` | `1/2` | `1/4` |  |  |  |  |  |  |  |  |
| 20 | `DAC4_VREF` |  |  |  |  |  |  |  |  |  |  |  |
| 21 | `COMP6` | `INM` | `PD10` | `PB15` | `-` | `-` | `-` | `CH1` | `VREF` | `VREF` | `VREF` |  |
| 22 | `CH2 INT` |  |  |  |  |  |  |  |  |  |  |  |
| 23 | `PA6` | `INT` | `INT` | `INT` |  |  |  |  |  |  |  |  |
| 24 | `OUT` | `PC6` | `PA10` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 25 | `INP` | `PD14` | `PB14` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |
| 26 | `DAC2_` | `3/4` | `1/2` | `1/4` |  |  |  |  |  |  |  |  |
| 27 | `DAC4_VREF` |  |  |  |  |  |  |  |  |  |  |  |
| 28 | `COMP7` | `INM` | `PD15` | `PB12` | `-` | `-` | `-` | `CH1` | `VREF` | `VREF` | `VREF` |  |
| 29 | `CH1 INT` |  |  |  |  |  |  |  |  |  |  |  |
| 30 | `PA6` | `INT` | `INT` | `INT` |  |  |  |  |  |  |  |  |
| 31 | `OUT` | `PC8` | `PA8` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |

1. It is an internal connection.

**Table 74. Interconnect 24**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Operational amplifier input/output signals assignment` |  |  |  |  |  |  |  |  |
| 2 | `Operational amplifier` |  |  |  |  |  |  |  |  |
| 3 | `input/output signals` | `ADC input on` | `ADC internal` |  |  |  |  |  |  |
| 4 | `GPIO` | `DAC output` |  |  |  |  |  |  |  |
| 5 | `GPIO` | `input` |  |  |  |  |  |  |  |
| 6 | `VINP` | `PA1` | `PA3` | `PA7` | `-` | `DAC3_CH1` | `-` | `-` |  |
| 7 | `OPAMP1` | `VINM` | `PA3` | `PC5` | `-` | `-` | `-` | `-` | `-` |
| 8 | `VOUT` | `PA2` | `-` | `-` | `-` | `ADC1_IN3` | `ADC1_IN13` |  |  |
| 9 | `VINP` | `PA7` | `PB14` | `PB0` | `PD14` | `-` | `-` | `-` |  |
| 10 | `OPAMP2` | `VINM` | `PA5` | `PC5` | `-` | `-` | `-` | `-` | `-` |
| 11 | `VOUT` | `PA6` | `-` | `-` | `-` | `ADC2_IN3` | `ADC2_IN16` |  |  |
| 12 | `VINP` | `PB0` | `PB13` | `PA1` | `-` | `DAC3_CH2` | `-` | `-` |  |
| 13 | `VINM` | `PB2` | `PB10` | `-` | `-` | `-` | `-` | `-` |  |
| 14 | `OPAMP3` |  |  |  |  |  |  |  |  |
| 15 | `ADC3_IN1/` | `ADC2_IN18/` |  |  |  |  |  |  |  |
| 16 | `VOUT` | `PB1` | `-` | `-` | `-` | `-` |  |  |  |
| 17 | `ADC1_IN12` | `ADC3_IN13` |  |  |  |  |  |  |  |

**Table 74. Interconnect 24 (continued)**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Operational amplifier input/output signals assignment` |  |  |  |  |  |  |  |  |
| 2 | `Operational amplifier` |  |  |  |  |  |  |  |  |
| 3 | `input/output signals` | `ADC input on` | `ADC internal` |  |  |  |  |  |  |
| 4 | `GPIO` | `DAC output` |  |  |  |  |  |  |  |
| 5 | `GPIO` | `input` |  |  |  |  |  |  |  |
| 6 | `VINP` | `PB13` | `PD11` | `PB11` | `-` | `DAC4_CH1` | `-` | `-` |  |
| 7 | `VINM` | `PB10` | `PD8` | `-` | `-` | `-` | `-` | `-` |  |
| 8 | `OPAMP4` |  |  |  |  |  |  |  |  |
| 9 | `ADC4_IN3/` |  |  |  |  |  |  |  |  |
| 10 | `VOUT` | `PB12` | `-` | `-` | `-` | `-` | `ADC5_IN5` |  |  |
| 11 | `ADC1_IN11` |  |  |  |  |  |  |  |  |
| 12 | `VINP` | `PB14` | `PD12` | `PC3` | `-` | `DAC4_CH2` | `-` | `-` |  |
| 13 | `OPAMP5` | `VINM` | `PB15` | `PA3` | `-` | `-` | `-` | `-` | `-` |
| 14 | `VOUT` | `PA8` | `-` | `-` | `-` | `ADC5_IN1` | `ADC5_IN3` |  |  |
| 15 | `VINP` | `PB12` | `PD9` | `PB13` | `-` | `DAC3_CH1` | `-` | `-` |  |
| 16 | `OPAMP6` | `VINM` | `PA1` | `PB1` | `-` | `-` | `-` | `-` | `-` |
| 17 | `VOUT` | `PB11` | `-` | `-` | `-` | `-` | `ADC12_IN14` | `ADC4_IN17` |  |

#### Active power mode

Run, Sleep, Low-power run, Low-power sleep.

### 11.3.9 From comparators (COMPx) to timers (TIMx, HRTIM)

Comparators (COMPx) output values can be connected to:

- Timers (TIMx) input captures or TIMx_ETR signals or TIMx_OCREFCLR signals.
- hrtim_eevx[4:1] and hrtim_in_fltx[4:1]

Comparators (COMPx) output values can also generate break input signals for timers (TIMx) see
Section 30.3.17: Bidirectional break inputs.

**Table 75. Interconnect 2**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Timer external` | `Timer external trigger signals assignment` |  |  |  |  |  |  |
| 2 | `trigger input` |  |  |  |  |  |  |  |
| 3 | `signal` | `TIM1` | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM20` |
| 4 | `TIM1_` | `TIM2_` | `TIM3_` | `TIM4_` | `TIM5_` | `TIM8_` | `TIM20_` |  |
| 5 | `timx_etr0` |  |  |  |  |  |  |  |
| 6 | `ETR` | `ETR` | `ETR` | `ETR` | `ETR` | `ETR` | `ETR` |  |
| 7 | `comp1_` | `comp1_` | `comp1_` | `comp1_` | `comp1_` | `comp1_` | `comp1_` |  |
| 8 | `timx_etr1` |  |  |  |  |  |  |  |
| 9 | `out` | `out` | `out` | `out` | `out` | `out` | `out` |  |
| 10 | `comp2_` | `comp2_` | `comp2_` | `comp2_` | `comp2_` | `comp2_` | `comp2_` |  |
| 11 | `timx_etr2` |  |  |  |  |  |  |  |
| 12 | `out` | `out` | `out` | `out` | `out` | `out` | `out` |  |
| 13 | `comp3_` | `comp3_` | `comp3_` | `comp3_` | `comp3_` | `comp3_` | `comp3_` |  |
| 14 | `timx_etr3` |  |  |  |  |  |  |  |
| 15 | `out` | `out` | `out` | `out` | `out` | `out` | `out` |  |
| 16 | `comp4_` | `comp4_` | `comp4_` | `comp4_` | `comp4_` | `comp4_` | `comp4_` |  |
| 17 | `timx_etr4` |  |  |  |  |  |  |  |
| 18 | `out` | `out` | `out` | `out` | `out` | `out` | `out` |  |
| 19 | `comp5_` | `comp5_` | `comp5_` | `comp5_` | `comp5_` | `comp5_` | `comp5_` |  |
| 20 | `timx_etr5` |  |  |  |  |  |  |  |
| 21 | `out` | `out` | `out` | `out` | `out` | `out` | `out` |  |

**Table 75. Interconnect 2 (continued)**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Timer external` | `Timer external trigger signals assignment` |  |  |  |  |  |  |
| 2 | `trigger input` |  |  |  |  |  |  |  |
| 3 | `signal` | `TIM1` | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM20` |
| 4 | `comp6_` | `comp6_` | `comp6_` | `comp6_` | `comp6_` | `comp6_` | `comp6_` |  |
| 5 | `timx_etr6` |  |  |  |  |  |  |  |
| 6 | `out` | `out` | `out` | `out` | `out` | `out` | `out` |  |
| 7 | `comp7_` | `comp7_` | `comp7_` | `comp7_` | `comp7_` | `comp7_` | `comp7_` |  |
| 8 | `timx_etr7` |  |  |  |  |  |  |  |
| 9 | `out` | `out` | `out` | `out` | `out` | `out` | `out` |  |
| 10 | `adc1_` | `tim3_` | `tim2_` | `adc2_` | `adc3_` |  |  |  |
| 11 | `timx_etr8` | `tim3_etr` | `tim2_etr` |  |  |  |  |  |
| 12 | `awd1` | `etr` | `etr` | `awd1` | `awd1` |  |  |  |
| 13 | `adc1_` | `tim5_` | `tim3_` | `adc2_` | `adc3_` |  |  |  |
| 14 | `timx_etr9` | `tim4_etr` | `tim4_etr` |  |  |  |  |  |
| 15 | `awd2` | `etr` | `etr` | `awd2` | `awd2` |  |  |  |
| 16 | `adc1_` | `adc2_` | `adc3_` |  |  |  |  |  |
| 17 | `timx_etr10` | `tim5_etr` | `-` | `-` | `-` |  |  |  |
| 18 | `awd3` | `awd3` | `awd3` |  |  |  |  |  |
| 19 | `adc4_` | `lse_` | `adc2_` | `adc3_` | `adc5_` |  |  |  |
| 20 | `timx_etr11` | `-` | `-` |  |  |  |  |  |
| 21 | `awd1` | `css_out` | `awd1` | `awd1` | `awd1` |  |  |  |
| 22 | `adc4_` | `adc2_` | `adc3_` | `adc5_` |  |  |  |  |
| 23 | `timx_etr12` | `-` | `-` | `-` |  |  |  |  |
| 24 | `awd2` | `awd2` | `awd2` | `awd2` |  |  |  |  |
| 25 | `adc4_` | `adc2_` | `adc3_` | `adc5_` |  |  |  |  |
| 26 | `timx_etr13` | `-` | `-` | `-` |  |  |  |  |
| 27 | `awd3` | `awd3` | `awd3` | `awd3` |  |  |  |  |

**Table 76. Interconnect 3**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Timer` | `Timer OCREF clear signals assignment` |  |  |  |  |  |  |
| 2 | `OCREF` |  |  |  |  |  |  |  |
| 3 | `clear` |  |  |  |  |  |  |  |
| 4 | `TIM1` | `TIM2` | `TIM3` | `TIM8` | `TIM15` | `TIM16` | `TIM17` | `TIM20` |
| 5 | `signal` |  |  |  |  |  |  |  |
| 6 | `timx_` |  |  |  |  |  |  |  |
| 7 | `comp1_out comp1_out comp1_out comp1_out comp1_out comp1_out comp1_out comp1_out` |  |  |  |  |  |  |  |
| 8 | `ocref_clr0` |  |  |  |  |  |  |  |
| 9 | `timx_` |  |  |  |  |  |  |  |
| 10 | `comp2_out comp2_out comp2_out comp2_out comp2_out comp2_out comp2_out comp2_out` |  |  |  |  |  |  |  |
| 11 | `ocref_clr1` |  |  |  |  |  |  |  |
| 12 | `timx_` |  |  |  |  |  |  |  |
| 13 | `comp3_out comp3_out comp3_out comp3_out comp3_out comp3_out comp3_out comp3_out` |  |  |  |  |  |  |  |
| 14 | `ocref_lr2` |  |  |  |  |  |  |  |
| 15 | `timx_` |  |  |  |  |  |  |  |
| 16 | `comp4_out comp4_out comp4_out comp4_out comp4_out comp4_out comp4_out comp4_out` |  |  |  |  |  |  |  |
| 17 | `ocref_clr3` |  |  |  |  |  |  |  |
| 18 | `timx_` |  |  |  |  |  |  |  |
| 19 | `comp5_out comp5_out comp5_out comp5_out comp5_out comp5_out comp5_out comp5_out` |  |  |  |  |  |  |  |
| 20 | `ocref_clr4` |  |  |  |  |  |  |  |
| 21 | `timx_` |  |  |  |  |  |  |  |
| 22 | `comp6_out comp6_out comp6_out comp6_out comp6_out comp6_out comp6_out comp6_out` |  |  |  |  |  |  |  |
| 23 | `ocref_clr5` |  |  |  |  |  |  |  |
| 24 | `timx_` |  |  |  |  |  |  |  |
| 25 | `comp7_out comp7_out comp7_out comp7_out comp7_out comp7_out comp7_out comp7_out` |  |  |  |  |  |  |  |
| 26 | `ocref_clr6` |  |  |  |  |  |  |  |

**Table 77. Interconnect 4**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 | Column 10 | Column 11 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Timer` | `Timer TI1 signals assignment` |  |  |  |  |  |  |  |  |  |
| 2 | `TI1` |  |  |  |  |  |  |  |  |  |  |
| 3 | `input` |  |  |  |  |  |  |  |  |  |  |
| 4 | `TIM1` | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM15` | `TIM16` | `TIM17` | `TIM20` |  |
| 5 | `signal` |  |  |  |  |  |  |  |  |  |  |
| 6 | `TIM1` | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM15` | `TIM16` | `TIM17` | `TIM20` |  |
| 7 | `timx_` | `external` | `external` | `external` | `external` | `external` | `external` | `external` | `external` | `external` | `external` |
| 8 | `ti1_in0` | `TI1 input` | `TI1 input` | `TI1 input` | `TI1 input` | `TI1 input` | `TI1 input` | `TI1 input` | `TI1 input` | `TI1 input` | `TI1 input` |
| 9 | `pins` | `pins` | `pins` | `pins` | `pins` | `pins` | `pins` | `pins` | `pins` | `pins` |  |
| 10 | `timx_` | `comp1_` | `comp1_` | `comp1_` | `comp1_` | `comp1_` | `lse_` | `comp6_` | `comp5_` | `comp1_` |  |
| 11 | `LSI` |  |  |  |  |  |  |  |  |  |  |
| 12 | `ti1_in1` | `out` | `out` | `out` | `out` | `out` | `css_out` | `out` | `out` | `out` |  |
| 13 | `timx_` | `comp2_` | `comp2_` | `comp2_` | `comp2_` | `lse_` | `comp2_` | `comp1_` | `comp2_` |  |  |
| 14 | `MCO MCO` |  |  |  |  |  |  |  |  |  |  |
| 15 | `ti1_in2` | `out` | `out` | `out` | `out` | `css_out` | `out` | `out` | `out` |  |  |
| 16 | `timx_` | `comp3_` | `comp3_` | `comp3_` | `comp3_` | `rtc_` | `comp3_` | `comp2_` | `HSE_Di` | `HSE_Di` | `comp3_` |
| 17 | `ti1_in3` | `out` | `out` | `out` | `out` | `Wakeup` | `out` | `out` | `v32` | `v32` | `out` |
| 18 | `timx_` | `comp4_` | `comp4_` | `comp4_` | `comp4_` | `comp1_` | `comp4_` | `comp5_` | `rtc_` | `rtc_` | `comp4_` |
| 19 | `ti1_in4` | `out` | `out` | `out` | `out` | `out` | `out` | `out` | `Wakeup` | `Wakeup` | `out` |
| 20 | `timx_` | `comp5_` | `comp5_` | `comp5_` | `comp2_` | `comp7_` | `lse_` | `lse_` |  |  |  |
| 21 | `-` | `-` | `-` |  |  |  |  |  |  |  |  |
| 22 | `ti1_in5` | `out` | `out` | `out` | `out` | `out` | `css_out` | `css_out` |  |  |  |
| 23 | `timx_` | `comp6_` | `comp6_` | `comp3_` |  |  |  |  |  |  |  |
| 24 | `-` | `-` | `-` | `-` | `LSI` | `LSI` | `-` |  |  |  |  |
| 25 | `ti1_in6` | `out` | `out` | `out` |  |  |  |  |  |  |  |
| 26 | `timx_` | `comp7_` | `comp7_` | `comp4_` |  |  |  |  |  |  |  |
| 27 | `-` | `-` | `-` | `-` | `-` | `-` | `-` |  |  |  |  |
| 28 | `ti1_in7` | `out` | `out` | `out` |  |  |  |  |  |  |  |
| 29 | `timx_` | `comp5_` |  |  |  |  |  |  |  |  |  |
| 30 | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |  |  |
| 31 | `ti1_in8` | `out` |  |  |  |  |  |  |  |  |  |
| 32 | `timx_` | `comp6_` |  |  |  |  |  |  |  |  |  |
| 33 | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |  |  |
| 34 | `ti1_in9` | `out` |  |  |  |  |  |  |  |  |  |
| 35 | `timx_` | `comp7_` |  |  |  |  |  |  |  |  |  |
| 36 | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` | `-` |  |  |
| 37 | `ti1_in10` | `out` |  |  |  |  |  |  |  |  |  |

**Table 78. Interconnect 5**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Timer` | `Timer TI2 signals assignment` |  |  |  |  |  |  |  |
| 2 | `TI2 input` |  |  |  |  |  |  |  |  |
| 3 | `signal` | `TIM1` | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM15` | `TIM20` |
| 4 | `TIM1` | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM15` | `TIM20` |  |
| 5 | `timx_` | `external` | `external` | `external` | `external` | `external` | `external` | `external` | `external` |
| 6 | `ti2_in0` | `TI2 input` | `TI2 input` | `TI2 input` | `TI2 input` | `TI2 input` | `TI2 input` | `TI2 input` | `TI2 input` |
| 7 | `pins` | `pins` | `pins` | `pins` | `pins` | `pins` | `pins` | `pins` |  |
| 8 | `timx_` |  |  |  |  |  |  |  |  |
| 9 | `-` | `comp1_out` | `comp1_out` | `comp1_out` | `comp1_out` | `-` | `comp2_out` | `-` |  |
| 10 | `ti2_in1` |  |  |  |  |  |  |  |  |
| 11 | `timx_` |  |  |  |  |  |  |  |  |
| 12 | `-` | `comp2_out` | `comp2_out` | `comp2_out` | `comp2_out` | `-` | `comp3_out` | `-` |  |
| 13 | `ti2_in2` |  |  |  |  |  |  |  |  |
| 14 | `timx_` |  |  |  |  |  |  |  |  |
| 15 | `-` | `comp3_out` | `comp3_out` | `comp3_out` | `comp3_out` | `-` | `comp6_out` | `-` |  |
| 16 | `ti2_in3` |  |  |  |  |  |  |  |  |
| 17 | `timx_` |  |  |  |  |  |  |  |  |
| 18 | `-` | `comp4_out` | `comp4_out` | `comp4_out` | `comp4_out` | `-` | `comp7_out` | `-` |  |
| 19 | `ti2_in4` |  |  |  |  |  |  |  |  |
| 20 | `timx_` |  |  |  |  |  |  |  |  |
| 21 | `-` | `comp6_out` | `comp5_out` | `comp5_out` | `comp5_out` | `-` | `-` | `-` |  |
| 22 | `ti2_in5` |  |  |  |  |  |  |  |  |
| 23 | `timx_` |  |  |  |  |  |  |  |  |
| 24 | `-` | `-` | `comp6_out` | `comp6_out` | `comp6_out` | `-` | `-` | `-` |  |
| 25 | `ti2_in6` |  |  |  |  |  |  |  |  |
| 26 | `timx_` |  |  |  |  |  |  |  |  |
| 27 | `-` | `-` | `comp7_out` | `comp7_out` | `comp7_out` | `-` | `-` | `-` |  |
| 28 | `ti2_in7` |  |  |  |  |  |  |  |  |

**Table 79. Interconnect 6**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Timer TI3 signals assignment` |  |  |  |  |  |  |
| 2 | `Timer TI3` |  |  |  |  |  |  |
| 3 | `input signal` |  |  |  |  |  |  |
| 4 | `TIM1` | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM20` |
| 5 | `TIM1` | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM20` |
| 6 | `timx_` |  |  |  |  |  |  |
| 7 | `external TI3` | `external TI3` | `external TI3` | `external TI3` | `external TI3` | `external TI3` | `external TI3` |
| 8 | `ti3_in0` |  |  |  |  |  |  |
| 9 | `input pins` | `input pins` | `input pins` | `input pins` | `input pins` | `input pins` | `input pins` |
| 10 | `timx_` |  |  |  |  |  |  |
| 11 | `-` | `comp4_out` | `comp3_out` | `comp5_out` | `-` | `-` | `-` |
| 12 | `ti3_in1` |  |  |  |  |  |  |

**Table 80. Interconnect 7**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Timer TI4 signals assignment` |  |  |  |  |  |  |
| 2 | `Timer TI4` |  |  |  |  |  |  |
| 3 | `input signal` |  |  |  |  |  |  |
| 4 | `TIM1` | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM20` |
| 5 | `TIM1` | `TIM2` | `TIM3` | `TIM4` | `TIM5` | `TIM8` | `TIM20` |
| 6 | `timx_` |  |  |  |  |  |  |
| 7 | `external TI4` | `external TI4` | `external TI4` | `external TI4` | `external TI4` | `external TI4` | `external TI4` |
| 8 | `ti4_in0` |  |  |  |  |  |  |
| 9 | `input pins` | `input pins` | `input pins` | `input pins` | `input pins` | `input pins` | `input pins` |
| 10 | `timx_` |  |  |  |  |  |  |
| 11 | `-` | `comp1_out` | `-` | `comp6_out` | `-` | `-` | `-` |
| 12 | `ti4_in1` |  |  |  |  |  |  |
| 13 | `timx_` |  |  |  |  |  |  |
| 14 | `-` | `comp2_out` | `-` | `-` | `-` | `-` | `-` |
| 15 | `ti4_in2` |  |  |  |  |  |  |
| 16 | `The timer break input features two channels:` |  |  |  |  |  |  |

- A break channel which gathers both application fault (from input pins and built-in comparators)
  and system-level fault (clock failure, parity error, ...).
- A break2 channel which only includes application faults (from input pins and built-in
  comparators).

Refer to Table 81, Table 82 and Table 85.

**Table 81. Interconnect 8**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `Timer break signals assignment` |  |  |  |  |  |
| 2 | `TIM1 break` | `TIM8 break` | `TIM15 break` | `TIM16 break` | `TIM17 break` | `TIM20 break` |
| 3 | `(tim1_bk)` | `(tim8_bk)` | `(tim15_bk)` | `(tim16_bk)` | `(tim17_bk)` | `(tim20_bk)` |
| 4 | `TIM1_BKIN` | `TIM8_BKIN` | `TIM15_BKIN` | `TIM16_BKIN` | `TIM17_BKIN` | `TIM20_BKIN` |
| 5 | `pin` | `pin` | `pin` | `pin` | `pin` | `pin` |
| 6 | `comp1_out` | `comp1_out` | `comp1_out` | `comp1_out` | `comp1_out` | `comp1_out` |
| 7 | `comp2_out` | `comp2_out` | `comp2_out` | `comp2_out` | `comp2_out` | `comp2_out` |
| 8 | `Timer break` |  |  |  |  |  |
| 9 | `comp3_out` | `comp3_out` | `comp3_out` | `comp3_out` | `comp3_out` | `comp3_out` |
| 10 | `signal sources` |  |  |  |  |  |
| 11 | `comp4_out` | `comp4_out` | `comp4_out` | `comp4_out` | `comp4_out` | `comp4_out` |
| 12 | `comp5_out` | `comp5_out` | `comp5_out` | `comp5_out` | `comp5_out` | `comp5_out` |
| 13 | `comp6_out` | `comp6_out` | `comp6_out` | `comp6_out` | `comp6_out` | `comp6_out` |
| 14 | `comp7_out` | `comp7_out` | `comp7_out` | `comp7_out` | `comp7_out` | `comp7_out` |

**Table 82. Interconnect 9**

| Source row | Column 1 | Column 2 | Column 3 |
| ---: | --- | --- | --- |
| 1 | `Timer break2 signals assignment` |  |  |
| 2 | `TIM1 break2` | `TIM8 break2` | `TIM20 break2` |
| 3 | `(tim1_bk2)` | `(tim8_bk2)` | `(tim20_bk2)` |
| 4 | `TIM1_BKIN2 pin` | `TIM8_BKIN2 pin` | `TIM20_BKIN2 pin` |
| 5 | `comp1_out` | `comp1_out` | `comp1_out` |
| 6 | `comp2_out` | `comp2_out` | `comp2_out` |
| 7 | `comp3_out` | `comp3_out` | `comp3_out` |
| 8 | `Timer break2` |  |  |
| 9 | `signal source` |  |  |
| 10 | `comp4_out` | `comp4_out` | `comp4_out` |
| 11 | `comp5_out` | `comp5_out` | `comp5_out` |
| 12 | `comp6_out` | `comp6_out` | `comp6_out` |
| 13 | `comp7_out` | `comp7_out` | `comp7_out` |

**Table 83. Interconnect 10**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `HRTIM external event signal assignment` |  |  |  |  |
| 2 | `HRTIM external` |  |  |  |  |
| 3 | `event input signal` | `EExSRC[1:0]=0` |  |  |  |
| 4 | `EExSRC[1:0]=1` | `EExSRC[1:0]=2` | `EExSRC[1:0]=3` |  |  |
| 5 | `(from GPIO pin)` |  |  |  |  |
| 6 | `hrtim_eev1[4:1]` | `HRTIM_EEV1` | `comp2_out` | `tim1_trgo` | `adc1_AWD1` |
| 7 | `hrtim_eev2[4:1]` | `HRTIM_EEV2` | `comp4_out` | `tim2_trgo` | `adc1_AWD2` |
| 8 | `hrtim_eev3[4:1]` | `HRTIM_EEV3` | `comp6_out` | `tim3_trgo` | `adc1_AWD3` |
| 9 | `hrtim_eev4[4:1]` | `HRTIM_EEV4` | `comp1_out` | `comp5_out` | `adc2_AWD1` |
| 10 | `hrtim_eev5[4:1]` | `HRTIM_EEV5` | `comp3_out` | `comp7_out` | `adc2_AWD2` |
| 11 | `hrtim_eev6[4:1]` | `HRTIM_EEV6` | `comp2_out` | `comp1_out` | `adc2_AWD3` |
| 12 | `hrtim_eev7[4:1]` | `HRTIM_EEV7` | `comp4_out` | `tim7_trgo` | `adc3_AWD1` |
| 13 | `hrtim_eev8[4:1]` | `HRTIM_EEV8` | `comp6_out` | `comp3_out` | `adc4_AWD1` |
| 14 | `hrtim_eev9[4:1]` | `HRTIM_EEV9` | `comp5_out` | `tim15_trgo` | `comp4_out` |
| 15 | `hrtim_eev10[4:1]` | `HRTIM_EEV10` | `comp7_out` | `tim6_trgo` | `adc5_AWD1` |

**Table 84. Interconnect 11**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `External Input` | `On-chip source` | `External Input` | `On-chip source` |  |
| 2 | `Fault channel` |  |  |  |  |
| 3 | `FLTxSRC[1:0] = 00` | `FLTxSRC[1:0] = 01` | `FLTxSRC[1:0] = 10` | `FLTxSRC[1:0] = 11` |  |
| 4 | `hrtim_flt1[4:1]` | `HRTIM_FLT1` | `comp2_out` | `EEV1_muxout` | `N/A` |
| 5 | `hrtim_flt2[4:1]` | `HRTIM_FLT2` | `comp4_out` | `EEV2_muxout` | `N/A` |
| 6 | `hrtim_flt3[4:1]` | `HRTIM_FLT3` | `comp6_out` | `EEV3_muxout` | `N/A` |
| 7 | `hrtim_flt4[4:1]` | `HRTIM_FLT4` | `comp1_out` | `EEV4_muxout` | `N/A` |
| 8 | `hrtim_flt5[4:1]` | `HRTIM_FLT5` | `comp3_out` | `EEV5_muxout` | `N/A` |
| 9 | `hrtim_flt6[4:1]` | `HRTIM_FLT6` | `comp5_out` | `EEV6_muxout` | `N/A` |

#### Active power mode

Run, Sleep, Low-power run, Low-power sleep.

### 11.3.10 From system errors to timers (TIMx) and HRTIM

TIMx (TIM1/TIM8/TIM20/TIM15/TIM16/TIM17) break inputs and HRTIM system fault input gather MCU
internal fault events coming from:

- the clock failure event generated by the clock security system (CSS),
- the PVD output,
- the SRAM parity error signal,
- the Cortex-M4 LOCKUP (Hardfault) output
- Flash ECC double error detection

The purpose of the break function is to protect power switches driven by PWM signals generated by
the timers.

The functionality is described in:

- [Section 29.3.18](chapter-29.md#29318-using-the-break-function): Using the break function (TIM1/TIM8/TIM20)
- [Section 31.4.15](chapter-31.md#31415-using-the-break-function): Using the break function (TIM15/TIM16/TIM17/TIM20)

#### Active power mode

Run, Sleep, Low-power run, Low-power sleep.

**Table 85. Interconnect 18**

| Source row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `System error signals to timer signals assignment` |  |  |  |  |  |  |  |
| 2 | `System error signal surce` |  |  |  |  |  |  |  |
| 3 | `TIM1` | `TIM8` | `TIM15` | `TIM16` | `TIM17` | `TIM20` | `HRTIM` |  |
| 4 | `Flash ECC error` |  |  |  |  |  |  |  |
| 5 | `PVD output` |  |  |  |  |  |  |  |
| 6 | `SRAM1/` |  |  |  |  |  |  |  |
| 7 | `CCM SRAM parity` | `tim1_bk` | `tim8_bk` | `tim15_bk` | `tim16_bk` | `tim17_bk` | `tim20_bk` | `hrtim_sys_flt` |
| 8 | `Cortex®-M4 Lockup` |  |  |  |  |  |  |  |
| 9 | `(hardfault)` |  |  |  |  |  |  |  |
| 10 | `Clock security system (CSS)` |  |  |  |  |  |  |  |

### 11.3.11 From timers (TIM16/TIM17) to IRTIM

**Table 86. Interconnect 16**

| IRTIM control signal | IRTIM control signals assignment |
| --- | --- |
| modulation envelope signal | tim16_oc1 |
| carrier signal | tim17_oc1 |

General-purpose timer (TIM16/TIM17) output channel TIMx_OC1 are used to generate the waveform of
infrared signal output.

The functionality is described in [Section 34](chapter-34.md#34-infrared-interface-irtim): Infrared interface (IRTIM).

#### Active power mode

Run, Sleep, Low-power run, Low-power sleep.
