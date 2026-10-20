# Probe Basic, Explained, and a complete LinuxCNC 6040 router build

An illustrated guide to **Probe Basic** (the LinuxCNC screen by kcjengr), plus the complete, working configuration of the machine it was written on: a Chinese 6040 router converted from Mach3 to **LinuxCNC 2.9.10 + Mesa 7I96S**, with:

- a Modbus RS-485 spindle VFD,
- a 3D probe, a touch plate and a tool setter,
- an E-stop,
- a wireless pendant.

**Read the guide:** the website (GitHub Pages) · EPUB (Kindle via Send-to-Kindle, Apple Books) · PDF. The links are in `docs/`.

## What's here

| Path | Contents |
|---|---|
| [`book/`](book/) | The guide's Markdown sources and diagrams |
| [`docs/`](docs/) | Built website, EPUB and PDF |
| [`AGENTS.md`](AGENTS.md) | **Step-by-step reproduction instructions written for an AI assistant** (and humans): what to ask, what to change, how to verify each stage |
| [`machine.yaml`](machine.yaml) | Every machine fact in one structured file: pins, scales, VFD parameters, calibration |
| [`config/6040_7i96s/`](config/6040_7i96s/) | The full LinuxCNC + Probe Basic configuration (INI, HAL, Modbus map, subroutines, remap, parameter file, tool table) |
| [`hardware/`](hardware/) | Wiring tables (TB1/TB2/TB3), RS-485, MK100 VFD setup |
| [`firmware/`](firmware/) | Mesa 7I96S PktUART firmware notes, hashes, `readhmid` before and after |
| [`system/`](system/) | NetworkManager profile for the card, r8168 driver options, pendant udev rule, desktop launcher |
| [`tools/build.py`](tools/build.py) | Rebuilds `docs/` (site, EPUB, PDF) from `book/` |

## Reproducing the machine with an AI assistant

Point your assistant at this repository and ask it to follow `AGENTS.md`. It is written so the assistant inventories *your* hardware first, adapts the config to it, and verifies each stage (network, firmware, inputs, motion, spindle, probing) before moving on. It never moves the machine without you being there.

## Guide contents

0. Preface
1. The two ideas everything rests on: work offsets and tool lengths
2. A tour of the screen
3. Your first job, start to finish
4. The OFFSETS tab
5. Probing
6. The tool setter, and measuring every tool automatically (M6 remap)
7. The tool table
8. Running programs
9. Conversational programming
10. From CAM to Probe Basic (Fusion 360)
11. Troubleshooting
12. Appendix A: Probe Basic parameters
13. Appendix B: The reference machine

## Licences

- Guide text and diagrams: [CC BY-SA 4.0](LICENSE-docs.md).
- Configuration files: [GPL-2.0-or-later](LICENSE), the same as LinuxCNC and Probe Basic, whose files several of them are, or are derived from.
- Mesa firmware isn't included; get it from Mesa (see `firmware/README.md`).

Probe Basic is developed by the [kcjengr](https://github.com/kcjengr/probe_basic) team. This is an independent user guide, not affiliated with them.
