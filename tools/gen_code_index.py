import io
import re
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\darke\Documents\GitHub\autosp")
FILES = ["autosp main branch v6.py", "autosp mainbranch v3.py"]
OUT = Path(__file__).resolve().parent.parent / "docs" / "code-index.md"


def build() -> str:
    out = io.StringIO()
    out.write("# Code index (auto-generated)\n\n")
    out.write("Snapshot of class/def locations in the active build. Line numbers "
              "shift as the script evolves — if a number looks off, grep for the "
              "symbol name instead.\n\n")
    out.write("- `main/autosp main branch v6.py` — the main script (GUI + engine)\n")
    out.write("- `autosp mainbranch v3.py` — backend, loaded in-process (read-only)\n\n")
    out.write("Regenerate: `python tools/gen_code_index.py`\n\n")
    for rel in FILES:
        p = ROOT / rel
        lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        out.write(f"\n## {rel} ({len(lines)} lines)\n\n")
        out.write("| Line | Kind | Symbol |\n|---|---|---|\n")
        for i, ln in enumerate(lines, 1):
            s = ln.strip()
            m = re.match(r"^(?:async\s+)?def\s+(\w+)", s)
            if m:
                out.write(f"| {i} | def | `{m.group(1)}` |\n")
                continue
            m = re.match(r"^class\s+(\w+)", s)
            if m:
                out.write(f"| {i} | class | `{m.group(1)}` |\n")
    return out.getvalue()


if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8")
    print(f"wrote {OUT}")