#!/usr/bin/env python3
"""US-AIR-E01 Stage B: frozen precipitation-delay relationship test."""

from __future__ import annotations

import csv
import hashlib
import io
import math
import re
import tempfile
import time
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import numpy as np
from scipy import stats

YEAR = 2025
MIN_AIRPORTS = 100
MIN_ROWS = 30000
FE_TOL = 1e-12
FE_MAX_ITER = 1000
UA = "AI-Innovative-Research-Engine/US-AIR-E01-stage-b"

ROOT = Path(__file__).resolve().parents[1]
F01 = ROOT / "research" / "US-AIR-F01"
E01 = ROOT / "research" / "US-AIR-E01"

F01_SUPPORT = F01 / "FULL_YEAR_DATE_SUPPORT.md"
WEATHER_PANEL = E01 / "STAGE_A_AIRPORT_DATE_WEATHER.csv"

SOURCE_MANIFEST = E01 / "STAGE_B_BTS_SOURCE_MANIFEST.csv"
PANEL_CSV = E01 / "STAGE_B_AIRPORT_DAY_PANEL.csv"
PRIMARY_CSV = E01 / "STAGE_B_PRIMARY_RESULT.csv"
SENSITIVITY_CSV = E01 / "STAGE_B_SENSITIVITY_RESULT.csv"
RESULT_MD = E01 / "STAGE_B_RESULT.md"

BTS_BASE = "https://transtats.bts.gov/PREZIP"


def bts_url(month: int) -> str:
    filename = (
        "On_Time_Marketing_Carrier_On_Time_Performance_"
        f"Beginning_January_2018_{YEAR}_{month}.zip"
    )
    return f"{BTS_BASE}/{filename}"


def load_expected_hashes() -> dict[int, dict[str, object]]:
    text = F01_SUPPORT.read_text(encoding="utf-8")
    expected: dict[int, dict[str, object]] = {}
    pattern = re.compile(
        r"^\|\s*(\d{1,2})\s*\|\s*(\d+)\s*\|\s*([0-9a-f]{64})\s*\|",
        re.MULTILINE,
    )
    for match in pattern.finditer(text):
        month = int(match.group(1))
        if 1 <= month <= 12:
            expected[month] = {
                "bytes": int(match.group(2)),
                "sha256": match.group(3),
            }
    if sorted(expected) != list(range(1, 13)):
        raise RuntimeError(f"Expected 12 frozen BTS hashes, found months={sorted(expected)}")
    return expected


def download_to_path(url: str, path: Path, attempts: int = 3) -> dict[str, object]:
    last = None
    for attempt in range(attempts):
        try:
            digest = hashlib.sha256()
            total = 0
            request = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(request, timeout=240) as response, path.open("wb") as out:
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    out.write(chunk)
                    digest.update(chunk)
                    total += len(chunk)
                status = getattr(response, "status", 200)
                final_url = response.geturl()
            return {
                "http": status,
                "final_url": final_url,
                "bytes": total,
                "sha256": digest.hexdigest(),
                "error": "",
            }
        except Exception as exc:
            last = exc
            if path.exists():
                path.unlink()
            if attempt + 1 < attempts:
                time.sleep(2 * (attempt + 1))
    return {
        "http": "ERROR",
        "final_url": "",
        "bytes": 0,
        "sha256": "",
        "error": f"{type(last).__name__}:{last}",
    }


def write_source_manifest(rows: list[dict[str, object]]) -> None:
    fields = [
        "month", "url", "expected_bytes", "actual_bytes",
        "expected_sha256", "actual_sha256", "hash_match",
        "http", "final_url", "error",
    ]
    with SOURCE_MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_hold(reason: str, source_rows: list[dict[str, object]], details: str) -> None:
    matched = sum(str(r["hash_match"]) == "True" for r in source_rows)
    lines = [
        "---",
        "id: US-AIR-E01-STAGE-B-RESULT",
        "type: preregistered-primary-relationship-result",
        "created: 2026-09-10",
        "issue: 90",
        "gate: HOLD_US_AIR_E01_SOURCE_OR_PANEL_SUPPORT",
        f"hold_reason: {reason}",
        "incremental_monetary_cost_usd: 0",
        "---",
        "",
        "# US-AIR-E01 Stage B Result",
        "# US-AIR-E01 Stage B 결과",
        "",
        "## Gate / 판정",
        "",
        "**HOLD_US_AIR_E01_SOURCE_OR_PANEL_SUPPORT**",
        "",
        f"Reason / 사유: **{reason}**",
        "",
        details,
        "",
        f"- frozen BTS ZIP hashes matched: **{matched}/12**",
        "",
        "No alternate weather variable, outcome, period or source is substituted.",
        "",
        "Incremental monetary cost remains **0 USD**.",
    ]
    RESULT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_weather_panel() -> dict[tuple[str, str], dict[str, object]]:
    panel: dict[tuple[str, str], dict[str, object]] = {}
    with WEATHER_PANEL.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {
            "airport_id", "date", "daily_precipitation_mm", "trace_flag",
            "usable_primary", "stage_a_airport_qualified",
        }
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise RuntimeError(f"Stage-A weather panel missing columns: {sorted(missing)}")
        for row in reader:
            if row["stage_a_airport_qualified"].strip().lower() != "true":
                continue
            if row["usable_primary"].strip().lower() != "true":
                continue
            key = (row["airport_id"].strip(), row["date"].strip())
            if key in panel:
                raise RuntimeError(f"Duplicate Stage-A airport-date key: {key}")
            precip = float(row["daily_precipitation_mm"])
            if not math.isfinite(precip) or precip < 0:
                raise RuntimeError(f"Invalid frozen precipitation for {key}: {precip}")
            panel[key] = {
                "precip_mm": precip,
                "trace": row["trace_flag"].strip().lower() == "true",
                "station_id": row.get("station_id", "").strip(),
            }
    return panel


TRUE_FLAGS = {"1", "1.0", "1.00", "Y", "YES", "TRUE"}


def is_true(value: str) -> bool:
    return str(value).strip().upper() in TRUE_FLAGS


def parse_bts_after_hash_pass(
    zip_paths: dict[int, Path],
    weather_keys: set[tuple[str, str]],
) -> tuple[dict[tuple[str, str], dict[str, float]], dict[str, object]]:
    agg = defaultdict(lambda: {
        "n_sched": 0,
        "delay_sum": 0.0,
        "delay_n": 0,
        "delay_nondiv_sum": 0.0,
        "delay_nondiv_n": 0,
    })
    source_rows = 0
    relevant_rows = 0
    negative_delay_rows = 0
    nonfinite_delay_rows = 0
    header_ref = None
    header_consistent = True

    required = [
        "FlightDate", "OriginAirportID", "Duplicate",
        "Cancelled", "Diverted", "DepDelayMinutes",
    ]

    for month in range(1, 13):
        with zipfile.ZipFile(zip_paths[month]) as archive:
            members = [
                name for name in archive.namelist()
                if name.lower().endswith(".csv")
                and "readme" not in name.lower()
            ]
            if not members:
                raise RuntimeError(f"No BTS CSV in month {month}")
            member = max(members, key=lambda name: archive.getinfo(name).file_size)
            with archive.open(member) as raw:
                text = io.TextIOWrapper(
                    raw, encoding="utf-8-sig", newline="", errors="replace"
                )
                reader = csv.reader(text)
                header = next(reader)
                if header_ref is None:
                    header_ref = header
                elif header != header_ref:
                    header_consistent = False
                hmap = {str(name).strip(): i for i, name in enumerate(header)}
                missing = [name for name in required if name not in hmap]
                if missing:
                    raise RuntimeError(f"BTS month {month} missing columns {missing}")
                idx = {name: hmap[name] for name in required}
                max_idx = max(idx.values())

                for row in reader:
                    source_rows += 1
                    if len(row) <= max_idx:
                        continue
                    key = (
                        row[idx["OriginAirportID"]].strip(),
                        row[idx["FlightDate"]].strip(),
                    )
                    if key not in weather_keys:
                        continue
                    relevant_rows += 1

                    duplicate = is_true(row[idx["Duplicate"]])
                    if duplicate:
                        continue

                    rec = agg[key]
                    rec["n_sched"] += 1

                    cancelled = is_true(row[idx["Cancelled"]])
                    if cancelled:
                        continue

                    delay_raw = row[idx["DepDelayMinutes"]].strip()
                    if delay_raw == "":
                        continue
                    try:
                        delay = float(delay_raw)
                    except ValueError:
                        nonfinite_delay_rows += 1
                        continue
                    if not math.isfinite(delay):
                        nonfinite_delay_rows += 1
                        continue
                    if delay < 0:
                        negative_delay_rows += 1
                        continue

                    rec["delay_sum"] += delay
                    rec["delay_n"] += 1

                    diverted = is_true(row[idx["Diverted"]])
                    if not diverted:
                        rec["delay_nondiv_sum"] += delay
                        rec["delay_nondiv_n"] += 1

    diagnostics = {
        "source_rows": source_rows,
        "relevant_rows": relevant_rows,
        "negative_delay_rows": negative_delay_rows,
        "nonfinite_delay_rows": nonfinite_delay_rows,
        "header_consistent": header_consistent,
    }
    return agg, diagnostics


def group_codes(values: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    levels, inverse = np.unique(values, return_inverse=True)
    return levels, inverse


def subtract_group_means(matrix: np.ndarray, inverse: np.ndarray, groups: int) -> None:
    counts = np.bincount(inverse, minlength=groups).astype(float)
    for col in range(matrix.shape[1]):
        sums = np.bincount(inverse, weights=matrix[:, col], minlength=groups)
        means = sums / counts
        matrix[:, col] -= means[inverse]


def absorb_two_way(
    matrix: np.ndarray,
    airport_inv: np.ndarray,
    date_inv: np.ndarray,
    n_airports: int,
    n_dates: int,
) -> tuple[np.ndarray, int, float]:
    transformed = matrix.astype(float, copy=True)
    last_change = math.inf
    for iteration in range(1, FE_MAX_ITER + 1):
        before = transformed.copy()
        subtract_group_means(transformed, airport_inv, n_airports)
        subtract_group_means(transformed, date_inv, n_dates)
        last_change = float(np.max(np.abs(transformed - before)))
        if last_change < FE_TOL:
            return transformed, iteration, last_change
    raise RuntimeError(
        f"FE_NONCONVERGENCE iterations={FE_MAX_ITER} last_change={last_change}"
    )


def ols(y: np.ndarray, x: np.ndarray) -> tuple[np.ndarray, np.ndarray, int, float]:
    rank = int(np.linalg.matrix_rank(x))
    if rank != x.shape[1]:
        raise RuntimeError(f"RANK_DEFICIENT rank={rank} columns={x.shape[1]}")
    xtx = x.T @ x
    beta = np.linalg.solve(xtx, x.T @ y)
    if not np.all(np.isfinite(beta)):
        raise RuntimeError("NONFINITE_COEFFICIENT")
    residual = y - x @ beta
    rmse = float(np.sqrt(np.mean(residual ** 2)))
    return beta, residual, rank, rmse


def cluster_meat(x: np.ndarray, u: np.ndarray, labels: np.ndarray):
    levels, inverse = np.unique(labels, return_inverse=True)
    g = len(levels)
    scores = np.zeros((g, x.shape[1]), dtype=float)
    np.add.at(scores, inverse, x * u[:, None])
    return scores.T @ scores, g


def cr1_factor(n: int, k: int, g: int) -> float:
    if g <= 1 or n <= k:
        raise RuntimeError(f"INVALID_CR1_DIMENSION N={n} K={k} G={g}")
    return (g / (g - 1.0)) * ((n - 1.0) / (n - k))


def two_way_covariance(
    x: np.ndarray,
    u: np.ndarray,
    first_labels: np.ndarray,
    second_labels: np.ndarray,
    k_total: int,
) -> tuple[np.ndarray, dict[str, int]]:
    n = len(u)
    bread = np.linalg.inv(x.T @ x)

    meat_1, g1 = cluster_meat(x, u, first_labels)
    meat_2, g2 = cluster_meat(x, u, second_labels)
    intersection = np.char.add(
        np.char.add(first_labels.astype(str), "|"),
        second_labels.astype(str),
    )
    meat_i, gi = cluster_meat(x, u, intersection)

    combined_meat = (
        cr1_factor(n, k_total, g1) * meat_1
        + cr1_factor(n, k_total, g2) * meat_2
        - cr1_factor(n, k_total, gi) * meat_i
    )
    covariance = bread @ combined_meat @ bread
    return covariance, {"g_first": g1, "g_second": g2, "g_intersection": gi}


def fit_model(rows: list[dict[str, object]], trace_override: float | None = None):
    airports = np.array([str(r["airport_id"]) for r in rows], dtype=str)
    dates = np.array([str(r["date"]) for r in rows], dtype=str)
    y = np.array([float(r["y_delay"]) for r in rows], dtype=float)
    volume = np.log1p(np.array([float(r["n_sched"]) for r in rows], dtype=float))

    precip_values = []
    for row in rows:
        p = float(row["precip_mm"])
        if trace_override is not None and bool(row["trace"]):
            p = trace_override
        precip_values.append(p)
    precip = np.log1p(np.array(precip_values, dtype=float))

    airport_levels, airport_inv = group_codes(airports)
    date_levels, date_inv = group_codes(dates)

    matrix = np.column_stack([y, volume, precip])
    transformed, iterations, last_change = absorb_two_way(
        matrix, airport_inv, date_inv, len(airport_levels), len(date_levels)
    )
    yt = transformed[:, 0]
    vt = transformed[:, 1]
    xt = transformed[:, 2]

    baseline_x = vt[:, None]
    baseline_beta, baseline_u, baseline_rank, baseline_rmse = ols(yt, baseline_x)

    weather_x = np.column_stack([vt, xt])
    beta, residual, rank, weather_rmse = ols(yt, weather_x)

    n = len(rows)
    a = len(airport_levels)
    d = len(date_levels)
    k_total = a + d + 1

    covariance, clusters = two_way_covariance(
        weather_x, residual, airports, dates, k_total
    )
    variance = float(covariance[1, 1])
    if not math.isfinite(variance) or variance <= 0:
        raise RuntimeError(f"INVALID_PRECIP_VARIANCE {variance}")

    se = math.sqrt(variance)
    precip_beta = float(beta[1])
    t_stat = precip_beta / se
    df = min(clusters["g_first"] - 1, clusters["g_second"] - 1)
    critical = float(stats.t.ppf(0.975, df))
    p_value = float(2 * stats.t.sf(abs(t_stat), df))
    ci_low = precip_beta - critical * se
    ci_high = precip_beta + critical * se
    delta_10 = precip_beta * math.log(11.0)

    return {
        "n": n,
        "airports": a,
        "dates": d,
        "k_total": k_total,
        "fe_iterations": iterations,
        "fe_last_change": last_change,
        "baseline_gamma": float(baseline_beta[0]),
        "baseline_rank": baseline_rank,
        "baseline_rmse": baseline_rmse,
        "volume_gamma": float(beta[0]),
        "beta": precip_beta,
        "rank": rank,
        "weather_rmse": weather_rmse,
        "se": se,
        "t": t_stat,
        "df": df,
        "p": p_value,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "delta_10mm": delta_10,
        "residual": residual,
        "x_matrix": weather_x,
        "airports_array": airports,
        "dates_array": dates,
        "clusters": clusters,
    }


def covariance_sensitivity_week(primary_fit: dict[str, object]):
    dates = primary_fit["dates_array"]
    weeks = np.array(
        [
            f"{date.fromisoformat(str(d)).isocalendar().year}-W"
            f"{date.fromisoformat(str(d)).isocalendar().week:02d}"
            for d in dates
        ],
        dtype=str,
    )
    covariance, clusters = two_way_covariance(
        primary_fit["x_matrix"],
        primary_fit["residual"],
        primary_fit["airports_array"],
        weeks,
        int(primary_fit["k_total"]),
    )
    variance = float(covariance[1, 1])
    if not math.isfinite(variance) or variance <= 0:
        raise RuntimeError(f"INVALID_WEEK_CLUSTER_VARIANCE {variance}")
    se = math.sqrt(variance)
    beta = float(primary_fit["beta"])
    t_stat = beta / se
    df = min(clusters["g_first"] - 1, clusters["g_second"] - 1)
    critical = float(stats.t.ppf(0.975, df))
    p_value = float(2 * stats.t.sf(abs(t_stat), df))
    return {
        "beta": beta,
        "se": se,
        "t": t_stat,
        "df": df,
        "p": p_value,
        "ci_low": beta - critical * se,
        "ci_high": beta + critical * se,
        "delta_10mm": beta * math.log(11.0),
        "clusters": clusters,
    }


def gate_from_primary(fit: dict[str, object]) -> str:
    beta = float(fit["beta"])
    ci_low = float(fit["ci_low"])
    delta_10 = float(fit["delta_10mm"])
    if beta > 0 and ci_low > 0 and delta_10 >= 1.0:
        return "PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION"
    if beta > 0 and ci_low > 0 and delta_10 < 1.0:
        return "DETECTABLE_BUT_SUBMATERIAL_US_AIR_E01"
    return "NO_PREREGISTERED_POSITIVE_US_AIR_E01_RELATIONSHIP"


def scalar_fit_row(name: str, fit: dict[str, object]) -> dict[str, object]:
    return {
        "analysis": name,
        "n_airport_days": fit["n"],
        "airports": fit["airports"],
        "dates": fit["dates"],
        "beta_log1p_precip": fit["beta"],
        "se": fit["se"],
        "t": fit["t"],
        "df": fit["df"],
        "p_two_sided": fit["p"],
        "ci95_low": fit["ci_low"],
        "ci95_high": fit["ci_high"],
        "delta_0_to_10mm_minutes": fit["delta_10mm"],
        "volume_gamma": fit["volume_gamma"],
        "baseline_rmse": fit["baseline_rmse"],
        "weather_rmse": fit["weather_rmse"],
        "fe_iterations": fit["fe_iterations"],
        "fe_last_change": fit["fe_last_change"],
        "g_first": fit["clusters"]["g_first"],
        "g_second": fit["clusters"]["g_second"],
        "g_intersection": fit["clusters"]["g_intersection"],
    }


def main():
    E01.mkdir(parents=True, exist_ok=True)
    expected = load_expected_hashes()
    source_rows = []

    with tempfile.TemporaryDirectory(prefix="us-air-e01-stage-b-") as temp:
        tempdir = Path(temp)
        paths: dict[int, Path] = {}

        # HARD BARRIER: download + hash every ZIP before opening any BTS CSV.
        for month in range(1, 13):
            path = tempdir / f"bts_2025_{month:02d}.zip"
            observed = download_to_path(bts_url(month), path)
            exp = expected[month]
            matched = (
                observed["error"] == ""
                and observed["sha256"] == exp["sha256"]
                and observed["bytes"] == exp["bytes"]
            )
            source_rows.append({
                "month": month,
                "url": bts_url(month),
                "expected_bytes": exp["bytes"],
                "actual_bytes": observed["bytes"],
                "expected_sha256": exp["sha256"],
                "actual_sha256": observed["sha256"],
                "hash_match": matched,
                "http": observed["http"],
                "final_url": observed["final_url"],
                "error": observed["error"],
            })
            paths[month] = path

        write_source_manifest(source_rows)

        if not all(bool(row["hash_match"]) for row in source_rows):
            write_hold(
                "BTS_SOURCE_SNAPSHOT_DRIFT",
                source_rows,
                "At least one current BTS 2025 PREZIP archive did not exactly match the F01 frozen byte/hash manifest. The ZIP CSV members were not opened, so no delay magnitude was parsed.",
            )
            print("HOLD_US_AIR_E01_SOURCE_OR_PANEL_SUPPORT;reason=BTS_SOURCE_SNAPSHOT_DRIFT")
            return

        # Only after the 12/12 exact hash barrier passes:
        weather = load_weather_panel()
        aggregates, parse_diag = parse_bts_after_hash_pass(paths, set(weather))

    if parse_diag["negative_delay_rows"] > 0:
        write_hold(
            "HOLD_INFERENCE_OR_SOURCE_SEMANTICS",
            source_rows,
            f"Observed {parse_diag['negative_delay_rows']} negative eligible DepDelayMinutes rows after source-integrity PASS. The frozen contract forbids silent truncation.",
        )
        print("HOLD_US_AIR_E01_SOURCE_OR_PANEL_SUPPORT;reason=NEGATIVE_DELAY")
        return

    panel_rows = []
    for key in sorted(weather):
        aid, day = key
        agg = aggregates.get(key)
        if not agg or agg["n_sched"] <= 0 or agg["delay_n"] <= 0:
            continue
        weather_row = weather[key]
        panel_rows.append({
            "airport_id": aid,
            "date": day,
            "station_id": weather_row["station_id"],
            "precip_mm": float(weather_row["precip_mm"]),
            "trace": bool(weather_row["trace"]),
            "n_sched": int(agg["n_sched"]),
            "eligible_delay_n": int(agg["delay_n"]),
            "y_delay": float(agg["delay_sum"]) / int(agg["delay_n"]),
            "nondiv_delay_n": int(agg["delay_nondiv_n"]),
            "y_delay_nondiv": (
                float(agg["delay_nondiv_sum"]) / int(agg["delay_nondiv_n"])
                if int(agg["delay_nondiv_n"]) > 0
                else ""
            ),
        })

    realized_airports = len({row["airport_id"] for row in panel_rows})
    if realized_airports < MIN_AIRPORTS or len(panel_rows) < MIN_ROWS:
        write_hold(
            "REALIZED_PANEL_SUPPORT",
            source_rows,
            f"Realized panel retained {realized_airports} airports and {len(panel_rows)} airport-days; frozen minimums are {MIN_AIRPORTS} and {MIN_ROWS}.",
        )
        print(
            "HOLD_US_AIR_E01_SOURCE_OR_PANEL_SUPPORT;"
            f"airports={realized_airports};rows={len(panel_rows)}"
        )
        return

    panel_fields = [
        "airport_id", "date", "station_id", "precip_mm", "trace",
        "n_sched", "eligible_delay_n", "y_delay",
        "nondiv_delay_n", "y_delay_nondiv",
    ]
    with PANEL_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=panel_fields)
        writer.writeheader()
        writer.writerows(panel_rows)

    try:
        primary = fit_model(panel_rows)
    except Exception as exc:
        write_hold(
            "HOLD_INFERENCE_DEGENERATE",
            source_rows,
            f"Frozen primary estimation failed: {type(exc).__name__}: {exc}",
        )
        print(f"HOLD_US_AIR_E01_SOURCE_OR_PANEL_SUPPORT;reason={type(exc).__name__}")
        return

    primary_gate = gate_from_primary(primary)

    # Primary gate is computed before sensitivities.
    primary_row = scalar_fit_row("PRIMARY_T_TRACE_0_DIVERTED_INCLUDED", primary)
    primary_row["gate"] = primary_gate
    primary_row["source_rows"] = parse_diag["source_rows"]
    primary_row["relevant_source_rows"] = parse_diag["relevant_rows"]
    primary_row["negative_delay_rows"] = parse_diag["negative_delay_rows"]
    primary_row["nonfinite_delay_rows"] = parse_diag["nonfinite_delay_rows"]
    primary_row["monthly_header_consistent"] = parse_diag["header_consistent"]

    primary_fields = list(primary_row.keys())
    with PRIMARY_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=primary_fields)
        writer.writeheader()
        writer.writerow(primary_row)

    sensitivities = []

    # S1: trace precipitation = 0.1 mm.
    try:
        s1 = fit_model(panel_rows, trace_override=0.1)
        row = scalar_fit_row("S1_TRACE_0_1MM", s1)
        row["status"] = "OK"
    except Exception as exc:
        row = {
            "analysis": "S1_TRACE_0_1MM",
            "status": f"ERROR:{type(exc).__name__}:{exc}",
        }
    sensitivities.append(row)

    # S2: exclude diverted flights from outcome.
    s2_rows = []
    for row0 in panel_rows:
        if int(row0["nondiv_delay_n"]) <= 0 or row0["y_delay_nondiv"] == "":
            continue
        row = dict(row0)
        row["y_delay"] = float(row0["y_delay_nondiv"])
        s2_rows.append(row)
    try:
        s2 = fit_model(s2_rows)
        row = scalar_fit_row("S2_EXCLUDE_DIVERTED", s2)
        row["status"] = "OK"
    except Exception as exc:
        row = {
            "analysis": "S2_EXCLUDE_DIVERTED",
            "status": f"ERROR:{type(exc).__name__}:{exc}",
            "n_airport_days": len(s2_rows),
            "airports": len({r["airport_id"] for r in s2_rows}),
        }
    sensitivities.append(row)

    # S3: keep primary coefficients/residuals, cluster by airport and ISO week.
    try:
        s3 = covariance_sensitivity_week(primary)
        row = {
            "analysis": "S3_CLUSTER_AIRPORT_ISO_WEEK",
            "status": "OK",
            "n_airport_days": primary["n"],
            "airports": primary["airports"],
            "dates": primary["dates"],
            "beta_log1p_precip": s3["beta"],
            "se": s3["se"],
            "t": s3["t"],
            "df": s3["df"],
            "p_two_sided": s3["p"],
            "ci95_low": s3["ci_low"],
            "ci95_high": s3["ci_high"],
            "delta_0_to_10mm_minutes": s3["delta_10mm"],
            "g_first": s3["clusters"]["g_first"],
            "g_second": s3["clusters"]["g_second"],
            "g_intersection": s3["clusters"]["g_intersection"],
        }
    except Exception as exc:
        row = {
            "analysis": "S3_CLUSTER_AIRPORT_ISO_WEEK",
            "status": f"ERROR:{type(exc).__name__}:{exc}",
        }
    sensitivities.append(row)

    sensitivity_fields = []
    for row in sensitivities:
        for key in row:
            if key not in sensitivity_fields:
                sensitivity_fields.append(key)
    with SENSITIVITY_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=sensitivity_fields)
        writer.writeheader()
        for row in sensitivities:
            writer.writerow(row)

    lines = [
        "---",
        "id: US-AIR-E01-STAGE-B-RESULT",
        "type: preregistered-primary-relationship-result",
        "created: 2026-09-10",
        "issue: 90",
        f"gate: {primary_gate}",
        "relationship_outcome_computed: true",
        "incremental_monetary_cost_usd: 0",
        "---",
        "",
        "# US-AIR-E01 Stage B Result",
        "# US-AIR-E01 Stage B 결과",
        "",
        "## Source-integrity barrier / source 무결성 장벽",
        "",
        "- BTS 2025 PREZIP exact hash matches: **12/12**",
        "- All twelve hashes were verified before any ZIP CSV member was opened.",
        f"- parsed BTS identity/outcome source rows after hash PASS: **{parse_diag['source_rows']:,}**",
        f"- rows belonging to the frozen Stage-A weather cohort: **{parse_diag['relevant_rows']:,}**",
        f"- negative eligible DepDelayMinutes rows: **{parse_diag['negative_delay_rows']}**",
        f"- non-finite/unparsed nonblank delay rows: **{parse_diag['nonfinite_delay_rows']}**",
        f"- monthly header consistency: **{parse_diag['header_consistent']}**",
        "",
        "## Realized frozen panel / 실현 고정 panel",
        "",
        f"- airport-date observations: **{primary['n']:,}**",
        f"- unique airports: **{primary['airports']}**",
        f"- unique FlightDate levels: **{primary['dates']}**",
        f"- full parameter count used for CR1 correction K: **{primary['k_total']}**",
        f"- FE alternating-projection iterations: **{primary['fe_iterations']}**",
        f"- final FE max absolute change: **{primary['fe_last_change']:.3e}**",
        "",
        "Frozen support minimums >=100 airports and >=30,000 airport-days are satisfied.",
        "",
        "## Primary preregistered result / 주결과",
        "",
        "Model: airport FE + FlightDate FE + log1p(scheduled departures) + log1p(DailyPrecipitation_mm).",
        "",
        f"- beta on log1p precipitation: **{primary['beta']:.12f} minutes**",
        f"- two-way CR1 SE (AirportID, FlightDate): **{primary['se']:.12f}**",
        f"- t: **{primary['t']:.6f}**",
        f"- df: **{primary['df']}**",
        f"- two-sided p: **{primary['p']:.12g}**",
        f"- 95% CI: **[{primary['ci_low']:.12f}, {primary['ci_high']:.12f}]**",
        f"- model-implied 0 mm to 10 mm difference beta*ln(11): **{primary['delta_10mm']:.6f} minutes**",
        f"- scheduled-volume coefficient gamma: **{primary['volume_gamma']:.12f}**",
        "",
        "### Descriptive baseline comparison / 기술적 baseline 비교",
        "",
        f"- baseline within-RMSE: **{primary['baseline_rmse']:.6f} minutes**",
        f"- weather-model within-RMSE: **{primary['weather_rmse']:.6f} minutes**",
        "",
        "RMSE is descriptive and is not a PASS gate.",
        "",
        "## Primary gate / 주 판정",
        "",
        f"**{primary_gate}**",
        "",
        "The gate was adjudicated before the prespecified sensitivities were run.",
        "",
        "## Prespecified non-gate sensitivities / 사전 sensitivity",
        "",
    ]

    for row in sensitivities:
        lines.append(
            f"- **{row.get('analysis')}**: status={row.get('status','OK')}, "
            f"beta={row.get('beta_log1p_precip','')}, "
            f"SE={row.get('se','')}, "
            f"95% CI=[{row.get('ci95_low','')}, {row.get('ci95_high','')}], "
            f"delta_10mm={row.get('delta_0_to_10mm_minutes','')}"
        )

    lines += [
        "",
        "Sensitivity results do not alter or rescue the primary gate.",
        "",
        "## Interpretation boundary / 해석 경계",
        "",
        "This is a preregistered contemporaneous association test. It is not advance prediction, causal inference, network propagation, airport/carrier ranking, novelty validation, operational utility validation, investment advice or policy superiority.",
        "",
        "## Durable outputs / 영속 산출물",
        "",
        "- research/US-AIR-E01/STAGE_B_BTS_SOURCE_MANIFEST.csv",
        "- research/US-AIR-E01/STAGE_B_AIRPORT_DAY_PANEL.csv",
        "- research/US-AIR-E01/STAGE_B_PRIMARY_RESULT.csv",
        "- research/US-AIR-E01/STAGE_B_SENSITIVITY_RESULT.csv",
        "- research/US-AIR-E01/STAGE_B_RESULT.md",
        "",
        f"- Python/numpy/scipy: {np.__version__} / {stats.__version__ if hasattr(stats,'__version__') else 'scipy-module'}",
        "",
        "Raw BTS ZIP/CSV bytes were transient and are not persisted.",
        "",
        "Incremental monetary cost remains **0 USD**.",
    ]
    RESULT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        f"{primary_gate};"
        f"N={primary['n']};airports={primary['airports']};"
        f"beta={primary['beta']};se={primary['se']};"
        f"ci_low={primary['ci_low']};delta10={primary['delta_10mm']}"
    )


if __name__ == "__main__":
    main()
