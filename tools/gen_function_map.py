import ast
import io
from pathlib import Path

ROOT = Path(r"C:\Users\darke\Documents\GitHub\autosp")
FILES = ["autosp main branch v6.py", "autosp mainbranch v3.py"]
OUT = Path(__file__).resolve().parent.parent / "docs" / "function-map.md"


def doc_summary(node):
    ds = ast.get_docstring(node)
    if not ds:
        return ""
    first = ds.strip().splitlines()[0] if ds.strip() else ""
    return first.strip()


def sig_of(node):
    name = node.name
    args = ast.unparse(node.args) if node.args else ""
    if not args:
        return f"{name}()"
    return f"{name}({args})"


def render(node, out, depth=0):
    ds = doc_summary(node)
    pad = "  " * depth
    if ds:
        out.write(f"{pad}- **`{node.name}`** `{sig_of(node)}` — lines {node.lineno}–{node.end_lineno} · {ds}\n")
    else:
        out.write(f"{pad}- **`{node.name}`** `{sig_of(node)}` — lines {node.lineno}–{node.end_lineno}\n")


def collect(nodes, out, depth=0):
    for n in nodes:
        if isinstance(n, ast.ClassDef):
            out.write(f"\n### class `{n.name}` — lines {n.lineno}–{n.end_lineno}\n\n")
            collect(n.body, out, 0)
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            render(n, out, depth)
            nested = [c for c in n.body
                      if isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef))]
            if nested:
                out.write(f"{'  ' * depth}  *nested inside `{n.name}`:*\n")
                for c in nested:
                    render(c, out, depth + 1)


def build() -> str:
    out = io.StringIO()
    out.write("# Function map (auto-generated)\n\n")
    out.write("Exact line spans + class context + signature summary for every "
              "function in the active build. Use this to jump straight to the "
              "lines that implement any behaviour. Line numbers shift as the "
              "script evolves — if a span looks off, grep the symbol name.\n\n")
    out.write("- `autosp main branch v6.py` — the main script (GUI + engine)\n")
    out.write("- `autosp mainbranch v3.py` — backend, loaded in-process (read-only)\n\n")
    out.write("Regenerate: `python tools/gen_function_map.py`\n\n")

    for rel in FILES:
        p = ROOT / rel
        src = p.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(src)
        top = [n for n in tree.body if isinstance(n, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))]
        ncls = sum(1 for n in top if isinstance(n, ast.ClassDef))
        ndef = sum(1 for n in top if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)))
        out.write(f"\n## {rel} ({len(src.splitlines())} lines, {ndef} top-level defs, {ncls} classes)\n\n")

        for n in top:
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                render(n, out, 0)
                nested = [c for c in n.body
                          if isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef))]
                if nested:
                    out.write("  *nested inside:*\n")
                    for c in nested:
                        render(c, out, 1)

        for n in top:
            if isinstance(n, ast.ClassDef):
                out.write(f"\n### class `{n.name}` — lines {n.lineno}–{n.end_lineno}\n\n")
                collect(n.body, out)
    return out.getvalue()


if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8")
    print(f"wrote {OUT}")