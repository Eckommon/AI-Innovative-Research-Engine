---
id: SOURCE-QUAL-FEMA-EPA-Q01-RESULT
created: 2026-10-19
parent_issue: 244
contract_commit: 73adb0a35e143d7871b243a64a94aea8132c40ed
observed_attempt_run: 39152768960
immutable_attempt_commit: 5f878ddc6573f5192bfe643e83e737441e7f9a18
type: terminal_source-qualification-not-science
disposition: HOLD_SOURCE_ACCESS_OR_SCHEMA
science_f01_authorized: false
incremental_monetary_cost_usd: 0
---

# FEMA×EPA Q01 — source-qualification verdict / 정부 원천 2종 실증 판정

**Final / 최종: `HOLD_SOURCE_ACCESS_OR_SCHEMA` — case-level or causal science NOT EXECUTED.**

## Actual original-source receipts / 공식 원본 확보

[GitHub Run #39152768960](https://github.com/Eckommon/AI-Innovative-Research-Engine/actions/runs/39152768960) passed 12/12 synthetic source-boundary tests and the bounded source-access job, committed [exact immutable evidence](evidence/source-qualification-01.json). Both full official original source payloads were read for SHA and size, never individual outcome rows. Each raw object was **reachable and completely fingerprinted**. The prospective *paired schema gate* nevertheless failed.

| Frozen first-party source | Actual HTTP | Bytes | SHA256 | Header gate |
|---|---:|---:|---|---|
| FEMA OpenFEMA v2 DisasterDeclarationsSummaries.csv | 200 | **25,009,462** | `0c51c72b0fd4f616afeb01bb1f7e95f6b7f1349832f7b3be9d12e7dd7e5aaa30` | PASS — source-native `fipsStateCode`+`fipsCountyCode` |
| EPA AQS annual_aqi_by_county_2024.zip | 200 | **20,730** | `f6bec6492d0d2a64c557a48ca7d54aa5ac39993051d1eea43d055d9b391d689b` | **HOLD** — the exact source CSV header does **not** expose jointly frozen `State Code`+`County Code` labels |

EPA member `annual_aqi_by_county_2024.csv` safely recognized, 18 CSV header columns, no outcome rows parsed. FEMA has 29 header columns; no disaster/declaration rows inspected. The result preserves exact header hashes and source timestamps without publishing case data.

## What passed, and what did not / 증거 범위 분리

- **Observed raw transport:** both exact public first-party full source bodies obtained and individually fingerprinted. This is a **D2 source-body receipt at each resource level**, not source qualification of the two as a *joined* reusable research pair.
- **Frozen pair:** the exact EPA county-field labels were predicted incorrectly for the *county AQI product*. Hence original prospective Q01 **HOLD**. Do not alter the original contract, try a different EPA dataset, use guessed text aliases or a name-to-FIPS mapping to rescue this exact attempt.
- **Official schema product distinction:** EPA [AirData FileFormats](https://aqs.epa.gov/aqsweb/airdata/FileFormats.html) defines `State Code` and `County Code` in several **monitor/site-oriented products**, while the [county annual AQI download](https://aqs.epa.gov/aqsweb/airdata/download_files.html) is a different product. Documentation of related AQS datasets did **not** prove this product had the same literal header. Before any **new, separately preregistered** prospective qualification, product-specific first-party header must be inspected independently and semantic key type assessed without access to outcomes.
- **No exact county join measured**; no claim of equal geography vintage, 2024 pairing support, quantified disasters, pollutant days, association or causal effect. The non-random EPA monitored-county universe is an independent eligibility concern even if key semantics are later proved.
- **Original S01 8-resource D0-D4 registry** and its `12/12 PASS_SOURCE_REGISTRY_S01_OPERATIONAL_ONLY` remain immutable. This new Q01 source receipt is a separate annex; it does not automatically rewrite S01 grade, mark two eligible D2 joined sources, promote an F01, or weaken `HOLD_NEED_DUAL_D2_SOURCE`.
- E01 primary Issue #203, `DEC-318`, 346,859 pairs, source watcher and science gate untouched. No zip bodies from E01, no paid API, no personal/source row outputs. Cost **0 USD**.

## Concrete source-first process improvement / 작업규약 개선 근거

For each future independent source-qualification **before** an F01/portfolio selection: (1) source-specific official binary/CSV header, not neighboring catalog data dictionary, (2) explicit exact native key field/unit/county vintage, (3) official complete-body SHA evidence from the no-cost canonical runner, (4) empirical exact-join support only under separately frozen structural rules, (5) no terminal route revival after near-miss. This is a prospective process requirement for later contracts, **not a change to the original Q01**.

**Next exact S01 work:** evidence-grade asset discovery remains open under Issue #244. Qualify a new independent, verifiable original-body source pair with *true* exact native bridge; if no such pair appears, keep `HOLD_NEED_DUAL_D2_SOURCE` rather than creating a speculative R60. No third research Issue, no F01 or outcome experiment authorized.

**Terminal Q01 disposition:** `HOLD_SOURCE_ACCESS_OR_SCHEMA`, not source-absence, not scientific F01-HOLD, not statistical null. **0 USD.**
