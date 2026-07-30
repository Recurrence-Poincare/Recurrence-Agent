# Architecture

Recurrence-Agent is organized as a set of roles rather than a single chatbot.

## Roles

### Problem Reader

Extracts the exact statement, hypotheses, conclusion, notation, and hidden dependencies. It must identify what is part of the problem and what is background commentary.

The runner writes this into `locked-statement.md`. Later agents may criticize or repair the statement, but they may not silently replace it.

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

Attack mode should keep proof lanes and disproof lanes separate. A positive proof branch is not allowed to erase a negative obstruction; unresolved counterexample pressure must stay visible until the verifier or a human closes it.

### Decomposer

Turns promising routes into lemma-sized claims. Each claim should be small enough for a verifier to attack directly.

### Prover

Writes proofs for specific claims. The prover must mark nontrivial steps and state what external facts are being used.

### Verifier

Checks claims harshly. It should not repair the proof silently. It should return a verdict and a reason.

There are two verifier passes:

- statement drift: checks whether the proof still targets the locked statement
- whole proof: checks the mathematical argument after the drift gate

### Cartographer

Builds the map of claims, failures, examples, and dependencies. This is the long-term memory layer.

## Data Flow

```text
problem
  -> locked statement
  -> problem card
  -> exploration map
  -> fresh critic report
  -> approach queue
  -> claim graph
  -> proof attempts
  -> statement drift report
  -> verification reports
  -> attack certificate
  -> revised claim graph
  -> next actions
```

Every stage writes an artifact that a human can read.

## Non-Goals

Recurrence-Agent is not meant to be an authority. It is not a substitute for peer review, formal verification, or expert checking. It is a research notebook with active agents inside it.
