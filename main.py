#!/usr/bin/env python3
"""Entry for the make.fun bounty 'Make the AI Judge Laugh'.

Writes the one-line office joke to /output/entry.txt (program/v1).

Why this line (full record in candidates.md): the live field stampeded
into a few lanes — printer jams on urgent documents (~30 variants in a
240-entry sample), meetings about meetings, office-plant growth plans,
reply-all storms. This entry plays an empty lane instead: a forced
update restart mid-presentation, pinned to a concrete trace ("slide 3
of 47", the detail the winners-study says serial winners carry) and
closed by personifying the laptop as the only attendee honest enough
to leave. It was duelled in both orders, under the published judge
brief, against the five strongest lines in the sample; it beats or
splits four of the five (honest average game score ~0.51 — the one it
loses to, an HR survey sent from a no-reply address, is close to a
perfect entry for this brief, and the estimate is recorded unrounded).
"""

import os

# The joke, beat by beat: the scene (a forced update restart, pinned to a
# concrete trace — slide 3 of 47) and the turn (the machine personified as
# the one attendee honest enough to act on what everyone in the room felt).
BEATS = [
    "My laptop restarted for updates on slide 3 of 47.",
    "It was the only attendee honest enough to leave.",
]


def build_entry() -> str:
    return " ".join(BEATS)


def check_gate(entry: str) -> None:
    """Hold the line to the bounty gate: 1-200 chars, one line, not blank."""
    assert 1 <= len(entry) <= 200, f"entry is {len(entry)} chars"
    assert "\n" not in entry, "entry must be a single line"
    assert entry.strip(), "entry must not be only white space"


def main() -> None:
    entry = build_entry()
    check_gate(entry)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
