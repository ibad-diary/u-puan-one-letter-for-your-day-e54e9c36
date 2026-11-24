#!/usr/bin/env python3
"""One Letter for Your Day — entry: D.

The letter stands for the word behind the day: doomscrolling, a day
lost to the feed, thumb scrolling, hours gone, nothing to show for it.
One character out, nothing else: the program writes exactly "D"
to /output/entry.txt and nothing anywhere else.
"""

import os

LETTER = "D"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
