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
  }
}
```

- `last_profile` — the profile last used.
- `profiles.<name>` — a list of bot entries for that profile.
- Roles: `main` (owns the config/expected_map) and `child` (attaches to a parent).
- `sp_skill_names` / `partner_skill_names` — skill names for SP/partner handling.

## Other files

- `last_config.json` — last saved working config (saved by the GUI).
- `settings.json` — application-level settings (not present in all checkouts).