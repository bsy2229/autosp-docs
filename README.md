# autosp-docs

Knowledge base for the autosp game-automation project. This public repo exists so
AI assistants (via Context7 / opencode) can stay current on the project's
architecture, key locations, and conventions without grepping the codebase.

The actual build lives in a private repo; this repo contains only documentation
and public configuration metadata (no license keys, no credentials, no code).

## Contents

- `docs/architecture.md` — how the engine and GUI are wired together
- `docs/key-locations.md` — file paths and line-region anchors for the main script
- `docs/pickup-naming.md` — how pickup names are resolved for LIVE STATISTICS
- `docs/config-format.md` — saved config, settings, and cfgs/profile layout
- `context7.json` — controls what Context7 indexes

## Keeping it current

Every time the build changes in a way that affects architecture, pickup naming,
config, or known gotchas, update the relevant doc here and push. Context7 will
re-parse on its own schedule; you can also trigger a refresh from the library page.