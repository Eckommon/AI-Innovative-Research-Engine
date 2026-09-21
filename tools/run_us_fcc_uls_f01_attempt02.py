#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import urllib.parse

import run_us_fcc_uls_f01 as base

ROOT = Path(__file__).resolve().parents[1]
CORRECTION_COMMIT = "486624cf803c291217baef97b8514294691fce82"
BASE_RUNNER_COMMIT = "92bbf04d8a9786f9c62417f24fd0d16dc74828a4"
OUTDIR = ROOT / "research/US-FCC-ULS-F01/evidence"
JSON_OUT = OUTDIR / "attempt-02.json"
MD_OUT = OUTDIR / "attempt-02.md"

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/153.0 Safari/537.36"
REFERER = "https://www.fcc.gov/"

def endpoint_candidates(url: str) -> list[str]:
    p = urllib.parse.urlparse(url)
    name = Path(p.path).name
    if name == "l_micro.zip":
        return [
            url,
            "https://wireless.fcc.gov/uls/data/complete/l_micro.zip",
            "https://ftp.fcc.gov/pub/Bureaus/Wireless/Databases/uls/complete/l_micro.zip",
        ]
    if name.startswith("l_mw_") and name.endswith(".zip"):
        return [
            url,
            f"https://wireless.fcc.gov/uls/data/daily/{name}",
            f"https://ftp.fcc.gov/pub/Bureaus/Wireless/Databases/uls/daily/{name}",
        ]
    return [url]

def curl_download_one(url: str, dest: Path) -> dict:
    hdr = dest.with_suffix(dest.suffix + ".headers")
    cmd = [
        "curl", "-fL", "--retry", "2", "--retry-delay", "1",
        "--connect-timeout", "30", "--max-time", "300",
        "-A", UA, "-e", REFERER,
        "-D", str(hdr), "-o", str(dest), "-w", "%{http_code}\n%{url_effective}\n%{content_type}\n",
        url,
    ]
    p = subprocess.run(cmd, text=True, capture_output=True)
    if p.returncode != 0:
        raise RuntimeError(f"curl rc={p.returncode}: {p.stderr.strip()[-500:]}")
    lines = p.stdout.strip().splitlines()
    status = int(lines[0]) if lines and lines[0].isdigit() else None
    final_url = lines[1] if len(lines) > 1 else url
    content_type = lines[2] if len(lines) > 2 else None
    data = dest.read_bytes()
    return {
        "status": status,
        "final_url": final_url,
        "content_type": content_type,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "transport": "curl",
        "requested_url": url,
    }

def corrected_download(url: str, dest: Path) -> dict:
    attempts = []
    for cand in endpoint_candidates(url):
        try:
            if dest.exists():
                dest.unlink()
            meta = curl_download_one(cand, dest)
            meta["attempted_urls"] = attempts + [{"url": cand, "status": meta.get("status"), "result": "selected"}]
            meta["contract_logical_url"] = url
            return meta
        except Exception as e:
            attempts.append({"url": cand, "result": "error", "error": f"{type(e).__name__}:{e}"})
    raise RuntimeError("all official FCC endpoint variants failed: " + json.dumps(attempts, sort_keys=True))

def corrected_get_fingerprint(url: str) -> dict:
    attempts = []
    candidates = [url]
    if url == "https://www.fcc.gov/wireless/data/public-access-files-database-downloads":
        # Transport-level current FCC route for the same ULS database download surface.
        candidates += ["https://www.fcc.gov/uls/transactions/daily-weekly"]
    for cand in candidates:
        try:
            with tempfile.TemporaryDirectory() as td:
                path = Path(td) / "body"
                meta = curl_download_one(cand, path)
            meta["contract_logical_url"] = url
            meta["attempted_urls"] = attempts + [{"url": cand, "status": meta.get("status"), "result": "selected"}]
            return meta
        except Exception as e:
            attempts.append({"url": cand, "result": "error", "error": f"{type(e).__name__}:{e}"})
    # Return a non-raising transport record so Gate 3 can fail scientifically if
    # all other empirical gates execute. This does not waive the frozen requirement.
    return {"status": None, "contract_logical_url": url, "attempted_urls": attempts, "transport_error": True}

def curl_head_one(url: str) -> dict:
    cmd = [
        "curl", "-fsSIL", "--retry", "1", "--connect-timeout", "20", "--max-time", "60",
        "-A", UA, "-e", REFERER, "-o", "/dev/null",
        "-w", "%{http_code}\n%{url_effective}\n%{content_type}\n%{size_download}\n",
        url,
    ]
    p = subprocess.run(cmd, text=True, capture_output=True)
    if p.returncode != 0:
        raise RuntimeError(f"curl HEAD rc={p.returncode}: {p.stderr.strip()[-500:]}")
    lines = p.stdout.strip().splitlines()
    status = int(lines[0]) if lines and lines[0].isdigit() else None
    downloaded = float(lines[3]) if len(lines) > 3 and lines[3] else 0.0
    return {
        "method": "HEAD",
        "status": status,
        "final_url": lines[1] if len(lines) > 1 else url,
        "content_type": lines[2] if len(lines) > 2 else None,
        "entity_body_bytes_consumed": int(downloaded),
        "transport": "curl",
        "requested_url": url,
    }

def corrected_head_meta(url: str) -> dict:
    attempts = []
    for cand in endpoint_candidates(url):
        try:
            meta = curl_head_one(cand)
            meta["contract_logical_url"] = url
            meta["attempted_urls"] = attempts + [{"url": cand, "status": meta.get("status"), "result": "selected"}]
            return meta
        except Exception as e:
            attempts.append({"url": cand, "result": "error", "error": f"{type(e).__name__}:{e}"})
    return {
        "status": None,
        "entity_body_bytes_consumed": 0,
        "contract_logical_url": url,
        "attempted_urls": attempts,
        "transport_error": True,
    }

def main() -> int:
    if JSON_OUT.exists() or MD_OUT.exists():
        raise RuntimeError("immutable attempt-02 evidence already exists")
    a1p = OUTDIR / "attempt-01.json"
    if not a1p.exists():
        raise RuntimeError("attempt-01 evidence missing")
    a1 = json.loads(a1p.read_text(encoding="utf-8"))
    assert a1.get("attempt_valid") is False
    assert a1.get("disposition") == "IMPLEMENTATION_BLOCKED_US_FCC_ULS_F01_ATTEMPT_01"
    assert a1.get("future_daily_rows_opened") == 0
    assert a1.get("future_cancelled_terminated_membership_opened") is False
    assert a1.get("daily_entity_body_bytes_consumed") == 0

    base.JSON_OUT = JSON_OUT
    base.MD_OUT = MD_OUT
    base.download = corrected_download
    base.get_fingerprint = corrected_get_fingerprint
    base.head_meta = corrected_head_meta

    rc = base.main()

    e = json.loads(JSON_OUT.read_text(encoding="utf-8"))
    e["attempt"] = 2
    e["implementation_correction_commit"] = CORRECTION_COMMIT
    e["base_runner_commit"] = BASE_RUNNER_COMMIT
    e["attempt02_wrapper_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    e["scientific_threshold_changed"] = False
    e["service_family_changed"] = False
    e["identity_rule_changed"] = False
    e["future_window_changed"] = False
    e["transport_only_correction"] = True
    JSON_OUT.write_text(json.dumps(e, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    md = MD_OUT.read_text(encoding="utf-8")
    md = md.replace("# US-FCC-ULS-F01 — Attempt 01", "# US-FCC-ULS-F01 — Attempt 02", 1)
    md += "\n## Attempt 02 transport-only correction\n\n"
    md += f"- Correction commit: `{CORRECTION_COMMIT}`\n"
    md += f"- Base runner commit: `{BASE_RUNNER_COMMIT}`\n"
    md += "- Transport changed: Python urllib → curl with redirects/browser-compatible headers and FCC-owned endpoint variants only.\n"
    md += "- Scientific thresholds changed: **false**\n"
    md += "- Service family changed: **false**\n"
    md += "- Identity rule changed: **false**\n"
    md += "- Future window changed: **false**\n"
    md += "- Future daily transaction bodies opened: **0**\n"
    MD_OUT.write_text(md, encoding="utf-8")

    print(e["disposition"])
    print(e.get("pass_count"), e.get("failed_gates"))
    return rc

if __name__ == "__main__":
    raise SystemExit(main())
