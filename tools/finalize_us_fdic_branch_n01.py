#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
STAGING='074df7191d38970e3082cb846fd7a397dfe30ce9'
RUN='35251883997'
DEC='DEC-235'
CONTRACT='c0f9f412b88b4ff54fd9999ff57fc3c4be40f374'
GATE='HOLD_US_FDIC_BRANCH_N01_MATCHED_NETWORK_POSITION_TRAJECTORY_DESIGN_NOT_IDENTIFIABLE'

x=json.loads((ROOT/'research/US-FDIC-BRANCH-N01/staging/n01_result.json').read_text(encoding='utf-8'))
assert x['gate']==GATE and x['scientific_disposition']=='HOLD'
assert x['contract_commit']==CONTRACT
assert x['requirements_total']==18 and x['requirements_passed']==15
failed=[r for r in x['requirements'] if not r['pass']]
assert [r['number'] for r in failed]==[12,13,14]
assert x['diagnostics']['historically_eligible_stable_branches']==70113
assert x['diagnostics']['eligible_strata_n_ge8']==1650
assert x['diagnostics']['matched_pairs']==13874
assert x['diagnostics']['states_in_pairs']==52
assert abs(x['diagnostics']['baseline_share_balance_rate']-0.6849502666858873)<1e-12
assert abs(x['diagnostics']['baseline_2022_deposit_balance_rate']-0.6849502666858873)<1e-12
assert abs(x['diagnostics']['baseline_2023_deposit_balance_rate']-0.7346835807986161)<1e-12
assert all(v is False for v in x['boundaries'].values())
assert x['incremental_monetary_cost_usd']==0

result=f'''---
id: US-FDIC-BRANCH-N01-RESULT
type: outcome-blind-matched-design-result
created: 2026-09-18
issue: 161
research: US-FDIC-BRANCH-N01
disposition: HOLD
staging_commit: {STAGING}
workflow_run: {RUN}
contract_commit: {CONTRACT}
gate: {GATE}
---

# US-FDIC-BRANCH-N01 Result / 결과

## Terminal disposition / 최종 판정

**`{GATE}`**

The first valid immutable outcome-blind N01 run passed **15 of 18** frozen requirements. The exact design is terminal HOLD because all three prospectively frozen baseline-balance gates failed.

최초 유효 immutable outcome-blind N01 실행은 고정된 18개 요건 중 **15개를 PASS**했습니다. 그러나 사전고정한 baseline-balance gate 3개가 모두 실패했으므로 이 exact design은 terminal HOLD입니다.

## Strong support that does not override HOLD / HOLD를 뒤집지 않는 강한 support

- historically eligible stable-ownership branches: **70,113**
- eligible exact `CERT × STALPBR` strata (`n >= 8`): **1,650**
- deterministic matched DECLINE–GAIN pairs: **13,874**
- states/territories represented: **52**
- same-year exact-ID conflicts: **0**
- strict trajectory separation: PASS
- exact same-bank/same-state pairing: PASS
- duplicate `UNINUMBR` across pairs: none
- pair-manifest SHA-256: `{x['diagnostics']['pair_manifest_sha256']}`

## Frozen balance failures / 고정 balance 실패

1. 2022 within-stratum deposit-share ratio within `[1/3, 3]`: **68.4950%** < frozen **75%**.
2. 2022 absolute branch-deposit ratio within `[1/3, 3]`: **68.4950%** < frozen **75%**.
3. 2023 absolute branch-deposit ratio within `[1/3, 3]`: **73.4684%** < frozen **75%**.

The design has abundant cardinality, but the prospectively required baseline comparability is not met. The 75% thresholds, matching order, quartile definitions, and strata may not be relaxed after observing these results.

## Future-outcome firewall / 미래 outcome 방화벽

No 2025 SOD row, future branch membership, future BankFind structure-event membership, closure/non-continuation disposition, relationship, prediction, causal estimate, bank/branch ranking, or novelty result was opened or computed.

## Consequence / 후속 조치

`US-FDIC-BRANCH-E01` is **not authorized**. Do not rescue this N01 by widening the balance ratio, lowering 75%, changing quartiles, changing the matching order, or redefining strata after observing the results. Return to independent portfolio reselection or a separately preregistered new branch/design that is not conditioned on future outcomes.

Incremental monetary cost: **0 USD**.
'''
(ROOT/'research/US-FDIC-BRANCH-N01/RESULT.md').write_text(result,encoding='utf-8')

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-18
issue: 161
research: US-FDIC-BRANCH-N01
status: terminal
---

# {DEC} — Terminate US-FDIC-BRANCH-N01 at frozen baseline-balance HOLD

Finalize `US-FDIC-BRANCH-N01` as `{GATE}` from immutable staging commit `{STAGING}` / Run `{RUN}`.

The design has 70,113 stable branches, 1,650 eligible bank-state strata, and 13,874 matched pairs across 52 states/territories, but the three frozen baseline-balance rates are 68.4950%, 68.4950%, and 73.4684%, each below the required 75%. Do not relax balance thresholds, quartiles, matching order, or strata post hoc. Future outcomes remained unopened. E01 is not authorized. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'; log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-18 | Finalize `US-FDIC-BRANCH-N01` as frozen baseline-balance HOLD; do not authorize E01 or relax the observed matching/balance rules. / `US-FDIC-BRANCH-N01`을 고정 baseline-balance HOLD로 종결하고 E01·사후 매칭완화를 금지. | 15/18 PASS; 13,874 pairs but balance rates 68.50%, 68.50%, 73.47% < frozen 75%. Future outcomes unopened. | Issue #161; `{STAGING}`; `research/US-FDIC-BRANCH-N01/RESULT.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={'checkpoint_id':'CHK-20260918-US-FDIC-BRANCH-N01-TERMINAL','active_issue':'none','active_research':'NONE','last_completed_issue':161,'last_completed_research':'US-FDIC-BRANCH-N01','last_decision':DEC,'updated':'2026-09-18'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260918-US-FDIC-BRANCH-N01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 161
last_completed_research: US-FDIC-BRANCH-N01
last_decision: DEC-235
updated: 2026-09-18
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `US_FDIC_BRANCH_N01_HOLD__PORTFOLIO_RESELECTION_REQUIRED`\n\nUS-FDIC-BRANCH-N01 is terminal scientific HOLD: 15/18 frozen gates passed, but all three prospectively frozen baseline-balance gates failed. Future branch closure/non-continuation outcomes remained unopened. E01 is not authorized.\n\n## Exact next action / 정확한 다음 행동\n\nReturn to an independent portfolio reselection. Do not relax the 75% balance gates, ratio band, quartile exposure, matching order, or CERT × STALPBR strata after observing N01 support.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`US_FDIC_BRANCH_N01_HOLD__PORTFOLIO_RESELECTION_REQUIRED`\n\n- Issue #161 completed.\n- Contract: `{CONTRACT}`.\n- Immutable staging: `{STAGING}` / Run `{RUN}`.\n- 15/18 PASS.\n- 70,113 stable branches; 1,650 eligible strata; 13,874 matched pairs; 52 states/territories.\n- Frozen balance failures: 68.4950%, 68.4950%, 73.4684% < 75%.\n- 2025/future branch/event outcomes remained unopened.\n- E01 not authorized.\n- Next: independent portfolio reselection; no post-hoc FDIC N01 rescue.\n- Cost: 0 USD.\n''',encoding='utf-8')
print(GATE)
