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
    # No stray leading/trailing whitespace.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    # No control characters other than tab/newline (DEL included).
    bad = [c for c in text if (ord(c) < 32 and c not in ("\t", "\n")) or ord(c) == 127]
    assert not bad, f"entry contains control character(s): {[hex(ord(c)) for c in bad]}"


def run_self_tests() -> None:
    """Negative self-tests: each bad input must FAIL validation as expected."""
    validate_entry(ENTRY)  # positive control: the real entry passes
    bad_cases = {
        "embedded control char": ENTRY.replace("guarded", "guard\x01ed"),
        "trailing whitespace": ENTRY + " ",
    }
    for name, bad_text in bad_cases.items():
        try:
            validate_entry(bad_text)
        except AssertionError:
            continue  # expected: validation rejected it
        raise AssertionError(f"self-test FAILED: {name} passed validation but must fail")
    print(f"self-tests passed ({len(bad_cases)} negative cases rejected as expected)")


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
    run_self_tests()
    main()
