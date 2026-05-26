from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


DEFAULT_CONFIG: dict[str, Any] = {
    "mode": "attack",
    "roles": {
        "explorer": {"provider": "codex", "model": "gpt-5.5", "reasoning_effort": "extra-high"},
        "prover": {"provider": "codex", "model": "gpt-5.5", "reasoning_effort": "extra-high"},
        "verifier": {"provider": "gemini", "model": "gemini-3.1-pro-preview", "reasoning_effort": "high"},
    },
    "run": {"timeout_seconds": 3600, "write_prompt_files": True},
    "providers": {
        "codex": {
            "command": 'codex -m "{model}" exec --reasoning-effort "{reasoning_effort}" "$(cat "{prompt_file}")"'
        },
        "claude": {"command": 'claude -p --model "{model}" "$(cat "{prompt_file}")"'},
        "gemini": {"command": 'gemini -m "{model}" -p "$(cat "{prompt_file}")"'},
    },
}


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    result = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def load_config(path: Path) -> dict[str, Any]:
    if not path.exists():
        return DEFAULT_CONFIG
    loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(loaded, dict):
        raise ValueError(f"Config must be a YAML mapping: {path}")
    return deep_merge(DEFAULT_CONFIG, loaded)
