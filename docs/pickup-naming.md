# Pickup naming (LIVE STATISTICS)

Pickup names shown in LIVE STATISTICS are resolved from three sources, in order
of reliability:

1. **Entity items cache** (`_drop_items`) — the engine caches item info for
   entities it observes.
2. **Sayi vnum** — item vnum lookups used to translate raw ids to names.
3. **Inventory-diff** — `_capture_pickup_history` compares inventory snapshots
   to detect what was actually gained.

The inventory-diff path depends on fresh `bot._inv_qty_by_name` snapshots, which
only update when a `query_inventory()` (type-17) response arrives. The engine
runs a background `_inventory_poll_loop` (started in `engine_start`, interval
10s) to keep those snapshots current. Without it, inventory only refreshes when
the ITEM FILTERS picker forces a `query_inventory()` — so the rolling log would
stay empty until the user opened the filter picker.

## Rules

- Pickup naming callbacks execute in `BackendManager`.
- The renderer lives in `CommandCentral`.
- Always read pickup data via `self.mgr` (`_pickup_log`, `_pickup_names`,
  `_drop_items`), never from `self` (CommandCentral).
- The goal is names that are reliable and responsive in LIVE STATISTICS.