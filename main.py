"""Fortune Cookie Wisdom for Developers — writes the entry to /output/entry.txt.

Why this line: it reads like a real fortune cookie — one short balanced
sentence that lands in a single breath — and it says something true about a
developer's day: code outlives its comments. The turn is quiet and fresh
rather than a reheated saying, and the second read rewards: the code your
future self will forgive is the code worth writing now.

The gate wants one line of 1 to 120 characters, UTF-8, not only whitespace.
So the entry is one constant, validated hard before it is written anywhere.
"""

import os

# The entry itself: one line, the fortune is about code outliving comments.
# Kept as a named constant so the choice is explicit and checkable.
ENTRY = "Your code will outlive your comments, so write the kind of code your future self will forgive."

OUTPUT_PATH = "/output/entry.txt"
# The gate allows 1 to 120 characters.
MAX_LENGTH = 120


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    # Guard: never submit a blank entry to the sealed gate.
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert len(text) <= MAX_LENGTH, (
        f"entry must be at most {MAX_LENGTH} chars, got {len(text)}"
    )
    # One line only: the gate reads a single fortune-cookie line.
    assert "\n" not in text, "entry must be a single line"
    # No stray leading/trailing whitespace: the gate reads the line as-is.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()
