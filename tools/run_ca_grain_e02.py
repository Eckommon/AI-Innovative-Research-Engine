#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import re
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "CA-GRAIN-E02"
OUT.mkdir(parents=True, exist_ok=True)

TC_URL = "https://tdih-cdit.tc.canada.ca/sites/default/files/ferroviaire-rail.zip"
GSW_URLS = {
    "2023-24": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2023-24/gsw-shg-en.csv",
    "2024-25": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2024-25/gsw-shg-en.csv",
}
START = date(2023, 8, 1)
END = date(2025, 7, 31)
UA = "AI-Innovative-Research-Engine/CA-GRAIN-E02 preregistered relationship runner"

GRAINS = (
    "Amber Durum", "Barley", "Beans", "Canaryseed", "Canola", "Chick Peas",
    "Corn", "Flaxseed", "Lentils", "Mustard Seed", "Oats", "Peas", "Rye",
    "Soybeans", "Wheat",
)
REGIONS = ("Alberta", "British Columbia", "Manitoba", "Saskatchewan")
CARRIERS = ("CN", "CPKC")
EXPECTED_COMPONENTS = {(g, r) for g in GRAINS for r in REGIONS}
MIN_N = 75
HAC_LAG = 2
MATERIALITY = 1.0


def fetch(url: str) -> tuple[bytes, dict]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=120) as r:
        b = r.read()
        return b, {
            "requested_url": url,
            "final_url": r.geturl(),
            "status": getattr(r, "status", 200),
            "bytes": len(b),
            "sha256": hashlib.sha256(b).hexdigest(),
            "content_type": r.headers.get("Content-Type"),
        }


def decode(b: bytes) -> str:
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    raise RuntimeError("cannot decode source text")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip()).casefold()


def hnorm(s: str) -> str:
    return re.sub(r"[_\-\s]+", " ", (s or "").strip()).casefold()


def exact_header(headers: list[str], *names: str) -> str | None:
    lookup = {hnorm(h): h for h in headers}
    for name in names:
        hit = lookup.get(hnorm(name))
        if hit is not None:
            return hit
    return None


def date_from_text(s: str):
    s = (s or "").strip()
    if re.match(r"^20\d\d-\d\d-\d\d", s):
        s = s[:10]
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def week_monday(d: date) -> date:
    return d - timedelta(days=d.weekday())


def parse_number(raw: str) -> float:
    s = (raw or "").strip().replace(",", "")
    if not s:
        raise ValueError("blank numeric source value")
    x = float(s)
    if not math.isfinite(x):
        raise ValueError("non-finite numeric source value")
    return x


def inv2(a: float, b: float, c: float, d: float) -> tuple[tuple[float, float], tuple[float, float]]:
    det = a * d - b * c
    if abs(det) < 1e-15:
        raise RuntimeError("singular 2x2 matrix")
    return ((d / det, -b / det), (-c / det, a / det))


def mat2mul(A, B):
    return (
        (A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]),
        (A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]),
    )


def fit_hac(x: list[float], y: list[float], lag: int = 2) -> dict:
    n = len(x)
    if n < 3 or len(y) != n:
        raise RuntimeError("insufficient observations for OLS")
    sx = sum(x)
    sy = sum(y)
    sxx = sum(v*v for v in x)
    sxy = sum(a*b for a, b in zip(x, y))
    XtX = ((float(n), sx), (sx, sxx))
    inv = inv2(*XtX[0], *XtX[1])
    alpha = inv[0][0]*sy + inv[0][1]*sxy
    beta = inv[1][0]*sy + inv[1][1]*sxy
    u = [yy - alpha - beta*xx for xx, yy in zip(x, y)]
    z = [(1.0, xx) for xx in x]

    S00 = S01 = S10 = S11 = 0.0
    for t in range(n):
        uu = u[t]*u[t]
        z0, z1 = z[t]
        S00 += uu*z0*z0
        S01 += uu*z0*z1
        S10 += uu*z1*z0
        S11 += uu*z1*z1
    for ell in range(1, lag + 1):
        w = 1.0 - ell/(lag + 1.0)
        for t in range(ell, n):
            q = w*u[t]*u[t-ell]
            a0, a1 = z[t]
            b0, b1 = z[t-ell]
            S00 += q*(a0*b0 + b0*a0)
            S01 += q*(a0*b1 + b0*a1)
            S10 += q*(a1*b0 + b1*a0)
            S11 += q*(a1*b1 + b1*a1)
    S = ((S00, S01), (S10, S11))
    cov = mat2mul(mat2mul(inv, S), inv)
    fsc = n/(n-2.0)
    cov = tuple(tuple(v*fsc for v in row) for row in cov)
    var_beta = cov[1][1]
    if var_beta < -1e-12:
        raise RuntimeError("negative HAC variance")
    se = math.sqrt(max(var_beta, 0.0))
    if se == 0:
        zstat = math.inf if beta != 0 else 0.0
        p = 0.0 if beta != 0 else 1.0
    else:
        zstat = beta/se
        p = math.erfc(abs(zstat)/math.sqrt(2.0))
    lo = beta - 1.96*se
    hi = beta + 1.96*se
    return {
        "n": n,
        "alpha": alpha,
        "beta": beta,
        "se_hac_lag2_fsc": se,
        "z": zstat,
        "p_two_sided_normal": p,
        "ci95_normal": [lo, hi],
        "hac_lag": lag,
        "finite_sample_multiplier": fsc,
    }


provenance: dict = {"gsw": {}, "transport_canada": {}}
structural: dict = {
    "frozen_grain_count": len(GRAINS),
    "frozen_region_count": len(REGIONS),
    "expected_components_per_week": len(EXPECTED_COMPONENTS),
    "gsw_source_weeks": 0,
    "gsw_complete_weeks": 0,
    "gsw_incomplete_weeks": [],
    "gsw_duplicate_component_weeks": [],
    "tc_carrier_week_counts": {},
    "tc_complete_two_carrier_weeks": 0,
    "tc_units": [],
    "final_model_observations": 0,
}

# ---- GSW frozen exposure ----
# Values become readable only after DEC-153 / Issue #110 authorization.
# Raw rows are never persisted.
week_components: dict[date, dict[tuple[str, str], float]] = defaultdict(dict)
week_key_counts: dict[date, Counter] = defaultdict(Counter)
source_weeks: set[date] = set()

for crop, url in GSW_URLS.items():
    b, meta = fetch(url)
    provenance["gsw"][crop] = meta
    reader = csv.DictReader(io.StringIO(decode(b)))
    headers = reader.fieldnames or []
    hm = {
        "date": exact_header(headers, "week_ending_date", "Week Ending Date"),
        "worksheet": exact_header(headers, "worksheet"),
        "metric": exact_header(headers, "metric"),
        "period": exact_header(headers, "period"),
        "grain": exact_header(headers, "grain"),
        "grade": exact_header(headers, "grade"),
        "region": exact_header(headers, "region"),
        "value": exact_header(headers, "Ktonnes"),
    }
    if not all(hm.values()):
        raise RuntimeError(f"GSW schema mismatch for {crop}: {hm}")

    for row in reader:
        if norm(row.get(hm["worksheet"], "")) != norm("Primary"):
            continue
        if norm(row.get(hm["metric"], "")) != norm("Deliveries"):
            continue
        if norm(row.get(hm["period"], "")) != norm("Current Week"):
            continue
        if (row.get(hm["grade"], "") or "").strip() != "":
            continue
        d = date_from_text(row.get(hm["date"], ""))
        if not d or not (START <= d <= END):
            continue
        grain = (row.get(hm["grain"], "") or "").strip()
        region = (row.get(hm["region"], "") or "").strip()
        if grain not in GRAINS or region not in REGIONS:
            continue
        wk = week_monday(d)
        source_weeks.add(wk)
        key = (grain, region)
        week_key_counts[wk][key] += 1
        # Preregistered numeric exposure is now opened.
        val = parse_number(row.get(hm["value"], ""))
        if key not in week_components[wk]:
            week_components[wk][key] = val

structural["gsw_source_weeks"] = len(source_weeks)
for wk in sorted(source_weeks):
    counts = week_key_counts[wk]
    duplicates = sorted([f"{g}|{r}" for (g, r), c in counts.items() if c != 1])
    missing = sorted([f"{g}|{r}" for g, r in EXPECTED_COMPONENTS if counts.get((g, r), 0) == 0])
    extras = sorted([f"{g}|{r}" for (g, r) in counts if (g, r) not in EXPECTED_COMPONENTS])
    if duplicates:
        structural["gsw_duplicate_component_weeks"].append({"week": wk.isoformat(), "keys": duplicates})
    if missing or extras or len(counts) != len(EXPECTED_COMPONENTS):
        structural["gsw_incomplete_weeks"].append({
            "week": wk.isoformat(),
            "missing_count": len(missing),
            "extra_count": len(extras),
            "observed_component_count": len(counts),
        })

structural_fail = bool(structural["gsw_duplicate_component_weeks"] or structural["gsw_incomplete_weeks"])
P: dict[date, float] = {}
if not structural_fail:
    for wk in sorted(source_weeks):
        P[wk] = sum(week_components[wk][key] for key in EXPECTED_COMPONENTS)
    structural["gsw_complete_weeks"] = len(P)

# ---- Transport Canada frozen outcome ----
tc_bytes, tc_meta = fetch(TC_URL)
provenance["transport_canada"] = tc_meta
carrier_values: dict[str, dict[date, float]] = {c: {} for c in CARRIERS}
carrier_counts: dict[tuple[str, date], int] = Counter()
tc_units: set[str] = set()

with zipfile.ZipFile(io.BytesIO(tc_bytes)) as z:
    members = [n for n in z.namelist() if n.lower().endswith(".csv")]
    selected = []
    for year in (2023, 2024, 2025):
        pat = re.compile(rf"(^|/)weekly_rail_system_performance_indicators_eng_{year}\.csv$", re.I)
        hits = [n for n in members if pat.search(n)]
        if len(hits) != 1:
            raise RuntimeError(f"expected exactly one English TC file for {year}: {hits}")
        selected.append(hits[0])
    provenance["transport_canada"]["selected_members"] = selected

    for member in selected:
        reader = csv.DictReader(io.StringIO(decode(z.read(member))))
        headers = reader.fieldnames or []
        hm = {
            "date": exact_header(headers, "Reference_Date", "Reference Date"),
            "carrier": exact_header(headers, "Carrier"),
            "measure": exact_header(headers, "Measure"),
            "unit": exact_header(headers, "Unit_of_Measure", "Unit of Measure"),
            "geography": exact_header(headers, "Geography"),
            "commodity": exact_header(headers, "Commodity"),
            "value": exact_header(headers, "Measure_Value", "Measure Value"),
        }
        if not all(hm.values()):
            raise RuntimeError(f"TC schema mismatch: {hm}")
        for row in reader:
            if norm(row.get(hm["commodity"], "")) != norm("All Western grain"):
                continue
            if norm(row.get(hm["measure"], "")) != norm("Average Dwell Time at Origin"):
                continue
            if norm(row.get(hm["geography"], "")) != norm("Canada"):
                continue
            carrier = (row.get(hm["carrier"], "") or "").strip()
            if carrier not in CARRIERS:
                continue
            d = date_from_text(row.get(hm["date"], ""))
            if not d or not (START <= d <= END):
                continue
            wk = week_monday(d)
            carrier_counts[(carrier, wk)] += 1
            unit = (row.get(hm["unit"], "") or "").strip()
            if unit:
                tc_units.add(unit)
            val = parse_number(row.get(hm["value"], ""))
            if carrier_counts[(carrier, wk)] == 1:
                carrier_values[carrier][wk] = val

structural["tc_units"] = sorted(tc_units)
structural["tc_carrier_week_counts"] = {c: len(carrier_values[c]) for c in CARRIERS}
tc_duplicates = [
    {"carrier": c, "week": wk.isoformat(), "count": n}
    for (c, wk), n in sorted(carrier_counts.items(), key=lambda kv: (kv[0][1], kv[0][0])) if n != 1
]
structural["tc_duplicate_carrier_weeks"] = tc_duplicates
unit_ok = len(tc_units) == 1 and norm(next(iter(tc_units), "")) in {"hour", "hours"}
if tc_duplicates or not unit_ok:
    structural_fail = True

D: dict[date, float] = {}
if not structural_fail:
    both = sorted(set(carrier_values["CN"]) & set(carrier_values["CPKC"]))
    for wk in both:
        D[wk] = (carrier_values["CN"][wk] + carrier_values["CPKC"][wk]) / 2.0
    structural["tc_complete_two_carrier_weeks"] = len(D)

# ---- Strictly consecutive preregistered model rows ----
model_dates: list[date] = []
x: list[float] = []
y: list[float] = []
if not structural_fail:
    for t in sorted(D):
        t1 = t - timedelta(days=7)
        t2 = t - timedelta(days=14)
        if t1 not in D or t1 not in P or t2 not in P:
            continue
        # These dictionary keys are normalized Mondays, so 7-day arithmetic enforces strict chains.
        model_dates.append(t)
        x.append((P[t1] - P[t2]) / 100.0)
        y.append(D[t] - D[t1])

structural["final_model_observations"] = len(model_dates)
structural["first_model_week"] = model_dates[0].isoformat() if model_dates else None
structural["last_model_week"] = model_dates[-1].isoformat() if model_dates else None

if structural_fail or len(model_dates) < MIN_N:
    gate = "HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL"
    primary = None
    diagnostics = None
else:
    primary = fit_hac(x, y, HAC_LAG)
    beta = primary["beta"]
    lo, hi = primary["ci95_normal"]
    if beta >= MATERIALITY and lo > 0:
        gate = "PASS_POSITIVE_MATERIAL_CA_GRAIN_E02_RELATIONSHIP"
    elif 0 < beta < MATERIALITY and lo > 0:
        gate = "POSITIVE_BELOW_MATERIALITY_CA_GRAIN_E02_RELATIONSHIP"
    else:
        gate = "NO_PREREGISTERED_POSITIVE_CA_GRAIN_E02_RELATIONSHIP"
    primary.update({
        "x_scale": "+100 Ktonnes weekly change in Primary deliveries at t-1",
        "y_unit": "hours weekly change in equal-weight CN/CPKC origin dwell at t",
        "materiality_floor_beta": MATERIALITY,
        "signed_hypothesis": "beta > 0",
        "gate": gate,
    })

    diagnostics = {}
    for carrier in CARRIERS:
        yc = [carrier_values[carrier][t] - carrier_values[carrier][t - timedelta(days=7)] for t in model_dates]
        diagnostics[carrier] = fit_hac(x, yc, HAC_LAG)
        diagnostics[carrier]["non_rescuing"] = True

payload = {
    "id": "CA-GRAIN-E02-STAGE-B-PRIMARY",
    "issue": 110,
    "preregistration": {
        "exposure": "GSW Primary / Deliveries / Current Week; exact 15 grains x 4 western regions; blank grade",
        "outcome": "TC All Western grain / Average Dwell Time at Origin / Canada; equal-weight CN+CPKC",
        "lag_weeks": 1,
        "transform": "weekly first differences",
        "min_n": MIN_N,
        "model": "OLS intercept",
        "covariance": "Newey-West HAC lag 2 with n/(n-2) finite-sample multiplier",
        "materiality_floor_hours_per_100_ktonnes": MATERIALITY,
        "causal_claim": False,
    },
    "provenance": provenance,
    "structural_gate": structural,
    "primary": primary,
    "diagnostics": diagnostics,
    "gate": gate,
    "raw_source_bytes_persisted": False,
    "incremental_monetary_cost_usd": 0,
}
(OUT / "STAGE_B_PRIMARY_RESULT.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

if primary is None:
    summary = f"""---
id: CA-GRAIN-E02-RESULT
type: preregistered-relationship-test
issue: 110
gate: {gate}
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-E02 Result

**`{gate}`**

The preregistered structural/data-completeness gate failed before model fitting.

- GSW source weeks: **{structural['gsw_source_weeks']}**; complete weeks: **{structural['gsw_complete_weeks']}**.
- GSW incomplete weeks: **{len(structural['gsw_incomplete_weeks'])}**; duplicate-component weeks: **{len(structural['gsw_duplicate_component_weeks'])}**.
- TC carrier weeks: CN **{structural['tc_carrier_week_counts'].get('CN', 0)}**, CPKC **{structural['tc_carrier_week_counts'].get('CPKC', 0)}**.
- Final eligible model observations: **{structural['final_model_observations']}** (required >= {MIN_N}).
- No relationship model was fitted. Raw source bytes were not persisted. Cost = **0 USD**.
"""
else:
    lo, hi = primary["ci95_normal"]
    summary = f"""---
id: CA-GRAIN-E02-RESULT
type: preregistered-relationship-test
issue: 110
gate: {gate}
relationship_computed: true
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-E02 Result

**`{gate}`**

Preregistered primary model completed with **N={primary['n']}** weekly observations.

- beta: **{primary['beta']:.9f} hours per +100 Ktonnes**
- HAC(2) SE with frozen finite-sample multiplier: **{primary['se_hac_lag2_fsc']:.9f}**
- 95% CI: **[{lo:.9f}, {hi:.9f}]**
- two-sided normal p: **{primary['p_two_sided_normal']:.9g}**
- materiality floor: **+{MATERIALITY:.1f} hour per +100 Ktonnes**
- model window: **{structural['first_model_week']} through {structural['last_model_week']}**

This is a preregistered **association/predictive bottleneck test**, not a causal estimate. Carrier-specific results are diagnostics only and cannot rescue the primary gate. Raw source bytes were not persisted. Cost = **0 USD**.
"""
(OUT / "RESULT.md").write_text(summary, encoding="utf-8")

print(json.dumps({
    "gate": gate,
    "n": structural["final_model_observations"],
    "beta": None if primary is None else primary["beta"],
    "ci95": None if primary is None else primary["ci95_normal"],
    "p": None if primary is None else primary["p_two_sided_normal"],
    "cost_usd": 0,
}))
