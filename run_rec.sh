#!/usr/bin/env bash
set -euo pipefail

problem="${1:-examples/problem-template.md}"
out="${2:-runs/latest}"
config="${3:-config.yaml}"

python3 -m rec run "$problem" --out "$out" --config "$config"
