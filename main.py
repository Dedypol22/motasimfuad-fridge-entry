"""Passive-aggressive fridge note entry for make.fun.

The joke is a courtroom exhibit: the fridge presents its broken ice
maker as evidence, then delivers the sting -- it is also the jury.
"""

import os
from pathlib import Path

LINE = "Exhibit A: the ice maker. You broke it in March, blamed me, and still demand cubes. The jury is me."
# Coordinator (25 Nov 2026): LINE 99 chars / 100 bytes entry.txt, verified 2 runs neutral-cwd; submit before R1 cutoff 20:45 WIB.


def _output_dir() -> Path:
    """Resolve MAKEFUN_OUTPUT_DIR, relative paths against this file."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = Path(raw)
    if not path.is_absolute():
        path = Path(__file__).resolve().parent / path
    return path


def main() -> int:
    out_dir = _output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")
    read_back = target.read_text(encoding="utf-8")
    assert read_back == LINE + "\n", "entry.txt content mismatch"
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
