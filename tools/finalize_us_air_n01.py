#!/usr/bin/env python3
"""Finalize PORTFOLIO-R10 and US-AIR-N01 without rerunning US-AIR effects."""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-11"
CHECKPOINT = "CHK-20260911-US-AIR-N01-LOW-NOVELTY-PORTFOLIO-RETURN"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    e01 = read("research/US-AIR-E01/RESULT.md")
    if "PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION" not in e01:
        raise RuntimeError("US-AIR-E01 canonical PASS missing")
    if "4.892129968812" not in e01 or "11.730815" not in e01:
        raise RuntimeError("US-AIR-E01 canonical numeric result mismatch")

    r10 = r'''---
id: PORTFOLIO-R10-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-11
issue: 91
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_gate: US-AIR-N01
next_issue: 92
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R10 Result — Post-Relationship Stage 0 Reselection
# PORTFOLIO-R10 결과 — 관계검증 이후 Stage 0 재선정

## Final selection / 최종 선정

**`SELECT_US_AIR_N01_EXACT_CONTRIBUTION_NOVELTY_PRACTICE`**

Selected gate: **Issue #92 `US-AIR-N01` — exact-contribution novelty and operational-practice assessment.**

This selection does not rerun or extend the favorable US-AIR-E01 effect. / 본 선정은 유리한 E01 효과를 재실행·확장하지 않는다.

## Why this uncertainty comes first / 왜 이 불확실성이 먼저인가

US-AIR-E01 is already `RELATIONSHIP_TESTED`, but `NOVELTY_ASSESSED` and `UTILITY_TESTED` remain unresolved. The project mission is innovation discovery, not accumulation of favorable p-values. / 프로젝트 목적은 유리한 p-value 축적이 아니라 혁신 탐색이다.

A bounded current-evidence refresh found direct precedent for precipitation/rain affecting flight/departure delay, including U.S. BTS-linked research, while FAA operational practice already treats weather as a central delay constraint. Therefore the highest-value immediate question is whether the exact US-AIR contribution adds something distinct enough to justify external-generalization work. / 강수-지연의 직접 선례와 현행 FAA 기상 대응이 존재하므로 일반화 재실험 전 정확한 기여의 신규성을 먼저 판정한다.

2026 temporal generalization is technically feasible in principle because BTS Marketing Carrier On-Time data are currently available through June 2026, but it is not selected automatically. / 2026 일반화는 데이터상 가능하지만 자동 선택하지 않는다.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; total /45. Scores are portfolio aids, not empirical innovation findings.

| Candidate | Mission bottleneck | Evidence contribution | Falsifiability / decision relevance | Evidence/unit diversity | Practical value | Zero-cost operability | Defensibility | Next-gate information gain | Low diminishing-return risk | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-AIR N01 novelty/practice** | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | **44** | **SELECT** |
| US-AIR untouched 2026 generalization | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 2 | **39** | HOLD_PENDING_NOVELTY |
| C-EU-001 Cross-National Grid Stress | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 5 | **39** | HOLD_HIGH_VALUE_OPERABILITY |
| C-CA-002 Grain Pressure × Rail Dwell | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 4 | 2 | **37** | HOLD_REDESIGN_GEOGRAPHY |
| AU-NEM continuation | 5 | 5 | 5 | 2 | 5 | 5 | 4 | 3 | 1 | **35** | PRESERVE_JOIN__NO_AUTO_CONTINUATION |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| JP-PORT continuation | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 2 | 0 | **33** | VALIDATED_RESULT__NO_AUTO_TUNING |

## Evidence used for selection / 선정에 사용한 증거

- Borsky & Unterberger (2019), *Economics of Transportation*, DOI 10.1016/j.ecotra.2019.02.002: 2.14 million departures from ten large U.S. airports; precipitation/wind effects on departure delay.
- Yablonsky et al. (2014), *Journal of Airline and Airport Management*, DOI 10.3926/jairm.22: BTS/RITA flight-delay data + NOAA precipitation + traffic volume at ATL.
- FAA Weather Delay FAQ: weather is a dominant operational delay factor and is incorporated into traffic-flow planning.
- BTS current Marketing Carrier On-Time Performance: latest available data June 2026.

## Exact next gate / 정확한 다음 gate

Execute only `US-AIR-N01` as a bounded novelty/current-practice assessment. Do not fit another US-AIR model inside R10. / R10에서는 새 모델을 적합하지 않는다.

Incremental monetary cost remained **0 USD**.
'''

    dec127 = r'''---
id: DEC-127
type: decision
created: 2026-09-11
status: ACTIVE
---

# DEC-127 — Select novelty/practice assessment before US-AIR generalization
# DEC-127 — US-AIR 일반화 전 신규성·현행관행 평가 선정

## Decision / 결정

PORTFOLIO-R10 selects **Issue #92 `US-AIR-N01`** as the next bounded gate:

**`SELECT_US_AIR_N01_EXACT_CONTRIBUTION_NOVELTY_PRACTICE`**

## Rationale / 근거

US-AIR already has a strong preregistered relationship result. Current peer-reviewed and official evidence contains close precipitation→flight/departure-delay precedent and weather-aware operational practice. Before spending research capacity on an untouched 2026 generalization, the project must determine whether the exact contribution is scientifically or operationally distinct enough to warrant continuation. / 강수→지연 선례가 존재하므로 일반화 전 정확한 기여의 신규성을 먼저 판정한다.

A favorable E01 result is not itself a continuation criterion. / 유리한 E01 결과 자체는 후속진행 근거가 아니다.

## Boundary / 경계

N01 is an innovation-assessment gate only. No new effect model, threshold, lag, airport subset, carrier ranking, causal claim or predictive claim is authorized.

Incremental monetary cost remains **0 USD**.
'''

    n01_readme = r'''---
id: US-AIR-N01
issue: 92
type: innovation-assessment
created: 2026-09-11
state: COMPLETED_LOW_NOVELTY
parent: US-AIR-E01
portfolio_decision: DEC-127
final_decision: DEC-128
claim: CLM-138
incremental_monetary_cost_usd: 0
---

# US-AIR-N01 — Exact-Contribution Novelty & Operational-Practice Assessment
# US-AIR-N01 — 정확한 기여 신규성·현행 운영관행 평가

## Exact contribution assessed / 평가대상

The assessment is limited to the contribution actually established by E01: a 2025, 255-airport U.S. public BTS + NOAA LCDv2 airport-day panel in which same-calendar-date `DailyPrecipitation` is positively associated with mean `DepDelayMinutes` after airport FE, FlightDate FE and scheduled-volume control, with preregistered clustered uncertainty and a reproducible zero-cost workflow.

It does not assess untested causal, forecasting, propagation, ranking or utility claims.

## Method / 방법

Bounded evidence search through 2026-09-11, prioritizing peer-reviewed research and current U.S. official operational material. Absence from this bounded search is not evidence of global absence. / 제한 검색의 미발견을 전세계적 부재 증거로 취급하지 않는다.

See `SOURCE_MATRIX.csv` and `RESULT.md`.
'''

    n01_result = r'''---
id: US-AIR-N01-RESULT
type: novelty-operational-practice-assessment
created: 2026-09-11
issue: 92
state: COMPLETED
final_gate: LOW_NOVELTY_CORE_RELATIONSHIP_KNOWN
decision: DEC-128
claim: CLM-138
relationship_recomputed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-N01 Result
# US-AIR-N01 결과

## Final gate / 최종 판정

**`LOW_NOVELTY_CORE_RELATIONSHIP_KNOWN`**

The exact US-AIR-E01 implementation is useful as a large, reproducible public-data asset, but the **core scientific relationship — precipitation/adverse weather is associated with flight/departure delay — is not novel on the bounded evidence reviewed**. / US-AIR-E01 구현은 대규모 재현가능 공개데이터 자산으로 유용하지만, 핵심 과학관계 자체는 검토한 근거상 신규하지 않다.

## Direct prior-work overlap / 직접 선행연구 중첩

### 1. Borsky & Unterberger, 2019 — strong direct overlap

*Bad weather and flight delays: The impact of sudden and slow onset weather events*, Economics of Transportation 18, 10–26, DOI `10.1016/j.ecotra.2019.02.002`.

The study used **2.14 million flight departures from ten large U.S. airports (2012–2017)** and explicitly estimated precipitation and wind impacts on **departure delay**, reporting increases up to 23 minutes depending on weather type/intensity.

Overlap: U.S. airports + precipitation + departure delay + statistical estimation. This is direct prior art for the core E01 relationship.

### 2. Yablonsky et al., 2014 — strong data-combination overlap

*Flight delay performance at Hartsfield-Jackson Atlanta International Airport*, Journal of Airline and Airport Management, DOI `10.3926/jairm.22`.

The study used **2.8 million ATL flights**, BTS/RITA delay data, **NOAA precipitation**, FAA delay information and traffic volume; it reported a repeatable delay pattern associated primarily with precipitation frequency/amount and flight volume.

Overlap: public U.S. flight data × NOAA precipitation × traffic volume × delay.

### 3. Ramadhani et al., 2026 — current mechanism overlap

*Analysis of the Impact of Weather Conditions on Flight Delays at Hartsfield–Jackson Atlanta International Airport (ATL) During 2013–2023*, International Journal of Climatology, DOI `10.1002/joc.70357`.

The study integrates BTS operational delay records with atmospheric data and reports precipitation as a dominant positive predictor of delays.

### 4. Other close evidence

- A 2023 Journal of Big Data study merges flight and weather data for ICN, JFK and MDW to predict weather-caused departure delay.
- A 2026 Journal of Air Transport Management study of 117,218 Beijing–Shanghai flights reports a strong positive rainfall-intensity/delay relationship across hourly, daily and monthly scales.

These are not exact replications of E01 but reduce any plausible claim that the precipitation-delay mechanism or flight×weather data integration is new.

## Current operational-practice overlap / 현행 운영관행 중첩

FAA material already treats weather as a major National Airspace System delay driver. Its Weather Delay FAQ reports weather as the largest cause of system-impacting delay in the cited 2017–2023 window and describes weather prediction as an input to traffic-flow planning. BTS also maintains causal delay reporting categories that explicitly include weather and predicted-weather-related cancellations/delays.

Therefore the E01 same-day association does not introduce a new operational concept that weather should be considered in delay management. / E01은 기상을 지연관리에서 고려해야 한다는 새로운 운영개념을 제시한 것이 아니다.

## Dimension assessment / 차원별 평가

| Dimension | Assessment | Reason |
|---|---|---|
| Mechanism novelty | **LOW** | precipitation/weather → delay directly established in prior studies |
| Data-combination novelty | **LOW** | BTS/RITA flight records × NOAA/weather data combinations already exist |
| Geographic/scale novelty | **POSSIBLE INCREMENT** | 255-airport panel is broader than the close examples reviewed, but bounded search cannot prove unique national coverage |
| Method novelty | **LOW / NOT ESTABLISHED** | fixed effects and clustered panel association are standard tools; no new estimator claimed |
| Operational-practice novelty | **LOW** | FAA/BTS already treat weather as a central delay/capacity factor |
| Reproducibility contribution | **MEANINGFUL INCREMENT** | 12/12 hashes, deterministic airport-station mapping, preregistration, open public route and derived manifests make the result unusually auditable |

## What remains genuinely useful / 남는 가치

The defensible incremental contribution is **reproducibility + breadth + evidence governance**, not discovery of a new precipitation-delay mechanism. / 방어 가능한 증분기여는 새 메커니즘 발견이 아니라 재현성·범위·증거거버넌스다.

This can still be valuable as:
- a reusable benchmark for later aviation resilience hypotheses;
- a transparent baseline against which a genuinely new predictor, propagation mechanism or decision intervention could be tested **if separately selected before outcomes**;
- a demonstration of the research engine's ability to reject inflated novelty claims after a statistically strong result.

## Utility boundary / 효용 경계

`UTILITY_TESTED` remains **UNKNOWN**. E01 used same-day realized precipitation and did not test information available at a named decision time, forecast skill, intervention benefit, or failure cost. / 구체적 의사결정 시점·예측·개입 효익을 검증하지 않았으므로 효용은 미검증이다.

## Branch-stop / 분기 중단

Do **not** automatically run 2026 external generalization merely because E01 passed. / E01 PASS만으로 2026 일반화를 자동실행하지 않는다.

Return to Stage 0. A US-AIR descendant may re-enter only if it proposes a separately testable uncertainty with stronger mission value — for example a decision-time forecast increment, propagation mechanism, resilience intervention, or other contribution that competes successfully against independent portfolio candidates. / US-AIR 후속은 더 강한 미션가치를 가진 별도 불확실성일 때만 다시 경쟁한다.

Incremental monetary cost remained **0 USD**.
'''

    dec128 = r'''---
id: DEC-128
type: decision
created: 2026-09-11
status: ACTIVE
---

# DEC-128 — Finalize US-AIR-N01 as low novelty; stop automatic generalization
# DEC-128 — US-AIR-N01 낮은 신규성 확정·자동 일반화 중단

## Decision / 결정

Finalize Issue #92 as:

**`LOW_NOVELTY_CORE_RELATIONSHIP_KNOWN`**

US-AIR is now `NOVELTY_ASSESSED` for the exact E01 contribution, with **LOW core novelty** and a meaningful but narrower reproducibility/scale increment. / 정확한 E01 기여는 신규성 평가 완료이며 핵심 신규성은 낮고 재현성·범위의 증분기여가 남는다.

## Basis / 근거

Direct precedent includes:
- U.S. multi-airport precipitation/wind → departure-delay estimation (Borsky & Unterberger, 2019);
- BTS/RITA + NOAA precipitation + traffic-volume delay analysis at ATL (Yablonsky et al., 2014);
- current BTS + atmospheric precipitation-delay evidence at ATL (Ramadhani et al., 2026);
- additional flight×weather prediction and rainfall-delay studies;
- FAA/BTS operational frameworks already treating weather as a major delay constraint/cause.

The 255-airport open reproducible implementation may be broader than examples found, but the bounded search does not justify claiming unique national-scale novelty. / 255개 공항 규모는 증분기여 가능성이 있으나 제한검색만으로 독점적 신규성을 주장하지 않는다.

## Promotion boundary / 승격 경계

Do not promote US-AIR to `INNOVATION_CANDIDATE` or `UTILITY_TESTED`. Do not automatically execute external generalization. / 혁신후보·효용검증 승격 및 자동 외적일반화 금지.

Return to Stage 0. Any future US-AIR descendant must compete against independent branches and target a distinct unresolved contribution rather than re-confirming precipitation-delay association. / 향후 후속은 독립 branch와 다시 경쟁하고 강수-지연 재확인이 아닌 별도 기여를 겨냥해야 한다.

Incremental monetary cost remains **0 USD**.
'''

    claim138 = r'''---
id: CLM-138
type: claim
created: 2026-09-11
state: DERIVED_ASSESSMENT_VALIDATED
---

# CLM-138 — US-AIR E01 core novelty is low on bounded prior-work/practice evidence
# CLM-138 — 제한 선행연구·관행 근거상 US-AIR E01 핵심 신규성 낮음

A bounded evidence assessment through 2026-09-11 finds close prior research that already links precipitation/weather to flight/departure delay, including U.S. multi-airport analysis and BTS/RITA + NOAA-style flight-weather integration, while current FAA/BTS operational practice already treats weather as a major delay constraint/cause. / 2026-09-11까지 제한 증거검토에서 강수·기상과 출발지연의 직접 선행연구 및 현행 FAA/BTS 운영관행이 확인된다.

Therefore the exact E01 contribution resolves to **`LOW_NOVELTY_CORE_RELATIONSHIP_KNOWN`**. Its defensible increment is primarily the breadth and auditable reproducibility of the 255-airport public-data workflow, not discovery of a new precipitation-delay mechanism. / 방어 가능한 증분은 새 메커니즘보다 255개 공항 공개데이터 workflow의 범위·감사가능 재현성이다.

This bounded assessment does not prove that no publication anywhere uses the exact same 255-airport specification, and it does not assess utility or external generalization. / 제한검색은 전세계 exact 동일논문 부재를 증명하지 않으며 효용·외적일반화도 검증하지 않는다.

**Verification:** `V2_BOUNDED_PEER_REVIEWED_AND_OFFICIAL_PRACTICE_ASSESSMENT`.

Evidence: `research/US-AIR-N01/SOURCE_MATRIX.csv`; `research/US-AIR-N01/RESULT.md`; Issue #92.
'''

    source_rows = [
        ["PW-01","peer-reviewed","Borsky & Unterberger","2019","Bad weather and flight delays: The impact of sudden and slow onset weather events","Economics of Transportation","10.1016/j.ecotra.2019.02.002","U.S.; ten large airports","2.14M departures; 2012-Sep 2017","precipitation/wind/temperature","departure delay","DIRECT_STRONG","Core U.S. precipitation-to-departure-delay mechanism already estimated"],
        ["PW-02","peer-reviewed","Yablonsky et al.","2014","Flight delay performance at Hartsfield-Jackson Atlanta International Airport","Journal of Airline and Airport Management","10.3926/jairm.22","ATL, U.S.","2.8M flights; 2005-2011","NOAA precipitation + traffic volume","flight delay","DIRECT_STRONG","BTS/RITA flight data plus NOAA precipitation and traffic-volume overlap"],
        ["PW-03","peer-reviewed","Ramadhani et al.","2026","Analysis of the Impact of Weather Conditions on Flight Delays at Hartsfield–Jackson Atlanta International Airport (ATL) During 2013–2023","International Journal of Climatology","10.1002/joc.70357","ATL, U.S.","2013-2023","precipitation and other meteorological variables","flight delays","DIRECT_STRONG","Current BTS plus atmospheric-data study reports precipitation as dominant positive predictor"],
        ["PW-04","peer-reviewed","Journal of Big Data study","2023","Prediction of flight departure delays caused by weather conditions adopting data-driven approaches","Journal of Big Data","https://link.springer.com/article/10.1186/s40537-023-00867-5","ICN/JFK/MDW","2010-2021","flight + weather variables","departure-delay prediction","CLOSE","Shows established flight-weather data integration including two U.S. airports"],
        ["PW-05","peer-reviewed","Gan et al.","2026","How rainfall and air pollution influence flight delays and its associated economic losses","Journal of Air Transport Management","10.1016/j.jairtraman.2025.102929","Beijing-Shanghai","117,218 flights; 2016-2018","rainfall intensity + pollution","flight delay","CLOSE","Recent independent geography confirms rainfall-delay relationship across multiple time scales"],
        ["OP-01","official-practice","Federal Aviation Administration","current accessed 2026-09-11","FAQ: Weather Delay","FAA","https://www.faa.gov/nextgen/programs/weather/faq","U.S. NAS","2017-May 2023 cited delay share","weather / forecasts","system-impacting delay and traffic-flow planning","DIRECT_PRACTICE","Weather already treated as dominant operational delay constraint and forecast input"],
        ["OP-02","official-practice","Bureau of Transportation Statistics","2026","Technical Directive #40: Reporting On-Time Performance 2026","BTS","https://www.bts.gov/explore-topics-and-geography/modes/aviation/number-40-technical-directive-reporting-time","U.S. domestic reporting","2026 rules","weather causal categories including predicted weather","delay/cancellation cause reporting","DIRECT_PRACTICE","Weather is already an explicit operational reporting/corrective-action category"],
        ["OP-03","official-data","Bureau of Transportation Statistics","2026","Marketing Carrier On-Time Performance","BTS TranStats","https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=&gnoyr_VQ=FGK","U.S.","latest June 2026","on-time/delay fields","flight performance","GENERALIZATION_AVAILABLE","Untouched 2026 temporal data exist, but generalization is deferred pending novelty assessment"],
    ]
    out = io.StringIO()
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(["evidence_id","type","authors_or_org","year","title","venue","doi_or_url","geography","sample_or_period","weather_input","outcome","overlap","assessment_note"])
    writer.writerows(source_rows)
    source_matrix = out.getvalue()

    write("research/PORTFOLIO-R10/RESULT.md", r10)
    write("registry/DEC-127.md", dec127)
    write("research/US-AIR-N01/README.md", n01_readme)
    write("research/US-AIR-N01/RESULT.md", n01_result)
    write("research/US-AIR-N01/SOURCE_MATRIX.csv", source_matrix)
    write("registry/DEC-128.md", dec128)
    write("registry/CLM-138.md", claim138)

    # Link the novelty assessment back to the empirical result without changing E01's gate.
    if "## Post-E01 novelty assessment / E01 이후 신규성 평가" not in e01:
        e01 += r'''

## Post-E01 novelty assessment / E01 이후 신규성 평가

`US-AIR-N01` / `DEC-128` subsequently assesses the exact E01 contribution as **`LOW_NOVELTY_CORE_RELATIONSHIP_KNOWN`**. This does not alter the empirical E01 PASS; it separates empirical validity from novelty. / N01은 E01의 실증 PASS를 변경하지 않고 신규성을 별도로 낮음으로 판정한다.

Defensible incremental value remains the breadth and reproducibility of the public-data workflow. `UTILITY_TESTED` and `GENERALIZATION_TESTED` remain unresolved.
'''
        write("research/US-AIR-E01/RESULT.md", e01)

    decision_log = read("registry/DECISION_LOG.md")
    if "[DEC-127]" not in decision_log:
        decision_log += "\n- [DEC-127](DEC-127.md): R10 selects US-AIR-N01 novelty/current-practice assessment before generalization / 일반화 전 신규성·현행관행 평가 선정.\n"
    if "[DEC-128]" not in decision_log:
        decision_log += "- [DEC-128](DEC-128.md): finalize US-AIR-N01 as LOW_NOVELTY_CORE_RELATIONSHIP_KNOWN and stop automatic generalization / 낮은 신규성 확정·자동 일반화 중단.\n"
    write("registry/DECISION_LOG.md", decision_log)

    ledger = read("registry/CLAIM_LEDGER.md")
    claim_row = "| `CLM-138` | Bounded peer-reviewed/official-practice evidence shows the US-AIR E01 core precipitation→delay relationship is already established; exact contribution is `LOW_NOVELTY_CORE_RELATIONSHIP_KNOWN`, with breadth/reproducibility as the main increment. / 강수→지연 핵심관계는 기존 근거에 존재하며 신규성은 낮고 범위·재현성이 주 증분. | `OBSERVED/DERIVED_ASSESSMENT` | `V2_BOUNDED_PEER_REVIEWED_AND_OFFICIAL_PRACTICE_ASSESSMENT` | `research/US-AIR-N01/RESULT.md`; `SOURCE_MATRIX.csv`; `registry/CLM-138.md`; Issue #92 | 2026-09-11 | active-novelty-low |\n\n"
    if "`CLM-138`" not in ledger:
        marker = "## Rule / 규칙"
        if marker in ledger:
            ledger = ledger.replace(marker, claim_row + marker)
        else:
            ledger += "\n" + claim_row
        write("registry/CLAIM_LEDGER.md", ledger)

    status = r'''---
checkpoint_id: CHK-20260911-US-AIR-N01-LOW-NOVELTY-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 92
last_completed_research: US-AIR-N01
last_decision: DEC-128
updated: 2026-09-11
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_AIR_RELATIONSHIP_PASS__NOVELTY_LOW__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

## Latest completed assessment / 최신 완료 평가

US-AIR-E01 remains empirically:
**`PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION`**.

US-AIR-N01 now separately resolves novelty as:
**`LOW_NOVELTY_CORE_RELATIONSHIP_KNOWN`**.

The core precipitation→delay relationship and its operational relevance have direct prior research/current-practice precedent. The defensible incremental contribution is primarily the 255-airport scope, reproducible public-data join, preregistration and evidence governance. / 핵심 관계는 알려져 있으며 증분가치는 범위·재현성·증거거버넌스 중심이다.

## Evidence ladder / 증거단계

- JOIN_READY: PASS
- RELATIONSHIP_TESTED: PASS for one 2025 contemporaneous precipitation-delay association
- GENERALIZATION_TESTED: **NO**
- NOVELTY_ASSESSED: **YES — LOW core novelty**
- UTILITY_TESTED: **NO**
- INNOVATION_CANDIDATE: **NO**

## Exact next action / 정확한 다음 행동

Return to **Stage 0 portfolio control** with no active research Issue. / 활성 연구 Issue 없이 Stage 0로 복귀한다.

Do not automatically run 2026 US-AIR generalization. The next gate must compare independent portfolio candidates against any US-AIR descendant that targets a genuinely distinct decision-time, propagation, resilience or utility uncertainty. / 2026 일반화 자동실행 금지; 다음 gate는 독립 후보와 더 구체적인 US-AIR 후속을 다시 경쟁시킨다.

Incremental monetary cost remains **0 USD**.
'''

    handoff = r'''---
checkpoint_id: CHK-20260911-US-AIR-N01-LOW-NOVELTY-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 92
last_completed_research: US-AIR-N01
last_decision: DEC-128
updated: 2026-09-11
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

PORTFOLIO-R10 selected and completed `US-AIR-N01` after the E01 relationship PASS.

Final novelty gate:
**`LOW_NOVELTY_CORE_RELATIONSHIP_KNOWN`**.

Do not rerun E01 or N01 by default. / E01/N01 기본 재실행 금지.

Canonical evidence:
- `research/PORTFOLIO-R10/RESULT.md`;
- `registry/DEC-127.md`;
- `research/US-AIR-N01/RESULT.md`;
- `research/US-AIR-N01/SOURCE_MATRIX.csv`;
- `registry/CLM-138.md`;
- `registry/DEC-128.md`.

## Interpretation / 해석

US-AIR has a valid preregistered 2025 relationship result but the core precipitation-delay mechanism is already represented in prior U.S. research and current FAA/BTS practice. Its remaining defensible increment is reproducibility/breadth, not a new mechanism. / 실증관계는 유효하나 핵심 메커니즘 신규성은 낮다.

`GENERALIZATION_TESTED` and `UTILITY_TESTED` remain unresolved. Do not promote to `INNOVATION_CANDIDATE`.

## Exact next action / 정확한 다음 행동

Return to Stage 0 with **no active research Issue**. / 활성 연구 Issue 없이 Stage 0로 복귀한다.

The next portfolio comparison should favor a genuinely new bottleneck/relationship opportunity unless a US-AIR descendant specifies a distinct named decision and measurable incremental utility or an untouched generalization whose value exceeds independent alternatives. / 다음에는 독립 신규 기회를 우선 비교하되 US-AIR은 명시적 의사결정 효익 또는 고가치 untouched 일반화일 때만 재진입한다.

Cost remains **0 USD**.
'''

    checkpoint = {
        "checkpoint_id": CHECKPOINT,
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 92,
        "last_completed_research": "US-AIR-N01",
        "last_decision": "DEC-128",
        "updated": TODAY,
    }

    write("STATUS.md", status)
    write("context/SESSION_HANDOFF.md", handoff)
    write("context/checkpoint.json", json.dumps(checkpoint, ensure_ascii=False, indent=2))

    print("US_AIR_N01_FINALIZED;gate=LOW_NOVELTY_CORE_RELATIONSHIP_KNOWN;next=STAGE_0")


if __name__ == "__main__":
    main()
