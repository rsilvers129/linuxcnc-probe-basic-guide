# MK100 spindle VFD over Modbus RTU

VFD: **MK100-1S2.2G-DK** (sold under the RATTMMOTOR name), 110 V single-phase input, 2.2 kW. Its Modbus behaves like the Inovance MD-series register map. Manual: *MK100 Series Manual*, sections 13.3–13.4.

## VFD parameters

Set on the keypad, or written over Modbus once comms work.

| Parameter | Value | Meaning |
|---|---|---|
| Pd-00 | 5005 | 9600 baud |
| Pd-01 | 0 | 8 data bits, no parity, **2 stop bits** (8N2) |
| Pd-02 | 1 | Modbus address 1 |
| Pd-03 | 2 | (unchanged, response delay) |
| Pd-04 | 10 | 1.0 s comms timeout: the VFD stops itself if LinuxCNC stops talking |
| Pd-05 | **31** | Standard Modbus protocol. It was 30 (non-standard) from the factory, and nothing answered until this was changed. |
| P0-02 | 2 | Run commands from communication |
| P0-03 | 9 | Frequency from communication |
| P0-10 | 4000 | Max frequency 400.0 Hz = 24,000 rpm |
| P0-17 / P0-18 | 100 | 10.0 s accel / decel |

> **P0 vs Pd:** the keypad groups look alike. Editing P0-xx while thinking it was Pd-xx breaks keypad control. Double-check the group letter.

## Registers used

| Register | Access | Meaning | HAL pin (`hm2_modbus.0.vfd.*`) |
|---|---|---|---|
| 2000H | write | Command: 1 forward, 2 reverse, 6 decelerate to stop, 7 fault reset | `cmd` |
| 1000H | write | Speed, −10000…10000 = % of P0-10 × 100 | `speed` (scale 10000/24000 = 0.41666667) |
| 1001H | read | Running frequency, 0.1 Hz | `freq` (scale 6 → rpm) |
| 1004H | read | Output current, 0.01 A | `current` (scale 0.01) |
| 3000H | read | State: 1 fwd, 2 rev, 3 stop | `state` |
| 8000H | read | Fault code, 0 = none | `faultcode` |

The MK100 answers **one register per read** (manual 13.3), so every read command has `count="1"`.

## LinuxCNC side

- Firmware: **7i96s_pktv3.bin** for the PktUART (see `firmware/`).
- Driver: `hm2_modbus` (LinuxCNC 2.9.10). The register map is `config/6040_7i96s/modbus/mk100.mbccs`, compiled with `mesambccc -o mk100.mbccb mk100.mbccs`. The HAL loads the `.mbccb`:

  ```
  loadrt hm2_modbus ports="hm2_[HOSTMOT2](BOARD).0.pktuart.0" mbccbs="/home/USER/linuxcnc/configs/6040_7i96s/modbus/mk100.mbccb"
  ```

- **At-speed**: the `near` component compares commanded and actual rpm (within 2 % or 100 rpm) → `spindle.0.at-speed`. Programs wait for it before cutting.
- **Fault**: a VFD fault code ≠ 0, *or* lost Modbus comms, → `spindle.0.amp-fault-in`. LinuxCNC stops.
- **Startup**: the `initlist` writes 7 (fault reset) to 2000H. That clears the comms-timeout fault (**Err16**) the VFD shows whenever LinuxCNC has been closed.
- `mk100-readonly.mbccs` only reads registers. Use it to test the link without being able to start the spindle.

Measured: M3 6000 → 6000 rpm in about 3 s, about 6.7 A unloaded. M4 reverses. No Modbus errors.
