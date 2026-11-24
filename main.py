#!/usr/bin/env python3
"""One Line, One Chill entry: a single sentence of horror, written to /output/entry.txt.

The program writes one original one-line horror sentence (97 characters,
inside the 1-200 character gate) and nothing else. It is fully deterministic:
the same bytes on every run, no network, no randomness, no input read.

The line was picked by pre-judging eight original candidates pairwise, in
both orders, against the horror-editor brief published in the kit, plus three
fresh challengers in a second round. The exact judge model
(z-ai/glm-5.3-flash on OpenRouter) was unreachable — the account's purchased
credits are exhausted (HTTP 402) and the :free variant returns 404 — and the
Gemini free tier was rate-limited (HTTP 429), so the rounds ran on a free
proxy model (AMD TokenLab DeepSeek-V4-Flash, free allowance, no money spent).
"The Extra Window" won the eight-way round-robin with a 0.614 mean game
score, and none of the three challengers beat it in the second round.
"""

import os

LINE = "Every photo I take of my house now shows one extra window, and last night it was lit from inside."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    line = LINE
    if not line.strip():
        raise SystemExit("line must not be blank")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"line is {len(line)} chars, over the {MAX_CHARS} cap")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read-back gate: prove the file on disk is byte-for-byte the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("read-back mismatch: entry.txt is not the line")
    if not 1 <= len(written) <= MAX_CHARS:
        raise SystemExit(f"entry.txt is {len(written)} chars, outside the 1-200 gate")


if __name__ == "__main__":
    main()
