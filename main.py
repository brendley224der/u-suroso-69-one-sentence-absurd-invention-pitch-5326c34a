#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry.

The pitch: a smoke alarm that, instead of shrieking at burnt toast,
quietly opens a window, fans the smoke away, and leaves a
passive-aggressive note about your cooking.

The program writes the one sentence to /output/entry.txt. Pure standard
library, fully deterministic: the same sentence on every run.
"""

import os
import sys

PITCH = (
    "Meet the ToastSaver, a smoke alarm that, instead of shrieking at burnt "
    "toast, silently opens a window, fans the smoke away, and leaves a note "
    "reading: 'we need to talk about your cooking.'"
)

MAX_CHARS = 220

OUTPUT_PATH = "/output/entry.txt"


def check_pitch(text):
    """Refuse anything that would fail the gate: blank, only whitespace,
    over 220 characters, more than one line, or padded with whitespace."""
    if not text:
        sys.exit("pitch must not be empty")
    if not text.strip():
        sys.exit("pitch must not be only whitespace")
    if text != text.strip():
        sys.exit("pitch must have no leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        sys.exit(
            "pitch is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        sys.exit("pitch must be a single line")


def main():
    check_pitch(PITCH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PITCH + "\n")
    print(PITCH)


if __name__ == "__main__":
    main()
