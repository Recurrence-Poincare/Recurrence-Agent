from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .config import load_config
from .model_runner import ModelResult, run_model


ROOT = Path(__file__).resolve().parents[1]
PROMPT_DIR = ROOT / "prompts"


def read_prompt(name: str) -> str:
    return (PROMPT_DIR / name).read_text(encoding="utf-8")


def fill(template: str, **values: str) -> str:
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered


def write_result(out_dir: Path, filename: str, result: ModelResult) -> None:
    body = result.stdout.strip() or "(no stdout)"
    if result.stderr.strip():
        body += "\n\n## stderr\n\n```text\n" + result.stderr.strip() + "\n```"
    (out_dir / filename).write_text(body + "\n", encoding="utf-8")


def append_run_log(out_dir: Path, result: ModelResult) -> None:
    log = {
        "role": result.role,
        "provider": result.provider,
        "model": result.model,
        "returncode": result.returncode,
        "elapsed_seconds": round(result.elapsed_seconds, 3),
        "command": result.command,
    }
    path = out_dir / "run-log.jsonl"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(log, ensure_ascii=False) + "\n")


def write_static_artifacts(out_dir: Path, problem_text: str, mode: str) -> None:
    (out_dir / "problem.md").write_text(problem_text, encoding="utf-8")
    (out_dir / "run.json").write_text(
        json.dumps(
            {
                "created_at": datetime.now(timezone.utc).isoformat(),
                "mode": mode,
                "artifact_contract": [
                    "exploration-map.md",
                    "approach-queue.md",
                    "counterexample-log.md",
                    "proof-attempt.md",
                    "verification-report.md",
                    "claim-map.md",
                    "failure-ledger.md",
                    "next-actions.md",
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def run_pipeline(
    problem_path: Path,
    out_dir: Path,
    config_path: Path,
    mode_override: str | None = None,
    dry_run: bool = False,
) -> None:
    config = load_config(config_path)
    mode = mode_override or str(config.get("mode", "attack"))
    problem_text = problem_path.read_text(encoding="utf-8")
    out_dir.mkdir(parents=True, exist_ok=True)
    write_static_artifacts(out_dir, problem_text, mode)

    explorer_prompt = fill(read_prompt("explorer.md"), problem=problem_text, mode=mode)
    explorer = run_model("explorer", explorer_prompt, config, out_dir, dry_run=dry_run)
    write_result(out_dir, "exploration-map.md", explorer)
    append_run_log(out_dir, explorer)

    prover_prompt = fill(
        read_prompt("prover.md"),
        problem=problem_text,
        mode=mode,
        exploration=(out_dir / "exploration-map.md").read_text(encoding="utf-8"),
    )
    prover = run_model("prover", prover_prompt, config, out_dir, dry_run=dry_run)
    write_result(out_dir, "proof-attempt.md", prover)
    append_run_log(out_dir, prover)

    verifier_prompt = fill(
        read_prompt("verifier.md"),
        problem=problem_text,
        proof=(out_dir / "proof-attempt.md").read_text(encoding="utf-8"),
    )
    verifier = run_model("verifier", verifier_prompt, config, out_dir, dry_run=dry_run)
    write_result(out_dir, "verification-report.md", verifier)
    append_run_log(out_dir, verifier)

    write_followup_artifacts(out_dir)


def run_verifier_only(
    problem_path: Path,
    proof_path: Path,
    out_dir: Path,
    config_path: Path,
    dry_run: bool = False,
) -> None:
    config = load_config(config_path)
    problem_text = problem_path.read_text(encoding="utf-8")
    proof_text = proof_path.read_text(encoding="utf-8")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "problem.md").write_text(problem_text, encoding="utf-8")
    (out_dir / "proof-attempt.md").write_text(proof_text, encoding="utf-8")

    verifier_prompt = fill(read_prompt("verifier.md"), problem=problem_text, proof=proof_text)
    verifier = run_model("verifier", verifier_prompt, config, out_dir, dry_run=dry_run)
    write_result(out_dir, "verification-report.md", verifier)
    append_run_log(out_dir, verifier)
    write_followup_artifacts(out_dir)


def write_followup_artifacts(out_dir: Path) -> None:
    verification = (out_dir / "verification-report.md").read_text(encoding="utf-8")
    proof = (out_dir / "proof-attempt.md").read_text(encoding="utf-8")

    (out_dir / "approach-queue.md").write_text(
        "# Approach Queue\n\nExtract concrete proof and disproof routes from `exploration-map.md` and `proof-attempt.md`.\n",
        encoding="utf-8",
    )
    (out_dir / "counterexample-log.md").write_text(
        "# Counterexample Log\n\nRecord attempted counterexamples, obstruction tests, and missing hypotheses here.\n",
        encoding="utf-8",
    )
    (out_dir / "claim-map.md").write_text(
        "# Claim Map\n\nCreate one node per lemma/proposition. Attach verifier verdicts from `verification-report.md`.\n",
        encoding="utf-8",
    )
    (out_dir / "failure-ledger.md").write_text(
        "# Failure Ledger\n\nBranches should be marked `failed`, `blocked`, `uncertain`, or `needs human input` with reasons.\n",
        encoding="utf-8",
    )
    (out_dir / "next-actions.md").write_text(
        "# Next Actions\n\n1. Read `verification-report.md`.\n2. Promote only verifier-passed claims.\n3. Rewrite or stop branches marked `FAIL` or `UNCERTAIN`.\n",
        encoding="utf-8",
    )
