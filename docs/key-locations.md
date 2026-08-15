# Key locations in the main script

Approximate anchors; line numbers shift as the script evolves. Grep for the
symbol names rather than relying on line numbers.

## Classes

- `CommandCentral` — the Tkinter GUI. Holds the manager as `self.mgr`.
- `BackendManager` — engine helpers and backend wiring.

## Important methods

- `_connect` (BackendManager) — registers callbacks.
- `_load_backend` — sandbox `exec` of `autosp mainbranch v3.py`; exposes
  `BotInstance`, `PhoenixBotAPI`, etc. via `BACKEND`.
- `_live_get_log` / `_stats_segments` (CommandCentral) — render LIVE STATISTICS.
- `_capture_pickup_history` — inventory-diff pickup naming.
- `_engine_poll_queries` — per-bot periodic queries.
- `_pickup_log`, `_pickup_names`, `_drop_items` — live pickup state, owned by
  BackendManager. Read them via `self.mgr`.

## Pickup naming sources

- Entity `items` cache (`_drop_items`).
- Sayi vnum lookups.
- Inventory-diff detection.

## Data files

- Log file (primary): `C:\debug_log.txt`.
- Saved config: `last_config.json`.
- Real config: `cfgs\config.json` (profile "KingVonFrmDaO").