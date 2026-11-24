#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line, at most 120 characters, to /output/entry.txt:
the error message a kitchen toaster shows its owner.

The line: deadpan resignation from a toaster outclassed by the air fryer.
No network, no randomness, no secrets — the same bytes every run.
No trailing newline: the gate counts characters, and the byte tie-break
rewards the shorter file.
"""

import sys

LINE = "ERROR: The air fryer does it faster. I have accepted this."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 120, "entry must be 1-120 characters"
    assert LINE.strip() == LINE and LINE, "entry must not be blank or padded"
    path = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_PATH
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
