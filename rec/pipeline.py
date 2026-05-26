from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .config import load_config
from .model_runner import ModelResult, run_model


ROOT = Path(__file__).resolve().parents[1]
PROMPT_DIR = ROOT / "prompts"

ARTIFACT_CONTRACT = [
    "problem.md",
    "locked-statement.md",
    "exploration-map.md",
    "fresh-critic-report.md",
    "proof-attempt.md",
    "statement-drift-report.md",
    "verification-report.md",
    "attack-certificate.md",
    "approach-queue.md",
    "proof-route-log.md",
    "counterexample-log.md",
    "claim-map.md",
    "failure-ledger.md",
    "next-actions.md",
    "method-matrix.jsonl",
    "toy-models.jsonl",
    "counterexample-attempts.jsonl",
    "retrieved-theorems.jsonl",
    "decomposition-plans.jsonl",
    "direct-attempts.jsonl",
    "recursive-attempts.jsonl",
    "key-failures.jsonl",
    "statement-repairs.jsonl",
    "return-map.jsonl",
    "critic-reports.jsonl",
    "verifier-reports.jsonl",
]

JSONL_CHANNELS = [
    "method-matrix.jsonl",
    "toy-models.jsonl",
    "counterexample-attempts.jsonl",
    "retrieved-theorems.jsonl",
    "decomposition-plans.jsonl",
    "direct-attempts.jsonl",
    "recursive-attempts.jsonl",
    "key-failures.jsonl",
    "statement-repairs.jsonl",
    "return-map.jsonl",
    "critic-reports.jsonl",
    "verifier-reports.jsonl",
]

SUCCESS_TIERS = [
    "T0_refuted",
    "T1_proved_and_verified",
    "T2_conditionally_proved",
    "T3_reduced_to_named_bottleneck",
    "T4_attacked_unresolved",
    "T5_incoherent_or_drifted",
]


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


def append_jsonl(out_dir: Path, filename: str, record: dict[str, object]) -> None:
    path = out_dir / filename
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def write_locked_statement(out_dir: Path, problem_text: str) -> None:
    locked = (
        "# Locked Statement\n\n"
        "Status: frozen\n\n"
        "The text below is the target statement for this run. Proof attempts, "
        "counterexample attempts, and verifier reports must be judged against this "
        "statement, not against a stronger, weaker, or cleaner nearby theorem.\n\n"
        "## Original Input\n\n"
        f"{problem_text.rstrip()}\n\n"
        "## Drift Rule\n\n"
        "Any branch that changes the hypotheses, conclusion, quantifiers, ambient "
        "category, regularity assumptions, compactness assumptions, or named object "
        "must mark the change explicitly in `statement-repairs.jsonl` and must not be "
        "reported as solving the locked statement.\n"
    )
    (out_dir / "locked-statement.md").write_text(locked, encoding="utf-8")


def write_jsonl_scaffolds(out_dir: Path) -> None:
    for channel in JSONL_CHANNELS:
        (out_dir / channel).write_text("", encoding="utf-8")
    append_jsonl(
        out_dir,
        "method-matrix.jsonl",
        {
            "id": "M0",
            "route_type": "proof_and_disproof",
            "method": "seed_method_matrix_from_exploration",
            "target_claim": "locked_statement",
            "status": "pending",
            "next_test": "Fill concrete methods after the exploration pass.",
        },
    )
    append_jsonl(
        out_dir,
        "return-map.jsonl",
        {
            "id": "R0",
            "branch": "root",
            "returns_to": "locked_statement",
            "status": "active",
            "note": "Every exploratory branch must explain this edge.",
        },
    )


def write_static_artifacts(out_dir: Path, problem_text: str, mode: str) -> None:
    (out_dir / "problem.md").write_text(problem_text, encoding="utf-8")
    write_locked_statement(out_dir, problem_text)
    write_jsonl_scaffolds(out_dir)
    (out_dir / "run.json").write_text(
        json.dumps(
            {
                "created_at": datetime.now(timezone.utc).isoformat(),
                "mode": mode,
                "artifact_contract": ARTIFACT_CONTRACT,
                "jsonl_channels": JSONL_CHANNELS,
                "success_tiers": SUCCESS_TIERS,
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
    locked_statement = (out_dir / "locked-statement.md").read_text(encoding="utf-8")

    explorer_prompt = fill(
        read_prompt("explorer.md"),
        problem=problem_text,
        locked_statement=locked_statement,
        mode=mode,
    )
    explorer = run_model("explorer", explorer_prompt, config, out_dir, dry_run=dry_run)
    write_result(out_dir, "exploration-map.md", explorer)
    append_run_log(out_dir, explorer)

    critic_report = ""
    if mode == "attack":
        critic_prompt = fill(
            read_prompt("attack-critic.md"),
            problem=problem_text,
            locked_statement=locked_statement,
            exploration=(out_dir / "exploration-map.md").read_text(encoding="utf-8"),
        )
        critic = run_model("critic", critic_prompt, config, out_dir, dry_run=dry_run)
        write_result(out_dir, "fresh-critic-report.md", critic)
        append_run_log(out_dir, critic)
        append_jsonl(
            out_dir,
            "critic-reports.jsonl",
            {
                "id": "C1",
                "stage": "fresh_context_attack_critic",
                "artifact": "fresh-critic-report.md",
                "provider": critic.provider,
                "model": critic.model,
                "returncode": critic.returncode,
            },
        )
        critic_report = (out_dir / "fresh-critic-report.md").read_text(encoding="utf-8")

    prover_prompt = fill(
        read_prompt("prover.md"),
        problem=problem_text,
        locked_statement=locked_statement,
        mode=mode,
        exploration=(out_dir / "exploration-map.md").read_text(encoding="utf-8"),
        critic_report=critic_report,
    )
    prover = run_model("prover", prover_prompt, config, out_dir, dry_run=dry_run)
    write_result(out_dir, "proof-attempt.md", prover)
    append_run_log(out_dir, prover)

    proof_text = (out_dir / "proof-attempt.md").read_text(encoding="utf-8")
    drift_prompt = fill(
        read_prompt("statement-drift-verifier.md"),
        problem=problem_text,
        locked_statement=locked_statement,
        exploration=(out_dir / "exploration-map.md").read_text(encoding="utf-8"),
        proof=proof_text,
    )
    drift = run_model(
        "verifier",
        drift_prompt,
        config,
        out_dir,
        dry_run=dry_run,
        result_role="statement_drift_verifier",
    )
    write_result(out_dir, "statement-drift-report.md", drift)
    append_run_log(out_dir, drift)
    append_jsonl(
        out_dir,
        "verifier-reports.jsonl",
        {
            "id": "V1",
            "stage": "statement_drift",
            "artifact": "statement-drift-report.md",
            "provider": drift.provider,
            "model": drift.model,
            "returncode": drift.returncode,
        },
    )

    verifier_prompt = fill(
        read_prompt("verifier.md"),
        problem=problem_text,
        locked_statement=locked_statement,
        exploration=(out_dir / "exploration-map.md").read_text(encoding="utf-8"),
        proof=proof_text,
        drift_report=(out_dir / "statement-drift-report.md").read_text(encoding="utf-8"),
    )
    verifier = run_model("verifier", verifier_prompt, config, out_dir, dry_run=dry_run)
    write_result(out_dir, "verification-report.md", verifier)
    append_run_log(out_dir, verifier)
    append_jsonl(
        out_dir,
        "verifier-reports.jsonl",
        {
            "id": "V2",
            "stage": "whole_proof",
            "artifact": "verification-report.md",
            "provider": verifier.provider,
            "model": verifier.model,
            "returncode": verifier.returncode,
        },
    )

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
    write_static_artifacts(out_dir, problem_text, "verify")
    (out_dir / "proof-attempt.md").write_text(proof_text, encoding="utf-8")
    locked_statement = (out_dir / "locked-statement.md").read_text(encoding="utf-8")

    drift_prompt = fill(
        read_prompt("statement-drift-verifier.md"),
        problem=problem_text,
        locked_statement=locked_statement,
        exploration="(verification-only run)",
        proof=proof_text,
    )
    drift = run_model(
        "verifier",
        drift_prompt,
        config,
        out_dir,
        dry_run=dry_run,
        result_role="statement_drift_verifier",
    )
    write_result(out_dir, "statement-drift-report.md", drift)
    append_run_log(out_dir, drift)
    append_jsonl(
        out_dir,
        "verifier-reports.jsonl",
        {
            "id": "V1",
            "stage": "statement_drift",
            "artifact": "statement-drift-report.md",
            "provider": drift.provider,
            "model": drift.model,
            "returncode": drift.returncode,
        },
    )

    verifier_prompt = fill(
        read_prompt("verifier.md"),
        problem=problem_text,
        locked_statement=locked_statement,
        exploration="(verification-only run)",
        proof=proof_text,
        drift_report=(out_dir / "statement-drift-report.md").read_text(encoding="utf-8"),
    )
    verifier = run_model("verifier", verifier_prompt, config, out_dir, dry_run=dry_run)
    write_result(out_dir, "verification-report.md", verifier)
    append_run_log(out_dir, verifier)
    append_jsonl(
        out_dir,
        "verifier-reports.jsonl",
        {
            "id": "V2",
            "stage": "whole_proof",
            "artifact": "verification-report.md",
            "provider": verifier.provider,
            "model": verifier.model,
            "returncode": verifier.returncode,
        },
    )
    write_followup_artifacts(out_dir)


def write_followup_artifacts(out_dir: Path) -> None:
    verification = (out_dir / "verification-report.md").read_text(encoding="utf-8")
    drift = (out_dir / "statement-drift-report.md").read_text(encoding="utf-8")
    critic_path = out_dir / "fresh-critic-report.md"
    if not critic_path.exists():
        critic_path.write_text(
            "# Fresh Critic Report\n\nNo fresh-context critic was run for this mode.\n",
            encoding="utf-8",
        )

    (out_dir / "approach-queue.md").write_text(
        "# Approach Queue\n\n"
        "Extract concrete proof and disproof routes from `exploration-map.md`, "
        "`fresh-critic-report.md`, and `proof-attempt.md`.\n\n"
        "Each route should also have a corresponding record in `method-matrix.jsonl`.\n",
        encoding="utf-8",
    )
    (out_dir / "proof-route-log.md").write_text(
        "# Proof Route Log\n\n"
        "Record proof-side attempts here. Each entry should name the method, target "
        "lemma, exact dependency on the locked statement, verifier status, and next "
        "test.\n",
        encoding="utf-8",
    )
    (out_dir / "counterexample-log.md").write_text(
        "# Counterexample Log\n\n"
        "Record disproof-side attempts here. Each entry should state the object being "
        "constructed, which hypothesis it satisfies, which conclusion it is meant to "
        "break, and the current obstruction.\n\n"
        "Machine-readable entries belong in `counterexample-attempts.jsonl`.\n",
        encoding="utf-8",
    )
    (out_dir / "claim-map.md").write_text(
        "# Claim Map\n\n"
        "Create one node per lemma/proposition. Attach verifier verdicts from "
        "`statement-drift-report.md` and `verification-report.md`.\n",
        encoding="utf-8",
    )
    (out_dir / "failure-ledger.md").write_text(
        "# Failure Ledger\n\n"
        "Branches should be marked `failed`, `blocked`, `uncertain`, or "
        "`needs human input` with reasons. Prefer a precise failed lemma or failed "
        "construction over a vague global failure.\n",
        encoding="utf-8",
    )
    (out_dir / "next-actions.md").write_text(
        "# Next Actions\n\n"
        "1. Read `statement-drift-report.md` before trusting any proof work.\n"
        "2. Read `verification-report.md`.\n"
        "3. Promote only claims that preserve the locked statement and pass verification.\n"
        "4. Rewrite, counterattack, or stop branches marked `FAIL` or `UNCERTAIN`.\n",
        encoding="utf-8",
    )
    (out_dir / "attack-certificate.md").write_text(
        "# Attack Certificate\n\n"
        "## Success Tier\n\n"
        "Choose one: `T0_refuted`, `T1_proved_and_verified`, "
        "`T2_conditionally_proved`, `T3_reduced_to_named_bottleneck`, "
        "`T4_attacked_unresolved`, `T5_incoherent_or_drifted`.\n\n"
        "## Drift Gate\n\n"
        f"{drift.strip()}\n\n"
        "## Verification Gate\n\n"
        f"{verification.strip()}\n\n"
        "## Required Human Audit\n\n"
        "- Did every promoted route return to `locked-statement.md`?\n"
        "- Were both proof and counterexample lanes attempted?\n"
        "- Are external theorems recorded in `retrieved-theorems.jsonl` with definitions "
        "and applicability checks?\n"
        "- Is the final status weaker than a solution if any verifier report is not `PASS`?\n",
        encoding="utf-8",
    )
