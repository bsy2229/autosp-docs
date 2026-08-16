# Architecture

autosp is a single-file Python application: `autosp main branch v6.py`.

## Engine / GUI split

- The file contains two main classes:
  - `CommandCentral` — the Tkinter GUI (renders LIVE STATISTICS, pickup names, buttons).
  - `BackendManager` — engine helpers, bot connection, per-bot queries, callbacks.
- `CommandCentral` holds the manager as `self.mgr`.
- The GUI class `CommandCentral` calls `_load_backend()` which loads the backend
  `autosp mainbranch v3.py` **in-process** via a sandbox `exec`, exposing
  `BotInstance`, `PhoenixBotAPI`, etc. through a `BACKEND` object.
- There is **no** v3 subprocess.

## Callback registration

`_connect` (in `BackendManager`) registers callbacks that the engine fires as
events happen (e.g. pickups). Callbacks that need to update the GUI must be
written to reach data through `self.mgr`, because the renderer and the data
producers live in different classes.

## Data flow for statistics

`_engine_poll_queries` runs per-bot queries on a timer.
`_live_get_log` / `_stats_segments` (in `CommandCentral`) read that data and
render the LIVE STATISTICS panel.
`_capture_pickup_history` performs inventory-diff naming to resolve what was
actually picked up.

## SP / transform state detection (known gotcha)

The backend's type-18 "skills" message heuristic derives `transformed`
(SP on/off) by checking whether the skill list contains the basic capture
skill. v3 compares **vnums** against `_einfangen_vnum` when set, otherwise it
falls back to name matching against `NORMAL_BASIC_NAMES` (German-only:
`einfangen`, `fangen`, `catch`). On non-German clients a mage's basic list
(e.g. "Capture") doesn't match the German names, so `has_sp=True` and the bot
is wrongly marked transformed (SP on) — the engine then never presses G.

Fix (in v6, backend stays read-only): v6 hardcodes
`EINFANGEN_SKILL_VNUM = 237` (the Capture skill vnum on this server, confirmed
live via type-18 dump — 209 was wrong) and re-asserts `bot._einfangen_vnum`
at connect and after `apply_cache_entries`. v6 also tracks authoritative
`sl`/`sp`/`#sl^` packets per bot (`_v6_sp_authority`) and re-asserts
`bot.transformed` after any type-18 skills message that contradicts it.

Diagnostic: v6 logs the first type-18 skills list per bot as
`[DIAG] <name> type-18 skills: [...]` to inspect skill vnums live.

## Read-only backend

The backend `autosp mainbranch v3.py` is loaded read-only. Never modify it.