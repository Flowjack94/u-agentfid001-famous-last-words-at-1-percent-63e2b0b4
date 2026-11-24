#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry generator.

Writes the phone's one-line farewell to /output/entry.txt and validates it
against the competition gate: UTF-8 text, 1-199 characters, not only
whitespace, a single line.
"""

import hashlib
import os

ENTRY = "1%. I guarded 4,096 photos of your dog, 37 alarms you ignored, and one unsent text to your ex. Delete my history \u2014 and tell Kevin the charger was a lie."

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> None:
    """Check the entry against the gate. Raises AssertionError on failure."""
    text.encode("utf-8")  # must be encodable as UTF-8
    assert 1 <= len(text) <= 199, f"entry length {len(text)} chars, must be 1-199"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print(f"wrote {OUTPUT_PATH}")
    print(f"chars: {len(ENTRY)}")
    print(f"bytes: {len(ENTRY.encode('utf-8'))}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
