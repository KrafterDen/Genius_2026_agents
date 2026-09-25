"""Offline safety/state tests. These do not claim to test an installed Codex client."""
from __future__ import annotations
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

module_path = Path(__file__).resolve().parents[1] / "run_blocks.py"
spec = importlib.util.spec_from_file_location("runner", module_path)
runner = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(runner)

class TestRunner(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        (self.root / ".agent/blocks").mkdir(parents=True)
        (self.root / "proof.txt").write_text("Actual controlled test evidence\n")
    def tearDown(self):
        self.temp.cleanup()
    def state(self, **changes):
        value = {"block_id":"00", "status":"passed", "started_at":"2026-09-25T00:00:00Z",
                 "ended_at":"2026-09-25T00:01:00Z", "elapsed_minutes":1,
                 "under_target_reason":"Controlled runner fixture, not a project work session",
                 "gates":[{"name":"fixture", "passed":True,"evidence_path":"proof.txt"}],
                 "evidence":["proof.txt"],"next_action":"Continue test"}
        value.update(changes)
        (self.root / ".agent/blocks/00.json").write_text(json.dumps(value))
        return value
    def config(self, **changes):
        value={"validated":True,"web_search_verified":True,"validated_for_codex_version":"test-version",
               "validation_evidence_paths":["proof.txt"],
               "command_template":["codex","exec","--output-last-message","{last_message}","-"]}
        value.update(changes)
        return value
    def test_valid_evidenced_state(self):
        self.state()
        self.assertEqual(runner.verify_state(self.root,"00")["status"],"passed")
    def test_missing_evidence_fails(self):
        self.state(evidence=["missing.txt"])
        with self.assertRaises(runner.RunnerError):runner.verify_state(self.root,"00")
    def test_false_gate_fails(self):
        self.state(gates=[{"name":"x","passed":False,"evidence_path":"proof.txt"}])
        with self.assertRaises(runner.RunnerError):runner.verify_state(self.root,"00")
    def test_no_automatic_pass_on_exit_success(self):
        self.state(status="blocked")
        with self.assertRaises(runner.RunnerError):runner.verify_state(self.root,"00")
    def test_short_duration_must_be_honest(self):
        self.state(under_target_reason=None)
        with self.assertRaises(runner.RunnerError):runner.verify_state(self.root,"00")
    def test_parent_path_rejected(self):
        with self.assertRaises(runner.RunnerError):runner.inside(self.root,"../private.txt")
    def test_absolute_path_rejected(self):
        with self.assertRaises(runner.RunnerError):runner.inside(self.root,str(self.root / "proof.txt"))
    def test_valid_config(self):
        self.assertEqual(runner.validate_config(self.root,self.config())[0],"codex")
    def test_unvalidated_config_fails(self):
        with self.assertRaises(runner.RunnerError):runner.validate_config(self.root,self.config(validated=False))
    def test_no_web_fails(self):
        with self.assertRaises(runner.RunnerError):runner.validate_config(self.root,self.config(web_search_verified=False))
    def test_shell_command_rejected(self):
        with self.assertRaises(runner.RunnerError):runner.validate_config(self.root,self.config(command_template=["bash","-c","codex exec -"]))
    def test_permission_bypass_rejected(self):
        command=["codex","exec","--yolo","--output-last-message","{last_message}","-"]
        with self.assertRaises(runner.RunnerError):runner.validate_config(self.root,self.config(command_template=command))
    def test_workdir_escape_rejected(self):
        command=["codex","exec","--cd","/elsewhere","--output-last-message","{last_message}","-"]
        with self.assertRaises(runner.RunnerError):runner.validate_config(self.root,self.config(command_template=command))
    def test_dry_run_no_state_or_agent_required(self):
        before=set(self.root.rglob("*"))
        with contextlib.redirect_stdout(io.StringIO()) as capture:
            result=runner.main(["--repo",str(self.root),"--from-block","1","--to-block","2"])
        self.assertEqual(result,0)
        self.assertIn("DRY RUN",capture.getvalue())
        self.assertEqual(before,set(self.root.rglob("*")))
    def test_bootstrap_not_launched_by_runner(self):
        with self.assertRaises(runner.RunnerError):runner.main(["--repo",str(self.root),"--from-block","0"])
    def test_prompt_is_one_block_only(self):
        block=json.loads((runner.PACK/"block_manifest.json").read_text())["blocks"][1]
        prompt=runner.block_prompt(self.root,block)
        self.assertIn("ONE work block",prompt)
        self.assertIn("do not continue into subsequent blocks",prompt)


class TestRunnerFullFlow(unittest.TestCase):
    def setUp(self):
        from unittest.mock import patch
        self.patch = patch
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        (self.root / '.agent/blocks').mkdir(parents=True)
        (self.root / '.agent/runtime').mkdir(parents=True)
        (self.root / 'AGENTS.md').write_text('Controlled test instructions')
        (self.root / 'proof.txt').write_text('Test evidence')
        self.write_state('00')
        config={"validated":True,"web_search_verified":True,"validated_for_codex_version":"test-version",
                "validation_evidence_paths":["proof.txt"],
                "command_template":["codex","exec","--output-last-message","{last_message}","-"]}
        (self.root / '.agent/runtime/runner_config.json').write_text(json.dumps(config))
    def tearDown(self): self.temp.cleanup()
    def write_state(self,bid,status='passed'):
        state={'block_id':bid,'status':status,'started_at':'2026-09-25T00:00:00Z',
               'ended_at':'2026-09-25T00:01:00Z','elapsed_minutes':1,
               'under_target_reason':'Controlled offline test fixture',
               'gates':[{'name':'fixture','passed':True,'evidence_path':'proof.txt'}],
               'evidence':['proof.txt'],'next_action':'Next test'}
        (self.root / f'.agent/blocks/{bid}.json').write_text(json.dumps(state))
    def args(self, extra=None):
        return ['--repo',str(self.root),'--from-block','1','--to-block','1','--execute']+(extra or [])
    def version(self):
        import subprocess
        return subprocess.CompletedProcess(['codex','--version'],0,stdout='test-version\n',stderr='')
    def test_real_loop_contract_with_fake_executor(self):
        def fake(*args,**kwargs):self.write_state('01');return 0
        with self.patch.object(runner.subprocess,'run',return_value=self.version()), self.patch.object(runner,'invoke',side_effect=fake), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(runner.main(self.args()),0)
        self.assertFalse((self.root/'.agent/runtime/runner.lock').exists())
        self.assertTrue((self.root/'.agent/runtime/runner_events.jsonl').is_file())
    def test_exit_zero_without_evidence_stops(self):
        with self.patch.object(runner.subprocess,'run',return_value=self.version()), self.patch.object(runner,'invoke',return_value=0), contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(runner.RunnerError):runner.main(self.args())
        self.assertFalse((self.root/'.agent/runtime/runner.lock').exists())
    def test_nonzero_stops_and_releases_lock(self):
        with self.patch.object(runner.subprocess,'run',return_value=self.version()), self.patch.object(runner,'invoke',return_value=3), contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(runner.RunnerError):runner.main(self.args())
        self.assertFalse((self.root/'.agent/runtime/runner.lock').exists())
    def test_timeout_contract_releases_lock(self):
        with self.patch.object(runner.subprocess,'run',return_value=self.version()), self.patch.object(runner,'invoke',side_effect=runner.RunnerError('timeout')), contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(runner.RunnerError):runner.main(self.args())
        self.assertFalse((self.root/'.agent/runtime/runner.lock').exists())
    def test_version_change_stops(self):
        changed=self.version();changed.stdout='other-version'
        with self.patch.object(runner.subprocess,'run',return_value=changed), self.patch.object(runner,'invoke') as inv, contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(runner.RunnerError):runner.main(self.args())
            inv.assert_not_called()
    def test_existing_lock_is_not_deleted(self):
        lock=self.root/'.agent/runtime/runner.lock';lock.write_text('another process')
        with self.patch.object(runner.subprocess,'run',return_value=self.version()), self.patch.object(runner,'invoke') as inv, contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(runner.RunnerError):runner.main(self.args())
            inv.assert_not_called()
        self.assertEqual(lock.read_text(),'another process')
    def test_verified_completed_block_skipped(self):
        self.write_state('01')
        with self.patch.object(runner.subprocess,'run',return_value=self.version()), self.patch.object(runner,'invoke') as inv, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(runner.main(self.args()),0)
            inv.assert_not_called()
    def test_invocation_cap(self):
        def fake(*args,**kwargs):self.write_state('01');return 0
        args=['--repo',str(self.root),'--from-block','1','--to-block','2','--execute','--max-blocks','1']
        with self.patch.object(runner.subprocess,'run',return_value=self.version()), self.patch.object(runner,'invoke',side_effect=fake) as inv, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(runner.main(args),0)
            self.assertEqual(inv.call_count,1)

if __name__=="__main__":unittest.main()
