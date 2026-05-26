# Memory Map

Recurrence-Agent should preserve a research memory that can be browsed as a graph.

## Node Types

- `problem`: original statement
- `locked-statement`: frozen target statement for a run
- `conjecture`: nearby positive or negative statement
- `example`: concrete test case
- `counterexample`: candidate obstruction
- `method`: proof technique or construction route
- `claim`: lemma-sized mathematical claim
- `proof`: proof attempt
- `drift-check`: statement preservation audit
- `verification`: verifier report
- `critic`: fresh-context critique
- `failure`: failed route with reason
- `next-action`: specific follow-up task

## Edge Types

- `supports`
- `contradicts`
- `depends-on`
- `generalizes`
- `specializes`
- `blocks`
- `repairs`
- `returns-to`

The `returns-to` edge is central. It records how an exploratory branch connects back to the original conjecture.

## JSONL Channels

The runner creates machine-readable channels in each run directory:

- `method-matrix.jsonl`
- `toy-models.jsonl`
- `counterexample-attempts.jsonl`
- `retrieved-theorems.jsonl`
- `decomposition-plans.jsonl`
- `direct-attempts.jsonl`
- `recursive-attempts.jsonl`
- `key-failures.jsonl`
- `statement-repairs.jsonl`
- `return-map.jsonl`
- `critic-reports.jsonl`
- `verifier-reports.jsonl`

Markdown files are for human reading. JSONL channels are the source of truth for later maps, dashboards, or Obsidian exports.

## Minimal Claim Record

```yaml
id:
statement:
source_branch:
depends_on:
proof_attempt:
verifier:
verdict:
reason:
drift_verdict:
next_action:
```

## Why Memory Matters

For hard open problems, most value comes from the search process. A clean memory map prevents the agent from repeating failed routes and helps a human see where the real mathematical pressure lies.
