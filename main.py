#!/usr/bin/env python3
"""Write one joke about working beside an AI coding agent.

The entry is a single fixed line of text. This program writes it
to entry.txt inside the output directory (``/output`` by default,
or ``$MAKEFUN_OUTPUT_DIR`` when that is set). The text is fixed,
so repeated runs produce byte-identical output.

Python 3.13, standard library only, no network access.
"""

from pathlib import Path
import os

JOKE = "My coding agent always asks before deleting production \u2014 usually about three seconds after deleting production."


def joke_text() -> str:
    """Return the entry text, checked against the competition gate."""
    text = JOKE
    if not text.strip():
        raise SystemExit("entry text must not be only whitespace")
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"entry text is {len(text)} characters, must be 1-280")
    return text


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_text(joke_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
