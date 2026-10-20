# 2. A tour of the screen

Probe Basic's window has two parts:

- **The top area** changes with the tab you pick: MAIN, FILE, TOOL, OFFSETS, PROBING, CONVERSATIONAL, SETTINGS and STATUS. ATC and USER tabs appear when they are enabled.
- **The control strip along the bottom** never changes. It holds everything you need while a program runs.

<!-- shot: full-screen -->

## The bottom control strip

Learn this strip first; it is where you spend most of your time.

### Program control (left)

| Button | What it does |
|---|---|
| **CYCLE START** | Runs the loaded program, or resumes after FEED HOLD. It is greyed out until the machine is on, homed, idle and has a program loaded. |
| **STOP** | Aborts the program. You lose your place; restarting mid-program needs RUN FROM LINE. |
| **FEED HOLD** | Freezes motion immediately and keeps your place. The **spindle keeps running.** Press CYCLE START to continue. |
| **SINGLE BLOCK** | When lit, each CYCLE START runs one line. Good for stepping through the start of a new program. |
| **BLOCK DELETE** | When lit, lines that start with `/` are skipped. |
| **M01 BREAK** | When lit, the program stops at every `M1` (optional stop). Fusion 360 often puts an `M1` before tool changes. |
| **POWER** | Machine on/off (after the E-stop is released). |
| **E-STOP** | Software E-stop toggle. Your physical E-stop button is separate and always wins. |
| Timer | Running time of the current program. |

### Tool panel

| Item | What it does |
|---|---|
| **T** box + **M6 G43** | Type a tool number and press it: tool change to that tool, then apply its length. Use it for the probe (T99) and for manual tool loads. |
| **G43 / G49** | Turn the tool length offset on or off. The lit one is active. |
| **LENGTH / DIAM** | Length and diameter of the tool in the spindle, from the tool table. |
| **GO TO ZERO** | Moves to the work zero: Z up first, then X0 Y0. |
| **GO TO G30** | Moves to the stored G30 position. Probe Basic uses it as the tool-setter position. |
| **GO TO HOME** | Moves to machine home. |

### Position readout (DRO)

One row per axis:

| Column | Meaning |
|---|---|
| **ZERO X / Y / Z / A** | Makes the current position zero in the active work offset. It **moves your work zero**, so don't press it by accident. |
| **G54 WORK** | Position relative to the part. That is the tool tip, if G43 is on. |
| **MACHINE** | Absolute machine position. |
| **DTG** | Distance to go in the current move. |
| **REF X / Y / Z / A** | Homes that axis. **REF ALL** homes everything; when done, the button reads **HOMED**. |
| **ZERO ALL** | Zeroes all axes at the current spot. |

### Overrides

Four sliders, each with a button that snaps back to 100 %:

| Slider | Effect |
|---|---|
| **F** | Feed override: scales every cutting feed. Turn it down for the first plunge of a new program, up once you trust it. |
| **R** | Rapid override. |
| **S** | Spindle speed override. |
| **V** | Maximum velocity for all moves. |

The **spindle load** bar shows spindle load when the machine reports it.

### Spindle and jog

- **FWD / STOP / REV** run the spindle manually at the default speed.
- The **JOG** panel has continuous and step jogging (1, 0.1, 0.01 mm on the reference machine).
- The **JOG / WCS / PLOT / USER** sub-tabs switch the small panel between jog buttons, work-offset buttons, preview options and user buttons.
- **MAN / AUTO / MDI** select the machine mode. Probe Basic usually switches for you.

## The tabs

### MAIN

<!-- shot: main-tab -->

The 3D toolpath preview (backplot) and the G-code listing. Preview buttons: ISO / X / Y / Z views, PAN, ZOOM ±, PGM EXT (fit the program), MCH EXT (fit the machine), PATH and CLEAR (the live tool trail), ORTHO/PSPECT.

The **MDI** sub-page has a keypad, MDI history and RUN FROM LINE controls. **RUN FROM LINE does not restore the state before that line**: position, feeds, work offset, tool, tool length, spindle. Only use it at the start of an operation, where the program sets all of those itself.

### FILE

<!-- shot: file-tab -->

The file browser for your `nc_files` folder and USB sticks. **LOAD G-CODE** opens a program. **TO PC / TO USB** copy files. There is also a built-in G-code editor (EDIT G-CODE, FIND/REPLACE, SAVE AS).

### TOOL

<!-- shot: tool-tab -->

The tool table, plus two panels:

- **Tool change panel**: **M6 G43** for a tool number. **LOAD SPINDLE / UNLOAD SPINDLE** are for ATC machines.
- **Electronic tool setter**: **TOUCH OFF CURRENT TOOL** measures the loaded tool on the setter. See chapter 6.

Table columns: tool number, pocket, Z (length), diameter, remark, and an **ATC** checkbox. ATC only matters with an automatic tool changer: it marks tools that fit in the carousel, and does nothing on a manual-change machine. **SAVE TABLE** commits your edits.

### OFFSETS

<!-- shot: offsets-tab -->

All nine work offsets as a table, plus the current one broken down. See chapter 4.

### PROBING

<!-- shot: probing-tab -->

Two sub-tabs:

- **TOUCH PROBE**: the probing parameters, the PROBE RESULTS panel, and the routine pages: OUTSIDE CORNERS, INSIDE CORNERS, BOSS AND POCKET, RIDGE AND VALLEY, EDGE ANGLE, ROTARY AXIS, CALIBRATE and PROBE HELP. See chapter 5.
- **TOOL SETTER**: the setter parameters (spindle zero, feeds, travel, retract) and **SET TOOL TOUCH OFF POS**. See chapter 6.

### CONVERSATIONAL

<!-- shot: conversational-tab -->

Generates simple programs without CAM: FACING, HOLE OPS (with XY COORD, PATTERN and THREAD MILL), PERIMETER, POCKETS and MISC. See chapter 9.

### SETTINGS and STATUS

SETTINGS holds startup options (which tab opens first), programmable-coolant constants, the spindle-rpm display source and the angular jog link. STATUS shows machine status messages and the error history: look here when something "did nothing".
