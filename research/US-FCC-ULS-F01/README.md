---
id: US-FCC-ULS-F01
type: outcome-blind-structural-feasibility
created: 2026-09-21
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R40
parent_decision: DEC-241
selected_candidate: US-FCC-ULS-001
radio_service_family: Microwave_and_Microwave_Broadcast_Auxiliary
future_cancelled_terminated_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-FCC-ULS-F01 — Microwave exact-system-ID structural gate before future cancellation/termination

## Mission / 목적

Determine, **before opening any post-baseline cancelled/terminated Microwave license membership**, whether official FCC Universal Licensing System public-access files can support a deterministic license-level prospective design using the FCC-assigned unique 9-digit system identifier.

F01 is structural only. It does not test whether any historical license, technical, ownership, application, geographic, build-out, or administrative characteristic predicts cancellation or termination.

## Frozen service family / 고정 서비스 family

The only authorized family is the FCC public-access **Microwave and Microwave Broadcast Auxiliary** license family distributed as:

- complete license archive: `l_micro.zip`;
- daily license transaction archives: `l_mw_xxx.zip`, where `xxx` is the FCC weekday suffix.

No Amateur, Aircraft, GMRS, Land Mobile, Cellular, Paging, Market-based, BRS/EBS, Coast/Ground, Ship, FRC, assignment/transfer, leasing, ASR, BDC or third-party mirror may replace this family after observation.

The family is frozen because FCC documentation identifies Microwave as a site-based Form-601 family with required `HD` header and `HS` application/license-history tables, while the public-access download architecture separately exposes complete and daily transaction files.

## Frozen official source anchors / 고정 공식 소스

Documentation:

- `https://wireless.fcc.gov/uls/documentation/pa_intro24.pdf`
- `https://wireless.fcc.gov/wtbfiles/pa_ddef51.pdf`
- `https://wireless.fcc.gov/uls/releases/d992205c.pdf`
- `https://www.fcc.gov/wireless/data/public-access-files-database-downloads`

Empirical baseline endpoint prospect:

- `https://data.fcc.gov/download/pub/uls/complete/l_micro.zip`

Future daily endpoint family prospect:

- `https://data.fcc.gov/download/pub/uls/daily/l_mw_mon.zip`
- `https://data.fcc.gov/download/pub/uls/daily/l_mw_tue.zip`
- `https://data.fcc.gov/download/pub/uls/daily/l_mw_wed.zip`
- `https://data.fcc.gov/download/pub/uls/daily/l_mw_thu.zip`
- `https://data.fcc.gov/download/pub/uls/daily/l_mw_fri.zip`

F01 may correct only an implementation-level host/path redirect if the official FCC download page or HTTP redirect proves that the same named FCC archive has moved. It may not substitute another dataset, mirror, service family, API-derived cohort or paid source.

## Frozen identity semantics / 고정 식별자 규칙

Primary license identity is the FCC **Unique System Identifier** in `HD`, documented as `numeric(9,0)` and described by FCC as a unique 9-digit system identifier that can distinguish a current call sign from an expired, cancelled or terminated prior license after call-sign reassignment.

F01 identity rules:

1. use only the source-native Unique System Identifier;
2. retain only source values that losslessly normalize to exactly nine decimal digits;
3. do not identify licenses by call sign alone;
4. do not use licensee name, FRN, address, coordinates, market, frequency, call-sign similarity, fuzzy matching, geospatial repair or manual reconciliation to repair identity;
5. `ULS File Number` may be retained as application/document context but is not a substitute license identity.

## Frozen baseline and future time boundary / 고정 시간 경계

### Historical structural baseline authorized in F01

One complete `l_micro.zip` body may be retrieved **after Issue binding on 2026-09-21**. Its HTTP metadata and SHA-256 become the immutable baseline fingerprint.

F01 may read the complete archive only to establish:

- archive/table structure;
- exact system-ID syntax and cardinality;
- `HD` license status/date fields;
- `HS` historical lineage support;
- non-outcome structural/technical table availability;
- the size of an **active-at-baseline** candidate license universe.

Historical statuses `C/E/T` that already exist inside the complete baseline are source-history context only. They may not be used to choose an exposure, score a candidate, or estimate an association.

### Future outcome source — sealed in F01

The prospective event window is frozen as:

- **start:** 2026-09-21
- **end:** 2027-03-20 inclusive.

A later descendant may identify a future event only from FCC daily Microwave license transactions whose source action/update falls inside the frozen window and whose exact system ID belongs to the baseline active cohort.

In F01:

- daily `l_mw_xxx.zip` entity bodies must not be opened;
- daily endpoints may receive only body-free `HEAD` or method-equivalent metadata requests;
- no baseline active system ID may be classified as future cancelled, terminated, survived or otherwise outcome-positive/negative.

## Frozen event semantics / 고정 event 의미

Official FCC code definitions establish `HD License Status`:

- `A` = Active
- `C` = Canceled
- `E` = Expired
- `T` = Terminated

The `HD` format separately documents Grant Date, Expired Date, Cancellation Date, Effective Date and Last Action Date.

F01 does not decide the final descendant event hierarchy beyond requiring that a later N01 freeze, before any daily body is opened:

1. exact baseline system-ID cohort;
2. cancellation vs termination adjudication;
3. expiration handling;
4. duplicate/multiple daily appearances;
5. date precedence among cancellation/effective/last-action/history dates;
6. assignment/transfer and service-code changes;
7. same-ID conflicts;
8. minimum event/cardinality requirements.

Ordinary expiration may not be silently merged into cancellation/termination.

## Immutable 18-gate contract / 불변 18개 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal R40 selection `US-FCC-ULS-001`, checkpoint `CHK-20260918-PORTFOLIO-R40-TERMINAL`, last decision `DEC-241` |
| 2 | Issue binding | empirical runner executes only after a new Issue is created and bound to this exact pre-Issue contract commit |
| 3 | Official documentation availability | all frozen FCC documentation anchors are reachable or have an official same-document redirect; identity/download/status semantics can be fingerprinted |
| 4 | Service-family freeze | official documentation maps Microwave/Microwave Broadcast Auxiliary to `l_micro.zip` complete license data and `l_mw_xxx.zip` daily license data |
| 5 | Complete baseline access | the frozen complete Microwave license archive resolves from an official FCC host at zero incremental cost and is a parseable ZIP |
| 6 | Required table structure | baseline archive contains parseable `HD.dat` and `HS.dat`; official documentation identifies HD and HS as required for Microwave license data |
| 7 | Frozen HD schema | parsed HD exposes source positions/concepts for Unique System Identifier, Call Sign, License Status, Radio Service Code, Grant Date, Expired Date, Cancellation Date, Effective Date and Last Action Date without inferred column shifting |
| 8 | Exact system-ID syntax | at least **99.90%** of nonblank HD Unique System Identifier values normalize losslessly to exactly 9 digits; invalid values are excluded, not repaired |
| 9 | Independent license support | at least **20,000** distinct valid exact system IDs exist in HD |
| 10 | Active baseline support | at least **10,000** distinct valid exact system IDs have HD License Status exactly `A` at baseline |
| 11 | License-status semantics | at least **99.90%** of nonblank HD status values are among the officially documented `A/C/E/T` codes; any other value is recorded, never remapped |
| 12 | Core date parseability | at least **99.00%** of active-baseline HD rows have parseable nonblank Grant Date or Effective Date, and all parsed dates preserve source precision without inference |
| 13 | History linkage support | at least **90.00%** of active-baseline exact system IDs appear in at least one HS row under the same exact system ID |
| 14 | Historical action/date structure | HS provides a deterministic exact-system-ID-linked action/history code plus a parseable history/action date for at least **90.00%** of HS rows linked to active-baseline IDs |
| 15 | Structural technical availability | at least two non-identity, non-name/address technical/administrative Microwave tables beyond HD/HS are present and exact-system-ID joinable, establishing substantive historical exposure potential without defining an exposure in F01 |
| 16 | Sealed future daily source | at least one frozen `l_mw_xxx.zip` daily endpoint accepts body-free HEAD or method-equivalent metadata access with **0 entity-body bytes consumed**; no daily ZIP body is opened |
| 17 | Outcome firewall | future daily rows opened = **0**; future cancelled/terminated membership opened = **false**; future relationship/prediction/ranking/causal metric computed = **false**; name/address/call-sign-only/fuzzy/geo/manual identity repair used = **false** |
| 18 | Reproducibility and cost | immutable JSON/Markdown evidence records exact final URLs, HTTP metadata, baseline ZIP SHA-256, table names/counts, schema mapping, gate values, contract SHA, runner SHA-256, firewall values and `incremental_monetary_cost_usd = 0` |

## Frozen terminal rule / 종결 규칙

PASS only if every gate passes:

`PASS_US_FCC_ULS_F01_MICROWAVE_EXACT_SYSTEM_ID_FUTURE_EVENT_DESIGN_READY`

Any valid empirical failure:

`HOLD_US_FCC_ULS_F01_MICROWAVE_EXACT_SYSTEM_ID_FUTURE_EVENT_DESIGN_NOT_READY`

A valid scientific HOLD is terminal for this exact F01. Radio-service family, baseline source, identity rule, minimum support, lineage thresholds, daily-source firewall and future window may not be relaxed or substituted after counts are observed.

Transport, host migration, parser or archive-format defects may be corrected only as implementation defects when the scientific contract remains unchanged and every prior attempt is preserved immutably.

## PASS consequence / PASS 이후

PASS authorizes only a separate outcome-blind `US-FCC-ULS-N01` design.

N01 must, **before any future daily license body is opened**, freeze:

- one non-tautological historical exposure from baseline/public-access structure;
- eligibility and exclusions within the exact active-baseline system-ID cohort;
- deterministic matching/stratification or comparison design;
- future `C/T` adjudication hierarchy and expiration rule;
- duplicate/conflict/action-date handling;
- minimum resolved-event support and the primary statistical gate.

PASS does not authorize E01 or opening any future daily transaction body.

## Non-claims / 비주장

F01 makes no claim that any Microwave license characteristic predicts or causes cancellation/termination; no spectrum-license risk score, licensee ranking, enforcement/regulatory recommendation, causal claim or novelty claim is authorized.

Incremental monetary cost must remain **0 USD**.
