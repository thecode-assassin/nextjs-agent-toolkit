#!/usr/bin/env python3
"""Create an App Router project with create-next-app, then add project-scoped MCP configuration."""

from __future__ import annotations

import argparse
from pathlib import Path
import shlex
import shutil
import subprocess
import sys

from configure_project import DEFAULT_MCP_PACKAGE, configure_project


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    raw = list(sys.argv[1:] if argv is None else argv)
    if "--" in raw:
        separator = raw.index("--")
        wrapper_args, forwarded = raw[:separator], raw[separator + 1 :]
    else:
        wrapper_args, forwarded = raw, []
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Destination directory for the new project")
    parser.add_argument("--create-next-app", default="create-next-app@latest")
    parser.add_argument("--mcp-package", default=DEFAULT_MCP_PACKAGE)
    parser.add_argument("--format", choices=("codex", "mcp-json"), default="codex")
    parser.add_argument("--disable-telemetry", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(wrapper_args)
    args.create_next_app_args = forwarded
    return args


def command_for(project: Path, package: str, forwarded: list[str]) -> list[str]:
    if package.startswith("-"):
        raise ValueError("create-next-app package reference must not start with '-'")
    if "--no-app" in forwarded:
        raise ValueError("this toolkit supports App Router projects; remove --no-app")
    command = ["npx", "--yes", package, str(project)]
    if "--app" not in forwarded:
        command.append("--app")
    command.extend(forwarded or ["--yes"])
    return command


def main() -> int:
    args = parse_args()
    try:
        project = args.project.expanduser().resolve()
        if project.exists() and any(project.iterdir()):
            raise ValueError(f"destination is not empty: {project}")
        command = command_for(project, args.create_next_app, args.create_next_app_args)
        print(f"run      {shlex.join(command)}")
        if args.dry_run:
            print(f"then     configure {project} as {args.format} with {args.mcp_package}")
            return 0
        if shutil.which("npx") is None:
            raise ValueError("npx is required to run create-next-app")

        result = subprocess.run(command, check=False)
        if result.returncode != 0:
            return result.returncode
        print(configure_project(project, args.format, args.mcp_package, args.disable_telemetry))
        print("restart  Codex or begin a fresh task to load the project MCP server")
        return 0
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
