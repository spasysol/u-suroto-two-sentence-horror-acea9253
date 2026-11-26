"""Two-Sentence Horror entry for make.fun bounty u-suroto-two-sentence-horror-acea9253.

Writes one horror story of exactly two sentences (at most 400 characters)
to /output/entry.txt. Python 3.13, standard library only, no network,
no input files.
"""

import os

STORY = (
    "The lighthouse log says the light went out for nine minutes the night "
    "my father drowned, and no one ever found out why. I found his last "
    "entry this morning: 'The light never went out \u2014 something stood "
    "in front of it.'"
)

MAX_CHARS = 400
OUTPUT_PATH = "/output/entry.txt"


def count_sentences(text):
    """Count sentence-ending periods, ignoring a closing quote after one."""
    stripped = text.rstrip("\"'")
    return stripped.count(".")


def validate(text):
    """Check the story meets the gate: 1-400 chars, exactly two sentences."""
    if not text or text.isspace():
        raise SystemExit("story must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "story must be at most %d characters, got %d" % (MAX_CHARS, len(text))
        )
    stripped = text.rstrip("\"'")
    if not stripped.endswith("."):
        raise SystemExit("story must end with a full stop")
    if count_sentences(text) != 2:
        raise SystemExit(
            "story must be exactly two sentences, got %d"
            % count_sentences(text)
        )
    return text


def write_entry(text):
    """Write the validated story to /output/entry.txt, world-readable."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


def main():
    write_entry(validate(STORY.strip()))


if __name__ == "__main__":
    main()
