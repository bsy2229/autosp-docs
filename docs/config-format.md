# Config format

## cfgs\config.json

Top-level structure:

```json
{
  "last_profile": "MainProfile",
  "profiles": {
    "MainProfile": [
      { "name": "MainChar", "role": "main",
        "config": "C:\\Games\\Example\\main.ini",
        "expected_map": 0,
        "partner_skill_names": [],
        "sp_skill_names": [ "Skill A", "Skill B", ... ] },
      { "name": "AltChar", "role": "child", "parent": "MainChar",
        "config": null, "expected_map": null,
        "partner_skill_names": [], "sp_skill_names": [] },
      ...
    ]
  },
  "settings": {
    "config_dir": "C:/Games/Example",
    "discord_webhook": { "MainProfile": "https://discord.com/api/webhooks/..." },
    "discord_webhook_sent": { "MainProfile": "2026-08-15" },
    "tracked_items_by_main": { "MainChar": [1012, 1007] },
    "partner_names": [ "CharA", "CharB" ],
    "tracked_items": [1012, 1007],
    "dump": { ... },
    "human": { ... },
    "mob_range": ...
  },
  "get_map": { "<ground-drop-object-id>": { "name": ..., "vnum": ..., ... } }
}
```

- `last_profile` — the profile last used (TOP-LEVEL key; used by the Discord webhook profile lookup).
- `profiles.<name>` — a list of bot entries for that profile.
- Roles: `main` (owns the config/expected_map) and `child` (attaches to a parent).
- `sp_skill_names` / `partner_skill_names` — skill names for SP/partner handling.
- `settings.discord_webhook` — per-profile webhook URL. Read by `_discord_webhook_url`.
- `settings.discord_webhook_sent` — per-profile marker of the last calendar day already delivered; prevents duplicate Discord sends. Written after a successful send.
- `settings.partner_names` / `settings.tracked_items` / `settings.config_dir` and the top-level `get_map` — read by `_load_backend` (v7) after it redirects `CFGS_DIR` to `%LOCALAPPDATA%\Autosp\cfgs`. If these are missing from that per-user config, LIVE STATISTICS pickup naming comes up blank even though the workspace copy has them. v7 recomputes `CONFIGURED_PARTNER_NAMES`, `TRACKED_ITEMS`, `GET_MAP`, `CONFIG_DIR` from the REDIRECTED file (v7 `_load_backend` ~145–191), so the canonical config must live at `%LOCALAPPDATA%\Autosp\cfgs\config.json`.

## Gotchas (Discord webhook)

- The profile is resolved as `CURRENT_PROFILE` → top-level `last_profile` → `settings.last_profile` (backwards-compat). `last_profile` lives at the TOP level of config.json, NOT inside `settings`.
- Day totals files (`<pickup summaries>/<bot>/day/YYYY-MM-DD.txt`) have NO `Ended:` line (only raw per-run files do), so webhook gathering must not require one.
- The "sent day" marker is set after a successful 2xx POST, once per calendar day.

## Other files

- `last_config.json` — last saved working config (saved by the GUI).
- `settings.json` — application-level settings (not present in all checkouts).