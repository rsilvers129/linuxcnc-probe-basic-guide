# Probe Basic, Explained

*An illustrated guide to running a CNC router or mill with LinuxCNC and the Probe Basic screen, from homing to the last tool change.*

## Why this guide exists

Probe Basic is one of the best-looking and most capable screens for LinuxCNC. It has a full probing suite, a tool-setter routine, conversational programming and a database tool table. Its official documentation covers installation and configuration well, but the parts a new operator needs most are thin. The interface pages are mostly screenshots with headings, and nothing walks you through a real job from start to finish.

This guide fills that gap. It was written while setting up and running a real machine: a Chinese 6040 router converted from Mach3 to LinuxCNC with a Mesa 7I96S card. Every procedure here was done on that machine, and every mistake in the troubleshooting chapter actually happened.

## Who it is for

- **New Probe Basic users** who can start LinuxCNC but are not sure what half the buttons do.
- **People coming from Mach3, UCCNC or GRBL senders**, where work offsets and tool lengths work a little differently.
- **Anyone (or any AI assistant) who wants to reproduce this exact machine.** The repository holds the complete, working configuration: Mesa firmware, HAL, INI, Modbus spindle control, wiring tables and calibration values. See *AGENTS.md* in the repository root.

## Versions

Written against:

| Component | Version |
|---|---|
| Probe Basic | 1.0.3 |
| QtPyVCP | 6.0.7 |
| LinuxCNC | 2.9.10 (uspace, PREEMPT_RT) |
| OS | Debian 13 "Trixie" |

Probe Basic changes between versions, so if a button described here is missing on your screen, check the version first.

## How to read it

Chapters 1 to 3 are the core: the two ideas everything rests on (work offsets and tool lengths), a tour of the screen, and a complete first job. After that, use the chapters as a reference.

Boxes marked **On the 6040** show how the reference machine is set up. Skip them if your machine is different.

> **Safety.** A CNC machine will do exactly what it is told, including driving a cutter into a vise. Keep a hand near FEED HOLD or the E-stop the first time you run anything, and run new programs slowly, or in the air, first.

## Licence

Text and diagrams: Creative Commons Attribution-ShareAlike 4.0. Configuration files: GPL-2.0-or-later, the same as LinuxCNC and Probe Basic, which several of them come from. Probe Basic is by the kcjengr team, and this guide is not affiliated with them.
