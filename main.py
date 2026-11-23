#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters or fewer.

Writes one original deadpan excuse from a robot vacuum for missing a
spot to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

v1 line: the vacuum's lidar reclassifies the missed crumb as a
load-bearing part of the floor, logs it as structural dust, and
docks before its battery can object.

Revision 2 (v3): restored a middle beat, but with a new joke instead
of the cut one — the vacuum "logs it as a permanent resident",
granting the crumb tenancy. Three beats now, each earning its place:
smug sensor classification, the crumb becoming a resident, and the
warranty punch at the end.
"""

import os

LINE = (
    "My lidar classified the crumb as a load-bearing part of the floor, "
    "so I left it, logged it as a permanent resident, and docked. "
    "My warranty does not cover heroics."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be one line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
