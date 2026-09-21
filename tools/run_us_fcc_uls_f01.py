#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
import csv
import hashlib
import io
import json
import os
import re
import tempfile
import time
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_SHA = "287f0e3dfe203beee3d9ca1f21e67e51ef2db6a5"
ISSUE = 166
BASELINE_URL = "https://data.fcc.gov/download/pub/uls/complete/l_micro.zip"
DAILY_URLS = [
    "https://data.fcc.gov/download/pub/uls/daily/l_mw_mon.zip",
    "https://data.fcc.gov/download/pub/uls/daily/l_mw_tue.zip",
    "https://data.fcc.gov/download/pub/uls/daily/l_mw_wed.zip",
    "https://data.fcc.gov/download/pub/uls/daily/l_mw_thu.zip",
    "https://data.fcc.gov/download/pub/uls/daily/l_mw_fri.zip",
]
DOC_URLS = [
    "https://wireless.fcc.gov/uls/documentation/pa_intro24.pdf",
    "https://wireless.fcc.gov/wtbfiles/pa_ddef51.pdf",
    "https://wireless.fcc.gov/uls/releases/d992205c.pdf",
    "https://www.fcc.gov/wireless/data/public-access-files-database-downloads",
]
UA = "Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)"
OUTDIR = ROOT / "research/US-FCC-ULS-F01/evidence"
JSON_OUT = OUTDIR / "attempt-01.json"
MD_OUT = OUTDIR / "attempt-01.md"

def req(url: str, method: str = "GET", timeout: int = 120):
    request = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
    last = None
    for i in range(3):
        try:
            return urllib.request.urlopen(request, timeout=timeout)
        except Exception as e:
            last = e
            if i < 2:
                time.sleep(2 ** i)
    raise last

def get_fingerprint(url: str) -> dict:
    with req(url, "GET", 120) as r:
        h = hashlib.sha256()
        n = 0
        while True:
            chunk = r.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
            n += len(chunk)
        return {
            "status": getattr(r, "status", None),
            "final_url": r.geturl(),
            "content_type": r.headers.get("Content-Type"),
            "content_length_header": r.headers.get("Content-Length"),
            "last_modified": r.headers.get("Last-Modified"),
            "bytes": n,
            "sha256": h.hexdigest(),
        }

def head_meta(url: str) -> dict:
    errs = []
    for method in ("HEAD", "OPTIONS"):
        try:
            r = req(url, method, 60)
            try:
                return {
                    "method": method,
                    "status": getattr(r, "status", None),
                    "final_url": r.geturl(),
                    "content_type": r.headers.get("Content-Type"),
                    "content_length": r.headers.get("Content-Length"),
                    "last_modified": r.headers.get("Last-Modified"),
                    "etag": r.headers.get("ETag"),
                    "entity_body_bytes_consumed": 0,
                }
            finally:
                r.close()
        except Exception as e:
            errs.append(f"{method}:{type(e).__name__}:{e}")
    return {"status": None, "entity_body_bytes_consumed": 0, "errors": errs}

def download(url: str, dest: Path) -> dict:
    h = hashlib.sha256()
    n = 0
    with req(url, "GET", 300) as r, dest.open("wb") as f:
        while True:
            chunk = r.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
            f.write(chunk)
            n += len(chunk)
        return {
            "status": getattr(r, "status", None),
            "final_url": r.geturl(),
            "content_type": r.headers.get("Content-Type"),
            "content_length_header": r.headers.get("Content-Length"),
            "last_modified": r.headers.get("Last-Modified"),
            "etag": r.headers.get("ETag"),
            "bytes": n,
            "sha256": h.hexdigest(),
        }

def valid_id(v: str) -> str | None:
    s = (v or "").strip()
    return s if re.fullmatch(r"\d{9}", s) else None

def parse_date(v: str):
    s = (v or "").strip()
    if not s:
        return None
    for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%Y%m%d"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    return None

def zip_member(names: list[str], target: str) -> str | None:
    target = target.lower()
    for n in names:
        if Path(n).name.lower() == target:
            return n
    return None

def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists():
        raise RuntimeError("immutable attempt-01 evidence already exists")

    evidence = {
        "research": "US-FCC-ULS-F01",
        "attempt": 1,
        "contract_sha": CONTRACT_SHA,
        "issue": ISSUE,
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "incremental_monetary_cost_usd": 0,
        "future_daily_rows_opened": 0,
        "future_cancelled_terminated_membership_opened": False,
        "future_relationship_computed": False,
        "predictive_metric_computed": False,
        "ranking_computed": False,
        "causal_claim_made": False,
        "name_address_call_sign_only_fuzzy_geo_manual_identity_repair_used": False,
        "daily_entity_body_bytes_consumed": 0,
        "gates": [],
    }
    evidence["runner_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    try:
        cp = json.loads((ROOT / "context/checkpoint.json").read_text(encoding="utf-8"))
        g1 = (
            cp.get("checkpoint_id") == "CHK-20260921-US-FCC-ULS-F01-ACTIVE"
            and cp.get("active_issue") == 166
            and cp.get("active_research") == "US-FCC-ULS-F01"
            and cp.get("last_decision") == "DEC-242"
        )
        evidence["gates"].append({"gate": 1, "pass": g1, "observed": cp})

        g2 = os.environ.get("FCC_ULS_F01_ISSUE_BOUND") == "1" and os.environ.get("FCC_ULS_F01_CONTRACT_SHA") == CONTRACT_SHA
        evidence["gates"].append({"gate": 2, "pass": g2, "observed": {"issue": ISSUE, "contract_sha": os.environ.get("FCC_ULS_F01_CONTRACT_SHA")}})

        docs = {}
        for url in DOC_URLS:
            try:
                docs[url] = get_fingerprint(url)
            except Exception as e:
                docs[url] = {"error": f"{type(e).__name__}:{e}"}
        g3 = all(d.get("status") and 200 <= int(d["status"]) < 400 and d.get("sha256") for d in docs.values())
        evidence["gates"].append({"gate": 3, "pass": g3, "observed": docs})

        contract_text = (ROOT / "research/US-FCC-ULS-F01/README.md").read_text(encoding="utf-8")
        g4 = (
            "Microwave and Microwave Broadcast Auxiliary" in contract_text
            and "l_micro.zip" in contract_text
            and all(Path(u).name in contract_text for u in DAILY_URLS)
        )
        evidence["gates"].append({"gate": 4, "pass": g4, "observed": {"family": "Microwave and Microwave Broadcast Auxiliary", "complete": "l_micro.zip", "daily": [Path(u).name for u in DAILY_URLS]}})

        with tempfile.TemporaryDirectory() as tds:
            td = Path(tds)
            zpath = td / "l_micro.zip"
            baseline_meta = download(BASELINE_URL, zpath)
            evidence["baseline"] = baseline_meta
            zip_ok = zipfile.is_zipfile(zpath)
            evidence["gates"].append({"gate": 5, "pass": bool(baseline_meta.get("status") and 200 <= int(baseline_meta["status"]) < 400 and zip_ok), "observed": {**baseline_meta, "parseable_zip": zip_ok}})

            if not zip_ok:
                raise RuntimeError("baseline archive is not a parseable ZIP")

            with zipfile.ZipFile(zpath) as z:
                names = z.namelist()
                evidence["archive_members"] = names
                hd_name = zip_member(names, "HD.dat")
                hs_name = zip_member(names, "HS.dat")
                g6 = hd_name is not None and hs_name is not None
                evidence["gates"].append({"gate": 6, "pass": g6, "observed": {"HD": hd_name, "HS": hs_name}})
                if not g6:
                    raise RuntimeError("required HD.dat/HS.dat missing")

                # Fixed official HD positions: 1=record type, 2=unique system ID, 5=call sign,
                # 6=status, 7=radio service, 8=grant, 9=expired, 10=cancellation,
                # 43=effective, 44=last action.
                hd_required_positions = {"unique_system_id":2,"call_sign":5,"license_status":6,"radio_service_code":7,"grant_date":8,"expired_date":9,"cancellation_date":10,"effective_date":43,"last_action_date":44}
                evidence["hd_schema_positions"] = hd_required_positions

                nonblank_id = valid_id_rows = 0
                all_ids = set()
                active_ids = set()
                nonblank_status = documented_status = 0
                status_counts = Counter()
                active_total = active_core_date_parseable = 0
                hd_rows = 0
                short_hd_rows = 0

                with io.TextIOWrapper(z.open(hd_name), encoding="latin-1", errors="replace", newline="") as fh:
                    reader = csv.reader(fh, delimiter="|")
                    for row in reader:
                        hd_rows += 1
                        if len(row) < 44:
                            short_hd_rows += 1
                            continue
                        raw_id = row[1].strip()
                        if raw_id:
                            nonblank_id += 1
                        sid = valid_id(raw_id)
                        if sid:
                            valid_id_rows += 1
                            all_ids.add(sid)
                        status = row[5].strip()
                        if status:
                            nonblank_status += 1
                            status_counts[status] += 1
                            if status in {"A","C","E","T"}:
                                documented_status += 1
                        if sid and status == "A":
                            active_ids.add(sid)
                            active_total += 1
                            if parse_date(row[7]) is not None or parse_date(row[42]) is not None:
                                active_core_date_parseable += 1

                g7 = hd_rows > 0 and short_hd_rows == 0
                evidence["gates"].append({"gate": 7, "pass": g7, "observed": {"rows": hd_rows, "short_rows_lt_44_fields": short_hd_rows, "positions": hd_required_positions}})

                id_rate = valid_id_rows / nonblank_id if nonblank_id else 0.0
                evidence["gates"].append({"gate": 8, "pass": id_rate >= 0.999, "observed": {"nonblank_id_rows": nonblank_id, "valid_9digit_id_rows": valid_id_rows, "rate": id_rate}})
                evidence["gates"].append({"gate": 9, "pass": len(all_ids) >= 20000, "observed": {"distinct_valid_system_ids": len(all_ids), "threshold": 20000}})
                evidence["gates"].append({"gate": 10, "pass": len(active_ids) >= 10000, "observed": {"distinct_active_system_ids": len(active_ids), "threshold": 10000}})

                status_rate = documented_status / nonblank_status if nonblank_status else 0.0
                evidence["gates"].append({"gate": 11, "pass": status_rate >= 0.999, "observed": {"nonblank_status_rows": nonblank_status, "documented_A_C_E_T_rows": documented_status, "rate": status_rate, "counts": dict(sorted(status_counts.items()))}})

                date_rate = active_core_date_parseable / active_total if active_total else 0.0
                evidence["gates"].append({"gate": 12, "pass": date_rate >= 0.99, "observed": {"active_rows": active_total, "grant_or_effective_parseable": active_core_date_parseable, "rate": date_rate}})

                hs_linked_rows = hs_good_rows = 0
                active_with_hs = set()
                hs_rows = 0
                short_hs_rows = 0
                with io.TextIOWrapper(z.open(hs_name), encoding="latin-1", errors="replace", newline="") as fh:
                    reader = csv.reader(fh, delimiter="|")
                    for row in reader:
                        hs_rows += 1
                        if len(row) < 6:
                            short_hs_rows += 1
                            continue
                        sid = valid_id(row[1])
                        if sid and sid in active_ids:
                            active_with_hs.add(sid)
                            hs_linked_rows += 1
                            if row[5].strip() and parse_date(row[4]) is not None:
                                hs_good_rows += 1

                hs_id_rate = len(active_with_hs) / len(active_ids) if active_ids else 0.0
                evidence["gates"].append({"gate": 13, "pass": hs_id_rate >= 0.90, "observed": {"active_ids": len(active_ids), "active_ids_with_hs": len(active_with_hs), "rate": hs_id_rate, "hs_rows": hs_rows, "short_hs_rows_lt_6_fields": short_hs_rows}})
                hs_struct_rate = hs_good_rows / hs_linked_rows if hs_linked_rows else 0.0
                evidence["gates"].append({"gate": 14, "pass": hs_struct_rate >= 0.90, "observed": {"linked_hs_rows": hs_linked_rows, "code_and_date_valid_rows": hs_good_rows, "rate": hs_struct_rate}})

                candidates = ["MW.dat","LO.dat","AN.dat","FR.dat","FC.dat","CP.dat"]
                joinable = {}
                lower_map = {Path(n).name.lower(): n for n in names}
                for target in candidates:
                    actual = lower_map.get(target.lower())
                    if not actual:
                        continue
                    scanned = overlap = valid = 0
                    with io.TextIOWrapper(z.open(actual), encoding="latin-1", errors="replace", newline="") as fh:
                        reader = csv.reader(fh, delimiter="|")
                        for row in reader:
                            if len(row) < 2:
                                continue
                            scanned += 1
                            sid = valid_id(row[1])
                            if sid:
                                valid += 1
                                if sid in all_ids:
                                    overlap += 1
                            if scanned >= 200000:
                                break
                    joinable[target] = {"member": actual, "scanned_rows_cap": scanned, "valid_id_rows": valid, "overlap_hd_ids": overlap, "joinable": overlap > 0}
                g15 = sum(1 for x in joinable.values() if x["joinable"]) >= 2
                evidence["gates"].append({"gate": 15, "pass": g15, "observed": joinable})

        daily_meta = {u: head_meta(u) for u in DAILY_URLS}
        evidence["daily_metadata"] = daily_meta
        evidence["daily_entity_body_bytes_consumed"] = sum(int(m.get("entity_body_bytes_consumed",0)) for m in daily_meta.values())
        g16 = any(m.get("status") and 200 <= int(m["status"]) < 400 and m.get("entity_body_bytes_consumed") == 0 for m in daily_meta.values())
        evidence["gates"].append({"gate": 16, "pass": g16, "observed": daily_meta})

        g17 = (
            evidence["future_daily_rows_opened"] == 0
            and evidence["future_cancelled_terminated_membership_opened"] is False
            and evidence["future_relationship_computed"] is False
            and evidence["predictive_metric_computed"] is False
            and evidence["ranking_computed"] is False
            and evidence["causal_claim_made"] is False
            and evidence["name_address_call_sign_only_fuzzy_geo_manual_identity_repair_used"] is False
            and evidence["daily_entity_body_bytes_consumed"] == 0
        )
        evidence["gates"].append({"gate": 17, "pass": g17, "observed": {k:evidence[k] for k in [
            "future_daily_rows_opened","future_cancelled_terminated_membership_opened","future_relationship_computed",
            "predictive_metric_computed","ranking_computed","causal_claim_made",
            "name_address_call_sign_only_fuzzy_geo_manual_identity_repair_used","daily_entity_body_bytes_consumed"
        ]}})

        g18 = (
            re.fullmatch(r"[0-9a-f]{64}", evidence["baseline"]["sha256"] or "") is not None
            and re.fullmatch(r"[0-9a-f]{64}", evidence["runner_sha256"] or "") is not None
            and evidence["incremental_monetary_cost_usd"] == 0
        )
        evidence["gates"].append({"gate": 18, "pass": g18, "observed": {"baseline_sha256": evidence["baseline"]["sha256"], "runner_sha256": evidence["runner_sha256"], "contract_sha": CONTRACT_SHA, "cost_usd": 0}})

        failed = [g["gate"] for g in evidence["gates"] if not g["pass"]]
        evidence["attempt_valid"] = True
        evidence["pass_count"] = 18 - len(failed)
        evidence["failed_gates"] = failed
        evidence["disposition"] = (
            "PASS_US_FCC_ULS_F01_MICROWAVE_EXACT_SYSTEM_ID_FUTURE_EVENT_DESIGN_READY"
            if not failed else
            "HOLD_US_FCC_ULS_F01_MICROWAVE_EXACT_SYSTEM_ID_FUTURE_EVENT_DESIGN_NOT_READY"
        )
    except Exception as e:
        evidence["attempt_valid"] = False
        evidence["implementation_error"] = {"type": type(e).__name__, "message": str(e)}
        evidence["pass_count"] = sum(1 for g in evidence["gates"] if g.get("pass"))
        evidence["failed_gates"] = []
        evidence["disposition"] = "IMPLEMENTATION_BLOCKED_US_FCC_ULS_F01_ATTEMPT_01"

    JSON_OUT.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "# US-FCC-ULS-F01 — Attempt 01","",
        f"**Disposition:** `{evidence['disposition']}`","",
        f"- Attempt valid: `{evidence.get('attempt_valid')}`",
        f"- Gates passed: **{evidence.get('pass_count',0)}/18**",
        f"- Failed gates: `{evidence.get('failed_gates',[])}`",
        f"- Future daily rows opened: **{evidence['future_daily_rows_opened']}**",
        f"- Future cancelled/terminated membership opened: **{evidence['future_cancelled_terminated_membership_opened']}**",
        f"- Daily entity-body bytes consumed: **{evidence['daily_entity_body_bytes_consumed']}**",
        f"- Incremental monetary cost: **{evidence['incremental_monetary_cost_usd']} USD**","",
        "## Gate ledger","",
        "| Gate | PASS | Observed |","|---:|:---:|---|"
    ]
    for g in evidence["gates"]:
        obs=json.dumps(g.get("observed"),sort_keys=True,ensure_ascii=False)
        if len(obs)>900:
            obs=obs[:897]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{obs.replace(chr(96),'')}` |")
    if evidence.get("implementation_error"):
        lines += ["","## Implementation error","",f"`{evidence['implementation_error']}`"]
    lines += ["","No future Microwave daily transaction body was opened by this attempt. Scientific thresholds were not modified.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(evidence["disposition"])
    print(evidence.get("pass_count"), evidence.get("failed_gates"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
