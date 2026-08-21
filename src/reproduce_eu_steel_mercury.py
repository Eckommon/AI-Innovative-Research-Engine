#!/usr/bin/env python3
"""EU-STEEL-R01 reproducibility harness.

KO: EEA의 E-PRTR × PRODCOM 철강 수은집약도 2008→2017 변화를
공식 raw 입력에서 재현하기 위한 보수적 하네스다. 스키마·단위·코드가
확인되지 않으면 추정하지 않고 실패한다.

EN: Conservative harness for reproducing EEA's 2008→2017 steel-mercury
intensity change from official E-PRTR and PRODCOM raw inputs. It fails closed
when schema, units, reporter scope, or legacy code semantics are ambiguous.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

YEARS = (2008, 2017)
EPRTR_ACTIVITIES = {"1.(d)", "2.(a)", "2.(b)"}
PRODCOM_CODES = {
    "2410T121", "2410T122",
    "2410T131", "2410T132",
    "2410T141", "2410T142",
}
EEA33_ISO2 = {
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "EL", "GR",
    "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI",
    "ES", "SE", "UK", "GB", "IS", "LI", "NO", "CH", "RS",
}
TARGET_REFERENCE_PCT = -36.0
PASS_MIN_PCT = -38.0
PASS_MAX_PCT = -34.0


@dataclass(frozen=True)
class Artifact:
    path: Path
    sha256: str
    size: int


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fingerprint(path: Path) -> Artifact:
    return Artifact(path=path, sha256=sha256_file(path), size=path.stat().st_size)


def download(url: str, dest: Path) -> Artifact:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "AI-Innovative-Research-Engine/0.3"})
    with urllib.request.urlopen(req, timeout=120) as r, dest.open("wb") as f:
        while True:
            chunk = r.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)
    return fingerprint(dest)


def normalize_header(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def detect_delimiter(sample: str) -> str:
    try:
        return csv.Sniffer().sniff(sample, delimiters=",;\t|").delimiter
    except csv.Error:
        return ";" if sample.count(";") > sample.count(",") else ","


def read_text_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError(f"Could not decode {path}")
    delim = detect_delimiter(text[:10000])
    reader = csv.DictReader(io.StringIO(text), delimiter=delim)
    if not reader.fieldnames:
        raise ValueError(f"No header row detected in {path}")
    return list(reader.fieldnames), [dict(r) for r in reader]


def extract_zip_member(zip_path: Path, out_dir: Path, member_hint: str | None = None) -> Path:
    with zipfile.ZipFile(zip_path) as zf:
        names = [n for n in zf.namelist() if not n.endswith("/")]
        if not names:
            raise ValueError(f"ZIP has no files: {zip_path}")
        if member_hint:
            matched = [n for n in names if member_hint.lower() in n.lower()]
            if len(matched) == 1:
                name = matched[0]
            elif len(matched) > 1:
                raise ValueError(f"Ambiguous ZIP member hint {member_hint!r}: {matched}")
            else:
                raise ValueError(f"ZIP member hint {member_hint!r} not found; members={names}")
        elif len(names) == 1:
            name = names[0]
        else:
            candidates = [n for n in names if re.search(r"\.(csv|txt|tsv)$", n, re.I)]
            if len(candidates) != 1:
                raise ValueError(f"Multiple ZIP members; specify --prodcom-member. members={names}")
            name = candidates[0]
        out_dir.mkdir(parents=True, exist_ok=True)
        dest = out_dir / Path(name).name
        with zf.open(name) as src, dest.open("wb") as dst:
            dst.write(src.read())
        return dest


def pick_column(headers: Sequence[str], aliases: Sequence[str], label: str) -> str:
    norm_map = {normalize_header(h): h for h in headers}
    exact = []
    for alias in aliases:
        a = normalize_header(alias)
        if a in norm_map:
            exact.append(norm_map[a])
    exact = list(dict.fromkeys(exact))
    if len(exact) == 1:
        return exact[0]
    if len(exact) > 1:
        raise ValueError(f"Ambiguous {label} columns: {exact}")
    contains = []
    for h in headers:
        n = normalize_header(h)
        if any(normalize_header(a) in n for a in aliases):
            contains.append(h)
    contains = list(dict.fromkeys(contains))
    if len(contains) == 1:
        return contains[0]
    raise ValueError(f"Could not uniquely identify {label}. headers={headers}; candidates={contains}")


def to_float(v: str) -> float:
    s = (v or "").strip().replace(" ", "").replace("\u00a0", "")
    if s in {"", ":", "-", "na", "n/a", "NA", "N/A"}:
        raise ValueError("missing numeric value")
    if "," in s and "." not in s:
        s = s.replace(",", ".")
    else:
        s = s.replace(",", "")
    return float(s)


def canonical_activity(v: str) -> str:
    s = re.sub(r"\s+", "", (v or ""))
    for code in EPRTR_ACTIVITIES:
        if code.replace(" ", "") in s:
            return code
    return s


def canonical_prodcom(v: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", (v or "").upper())


def canonical_country(v: str) -> str:
    s = (v or "").strip().upper()
    name_to_iso = {
        "UNITED KINGDOM": "UK", "GREAT BRITAIN": "UK", "GREECE": "EL",
        "SERBIA": "RS", "ICELAND": "IS", "LIECHTENSTEIN": "LI", "NORWAY": "NO",
        "SWITZERLAND": "CH",
    }
    if s in name_to_iso:
        return name_to_iso[s]
    if len(s) == 2 and s.isalpha():
        return s
    return s


def eprtr_totals(csv_path: Path) -> dict[int, float]:
    headers, rows = read_text_rows(csv_path)
    year_col = pick_column(headers, ["reportingyear", "year", "referenceyear"], "E-PRTR year")
    act_col = pick_column(headers, ["annexiactivitycode", "eprtractivitycode", "activitycode"], "E-PRTR activity")
    pollutant_col = pick_column(headers, ["pollutantname", "pollutant", "pollutantcode"], "E-PRTR pollutant")
    value_col = pick_column(headers, ["totalrelease", "releasekg", "release", "quantity", "amount", "value"], "E-PRTR release value")
    country_col = pick_column(headers, ["countrycode", "country", "reportercountry", "countryid"], "E-PRTR country")
    try:
        unit_col = pick_column(headers, ["unit", "quantityunit", "releaseunit"], "E-PRTR unit")
    except ValueError:
        unit_col = None

    totals = {y: 0.0 for y in YEARS}
    matched = {y: 0 for y in YEARS}
    units: set[str] = set()
    for r in rows:
        try:
            y = int(float((r.get(year_col) or "").strip()))
        except ValueError:
            continue
        if y not in YEARS:
            continue
        if canonical_activity(r.get(act_col, "")) not in EPRTR_ACTIVITIES:
            continue
        pol = (r.get(pollutant_col) or "").lower()
        if not ("mercur" in pol or pol.strip() in {"hg", "hg and compounds", "hgandcompounds"}):
            continue
        country = canonical_country(r.get(country_col, ""))
        if country not in EEA33_ISO2:
            continue
        try:
            value = to_float(r.get(value_col, ""))
        except ValueError:
            continue
        totals[y] += value
        matched[y] += 1
        if unit_col and r.get(unit_col):
            units.add((r.get(unit_col) or "").strip())

    if any(matched[y] == 0 for y in YEARS):
        raise ValueError(f"No E-PRTR mercury rows found for one or more target years: matched={matched}")
    if units and not all("kg" in u.lower() for u in units):
        raise ValueError(f"E-PRTR units are not unambiguously kg/year: {sorted(units)}")
    return totals


def prodcom_totals(data_path: Path) -> tuple[dict[int, float], set[str]]:
    headers, rows = read_text_rows(data_path)
    year_col = pick_column(headers, ["period", "year", "refyear", "referenceyear"], "PRODCOM year")
    code_col = pick_column(headers, ["prccode", "prodcomcode", "prodcom", "productcode"], "PRODCOM code")
    value_col = pick_column(headers, ["aprodqnt", "productionquantity", "quantity", "value", "obsvalue"], "PRODCOM quantity")
    unit_col = pick_column(headers, ["qntunit", "quantityunit", "unit"], "PRODCOM quantity unit")
    country_col = pick_column(headers, ["decl", "reporter", "countrycode", "geo", "country"], "PRODCOM reporter")

    totals = {y: 0.0 for y in YEARS}
    matched_codes = {y: set() for y in YEARS}
    units: set[str] = set()
    for r in rows:
        try:
            y = int(float((r.get(year_col) or "").strip()))
        except ValueError:
            continue
        if y not in YEARS:
            continue
        code = canonical_prodcom(r.get(code_col, ""))
        if code not in PRODCOM_CODES:
            continue
        reporter = canonical_country(r.get(country_col, ""))
        if reporter not in EEA33_ISO2:
            continue
        try:
            value = to_float(r.get(value_col, ""))
        except ValueError:
            continue
        unit = (r.get(unit_col) or "").strip()
        if not unit:
            raise ValueError(f"Missing QNTUNIT for target row: {r}")
        totals[y] += value
        matched_codes[y].add(code)
        units.add(unit)

    missing = {y: sorted(PRODCOM_CODES - matched_codes[y]) for y in YEARS}
    if any(missing[y] for y in YEARS):
        raise ValueError(f"Target PRODCOM codes not all observed in each target year: {missing}")
    if len(units) != 1:
        raise ValueError(f"Target rows do not have a single consistent QNTUNIT: {sorted(units)}")
    return totals, units


def compute(hg_kg: Mapping[int, float], steel_qty: Mapping[int, float], unit: str) -> dict[str, object]:
    if any(steel_qty[y] <= 0 for y in YEARS):
        raise ValueError(f"Non-positive steel denominator: {steel_qty}")
    intensity = {y: hg_kg[y] / steel_qty[y] for y in YEARS}
    change = (intensity[2017] / intensity[2008] - 1.0) * 100.0
    gate = "PASS" if PASS_MIN_PCT <= change <= PASS_MAX_PCT else "FAIL_OUTSIDE_GATE"
    return {
        "eprtr_mercury_kg": dict(hg_kg),
        "prodcom_steel_quantity": dict(steel_qty),
        "prodcom_qntunit": unit,
        "raw_intensity_kg_per_qntunit": intensity,
        "change_2008_2017_pct": change,
        "reference_pct": TARGET_REFERENCE_PCT,
        "gate": gate,
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Reproduce EEA steel-mercury intensity change from raw inputs.")
    p.add_argument("--eprtr", type=Path, help="Local E-PRTR activity-level air-release CSV")
    p.add_argument("--prodcom", type=Path, help="Local PRODCOM total-production CSV/TXT or ZIP")
    p.add_argument("--prodcom-member", help="ZIP member hint if PRODCOM ZIP has multiple files")
    p.add_argument("--eprtr-url", help="Official E-PRTR CSV URL to download")
    p.add_argument("--prodcom-url", help="Official PRODCOM ZIP/CSV URL to download")
    p.add_argument("--workdir", type=Path, default=Path("data/raw/EU-STEEL-R01"))
    p.add_argument("--inspect", action="store_true", help="Only print fingerprints/headers; do not calculate")
    p.add_argument("--output", type=Path, default=Path("research/EU-STEEL-R01/reproduction_result.json"))
    args = p.parse_args()

    args.workdir.mkdir(parents=True, exist_ok=True)
    eprtr = args.eprtr
    prodcom = args.prodcom
    if args.eprtr_url:
        eprtr = args.workdir / "eprtr_raw.csv"
        a = download(args.eprtr_url, eprtr)
        print(json.dumps({"downloaded_eprtr": a.__dict__ | {"path": str(a.path)}}, ensure_ascii=False))
    if args.prodcom_url:
        suffix = ".zip" if ".zip" in args.prodcom_url.lower() else ".csv"
        prodcom = args.workdir / f"prodcom_raw{suffix}"
        a = download(args.prodcom_url, prodcom)
        print(json.dumps({"downloaded_prodcom": a.__dict__ | {"path": str(a.path)}}, ensure_ascii=False))

    if not eprtr or not prodcom:
        p.error("Provide --eprtr/--eprtr-url and --prodcom/--prodcom-url")
    if not eprtr.exists() or not prodcom.exists():
        raise FileNotFoundError(f"Missing input: eprtr={eprtr}, prodcom={prodcom}")

    eprtr_art = fingerprint(eprtr)
    prodcom_art = fingerprint(prodcom)
    if zipfile.is_zipfile(prodcom):
        prodcom_data = extract_zip_member(prodcom, args.workdir / "extracted", args.prodcom_member)
    else:
        prodcom_data = prodcom

    eh, _ = read_text_rows(eprtr)
    ph, _ = read_text_rows(prodcom_data)
    manifest = {
        "eprtr": {"path": str(eprtr_art.path), "sha256": eprtr_art.sha256, "size": eprtr_art.size, "headers": eh},
        "prodcom": {"path": str(prodcom_art.path), "sha256": prodcom_art.sha256, "size": prodcom_art.size, "data_path": str(prodcom_data), "headers": ph},
        "frozen_crosswalk": {
            "years": YEARS,
            "eprtr_activities": sorted(EPRTR_ACTIVITIES),
            "prodcom_codes": sorted(PRODCOM_CODES),
            "eea33_iso2": sorted(EEA33_ISO2),
            "pass_gate_pct": [PASS_MIN_PCT, PASS_MAX_PCT],
        },
    }
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    if args.inspect:
        return 0

    hg = eprtr_totals(eprtr)
    steel, units = prodcom_totals(prodcom_data)
    unit = next(iter(units))
    result = manifest | {"result": compute(hg, steel, unit)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result["result"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
