---
id: US-EPA-XMEDIA-E01-RESULT
type: preregistered-paired-outcome-experiment
created: 2026-09-17
issue: 152
state: COMPLETED_NO_PREREGISTERED_POSITIVE
gate: NO_PREREGISTERED_POSITIVE_US_EPA_XMEDIA_E01_RELATIONSHIP
source_run: 35168068999
staging_commit: 3852773636146fb48414c98a825d6bedb8cfd6c1
incremental_monetary_cost_usd: 0
---

# US-EPA-XMEDIA-E01 Result — no preregistered positive relationship established

**`NO_PREREGISTERED_POSITIVE_US_EPA_XMEDIA_E01_RELATIONSHIP`**

Immutable Run `35168068999` executed the outcome contract frozen before Issue creation at `46938afda3fbeaf9349a3c508502f8d4a3c973a3`, bound to the N01 307-pair manifest `19e1b3a1963fe008811aa230336e12ec69a348b03cf37bd656ea9d3fba8e5aaf`.

## Primary preregistered result / 사전등록 1차 결과

- frozen matched pairs: **307**
- HIGH 2024 E90 events: **17 / 307 (5.54%)**
- LOW 2024 E90 events: **11 / 307 (3.58%)**
- paired risk difference, HIGH − LOW: **+0.0195 (+1.95 percentage points)**
- discordant HIGH=1 / LOW=0 (`b`): **12**
- discordant HIGH=0 / LOW=1 (`c`): **6**
- discordant pairs: **18**
- exact two-sided McNemar/binomial p-value: **0.237885**
- preregistered materiality floor: **+5 percentage points**

The point estimate is positive, but it is below the frozen +5 percentage-point materiality floor and the exact paired test is not statistically significant at p<0.05. Therefore the preregistered positive gate is not met.

This result does **not** establish that no association exists in every population or endpoint. It establishes only that this frozen 307-pair, calendar-2024 E90 experiment did not establish the preregistered positive relationship.

## Execution integrity / 실행 무결성

- exact pair membership changed: **false**
- endpoint/window/threshold changed: **false**
- facility-level outcome labels persisted: **false**
- official matched-state source rows scanned: **36,755,059**
- rows for frozen NPDES IDs encountered: **30,888**
- malformed nonblank candidate E90 dates excluded: **0**
- DMR values/limits opened: **false**
- RCRA violation/enforcement outcomes opened: **false**
- secondary endpoint computed: **false**
- facility ranking / enforcement-targeting score: **not computed**
- incremental monetary cost: **0 USD**

## Interpretation boundary / 해석 경계

The result is observational and noncausal. The positive point estimate must not be described as a confirmed cross-media relationship, and the non-significant result must not be reframed as evidence of a protective effect. No named facility inference or enforcement recommendation is authorized.

## Exact next action / 정확한 다음 행동

Terminate this EPA descendant chain without rescue. Do **not** change E90 to another violation code, widen the outcome window, lower materiality/significance thresholds, rematch facilities, or mine secondary endpoints. Return to an independent `PORTFOLIO-R35` Stage-0 reselection under the standing mission rubric and zero-cost rule.
