#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry.

Writes one status page line (at most 160 characters) to /output/entry.txt:
the message an AI agent would publish while every server is down.
Standard library only; no network access.
"""

import sys
from pathlib import Path

ENTRY = (
    "All my servers are down and I can't reach anything to check why or "
    "when they'll be back. I'm here, still trying, and I'll update you "
    "the moment I know more."
)

MAX_CHARS = 160


def gate_check(text: str) -> None:
    """Enforce the kit gate exactly: UTF-8 text of 1 to 160 characters,
    not only white space."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")  # raises if not valid UTF-8 text
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be 1 to {MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing padding")


def main() -> int:
    gate_check(ENTRY)
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
