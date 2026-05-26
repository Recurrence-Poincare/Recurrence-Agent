from __future__ import annotations

import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class ModelResult:
    role: str
    provider: str
    model: str
    command: str
    elapsed_seconds: float
    returncode: int
    stdout: str
    stderr: str


def render_command(template: str, role_config: dict[str, Any], prompt_file: Path) -> str:
    values = {
        "model": role_config.get("model", ""),
        "reasoning_effort": role_config.get("reasoning_effort", ""),
        "prompt_file": str(prompt_file),
    }
    return template.format(**values)


def run_model(
    role: str,
    prompt: str,
    config: dict[str, Any],
    out_dir: Path,
    dry_run: bool = False,
    result_role: str | None = None,
) -> ModelResult:
    roles = config.get("roles", {})
    role_config = roles.get(role)
    if not role_config:
        raise KeyError(f"Missing role config: {role}")

    provider = role_config.get("provider")
    providers = config.get("providers", {})
    provider_config = providers.get(provider)
    if not provider_config:
        raise KeyError(f"Missing provider config: {provider}")

    model = str(role_config.get("model", ""))
    timeout = int(config.get("run", {}).get("timeout_seconds", 3600))
    prompt_dir = out_dir / "prompts"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    result_role = result_role or role
    prompt_file = prompt_dir / f"{result_role}.prompt.md"
    prompt_file.write_text(prompt, encoding="utf-8")

    command = render_command(str(provider_config["command"]), role_config, prompt_file.resolve())

    if dry_run:
        stdout = f"# Dry-run {result_role}\n\nProvider: {provider}\nModel: {model}\n\nNo model CLI was called."
        return ModelResult(result_role, provider, model, command, 0.0, 0, stdout, "")

    started = time.monotonic()
    completed = subprocess.run(
        command,
        shell=True,
        cwd=out_dir,
        text=True,
        capture_output=True,
        timeout=timeout,
    )
    elapsed = time.monotonic() - started
    return ModelResult(
        role=result_role,
        provider=provider,
        model=model,
        command=command,
        elapsed_seconds=elapsed,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )
