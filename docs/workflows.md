# Workflows

## Explore Workflow

Use explore mode when the problem is broad, risky, or possibly misstated.

Required outputs:

- problem card
- positive conjecture list
- negative conjecture list
- example and counterexample candidates
- approach queue
- failure ledger
- return-to-conjecture map

Stopping rule:

Explore mode should stop when it has produced a small number of concrete branches worth attacking, or when it can explain why the statement is currently too ambiguous.

## Attack Workflow

Use attack mode when a human wants direct pressure on a specific conjecture.

Required outputs:

- locked statement
- method matrix
- proof-route log
- counterexample-route log
- fresh-context critic report
- statement-drift report
- bottleneck lemma list
- verification targets
- attack certificate
- next actions

Required loop:

```text
lock statement
  -> generate proof-side and disproof-side plans
  -> run fresh-context critic
  -> attempt selected proof route
  -> run statement-drift verifier
  -> run whole-proof verifier
  -> assign success tier
  -> write next actions
```

Stopping rule:

Attack mode should stop when every high-priority proof and disproof route has either produced a checkable claim, failed with a reason, or requires external input.

## Verification Workflow

Verification is separate from generation.

For each claim, the verifier receives:

- original problem
- claim statement
- proof attempt
- cited facts or references
- local context from the claim graph

The verifier returns:

```text
verdict: PASS | FIXABLE | FAIL | UNCERTAIN
reason:
missing hypotheses:
logical gaps:
counterexample risks:
repair suggestions:
```

The verifier should be conservative. `UNCERTAIN` is better than a false pass.

The verifier should return `FAIL` when the candidate proves a changed theorem. A separate drift report should be read before the whole-proof report.

## Human Review Workflow

Human review should focus on:

- whether the original conjecture was preserved
- whether the strongest branches were tried
- whether failures are informative
- whether verifier objections are real
- whether the next-actions list is specific enough
