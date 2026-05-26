# Publication Checklist

Before public code or generated artifacts are added to this repository, run these checks.

## Identity Scan

Reject the publish candidate if it contains:

- personal names or emails not intended for publication
- local filesystem paths
- private account names
- old repository URLs
- hidden metadata that identifies a private workspace

Run:

```bash
python scripts/privacy_scan.py
```

## Lineage Scan

Reject the publish candidate if it contains copied code, copied documentation, inherited license text, or upstream project branding that is not intended to appear in this repository.

Do not publish old project names, old author blocks, or upstream paper sections unless they are intentionally cited in a references section.

## Artifact Scan

Reject the publish candidate if it contains:

- run logs with private prompts
- model transcripts not intended for release
- API keys or tokens
- problem PDFs without permission
- cached web pages
- generated proof claims that are not clearly labeled as unverified

## Git History Scan

The public branch should have clean history. Do not publish a branch that previously contained private or unwanted material.

Recommended command pattern:

```bash
git log --all --stat
git grep -n "SEARCH_TERM"
```

Also scan the working tree with a fast text search tool before pushing.

## Mathematical Claims

Do not present a proof as solved unless it has passed independent verification. Prefer labels such as:

- exploratory
- conjectural
- unverified
- verifier-passed
- human-reviewed

For attack-mode output, distinguish three different claims:

- the original theorem or conjecture
- a proposed proof or counterexample
- the structural honesty of an attack certificate

A verified attack certificate is not a verified proof of the original theorem.

## Release Rule

If in doubt, keep the artifact private.

## Required Local Checks

Before pushing code changes, run:

```bash
python -m compileall rec
python -m unittest discover -s tests
python -m rec run examples/problem-template.md --out runs/dry-run --dry-run
python scripts/privacy_scan.py
```
