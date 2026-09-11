#!/usr/bin/env python3
"""Finalize US-WATERWAY-F01 from committed outcome-blind evidence only.

No external data are fetched and no delay/hydrology magnitudes are read.
"""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'research'/'US-WATERWAY-F01'
REG=ROOT/'registry'
CTX=ROOT/'context'
TODAY='2026-09-11'
CLAIM='CLM-141'
DECISION='DEC-135'
ISSUE=98
GATE='PASS_US_WATERWAY_F01_JOIN_READY'
CHECKPOINT='CHK-20260911-US-WATERWAY-F01-PASS-PORTFOLIO-RETURN'


def need(path:Path, text:str):
    if text not in path.read_text(encoding='utf-8'):
        raise SystemExit(f'missing required evidence: {path} :: {text}')

def main():
    annual=(R/'ANNUAL_USAGE_SESSION_DIAGNOSTIC.md').read_text(encoding='utf-8')
    toc=json.loads((R/'USAGE_TOC_PREFLIGHT.json').read_text(encoding='utf-8'))
    cross=json.loads((R/'HISTORICAL_HYDROLOGY_CROSSWALK.json').read_text(encoding='utf-8'))
    hydro=json.loads((R/'HYDROLOGY_METADATA_PREFLIGHT_V2.json').read_text(encoding='utf-8'))
    source=json.loads((R/'SOURCE_ROUTE_DIAGNOSTIC.json').read_text(encoding='utf-8'))

    for y in ['2018','2019','2020']:
        if y not in annual: raise SystemExit(f'annual route missing overlap year {y}')
    for s in ['Average Delay','processing-time label present: **True**','This report summarizes usage metrics for each lock']:
        if s not in annual: raise SystemExit(f'annual route missing schema signal: {s}')
    if toc.get('lock_identity_unique_count',0) < 30:
        raise SystemExit('historical usage lock identities below frozen minimum')
    if cross.get('crosswalk_matched_count',0) < 25 or cross.get('crosswalk_unmatched_count') != 0:
        raise SystemExit('historical↔USGS deterministic crosswalk below frozen minimum')
    if hydro.get('qualified_matches',0) < 25 or hydro.get('target_overlap') != ['2018-01-01','2020-12-31']:
        raise SystemExit('USGS metadata support below frozen minimum/same interval')
    layer=source.get('lock_layer',{})
    if layer.get('feature_count',0) < 30:
        raise SystemExit('machine-readable public lock coordinate layer below minimum')
    if any([
        toc.get('boundary',{}).get('numeric_outcome_cells_read'),
        cross.get('boundary',{}).get('delay_magnitudes_parsed'),
        cross.get('boundary',{}).get('hydrology_values_parsed'),
        hydro.get('boundary',{}).get('delay_magnitudes_parsed'),
        hydro.get('boundary',{}).get('hydrology_values_parsed'),
        hydro.get('boundary',{}).get('relationship_computed'),
    ]):
        raise SystemExit('outcome-blind boundary violated')

    result=f'''---
id: US-WATERWAY-F01-RESULT
type: outcome-blind-join-feasibility-result
created: {TODAY}
issue: {ISSUE}
state: COMPLETED_PASS
final_gate: {GATE}
decision: {DECISION}
claim: {CLAIM}
delay_magnitudes_parsed: false
hydrology_values_parsed: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-WATERWAY-F01 Result / 결과

## Final gate / 최종 판정

**`{GATE}`**

The frozen source/identity/date-support gate passes without parsing any lock-delay magnitude or hydrologic observation value. / lock 지연값·수문 관측값을 열지 않고 source·identity·기간지원 gate를 통과했다.

## Verified structure / 검증 구조

- Official Corps Locks Annual Usage public route is HTTP 200, describes usage metrics **for each lock**, exposes annual labels **2016–2025**, and includes `Average Delay` plus processing-time schema labels.
- The official historical Public Lock Usage XLSX (`2959.xlsx`) is reproducibly downloadable, SHA-256 `0db8e4ae602bb60fea029a17a3c39929fe58cef6cc46b6f05bd1f45c4088f90f`, and its TOC contains **{toc['lock_identity_unique_count']}** unique lock identities with `Waterway` and `Lock` columns.
- The public USACE lock feature layer exposes **{layer.get('feature_count')}** lock features with stable machine-readable identity/location fields.
- Existing USGS metadata qualification provides **{hydro['qualified_matches']}** lock↔monitoring-location matches with Daily `00060` and/or `00065` metadata covering **2018-01-01–2020-12-31**.
- Historical Usage identity ↔ qualified USGS lock crosswalk resolves **{cross['crosswalk_matched_count']}/{hydro['qualified_matches']}**, with no fuzzy matching; three named aliases are admitted only because the official USACE TOC directly documents the historical names.

The same prospective three-year interval **2018–2020** is supported by the Annual Usage route and the USGS metadata route. / 동일 3개년 2018–2020이 양쪽 source route에서 지원된다.

## Evidence boundary / 증거 경계

This PASS means **JOIN_READY only**. It does not establish:
- the magnitude or distribution of lock delay;
- any streamflow/gage-height magnitude;
- a hydrology → delay relationship;
- causality, prediction, propagation, novelty, or decision utility.

Any effect experiment must return through Stage 0 and separately preregister one outcome, one hydrology exposure, temporal aggregation/alignment, lock dependence, seasonality/navigation controls, falsification, materiality, and novelty/utility assessment. / 효과실험은 별도 사전등록 전 자동 승인되지 않는다.

## Durable evidence / 영속 근거

- `ANNUAL_USAGE_SESSION_DIAGNOSTIC.md`
- `USAGE_ARCHIVE_PREFLIGHT.md`
- `USAGE_TOC_PREFLIGHT.md`
- `NAMED_LOCK_ALIAS_DIAGNOSTIC.md`
- `HISTORICAL_HYDROLOGY_CROSSWALK.md`
- `HYDROLOGY_METADATA_PREFLIGHT_V2.md`
- `SOURCE_ROUTE_DIAGNOSTIC.md`

Incremental monetary cost remained **0 USD**.
'''
    (R/'RESULT.md').write_text(result,encoding='utf-8')

    readme=(R/'README.md').read_text(encoding='utf-8')
    readme=re.sub(r'state: .*', 'state: COMPLETED_PASS', readme, count=1)
    if 'final_gate:' not in readme:
        readme=readme.replace('decision: DEC-134\n', f'decision: {DECISION}\nclaim: {CLAIM}\nfinal_gate: {GATE}\n')
    readme += f'''\n## Final disposition / 최종 상태\n\n**`{GATE}`** under `{DECISION}` / `{CLAIM}`.\n\nVerified outcome-blind structure: {toc['lock_identity_unique_count']} historical Usage lock identities; {cross['crosswalk_matched_count']}/{hydro['qualified_matches']} qualified historical-lock↔USGS crosswalks; shared 2018–2020 support; public Corps Locks Annual Usage route spans 2016–2025. No delay or hydrology magnitude was parsed.\n\n`JOIN_READY ≠ EXPERIMENT_READY`; return to Stage 0 before any relationship test.\n'''
    (R/'README.md').write_text(readme,encoding='utf-8')

    claim=f'''---
id: {CLAIM}
type: claim
created: {TODAY}
status: active
---

# {CLAIM} — US-WATERWAY-F01 outcome-blind JOIN_READY

Under the frozen `US-WATERWAY-F01` contract, the official public Corps Locks Annual Usage route exposes lock-level annual usage metrics for 2016–2025 including Average Delay/processing schema labels; the reproducible historical Public Lock Usage XLSX contains {toc['lock_identity_unique_count']} unique lock identities; and {cross['crosswalk_matched_count']} USGS-qualified locks deterministically crosswalk to historical Usage identities with Daily 00060/00065 metadata covering the shared 2018–2020 interval. Therefore the structural gate resolves to **`{GATE}`**.

Evidence class: `OBSERVED_DERIVED_VALIDATED`  
Verification: `V3_REPRODUCED_SOURCE_SEMANTICS_IDENTITY_AND_DATE_SUPPORT`

This is not an effect, causal, predictive, novelty, or utility claim. No delay/hydrology magnitude was parsed. Incremental cost: 0 USD.
'''
    (REG/f'{CLAIM}.md').write_text(claim,encoding='utf-8')

    decision=f'''---
id: {DECISION}
type: decision
created: {TODAY}
issue: {ISSUE}
status: accepted
---

# {DECISION} — Finalize US-WATERWAY-F01 as JOIN_READY and return to Stage 0

## Decision / 결정

Finalize Issue #{ISSUE} / `US-WATERWAY-F01` as **`{GATE}`** based on committed outcome-blind source, identity, crosswalk and date-support evidence.

## Boundary / 경계

- `JOIN_READY ≠ EXPERIMENT_READY`.
- Do not automatically open or analyze delay magnitudes, hydrology magnitudes, or their relationship.
- Return to Stage 0 portfolio control after Issue #{ISSUE} closes.
- If this branch re-enters, a new bounded preregistration must freeze exact delay outcome, hydrology predictor, 2018–2020 or other prospectively selected interval, time aggregation/alignment, navigation/seasonality controls, dependence, baseline, falsification/materiality, and novelty/decision-utility plan before values are opened.
- COST-001 and RAW-001 remain mandatory.
'''
    (REG/f'{DECISION}.md').write_text(decision,encoding='utf-8')

    ledger=REG/'CLAIM_LEDGER.md'
    lt=ledger.read_text(encoding='utf-8')
    if f'`{CLAIM}`' not in lt:
        lt += f'\n| `{CLAIM}` | US-WATERWAY-F01 has reproducible public lock-level historical-delay schema/identity support and 25 deterministic historical-lock↔USGS metadata matches over shared 2018–2020 support; gate `{GATE}`. | `OBSERVED_DERIVED_VALIDATED` | `V3_REPRODUCED_SOURCE_SEMANTICS_IDENTITY_AND_DATE_SUPPORT` | Issue #{ISSUE}; `research/US-WATERWAY-F01/RESULT.md` | {TODAY} | active |\n'
        ledger.write_text(lt,encoding='utf-8')

    dlog=REG/'DECISION_LOG.md'
    dt=dlog.read_text(encoding='utf-8')
    if f'`{DECISION}`' not in dt:
        dt += f'\n- `{DECISION}` — Finalize US-WATERWAY-F01 as `{GATE}` and return to Stage 0; no automatic effect exposure. / US-WATERWAY-F01 구조 PASS 후 Stage 0 복귀.\n'
        dlog.write_text(dt,encoding='utf-8')

    status=f'''---
checkpoint_id: {CHECKPOINT}
active_issue: none
active_research: NONE
last_completed_issue: {ISSUE}
last_completed_research: US-WATERWAY-F01
last_decision: {DECISION}
updated: {TODAY}
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_WATERWAY_F01_JOIN_READY_PASS__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

## Latest completed research / 최신 완료 연구

Issue #{ISSUE} `US-WATERWAY-F01` resolves to **`{GATE}`**.

Outcome-blind verified support:
- official Corps Locks Annual Usage: lock-level metrics, 2016–2025, Average Delay/processing schema;
- {toc['lock_identity_unique_count']} unique historical Public Lock Usage identities;
- {layer.get('feature_count')} public machine-readable lock features;
- {cross['crosswalk_matched_count']}/{hydro['qualified_matches']} deterministic historical-lock↔USGS metadata crosswalks;
- shared 2018–2020 source/date support.

No delay magnitude, hydrology value, or relationship was opened.

## Exact next action / 정확한 다음 행동

Return to **Stage 0 portfolio control**. Recompare a preregistered US-WATERWAY relationship descendant against independent opportunities before opening magnitudes. `JOIN_READY ≠ EXPERIMENT_READY`.

Incremental monetary cost remains **0 USD**.
'''
    (ROOT/'STATUS.md').write_text(status,encoding='utf-8')

    handoff=f'''---
checkpoint_id: {CHECKPOINT}
active_issue: none
active_research: NONE
last_completed_issue: {ISSUE}
last_completed_research: US-WATERWAY-F01
last_decision: {DECISION}
updated: {TODAY}
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

US-WATERWAY-F01 is complete under `{DECISION}` with **`{GATE}`**.

Do not rerun F01 by default. Do not open delay/hydrology magnitudes or compute a relationship automatically.

Canonical evidence: `research/US-WATERWAY-F01/RESULT.md`, `USAGE_TOC_PREFLIGHT.md`, `HISTORICAL_HYDROLOGY_CROSSWALK.md`, `HYDROLOGY_METADATA_PREFLIGHT_V2.md`, `registry/{CLAIM}.md`, `registry/{DECISION}.md`.

Verified structure: {toc['lock_identity_unique_count']} historical Usage lock identities; {cross['crosswalk_matched_count']} deterministic USGS-qualified crosswalks; shared 2018–2020 support; official Annual Usage route spans 2016–2025.

## Exact next action / 정확한 다음 행동

Return to **Stage 0 portfolio control** with no active research Issue. Compare a prospective US-WATERWAY preregistered relationship design against independent alternatives before opening values.

Cost remains **0 USD**; any potentially billable action requires explicit prior approval.
'''
    (CTX/'SESSION_HANDOFF.md').write_text(handoff,encoding='utf-8')
    checkpoint={'checkpoint_id':CHECKPOINT,'active_issue':'none','active_research':'NONE','last_completed_issue':ISSUE,'last_completed_research':'US-WATERWAY-F01','last_decision':DECISION,'updated':TODAY}
    (CTX/'checkpoint.json').write_text(json.dumps(checkpoint,indent=2)+'\n',encoding='utf-8')

    print(json.dumps({'gate':GATE,'locks':toc['lock_identity_unique_count'],'crosswalk':cross['crosswalk_matched_count'],'overlap':hydro['target_overlap'],'decision':DECISION,'claim':CLAIM,'cost_usd':0}))

if __name__=='__main__': main()
