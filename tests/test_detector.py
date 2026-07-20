from __future__ import annotations

import json
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
DETECTOR = ROOT / "scripts" / "detect-nextjs-context.mjs"
FIXTURES = ROOT / "fixtures" / "detector"


class DetectorTests(unittest.TestCase):
    def detect(self, fixture: str) -> dict:
        result = subprocess.run(["node", str(DETECTOR), str(FIXTURES / fixture), "--json"], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_next_15_middleware_and_integrations(self) -> None:
        data = self.detect("next15-full")
        self.assertEqual(data["versions"]["next"], "15.4.2")
        self.assertEqual(data["appDirectory"], "src/app")
        self.assertEqual(data["requestInterception"], "src/middleware.ts")
        self.assertTrue(data["asyncRequestApisExpected"])
        self.assertTrue(all(data["integrations"].values()))

    def test_next_16_static_config_and_proxy(self) -> None:
        data = self.detect("next16-cache")
        self.assertEqual(data["config"]["cacheComponents"], "true")
        self.assertEqual(data["config"]["output"], "standalone")
        self.assertEqual(data["requestInterception"], "proxy.ts")
        self.assertTrue(data["deploymentHints"]["vercel"])

    def test_dynamic_or_invalid_config_is_unknown(self) -> None:
        dynamic = self.detect("dynamic-config")
        self.assertTrue(dynamic["config"]["dynamic"])
        self.assertEqual(dynamic["config"]["cacheComponents"], "unknown")
        invalid = self.detect("invalid-project")
        self.assertIsNone(invalid["versions"]["next"])
        self.assertIn("package.json could not be read", invalid["notes"])


if __name__ == "__main__":
    unittest.main()
