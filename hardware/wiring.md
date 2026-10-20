# Wiring: Mesa 7I96S on a 6040 router

This is the wiring as built and verified on the reference machine (October 2026). The config in `config/6040_7i96s/` matches it exactly. Terminal numbers are from the Mesa 7I96S manual: TB1 = step/dir and 5 V, TB2 = encoder/analog/RS-422, TB3 = isolated inputs.

> Check every connection against **your** hardware's manuals. Wire colors are from this machine's original Mach3 harness. Yours will differ.

## Power

| Supply | Goes to |
|---|---|
| 5 V DC | 7I96S **P4** (logic). Use a regulated, ideally isolated 5 V supply (e.g. Mean Well DDR-15G-5 from the 24 V rail). A USB charger works for bench testing only. |
| 24 V DC (+) | TB3 **INPUT COMMON** (pin 12, "NPN style": common to +24 V) and the 3D probe's red wire |
| 24 V DC (V−) | Limit-switch common, E-stop return, tool-setter return, 3D probe black |
| Stepper supply | DM542H drivers (up to about 50 V) |
| Mains | VFD, then spindle |

The control box's big red button cuts mains to everything, including the Mesa card. LinuxCNC then sees a lost card: restart LinuxCNC and home again afterwards. A second, latching **NC** E-stop on INPUT5 gives a normal LinuxCNC E-stop, which stops the spindle and motion without killing the card.

## Step / direction (TB1)

X, Y and Z use DM542H drivers wired **common-anode** at 5 V. A uses the 4th-axis board's own common-anode input.

| Axis | stepgen | Driver | PUL+ / DIR+ | PUL− | DIR− |
|---|---|---|---|---|---|
| X | 00 | DM542H | TB1 +5V | TB1 STEP0− | TB1 DIR0− |
| Y | 01 | DM542H | TB1 +5V | TB1 STEP1− | TB1 DIR1− |
| Z | 02 | DM542H | TB1 +5V | TB1 STEP2− | TB1 DIR2− |
| A | 03 | JP-1635A board | board +5V → TB1 +5V | PU → TB1 STEP3− | DR → TB1 DIR3− |

INI polarity, since the drivers are wired to the "−" outputs: `STEP_INVERT = 0` on all axes; `DIR_INVERT` X 1, Y 0, Z 0, A 1. Step timing (ns): DIRSETUP/DIRHOLD 10000, STEPLEN/STEPSPACE 5000.

DM542H DIP settings: **1600 steps/rev**. Current **3.76 A peak** (SW1 on, SW2 off, SW3 off), SW4 off = half current at standstill. Heat sinks were added to the drivers.

Resulting scale: 5 mm lead ballscrews → 320 steps/mm nominal. X is calibrated to **321.034** (its screw's lead is slightly under 5 mm). A = 26.6667 steps/deg.

## Inputs (TB3)

INPUT COMMON (TB3-12) = +24 V. A switch pulls its input to 24 V V−, and the input reads TRUE while current flows.

| Input | TB3 pin | Device | Contact | HAL |
|---|---|---|---|---|
| INPUT0 | 1 | X home/limit switches (yellow) | NO | `input-00` → X home + both limits |
| INPUT1 | 2 | Y home/limit switches (red) | NO | `input-01` |
| INPUT2 | 3 | Z home/limit switches (white) | NO | `input-02` |
| — | — | Switch common (black) | — | to 24 V **V−** (not to a TB3 pin) |
| INPUT3 | 4 | Touch plate lead (clip on the bit) | NO | `input-03` → probe OR |
| INPUT4 | 5 | PGFUN TP05C 3D probe, yellow (signal) | NPN-NO | `input-04` → probe OR |
| INPUT5 | 6 | Latching E-stop button, other side to V− | **NC** | `input-05` → `iocontrol.0.emc-enable-in` |
| INPUT6 | 7 | Tool setter "tool signal", other side to V− | **NC** | `input-06-not` → probe OR |

Notes:

- **One switch input per axis** serves as home and both limits (as in the original Mach3 profile). Homing: X/Y toward minus, Z up. The park point is 4 mm off the switch, so it doesn't sit on it.
- **3D probe power:** its internal pull-up goes to its own supply, so it must run from the same +24 V as INPUT COMMON. On 5 V the input would see about 19 V at rest and read as on.
- **Probe input:** INPUT3, INPUT4 and INPUT6 (inverted) are ORed in HAL into `motion.probe-input`. Any of them stops a G38 move.
- **Tool setter overtravel:** the setter's "stroke protect" NC contact is not wired yet. The natural place is in series with the E-stop.

## RS-485 Modbus to the VFD (TB2)

Requires firmware **7i96s_pktv3.bin** (see `firmware/`). It turns the RS-422 port on TB2-16..19 into a PktUART.

| 7I96S | Signal | Connect to |
|---|---|---|
| TB2-16 ↔ TB2-18 | RX+ ↔ TX+ (jumper: 2-wire half duplex) | VFD **485−** |
| TB2-17 ↔ TB2-19 | RX− ↔ TX− (jumper) | VFD **485+** |
| TB2-15 | GND | VFD **COM** |
| W7 | termination | off (the short cable runs fine without it) |

Yes, Mesa's "+" pair goes to the VFD's "485−". The first attempt, + to +, got no replies. RS-485 polarity labels are notoriously inconsistent between makers. If you get no response, swap the pair before changing anything else.

## Spindle

GDZ-80 2.2 kW water-cooled, ER20, 400 Hz = 24,000 rpm, driven by an MK100-1S2.2G-DK VFD (110 V). Speed, direction, at-speed and fault all go over Modbus; there are no analog or relay wires. See `vfd-mk100.md`.

> The spindle cable's plug can be inserted rotated. When it was, the VFD tripped **Err05** (overvoltage during acceleration) even when run from its own keypad. If a VFD that used to work faults on start, check the motor plug before blaming the configuration.

## USB pendant

XHC WHB04B-6 wireless pendant (receiver 10ce:eb93). Driver `xhc-whb04b-6`, which ships with LinuxCNC. Needs the udev rule in `system/99-xhc-whb04b-6.rules`. HAL mapping: `config/6040_7i96s/hallib/xhc_whb04b6.hal`.
