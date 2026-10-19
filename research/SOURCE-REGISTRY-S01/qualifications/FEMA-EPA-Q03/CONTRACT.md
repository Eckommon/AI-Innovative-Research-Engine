---
id: SOURCE-QUAL-FEMA-EPA-Q03
type: prospective-source-native-geography-and-time-support-qualification
date: 2026-10-19
parent_issue: 244
base_commit: 8112348a69d3679c5c2c4c03f2e0f7ca1a8407c2
status: FROZEN_BEFORE_ANY_SOURCE_ROW_ID_ACCESS
science_f01_authorized: false
cost_usd: 0
---

# Q03 — Historical FEMA geography ↔ 2024 EPA monitor geography, source-key-only preflight / 독립 구조 적격성 사전계약

**Independent sequence / 독립순서:** Q01 `HOLD_SOURCE_ACCESS_OR_SCHEMA` remains terminal (2024 county AQI product). Q02 `DUAL_D2_SOURCE_HEADERS_ONLY_Q02` proved *another EPA annual monitor concentration product* has 7/7 literal source headers and dual individual D2 original-body receipts, NOT a row join. Q03 is a new **S01 source/geography/time support operation** under existing secondary Issue #244. It is NOT F01/N01/E01, scientific inference, Q01 rescue, grade D3, or R60.

## Source/fingerprint freeze BEFORE row inspection / 원본 고정
- FEMA V2 exact `https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries.csv`, original Q01 verified SHA256 `0c51c72b0fd4f616afeb01bb1f7e95f6b7f1349832f7b3be9d12e7dd7e5aaa30`; maximum 64 MiB.
- EPA 2024 *Annual Concentration by Monitor* exact `https://aqs.epa.gov/aqsweb/airdata/annual_conc_by_monitor_2024.zip`, original Q02 verified SHA256 `8af92d1ec8ac9271babc84e3512cb2068e6a8849af438448c4170fd9e99ea5bb`, ZIP member exactly `annual_conc_by_monitor_2024.csv`; maximum 16 MiB. No use of the separate held Q01 county AQI ZIP.
- Each **one** HTTPS GET, no follow-redirect, no retry, no mirror/auth/paywall or alternative version; full bytes/ZIP SHA equality **must precede any row parsing**. A changed blob is `HOLD_Q03_SOURCE_VINTAGE_CHANGED`, not a newly qualified source. No raw objects, row samples or identifiers committed.

## Prospective *feasibility* question (not a science hypothesis) / 사전질문
Does the 2019-01-01..2023-12-31 *historical FEMA declared-area* source support share syntactically native 5-digit state+county FIPS geography with the 2024 EPA *any-pollutant monitoring location* universe, with enough overlap to justify **later separately pre-registering** a non-causal study? No exposure–concentration claim. FEMA historical declared geography is *not* a valid untreated comparison group and historical declaration presence is not absence of disasters. EPA monitor coverage is non-random.

## Exact accessible columns / 판독 허용 열
- FEMA: ONLY `fipsStateCode`, `fipsCountyCode`, `incidentBeginDate` for historical time qualification; no declaration number, type, severity, assistance, title, counts per disaster or event-level reporting. Dates strictly `2019-01-01` inclusive to `2024-01-01` exclusive. Zero 2024+ FEMA event values permitted (parse date only to exclude).
- EPA: ONLY `State Code`, `County Code`, `Site Num`, `Parameter Code`, `POC`, `Sample Duration`, `Pollutant Standard`, `Event Type`, `Year`. Require literal source headers, validate `Year == 2024`; no pollutant selection, air concentration/mean, observation count, AQI, units, completeness, names, coordinates or metadata suggesting result selection.
- Full source-body acquisition necessarily transfers raw bytes; **only these source ID/time fields may be decoded for structure**, all other columns dropped, not evaluated or printed. No emitted county IDs or raw row records. Source access is a historical structural exploration, not blinded clinical-like inference; freeze the rule before any reading.

## Frozen normalization and counters / 고정 정규화
1. Keys are exact fixed-width source text `SSCCC` (no coercion from integers, inferred aliases or county-name matching). `SS` exactly two digits; `CCC` exactly three digits, reject state `00`, county `000` and `999` conservatively; syntactically valid does not prove current county equivalent. Keep original string leading zeros.
2. No geography vintage crosswalk and **no placeCode-based repair**. Count excluded/invalid geography rows for each source only in aggregate; do not disclose which IDs. Do not treat syntactic matching as same 2024 county vintage.
3. Historical FEMA scan retains a **set of unique 5-digit county keys only** for rows in fixed 2019–2023 window; no per-event frequencies or FEMA disaster count outputs. EPA scan retains 2024 unique county set, unique site+parameter+POC identity set and duplicated monitor-grain signatures across annual duration/standard/event dimensions. Only aggregate sizes/counts may be recorded, no individual or ranked counties.
4. Deduplicate EPA county **for support only**, never aggregate concentrations. Monitor has potentially many summary records; never assert one row per county or site. Any row-level geography invalidity is counted and excluded, not repaired.
5. Predeclared metrics: `N_FEMA_HISTORICAL_DISTINCT_COUNTIES`, `N_EPA_2024_DISTINCT_MONITORED_COUNTIES`, `N_DISTINCT_KEY_OVERLAP`, `OVERLAP_SHARE_OF_EPA_COUNTIES`, `N_EPA_COVERED_COUNTIES_WITHOUT_HISTORICAL_FEMA`, `N_MATCHED_STATES`, EPA monitor-signature/row multiplicity, source-year/header/code syntax exceptions.
6. Prospective **minimum operational overlap (not model power or future science gate):** EPA monitored-county denominator `>=100`, shared keys `>=100`, shared states `>=15`, `OVERLAP_SHARE_OF_EPA_COUNTIES >= 0.20`; each must pass. If not, `HOLD_Q03_INSUFFICIENT_SOURCE_NATIVE_KEY_SUPPORT`. If achieved, `PASS_Q03_SYNTAX_SUPPORT_ONLY__F01_NOT_AUTHORIZED`. Distinct FEMA historical coverage of all/most EPA counties can invalidate any unexposed comparison and must not become evidence of a difference.
7. **Hard fail-closed on** absent columns, unexpected ZIP member, invalid source SHA, parser exceptions, second request, or time metadata ambiguity: report operational HOLD, no threshold adjustment or retry.

## Gates and authority / 실행전 승인조건
A. Q01 original terminal HOLD, Q02 distinct-source D2 evidence and specific SHA/URL all exist on canonical main; frozen Q03 contract commit predates network/row access.
B. Primary canonical `#203` / `DEC-318` and secondary `#244` exact two-issue state, no E01 candidate/attempt or changed E01 runner.
C. Safe bounded read, no redirect, exact SHA verification, no data archived; synthetic tests before first real source access.
D. Schema/payload grain/time/format verified; invalid keys excluded without repair; all source-native counters deterministic.
E. Single immutable `evidence/source-structure-01.json` + bilingual .md and Q03 terminal RESULT *only after verified execution*; no raw county IDs or observed air/disaster outcomes in artifacts.
F. **No scientific promotion**: regardless of pass, next is a separately prospective geography vintage/monitor-selection/scientific F01 design. Do not infer a 2024 FEMA-to-EPA panel, causal impact, statistical association, or power. No future CMS NPI ZIP/provider outcomes.
G. Standard public GitHub Ubuntu only, no added fee, no new Issue or R60 and no third Track. Zero USD.

**Prospective output classes:** `PASS_Q03_SYNTAX_SUPPORT_ONLY__F01_NOT_AUTHORIZED`, `HOLD_Q03_INSUFFICIENT_SOURCE_NATIVE_KEY_SUPPORT`, `HOLD_Q03_SOURCE_VINTAGE_CHANGED`, `HOLD_Q03_SOURCE_ACCESS_OR_SCHEMA`, `HOLD_Q03_OPERATIONAL_INTEGRITY`. Even PASS is D2+geography feasibility **not** validated D3/F01.
