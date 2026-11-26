#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun bounty entry.

Writes the single status update to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The text is fixed: every run writes
the exact same bytes. Standard library only, no network, no input.

The line: a lost sock reports in from inside the vacuum cleaner,
where the dust bunnies have elected it mayor. The joke dodges the
two obvious sock clichés entirely — no dryer, no missing partner —
and lands its punchline on a campaign platform that only a vacuum
could run on: "less sucking, more snacks." The setup is a diary-style
status log ("Day 12"), the turn is the election, and the punchline
lands in the last few words. It sounds like a sock: small, domestic,
a little anxious, and suddenly, absurdly, in charge.
"""

import os
from pathlib import Path

ENTRY = (
    "Day 12 inside the vacuum cleaner. "
    "The dust bunnies elected me mayor. "
    "My platform: less sucking, more snacks."
)

# Gate: UTF-8 text of 1 to 120 characters, not only white space.
MAX_CHARS = 120


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
