#!/usr/bin/env python3
"""Generate JSONL (one record per line, for RAG/agents) for the merged collections.

Sources of truth:
  awesome-anime-ai-characters/README.md        -> characters.jsonl
  entertainment-ai-2026-code-models/papers.json -> papers.jsonl
  entertainment-ai-2026-code-models/entertainment-research-2026.json -> entertainment-research-2026.jsonl

Usage: export_collections.py [--check]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AWESOME = ROOT / "awesome-anime-ai-characters"
ENT = ROOT / "entertainment-ai-2026-code-models"
BULLET = re.compile(r"^- \[([^\]]+)\]\((https?://[^)]+)\) — (.+)$")


def characters():
    section = None
    out = []
    for line in (AWESOME / "README.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        m = BULLET.match(line)
        if m and section and section != "探し方・掲載基準":
            out.append({"name": m[1], "url": m[2], "section": section, "description_ja": m[3]})
    return out


def dump(rows):
    return "".join(json.dumps(r, ensure_ascii=False, sort_keys=False) + "\n" for r in rows)


def build():
    ent = json.loads((ENT / "entertainment-research-2026.json").read_text(encoding="utf-8"))
    sig = json.loads((ENT / "papers.json").read_text(encoding="utf-8"))
    return {
        AWESOME / "characters.jsonl": dump(characters()),
        ENT / "papers.jsonl": dump([{"collection": "siggraph-2026", **p} for p in sig["papers"]]),
        ENT / "entertainment-research-2026.jsonl": dump(ent["papers"]),
    }


def main():
    files = build()
    if "--check" in sys.argv:
        stale = [str(p.relative_to(ROOT)) for p, c in files.items()
                 if not p.exists() or p.read_text(encoding="utf-8") != c]
        if stale:
            sys.exit("out of date (run scripts/export_collections.py): " + ", ".join(stale))
        print(f"Checked {len(files)} collection files")
        return
    for p, c in files.items():
        p.write_text(c, encoding="utf-8")
        print(f"wrote {p.relative_to(ROOT)} ({c.count(chr(10))} records)")


if __name__ == "__main__":
    main()
