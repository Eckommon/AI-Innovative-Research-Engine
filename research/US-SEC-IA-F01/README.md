---
id: US-SEC-IA-F01
type: outcome-blind-structural-feasibility
created: 2026-09-30
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R49
parent_decision: DEC-284
selected_candidate: US-SEC-IA-001
future_advw_membership_opened: false
post_cutoff_advw_body_opened: false
incremental_monetary_cost_usd: 0
---

# US-SEC-IA-F01 — exact CRD structural gate before future full ADV-W withdrawal

## Mission / 목적

Determine, **before opening any post-cutoff Form ADV-W membership**, whether SEC/IAPD public data support a deterministic firm-level prospective design for future **full registration withdrawal** using exact adviser CRD identity.

F01 is structural only. It does not test whether adviser business structure predicts a later withdrawal and does not interpret withdrawal as firm failure.

## Frozen official source anchors / 공식 소스

### Current / longitudinal adviser baseline
- SEC Investment Adviser Information Reports:
  `https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers`

The official page provides monthly ZIP reports and currently exposes Registered Investment Advisers through **August 2026**.

### Historical ADV / ADV-W lineage
- SEC historical Form ADV data:
  `https://www.sec.gov/foia-services/frequently-requested-documents/form-adv-data`
- Historical aggregate ADV-W ZIP prospectively fixed:
  `https://www.sec.gov/files/advw-20001019-20241231.zip`
- IAPD Form ADV Data, 2025 onward:
  `https://adviserinfo.sec.gov/adv`

### Event semantics
- Form ADV-W:
  `https://www.sec.gov/files/formadv-w.pdf`
- SEC Form ADV / IARD FAQ:
  `https://www.sec.gov/about/divisions-offices/division-investment-management/electronic-filing-investment-advisers-iard/frequently-asked-questions-form-adv-iard`

## Frozen baseline window / 고정 baseline 기간

F01 may resolve exactly **12 monthly SEC Registered Investment Adviser Information Report ZIPs**:

> September 2025 through August 2026 inclusive.

Every resolved monthly file must originate from the official SEC Information Reports page and be fingerprinted by:
- final URL;
- HTTP metadata;
- compressed bytes;
- SHA-256;
- contained spreadsheet filename;
- parsed header.

The exact **August 2026** registered-adviser report is the primary prospective baseline.

Raw ZIP/XLSX bytes are transient under RAW-001 and are not committed.

## Frozen historical event source / historical event source

F01 may download exactly the official historical aggregate:

> `advw-20001019-20241231.zip`

for historical ADV-W event semantics/support only.

No 2025-09-01-or-later ADV-W row body may be opened during F01.

Historical ADV-W rows may be used only for:
- exact CRD syntax/support;
- full/partial withdrawal classification;
- filing/event date semantics;
- reason/transition semantics;
- historical support counts.

They may not be used to tune a future predictive exposure.

## Frozen future event / 미래 event

A future descendant may classify a primary event only as:

> a source-native **full withdrawal** Form ADV-W filing for a baseline-eligible adviser after the separately frozen N01 cutoff.

Partial withdrawal remains non-primary.

A full withdrawal is a registration event. It must **not** be labeled:
- firm failure;
- insolvency;
- business cessation;
- client harm

without separate evidence.

SEC→state, SEC→exempt-reporting-adviser, succession/reorganization, or other regulatory transitions must remain explicit competing/administrative event classes when source fields permit.

Disappearance from the monthly registered-adviser report **without a qualifying ADV-W record is not a withdrawal outcome**.

## Frozen firm identity / 고정 firm identity

Primary identity is exact source-native **Organization CRD Number**.

Allowed normalization:
1. convert to text;
2. trim ASCII whitespace;
3. remove a trailing spreadsheet-style `.0` only when the remaining string is digits;
4. accept only digits with integer value > 0.

Prohibited:
- name matching;
- SEC file number substitution as the primary join;
- address/location repair;
- CIK substitution;
- owner/person CRD substitution;
- fuzzy/manual repair.

SEC file number may be recorded only as a secondary consistency field.

## Frozen baseline population / baseline 모집단

August 2026 baseline includes only advisers in the official **Registered Investment Advisers** Information Report.

Exempt Reporting Advisers are excluded from the primary baseline.

F01 must record, without predictive modeling:
- exact distinct CRD count;
- organization-form support;
- SEC registration fields;
- regulatory AUM/business/client structure availability;
- monthly CRD persistence across the 12 baseline reports.

No withdrawal/cessation/ineligibility field may define baseline exposure.

## Anti-tautology firewall / 순환성 방화벽

A descendant predictive exposure may not include:
- ADV-W filing or intent;
- reason for withdrawal;
- cessation date;
- registration termination/withdrawal status;
- direct switch-to-state/ERA marker;
- pending withdrawal;
- any variable mechanically derived from the future withdrawal window.

F01 computes no relationship or direction.

## Immutable 18-gate contract / 불변 18개 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical checkpoint = `CHK-20260930-PORTFOLIO-R49-TERMINAL`; last decision `DEC-284`; selected candidate = `US-SEC-IA-001` |
| 2 | Issue binding | runner executes only after a new Issue is bound to this exact pre-Issue contract commit |
| 3 | Official source access | SEC adviser-report page, historical ADV page, IAPD Form ADV page, Form ADV-W and SEC FAQ are reachable or officially redirected |
| 4 | Twelve-month baseline resolution | exactly 12 official Registered Investment Adviser report ZIPs for 2025-09..2026-08 are resolved and parseable |
| 5 | Baseline fingerprint distinctness | all 12 monthly report body SHA-256 values are recorded and at least **10/12** are distinct |
| 6 | August schema | August report exposes source-native firm CRD plus SEC registration, organization/business and at least one adviser-size/client/business-structure concept |
| 7 | Exact CRD syntax | ≥ **99.90%** of nonblank August firm CRDs satisfy the frozen CRD rule |
| 8 | August independent support | ≥ **15,000** distinct exact CRDs in the August Registered Investment Adviser report |
| 9 | Monthly identity continuity | ≥ **90.00%** of August exact CRDs appear in at least **6 of 12** frozen monthly reports |
| 10 | Historical ADV-W ZIP access | fixed official `advw-20001019-20241231.zip` is parseable, fingerprinted and contains at least one structured ADV-W table |
| 11 | ADV-W identity support | ≥ **99.00%** of nonblank historical adviser CRDs satisfy the frozen exact-CRD rule |
| 12 | Full/partial semantics | ≥ **99.00%** of rows with nonblank withdrawal-status/classification use source values deterministically mappable to full versus partial withdrawal, without inference from firm disappearance |
| 13 | Historical full-withdrawal support | ≥ **1,000** distinct exact CRDs have at least one source-classified full withdrawal in the historical ADV-W body |
| 14 | ADV-W date support | ≥ **99.00%** of source-classified full-withdrawal rows have a parseable source-native filing/submission/effective date suitable for historical event ordering |
| 15 | Identity bridge support | ≥ **90.00%** of exact CRDs in a fixed recent historical full-withdrawal subset (2023-01-01..2024-12-31 when source date supports it) exact-match at least one CRD appearing in the official adviser-report lineage or historical ADV source family without name/address repair |
| 16 | Future filing seal | no ADV-W row body dated/filed on or after **2025-09-01** is opened; future ADV-W membership opened = false |
| 17 | Outcome/identity firewall | withdrawal/business-failure relationship, prediction, ranking or causal metric = false; prohibited withdrawal exposure = false; name/address/fuzzy/manual identity repair = false |
| 18 | Reproducibility/cost | immutable evidence records all source URLs/HTTP metadata, 12 report SHA-256 values, ADV-W SHA-256/member inventory, schemas, row/cardinality/date/classification counts, contract SHA, runner SHA, firewall values and cost = 0 USD |

## Frozen implementation boundary / 구현 경계

A parser may resolve spreadsheet header rows/sheets only deterministically from source concepts. Parser/transport defects may be corrected only if:
- every scientific criterion remains unchanged;
- prior attempts remain immutable;
- no future/post-cutoff withdrawal body is opened.

## Frozen terminal rule / 종결 규칙

PASS only if every gate passes:

`PASS_US_SEC_IA_F01_EXACT_CRD_FUTURE_FULL_ADVW_DESIGN_READY`

Any valid empirical gate failure:

`HOLD_US_SEC_IA_F01_EXACT_CRD_FUTURE_FULL_ADVW_DESIGN_NOT_READY`

A valid scientific HOLD is terminal for this exact F01. Do not lower support/completeness thresholds, substitute another identity, reinterpret partial withdrawals as full withdrawals, or add post-cutoff event data after observation.

## PASS consequence / PASS 이후

PASS authorizes only a separate outcome-blind `US-SEC-IA-N01`.

N01 must freeze before any post-cutoff ADV-W membership is opened:
1. one non-tautological baseline exposure;
2. eligible registered-adviser cohort;
3. comparator/matching/stratification;
4. regulatory-transition competing states;
5. future filing window;
6. minimum full-withdrawal support;
7. balance/statistical gates.

E01 and post-cutoff ADV-W membership are not authorized by F01 PASS alone.

## Non-claims / 비주장

F01 makes no claim that business structure predicts full withdrawal and no claim that withdrawal is failure, insolvency or client harm. It does not rank advisers or recommend regulatory, investment or client actions.

Incremental monetary cost must remain **0 USD**.
