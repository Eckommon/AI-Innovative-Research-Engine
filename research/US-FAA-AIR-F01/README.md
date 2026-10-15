---
id: US-FAA-AIR-F01
created: 2026-10-16
type: prospective-outcome-blind-structural-feasibility
status: CONTRACT_FROZEN_PRE_ISSUE
parent_portfolio: PORTFOLIO-R57
parent_portfolio_result_commit: 1aeefb979eff7836404d26715c7260d637e20005
parallel_parent: US-CMS-NPI-E01
future_deregistration_rows_authorized: false
incremental_monetary_cost_usd: 0
---

# US-FAA-AIR-F01 — Airframe identity and future deregistration feasibility / 항공기 식별·장래 등록말소 구조 검증

## Mandate and independence / 승인 범위

This F01 is the outcome-blind structural descendant of the **independently frozen** R57 selection; it is a **secondary Track B** and MUST NOT replace the canonical active `US-CMS-NPI-E01 / Issue #203`. The frozen E01 runner, source-release lock, 346,859 matched pairs, events, 18 gates and decision `DEC-318` are untouched.

**Mission / 목적:** determine, using only already available FAA source architecture and *non-event* baseline structural records, whether one physical aircraft can be identified through official registration snapshots without N-number-only reuse, so a later separately frozen future-registration-event experiment might become scientifically feasible.

**No FAA deregistration outcome membership may be opened in F01.** The FAA Deregistered file's *header/schema* may be verified without reading/aggregating its event rows; no future event counts, event dates, reasons, correlations, ranking or inferred rate may be calculated.

## Official frozen source family / 공식 고정 출처

- FAA current aircraft registry info and ZIP: `https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download`; `https://registry.faa.gov/database/ReleasableAircraft.zip`.
- Official FAA ZIP includes Master, Deregistered, aircraft and engine reference tables, document index; approximately 60 MB, daily refreshed at 11:30pm US Central.
- Authoritative field-layout description linked from same FAA landing page. Do **not** replace source with third-party mirror, scraping protected EDRS, PDF owner records, name/address identity repair or paid/private registry.
- Previously publicly listed historical yearly FAA archive bundles 2020 and 2021 **if exact FAA official URLs are independently verified before execution**. Historical-snapshot identity is a mandatory test; do not silently substitute a different year.

The exact binary SHA/byte length **cannot be invented in this prospective contract**; they must be captured into immutable attempt evidence from actual allowed first-party access. Current download and historical snapshots have NOT been retrieved in R57.

## Unit, exposure, temporal firewall / 단위·노출·시간

- **Unit hypothesis:** physical aircraft exact compound identity `(source-native manufacturer/model code, source-native manufacturer serial)`. Require nonblank canonical-preserving strings and strict unique qualifying mapping; treat N-number as mutable alias, never identity.
- **Exposure candidate family:** strictly non-outcome manufacturer/model/engine reference/aircraft category and independently documented manufacture age, with a frozen baseline snapshot prior to any future data access. No `Deregistered` status, dereg reason, prior loss, enforcement, crash, accident, or direct target proxy as exposure.
- **Privacy:** do not store or emit names, postal addresses, personally identifying owner fields or other unnecessary sensitive FAA record contents in result artifacts.
- **Time:** baseline historical 2020/2021 annual full archives and frozen 2026 current snapshot; no future dereg change until an independently selected N01/E01 with its own prospective first-refresh lock.

## Prospective 18 feasibility gates / 사전고정 18개 F01 게이트

All **18/18** must pass for a structural F01 PASS; else **scientific HOLD** if source body was actually evaluated; **BLOCKED_TRANSPORT** if official source cannot be acquired without a new method. No post hoc thresholds, exclusions or repairs.

1. **Official path / 출처:** both FAA landing documentation and public `registry.faa.gov` source resolve first-party HTTPS without authentication/purchase.
2. **Baseline immutable archive / 기준자료 지문:** downloaded official current ZIP HTTP 200, nonzero bytes, exact byte count + SHA256 recorded with fetch UTC and final canonical URL.
3. **Archive integrity / ZIP 구조:** ZIP readable, safe file paths, required source-native Master, Deregistered, aircraft reference, engine reference files identified by deterministic names and unambiguous single choice.
4. **Authoritative source schema / 공식 필드 매핑:** FAA original field dictionary available and Master serial, model-code and N-number mappings independently verified (do not infer undocumented character positions).
5. **Outcome firewall / 결과 방화벽:** Deregistered source inspected **only for filename and structural header/field-layout metadata**, not its event rows or member identities; no future ZIP fetched.
6. **Master row validity / 원본 기본 행:** at least 90% of structural Master rows have source-valid field boundaries/record parsing under official CSV/TXT layout (invalid rows counted, not repaired).
7. **Qualified identity support / 복합식별 지지:** >=100,000 distinct baseline Master aircraft have nonblank source-valid compound `(manufacturer/model code, serial)` identity.
8. **Compound uniqueness / 복합키 유일성:** >=99.9% of source-valid nonblank compound identities occur once among baseline Master aircraft; ambiguous identities excluded rather than manual repaired.
9. **N-number reuse quantification / 번호 재사용:** all available validated year-to-year N-number→compound conflicting relationships are counted and never N-number-only joined; no unresolved collisions silently retained.
10. **Reference integrity / 모델 참조:** >=95% of qualified aircraft model codes exactly match a unique official make/model reference code; ambiguity excluded.
11. **Engine structural linkage / 엔진 참조:** engine-reference file is schema-parseable; non-outcome exact-reference qualification and missingness reported. No engine attributes may be used as an event proxy.
12. **Official historic support / 과거 관측:** verify official FAA 2020 and 2021 annual archived source identity, successful downloads, unambiguous ZIP member layouts, SHA/time evidence for both.
13. **Temporal identity alignment / 종적 일치:** >=10,000 distinct compound aircraft IDs consistently traceable between at least two validated official historic/current snapshots with no compound collision or fuzzy repair.
14. **Snapshot chronology / 출처 시점:** official collection/download timestamps and archive years are distinguishable; no claim that snapshot refresh equals dereg event date.
15. **Prospective at-risk baseline / 모집단:** at least 100,000 qualified, non-ambiguous *current* aircraft remain in an at-risk cohort (registration status needs source-native non-outcome eligibility, no future dereg info).
16. **Exposure independence / 독립 변수:** at least one distinct, documented non-outcome structural exposure family measurable for >=90% of qualified at-risk cohort, without using any dereg/event/accident/enforcement field.
17. **Safety, ethics, provenance / 안전성:** no owner names/addresses emitted; no paid/source-rights violation, no unauthorized redirection, no third-party identity joining, no output that identifies personal owners.
18. **Terminal declaration discipline / 판정:** 18 gate results and exact per-gate numerator/denominator, source SHA/URL, exception/transport notes and a signed outcome-blind finding are produced and durable before any N01 approval. Cost precisely 0 USD.

## Execution boundaries / 실행 금지사항

- No experimental future-event access, classifier, risk ranking, causal claim, safety-quality inference or unregistered alternative join; no exposure definition repair after observing support results.
- No automatic runner-up choice if FAA fails; return to separately authorized new portfolio screening.
- Do not promote a conditional Stage-0 feasibility score into factual FAA outcome discovery.
- F01 implementation must validate static/documented official endpoints and operator costs before actual download; if official host yields 403 in canonical free environment, stop after bounded lawful transport checks (no VPN/proxy/paid workaround).
- If 18/18 structural PASS: a separate N01 prospective support-and-opportunity contract must be frozen **before** any outcome opening.
- E01 active checkpoint and Issue #203 remain continuously authoritative. Distinct Track B Issue only.

**Initial disposition:** `FROZEN_F01_CONTRACT__NOT_EXECUTED`.  
**Monetary boundary:** `COST-001`, **0 USD**.
