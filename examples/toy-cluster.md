# Toy Cluster

This is a deliberately elementary example for testing REC artifacts. It is not a research claim.

## Target A

For every integer `n`, the number `n^2 + n` is even.

## Target B

For every integer `n`, the number `n^2 - n` is even.

## Nearby False Statement

For every integer `n`, the number `n^2 + 1` is even.

## Desired Mode

attack

## Constraints

- Preserve the quantifier "for every integer".
- Try both parity proof routes and counterexample routes.
- Record the nearby false statement as a warning, not as a target replacement.

## Output Preference

Produce a locked statement, route matrix, proof-side route, disproof-side pressure, drift check, verifier report, and attack certificate.
