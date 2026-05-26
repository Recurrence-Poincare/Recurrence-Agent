# Recurrence-Agent

Recurrence-Agent is a research design for AI-assisted mathematics. It is meant for hard problems where the useful output is not only a proof attempt, but a map of ideas, failures, counterexamples, partial lemmas, and verification pressure.

The project is currently published as a clean specification repository. Runnable code will be added only after it has been written under this project and passes the publication checklist in `docs/publication-checklist.md`.

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

Attack mode should not drift into a different theorem. Each branch must explain how it returns to the original conjecture.

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
exploration-map.md
approach-queue.md
counterexample-log.md
claim-map.md
verification-report.md
failure-ledger.md
proof-attempt.md
next-actions.md
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

This repository is intentionally lightweight right now. It contains the public design, workflow, and publication rules for Recurrence-Agent.

Runnable implementation will be added later in small, auditable pieces.

## Documentation

- `docs/architecture.md`: proposed system architecture
- `docs/workflows.md`: explore, attack, and verification workflows
- `docs/memory-map.md`: how runs should be recorded and connected
- `docs/publication-checklist.md`: required checks before adding public code
- `examples/problem-template.md`: template for input problems

## License

No license has been granted yet. All rights reserved unless a license file is added later.
