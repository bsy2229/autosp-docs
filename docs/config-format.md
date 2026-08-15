# Config format

## cfgs\config.json (real config, profile "KingVonFrmDaO")

Top-level structure:

```json
{
  "last_profile": "KingVonFrmDaO",
  "profiles": {
    "KingVonFrmDaO": [
      { "name": "KingVonFrmDaO", "role": "main",
        "config": "E:\\Games\\Nostale\\merlin räuberinnenhof.ini",
        "expected_map": 193,
        "partner_skill_names": [],
        "sp_skill_names": [ "Lichtstrahl", "Lichtknall", ... ] },
      { "name": "DurkioKrazy", "role": "child", "parent": "KingVonFrmDaO",
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