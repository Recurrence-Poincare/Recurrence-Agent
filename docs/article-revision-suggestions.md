# Article Revision Suggestions

The article should not pitch REC as a better prover, verifier, formalizer, or generic multi-agent system. The practical contribution is narrower and more defensible:

> REC turns an AI-assisted attack on a fragile mathematical target into an auditable research-state artifact: locked statement, route matrix, counterexample pressure, drift report, verifier report, failure ledger, and next-target certificate.

## Stronger Thesis

Use this framing:

> Recurrence is a locked-statement research-state harness. It evaluates progress by whether an AI run preserves the exact target, applies proof-side and disproof-side pressure, detects statement drift, and outputs a reusable attack certificate.

## Reduce These Claims

- multi-agent orchestration as novelty
- generator/checker separation as novelty
- best-of-N, retrieval, or verifier loops as novelty
- natural-language verification as mathematical certification
- "self-evolving" language unless it is clearly limited to artifact memory and prompt state

## Emphasize These Claims

- locked statement discipline
- statement-drift detection
- simultaneous proof and disproof lanes
- failed routes as reusable mathematical guardrails
- attack certificates as the measurable output
- human evaluation of next-target quality
- complementarity with Lean/formal systems downstream

## Suggested System Diagram

```text
problem
  -> locked statement
  -> proof/disproof route matrix
  -> fresh-context critic
  -> proof attempt
  -> statement-drift verifier
  -> whole-proof verifier
  -> attack certificate
  -> memory
```

## Evaluation Metrics

Add artifact-level metrics:

- target preservation rate
- drift detection rate
- branch return-to-target coverage
- verifier-labeled claim coverage
- failed routes converted into reusable warnings
- next-target files produced
- human-rated next-target usefulness

## Key Caution

If the verifier labels an attack certificate as structurally honest, that is not the same as proving the underlying open theorem. The paper should keep that distinction visible.
