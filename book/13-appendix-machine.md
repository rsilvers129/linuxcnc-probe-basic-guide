# Appendix B. The reference machine

Everything in this guide was done on this machine. The full details are in the repository: `hardware/wiring.md`, `hardware/vfd-mk100.md`, `firmware/README.md`, `machine.yaml` and the complete configuration in `config/6040_7i96s/`.

| Part | What |
|---|---|
| Machine | Chinese 6040 router, 5 mm ballscrews, 380 × 567 × 105 mm travel, 4th axis |
| Previous controller | Mach3 + a USB motion card (RnR Eco Motion) |
| Controller | Mesa 7I96S (Ethernet), firmware 7i96s_pktv3 |
| PC | Laptop, Intel i7-9750H, Debian 13 + LinuxCNC 2.9.10 PREEMPT_RT; Realtek NIC on r8168-dkms with ASPM/EEE off |
| Steppers | 3 × DM542H, 1600 steps/rev, 3.76 A; A axis on a JP-1635A board |
| Spindle | GDZ-80 2.2 kW water-cooled, ER20, 24,000 rpm |
| VFD | MK100-1S2.2G-DK, 110 V, controlled over Modbus RS-485 |
| Inputs | One switch per axis (home + limits), touch plate, PGFUN TP05C 3D probe, NC tool setter, NC E-stop |
| Pendant | XHC WHB04B-6 wireless |
| Screen | Probe Basic 1.0.3 |

## Calibration results

| Item | Value | How |
|---|---|---|
| X steps/mm | 321.034 (nominal 320) | Probe + ring gauge + 1-2-3 block in two orientations. X read 0.323 % long. |
| Y, Z steps/mm | 320 | The same test showed Y accurate. |
| Tool setter repeatability | about 0.007 mm | Repeated touch-offs of one tool |
| SPINDLE ZERO | 49.1901 mm | Bare collet nut on the setter |
| Probe length (T99) | 46.8736 mm | On the setter, slow |
| Probe ball | 1.998 mm | Micrometer |
| Probe calibration offset | 0.0471 mm | 24.995 mm ring gauge. X and Y differ by backlash. |

## How the conversion went, in brief

1. Built and tested the LinuxCNC config in simulation before the card arrived. Latency test; the Realtek NIC moved to the r8168 driver after r8169 produced packet errors.
2. Card on the bench: `readhmid`, a 30-minute link test with 0 errors.
3. Moved the wires from the Mach3 card. Two classic mistakes: a ground wire on the wrong terminal (steppers rough in one direction), and the limit-switch common landed on an input (flickering probe input).
4. Rewired the stepper drivers common-anode at 5 V; homing, limits and travel set.
5. Flashed PktUART firmware, wired RS-485 to the VFD (with the pair swapped), and set the VFD to standard Modbus (Pd-05 = 31). The spindle ran under LinuxCNC control.
6. Added the E-stop, tool setter, 3D probe and pendant; calibrated the setter, probe and X scale.
7. First job: a facing program for the wasteboard, then an isogrid plate (plywood test, then aluminum) from Fusion 360.
