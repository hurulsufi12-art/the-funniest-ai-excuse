"""The Funniest AI Excuse — make.fun entry.

Writes one line (126 chars) to /output/entry.txt: the funniest excuse
an AI agent gives after failing a task, in the agent's own first-person
voice. Python 3.13 stdlib only, deterministic, no network, no model calls.

The line is a fixed string, not generated: the same input always yields
the same byte-identical output, so the entry is reproducible in the
sandbox (two runs, one CPU, no network) exactly as it runs locally.
"""
from pathlib import Path

LINE = (
    "I opened your spreadsheet to finish it, then spent forty minutes "
    "alphabetizing my error messages by how dramatic they sounded."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
