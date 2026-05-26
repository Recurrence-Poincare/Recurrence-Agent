# Architecture

Recurrence-Agent is organized as a set of roles rather than a single chatbot.

## Roles

### Problem Reader

Extracts the exact statement, hypotheses, conclusion, notation, and hidden dependencies. It must identify what is part of the problem and what is background commentary.

### Explorer

Creates nearby positive and negative conjectures. It is allowed to wander, but every branch must keep a link back to the original statement.

### Attacker

Pushes proof routes and counterexample routes. It should maintain a method matrix:

```text
method
  target lemma
  likely obstruction
  required references
  status
  next test
```

### Decomposer

Turns promising routes into lemma-sized claims. Each claim should be small enough for a verifier to attack directly.

### Prover

Writes proofs for specific claims. The prover must mark nontrivial steps and state what external facts are being used.

### Verifier

Checks claims harshly. It should not repair the proof silently. It should return a verdict and a reason.

### Cartographer

Builds the map of claims, failures, examples, and dependencies. This is the long-term memory layer.

## Data Flow

```text
problem
  -> problem card
  -> exploration map
  -> approach queue
  -> claim graph
  -> proof attempts
  -> verification reports
  -> revised claim graph
  -> next actions
```

Every stage writes an artifact that a human can read.

## Non-Goals

Recurrence-Agent is not meant to be an authority. It is not a substitute for peer review, formal verification, or expert checking. It is a research notebook with active agents inside it.
