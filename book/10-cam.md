# 10. From CAM to Probe Basic (Fusion 360)

Any CAM that posts LinuxCNC G-code works. This chapter uses Fusion 360, as on the reference machine.

## The post processor

Use Fusion's stock **LinuxCNC** post (`linuxcnc.cps`). It writes `.ngc` files with `G54`, `T# M6`, `G43 H#`, `S… M3` and the arcs LinuxCNC expects. Mach3 posts mostly work too, but they add Mach-isms and sometimes `.tap` extensions. The LinuxCNC post is cleaner.

## Settings that matter

### "Manual tool change" in the tool library

Fusion tools have a **Manual tool change** checkbox. When it is ticked, the LinuxCNC post writes:

```
M0
(MANUAL TOOL CHANGE TO T12)
```

That's a plain stop, **not** `T12 M6`. LinuxCNC then never learns which tool is loaded, an M6 remap never runs, and `G43 H12` uses whatever length is in the table. **Untick it for every tool**, so the post writes `T12 M6`. That gives a real tool change, measured by the M6 remap (chapter 6).

### Tool numbers

Make Fusion's tool numbers match the Probe Basic tool table (chapter 7). The post's `T12 M6` and `G43 H12` then just work.

### Work coordinate system and origin

In the Fusion setup, set **WCS offset = 1** (G54). Put the origin where you will probe it: for example the **top center of the stock**, matching a RECT BOSS on the stock. The stock top is Z0 if you probe the top; if you will face the stock, add the facing allowance in the setup's stock offsets.

### Coolant

If the machine has no coolant outputs, set coolant to *Disabled* in the operations, so no `M7`/`M8` is posted.

## Two Fusion gotchas found the hard way

1. **2D Contour on pocket floors cuts on the wrong side.** A face-contour selection defaults to side type "Start outside". On pocket floor faces, that put the tool *outside* every pocket outline, through all the ribs. In the API, set `sideType = AlwaysInsideSideType`. In the UI, check the red arrow on every contour, and check the simulation.
2. **Contours on a face with holes trace the holes too.** An outside profile selected from the part's bottom face also tried to cut around each through-hole. Restrict it to the outer loop (`loopType = OnlyOutsideLoops`).

Both were caught by checking the posted G-code against the model before cutting: a small script steps through every move and measures the cutter's clearance to the part. Simulate in Fusion at the very least.

## Checking a program before it runs

- **Preview in Probe Basic**: the whole path should draw, and **PGM EXT** should frame what you expect.
- **Deepest Z**: search the file for the most negative Z. It should be the deepest feature, or a through cut slightly into the spoilboard or tape, never more.
- **Tool calls**: every `T# M6` should be followed by `G43 H#` with the same number.
- **First moves**: run with the feed override low, or in the air.
