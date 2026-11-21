"""One-line joke about working beside an AI coding agent.

The program writes a single fixed joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set). The joke is a
fixed string, so every run produces byte-identical output.
Pure Python 3.13 standard library; no network use.
"""

import os

JOKE = (
    "My coding agent always asks before deleting production "
    "— usually about three seconds after deleting production."
)


def main() -> None:
    text = JOKE
    if not 1 <= len(text) <= 280:
        raise SystemExit("joke must be 1-280 characters")
    if not text.strip():
        raise SystemExit("joke must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
