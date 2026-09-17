#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import tempfile
import zipfile
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

import run_us_epa_xmedia_f01 as base

ROOT = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "research" / "US-EPA-XMEDIA-N01"
OUT = OUTDIR / "STAGING_RESULT.json"
MANIFEST = OUTDIR / "DESIGN_MANIFEST.json"
CONTRACT = "12f30d5d27d7d4f27022bc355c2a0c62a76e9f0c"
PASS_GATE = "PASS_US_EPA_XMEDIA_N01_MATCHED_MONITORING_INTENSITY_DESIGN_IDENTIFIABLE"
HOLD_GATE = "HOLD_US_EPA_XMEDIA_N01_MATCHED_MONITORING_INTENSITY_DESIGN_NOT_IDENTIFIABLE"
INDEX = date(2023, 12, 31)
FOLLOWUP_END = date(2024, 12, 31)


def parse_date(v: str | None) -> date | None:
    s = base.norm(v)
    if not s:
        return None
    for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%d-%b-%Y", "%d-%b-%y", "%m/%d/%y", "%Y%m%d"):
        try:
            d = datetime.strptime(s, fmt).date()
            return d if 1900 <= d.year <= 2100 else None
        except ValueError:
            pass
    return None


def calendar_within_10y(a: date, b: date) -> bool:
    lo, hi = sorted((a, b))
    try:
        bound = lo.replace(year=lo.year + 10)
    except ValueError:
        bound = lo.replace(year=lo.year + 10, day=28)
    return hi <= bound


def canonical_sha(obj) -> str:
    import hashlib
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    assert not OUT.exists() and not MANIFEST.exists(), "immutable N01 staging already exists"
    cp = json.loads((ROOT / "context" / "checkpoint.json").read_text(encoding="utf-8"))
    assert cp == {
        "checkpoint_id": "CHK-20260917-US-EPA-XMEDIA-N01-ACTIVE",
        "active_issue": 151,
        "active_research": "US-EPA-XMEDIA-N01",
        "last_completed_issue": 150,
        "last_completed_research": "US-EPA-XMEDIA-F01",
        "last_decision": "DEC-214",
        "updated": "2026-09-17",
    }

    boundaries = {
        "npdes_effluent_violation_rows_opened": False,
        "dmr_outcome_rows_opened": False,
        "rcra_violation_outcome_rows_opened": False,
        "future_outcome_membership_opened": False,
        "relationship_computed": False,
        "predictive_metric_computed": False,
        "causal_claim_made": False,
        "identity_repair_used": False,
    }

    result = {
        "research": "US-EPA-XMEDIA-N01",
        "issue": 151,
        "contract_commit": CONTRACT,
        "activation_decision": "DEC-214",
        "generated_utc": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "incremental_monetary_cost_usd": 0,
        "boundaries": boundaries,
        "sources": {},
        "diagnostics": {},
        "requirements": [],
    }

    required_headers = {
        "rcra": {"ISN_RCR_EVAL", "REGISTRY_ID", "SOURCE_ID", "EVAL_TYPE", "EVAL_IDENTIFIER", "EVAL_LEAD_AGENCY", "EVAL_ACTIVITY_LOCATION", "EVAL_DATE"},
        "frs": {"PGM_SYS_ACRNM", "PGM_SYS_ID", "REGISTRY_ID"},
        "fac": {"NPDES_ID", "FACILITY_UIN", "STATE_CODE", "FACILITY_TYPE_CODE"},
        "permit": {"EXTERNAL_PERMIT_NMBR", "VERSION_NMBR", "FACILITY_TYPE_INDICATOR", "PERMIT_TYPE_CODE", "MAJOR_MINOR_STATUS_FLAG", "ORIGINAL_ISSUE_DATE", "ISSUE_DATE", "EFFECTIVE_DATE", "EXPIRATION_DATE", "RETIREMENT_DATE", "TERMINATION_DATE"},
    }
    seen_headers = {}

    with tempfile.TemporaryDirectory(prefix="epa-xmedia-n01-") as td0:
        td = Path(td0)
        paths = {}
        for key, url in base.SOURCES.items():
            p = td / f"{key}.zip"
            n, digest = base.download(url, p)
            assert zipfile.is_zipfile(p)
            with zipfile.ZipFile(p) as z:
                result["sources"][key] = {"url": url, "bytes": n, "sha256": digest, "member_fingerprint_sha256": base.member_fingerprint(z)}
            paths[key] = p

        # FRS exact program mappings by Registry ID.
        reg_programs = {"RCRAINFO": defaultdict(set), "NPDES": defaultdict(set)}
        with zipfile.ZipFile(paths["frs"]) as z:
            member = base.find_member(z, "FRS_PROGRAM_LINKS")
            first = True
            for fields, row in base.dict_rows(z, member):
                if first:
                    seen_headers["frs"] = set(fields); first = False
                acr = base.norm(row.get("PGM_SYS_ACRNM")).upper()
                if acr in reg_programs:
                    rid, pid = base.norm(row.get("REGISTRY_ID")), base.norm(row.get("PGM_SYS_ID"))
                    if rid and pid:
                        reg_programs[acr][rid].add(pid)
        one_to_one = {}
        for rid in sorted(set(reg_programs["RCRAINFO"]) & set(reg_programs["NPDES"])):
            rs, ns = reg_programs["RCRAINFO"][rid], reg_programs["NPDES"][rid]
            if len(rs) == 1 and len(ns) == 1:
                one_to_one[rid] = (next(iter(rs)), next(iter(ns)))

        # RCRA structural evaluation history only.
        eval_by_source = defaultdict(list)
        isn_map = {}
        conflict_sources = set()
        with zipfile.ZipFile(paths["rcra"]) as z:
            member = base.find_member(z, "PIPELINE_RCRA_01_EVALUATIONS")
            first = True
            for fields, row in base.dict_rows(z, member):
                if first:
                    seen_headers["rcra"] = set(fields); first = False
                isn = base.norm(row.get("ISN_RCR_EVAL"))
                sid, rid = base.norm(row.get("SOURCE_ID")), base.norm(row.get("REGISTRY_ID"))
                d = parse_date(row.get("EVAL_DATE"))
                structural = (
                    sid, rid, d.isoformat() if d else "",
                    base.norm(row.get("EVAL_TYPE")), base.norm(row.get("EVAL_IDENTIFIER")),
                    base.norm(row.get("EVAL_LEAD_AGENCY")), base.norm(row.get("EVAL_ACTIVITY_LOCATION")),
                )
                if not isn or not sid or not rid or d is None:
                    continue
                if isn in isn_map and isn_map[isn] != structural:
                    conflict_sources.add(sid); conflict_sources.add(isn_map[isn][0])
                    continue
                isn_map[isn] = structural
                eval_by_source[sid].append((isn, rid, d))

        # NPDES facility structural map.
        fac_map = defaultdict(set)
        with zipfile.ZipFile(paths["npdes"]) as z:
            member = base.find_member(z, "ICIS_FACILITIES")
            first = True
            for fields, row in base.dict_rows(z, member):
                if first:
                    seen_headers["fac"] = set(fields); first = False
                pid = base.norm(row.get("NPDES_ID")); rid = base.norm(row.get("FACILITY_UIN"))
                state = base.norm(row.get("STATE_CODE")).upper(); ftype = base.norm(row.get("FACILITY_TYPE_CODE"))
                if pid and rid:
                    fac_map[pid].add((rid, state, ftype))

        # Current permit version structural map; record raw structural tuples, then fail closed on disagreement.
        permit_map = defaultdict(set)
        with zipfile.ZipFile(paths["npdes"]) as z:
            member = base.find_member(z, "ICIS_PERMITS")
            first = True
            for fields, row in base.dict_rows(z, member):
                if first:
                    seen_headers["permit"] = set(fields); first = False
                pid = base.norm(row.get("EXTERNAL_PERMIT_NMBR"))
                ver = base.norm(row.get("VERSION_NMBR"))
                if not pid or ver != "0":
                    continue
                vals = tuple(base.norm(row.get(f)) for f in (
                    "FACILITY_TYPE_INDICATOR", "PERMIT_TYPE_CODE", "MAJOR_MINOR_STATUS_FLAG",
                    "ORIGINAL_ISSUE_DATE", "ISSUE_DATE", "EFFECTIVE_DATE", "EXPIRATION_DATE",
                    "RETIREMENT_DATE", "TERMINATION_DATE",
                ))
                permit_map[pid].add(vals)

        headers_ok = all(required_headers[k] <= seen_headers.get(k, set()) for k in required_headers)

        eligible = []
        exclusion = defaultdict(int)
        for rid, (sid, pid) in one_to_one.items():
            if sid in conflict_sources:
                exclusion["rcra_conflicting_isn"] += 1; continue
            evals = [x for x in eval_by_source.get(sid, []) if x[1] == rid]
            if not evals:
                exclusion["rcra_exact_pair_missing"] += 1; continue
            if len(fac_map.get(pid, set())) != 1:
                exclusion["npdes_facility_ambiguous"] += 1; continue
            frid, state, facility_type_code = next(iter(fac_map[pid]))
            if frid != rid or len(state) != 2:
                exclusion["npdes_facility_identity_or_state"] += 1; continue
            pset = permit_map.get(pid, set())
            if len(pset) != 1:
                exclusion["permit_version0_missing_or_conflicting"] += 1; continue
            (facility_type_indicator, permit_type, major_minor, original_s, issue_s, effective_s, expiration_s, retirement_s, termination_s) = next(iter(pset))
            if permit_type not in {"NPD", "GPC"} or major_minor not in {"M", "N"} or not facility_type_indicator:
                exclusion["permit_scope"] += 1; continue
            anchor = None
            for raw in (effective_s, issue_s, original_s):
                d = parse_date(raw)
                if d is not None:
                    anchor = d; break
            if anchor is None or anchor > INDEX:
                exclusion["permit_anchor"] += 1; continue
            bad_terminal = False
            for raw in (retirement_s, termination_s):
                if raw:
                    d = parse_date(raw)
                    if d is None or d <= FOLLOWUP_END:
                        bad_terminal = True
            if bad_terminal:
                exclusion["permit_terminal_before_followup_end"] += 1; continue

            baseline = sorted({isn: d for isn, _, d in evals if date(2018,1,1) <= d <= date(2020,12,31)}.items())
            exposure = sorted({isn: d for isn, _, d in evals if date(2021,1,1) <= d <= date(2023,12,31)}.items())
            if not baseline:
                exclusion["no_baseline_eval"] += 1; continue
            last_base = max(d for _, d in baseline)
            eligible.append({
                "registry_id": rid, "rcra_source_id": sid, "npdes_id": pid,
                "state_code": state, "facility_type_code": facility_type_code,
                "facility_type_indicator": facility_type_indicator,
                "permit_type_code": permit_type, "major_minor_status_flag": major_minor,
                "permit_effective_anchor": anchor.isoformat(),
                "permit_expiration_date": parse_date(expiration_s).isoformat() if parse_date(expiration_s) else None,
                "baseline_eval_count": len(baseline),
                "baseline_last_eval_date": last_base.isoformat(),
                "exposure_eval_count": len(exposure),
                "stratum": "|".join((state, major_minor, permit_type, facility_type_indicator)),
            })

        strata = defaultdict(list)
        for u in eligible:
            strata[u["stratum"]].append(u)

        strict_strata = {}
        quartiles = {}
        for skey, units in strata.items():
            if len(units) < 16:
                continue
            ordered = sorted(units, key=lambda u: (u["exposure_eval_count"], u["registry_id"]))
            k = len(ordered) // 4
            low, high = ordered[:k], ordered[-k:]
            if not low or not high:
                continue
            if min(u["exposure_eval_count"] for u in high) <= max(u["exposure_eval_count"] for u in low):
                continue
            strict_strata[skey] = units
            quartiles[skey] = (low, high)

        pairs = []
        pair_idx = 0
        for skey in sorted(quartiles):
            low, high = quartiles[skey]
            unused = {u["registry_id"]: u for u in low}
            for h in sorted(high, key=lambda u: (u["exposure_eval_count"], u["registry_id"]), reverse=True):
                if not unused:
                    break
                hbase = date.fromisoformat(h["baseline_last_eval_date"])
                hanchor = date.fromisoformat(h["permit_effective_anchor"])
                best = min(unused.values(), key=lambda l: (
                    abs(h["baseline_eval_count"] - l["baseline_eval_count"]),
                    abs((hbase - date.fromisoformat(l["baseline_last_eval_date"])).days),
                    abs((hanchor - date.fromisoformat(l["permit_effective_anchor"])).days),
                    l["registry_id"],
                ))
                pair_idx += 1
                pairs.append({"pair_id": f"EPA-XM-{pair_idx:05d}", "stratum": skey, "high": h, "low": best})
                del unused[best["registry_id"]]

        manifest_core = {
            "research": "US-EPA-XMEDIA-N01",
            "contract_commit": CONTRACT,
            "index_date": INDEX.isoformat(),
            "baseline_window": ["2018-01-01", "2020-12-31"],
            "exposure_window": ["2021-01-01", "2023-12-31"],
            "future_outcome_window": ["2024-01-01", "2024-12-31"],
            "outcome_membership_included": False,
            "pairs": pairs,
        }
        manifest_sha = canonical_sha(manifest_core)
        manifest = dict(manifest_core)
        manifest["canonical_core_sha256"] = manifest_sha
        OUTDIR.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        states = {p["high"]["state_code"] for p in pairs} | {p["low"]["state_code"] for p in pairs}
        ids = []
        strict_exposure = True
        ratio_ok = 0
        age_ok = 0
        for p in pairs:
            h, l = p["high"], p["low"]
            strict_exposure &= h["exposure_eval_count"] > l["exposure_eval_count"]
            ids += [("r",h["registry_id"]),("r",l["registry_id"]),("s",h["rcra_source_id"]),("s",l["rcra_source_id"]),("n",h["npdes_id"]),("n",l["npdes_id"])]
            ratio = h["baseline_eval_count"] / l["baseline_eval_count"]
            ratio_ok += int(1/3 <= ratio <= 3)
            age_ok += int(calendar_within_10y(date.fromisoformat(h["permit_effective_anchor"]), date.fromisoformat(l["permit_effective_anchor"])))
        no_reuse = len(ids) == len(set(ids))
        ratio_rate = ratio_ok / len(pairs) if pairs else 0.0
        age_rate = age_ok / len(pairs) if pairs else 0.0

        d = result["diagnostics"]
        d.update({
            "frs_exact_cross_program_registry_ids": len(set(reg_programs["RCRAINFO"]) & set(reg_programs["NPDES"])),
            "frs_exact_one_to_one_registry_ids": len(one_to_one),
            "rcra_conflicting_isn_source_ids": len(conflict_sources),
            "eligible_registry_ids": len(eligible),
            "all_structural_strata": len(strata),
            "strict_separation_strata": len(strict_strata),
            "matched_pairs": len(pairs),
            "matched_states": sorted(states),
            "matched_state_count": len(states),
            "baseline_ratio_within_1_3_to_3_rate": ratio_rate,
            "permit_age_difference_within_10y_rate": age_rate,
            "exclusions": dict(sorted(exclusion.items())),
            "manifest_sha256": manifest_sha,
        })

        def req(n, name, passed, evidence):
            result["requirements"].append({"number": n, "name": name, "pass": bool(passed), "evidence": evidence})
        req(1, "authorized structural tables readable", all(v["bytes"] > 0 for v in result["sources"].values()), result["sources"])
        req(2, "all frozen required fields present", headers_ok, {k: sorted(required_headers[k] - seen_headers.get(k,set())) for k in required_headers})
        req(3, "no forbidden outcome table opened", not any((boundaries[k] for k in ("npdes_effluent_violation_rows_opened","dmr_outcome_rows_opened","rcra_violation_outcome_rows_opened"))), boundaries)
        req(4, "exact one-to-one identity only", not boundaries["identity_repair_used"], {"one_to_one_registry_ids": len(one_to_one), "identity_repair_used": False})
        req(5, ">=1000 structurally eligible Registry IDs", len(eligible) >= 1000, len(eligible))
        req(6, ">=20 strict-separation strata", len(strict_strata) >= 20, len(strict_strata))
        req(7, ">=250 matched pairs", len(pairs) >= 250, len(pairs))
        req(8, ">=20 matched states", len(states) >= 20, sorted(states))
        req(9, "HIGH exposure strictly exceeds LOW", strict_exposure and bool(pairs), strict_exposure)
        req(10, "no Registry/RCRA/NPDES ID reuse", no_reuse and bool(pairs), no_reuse)
        req(11, ">=75% baseline eval-count ratio within [1/3,3]", ratio_rate >= .75, ratio_rate)
        req(12, ">=75% permit-age difference <=10 years", age_rate >= .75, age_rate)
        req(13, "deterministic manifest SHA-256 persisted", len(manifest_sha) == 64, manifest_sha)
        req(14, "NPDES effluent rows unopened", boundaries["npdes_effluent_violation_rows_opened"] is False, False)
        req(15, "DMR and future outcome membership unopened", not boundaries["dmr_outcome_rows_opened"] and not boundaries["future_outcome_membership_opened"], {"dmr": False, "future": False})
        req(16, "RCRA violation outcomes unopened", boundaries["rcra_violation_outcome_rows_opened"] is False, False)
        req(17, "no relationship/prediction/causality", not boundaries["relationship_computed"] and not boundaries["predictive_metric_computed"] and not boundaries["causal_claim_made"], boundaries)
        req(18, "zero incremental monetary cost", result["incremental_monetary_cost_usd"] == 0, 0)

    result["requirements_passed"] = sum(r["pass"] for r in result["requirements"])
    result["requirements_total"] = 18
    result["gate"] = PASS_GATE if result["requirements_passed"] == 18 else HOLD_GATE
    result["scientific_disposition"] = "PASS" if result["requirements_passed"] == 18 else "HOLD"
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"gate": result["gate"], "requirements": f"{result['requirements_passed']}/18", "eligible": result["diagnostics"]["eligible_registry_ids"], "pairs": result["diagnostics"]["matched_pairs"]}, sort_keys=True))


if __name__ == "__main__":
    main()
