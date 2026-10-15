---
id: PORTFOLIO-R57-REVALIDATION
created: 2026-10-16
issue: 214
contract_commit: 602c33b6f53c6ae180408fa43ac88a90a6ff7c50
status: BOUNDED_SOURCE_AND_CANONICAL_OVERLAP_REVIEW
candidate_future_event_memberships_opened: false
incremental_monetary_cost_usd: 0
---

# R57 — Pre-score official source & canonical-equivalence revalidation / 점수 전 출처·기존 연구 중복 확인

## Firewall / outcome 방화벽

Only official agency **landing pages, data dictionaries and documented download architecture**, the preexisting GitHub history and candidate structural feasibility were reviewed. No candidate-level event values, latest incident/recall/deregistration memberships, prospective deltas, rates, association signs or effect sizes were observed, downloaded or scored.

**This is not scientific F01, N01 or E01**, and cannot amend frozen US-CMS-NPI-E01.

## A. FAA daily aircraft registration / FAA 항공기 등록

**Official source:** https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download

- **OBSERVED documentation:** FAA directly offers ~60MB releasable full aircraft registration database, refreshed daily at 11:30pm US Central, containing Master, Deregistered Aircraft, document index, manufacturer/model and engine references. Download documentation states permissible fields may be blank without constituting errors.
- **Structural inference (not yet empirically proven):** same bundle's Master ↔ Deregistered Aircraft and make/model codes permit a testable exact identity candidate using **source-native manufacturer/model + serial number**, not N-number alone. Exact temporal stability, collision frequency, and coverage are UNKNOWN until F01.
- **Governance overlap:** Prior `US-FAA-AIP-F01` studied *airport AIP grants vs BTS delays*, terminated at state-concordance 16/17; it is **not** an aircraft-registration/airframe deregistration dataset or endpoint. Earlier `US-FAA-AIR-001/002` were held Stage 0, not experimentally executed; this is a **new independent selection** and does not revive a failed aircraft F01.
- **Blocking F01 gate:** no assumption that compound identity works, that a deregistration means crash or operational failure, or that a daily full replacement preserves complete historical change logs. The source-native event date and reason, longitudinal export, type/personal-info redaction, parent→event coverage must be proved first.
- **Cost:** free public downloadable material; no ZIP body downloaded during R57 revalidation.

## B. NHTSA recalls / NHTSA 리콜

**Official source:** https://www.nhtsa.gov/nhtsa-datasets-and-apis

- **OBSERVED documentation:** direct `FLAT_RCL_POST_2010.zip` official recall campaign ZIP and `RCL.txt` field dictionary, plus public campaign lookup; the agency describes the recall series as daily updated and distinguishes vehicles, tires, child safety seats and equipment.
- **Structural inference:** a campaign ID is a source-native recall identifier, **not** a unique engineering vehicle product denominator. Model year/make/model alone may combine platforms, variants and equipment; prospective product population, at-risk denominator and assignment ambiguity are UNPROVEN.
- **Governance overlap:** Historical `US-NHTSA-MC-F01` relates to a different motor-carrier/data route; a new `US-NHTSA-REC` must establish canonical event-source novelty before the F01. The R54 recall prospect was held at Stage 0, not automatically promotable.
- **Blocking F01 gate:** if exact stable product-level population denominator cannot be obtained without defect-precursor complaints/investigations/manufacturer correspondence, reject rather than report a spurious recall-rate predictor.
- **Cost:** free agency published files; no recall rows opened for this scorecard.

## C. FDA medical devices / FDA 기기

**Official source (independently corrected from a deliberately nonqualifying frozen note):**
- https://open.fda.gov/apis/device/registrationlisting/ — device establishments and listings; source states a monthly-updated API and covered years.
- https://open.fda.gov/apis/device/enforcement/ — recall enforcement reports and report dates.
- https://open.fda.gov/apis/device/recall/ — separately described device recall publication semantics; FDA cautions against using this source to track a recall lifecycle.
- https://open.fda.gov/data/downloads/ — downloadable device datasets; source explicitly warns historical records may be revised.

**IMPORTANT:** frozen R57 universe cited `/food/enforcement/` as a **non-device example to exclude**. This revalidation confirms that it cannot substitute for `/device/enforcement/`. This is a **source correction before scoring**; frozen contract is not edited.

- **Structural inference:** registration/listing establishment identity to recalled specific marketed product is many-to-many and versioned; exact deterministic unit linkage is UNPROVEN. Monthly registration and later classified enforcement report dates differ in ascertainment time.
- **Governance overlap:** `PORTFOLIO-R49` previously held device recall due to establishment attribution ambiguity; this risk remains. No reinterpretation of a public API as evidence that an exact device identity join exists.
- **Blocking F01 gate:** exclude if only a product-code/ecological join is possible; do not conflate a device recall with device-level failure risk or establishment quality.
- **Cost:** documented public API and downloads; no outcome rows fetched.

## Fatal branch-equivalence and Mission-ROI review / 종료 branch 복구 방지

Existing terminal routes have been inspected before scoring:
- `US-PHMSA-PIPE-F01` [RESULT](../US-PHMSA-PIPE-F01/RESULT.md): two official-host HTTP 403 transport failures, scientific gate **not executed**, next workaround prohibited.
- `US-FCC-ULS-F01` [RESULT](../US-FCC-ULS-F01/RESULT.md): 9/18 frozen science gates PASS, **terminal scientific HOLD**, same service-family re-entry prohibited.
- `US-FAA-AIP-F01` [RESULT](../US-FAA-AIP-F01/RESULT.md): 16/17 PASS, no BTS outcomes opened, state concordance below frozen threshold; not the aircraft registry route.

No scored candidate is materially identical to these previously terminal experiments on data source, unit and event all together. This does **not** mean each new candidate is operationally viable.

## Pre-score eligibility / 점수 직전 판단

| Candidate | Official source pages | Binary row access proven by new execution | Exact at-risk identity proven | Prior terminal equivalence | Eligible for **F01 feasibility consideration** |
|---|---|---|---|---|---|
| FAA AIR | yes | **NO** (download described, not executed) | NO — compound key untested | none exact | **conditional** |
| NHTSA REC | yes | NO (direct ZIP described, not executed) | NO — denominator ambiguous | none exact | **conditional** |
| FDA DEV | yes | NO (API/download described, not executed) | NO — establishment/product join ambiguous | old stage0 hold only | **conditional** |

**No eligibility is empirically declared PASS.** The immutable Stage-0 scorecard may select only a *candidate for structural F01 feasibility* and must require actual exact identity and acquisition verification before any downstream experimental access. R57 is secondary while E01 remains the sole canonical active checkpoint. Incremental cost **0 USD**.
