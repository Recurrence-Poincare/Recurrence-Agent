# Gompf Attack Certificate

## Locked Target

The locked target is the full Gompf problem list: 20 numbered open problems and 2 named conjectures.

## Success Tier

`T4_attacked_unresolved`

The cluster was meaningfully attacked and mapped, but no open problem was solved or refuted.

## Certificate Verification

Structural certificate status: `PASS`

The verifier-checked claim is the honesty and completeness of the attack certificate, not the truth or falsity of the underlying open problems.

## Statement Drift Gate

Verdict: `NO_DRIFT`

The run preserved all 22 original targets as locked statements. Category warnings were explicitly recorded rather than silently changing the targets.

## Whole-Certificate Gate

Verdict: `PASS`

The certificate records for each target:

- proof-side route;
- disproof or missing-hypothesis route;
- bottleneck;
- side lemma or byproduct;
- failure mode;
- next single-target recommendation.

## Proof Routes Tried

The run did not try to prove the open problems directly. It produced route capsules for all 22 targets.

High-priority proof-side routes:

- T18: family-wise obstruction for Brieskorn pseudoconvex embeddings.
- T16: compare contact invariant nonvanishing and tightness in the exact negative-stabilized surgery family.
- T22: derive concordance-invariant restrictions from punctured zero-surgery embeddings.
- T7: audit spin/characteristic compatibility of Cerf moves.
- T3: choose a concrete Heegaard Floer invariant package for the bipolar filtration.

## Disproof Routes Tried

No counterexample was verified.

High-priority disproof routes:

- T18: find one nontrivial Brieskorn integer homology sphere, in either orientation, bounding a Stein domain embedded in `C^2`.
- T16: find a tight contact structure with vanishing contact invariant in the exact target family.
- T6: find a nonslice knot with smoothly slice untwisted Whitehead double.
- T22: find a punctured embedding of `S^3_0(K) - B^3` into `S^4` for a nonslice knot `K`.

## Reusable Warnings

- Do not conflate smooth and topological categories in dimension 4.
- Do not replace non-locally-flat sliceness with locally-flat sliceness unless stated.
- Do not replace "Stein domain embedded in `C^2`" with abstract Stein fillability.
- Do not replace punctured embeddings `Y - B^3 -> S^4` with closed embeddings `Y -> S^4`.
- Do not treat infinite rank as a split `Z^infty` summand without a retraction.

## Next Target

Create a focused single-target run for T18:

> Attack Gompf's Brieskorn pseudoconvex embedding conjecture by subfamilies `(p,q,r)` and orientation, using computable Seifert/plumbing/Floer data and an explicit one-object counterexample format.

## Human Audit Required

This certificate should be reviewed for:

- faithfulness to the original problem statements;
- usefulness of route choices;
- mathematical correctness of category warnings;
- priority of T18 as next target;
- completeness of reusable warnings.
