# Attack Certificate Schema

An attack certificate is the final human-readable summary of an attack-mode run. It is not automatically a proof of the original theorem. It records what was attacked, what was checked, what failed, and what should happen next.

## Required Fields

```yaml
certificate_id:
run_id:
created_at:
mode: attack
success_tier:
locked_statement:
statement_drift_verdict:
whole_proof_verdict:
proof_routes:
disproof_routes:
counterexample_pressure:
retrieved_theorems:
failed_routes:
bottleneck_lemmas:
verifier_objections:
human_audit_required:
next_target:
```

## Success Tiers

- `T0_refuted`: a counterexample or contradiction to the locked statement is found and verified
- `T1_proved_and_verified`: a proof of the locked statement passes verification
- `T2_conditionally_proved`: proof works after explicit extra hypotheses or cited facts
- `T3_reduced_to_named_bottleneck`: the problem is reduced to a precise unresolved lemma
- `T4_attacked_unresolved`: meaningful proof and disproof pressure was applied, but no decisive result
- `T5_incoherent_or_drifted`: the run lost the statement or produced unusable artifacts

## Markdown Template

```markdown
# Attack Certificate

## Locked Statement

Summarize the exact target statement and link to `locked-statement.md`.

## Success Tier

Choose one: `T0_refuted`, `T1_proved_and_verified`, `T2_conditionally_proved`, `T3_reduced_to_named_bottleneck`, `T4_attacked_unresolved`, `T5_incoherent_or_drifted`.

## Statement Drift Gate

Verdict: `NO_DRIFT | MINOR_CLARIFICATION | MAJOR_DRIFT | UNCERTAIN`

Evidence:

## Whole-Proof Verification Gate

Verdict: `PASS | FIXABLE | FAIL | UNCERTAIN`

Evidence:

## Proof Routes Tried

| id | method | target lemma | status | next test |
| --- | --- | --- | --- | --- |

## Disproof Routes Tried

| id | construction | intended failure | status | next test |
| --- | --- | --- | --- | --- |

## Counterexample Pressure

List live risks that the proof did not close.

## Retrieved Theorems

List citations, definitions checked, applicability checks, and proof-read status.

## Failed Routes

List failed routes as reusable warnings.

## Bottleneck Lemmas

List unresolved lemmas that would change the state of the problem.

## Human Audit

- Did the proof preserve the locked statement?
- Were proof and disproof lanes both attempted?
- Were external facts checked rather than merely cited?
- Is any success claim weaker than a theorem proof if verification is not `PASS`?

## Next Target

Name the next single target, computation, example, or literature check.
```

## Promotion Rule

Do not report a theorem as solved unless:

- the drift gate is `NO_DRIFT` or an explicitly harmless clarification
- the whole-proof verifier returns `PASS`
- all external facts used in the proof have been checked or formalized
- a human or formal checker has reviewed the promoted claim
