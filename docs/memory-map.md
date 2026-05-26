# Memory Map

Recurrence-Agent should preserve a research memory that can be browsed as a graph.

## Node Types

- `problem`: original statement
- `conjecture`: nearby positive or negative statement
- `example`: concrete test case
- `counterexample`: candidate obstruction
- `method`: proof technique or construction route
- `claim`: lemma-sized mathematical claim
- `proof`: proof attempt
- `verification`: verifier report
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
next_action:
```

## Why Memory Matters

For hard open problems, most value comes from the search process. A clean memory map prevents the agent from repeating failed routes and helps a human see where the real mathematical pressure lies.
