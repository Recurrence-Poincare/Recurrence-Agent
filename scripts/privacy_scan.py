from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    "runs",
    "memory",
    "problem",
}
TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".yaml",
    ".yml",
    ".toml",
    ".txt",
    ".json",
    ".jsonl",
    ".sh",
}

PRIVATE_TERMS = [
    "Original Upstream",
    "Chenyang",
    "Qih" + "ao",
    "Minghao",
    "Jiayun",
    "Q" + "ED",
    "lijungeometry",
    "ar_jl865495",
    "OneDrive-Personal",
]


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_dir() or should_skip(path):
            continue
        if path.relative_to(ROOT) == Path("scripts/privacy_scan.py"):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"README.md"}:
            files.append(path)
    return files


def main() -> int:
    findings: list[str] = []
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for term in PRIVATE_TERMS:
            if term in text:
                findings.append(f"{path.relative_to(ROOT)}: contains blocked term {term!r}")

    if findings:
        print("Privacy scan failed:", file=sys.stderr)
        for finding in findings:
            print(f"- {finding}", file=sys.stderr)
        return 1

    print("Privacy scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
