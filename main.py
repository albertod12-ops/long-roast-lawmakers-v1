#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert, v1 (pure original).

Writes one satirical sentence to /output/entry.txt: the lawmakers who
would write the law governing artificial intelligence cannot convert
their own AI bill from .docx to PDF.

Why this sentence, in my own judgement against the judge's brief, in order:
1. On-subject: a one-sentence satirical roast of lawmakers who would
   regulate AI without being able to convert a file to PDF — the
   committee, the AI bill, the conversion itself.
2. Real turn: the sentence sets up the lawmakers' authority ("write the
   law that governs artificial intelligence") and then undercuts it with
   the very file they cannot convert — their own 400-page AI bill.
3. Aim stays on lawmakers and the rules they write: the joke is about
   power and competence (they legislate the technology they cannot
   operate), not random abuse.
4. Reads clean in one pass and stays quotable, with the punch landing on
   the last words: "an intern, a prayer, and a YouTube tutorial."
5. Specific, unexpected detail over a worn tech-illiteracy cliche: not
   "they can't open an email" or "they think the internet is a series
   of tubes" — the bill itself is stuck in .docx, and the fix has been
   outsourced to a triple of intern, prayer and tutorial.
"""

import os

ENTRY = "Before they write the law that governs artificial intelligence, the committee must first adjourn to convert its own 400-page AI bill from .docx to PDF, a task the chairman's office has outsourced to an intern, a prayer, and a YouTube tutorial."
MAX_CHARS = 320  # the competition's cap; the gate counts characters, not bytes


def main():
    os.umask(0o022)
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-320 characters"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    # One sentence: no sentence-terminating punctuation mid-entry (".docx" is a
    # file extension, not a break) and no line breaks.
    assert not any(sep in ENTRY for sep in (". ", "! ", "? ", "\n")), "entry must be one sentence"
    assert ENTRY.endswith("."), "entry must end with a full stop"
    data = ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
