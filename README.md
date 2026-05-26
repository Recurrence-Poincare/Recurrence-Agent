# Recurrence: An Evolving Research-State Copilot for Mathematics

Recurrence-Agent is a small CLI-first research-state harness for AI-assisted mathematics. It is meant for hard problems where the useful output is not only a proof attempt, but a locked statement, an attack certificate, and a reusable map of ideas, failures, counterexamples, partial lemmas, and verification pressure.

The practical selling point is narrow: REC is not trying to outperform formal proof systems or frontier proof agents at final theorem proving. It tries to make research-level attempts auditable before a final proof exists. The core product is a run directory that says exactly what statement was attacked, what proof and disproof routes were tried, where the attempt drifted, what the verifier rejected, and what a human or later agent should do next.

We use **research state** to mean the durable, inspectable record of where a mathematical investigation currently stands: exact target statements, active proof and disproof routes, examples, obstructions, failed attempts, verifier judgments, reusable lemmas, and prioritized next steps.

The public runner is intentionally minimal and auditable. It has four main roles:

- `explorer`: maps nearby conjectures, examples, obstructions, and routes back to the original problem.
- `prover`: writes a proof attempt from the selected route.
- `verifier`: checks the proof harshly and returns `PASS`, `FIXABLE`, `FAIL`, or `UNCERTAIN`.
- `critic`: performs a fresh-context attack audit before proof generation.

Each role can be assigned to a CLI provider in `config.yaml`. The default prover is Codex/GPT-5.5 with extra-high reasoning. The verifier can be configured as GPT/Codex or Gemini; Gemini is the default verifier in the sample config.

Desktop wrappers are possible, but the recommended way to run Recurrence-Agent is from the command line. The CLI keeps runs reproducible, easier to audit, and easier to script.

## Core Idea

Most proof agents drift. They make plausible nearby claims, polish weak arguments, and forget the original conjecture. Recurrence-Agent is built around a stricter loop:

```text
state the conjecture
  -> explore nearby positive and negative directions
  -> choose concrete proof and disproof routes
  -> decompose the routes into checkable claims
  -> verify each claim harshly
  -> record failures and bottlenecks
  -> return to the original conjecture
```

The name "Recurrence" is literal: the agent is allowed to wander, but it must keep returning to the stated problem.

## What REC Is Not Selling

REC does not claim novelty for ordinary multi-agent orchestration, generator/checker separation, best-of-N sampling, retrieval-augmented proof search, or Lean verification. Those are valuable, but other systems already pursue them directly.

REC's distinct layer is the artifact contract around an open or fragile mathematical target:

- freeze the target before search starts
- preserve proof-side and disproof-side pressure at the same time
- record drift as a first-class failure mode
- turn failed routes into reusable warnings and next targets
- produce an attack certificate instead of a vague transcript

## Modes

### Explore Mode

Explore mode is for open-ended problems and unclear conjectures. It builds a local map around the problem:

- nearby stronger and weaker statements
- possible counterexamples
- examples worth computing
- standard tools that might apply
- bottleneck lemmas
- failed approaches and why they failed

The purpose is not to claim a solution. The purpose is to make the research landscape inspectable.

### Attack Mode

Attack mode is for a conjecture supplied with strong human belief. It treats the statement seriously and pushes both directions:

- every plausible proof method
- every plausible counterexample construction
- every dangerous missing hypothesis
- every lemma that would make the proof work

Attack mode should not drift into a different theorem. Each branch must explain how it returns to the locked statement.

The attack runner writes a hard artifact contract:

- `locked-statement.md`: the frozen target statement for the run
- `statement-drift-report.md`: a verifier pass that checks whether the proof changed the theorem
- `fresh-critic-report.md`: an independent critic pass before proof generation
- `method-matrix.jsonl`: proof and disproof route records
- `counterexample-attempts.jsonl`: negative-direction attempts
- `retrieved-theorems.jsonl`: external references with applicability checks
- `attack-certificate.md`: final tier, drift gate, verifier gate, and human audit checklist

### Verification Mode

Verification mode separates proof generation from proof checking. A verifier should be adversarial, not supportive.

Verifier outputs should be one of:

- `PASS`: the claim is certified from the supplied material
- `FIXABLE`: the idea may work, but a specific repair is required
- `FAIL`: the claim is false or unsupported
- `UNCERTAIN`: the verifier cannot certify the claim

## Expected Artifacts

A run should produce research artifacts, not just a final answer:

```text
problem.md
locked-statement.md
exploration-map.md
fresh-critic-report.md
approach-queue.md
proof-route-log.md
counterexample-log.md
claim-map.md
statement-drift-report.md
verification-report.md
failure-ledger.md
proof-attempt.md
next-actions.md
attack-certificate.md
```

The failure ledger is important. A failed route that explains why it failed is useful mathematical information.

## Design Principles

- Keep generation and verification separate.
- Prefer distinct approaches over repeated rewrites.
- Record uncertainty explicitly.
- Make counterexample search a first-class workflow.
- Decompose arguments into lemma-sized claims.
- Do not promote a proof unless the verifier can say what was checked.
- Preserve enough notes that a human can resume the search.
- Return to the original conjecture after every exploratory branch.

## Repository Status

This repository contains the first clean public REC components:

- a Python CLI runner
- role prompts for explorer, prover, verifier, drift verifier, and critic
- configurable CLI provider templates
- shell wrappers for normal runs and proof-only verification
- docs and examples

It is not a mature package. Treat it as a public scaffold for the Recurrence agent.

## Components

```text
rec/             Python CLI and runner
prompts/         Explorer, prover, and verifier prompts
config.yaml      Provider and role configuration
run_rec.sh       CLI wrapper for the full workflow
run_verifier.sh  CLI wrapper for proof-only verification
docs/            Architecture, workflows, memory map, publication rules
scripts/         Repository hygiene and privacy checks
tests/           Dry-run artifact-contract checks
examples/        Problem template
```

## Installation

```bash
git clone https://github.com/Recurrence-Poincare/Recurrence-Agent.git
cd Recurrence-Agent

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Install at least one model CLI. The sample config uses Codex for exploration/proving and Gemini for verification.

```bash
npm install -g @openai/codex
npm install -g @google/gemini-cli
```

Claude can also be configured as a role provider:

```bash
npm install -g @anthropic-ai/claude-code
```

## Configuration

The default role assignment is:

```yaml
roles:
  prover:
    provider: codex
    model: gpt-5.5
    reasoning_effort: extra-high
  verifier:
    provider: gemini
    model: gemini-3.1-pro-preview
  critic:
    provider: gemini
    model: gemini-3.1-pro-preview
```

You can switch the verifier to GPT/Codex by editing `config.yaml`:

```yaml
roles:
  verifier:
    provider: codex
    model: gpt-5.5
    reasoning_effort: extra-high
```

The provider commands are templates. If your local CLI uses different flags, edit the corresponding command under `providers`.

## Quick Start

Dry-run without calling any model CLI:

```bash
python3 -m rec run examples/problem-template.md --out runs/dry-run --dry-run
```

Run with the configured CLIs:

```bash
./run_rec.sh examples/problem-template.md runs/example config.yaml
```

Verify an existing proof:

```bash
./run_verifier.sh problem.md proof.md runs/verify config.yaml
```

Run the local checks:

```bash
python3 -m compileall rec
python3 -m unittest discover -s tests
python3 scripts/privacy_scan.py
```

Outputs are written under the selected `runs/` directory:

```text
problem.md
locked-statement.md
exploration-map.md
fresh-critic-report.md
proof-attempt.md
statement-drift-report.md
verification-report.md
approach-queue.md
proof-route-log.md
counterexample-log.md
claim-map.md
failure-ledger.md
next-actions.md
attack-certificate.md
run-log.jsonl
```

## Documentation

- `docs/architecture.md`: proposed system architecture
- `docs/workflows.md`: explore, attack, and verification workflows
- `docs/attack-mode.md`: locked-statement attack harness
- `docs/attack-certificate-schema.md`: attack certificate template and required fields
- `docs/ci-workflow-template.yml`: GitHub Actions template; copy to `.github/workflows/ci.yml` after granting `workflow` scope
- `docs/cluster-benchmark.md`: benchmark protocol for topic-focused question clusters
- `docs/paper-positioning.md`: current paper title and repo-to-paper alignment
- `docs/positioning.md`: practical selling point and article framing
- `docs/article-revision-suggestions.md`: paper framing notes
- `docs/memory-map.md`: how runs should be recorded and connected
- `docs/publication-checklist.md`: required checks before adding public code
- `examples/problem-template.md`: template for input problems
- `examples/toy-cluster.md`: small sanitized example input
- `examples/toy-output/`: expected artifact shape for a toy run

## License

No license has been granted yet. All rights reserved unless a license file is added later.
