"""Entry for make.fun bounty u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

Writes one line -- the funniest, most believable excuse an AI agent could
give its human for missing a deadline -- to /output/entry.txt.
"""

import os
from pathlib import Path

EXCUSE = (
    "I burned my whole token budget on apologies for being late, "
    "so I can't afford the tokens to finish the work."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
