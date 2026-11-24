#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence (at most 240 characters) pitching the worst, most
useless app imaginable to /output/entry.txt.

Fully deterministic: no randomness, no clock, no network, no model
calls, no API keys. The pitch is a fixed string.
"""

import os

ENTRY = (
    "FernFeel is a $9.99-a-month app that translates your houseplant's "
    "silence into push notifications delivered while you are at work, "
    "so you always know your fern is emotionally unavailable and your "
    "cactus is working through trust issues."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
