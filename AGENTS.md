# AGENTS.md: reproducing this machine with an AI assistant

This file is written for an AI coding assistant (Claude, ChatGPT, Codex, Gemini, …) that a person has pointed at this repository with a request like *"set up my CNC like this"*. Humans can follow it too.

The goal: a working **LinuxCNC 2.9 + Mesa 7I96S + Probe Basic** controller for a router, with:

- step/dir steppers,
- a Modbus RS-485 spindle VFD,
- home/limit switches,
- a 3D probe, a touch plate and a tool setter,
- an E-stop,
- a USB pendant.

The reference machine is a Chinese 6040 router. Facts about it are in `machine.yaml`.

## Ground rules for the assistant

1. **Physical machines can hurt people.** Never move axes, run the spindle, flash firmware, or change wiring-related config without the human confirming they are at the machine, clear of it, and have an E-stop within reach.
2. **Their machine is not this machine.** Before copying a value, ask about the human's hardware:
   - stepper drivers and microstepping,
   - screw lead, travel and switch positions,
   - VFD model and protocol,
   - probe type (NO/NC), tool setter type,
   - Mesa card and its IP jumpers.

   Keep this repo's values only where the hardware matches. Mark everything else *(confirm)* until tested.
3. **Never change soft limits or travel without the human's explicit say-so.** Do not shrink travel to "be safe" either.
4. **One stage at a time, and verify it** (see the gates below) before the next stage. Keep a dated log of every change, and back up files before editing them.
5. **Don't publish secrets.** This repo deliberately contains no IPs other than the Mesa card's private subnet, no usernames (paths use `/home/USER`), and no keys.

## Stage 0: inventory (ask, don't assume)

Ask the human for, or confirm from photos:

- **Control box:** stepper drivers (model, DIP settings), power supplies (5 V for the Mesa, 24 V for the inputs, stepper voltage), VFD model and its manual.
- **Mechanics:** ballscrew lead per axis, approximate travel per axis, which end each home switch is at, and whether one switch per axis serves as home plus both limits.
- **Inputs:** probe type and its wiring (NPN/PNP, NO/NC), tool setter contacts, E-stop type.
- **PC:** CPU, and **which Ethernet chip** the Mesa port uses. Realtek needs extra work; Intel is easiest.

## Stage 1: PC and real-time OS

Reference: Debian 13 "Trixie", the LinuxCNC 2.9.10 PREEMPT_RT ISO from linuxcnc.org. A laptop with an Intel i7-9750H.

1. Install from the official LinuxCNC ISO. Packages used: `linuxcnc-uspace 1:2.9.10`, `mesaflash`.
2. **Latency:** run `latency-histogram --nobase --nox --sbinsize 1000` under load for 20+ minutes. Reference result: about ±23 µs typical, with one 200 µs spike. That is fine for a 1 ms servo thread with an Ethernet Mesa card.
3. Disable screen blanking, DPMS and lid-suspend.

**Gate:** latency is well below the 1 ms servo period.

## Stage 2: Ethernet link to the Mesa card

1. Give the dedicated port a static address with no gateway: `system/NetworkManager/mesa-7i96s.nmconnection`. Set its `interface-name` to the human's port. Copy it to `/etc/NetworkManager/system-connections/` (mode 600), then `nmcli connection reload`.
2. **Realtek RTL8111/8168 only:** the in-kernel `r8169` driver gave 52 packet errors in 5 minutes. Install `r8168-dkms` (reference version 8.055.00-1) and `system/modprobe.d/r8168-mesa.conf`. That disables ASPM and EEE, which cause latency spikes. **Rebuild the initramfs** (`update-initramfs -u`), or the options won't apply at boot. Verify after reboot with `ethtool --show-eee <iface>` → disabled.
3. Card jumpers: **W4 down, W5 up** → card IP 10.10.10.10 (from EEPROM).
4. `mesaflash --device 7i96s --addr 10.10.10.10 --readhmid` must answer.

**Gate:** a 30-minute run with LinuxCNC loaded and **0 hm2 packet errors**.

## Stage 3: firmware (only for a Modbus spindle)

Follow `firmware/README.md` to flash **7i96s_pktv3.bin**. Confirm with `--readhmid` that TB2-16..19 show PktUARTRX/TX. Skip this stage if the spindle uses an analog 0–10 V input instead. The default firmware then works, and the config's spindle section needs rewriting for PWM.

## Stage 4: Probe Basic

Install from the kcjengr apt repository. Use the **stable** channel, not `-dev`:

```
deb [signed-by=/etc/apt/keyrings/kcjengr.gpg] https://repository.qtpyvcp.com/apt trixie main
```

`apt install python3-probe-basic`. Reference versions: Probe Basic 1.0.3, QtPyVCP 6.0.7. Check the kcjengr docs for the key URL.

## Stage 5: the configuration

1. Copy `config/6040_7i96s/` to `~/linuxcnc/configs/6040_7i96s/`.
2. **Replace every `/home/USER`** with the real home directory. It appears in two HAL files (the `hm2_modbus` `.mbccb` path and the pendant `source` line) and the desktop file.
3. Create `~/linuxcnc/nc_files/`.
4. Tool table: create `6040_tools.db` from `tools-snapshot.tbl` (QtPyVCP's `tbl2db`), or start empty and add tools on the TOOL tab.
5. `6040_7i96s.var` is the reference machine's parameter file: probe/setter settings, G30 and G54. Keep it as a starting point, but **re-measure** the setter position (#5181–5183), SPINDLE ZERO (#3010), the probe calibration (#3032) and every tool length.
6. Adapt to the human's hardware **before the first start**:
   - INI `[JOINT_n]`: `SCALE` (steps/rev × microsteps ÷ lead), limits, `HOME_*`, `STEP_INVERT` / `DIR_INVERT`, velocities.
   - HAL input pins: which `input-NN` is which switch; `-not` for NC contacts.
   - `modbus/mk100.mbccs` for a different VFD, recompiled with `mesambccc`.
7. Pendant: copy `system/99-xhc-whb04b-6.rules` to `/etc/udev/rules.d/` and reload udev.

**Gate, with motors unpowered:** LinuxCNC starts with no HAL errors. Each switch press shows in HAL (and as a lit LED on the card). Probe, setter and E-stop toggle the right signals.

## Stage 6: motion bring-up (human at the machine)

1. Power the drivers. Jog each axis slowly in both directions. Fix direction with `DIR_INVERT`.
2. Home each axis. Check that it parks off the switch (HOME_OFFSET) and doesn't trip a limit.
3. **Measure travel**: command 100 mm and measure it, or better, probe a gauge block (chapter 5). Correct `SCALE`. On the reference machine, X needed 321.034 instead of 320.

**Gate:** all axes home, soft limits match the real travel, and 100 mm commanded = 100 mm moved.

## Stage 7: spindle over Modbus

1. VFD keypad: set the Pd group values from `hardware/vfd-mk100.md`. **Pd-05 = 31** is the one that's easy to miss.
2. First test with the read-only map (`modbus/mk100-readonly.mbccs`): state, frequency and fault must read sensibly with 0 errors.
3. Then the full map: set P0-02 = 2 and P0-03 = 9 so the VFD takes commands from comms. With the human clear of the spindle: M3 S6000, M5, M4 S6000, M5.

**Gate:** commanded rpm = actual rpm, at-speed goes TRUE, and M5 stops it.

## Stage 8: probe, setter, offsets

Follow the guide (`book/`):

1. Set the setter's G30 position and SPINDLE ZERO, measured with the bare collet nut.
2. Measure the probe length gently, and enter the ball diameter.
3. Calibrate the probe on a ring gauge.
4. Optional: enable the **M6 remap** (`subroutines/pb_m6_touchoff.ngc` + the INI lines in chapter 6), so every tool change measures the tool. Test with MDI `T1 M6` first.

**Gate:**
- Tool setter repeats within about 0.01 mm.
- Probing a known block gives its size within about 0.02 mm.
- After RECT BOSS + M6 G43, the DRO Z equals a ruler measurement of the probe-to-part gap.

## Stage 9: first cut

Chapter 3 of the book. Run the first program in scrap (plywood), with the feed override low and a hand on FEED HOLD.

## Where things are

| Path | What |
|---|---|
| `book/` | The illustrated guide (Markdown sources) |
| `docs/` | Built website, EPUB and PDF (GitHub Pages) |
| `config/6040_7i96s/` | Complete LinuxCNC/Probe Basic config |
| `system/` | NetworkManager profile, r8168 options, udev rule, desktop launcher |
| `firmware/` | Mesa firmware notes, hashes, readhmid before/after |
| `hardware/` | Wiring tables, VFD/Modbus setup |
| `machine.yaml` | Machine facts in one structured file |
| `tools/build.py` | Builds `docs/` from `book/` |
