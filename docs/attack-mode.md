# Attack Mode Harness

Attack mode is for a conjecture that should be taken seriously. The goal is not free wandering. The goal is to pressure the locked statement from both sides until the run produces a proof, a counterexample, a precise bottleneck, or a useful failure certificate.

## Locked Statement

Every run starts with `locked-statement.md`. This is the target theorem. Agents may propose repairs, variants, or nearby conjectures, but those belong in `statement-repairs.jsonl` and cannot be reported as solutions to the locked statement.

Statement drift includes:

- adding or removing hypotheses
- weakening or strengthening the conclusion
- changing quantifiers
- changing the ambient category
- adding regularity, compactness, finiteness, smoothness, or boundary assumptions
- replacing the theorem with a known adjacent result

## Required Lanes

Attack mode keeps two lanes alive:

- proof lane: methods, decompositions, bottleneck lemmas, citations
- disproof lane: counterexample shapes, toy models, obstruction tests, missing hypotheses

A polished proof attempt is not enough. The run must also record which counterexample risks remain open.

## Plan Generations

The explorer should produce four plan generations:

- A: direct proof methods
- B: structural reductions and known-theorem routes
- C: counterexample constructions and obstruction tests
- D: statement repairs that would make the result plausible

Generation D is useful, but it is not a solution unless the user explicitly changes the locked statement.

## Fresh Critic

Before proof generation, a fresh-context critic reads the locked statement and exploration map. The critic should not continue the search. It should look for drift, missing methods, sunk-cost branches, unclosed counterexample pressure, and unverified references.

## Verification Gates

Attack mode has two verifier gates:

```text
statement-drift verifier
  -> whole-proof verifier
```

If the drift verifier returns `MAJOR_DRIFT`, the whole-proof result cannot be promoted as a proof of the locked statement.

## Success Tiers

Use one of these final tiers in `attack-certificate.md`:

- `T0_refuted`: a counterexample or contradiction to the locked statement is found and verified
- `T1_proved_and_verified`: a proof of the locked statement passes verification
- `T2_conditionally_proved`: proof works after explicit extra hypotheses or cited facts
- `T3_reduced_to_named_bottleneck`: the problem is reduced to a precise unresolved lemma
- `T4_attacked_unresolved`: meaningful proof and disproof pressure was applied, but no decisive result
- `T5_incoherent_or_drifted`: the run lost the statement or produced unusable artifacts

## Reference Discipline

External results should be recorded in `retrieved-theorems.jsonl` with:

- source title or identifier
- exact theorem or proposition used
- definitions required
- applicability check against the locked statement
- proof status: read, skimmed, not checked, or formalized

Do not treat a plausible citation as verified mathematics.
