#!/usr/bin/env python3
"""Six Words, One Story - make.fun entry.

Writes one complete six-word story to /output/entry.txt.

The story: "She planted tulips. He never returned."
A whole arc in six words - planting as hope for a shared
future, "never returned" as the turn that closes it. Who he is,
why he left, and whether she is still waiting are left unsaid.
Every word earns its place: no filler, no word a better one
could replace, and the two short sentences read cleanly aloud.
"""

from pathlib import Path

STORY = "She planted tulips. He never returned."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        raise ValueError(f"expected exactly six words, got {len(words)}")
    if not 1 <= len(STORY) <= 60:
        raise ValueError("story must be 1-60 characters")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(STORY, encoding="utf-8")
    print(f"Wrote {len(words)}-word story ({len(STORY)} chars) to {OUTPUT}")


if __name__ == "__main__":
    main()
