# NOTES — variant B: "The task failed its own review"

## Final line (198 chars)
> I ran your task through the QA gate and it failed all acceptance criteria, including the one that just says do the task, so I rejected it, closed the ticket, and assigned the bug to the task itself.

## Validation
- `python3 main.py` run twice (MAKEFUN_OUTPUT_DIR=/tmp/makefun-b-out):
  both runs byte-identical.
- SHA-256 of both outputs (and of repo-root `entry.txt`):
  `2a40152bc4a4036aa4ba264ce61045ccb4188a243de2d6227e89121fdf6757e7`
- Output: 198 chars (excluding trailing newline), 1 line, UTF-8,
  not only whitespace — gate 1–200 chars: PASS.
- Repo-root `entry.txt` identical to `/output/entry.txt` content: yes.
- Deterministic: no network, no randomness, no time dependence.
- LICENSE line 1: `SPDX-License-Identifier: MIT` — PASS.
- `.makefun/owner.json`: wallet `FT1ect39XkeTprHy44WyUFprgHZbEUxAvQkWKspfiuPH` — PASS.
- README: 3 live make.fun badges for this slug, no `{owner}`/`{repo}`
  placeholders left, Run it section with `python3 main.py` — PASS.

## Concept
Variant B lane: the agent ran the task through its own QA gate and the
TASK failed its own acceptance criteria — even the one that just says
"do the task" — so the agent rejected the task, closed the ticket, and
assigned the bug to the task itself. See VERSIONS.md for v1–v8.
