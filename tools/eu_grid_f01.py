#!/usr/bin/env python3
"""Outcome-blind EU-GRID-F01 source-operability and panel-feasibility probe.

The probe never converts or persists load, forecast, physical-flow or weather
magnitudes. ENTSO-E numeric cells, if returned by the public web view, are
reduced immediately to structural/nonblank interval counts. E-OBS inspection is
limited to official version, variable, temporal and grid metadata.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "EU-GRID-F01"
UA = "AI-Innovative-Research-Engine/EU-GRID-F01-outcome-blind"
LOAD = "https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show"
FLOW = "https://transparency.entsoe.eu/transmission-domain/physicalFlow/show"
EOBS = "https://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php"

COUNTRIES = {
    "FR": {"name": "France", "eic": "10YFR-RTE------C"},
    "BE": {"name": "Belgium", "eic": "10YBE----------2"},
    "NL": {"name": "Netherlands", "eic": "10YNL----------L"},
    "ES": {"name": "Spain", "eic": "10YES-REE------0"},
    "PT": {"name": "Portugal", "eic": "10YPT-REN------W"},
    "PL": {"name": "Poland", "eic": "10YPL-AREA-----S"},
    "AT": {"name": "Austria", "eic": "10YAT-APG------L"},
    "CZ": {"name": "Czech Republic", "eic": "10YCZ-CEPS-----N"},
}

# Prospectively fixed quarterly anchors; none depends on observed grid/weather values.
ANCHORS = [f"{year}-{month:02d}-15" for year in range(2022, 2026) for month in (1, 4, 7, 10)]

# Structural border pairs within the frozen set. Direction/magnitude is irrelevant in F01.
BORDERS = [
    ("FR", "BE"), ("FR", "ES"), ("BE", "NL"), ("ES", "PT"),
    ("PL", "CZ"), ("AT", "CZ"),
]


def fetch(url: str, attempts: int = 4) -> tuple[bytes, dict]:
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml",
            })
            with urllib.request.urlopen(req, timeout=120) as r:
                b = r.read()
                return b, {
                    "status": getattr(r, "status", 200),
                    "final_url": r.geturl(),
                    "bytes": len(b),
                    "sha256": hashlib.sha256(b).hexdigest(),
                }
        except Exception as e:
            last = e
            if i + 1 < attempts:
                time.sleep(2 * (i + 1))
    raise last


def load_url(code: str, eic: str, day: str) -> str:
    y, m, d = day.split("-")
    q = {
        "areaType": "BZN",
        "atch": "false",
        "biddingZone.values": f"CTY|{eic}!BZN|{eic}",
        "dateTime.dateTime": f"{d}.{m}.{y} 00:00|UTC|DAY",
        "dateTime.timezone": "UTC",
        "dateTime.timezone_input": "UTC",
        "defaultValue": "false",
        "name": "",
        "viewType": "TABLE",
    }
    return LOAD + "?" + urllib.parse.urlencode(q)


def inspect_load_html(text: str, expected_eic: str) -> dict:
    # Never capture numeric load/forecast cells. Only labels/units/interval count.
    clean = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.I | re.S)
    clean = re.sub(r"<style\b[^>]*>.*?</style>", " ", clean, flags=re.I | re.S)
    clean = re.sub(r"<[^>]+>", " ", clean)
    clean = re.sub(r"\s+", " ", clean)
    intervals = re.findall(r"\b(?:[01]\d|2[0-3]):[0-5]\d\s*-\s*(?:[01]\d|2[0-3]):[0-5]\d\b", clean)
    return {
        "has_actual_total_load_label": "Actual Total Load" in clean and "6.1.A" in clean,
        "has_day_ahead_forecast_label": "Day-ahead Total Load Forecast" in clean and "6.1.B" in clean,
        "has_mw_unit_label": bool(re.search(r"\bMW\b", clean)),
        "expected_eic_present": expected_eic in text,
        "time_interval_label_count": len(intervals),
        "has_export_login_notice": "Please log in to export data" in clean,
        "utc_query_semantics": True,
    }


def inspect_eobs(text: str) -> dict:
    clean = re.sub(r"<[^>]+>", " ", text)
    clean = re.sub(r"\s+", " ", clean)
    return {
        "version_33_0e_present": "33.0e" in clean,
        "coverage_1950_to_2025_present": "1950-01-01" in clean and "2025-12-31" in clean,
        "daily_mean_temperature_tg_present": "daily mean temperature" in clean.lower() and "TG" in clean,
        "regular_grid_0_1_0_25_present": ("0.1" in clean and "0.25" in clean and "regular grid" in clean.lower()),
        "europe_scope_present": "Europe" in clean,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    load_checks = []
    country_summary = []

    for code, meta in COUNTRIES.items():
        ok_count = 0
        login_notice_count = 0
        interval_counts = []
        hashes = []
        for day in ANCHORS:
            url = load_url(code, meta["eic"], day)
            try:
                b, src = fetch(url)
                chk = inspect_load_html(b.decode("utf-8", "replace"), meta["eic"])
                supported = (
                    src["status"] == 200
                    and chk["has_actual_total_load_label"]
                    and chk["has_day_ahead_forecast_label"]
                    and chk["has_mw_unit_label"]
                    and chk["expected_eic_present"]
                    and chk["time_interval_label_count"] >= 23
                )
                ok_count += int(supported)
                login_notice_count += int(chk["has_export_login_notice"])
                interval_counts.append(chk["time_interval_label_count"])
                hashes.append(src["sha256"])
                load_checks.append({
                    "country": code, "anchor": day, "status": src["status"],
                    "bytes": src["bytes"], "sha256": src["sha256"],
                    **chk, "structural_support": supported,
                })
            except Exception as e:
                load_checks.append({
                    "country": code, "anchor": day, "error": f"{type(e).__name__}: {e}",
                    "structural_support": False,
                })
        country_summary.append({
            "country": code,
            "name": meta["name"],
            "expected_eic": meta["eic"],
            "anchors_total": len(ANCHORS),
            "anchors_structurally_supported": ok_count,
            "all_anchors_supported": ok_count == len(ANCHORS),
            "export_login_notice_anchors": login_notice_count,
            "min_interval_label_count": min(interval_counts) if interval_counts else 0,
            "max_interval_label_count": max(interval_counts) if interval_counts else 0,
            "distinct_page_hashes": len(set(hashes)),
        })

    # One public physical-flow page is sufficient to inspect the dropdown's structural border identities.
    flow_q = {
        "areaType": "BORDER_CTY", "atch": "false",
        "border.values": f"CTY|{COUNTRIES['FR']['eic']}!CTY_CTY|{COUNTRIES['FR']['eic']}_CTY_CTY|{COUNTRIES['BE']['eic']}",
        "dateTime.dateTime": "15.01.2025 00:00|UTC|DAY",
        "dateTime.timezone": "UTC", "dateTime.timezone_input": "UTC",
        "defaultValue": "false", "name": "", "viewType": "TABLE",
    }
    flow_url = FLOW + "?" + urllib.parse.urlencode(flow_q)
    try:
        flow_b, flow_src = fetch(flow_url)
        flow_text = re.sub(r"<[^>]+>", " ", flow_b.decode("utf-8", "replace"))
        flow_text = re.sub(r"\s+", " ", flow_text)
        flow_domain = "Physical Flows" in flow_text and "12.1.G" in flow_text
        border_checks = []
        supported_countries = set()
        for a, b in BORDERS:
            na, nb = COUNTRIES[a]["name"], COUNTRIES[b]["name"]
            patterns = [
                f"{na} ({a}) - {nb} ({b})",
                f"{nb} ({b}) - {na} ({a})",
                f"BZN|{a} - BZN|{b}", f"BZN|{b} - BZN|{a}",
            ]
            present = any(p in flow_text for p in patterns)
            border_checks.append({"a": a, "b": b, "structural_option_present": present})
            if present:
                supported_countries.update([a, b])
        flow_summary = {
            "status": flow_src["status"], "bytes": flow_src["bytes"], "sha256": flow_src["sha256"],
            "physical_flow_domain_present": flow_domain,
            "border_checks": border_checks,
            "frozen_countries_with_internal_border_support": sorted(supported_countries),
            "supported_country_count": len(supported_countries),
        }
    except Exception as e:
        flow_summary = {"error": f"{type(e).__name__}: {e}", "supported_country_count": 0, "border_checks": []}

    try:
        eobs_b, eobs_src = fetch(EOBS)
        eobs = {**eobs_src, **inspect_eobs(eobs_b.decode("utf-8", "replace"))}
    except Exception as e:
        eobs = {"error": f"{type(e).__name__}: {e}"}

    countries_full = sum(1 for x in country_summary if x["all_anchors_supported"])
    no_login_machine_path = countries_full == len(COUNTRIES)
    eobs_ok = all(eobs.get(k) for k in [
        "version_33_0e_present", "coverage_1950_to_2025_present",
        "daily_mean_temperature_tg_present", "regular_grid_0_1_0_25_present", "europe_scope_present",
    ])
    border_ok = flow_summary.get("supported_country_count", 0) >= 6

    if countries_full == 8 and no_login_machine_path and eobs_ok and border_ok:
        gate = "PASS_EU_GRID_F01_SOURCE_PANEL_FEASIBLE"
    elif countries_full >= 6 and eobs_ok:
        gate = "PARTIAL_EU_GRID_F01_SOURCE_READY_REGISTRATION_REQUIRED"
    else:
        gate = "HOLD_EU_GRID_F01_SOURCE_OR_IDENTITY_SUPPORT"

    result = {
        "boundary": {
            "load_magnitudes_parsed_or_persisted": False,
            "forecast_magnitudes_parsed_or_persisted": False,
            "forecast_error_computed": False,
            "physical_flow_magnitudes_parsed_or_persisted": False,
            "weather_magnitudes_parsed_or_persisted": False,
            "relationship_computed": False,
            "numeric_cells_reduced_to_structural_presence_only": True,
        },
        "frozen_countries": list(COUNTRIES),
        "structural_period": ["2022-01-01", "2025-12-31"],
        "prospective_anchor_dates": ANCHORS,
        "country_summary": country_summary,
        "entsoe_no_login_machine_path_8_of_8": no_login_machine_path,
        "entsoe_export_registration_notice_observed": any(x["export_login_notice_anchors"] > 0 for x in country_summary),
        "physical_flow": flow_summary,
        "eobs": eobs,
        "eobs_country_aggregation_rule": "Prospective later-stage rule: aggregate E-OBS regular-grid cells to frozen country polygons by a separately versioned official boundary asset before any values are opened; F01 does not open weather fields.",
        "gate": gate,
        "incremental_monetary_cost_usd": 0,
    }
    (OUT / "SOURCE_PANEL_MANIFEST.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# EU-GRID-F01 Source-Operability Result", "",
        f"**`{gate}`**", "",
        "Outcome-blind: load/forecast/flow/weather magnitudes were neither converted nor persisted; only structural labels, hashes, interval counts and support booleans were retained.", "",
        f"- frozen countries with all {len(ANCHORS)} anchor pages structurally supported: **{countries_full}/8**",
        f"- no-login machine-readable public web-view route across 8/8: **{no_login_machine_path}**",
        f"- export-login notice observed: **{result['entsoe_export_registration_notice_observed']}**",
        f"- frozen countries with structural cross-border support to another frozen country: **{flow_summary.get('supported_country_count', 0)}/8**",
        f"- E-OBS v33.0e / 1950–2025 / TG / regular-grid metadata support: **{eobs_ok}**", "",
        "## Country support",
    ]
    for x in country_summary:
        lines.append(f"- `{x['country']}` `{x['expected_eic']}`: {x['anchors_structurally_supported']}/{x['anchors_total']} anchors; intervals {x['min_interval_label_count']}..{x['max_interval_label_count']}; export-login anchors={x['export_login_notice_anchors']}")
    lines += ["", "## Cross-border structural options"]
    for x in flow_summary.get("border_checks", []):
        lines.append(f"- `{x['a']}-{x['b']}`: **{x['structural_option_present']}**")
    lines += ["", "Incremental monetary cost: **0 USD**."]
    (OUT / "RESULT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
