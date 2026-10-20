# 4. The OFFSETS tab

<!-- shot: offsets-tab -->

Chapter 1 explains what a work offset is. This chapter is the screen.

## The table (left)

One row per work coordinate system, in order: **G54, G55, G56, G57, G58, G59, G59.1, G59.2, G59.3**. Columns: **X, Y, Z, A** (the zero point, in machine coordinates) and **R** (rotation in degrees, set by EDGE ANGLE → SET ROTATION WCO).

- **SAVE TABLE / RELOAD TABLE** write or re-read the parameter file. Values set by probing or ZERO buttons are already saved; use these after editing cells by hand.
- **CLEAR SELECTED / CLEAR ALL** zero offsets. CLEAR ALL wipes every fixture you have set up.

## Selecting the active offset (right, top)

The buttons **G54 … G59.3** select which one is active. The lit one is what programs, probing and the ZERO buttons use. A program can also select one itself with a line like `G55`, and most CAM posts write `G54` at the start.

## The breakdown table (right, bottom)

For each axis:

| Column | Meaning |
|---|---|
| **SET TO ZERO** | The ZERO button: makes the current position zero in the active offset. |
| **WC CURRENT POSITION** | Where the tool tip is relative to the part. |
| **MACHINE COORDS** | Absolute position. |
| **WC OFFSET** | The active offset's value, the same as the table row. |
| **G52/G92 OFFSET** | A temporary extra shift. Keep it 0 unless you use G52/G92 on purpose. |
| **TOOL OFFSET** | The active tool length (Z) from G43. |

They always add up: **WC current = machine − WC offset − G52/G92 − tool offset**.

Worked example from the reference machine, with the probe (length 46.8736) loaded and G43 on, and Z all the way up:

```
Z:  0.000 − (−102.4266) − 0 − 46.8736 = 55.553
```

So the probe's ball was 55.55 mm above the part's top surface. A ruler confirmed it.

## Good practice

- **Don't press ZERO buttons you don't mean to.** Each one silently moves your part's zero.
- **Use one offset per fixture.** G54 for the vise, G55 for a second vise, G56 for a jig. Then a program for a different fixture just selects its offset, and nothing needs re-probing.
- **Write offsets down for repeat fixtures.** If a fixture is pinned to the table, its offset is valid every time you mount it.
