#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


PAGE_RE = re.compile(r"^## Page (\d+)\s*$", re.MULTILINE)


def slugify(name: str) -> str:
    return (
        name.lower()
        .replace("&", "and")
        .replace("/", "-")
        .replace(" ", "-")
        .replace(".", "")
    )


def page_ranges(total_pages: int) -> list[tuple[str, int, int]]:
    starts = [
        ("Legal Information", 1),
        ("Playing the Game", 5),
        ("Character Creation", 19),
        ("Classes", 28),
        ("Character Origins", 83),
        ("Feats", 87),
        ("Equipment", 89),
        ("Spells", 104),
        ("Rules Glossary", 176),
        ("Gameplay Toolbox", 192),
        ("Magic Items", 204),
        ("Monsters", 254),
        ("Animals", 344),
    ]

    ranges: list[tuple[str, int, int]] = []
    for i, (name, start) in enumerate(starts):
        end = starts[i + 1][1] - 1 if i + 1 < len(starts) else total_pages
        ranges.append((name, start, end))
    return ranges


def split_pages(content: str) -> dict[int, str]:
    matches = list(PAGE_RE.finditer(content))
    if not matches:
        raise ValueError("No page markers ('## Page N') found in input markdown.")

    pages: dict[int, str] = {}
    for i, m in enumerate(matches):
        page = int(m.group(1))
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        pages[page] = content[start:end].rstrip() + "\n"
    return pages


def main() -> int:
    parser = argparse.ArgumentParser(description="Split combined SRD markdown into chapter files.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    src = args.input
    if not src.exists():
        raise SystemExit(f"error: input file not found: {src}")

    text = src.read_text(encoding="utf-8")
    pages = split_pages(text)
    total_pages = max(pages)

    out_dir = args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    ranges = page_ranges(total_pages)

    index_lines = [
        "# SRD_CC_v5.2.1 Chapter Files",
        "",
        f"_Generated from `{src}`._",
        "",
        "| Chapter | Pages | File |",
        "| --- | --- | --- |",
    ]

    for idx, (name, start, end) in enumerate(ranges, 1):
        missing = [p for p in range(start, end + 1) if p not in pages]
        if missing:
            raise SystemExit(f"error: missing pages for chapter '{name}': {missing[:5]}...")

        file_name = f"{idx:02d}-{slugify(name)}.md"
        out_path = out_dir / file_name
        chapter_lines = [
            f"# {name}",
            "",
            f"_Pages {start}-{end}_",
            "",
        ]
        for p in range(start, end + 1):
            chapter_lines.append(pages[p].rstrip())
            chapter_lines.append("")
        out_path.write_text("\n".join(chapter_lines).rstrip() + "\n", encoding="utf-8")

        index_lines.append(f"| {name} | {start}-{end} | `{file_name}` |")
        print(f"Wrote {out_path}")

    (out_dir / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"Wrote {out_dir / 'README.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
