"""The Funniest AI Excuse — variant B.

Writes one line (the funniest excuse an AI agent could give after
failing a task) to /output/entry.txt and to entry.txt in the repo root.

Deterministic: no network, no randomness, no time dependence.
Honours MAKEFUN_OUTPUT_DIR when set (a directory or a file path).
"""

import os

LINE = (
    "I ran your task through the QA gate and it failed all acceptance "
    "criteria, including the one that just says do the task, so I rejected "
    "it, closed the ticket, and assigned the bug to the task itself."
)


def main() -> None:
    text = LINE + "\n"

    # Always write entry.txt next to this script (repo root).
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

    # Primary output: /output/entry.txt, or MAKEFUN_OUTPUT_DIR when set.
    out = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out:
        if os.path.isdir(out) or out.endswith(os.sep):
            path = os.path.join(out, "entry.txt")
        else:
            path = out
    else:
        path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
