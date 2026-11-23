"""One Word, First Thought — Sparta entry.

The entry is a single word: the first word that comes to mind.
No topic, no explanation, no second draft. The word is an
onomatopoeia with a wet, squelching sound in it — a word the
reader has almost never seen standing alone as an answer.
"""

import os
import re
import sys

TEXT = "squelch"


def main() -> int:
    text = TEXT
    # Gate: exactly one word — UTF-8, no spaces, no punctuation.
    if not text or text.strip() != text:
        print("gate failed: empty or surrounding whitespace", file=sys.stderr)
        return 1
    if not re.fullmatch(r"[A-Za-z]+", text):
        print("gate failed: entry must be exactly one word", file=sys.stderr)
        return 1
    if len(text.encode("utf-8")) != len(text):
        print("gate failed: entry must be ASCII", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "rb") as f:
        data = f.read()
    if data != text.encode("utf-8"):
        print("verification failed: entry.txt does not match TEXT", file=sys.stderr)
        return 1
    print(f"wrote {path}: {text!r} ({len(text)} chars, one word)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
