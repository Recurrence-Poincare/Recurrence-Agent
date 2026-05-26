# REC Components

This document names the public components that make up the initial REC runner.

## Python Package

`rec/` contains the command-line runner.

- `rec/cli.py`: argument parsing
- `rec/config.py`: YAML config loading and defaults
- `rec/model_runner.py`: CLI provider invocation
- `rec/pipeline.py`: locked statement, explore, fresh critic, prove, drift verify, whole-proof verify, and artifact writing

The package is runnable with:

```bash
python3 -m rec run examples/problem-template.md --out runs/example
python3 -m rec verify problem.md proof.md --out runs/verify
```

## Prompts

`prompts/` contains role prompts.

- `explorer.md`: produces the neighborhood map and route queue
- `prover.md`: writes a proof attempt without changing the target
- `verifier.md`: checks the proof harshly and returns a conservative verdict
- `attack-critic.md`: fresh-context audit for drift, missing methods, and unresolved counterexample pressure
- `statement-drift-verifier.md`: checks whether a proof attempt still targets the locked statement

## Configuration

`config.yaml` assigns each role to a provider CLI.

Default:

- explorer: Codex, GPT-5.5, extra-high reasoning
- prover: Codex, GPT-5.5, extra-high reasoning
- verifier: Gemini
- critic: Gemini

The verifier may also be set to GPT/Codex by changing `roles.verifier.provider`.

## Attack Artifacts

Attack-mode runs write:

- `locked-statement.md`
- `fresh-critic-report.md`
- `statement-drift-report.md`
- `verification-report.md`
- `attack-certificate.md`
- JSONL memory channels for method, counterexample, theorem, failure, critic, and verifier records

## Shell Wrappers

- `run_rec.sh`: full workflow
- `run_verifier.sh`: proof-only verification

The CLI is the recommended execution path. A desktop wrapper can call the same commands later.
