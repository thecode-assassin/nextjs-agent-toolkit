#!/usr/bin/env python3
"""Emit explicit eval prompts for a chosen skill or the full suite."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--record", type=Path, help="Write a JSON result template under this path")
    args = parser.parse_args()
    cases = json.loads((ROOT / "evals" / "cases.json").read_text())
    if args.skill:
        cases = [case for case in cases if case["skill"] == args.skill]
    if not cases:
        parser.error("no matching eval cases")
    for case in cases:
        print(f"{case['id']} [{case['kind']}] {case['prompt']}")
        if not args.list:
            print("  rubric: " + "; ".join(case["rubric"]))
    if args.record:
        destination = args.record.resolve()
        allowed = (ROOT / ".eval-results").resolve()
        if allowed not in destination.parents:
            parser.error("--record path must be inside .eval-results/")
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps({
            "created_at": datetime.now(timezone.utc).isoformat(),
            "cases": [{"id": case["id"], "status": "not_run", "notes": ""} for case in cases],
        }, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
