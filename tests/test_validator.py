"""Controlled fault rehearsals for B00; fixtures are synthetic."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts.validate_repository import (
    ValidationError, assess_attempt, evidence_path, validate_state, validate_tasks,
)


class ValidatorFaultRehearsal(unittest.TestCase):
    def test_path_traversal_and_absolute_path_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for path in ("../escape.txt", "/tmp/escape.txt"):
                with self.subTest(path=path), self.assertRaises(ValidationError):
                    evidence_path(root, path)

    def test_symlink_escape_rejected(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root = Path(directory)
            (root / "link").symlink_to(outside)
            with self.assertRaises(ValidationError):
                evidence_path(root, "link/secret.txt")

    def test_invalid_state_and_missing_artifact_remain_failed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state = {"block_id": "00", "status": "passed", "started_at": "2026-01-01T00:00:00Z",
                     "ended_at": "2026-01-01T00:01:00Z", "elapsed_minutes": 1,
                     "under_target_reason": "fixture", "gates": [{"name": "artifact", "passed": True,
                     "evidence_path": "absent.txt"}], "evidence": ["absent.txt"],
                     "next_action": "continue"}
            with self.assertRaisesRegex(ValidationError, "missing or empty evidence"):
                validate_state(root, state, "00")
            state["status"] = "imaginary"
            with self.assertRaisesRegex(ValidationError, "invalid status"):
                validate_state(root, state, "00")

    def test_conflicting_nested_writers_rejected(self):
        tasks = {"tasks": [
            {"id": "a", "status": "in_progress", "passed": False,
             "write_scope": ["src/textileroute"]},
            {"id": "b", "status": "in_progress", "passed": False,
             "write_scope": ["src/textileroute/models.py"]},
        ]}
        with self.assertRaisesRegex(ValidationError, "conflicting writers"):
            validate_tasks(tasks)

    def test_stopped_unknown_model_network_and_failed_command(self):
        self.assertEqual(assess_attempt(stopped=True, command_exit=0, model="gpt-5.6-sol",
                                        network_available=True, needs_network=False), "blocked")
        self.assertEqual(assess_attempt(stopped=False, command_exit=0, model="unknown-model",
                                        network_available=True, needs_network=False), "blocked")
        self.assertEqual(assess_attempt(stopped=False, command_exit=0, model="gpt-6-sol",
                                        network_available=True, needs_network=False), "blocked")
        self.assertEqual(assess_attempt(stopped=False, command_exit=0, model="gpt-5.6-sol",
                                        network_available=False, needs_network=True), "blocked")
        failed = subprocess.run([sys.executable, "-c", "raise SystemExit(7)"], check=False)
        self.assertEqual(failed.returncode, 7)
        self.assertEqual(assess_attempt(stopped=False, command_exit=failed.returncode,
                                        model="gpt-5.6-sol", network_available=True,
                                        needs_network=False), "needs_revision")

    def test_safe_rerun_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evidence = root / "proof.txt"
            evidence.write_text("fixture proof\n")
            state = {"block_id": "00", "status": "passed", "started_at": "2026-01-01T00:00:00Z",
                     "ended_at": "2026-01-01T00:01:00Z", "elapsed_minutes": 1,
                     "under_target_reason": "fixture", "gates": [{"name": "proof", "passed": True,
                     "evidence_path": "proof.txt"}], "evidence": ["proof.txt"],
                     "next_action": "continue"}
            before = json.dumps(state, sort_keys=True), evidence.read_bytes()
            validate_state(root, state, "00")
            validate_state(root, state, "00")
            self.assertEqual(before, (json.dumps(state, sort_keys=True), evidence.read_bytes()))


if __name__ == "__main__":
    unittest.main()
