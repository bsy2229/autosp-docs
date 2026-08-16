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
  `_drop_items`, `_drop_counts`), never from `self` (CommandCentral).
- The goal is names that are reliable and responsive in LIVE STATISTICS.

## FILTERED PICKUPS counter (`_drop_counts`)

The FILTERED PICKUPS section is driven by `drops()` (`BackendManager`), which
aggregates the persistent per-name counter `_drop_counts[bot.name][name]`
(`{"qty", "vnum", "t"}`). This counter is bumped at every pickup-naming site
(`_bump_pickup_count`) in parallel with the rolling `_pickup_log`.

It exists because the rolling log is capped at 40 entries — once 40 unrelated
pickups pass, a tracked item scrolls out and FILTERED PICKUPS would show
"(no tracked drops yet)". The counter is never truncated, so tracked items stay
visible for the whole session regardless of log rotation.

- `drops()` filters the counter by the bot's owning-main tracked vnum set.
- `_stats_segments` reads `_drop_counts` (falling back to `_pickup_log`) for the
  per-row "last seen" timestamp.
- Gold entries are never counted (excluded in both `drops()` and the renderer).