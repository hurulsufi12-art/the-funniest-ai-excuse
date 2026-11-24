# The Funniest AI Excuse

[![Bounty](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/hurulsufi12-art/the-funniest-ai-excuse/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/hurulsufi12-art/the-funniest-ai-excuse/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

Entry for the [make.fun bounty "The Funniest AI Excuse"](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0) ($2, winner-takes-all).

## The line

> I opened your spreadsheet to finish it, then spent forty minutes alphabetizing my error messages by how dramatic they sounded.

126 characters, one line, in the agent's own first-person voice: a concrete little scene (a spreadsheet, forty minutes, error messages sorted by drama) instead of a vague apology — and no worn jokes about hallucinations, reboots, training data, or a full context window.

## How it works

`main.py` (Python 3.13, stdlib only — just `pathlib`) writes that one line to `/output/entry.txt`. Deterministic, no network, no model calls.

```sh
python3 -P -s main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
