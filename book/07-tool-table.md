# 7. The tool table

<!-- shot: tool-tab -->

## Where it lives

Probe Basic 1.0.x can keep the tool table in an **SQLite database** instead of LinuxCNC's classic `tool.tbl` text file. The INI selects it:

```
[EMCIO]
DB_PROGRAM = ./tool_db.sh
TOOL_DB_FILE = 6040_tools.db
```

`tool_db.sh` starts QtPyVCP's `tool_db_backend`, which answers LinuxCNC's tool queries from the database. The TOOL tab edits the same file. One database is the single source of truth: diameter, length, remark and the ATC flag.

## Columns

| Column | Meaning |
|---|---|
| T | Tool number: what `T5` and `H5` refer to. |
| P | Pocket. Only matters for an ATC. |
| Z | Tool length (from the setter). |
| D | Diameter: used by cutter compensation and the preview, and by the probe routines for the ball. |
| ATC | Whether the tool fits the automatic changer's carousel. Unused without an ATC. |
| Remark | Free text: maker, flute count, stick-out, collet. |

Edit cells, then **SAVE TABLE**. **ADD TOOL** and **DELETE** manage rows. **UPDATE LOADED TOOL** pushes edits for the tool in the spindle.

## Numbering advice

- **Use the same numbers as your CAM library.** If Fusion's library has your 1/8" O-flute as tool 12, make it T12 here too. Then posted programs need no renumbering.
- **Reserve a high number for the probe** (99 is conventional), so a program can never call it by accident.
- **Put stick-out and collet in the remark**, so the next time you load the tool you set the same length.

## If LinuxCNC says "tool not found in tool table"

The database file is probably fine, but LinuxCNC's in-memory copy isn't. A restart of LinuxCNC reloads it. On the reference machine this happened because a tool process from an earlier LinuxCNC session was still running alongside the new one. Chapter 11 has the full story and the fix.
