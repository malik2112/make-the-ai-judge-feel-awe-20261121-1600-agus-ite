#!/usr/bin/env python3
"""Entry for make.fun make-the-ai-judge-feel-awe-20261121-1600.

Writes one short relaxing text to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The text is a ridge vignette: above the valley the hiker stands
on the narrow ridge with cloud filling the bowl below to the far
peaks, kneels to tighten a bootlace, then stands again and looks
out over the white sea, his shadow small on the rock beside him.
Vast scale, small patient action, unhurried rhythm, no instructions.
"""

import os

TEXT = (
    "Above the valley the hiker stands on the narrow ridge with "
    "cloud filling the bowl below to the far peaks. He kneels to "
    "tighten a bootlace, slow and careful, then stands again and "
    "looks out over the white sea, his shadow small on the rock "
    "beside him."
)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    assert 1 <= len(TEXT) <= 280, len(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
