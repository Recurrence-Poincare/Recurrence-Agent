# Attack Certificate

## Locked Statement

See `locked-statement.md`.

## Success Tier

`T1_proved_and_verified`

## Statement Drift Gate

Verdict: `NO_DRIFT`

## Whole-Proof Verification Gate

Verdict: `PASS`

## Proof Routes Tried

| id | method | target lemma | status | next test |
| --- | --- | --- | --- | --- |
| M1 | factorization | `n(n+1)` is even | passed | none |
| M2 | factorization | `n(n-1)` is even | passed | none |

## Disproof Routes Tried

| id | construction | intended failure | status | next test |
| --- | --- | --- | --- | --- |
| C1 | small integer tests | odd value of `n^2+n` | not refuted | none |
| C2 | small integer tests | odd value of `n^2-n` | not refuted | none |
| C3 | `n=0` | nearby false statement | refuted nearby statement | keep as drift warning |

## Failed Routes

The nearby claim `n^2+1 is even` fails at `n=0` and should not be substituted for the locked targets.

## Next Target

No next mathematical target is needed for the toy example. In a real cluster, this section should name the next lemma, computation, example, or literature check.
