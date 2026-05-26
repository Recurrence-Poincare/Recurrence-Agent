# Gompf Cluster Benchmark

This run applies REC attack mode to a 22-target low-dimensional topology cluster: 20 numbered problems and 2 named conjectures from the Gompf problem list.

## Status

No Gompf open problem is claimed solved.

The verified object is a research-state attack certificate over the cluster: every target has a locked statement, proof-side route, disproof-side route, bottleneck, side lemma or warning, failure mode, and next-target recommendation.

## Cluster Scope

The targets span:

- symplectic and smooth 4-manifolds
- symplectic geography
- handle theory and bordism
- knot concordance and filtrations
- contact and Stein geometry
- homology balls and punctured 3-manifold embeddings

## Summary Metrics

| Quantity | Value |
| --- | ---: |
| Open-problem targets | 22 |
| Numbered problems | 20 |
| Named conjectures | 2 |
| Locked statements produced | 22 |
| Proof-side routes produced | 22 |
| Disproof-side routes produced | 22 |
| Side lemmas / byproducts produced | 22 |
| Failure modes recorded | 22 |
| Recommended next-target files | 22 |
| Claim-map verdicts | 27 YES / 0 NO / 0 UNCERTAIN |
| False open-problem solution claims | 0 |
| Selected next benchmark target | T18 |

## Selected Next Target

T18 is Gompf's second conjecture:

> No Brieskorn integer homology sphere, other than `S^3`, admits a pseudoconvex embedding in `C^2`, with either orientation.

REC selected T18 because it has:

- an explicit countable input space: pairwise-coprime triples `(p,q,r)` and orientations;
- a one-object counterexample certificate: one nontrivial Brieskorn sphere bounding a Stein domain embedded in `C^2`;
- computable subfamily data from Seifert, plumbing, and Floer-theoretic descriptions.

## Main Interpretation

The run is a cluster-benchmark result, not a theorem-solving result.

The useful output is that the cluster was converted into a structured research state:

- precise target preservation;
- one proof-side and one disproof-side route for every target;
- reusable warnings against common false shortcuts;
- a prioritized next target;
- a verifier-audited claim map for the certificate structure.

## Files

- `attack-certificate.md`: public attack certificate summary.
- `reusable-statements.md`: reusable side lemmas, warnings, and next-target candidates.
- `token-usage.json`: resource accounting for the run.
