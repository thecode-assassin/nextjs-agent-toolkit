#!/usr/bin/env python3
"""Install toolkit skills and Codex agents as safe, repo-owned symlinks."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
PROFILES_FILE = ROOT / "profiles" / "profiles.json"
LEGACY_NAMES = {
    "nextjs-api-routes",
    "nextjs-auth-session-architecture",
    "nextjs-auth-and-security-boundaries",
    "nextjs-backend-transport",
    "nextjs-caching-and-revalidation",
    "nextjs-comprehensive-pr-review",
    "nextjs-data-flow-and-mutations",
    "nextjs-data-security-boundaries",
    "nextjs-error-loading-and-recovery",
    "nextjs-i18n-and-localization",
    "nextjs-material-ui",
    "nextjs-observability-and-runtime-debugging",
    "nextjs-performance-and-bundle-optimization",
    "nextjs-playwright-e2e",
    "nextjs-pr-review",
    "nextjs-react-query-integration",
    "nextjs-rendering-and-data-fetching",
    "nextjs-seo-and-metadata",
    "nextjs-server-actions-and-forms",
    "nextjs-tailwind-ui",
    "nextjs-ui-interaction-review",
    "nextjs-upgrade-and-migration",
    "nextjs-vitest-hermetic-tests",
    "spring-boot-nextjs-contract-guard",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", default="full")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--uninstall", action="store_true")
    parser.add_argument("--remove-legacy", action="store_true")
    parser.add_argument("--skills-dir", type=Path, default=Path.home() / ".agents" / "skills")
    parser.add_argument("--agents-dir", type=Path, default=Path.home() / ".codex" / "agents")
    parser.add_argument("--legacy-dir", type=Path, default=Path.home() / ".codex" / "skills", help=argparse.SUPPRESS)
    return parser.parse_args()


def load_profiles() -> dict[str, list[str]]:
    return json.loads(PROFILES_FILE.read_text())


def resolve_profile(name: str, profiles: dict[str, list[str]], stack: tuple[str, ...] = ()) -> list[str]:
    if name not in profiles:
        raise ValueError(f"unknown profile: {name}")
    if name in stack:
        raise ValueError(f"cyclic profile reference: {' -> '.join((*stack, name))}")
    result: list[str] = []
    for item in profiles[name]:
        additions = resolve_profile(item[1:], profiles, (*stack, name)) if item.startswith("@") else [item]
        for addition in additions:
            if addition not in result:
                result.append(addition)
    return result


def owned_link(target: Path, source: Path) -> bool:
    return target.is_symlink() and target.resolve(strict=False) == source.resolve(strict=False)


def install_link(source: Path, target: Path, dry_run: bool) -> None:
    if target.is_symlink():
        if owned_link(target, source):
            print(f"ok       {target}")
            return
        raise RuntimeError(f"refusing unrelated symlink: {target} -> {os.readlink(target)}")
    if target.exists():
        raise RuntimeError(f"refusing existing path: {target}")
    print(f"link     {target} -> {source}")
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.symlink_to(source, target_is_directory=source.is_dir())


def remove_owned_link(source: Path, target: Path, dry_run: bool) -> None:
    if not target.is_symlink():
        if target.exists():
            print(f"preserve {target} (not a symlink)")
        return
    if not owned_link(target, source):
        print(f"preserve {target} (unrelated symlink)")
        return
    print(f"unlink   {target}")
    if not dry_run:
        target.unlink()


def remove_legacy(directory: Path, dry_run: bool) -> None:
    if not directory.exists():
        return
    for name in sorted(LEGACY_NAMES):
        target = directory / name
        if target.is_symlink() or target.is_file():
            print(f"legacy  remove {target}")
            if not dry_run:
                target.unlink()
        elif target.is_dir():
            if target.parent.resolve() != directory.resolve() or not (target / "SKILL.md").is_file():
                print(f"legacy  refuse unrecognized directory {target}")
                continue
            print(f"legacy  remove skill directory {target}")
            if not dry_run:
                shutil.rmtree(target)


def main() -> int:
    args = parse_args()
    try:
        profiles = load_profiles()
        selected = resolve_profile(args.profile, profiles)
        skill_sources = [(ROOT / "skills" / name, args.skills_dir / name) for name in selected]
        agent_sources = [(source, args.agents_dir / source.name) for source in sorted((ROOT / ".codex" / "agents").glob("*.toml"))]
        for source, _ in (*skill_sources, *agent_sources):
            if not source.exists():
                raise RuntimeError(f"missing source: {source}")
        operation = remove_owned_link if args.uninstall else install_link
        for source, target in (*skill_sources, *agent_sources):
            operation(source, target, args.dry_run)
        if args.remove_legacy:
            remove_legacy(args.legacy_dir, args.dry_run)
        return 0
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
