# RP2 Packing Attack Certificate

## Locked Target

Study Lagrangian `RP2` packing questions in many-point blowups of `CP2`, especially the existence and smooth isotopy uniqueness of embedded Lagrangian `RP2`s in fixed `Z/2` homology classes.

## Success Tier

`T3_reduced_to_named_bottleneck`

The run did not classify the full packing cone. It reduced the project to a boundary-to-interior persistence lemma and concrete boundary-configuration tasks.

## Statement Drift Gate

Verdict: `MINOR_CLARIFICATION`

The run narrows the broad classification question to a reusable perturbation principle. This is a partial research-state result, not a replacement theorem for the full classification.

## Verification Gate

Verdict: `UNCERTAIN`

The compactness-and-continuity proof outline is plausible and useful as a candidate lemma, but the public artifact does not include independent expert verification or formal proof checking.

## Proof-Side Route

Show that a positive margin for the relaxed obstruction-area minimum persists under sufficiently small inward perturbations.

Core ingredients:

- compactness of the relaxed obstruction domain;
- continuity of the objective pairing;
- continuity of the marginal minimum;
- elementary positive-margin argument.

## Disproof-Side Pressure

The proof route can fail if:

- the relaxed obstruction domain is not actually compact in the required setting;
- the relaxed domain is too weak or too strong compared with genuine exceptional classes;
- the perturbation direction leaves the relevant packing framework;
- boundary non-uniqueness examples do not exist in the required class;
- the smooth isotopy distinction is not preserved by the perturbation argument.

## Bottleneck Lemmas

- Precise compactness statement for the obstruction class domain.
- Applicability of the relaxed constraint model to the actual packing cone.
- Construction of boundary configurations with distinct smooth isotopy classes.
- Invariant separating the candidate `RP2` surfaces.

## Reusable Output

The main reusable output is not a full classification theorem. It is a stability template:

> Boundary non-uniqueness plus a positive area margin should imply nearby interior non-uniqueness, provided the obstruction model and isotopy distinction are stable under the perturbation.

## Next Target

Choose one explicit boundary configuration and verify all hypotheses of the persistence template by hand or by a specialized symplectic-topology checker.

## Human Audit Required

This run needs expert review on:

- exact hypotheses of the compactness domain;
- whether the relaxed model faithfully reflects exceptional classes;
- whether the perturbation preserves the desired Lagrangian representatives;
- whether the proposed smooth non-isotopy certificate is valid.
