# Pickup naming (LIVE STATISTICS)

Pickup names shown in LIVE STATISTICS are resolved from three sources, in order
of reliability:

1. **Entity items cache** (`_drop_items`) — the engine caches item info for
   entities it observes.
2. **Sayi vnum** — item vnum lookups used to translate raw ids to names.
3. **Inventory-diff** — `_capture_pickup_history` compares inventory snapshots
   to detect what was actually gained.

## Rules

- Pickup naming callbacks execute in `BackendManager`.
- The renderer lives in `CommandCentral`.
- Always read pickup data via `self.mgr` (`_pickup_log`, `_pickup_names`,
  `_drop_items`), never from `self` (CommandCentral).
- The goal is names that are reliable and responsive in LIVE STATISTICS.