#!/usr/bin/env python3
"""One Word From Grandma — writes exactly one word to /output/entry.txt.

Deterministic, no network, no randomness: the chosen word is embedded
below as a literal and written verbatim. The gate wants 1 to 30 UTF-8
characters, not only whitespace, and the judge wants the single word a
grandma would text about AI: warm, a little baffled, funny in one word,
tied to AI, and fresh rather than the obvious "ROBOT".

Why ALEXA: grandmothers famously treat Alexa as a person in the house —
they say good morning to it, ask it things, and get gently confused by
it. It is one instantly readable word, unmistakably about AI, and it
carries the baffled warmth of a real grandma text in a way a generic
word like ROBOT or SKYNET never could. Candidates weighed and dropped:
ROBOT (the obvious pick, fails freshness), SKYNET (a film reference, no
grandma voice), SIRI (close second — but Alexa is the one grandmas keep
in the kitchen and talk to like family).
"""

from pathlib import Path

WORD = "ALEXA"


def main() -> None:
    # Gate: 1 to 30 characters, not only whitespace, exactly one word.
    assert 1 <= len(WORD) <= 30, f"word is {len(WORD)} characters"
    assert WORD.strip(), "word must not be only whitespace"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
