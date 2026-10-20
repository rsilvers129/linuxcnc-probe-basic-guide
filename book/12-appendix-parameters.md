# Appendix A. Probe Basic parameters (#3000–#3058)

Probe Basic stores its settings as numbered parameters in the LinuxCNC parameter file (`.var`). The screen fields are bound to these numbers, so the values persist across restarts and you can set them from MDI (for example `#3026 = 200`). The screen updates when the file changes.

| # | Name in the subroutines | Screen / meaning |
|---|---|---|
| 3000 | activate_programmable_coolant | Settings: programmable coolant on (1) |
| 3001 | horizontal_spindle_nozzle_dist | Settings: nozzle horizontal distance |
| 3002 | vertical_spindle_nozzle_dist | Settings: nozzle vertical distance |
| 3003 | pc_angle_offset | Settings: nozzle angle offset |
| 3004 | probe_fast_fr (tool setter) | Tool setter: fast probe feed |
| 3005 | probe_slow_fr (tool setter) | Tool setter: slow probe feed (0 = single touch) |
| 3006 | probe_traverse_fr (tool setter) | Tool setter: traverse feed |
| 3007 | max_z_distance (tool setter) | Tool setter: Z max travel |
| 3008 | xy_max_travel | Tool setter: XY max travel |
| 3009 | retract_distance | Tool setter: retract between touches |
| 3010 | spindle_zero_height | Tool setter: SPINDLE ZERO (positive) |
| 3011 | tool_diameter_probe_mode | Tool setter: TOOL DIAM PROBE |
| 3012 | tool_diameter_offset_mode | Tool setter: TOOL DIAM OFFSET |
| 3013 | tool_setter_offset_direction | Tool setter: offset direction (0 left, 1 right, 2 front, 3 back) |
| 3014 | probe_tool_number | Touch probe: probe tool # |
| 3015 | probe_slow_fr | Touch probe: slow feed |
| 3016 | probe_fast_fr | Touch probe: fast feed |
| 3017 | probe_traverse_fr | Touch probe: traverse feed |
| 3018 | max_xy_distance | Touch probe: max X/Y distance |
| 3019 | xy_clearance | Touch probe: X/Y clearance |
| 3020 | max_z_distance | Touch probe: max Z distance |
| 3021 | z_clearance | Touch probe: Z clearance |
| 3022 | extra_probe_depth | Touch probe: extra probe depth |
| 3023 | step_off_width | Touch probe: step off width |
| 3024 | edge_width | Edge angle: spacing of the two touches |
| 3025 | diameter_hint | Round boss/pocket hint |
| 3026 | x_hint_boss_pocket | Rect boss/pocket X hint |
| 3027 | y_hint_boss_pocket | Rect boss/pocket Y hint |
| 3028 | x_hint_ridge_valley | Ridge/valley X hint |
| 3029 | y_hint_ridge_valley | Ridge/valley Y hint |
| 3030 | probe_mode | PROBE POSITION ONLY (1 = measure only, 0 = write the work offset) |
| 3031 | wco_rotation | SET ROTATION WCO |
| 3032 | calibration_offset | Probe calibration offset |
| 3033 | cal_diameter | Calibration ring/pin diameter |
| 3034 / 3035 | x_cal_width / y_cal_width | Square calibration widths |
| 3048–3050 | xy/x/y_cal_axis | Which calibration error to store |
| 3050–3058 | x0, y0, height, width, step, feeds, safe/search Z | Surface-scan routine |

Other parameters Probe Basic relies on:

| # | Meaning |
|---|---|
| 5181–5183 | G30 position (tool setter touch-off position), machine coordinates |
| 5221–5223 | G54 X, Y, Z |
| 5400 / 5410 | Tool in spindle / its diameter |
| 5061–5063, 5070 | Last probe result X, Y, Z, and whether it triggered |
