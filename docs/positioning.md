# REC Positioning

REC should not be sold as a stronger theorem prover, a better Lean formalizer, or a generic multi-agent framework. Those claims are already covered by stronger systems.

The practical selling point is:

> REC turns an AI math attempt into an auditable research-state package: a locked statement, proof-side pressure, disproof-side pressure, drift checks, verifier objections, failed-route memory, and a next-target certificate.

## What Other Systems Already Have

Do not claim novelty for:

- generator/checker separation
- verifier agents
- best-of-N proof attempts
- web or literature retrieval
- Lean or formal proof checking
- multi-agent orchestration
- autonomous proof repair loops
- isolated benchmark problem solving

These are important components, but they are not REC's differentiator.

## REC's Differentiator

REC is strongest when the target is open, broad, fragile, or research-level. In that setting, the valuable question is often not "did the agent solve it?" but:

- Did it preserve the exact statement?
- Did it avoid proving a nearby theorem?
- Did it record both proof routes and counterexample pressure?
- Did it identify missing hypotheses?
- Did it convert failures into reusable mathematical guardrails?
- Did it produce the next useful lemma, computation, example, or literature check?

This is the research-state niche.

## Attack Mode Claim

Attack mode should be described as a locked-statement pressure test.

It must produce:

- `locked-statement.md`
- proof route records
- counterexample route records
- `statement-drift-report.md`
- `verification-report.md`
- `attack-certificate.md`

The final result should be a tier, not a binary success claim:

- `T0_refuted`
- `T1_proved_and_verified`
- `T2_conditionally_proved`
- `T3_reduced_to_named_bottleneck`
- `T4_attacked_unresolved`
- `T5_incoherent_or_drifted`

## Article Revision Direction

The article should move away from "another agentic proof pipeline" and toward "a benchmarkable artifact contract for research-state preservation."

Recommended framing:

1. Claim less about solving mathematics.
2. Claim more about preserving exact statements and avoiding false progress.
3. Treat Gompf as a benchmark for research-state quality, not theorem discovery.
4. Make attack certificates the central measurable object.
5. Compare explicitly against formal-proof agents as complementary downstream consumers.

## Bad Pitch

"REC is a multi-agent system that proves hard open problems."

This is too broad, too easy to attack, and not true enough.

## Better Pitch

"REC is a CLI-first harness for turning AI-assisted attacks on research-level conjectures into auditable artifacts: locked statements, route matrices, counterexample pressure, verifier reports, failure ledgers, and next-target certificates."
