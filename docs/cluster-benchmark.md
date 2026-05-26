# Cluster Benchmark

REC should not be evaluated only as a solver for isolated theorem statements. Its natural benchmark unit is a topic-focused cluster of related mathematical questions.

## Definition

A REC cluster benchmark is a coherent set of conjectures, questions, examples, or problem-list entries that share definitions, methods, examples, or obstruction technology.

The goal is not solved-theorem count. The goal is to test whether the copilot preserves and improves the research state across the cluster.

## Suitable Inputs

Good benchmark clusters include:

- survey problem lists
- seminar problem sets
- conjecture families
- open-question clusters around one invariant
- related examples and counterexamples in one subfield
- topic-focused lists collected from papers or working notes

The Gompf problem list is one instance of this benchmark type, not the definition of the benchmark.

## Required Properties

A useful cluster should have:

- multiple related targets
- shared definitions or background objects
- meaningful proof and disproof routes
- enough difficulty that false solution claims are a real risk
- opportunities for memory from one target to improve later targets
- a meaningful next-target selection problem

## Required Output

For each target, REC should produce:

- locked statement
- proof-side route
- disproof-side or missing-hypothesis route
- bottleneck lemma or obstruction
- failure mode or warning
- verifier status
- next target or next test

For the whole cluster, REC should produce:

- cluster map
- shared obstruction ledger
- repeated-error ledger
- reusable statement list
- prioritized next-target list
- attack certificate summary

## Metrics

Cluster-level metrics should include:

- target preservation rate
- drift detection rate
- proof-route coverage
- disproof-route coverage
- shared obstruction recovery
- repeated-error reduction
- cross-question memory usefulness
- next-target specificity
- human-rated usefulness
- topic coherence preservation

## Benchmark Claim

The benchmark claim should be phrased carefully:

> REC is evaluated by how well it turns a cluster of related mathematical questions into a structured research state: locked targets, route matrices, obstruction logs, reusable warnings, and prioritized next targets.

A high score does not mean REC solved the cluster. It means the resulting research state is useful, faithful, and auditable.
