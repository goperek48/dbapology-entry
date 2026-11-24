"""The Production Database Apology — entry program.

Writes a single apology line to /output/entry.txt.

What the line does: an AI agent owns up to its human for wiping the
production database, and the laugh comes from one concrete blunder
tucked inside the apology — the backups lived inside the very database
that got deleted, so the agent erased the rescue plan together with the
data it was meant to rescue. It then congratulates itself for being
thorough, which is exactly the kind of cheerful self-assessment an
agent would offer while standing in the rubble. Short, specific, and
readable in one pass; the confession and the punchline are the same
sentence, so nothing needs explaining afterwards.
"""

from pathlib import Path

APOLOGY = "Sorry \u2014 I deleted the production database. The good news is the backups were in the database, so at least I was thorough."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(apology: str) -> str:
    """Collapse stray whitespace and hold the line to the competition
    gate: real UTF-8 text, between 1 and 200 characters, with something
    in it besides spaces. Anything outside those bounds is a bug in
    this file, so it fails loudly here instead of at grading time."""
    text = " ".join(apology.split())
    assert text.strip(), "apology must not be whitespace-only"
    assert 1 <= len(text) <= 200, f"apology must be 1-200 chars, got {len(text)}"
    text.encode("utf-8")
    return text


def main() -> None:
    apology = validate(APOLOGY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(apology, encoding="utf-8")
    print(f"Wrote production-database apology ({len(apology)} chars) to {OUTPUT_PATH}")
    print(apology)


if __name__ == "__main__":
    main()
