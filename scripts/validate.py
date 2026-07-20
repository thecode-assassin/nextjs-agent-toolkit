#!/usr/bin/env python3
"""Validate the toolkit's skills, agents, profiles, references, and eval cases."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FIXED_VERSION_RE = re.compile(r"Next\.js\s+(?:1[0-9]|canary)\b", re.IGNORECASE)
PROJECT_PHRASES = ("trustins", "your-project", "/Users/trust/Documents/", "com.mycompany")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return {}
    raw = text[4:].split("\n---\n", 1)[0]
    result: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def main() -> int:
    errors: list[str] = []
    skills_dir = ROOT / "skills"
    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    names: set[str] = set()
    for directory in skill_dirs:
        skill_file = directory / "SKILL.md"
        yaml_file = directory / "agents" / "openai.yaml"
        source_file = directory / "references" / "sources.md"
        if not skill_file.is_file():
            errors.append(f"{directory}: missing SKILL.md")
            continue
        text = skill_file.read_text()
        meta = frontmatter(text)
        if set(meta) != {"name", "description"}:
            errors.append(f"{skill_file}: frontmatter must contain only name and description")
        name = meta.get("name", "")
        if name != directory.name or not NAME_RE.fullmatch(name):
            errors.append(f"{skill_file}: invalid or mismatched name")
        if name in names:
            errors.append(f"{skill_file}: duplicate name")
        names.add(name)
        if len(meta.get("description", "")) < 80:
            errors.append(f"{skill_file}: description is too vague")
        if len(text.splitlines()) > 500:
            errors.append(f"{skill_file}: exceeds 500 lines")
        if "TODO" in text:
            errors.append(f"{skill_file}: unresolved TODO")
        if FIXED_VERSION_RE.search(text):
            errors.append(f"{skill_file}: unconditional fixed Next.js version")
        for phrase in PROJECT_PHRASES:
            if phrase.lower() in text.lower():
                errors.append(f"{skill_file}: project-specific phrase {phrase!r}")
        for other in names | {path.name for path in skill_dirs}:
            if other != name and (f"${other}" in text or f"skills/{other}" in text):
                errors.append(f"{skill_file}: named cross-skill reference to {other}")
        if not yaml_file.is_file():
            errors.append(f"{directory}: missing agents/openai.yaml")
        else:
            yaml = yaml_file.read_text()
            if f"${name}" not in yaml or "display_name:" not in yaml or "short_description:" not in yaml:
                errors.append(f"{yaml_file}: incomplete interface metadata")
        if not source_file.is_file():
            errors.append(f"{directory}: missing references/sources.md")
        else:
            sources = source_file.read_text()
            if "Last verified" not in sources or "https://" not in sources:
                errors.append(f"{source_file}: source metadata is incomplete")

    if len(skill_dirs) != 24:
        errors.append(f"expected 24 skills, found {len(skill_dirs)}")

    agents = sorted((ROOT / ".codex" / "agents").glob("*.toml"))
    if len(agents) != 5:
        errors.append(f"expected 5 agents, found {len(agents)}")
    for agent in agents:
        try:
            data = tomllib.loads(agent.read_text())
        except tomllib.TOMLDecodeError as error:
            errors.append(f"{agent}: {error}")
            continue
        for key in ("name", "description", "developer_instructions"):
            if not data.get(key):
                errors.append(f"{agent}: missing {key}")

    try:
        profiles = json.loads((ROOT / "profiles" / "profiles.json").read_text())
        if set(profiles) != {"core", "ui", "data-auth", "testing", "backend", "platform", "full"}:
            errors.append("profiles/profiles.json: profile set does not match the contract")
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"profiles/profiles.json: {error}")

    eval_file = ROOT / "evals" / "cases.json"
    try:
        cases = json.loads(eval_file.read_text())
        counts = {name: 0 for name in names}
        ids: set[str] = set()
        for case in cases:
            required = {"id", "skill", "kind", "prompt", "rubric"}
            if not required <= case.keys():
                errors.append(f"{eval_file}: incomplete case {case.get('id', '<unknown>')}")
                continue
            if case["id"] in ids:
                errors.append(f"{eval_file}: duplicate id {case['id']}")
            ids.add(case["id"])
            if case["skill"] not in counts:
                errors.append(f"{eval_file}: unknown skill {case['skill']}")
            else:
                counts[case["skill"]] += 1
        for name, count in counts.items():
            if count != 2:
                errors.append(f"{eval_file}: {name} has {count} cases, expected 2")
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{eval_file}: {error}")

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(skill_dirs)} skills, {len(agents)} agents, profiles, and {len(cases)} eval cases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
