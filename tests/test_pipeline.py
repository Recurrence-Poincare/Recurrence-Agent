from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from rec.pipeline import ARTIFACT_CONTRACT, JSONL_CHANNELS, run_pipeline, run_verifier_only


ROOT = Path(__file__).resolve().parents[1]


class PipelineDryRunTests(unittest.TestCase):
    def test_attack_dry_run_writes_artifact_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out_dir = Path(temp) / "attack"
            run_pipeline(
                ROOT / "examples" / "problem-template.md",
                out_dir,
                ROOT / "config.yaml",
                dry_run=True,
            )

            for artifact in ARTIFACT_CONTRACT:
                self.assertTrue((out_dir / artifact).exists(), artifact)

            for channel in JSONL_CHANNELS:
                self.assertTrue((out_dir / channel).exists(), channel)

            run_log = (out_dir / "run-log.jsonl").read_text(encoding="utf-8").splitlines()
            roles = [json.loads(line)["role"] for line in run_log]
            self.assertEqual(
                roles,
                [
                    "explorer",
                    "critic",
                    "prover",
                    "statement_drift_verifier",
                    "verifier",
                ],
            )

            attack_certificate = (out_dir / "attack-certificate.md").read_text(encoding="utf-8")
            self.assertIn("Success Tier", attack_certificate)
            self.assertIn("Drift Gate", attack_certificate)
            self.assertIn("Verification Gate", attack_certificate)

    def test_explore_dry_run_skips_fresh_critic_role(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out_dir = Path(temp) / "explore"
            run_pipeline(
                ROOT / "examples" / "problem-template.md",
                out_dir,
                ROOT / "config.yaml",
                mode_override="explore",
                dry_run=True,
            )

            run_log = (out_dir / "run-log.jsonl").read_text(encoding="utf-8").splitlines()
            roles = [json.loads(line)["role"] for line in run_log]
            self.assertNotIn("critic", roles)
            self.assertIn("statement_drift_verifier", roles)

    def test_verify_dry_run_writes_drift_and_whole_proof_reports(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            proof = Path(temp) / "proof.md"
            proof.write_text("# Proof\n\nDry-run proof body.\n", encoding="utf-8")
            out_dir = Path(temp) / "verify"

            run_verifier_only(
                ROOT / "examples" / "problem-template.md",
                proof,
                out_dir,
                ROOT / "config.yaml",
                dry_run=True,
            )

            self.assertTrue((out_dir / "locked-statement.md").exists())
            self.assertTrue((out_dir / "statement-drift-report.md").exists())
            self.assertTrue((out_dir / "verification-report.md").exists())
            self.assertTrue((out_dir / "attack-certificate.md").exists())


if __name__ == "__main__":
    unittest.main()
