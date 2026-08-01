from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills" / "nextjs-devtools-mcp" / "scripts"
CONFIGURE = SCRIPTS / "configure_project.py"
CREATE = SCRIPTS / "create_project.py"


class McpProjectTests(unittest.TestCase):
    def project(self, base: Path, version: str = "^16.0.0") -> Path:
        project = base / "app"
        project.mkdir()
        (project / "package.json").write_text(json.dumps({"dependencies": {"next": version}}))
        return project

    def run_script(self, script: Path, *args: str, expected: int = 0) -> subprocess.CompletedProcess[str]:
        result = subprocess.run([sys.executable, str(script), *args], text=True, capture_output=True)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def test_codex_configuration_is_project_scoped_and_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            project = self.project(Path(temp))
            config = project / ".codex" / "config.toml"
            config.parent.mkdir()
            config.write_text('[mcp_servers.other]\ncommand = "other"\n')

            self.run_script(CONFIGURE, str(project), "--disable-telemetry")
            first = config.read_text()
            self.assertIn("[mcp_servers.other]", first)
            self.assertIn("[mcp_servers.next-devtools]", first)
            self.assertIn('NEXT_TELEMETRY_DISABLED = "1"', first)
            self.run_script(CONFIGURE, str(project), "--disable-telemetry")
            self.assertEqual(config.read_text(), first)

    def test_conflicting_codex_configuration_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            project = self.project(Path(temp))
            config = project / ".codex" / "config.toml"
            config.parent.mkdir()
            config.write_text('[mcp_servers.next-devtools]\ncommand = "custom"\n')

            result = self.run_script(CONFIGURE, str(project), expected=1)
            self.assertIn("refusing conflicting", result.stderr)
            self.assertEqual(config.read_text(), '[mcp_servers.next-devtools]\ncommand = "custom"\n')

    def test_mcp_json_preserves_unrelated_servers(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            project = self.project(Path(temp))
            config = project / ".mcp.json"
            config.write_text(json.dumps({"mcpServers": {"other": {"command": "other"}}}))

            self.run_script(CONFIGURE, str(project), "--format", "mcp-json")
            data = json.loads(config.read_text())
            self.assertEqual(data["mcpServers"]["other"], {"command": "other"})
            self.assertEqual(
                data["mcpServers"]["next-devtools"],
                {"command": "npx", "args": ["-y", "next-devtools-mcp@latest"]},
            )

    def test_old_next_version_warns_but_keeps_non_runtime_capabilities(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            project = self.project(Path(temp), "15.5.0")
            result = self.run_script(CONFIGURE, str(project))
            self.assertIn("lacks the built-in runtime MCP endpoint", result.stdout)
            self.assertTrue((project / ".codex" / "config.toml").is_file())

    def test_configure_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            project = self.project(Path(temp))
            result = self.run_script(CONFIGURE, str(project), "--dry-run")
            self.assertIn("would add", result.stdout)
            self.assertFalse((project / ".codex").exists())

    def test_create_dry_run_forwards_create_next_app_options(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "new-app"
            result = self.run_script(
                CREATE,
                str(destination),
                "--format",
                "mcp-json",
                "--dry-run",
                "--",
                "--use-pnpm",
                "--ts",
                "--yes",
            )
            self.assertIn("create-next-app@latest", result.stdout)
            self.assertIn("--app", result.stdout)
            self.assertIn("--use-pnpm", result.stdout)
            self.assertIn("as mcp-json", result.stdout)
            self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
