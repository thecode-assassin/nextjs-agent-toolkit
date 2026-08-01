#!/usr/bin/env python3
"""Add project-scoped Next.js DevTools MCP configuration without overwriting conflicts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import tomllib

DEFAULT_MCP_PACKAGE = "next-devtools-mcp@latest"
SERVER_NAME = "next-devtools"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Existing Next.js project directory")
    parser.add_argument(
        "--format",
        choices=("codex", "mcp-json"),
        default="codex",
        help="Write .codex/config.toml for Codex or the portable .mcp.json format",
    )
    parser.add_argument("--mcp-package", default=DEFAULT_MCP_PACKAGE)
    parser.add_argument("--disable-telemetry", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def package_version(project: Path) -> str | None:
    manifest = json.loads((project / "package.json").read_text())
    for section in ("dependencies", "devDependencies", "optionalDependencies"):
        dependencies = manifest.get(section, {})
        if isinstance(dependencies, dict) and isinstance(dependencies.get("next"), str):
            return dependencies["next"]
    return None


def detected_major(version: str) -> int | None:
    match = re.search(r"(?<!\d)(\d+)(?:\.\d+){0,2}", version)
    return int(match.group(1)) if match else None


def server_config(package: str, disable_telemetry: bool) -> dict[str, object]:
    result: dict[str, object] = {"command": "npx", "args": ["-y", package]}
    if disable_telemetry:
        result["env"] = {"NEXT_TELEMETRY_DISABLED": "1"}
    return result


def toml_block(package: str, disable_telemetry: bool) -> str:
    package_literal = json.dumps(package)
    lines = [
        f"[mcp_servers.{SERVER_NAME}]",
        'command = "npx"',
        f'args = ["-y", {package_literal}]',
        "enabled = true",
    ]
    if disable_telemetry:
        lines.append('env = { NEXT_TELEMETRY_DISABLED = "1" }')
    return "\n".join(lines) + "\n"


def configure_codex(project: Path, package: str, disable_telemetry: bool, dry_run: bool) -> str:
    target = project / ".codex" / "config.toml"
    existing = target.read_text() if target.exists() else ""
    try:
        parsed = tomllib.loads(existing) if existing.strip() else {}
    except tomllib.TOMLDecodeError as error:
        raise ValueError(f"refusing invalid TOML at {target}: {error}") from error

    servers = parsed.get("mcp_servers", {})
    if not isinstance(servers, dict):
        raise ValueError(f"refusing non-table mcp_servers configuration at {target}")
    if SERVER_NAME in servers:
        current = servers[SERVER_NAME]
        expected = server_config(package, disable_telemetry) | {"enabled": True}
        if current == expected:
            return f"ok       {target}"
        raise ValueError(f"refusing conflicting {SERVER_NAME} configuration at {target}")

    separator = "" if not existing or existing.endswith("\n\n") else ("\n" if existing.endswith("\n") else "\n\n")
    updated = existing + separator + toml_block(package, disable_telemetry)
    if dry_run:
        return f"would add {target}\n{toml_block(package, disable_telemetry).rstrip()}"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(updated)
    return f"added    {target}"


def configure_mcp_json(project: Path, package: str, disable_telemetry: bool, dry_run: bool) -> str:
    target = project / ".mcp.json"
    try:
        data = json.loads(target.read_text()) if target.exists() else {}
    except json.JSONDecodeError as error:
        raise ValueError(f"refusing invalid JSON at {target}: {error}") from error
    if not isinstance(data, dict):
        raise ValueError(f"refusing non-object configuration at {target}")

    servers = data.setdefault("mcpServers", {})
    if not isinstance(servers, dict):
        raise ValueError(f"refusing non-object mcpServers configuration at {target}")
    expected = server_config(package, disable_telemetry)
    if SERVER_NAME in servers:
        if servers[SERVER_NAME] == expected:
            return f"ok       {target}"
        raise ValueError(f"refusing conflicting {SERVER_NAME} configuration at {target}")
    servers[SERVER_NAME] = expected

    rendered = json.dumps(data, indent=2) + "\n"
    if dry_run:
        return f"would write {target}\n{rendered.rstrip()}"
    target.write_text(rendered)
    return f"added    {target}"


def configure_project(
    project: Path,
    config_format: str = "codex",
    package: str = DEFAULT_MCP_PACKAGE,
    disable_telemetry: bool = False,
    dry_run: bool = False,
) -> str:
    project = project.expanduser().resolve()
    if config_format not in {"codex", "mcp-json"}:
        raise ValueError(f"unsupported configuration format: {config_format}")
    if package.startswith("-"):
        raise ValueError("MCP package reference must not start with '-'")
    manifest = project / "package.json"
    if not project.is_dir() or not manifest.is_file():
        raise ValueError(f"not a Next.js project directory: {project}")
    version = package_version(project)
    if version is None:
        raise ValueError(f"package.json does not declare next: {manifest}")
    major = detected_major(version)
    warning = ""
    if major is not None and major < 16:
        warning = f"warning  Next.js {version} lacks the built-in runtime MCP endpoint; non-runtime tools remain available\n"

    if config_format == "codex":
        result = configure_codex(project, package, disable_telemetry, dry_run)
    else:
        result = configure_mcp_json(project, package, disable_telemetry, dry_run)
    return warning + result


def main() -> int:
    args = parse_args()
    try:
        print(configure_project(args.project, args.format, args.mcp_package, args.disable_telemetry, args.dry_run))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
