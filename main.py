#!/usr/bin/env python3
"""Charm the Commuter entry.

Writes one line of weather forecast for a city that does not exist
to /output/entry.txt (UTF-8, inside the 1-140 character gate).
Deterministic, standard library only, no network, no environment
reads.

The line: Puddlewick: sunny intervals all morning, light drizzle
by lunch, and the ducks have formally requested the canal back by
Friday. It keeps the register of a real broadcast forecast (place
name, intervals, by lunch), gives the invented city one concrete
detail of its life (ducks, a canal, a formal request), and bends
the register at the end instead of dropping it. The smile comes
from the ducks filing paperwork: civic, patient, and certain the
canal is theirs by rights.
"""

import os

TEXT = (
    "Puddlewick: sunny intervals all morning, light drizzle by lunch, "
    "and the ducks have formally requested the canal back by Friday."
)


def main() -> None:
    # The gate requires 1-140 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 140, "entry must be 1-140 characters"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be exactly one line"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
