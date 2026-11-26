#!/usr/bin/env python3
"""Robot band name entry for make.fun.

The program carries one line: a robot band name together with its hit
single. Running it with no arguments writes that line to
/output/entry.txt. The gate allows UTF-8 text of 1 to 200 characters;
this line is 64 characters, so 136 characters of headroom remain.

Usage:
    python3 main.py            write the entry
    python3 main.py --check    report the character count and gate margin
    python3 main.py --self-test  round-trip the line through a temp file
    python3 main.py --tournament  print the candidate tournament table
"""

import sys
from pathlib import Path

BAND_LINE = "The CAPTCHAs \u2014 hit single 'Prove You're Not a Robot (We Can't)'."
GATE_MAX = 200
ENTRY_PATH = Path("/output/entry.txt")

# Candidate tournament, scored on specificity / surprise / freshness.
# Winner: The CAPTCHAs, 5/5/4 = 14. Runner-up: The Servo Motors, 5/4/4 = 13.
TOURNAMENT = [
    ("The CAPTCHAs", "Prove You're Not a Robot (We Can't)", 5, 5, 4),
    ("The Servo Motors", "We Only Move When Told", 5, 4, 4),
    ("Error 404", "Band Not Found", 3, 3, 2),
    ("Beep Boop & The Boops", "Beep Boop Boop", 3, 2, 2),
    ("The Algorithm", "You Will Like This Song", 4, 3, 3),
]


def show_tournament() -> int:
    """Print the candidate table with scores."""
    print(f"{'band':<28} {'hit single':<32} spec/surp/fresh  total")
    for band, song, spec, surp, fresh in TOURNAMENT:
        print(f"{band:<28} {song:<32} {spec}/{surp}/{fresh}      {spec + surp + fresh}")
    return 0


def check_line() -> int:
    """Print the line's length and how much gate room is left."""
    size = len(BAND_LINE)
    words = len(BAND_LINE.split())
    print(f"VALID: {size} chars, {words} words, {GATE_MAX - size} spare of {GATE_MAX}")
    return 0


def self_test() -> int:
    """Write the line to a scratch file and read it back unchanged."""
    scratch = Path("/tmp/robot-band-roundtrip.txt")
    scratch.write_text(BAND_LINE + "\n", encoding="utf-8")
    back = scratch.read_text(encoding="utf-8")
    if back != BAND_LINE + "\n":
        print("self-test: MISMATCH")
        return 1
    print("self-test: byte-identical")
    return 0


def write_entry() -> int:
    """Write the band line to the entry path."""
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(BAND_LINE, encoding="utf-8")
    print(f"wrote {len(BAND_LINE)} chars to {ENTRY_PATH}")
    return 0


def main(argv: list[str]) -> int:
    if "--check" in argv:
        return check_line()
    if "--self-test" in argv:
        return self_test()
    if "--tournament" in argv:
        return show_tournament()
    return write_entry()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
