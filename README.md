# autosp-docs

Private engineering knowledge base (publicly mirrored for AI indexing).

This repo exists so AI assistants can stay current on the project's architecture,
key locations, and conventions without grepping the codebase. It contains only
documentation — no source, no credentials, no data.

## Contents

- `docs/architecture.md` — how the engine and GUI are wired together
- `docs/key-locations.md` — file paths and line-region anchors for the main script
- `docs/function-map.md` — every function in v6 + v3: exact line spans, class, signature, purpose
- `docs/code-index.md` — quick symbol→line lookup table
- `docs/pickup-naming.md` — how pickup names are resolved for LIVE STATISTICS
- `docs/config-format.md` — saved config, settings, and profile layout
- `context7.json` — controls what Context7 indexes

## Keeping it current

Every time the build changes in a way that affects architecture, pickup naming,
config, or known gotchas, update the relevant doc here and push. Context7 will
re-parse on its own schedule; you can also trigger a refresh from the library page.