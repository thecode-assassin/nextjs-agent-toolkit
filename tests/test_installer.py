from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install.py"


class InstallerTests(unittest.TestCase):
    def run_installer(self, *args: str, expected: int = 0) -> subprocess.CompletedProcess[str]:
        result = subprocess.run([sys.executable, str(INSTALLER), *args], text=True, capture_output=True)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def test_full_install_is_idempotent_and_uninstalls_owned_links(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            skills = base / "skills"
            agents = base / "agents"
            args = ("--profile", "full", "--skills-dir", str(skills), "--agents-dir", str(agents))
            self.run_installer(*args)
            self.assertEqual(len(list(skills.iterdir())), 25)
            self.assertEqual(len(list(agents.iterdir())), 5)
            self.run_installer(*args)
            self.run_installer(*args, "--uninstall")
            self.assertEqual(list(skills.iterdir()), [])
            self.assertEqual(list(agents.iterdir()), [])

    def test_profiles_install_expected_union(self) -> None:
        expected = {
            "core": 16,
            "ui": 17,
            "data-auth": 18,
            "testing": 18,
            "devtools": 17,
            "backend": 18,
            "platform": 17,
            "full": 25,
        }
        for profile, count in expected.items():
            with self.subTest(profile=profile), tempfile.TemporaryDirectory() as temp:
                base = Path(temp)
                self.run_installer("--profile", profile, "--skills-dir", str(base / "s"), "--agents-dir", str(base / "a"))
                self.assertEqual(len(list((base / "s").iterdir())), count)

    def test_collision_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            skills = base / "skills"
            skills.mkdir()
            (skills / "nextjs-project-configuration").mkdir()
            result = self.run_installer("--profile", "core", "--skills-dir", str(skills), "--agents-dir", str(base / "agents"), expected=1)
            self.assertIn("refusing existing path", result.stderr)

    def test_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            skills = base / "skills"
            agents = base / "agents"
            self.run_installer("--profile", "full", "--dry-run", "--skills-dir", str(skills), "--agents-dir", str(agents))
            self.assertFalse(skills.exists())
            self.assertFalse(agents.exists())

    def test_legacy_flag_removes_only_named_links_and_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            legacy = base / "legacy"
            legacy.mkdir()
            removable = legacy / "nextjs-api-routes"
            removable.write_text("legacy")
            preserved = legacy / "shadcn"
            preserved.write_text("keep")
            real_directory = legacy / "nextjs-tailwind-ui"
            real_directory.mkdir()
            result = self.run_installer(
                "--profile", "core", "--dry-run", "--remove-legacy",
                "--skills-dir", str(base / "skills"), "--agents-dir", str(base / "agents"),
                "--legacy-dir", str(legacy),
            )
            self.assertTrue(removable.exists())
            self.assertTrue(preserved.exists())
            self.assertIn("refuse unrecognized directory", result.stdout)

    def test_legacy_flag_removes_recognized_skill_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            legacy = base / "legacy"
            old_skill = legacy / "nextjs-api-routes"
            old_skill.mkdir(parents=True)
            (old_skill / "SKILL.md").write_text("---\nname: nextjs-api-routes\n---\n")
            self.run_installer(
                "--profile", "core", "--remove-legacy",
                "--skills-dir", str(base / "skills"), "--agents-dir", str(base / "agents"),
                "--legacy-dir", str(legacy),
            )
            self.assertFalse(old_skill.exists())


if __name__ == "__main__":
    unittest.main()
