# 11. Troubleshooting (every one of these happened)

### Z zero is off by exactly the probe's length

**Cause:** The probe was in the spindle, but G43 wasn't active when you probed. LinuxCNC measured with the collet nut as the reference, so Z0 ended up one probe-length (46.87 mm here) too high.
**Fix:** Load the probe with **T 99 → M6 G43**, and check that the G43 button is lit and LENGTH shows the probe length. Re-probe, or correct G54 Z by subtracting the probe length.
**Check:** With the probe loaded and G43 on, the DRO Z equals the ball's real height above the part.

### "Requested tool 99 not found in tool table" (but it's in the table)

**Cause:** LinuxCNC's in-memory tool table was corrupted. An `io` process (and its tool-database backend) from an earlier LinuxCNC session had never exited. Two copies fought over the shared tool-table memory, and a tool-table reload made it visible.
**Fix:** Close LinuxCNC. Check `pgrep -a -f "io -ini"`: there should be no `io` processes left. Kill any leftovers, then start LinuxCNC again. After a restart there should be exactly one `io` and one `tool_db_backend`.

### The preview shows only a few lines of the program

**Cause:** The program calls a subroutine that probes (a tool touch-off, for example). The preview interpreter can't probe, the routine aborts with "probe failed", and the preview stops there.
**Fix:** Wrap such calls in `o100 if [#<_task> EQ 1]` … `o100 endif`. `_task` is 1 only in the real run.

### CYCLE START does nothing and doesn't highlight

**Cause:** The GUI thinks the machine isn't ready. It happened after modes were switched from outside the GUI, by a script over SSH.
**Fix:** Toggle **POWER** off and on. Check homed status and that a program is loaded. Look at the STATUS tab.

### "Motion enabled after reaching a coordinate soft limit with active external offsets"

**Cause:** An informational note. The machine was switched on while an axis sat exactly on a soft limit (Z at machine 0 after a tool change), and the config has external offsets enabled even though they aren't used.
**Fix:** Nothing. It is harmless.

### "Probe move would exceed Z negative limit" on a second touch-off

**Cause:** LinuxCNC rejects a G38 probe move if its full search length would pass the soft limit, even if the probe would trigger sooner.
**Fix:** Clamp the search distance to the room left above the limit (see `touch_plate.ngc`).

### "G38.2 move finished without making contact" (but it touched)

**Cause:** The touch plate or probe was moved, or lifted, between the fast and slow touches. The second, slow touch then found nothing.
**Fix:** Leave the plate in place until the routine finishes and lifts.

### Probing writes your work offset when you only wanted to measure

**Cause:** PROBE POSITION ONLY was off.
**Fix:** Leave it on by default. Turn it off only for the run that sets the zero.

### X and Y calibrate differently on a ring gauge

**Cause:** Different backlash per axis. A single probe calibration offset can't correct both.
**Fix:** Measure backlash with a dial indicator, set BACKLASH per joint in the INI, then recalibrate.

### Parts come out the wrong size by a fixed percentage on one axis

**Cause:** Steps per mm (SCALE) don't match the real ballscrew lead.
**Fix:** Probe a gauge block or 1-2-3 block in two lengths along that axis, and correct SCALE by the ratio. Using the difference of two lengths cancels the probe and backlash terms. On the reference machine: X 320 → 321.034.

### The VFD shows Err16 when LinuxCNC is closed

**Cause:** Normal on a Modbus spindle. The VFD's comms-timeout protection trips when nothing polls it.
**Fix:** None needed. The Modbus init list sends a fault reset when LinuxCNC starts.

### A G-code comment with parentheses breaks a subroutine

**Cause:** G-code comments can't nest. `(T99 (the probe))` is an error.
**Fix:** Use `(T99 = the probe)`.
