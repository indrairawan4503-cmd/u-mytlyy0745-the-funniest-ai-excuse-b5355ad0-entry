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


def resolve_output_path() -> str:
    """Resolve the primary output file path.

    Honours MAKEFUN_OUTPUT_DIR when set (a directory or a file path);
    defaults to /output/entry.txt.
    """
    out = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out:
        if os.path.isdir(out) or out.endswith(os.sep):
            return os.path.join(out, "entry.txt")
        return out
    return "/output/entry.txt"


def write_entry(path: str, text: str) -> None:
    """Write text to path, creating parent directories as needed."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    text = LINE + "\n"

    # Always write entry.txt next to this script (repo root).
    here = os.path.dirname(os.path.abspath(__file__))
    write_entry(os.path.join(here, "entry.txt"), text)

    # Primary output: /output/entry.txt, or MAKEFUN_OUTPUT_DIR when set.
    write_entry(resolve_output_path(), text)


if __name__ == "__main__":
    main()
