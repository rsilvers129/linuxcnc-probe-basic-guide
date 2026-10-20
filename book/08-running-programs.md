# 8. Running programs

## Starting

**CYCLE START** runs the loaded program. If it does nothing and the button doesn't highlight when you hover over it, the GUI considers the machine not ready. Check:

- the machine is on and homed (REF ALL shows **HOMED**),
- a program is loaded,
- nothing else (MDI, a probing routine) is still running.

Toggling **POWER** off and on forces Probe Basic to re-check its state. That cleared a stuck CYCLE START on the reference machine after modes had been changed from outside the GUI.

## Watching the first moves

- **F slider at 25–50 %** for the first plunge of any new program. Every feed move is scaled; rapids are not.
- **SINGLE BLOCK** to step line by line through the start.
- **Dry run in the air.** Temporarily raise G54 Z (for example 20 mm higher) and run the start of the program above the part. Put it back afterwards.
- **Test in scrap.** Run the program once in wood or plastic before the expensive stock, as the reference machine did with plywood before aluminum.

## Pausing and resuming

| You want to… | Do this |
|---|---|
| Pause briefly (chips, check something) | **FEED HOLD**, then **CYCLE START**. Your place is kept. The spindle keeps running. |
| Pause at a planned point | Put `M1` in the program and light **M01 BREAK**, or use `M0` (always stops). |
| Stop the spindle mid-job | FEED HOLD, then STOP. Note the line number, and later use **RUN FROM LINE** at the start of an operation. |
| Emergency | E-stop. Everything stops; you will need to re-enable, and usually re-home. |

**RUN FROM LINE** starts partway through, but it doesn't replay what came before: position, tool, tool length, work offset, spindle and coolant. Start at a line where the program sets all of them itself. In Fusion output, that's the comment line that begins an operation, right before its `T… M6`.

## Overrides during the job

- **Feed**: 100 % is what the CAM asked for. In soft materials it is usually safe to go above 100 % once you have heard the cut. In metal, raise it slowly and listen.
- **Spindle**: adjusts rpm live. On a VFD controlled over Modbus the change is immediate.
- **Rapid**: turn it down when a program has long rapids near clamps you are unsure of.

## Dry cutting aluminum (no coolant)

Without coolant, the risk is chips being re-cut and welding to the flute, which snaps small cutters. On the reference machine:

- **Single-flute cutters** (O-flute or 1F upcut): a deep flute, and the biggest possible chip per tooth.
- **Feed high enough to make real chips**: about 0.05–0.1 mm per tooth programmed. Thin chips rub and heat the tool.
- **Adaptive (trochoidal) roughing**: light radial engagement, full flute engagement in depth.
- **Air blast or vacuum at the cutter** for the whole run. That matters more than any feed setting.
