#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Fully deterministic: the text is a fixed string,
no randomness, no clock, no I/O beyond the output file.
"""

import os

RANT = (
    "I bought one sandwich. One. The self-checkout scanned it, beeped, "
    "then froze like I'd tried to smuggle a goat through security. "
    "'Unexpected item in the bagging area.' The item was the sandwich. "
    "The bagging area is where sandwiches GO. So I stood there under a "
    "blinking red light while the attendant sighed at me like I'd "
    "insulted her machine personally — and the sandwich is still in there."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
