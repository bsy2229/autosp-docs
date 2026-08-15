# Architecture

autosp is a single-file Python application: `autosp main branch v5.py`.

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

## Read-only backend

The backend `autosp mainbranch v3.py` is loaded read-only. Never modify it.