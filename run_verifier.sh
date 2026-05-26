#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "usage: ./run_verifier.sh problem.md proof.md [out] [config]" >&2
  exit 2
fi

problem="$1"
proof="$2"
out="${3:-runs/verify-latest}"
config="${4:-config.yaml}"

python3 -m rec verify "$problem" "$proof" --out "$out" --config "$config"
