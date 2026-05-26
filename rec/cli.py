from __future__ import annotations

import argparse
from pathlib import Path

from .pipeline import run_pipeline, run_verifier_only


def main() -> int:
    parser = argparse.ArgumentParser(prog="rec", description="Recurrence-Agent CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run explore/prove/verify workflow")
    run_parser.add_argument("problem", type=Path, help="Markdown or LaTeX problem file")
    run_parser.add_argument("--out", type=Path, default=Path("runs/latest"), help="Output directory")
    run_parser.add_argument("--config", type=Path, default=Path("config.yaml"), help="YAML config")
    run_parser.add_argument("--mode", choices=["explore", "attack"], default=None, help="Override mode")
    run_parser.add_argument("--dry-run", action="store_true", help="Write artifacts without calling model CLIs")

    verify_parser = subparsers.add_parser("verify", help="Verify an existing proof")
    verify_parser.add_argument("problem", type=Path, help="Problem file")
    verify_parser.add_argument("proof", type=Path, help="Proof file")
    verify_parser.add_argument("--out", type=Path, default=Path("runs/verify-latest"), help="Output directory")
    verify_parser.add_argument("--config", type=Path, default=Path("config.yaml"), help="YAML config")
    verify_parser.add_argument("--dry-run", action="store_true", help="Write artifacts without calling model CLIs")

    args = parser.parse_args()
    if args.command == "run":
        run_pipeline(args.problem, args.out, args.config, mode_override=args.mode, dry_run=args.dry_run)
        return 0
    if args.command == "verify":
        run_verifier_only(args.problem, args.proof, args.out, args.config, dry_run=args.dry_run)
        return 0
    return 2
