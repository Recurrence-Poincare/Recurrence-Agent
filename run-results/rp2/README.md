# Lagrangian RP2 Packing Run

This run studies a cluster around Lagrangian real projective planes in rational symplectic 4-manifolds, especially many-point blowups of `CP2`.

## Status

This is a research-state case study, not a complete classification of the Lagrangian `RP2` packing cone.

The useful output is a candidate reusable lemma and a decomposition of the larger program into more focused mathematical tasks.

## Background Cluster

The run used background from:

- Shevchishin--Smirnov, *Symplectic Triangle Inequality*.
- Evans, *A Lagrangian Klein bottle you can't squeeze*.
- Adaloglou, work on Lagrangian pinwheels and rational blowups.

The shared theme is rigidity and flexibility of nonorientable Lagrangian surfaces in rational symplectic 4-manifolds.

## Research Question

Let `X_k` be `CP2` blown up at `k` balls. For `k > 10`, exceptional classes become infinite and the finite triangle-inequality picture is no longer enough.

The cluster asks:

1. Which symplectic packing forms on `X_k` admit embedded Lagrangian `RP2`s?
2. In a fixed `Z/2` homology class, are such `RP2`s smoothly unique?
3. Near the boundary of the packing cone, can boundary non-uniqueness be transported into nearby honest symplectic forms?

## Partial Achievement

The run isolated a boundary-to-interior persistence principle:

> If a boundary-positive form in the `RP2` packing framework has a positive obstruction margin, then a sufficiently small inward perturbation remains in the positive region. Consequently, once boundary data provide two smoothly non-isotopic `RP2`s in the same `Z/2` class, the continuity argument gives a nearby interior window where this non-uniqueness persists.

This does not classify the full cone. It converts a global classification problem into a reusable stability lemma plus concrete next tasks.

## Proof Mechanism

The proof strategy is compactness and continuity:

- define a relaxed compact constraint space for obstruction classes;
- express the relevant area minimum as a continuous marginal function;
- use positivity at the boundary-positive point;
- conclude that small perturbations preserve positivity.

## Next Tasks

- Make the obstruction class domain precise enough for independent verification.
- Identify concrete boundary configurations with two smoothly non-isotopic `RP2`s in the same `Z/2` class.
- Translate candidate boundary configurations into almost toric diagrams.
- Compute or compare disk-counting invariants when available.
- Decide which parts should be formalized or checked by a symplectic topologist.

## Files

- `attack-certificate.md`: conservative public certificate for this run.
- `references.md`: background references and their role in the cluster.
