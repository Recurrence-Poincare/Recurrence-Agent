# Gompf Reusable Statements

These are candidate research-state artifacts from the Gompf cluster run. They are not claimed solutions.

## Side Lemmas, Byproducts, And Warnings

| ID | Target | Reusable statement | Failure mode / warning |
| --- | --- | --- | --- |
| R1 | T1 | Audit `b^+=1` symplectic / Seiberg-Witten chamber data for a homology `CP^2`. | This route collapses into the unknown smooth uniqueness problem for manifolds homeomorphic to `CP^2`. |
| R2 | T2 | Split torsion-canonical symplectic 4-manifolds by `pi_1`, Euler characteristic, signature, and canonical-class torsion order. | Homological classification alone cannot determine diffeomorphism type in dimension 4. |
| R3 | T3 | Choose a specific Heegaard Floer invariant package and test whether it vanishes on `T_{n+1}` while detecting a certified `T_n` witness. | The invariant may only detect sliceness or the wrong filtration level. |
| R4 | T4 | A 2-torsion witness should certify `K in T_n`, `K notin T_{n+1}`, and `2K in T_{n+1}`. | A candidate is not useful unless membership, nonmembership, and doubling are all certified. |
| R5 | T5 | A split `Z^infty` summand proof needs coordinate homomorphisms or a retraction. | Infinite rank alone does not prove a direct summand. |
| R6 | T6 | A Whitehead-double certificate needs a smooth slice disk for `Wh(K)` and an independent nonsliceness certificate for `K`. | Many classical invariants are killed by Whitehead doubling. |
| R7 | T7 | Build a move-by-move Cerf compatibility table for spin or characteristic data. | One incompatible local move would obstruct the direct proof route. |
| R8 | T8 | Treat `(b1,b2)=(2,1)`, giving `chi=-1`, as the first small negative-Euler threat profile. | Betti arithmetic alone does not construct a symplectic non-ruled manifold. |
| R9 | T9 | Formalize the exact symplectic BMY inequality and hypotheses before proof or counterexample search. | Without a precise inequality, the target is not verifier-ready. |
| R10 | T10 | Analyze positive-definite BMY through handle / perfect-Morse control. | The route may reduce exactly to the unsolved perfect-Morse problem. |
| R11 | T11 | Separate algebraic simplification of presentations from geometric handle cancellation. | Algebraic simple connectivity does not imply handle cancellation. |
| R12 | T12 | Build a dual-handlebody test for necessary 3-handles in weight-one homology-sphere constructions. | The route may only recover already-known 1-handle obstructions. |
| R13 | T13 | Test associated-manifold packages using nonconcordant knots with equivalent associated manifolds. | Associated manifolds can forget concordance information. |
| R14 | T14 | Define "interesting" for satellite-induced homomorphisms before evaluating a theorem. | Otherwise only identity or constant maps may qualify. |
| R15 | T15 | Combine an explicit hyperbolic rational homology sphere with an exhaustive contact/tightness classification. | Constructing tight structures on some families cannot rule out all counterexamples. |
| R16 | T16 | Compare Mark-Tosun nonvanishing with an independent tightness criterion in the exact negative-stabilized surgery family. | A tight example with zero invariant in the exact family would kill the route. |
| R17 | T17 | A Brieskorn embedding certificate must include a nontrivial Brieskorn sphere, orientation, Stein domain, and actual embedding in `C^2`. | Abstract Stein fillability is not enough. |
| R18 | T18 | Decompose Brieskorn integer homology spheres by pairwise-coprime triples `(p,q,r)` and both orientations. | A parametric obstruction leaving an infinite uncovered family does not prove the conjecture. |
| R19 | T19 | Fix the disk category because non-locally-flat disks are allowed unless a variant says otherwise. | Standard sliceness obstructions often require local flatness. |
| R20 | T20 | Separate free actions from nonfree actions and audit fixed-point local models. | A proof handling only free actions does not address the full problem. |
| R21 | T21 | Choose an explicit surgery-theoretic topological 4-manifold before computing smoothing obstructions. | Without a concrete model, there is no obstruction to compute. |
| R22 | T22 | Derive restrictions from embeddings of `S^3_0(K)-B^3` in `S^4`, not closed embeddings of `S^3_0(K)`. | Closed-embedding arguments do not automatically apply to punctured embeddings. |

## High-Priority Next Lemma Candidates

| ID | Target | Candidate task | Why it matters |
| --- | --- | --- | --- |
| H1 | T18 | For a fixed Brieskorn family such as `Sigma(2,3,6n +/- 1)`, prove that neither orientation can occur as the pseudoconvex boundary of a Stein domain embedded in `C^2`. | Explicit infinite family and direct relevance to Gompf Conjecture 2. |
| H2 | T16 | In the Mark-Tosun negative-stabilized surgery family, prove or refute that tightness is equivalent to nonvanishing of the Heegaard Floer contact invariant. | Concrete criterion and good bridge between computation and tightness. |
| H3 | T3 | Choose one Heegaard Floer invariant package and test it against a certified bipolar filtration knot family. | Turns an open question into a verifier-ready invariant test. |
| H4 | T7 | Given Gay's oriented Cerf proof, audit each local move for spin or characteristic compatibility. | A finite audit could produce a proof path or a precise obstruction. |
| H5 | T22 | For `Y=S^3_0(K)`, derive necessary conditions from an embedding `Y-B^3 -> S^4`. | Makes the punctured-vs-closed distinction explicit. |
| H6 | T12 | For a selected weight-one homology sphere and generator knot, prove a 3-handle obstruction or construct a failure example. | Focused examples may clarify known handle obstructions. |
| H7 | T17/T18 | Find or rule out one nontrivial Brieskorn integer homology sphere bounding a Stein domain embedded in `C^2`. | One positive example answers T17 and refutes T18; one ruled-out family strengthens T18 evidence. |
