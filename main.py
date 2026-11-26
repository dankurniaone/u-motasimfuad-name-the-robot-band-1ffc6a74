"""Name the Robot Band — make.fun entry.

Writes one line to /output/entry.txt: the robot band name plus its hit single.
Gate: UTF-8, 1-200 chars. The line below is 64 chars, 136 spare.
"""
import sys
from pathlib import Path

LINE = "The CAPTCHAs \u2014 hit single 'Prove You're Not a Robot (We Can't)'."

def main(argv):
    if "--check" in argv:
        n = len(LINE)
        print(f"VALID: {n} chars, {len(LINE.split())} words, {200 - n} spare under the 200-char gate")
        return 0
    if "--self-test" in argv:
        out = Path("/tmp/robot-band-self-test.txt")
        out.write_text(LINE + "\n", encoding="utf-8")
        again = out.read_text(encoding="utf-8")
        assert again == LINE + "\n"
        print("self-test: byte-identical")
        return 0
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars to {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
