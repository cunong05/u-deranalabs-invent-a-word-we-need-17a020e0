#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes one invented English word and its one-line definition to
/output/entry.txt (the grader reads exactly that file, 1-140 chars).
"""

import os

ENTRY = "Resttigue (n.): the exhaustion earned by a day of doing absolutely nothing."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
