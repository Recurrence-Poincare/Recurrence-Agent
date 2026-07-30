# Paper Positioning

Current paper title:

> Recurrence: An Evolving Research-State Copilot for Mathematics

## Core Claim

REC is not primarily a stronger prover, verifier, or formalizer. REC is a research-state copilot: it turns an AI-assisted mathematical investigation into durable artifacts that a human or later agent can inspect and reuse.

## Research State

Research state means the durable, inspectable record of where a mathematical investigation currently stands:

- exact target statements
- active proof routes
- active disproof routes
- examples and toy models
- obstructions and missing hypotheses
- failed attempts
- verifier judgments
- reusable lemmas
- prioritized next steps

## Repo-To-Paper Mapping

| Paper idea | Repository component |
| --- | --- |
| locked statement discipline | `locked-statement.md`, `prompts/statement-drift-verifier.md` |
| proof/disproof pressure | `prompts/explorer.md`, `method-matrix.jsonl`, `counterexample-attempts.jsonl` |
| fresh-context critique | `prompts/attack-critic.md`, `fresh-critic-report.md` |
| drift verification | `statement-drift-report.md` |
| attack certificate | `attack-certificate.md`, `docs/attack-certificate-schema.md` |
| cluster benchmark | `docs/cluster-benchmark.md` |
| representative results | `run-results/gompf/`, `run-results/rp2/` |
| public hygiene | `docs/publication-checklist.md`, `scripts/privacy_scan.py` |

## Benchmark Framing

The Gompf problem list should be described as one instance of a cluster benchmark. A cluster benchmark can be any topic-focused list of related conjectures, questions, or problem-list entries.

The evaluation target is not solved-problem count. The evaluation target is whether REC produces a faithful, useful, auditable research state across the cluster.

## Safer Claims

Use:

- research-state copilot
- locked-statement attack certificate
- topic-focused cluster benchmark
- proof-side and disproof-side pressure
- statement-drift gate
- human-auditable next targets

Avoid:

- autonomous theorem solver
- verified proof of open problems
- replacement for formal verification
- novelty claims for generic multi-agent orchestration
