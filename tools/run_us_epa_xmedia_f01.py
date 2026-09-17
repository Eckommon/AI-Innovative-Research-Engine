#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import shutil
import tempfile
import urllib.request
import zipfile
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "research" / "US-EPA-XMEDIA-F01"
OUT = OUTDIR / "STAGING_RESULT.json"

SOURCES = {
    "rcra": "https://echo.epa.gov/files/echodownloads/pipeline_rcra_downloads.zip",
    "frs": "https://echo.epa.gov/files/echodownloads/frs_downloads.zip",
    "npdes": "https://echo.epa.gov/files/echodownloads/npdes_downloads.zip",
}

EXPECTED = {
    "rcra_eval": "PIPELINE_RCRA_01_EVALUATIONS",
    "frs_links": "FRS_PROGRAM_LINKS",
    "npdes_fac": "ICIS_FACILITIES",
    "npdes_permit": "ICIS_PERMITS",
}

FORBIDDEN_TOKENS = (
    "NPDES_EFF_VIOLATIONS",
    "effluent_violations",
    "part2",
    "dmr_values",
    "dmr_limits",
)

PASS_GATE = "PASS_US_EPA_XMEDIA_F01_EXACT_FRS_CROSS_PROGRAM_JOIN_READY"
HOLD_GATE = "HOLD_US_EPA_XMEDIA_F01_SOURCE_SCHEMA_SCOPE_OR_IDENTITY"


def norm(v: str | None) -> str:
    return (v or "").strip()


def sha_lines(values) -> str:
    h = hashlib.sha256()
    for value in sorted(values):
        h.update(str(value).encode("utf-8"))
        h.update(b"\n")
    return h.hexdigest()


def download(url: str, dest: Path) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "AI-Innovative-Research-Engine/US-EPA-XMEDIA-F01"})
    h = hashlib.sha256()
    total = 0
    with urllib.request.urlopen(req, timeout=180) as r, dest.open("wb") as f:
        while True:
            chunk = r.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)
            h.update(chunk)
            total += len(chunk)
    return total, h.hexdigest()


def member_fingerprint(zf: zipfile.ZipFile) -> str:
    rows = [f"{i.filename}\t{i.file_size}\t{i.CRC}" for i in zf.infolist() if not i.is_dir()]
    return sha_lines(rows)


def find_member(zf: zipfile.ZipFile, stem: str) -> str:
    target = stem.upper()
    matches = []
    for name in zf.namelist():
        base = Path(name).name.upper()
        if base.endswith(".CSV"):
            base = base[:-4]
        if base == target:
            matches.append(name)
    if len(matches) != 1:
        raise RuntimeError(f"expected exactly one member for {stem}, found {matches}")
    return matches[0]


def dict_rows(zf: zipfile.ZipFile, member: str):
    raw = zf.open(member, "r")
    text = io.TextIOWrapper(raw, encoding="utf-8-sig", errors="replace", newline="")
    reader = csv.DictReader(text)
    fields = [norm(x) for x in (reader.fieldnames or [])]
    for row in reader:
        yield fields, {norm(k): norm(v) for k, v in row.items() if k is not None}


def parse_year(value: str) -> int | None:
    s = norm(value)
    if not s:
        return None
    m = re.search(r"(?<!\d)((?:19|20)\d{2})(?!\d)", s)
    if m:
        y = int(m.group(1))
        if 1900 <= y <= 2100:
            return y
    for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%d-%b-%Y", "%d-%b-%y", "%m/%d/%y"):
        try:
            return datetime.strptime(s, fmt).year
        except ValueError:
            pass
    return None


def update_unique(mapping: dict[str, str | None], key: str, value: str) -> None:
    if not key or not value:
        return
    if key not in mapping:
        mapping[key] = value
    elif mapping[key] != value:
        mapping[key] = None


def main() -> None:
    # Hard source-level firewall: the runner has exactly three authorized URLs.
    assert set(SOURCES) == {"rcra", "frs", "npdes"}
    assert all("echo.epa.gov/files/echodownloads/" in u for u in SOURCES.values())
    assert all(not any(t.lower() in u.lower() for t in FORBIDDEN_TOKENS) for u in SOURCES.values())

    checkpoint = json.loads((ROOT / "context" / "checkpoint.json").read_text(encoding="utf-8"))
    assert checkpoint == {
        "checkpoint_id": "CHK-20260917-US-EPA-XMEDIA-F01-ACTIVE",
        "active_issue": 150,
        "active_research": "US-EPA-XMEDIA-F01",
        "last_completed_issue": 149,
        "last_completed_research": "PORTFOLIO-R34",
        "last_decision": "DEC-212",
        "updated": "2026-09-17",
    }
    assert not OUT.exists(), "immutable staging result already exists"

    result: dict = {
        "research": "US-EPA-XMEDIA-F01",
        "issue": 150,
        "contract_commit": "86a7a01ba3b64160ee21a7ea821536d3d1adbb14",
        "activation_decision": "DEC-212",
        "generated_utc": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "incremental_monetary_cost_usd": 0,
        "effluent_violation_rows_opened": False,
        "dmr_outcome_rows_opened": False,
        "relationship_computed": False,
        "predictive_metric_computed": False,
        "causal_claim_made": False,
        "identity_repair_used": False,
        "sources": {},
        "measurements": {},
        "requirements": [],
    }

    with tempfile.TemporaryDirectory(prefix="epa-xmedia-f01-") as td:
        td = Path(td)
        paths = {}
        for key, url in SOURCES.items():
            p = td / f"{key}.zip"
            n, digest = download(url, p)
            if not zipfile.is_zipfile(p):
                raise RuntimeError(f"not a zip: {url}")
            with zipfile.ZipFile(p) as z:
                result["sources"][key] = {
                    "url": url,
                    "bytes": n,
                    "sha256": digest,
                    "member_count": len([x for x in z.infolist() if not x.is_dir()]),
                    "member_fingerprint_sha256": member_fingerprint(z),
                }
            paths[key] = p

        # RCRA Pipeline: read evaluation identity/date only. Do not touch violation/enforcement members.
        rcra_pairs: set[tuple[str, str]] = set()
        rcra_source_ids: set[str] = set()
        rcra_registry_ids: set[str] = set()
        rcra_years: set[int] = set()
        rcra_rows = 0
        rcra_valid_rows = 0
        rcra_source_map: dict[str, str | None] = {}
        with zipfile.ZipFile(paths["rcra"]) as z:
            member = find_member(z, EXPECTED["rcra_eval"])
            header = None
            for fields, row in dict_rows(z, member):
                if header is None:
                    header = fields
                rcra_rows += 1
                sid, rid, d = norm(row.get("SOURCE_ID")), norm(row.get("REGISTRY_ID")), norm(row.get("EVAL_DATE"))
                y = parse_year(d)
                if sid and rid and y is not None:
                    rcra_valid_rows += 1
                    rcra_pairs.add((sid, rid))
                    rcra_source_ids.add(sid)
                    rcra_registry_ids.add(rid)
                    rcra_years.add(y)
                    update_unique(rcra_source_map, sid, rid)
        rcra_required_header = all(x in (header or []) for x in ("REGISTRY_ID", "SOURCE_ID", "EVAL_DATE"))
        rcra_conflict_ids = {k for k, v in rcra_source_map.items() if v is None}
        rcra_unique_ids = {k for k, v in rcra_source_map.items() if v is not None}

        # FRS Program Links: exact source-native program record -> REGISTRY_ID only.
        frs_rows = 0
        frs_header = None
        frs_maps: dict[str, dict[str, str | None]] = {"RCRAINFO": {}, "NPDES": {}}
        frs_seen_acronyms: set[str] = set()
        with zipfile.ZipFile(paths["frs"]) as z:
            member = find_member(z, EXPECTED["frs_links"])
            for fields, row in dict_rows(z, member):
                if frs_header is None:
                    frs_header = fields
                frs_rows += 1
                acr = norm(row.get("PGM_SYS_ACRNM")).upper()
                if acr in frs_maps:
                    frs_seen_acronyms.add(acr)
                    update_unique(frs_maps[acr], norm(row.get("PGM_SYS_ID")), norm(row.get("REGISTRY_ID")))
        frs_required_header = all(x in (frs_header or []) for x in ("PGM_SYS_ACRNM", "PGM_SYS_ID", "REGISTRY_ID"))
        frs_clean_pairs = {
            acr: {(pid, rid) for pid, rid in mp.items() if rid is not None and pid and rid}
            for acr, mp in frs_maps.items()
        }
        frs_clean_ids = {acr: {pid for pid, rid in pairs} for acr, pairs in frs_clean_pairs.items()}
        frs_registries = {acr: {rid for pid, rid in pairs} for acr, pairs in frs_clean_pairs.items()}
        frs_conflicts = {acr: sum(v is None for v in mp.values()) for acr, mp in frs_maps.items()}
        frs_cross_registry = frs_registries["RCRAINFO"] & frs_registries["NPDES"]

        # ICIS-NPDES Part 1 only: facility identity plus permit structural dates.
        npdes_fac_rows = 0
        npdes_fac_header = None
        npdes_fac_pairs: set[tuple[str, str]] = set()
        npdes_ids: set[str] = set()
        npdes_registry_ids: set[str] = set()
        npdes_map: dict[str, str | None] = {}
        npdes_permit_rows = 0
        npdes_permit_header = None
        permit_ids: set[str] = set()
        permit_years: set[int] = set()
        permit_date_fields = ("ORIGINAL_ISSUE_DATE", "ISSUE_DATE", "EFFECTIVE_DATE", "EXPIRATION_DATE", "RETIREMENT_DATE", "TERMINATION_DATE")
        with zipfile.ZipFile(paths["npdes"]) as z:
            fac_member = find_member(z, EXPECTED["npdes_fac"])
            for fields, row in dict_rows(z, fac_member):
                if npdes_fac_header is None:
                    npdes_fac_header = fields
                npdes_fac_rows += 1
                pid, rid = norm(row.get("NPDES_ID")), norm(row.get("FACILITY_UIN"))
                if pid:
                    npdes_ids.add(pid)
                if rid:
                    npdes_registry_ids.add(rid)
                if pid and rid:
                    npdes_fac_pairs.add((pid, rid))
                    update_unique(npdes_map, pid, rid)

            permit_member = find_member(z, EXPECTED["npdes_permit"])
            for fields, row in dict_rows(z, permit_member):
                if npdes_permit_header is None:
                    npdes_permit_header = fields
                npdes_permit_rows += 1
                pid = norm(row.get("EXTERNAL_PERMIT_NMBR"))
                if pid:
                    permit_ids.add(pid)
                for f in permit_date_fields:
                    y = parse_year(row.get(f, ""))
                    if y is not None:
                        permit_years.add(y)

        npdes_fac_required_header = all(x in (npdes_fac_header or []) for x in ("NPDES_ID", "FACILITY_UIN"))
        npdes_permit_required_header = "EXTERNAL_PERMIT_NMBR" in (npdes_permit_header or []) and any(f in (npdes_permit_header or []) for f in permit_date_fields)
        npdes_clean_pairs = {(pid, rid) for pid, rid in npdes_fac_pairs if npdes_map.get(pid) == rid}
        npdes_conflict_ids = {k for k, v in npdes_map.items() if v is None}

        # Exact corroboration and cross-source support.
        rcra_represented_pairs = {(sid, rid) for sid, rid in rcra_pairs if sid in frs_clean_ids["RCRAINFO"]}
        rcra_corroborated_pairs = rcra_represented_pairs & frs_clean_pairs["RCRAINFO"]
        rcra_cov = len(rcra_corroborated_pairs) / len(rcra_represented_pairs) if rcra_represented_pairs else 0.0

        npdes_represented_pairs = {(pid, rid) for pid, rid in npdes_clean_pairs if pid in frs_clean_ids["NPDES"]}
        npdes_corroborated_pairs = npdes_represented_pairs & frs_clean_pairs["NPDES"]
        npdes_cov = len(npdes_corroborated_pairs) / len(npdes_represented_pairs) if npdes_represented_pairs else 0.0

        icis_permit_supported_registry = {rid for pid, rid in npdes_clean_pairs if pid in permit_ids}
        exact_cross_supported = (
            rcra_registry_ids
            & frs_registries["RCRAINFO"]
            & frs_registries["NPDES"]
            & icis_permit_supported_registry
        )

        m = result["measurements"]
        m.update({
            "rcra_evaluation_rows": rcra_rows,
            "rcra_valid_identity_date_rows": rcra_valid_rows,
            "rcra_distinct_source_ids": len(rcra_source_ids),
            "rcra_distinct_registry_ids": len(rcra_registry_ids),
            "rcra_distinct_valid_years": sorted(rcra_years),
            "rcra_source_ids_unique_registry": len(rcra_unique_ids),
            "rcra_source_ids_conflicting_registry": len(rcra_conflict_ids),
            "frs_program_link_rows": frs_rows,
            "frs_seen_required_program_families": sorted(frs_seen_acronyms),
            "frs_rcra_program_ids_nonconflicting": len(frs_clean_ids["RCRAINFO"]),
            "frs_npdes_program_ids_nonconflicting": len(frs_clean_ids["NPDES"]),
            "frs_rcra_program_id_conflicts": frs_conflicts["RCRAINFO"],
            "frs_npdes_program_id_conflicts": frs_conflicts["NPDES"],
            "frs_rcra_registry_ids": len(frs_registries["RCRAINFO"]),
            "frs_npdes_registry_ids": len(frs_registries["NPDES"]),
            "frs_exact_cross_program_registry_intersection": len(frs_cross_registry),
            "rcra_pairs_represented_in_frs": len(rcra_represented_pairs),
            "rcra_pairs_exactly_corroborated_by_frs": len(rcra_corroborated_pairs),
            "rcra_exact_corroboration_rate": rcra_cov,
            "npdes_facility_rows": npdes_fac_rows,
            "npdes_permit_rows": npdes_permit_rows,
            "npdes_distinct_ids": len(npdes_ids),
            "npdes_distinct_registry_ids": len(npdes_registry_ids),
            "npdes_id_registry_conflicts": len(npdes_conflict_ids),
            "npdes_permit_date_years": sorted(permit_years),
            "npdes_pairs_represented_in_frs": len(npdes_represented_pairs),
            "npdes_pairs_exactly_corroborated_by_frs": len(npdes_corroborated_pairs),
            "npdes_exact_corroboration_rate": npdes_cov,
            "exact_cross_program_registry_ids_with_rcra_eval_and_npdes_part1_permit": len(exact_cross_supported),
            "fingerprints": {
                "rcra_exact_identity_pairs_sha256": sha_lines(f"{a}\t{b}" for a, b in rcra_pairs),
                "frs_rcra_exact_pairs_sha256": sha_lines(f"{a}\t{b}" for a, b in frs_clean_pairs["RCRAINFO"]),
                "frs_npdes_exact_pairs_sha256": sha_lines(f"{a}\t{b}" for a, b in frs_clean_pairs["NPDES"]),
                "npdes_part1_exact_identity_pairs_sha256": sha_lines(f"{a}\t{b}" for a, b in npdes_clean_pairs),
                "frs_cross_program_registry_intersection_sha256": sha_lines(frs_cross_registry),
                "exact_cross_supported_registry_sha256": sha_lines(exact_cross_supported),
            },
        })

        def req(n: int, name: str, passed: bool, evidence) -> None:
            result["requirements"].append({"number": n, "name": name, "pass": bool(passed), "evidence": evidence})

        req(1, "official EPA documentation/source readable", True, "all three official source ZIP bytes read")
        req(2, "authorized ZIP integrity and fingerprint", all(v["bytes"] > 0 and v["sha256"] for v in result["sources"].values()), result["sources"])
        req(3, "RCRA required schema", rcra_required_header, {"required": ["REGISTRY_ID", "SOURCE_ID", "EVAL_DATE"]})
        req(4, "RCRA >=5000 distinct SOURCE_ID and REGISTRY_ID", len(rcra_source_ids) >= 5000 and len(rcra_registry_ids) >= 5000, {"source_ids": len(rcra_source_ids), "registry_ids": len(rcra_registry_ids)})
        req(5, "RCRA >=10 years and max >=2025", len(rcra_years) >= 10 and bool(rcra_years) and max(rcra_years) >= 2025, {"n_years": len(rcra_years), "min": min(rcra_years) if rcra_years else None, "max": max(rcra_years) if rcra_years else None})
        req(6, "FRS required schema and RCRAINFO/NPDES families", frs_required_header and frs_seen_acronyms == {"RCRAINFO", "NPDES"}, {"families": sorted(frs_seen_acronyms)})
        req(7, "RCRA exact FRS corroboration >=90%", len(rcra_represented_pairs) > 0 and rcra_cov >= 0.90, {"denominator": len(rcra_represented_pairs), "numerator": len(rcra_corroborated_pairs), "rate": rcra_cov})
        req(8, "NPDES Part 1 required facility/permit schema", npdes_fac_required_header and npdes_permit_required_header, {"facility_required": npdes_fac_required_header, "permit_required": npdes_permit_required_header})
        req(9, "NPDES >=10000 IDs and Registry IDs", len(npdes_ids) >= 10000 and len(npdes_registry_ids) >= 10000, {"npdes_ids": len(npdes_ids), "registry_ids": len(npdes_registry_ids)})
        req(10, "NPDES exact FRS corroboration >=90%", len(npdes_represented_pairs) > 0 and npdes_cov >= 0.90, {"denominator": len(npdes_represented_pairs), "numerator": len(npdes_corroborated_pairs), "rate": npdes_cov})
        req(11, "NPDES permit-date support >=10 years", len(permit_years) >= 10, {"n_years": len(permit_years), "min": min(permit_years) if permit_years else None, "max": max(permit_years) if permit_years else None})
        req(12, "FRS cross-program Registry intersection >=500", len(frs_cross_registry) >= 500, {"count": len(frs_cross_registry)})
        req(13, "fully cross-supported Registry IDs >=500", len(exact_cross_supported) >= 500, {"count": len(exact_cross_supported)})
        req(14, "no identity repair", result["identity_repair_used"] is False, {"identity_repair_used": False})
        req(15, "deterministic identity fingerprints persisted", all(len(v) == 64 for v in m["fingerprints"].values()), m["fingerprints"])
        req(16, "effluent/DMR outcome source unopened", result["effluent_violation_rows_opened"] is False and result["dmr_outcome_rows_opened"] is False, {"effluent_violation_rows_opened": False, "dmr_outcome_rows_opened": False})
        req(17, "no RCRA-conditioned NPDES outcome/ranking/effect", result["relationship_computed"] is False and result["predictive_metric_computed"] is False and result["causal_claim_made"] is False, {"relationship_computed": False, "predictive_metric_computed": False, "causal_claim_made": False})
        req(18, "zero-cost and no relationship/prediction/causality", result["incremental_monetary_cost_usd"] == 0 and not result["relationship_computed"] and not result["predictive_metric_computed"] and not result["causal_claim_made"], {"incremental_monetary_cost_usd": 0})

    result["requirements_passed"] = sum(r["pass"] for r in result["requirements"])
    result["requirements_total"] = len(result["requirements"])
    result["gate"] = PASS_GATE if result["requirements_passed"] == result["requirements_total"] else HOLD_GATE
    result["scientific_disposition"] = "PASS" if result["gate"] == PASS_GATE else "HOLD"

    OUTDIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"gate": result["gate"], "requirements": f"{result['requirements_passed']}/{result['requirements_total']}", "output": str(OUT)}, sort_keys=True))


if __name__ == "__main__":
    main()
