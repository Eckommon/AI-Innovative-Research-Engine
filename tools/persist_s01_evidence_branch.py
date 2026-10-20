#!/usr/bin/env python3
"""Publish only vetted S01 operational evidence to a unique per-run Git ref.

Never pushes directly to main or downloads original source data. Source-science
gates belong to the caller; this is a persistence boundary, not qualification.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REPO = "Eckommon/AI-Innovative-Research-Engine"
QUAL = re.compile(r"[A-Z][A-Z0-9-]{2,63}\Z")
RUN = re.compile(r"[1-9][0-9]{4,19}\Z")
SAFE_FILE = re.compile(r"[a-z0-9][a-z0-9-]{1,70}\.(json|md)\Z")
MAX_RECEIPT_BYTES = 256 * 1024

def branch_ref(qualification, run_id):
    if not QUAL.fullmatch(qualification) or not RUN.fullmatch(str(run_id)):
        raise ValueError("qualification and numeric GitHub Actions run ID required")
    return f"refs/heads/evidence/s01/{qualification.lower()}/{run_id}"

def validate_receipts(root, qualification, json_name, md_name):
    if not QUAL.fullmatch(qualification):
        raise ValueError("invalid qualification ID")
    if not SAFE_FILE.fullmatch(json_name) or not json_name.endswith(".json"):
        raise ValueError("unsafe JSON receipt name")
    if not SAFE_FILE.fullmatch(md_name) or not md_name.endswith(".md"):
        raise ValueError("unsafe Markdown receipt name")
    if json_name[:-5] != md_name[:-3]:
        raise ValueError("receipt basename mismatch")
    sub=Path("research/SOURCE-REGISTRY-S01/qualifications") / qualification / "evidence"
    paths=(sub/json_name,sub/md_name)
    for rel in paths:
        full=root/rel
        if (not full.is_file() or full.is_symlink()
            or not full.resolve().is_relative_to(root.resolve())
            or full.stat().st_size>MAX_RECEIPT_BYTES or full.stat().st_size==0):
            raise ValueError("invalid, symlinked, missing, or oversized evidence file")
        full.read_text(encoding="utf-8", errors="strict")
    payload=json.loads((root/paths[0]).read_text(encoding="utf-8"))
    for field,expected in {
        "incremental_monetary_cost_usd":0,
        "science_f01_authorized":False,
        "source_case_rows_emitted":False,
        "future_outcome_values_emitted":False,
        "individual_identifiers_emitted":False,
    }.items():
        if type(payload.get(field)) is not type(expected) or payload.get(field) != expected:
            raise ValueError("source-only evidence envelope missing: "+field)
    if payload.get("qualification") != qualification:
        raise ValueError("qualification source/evidence ID mismatch")
    return paths

def command(argv, *, check=True):
    return subprocess.run(argv, cwd=ROOT, check=check, capture_output=True, text=True)

def publish(qualification, run_id, json_name, md_name, *, root=ROOT, runner=command):
    ref=branch_ref(qualification,run_id)
    paths=validate_receipts(root,qualification,json_name,md_name)
    if os.environ.get("GITHUB_REPOSITORY") != REPO or os.environ.get("GITHUB_RUN_ID") != str(run_id):
        raise RuntimeError("untrusted noncanonical CI environment")
    listed=runner(["git","ls-remote","--exit-code","--heads","origin",ref],check=False)
    if listed.returncode==0:
        raise RuntimeError("immutable per-run evidence ref already exists; refuse overwrite")
    if listed.returncode!=2:
        raise RuntimeError("remote ref existence could not be safely adjudicated")
    runner(["git","config","user.name","github-actions[bot]"])
    runner(["git","config","user.email","41898282+github-actions[bot]@users.noreply.github.com"])
    runner(["git","add","--",*(str(p) for p in paths)])
    runner(["git","commit","-m",f"Preserve immutable {qualification} original-run evidence {run_id}"])
    # Never force. Ref is unique per run and independent from a moving main.
    runner(["git","push","origin",f"HEAD:{ref}"])
    return {"qualified_research":qualification,"github_run_id":str(run_id),
            "remote_evidence_ref":ref,"main_branch_direct_write":False}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--qualification",required=True)
    p.add_argument("--run-id",required=True)
    p.add_argument("--json",required=True)
    p.add_argument("--md",required=True)
    p.add_argument("--publish",action="store_true")
    args=p.parse_args()
    ref=branch_ref(args.qualification,args.run_id)
    validate_receipts(ROOT,args.qualification,args.json,args.md)
    if not args.publish:
        print(json.dumps({"offline_verified":True,"proposed_branch":ref,"network_or_git_mutation":False}))
        return
    print(json.dumps(publish(args.qualification,args.run_id,args.json,args.md),sort_keys=True))

if __name__=="__main__":
    main()
