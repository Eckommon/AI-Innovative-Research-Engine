#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / 'research' / 'EU-GRID-F01'
REG = ROOT / 'registry'

manifest = json.loads((R / 'SOURCE_PANEL_MANIFEST.json').read_text(encoding='utf-8'))
result = (R / 'RESULT.md').read_text(encoding='utf-8')

gate = 'HOLD_EU_GRID_F01_SOURCE_OR_IDENTITY_SUPPORT'
assert manifest['gate'] == gate
assert gate in result
assert manifest['frozen_countries'] == ['FR', 'BE', 'NL', 'ES', 'PT', 'PL', 'AT', 'CZ']
assert all(c['anchors_total'] == 16 for c in manifest['country_summary'])
assert all(c['anchors_structurally_supported'] == 0 for c in manifest['country_summary'])
assert manifest['physical_flow']['supported_country_count'] == 0
assert manifest['eobs']['version_33_0e_present'] is True
assert manifest['eobs']['coverage_1950_to_2025_present'] is True
assert manifest['boundary']['relationship_computed'] is False
assert manifest['boundary']['load_magnitudes_parsed_or_persisted'] is False
assert manifest['boundary']['forecast_magnitudes_parsed_or_persisted'] is False
assert manifest['boundary']['physical_flow_magnitudes_parsed_or_persisted'] is False
assert manifest['boundary']['weather_magnitudes_parsed_or_persisted'] is False
assert manifest['incremental_monetary_cost_usd'] == 0

claim_ledger = REG / 'CLAIM_LEDGER.md'
decision_log = REG / 'DECISION_LOG.md'
assert 'CLM-147' not in claim_ledger.read_text(encoding='utf-8')
assert 'DEC-145' not in decision_log.read_text(encoding='utf-8')

(REG / 'CLM-147.md').write_text('''---
id: CLM-147
type: claim
created: 2026-09-12
issue: 104
status: active
---

# CLM-147 — EU-GRID-F01 terminates at source/identity-support HOLD

The outcome-blind F01 probe resolves to **`HOLD_EU_GRID_F01_SOURCE_OR_IDENTITY_SUPPORT`**. Across the frozen 8-country cohort (`FR, BE, NL, ES, PT, PL, AT, CZ`), every country produced `0/16` structurally supported fixed-anchor ENTSO-E pages, and `0/8` frozen countries had structural cross-border support to another frozen country. E-OBS v33.0e / 1950–2025 / TG / regular-grid metadata support was available, but it does not satisfy the missing ENTSO-E source/identity gate.

No load, forecast, physical-flow or weather magnitudes were opened or persisted and no relationship/effect model was computed. This HOLD is a source-operability/identity result, not evidence against the substantive grid-stress hypothesis. Incremental monetary cost: **0 USD**.
''', encoding='utf-8')

(REG / 'DEC-145.md').write_text('''---
id: DEC-145
type: decision
created: 2026-09-12
issue: 104
status: accepted
---

# DEC-145 — Finalize EU-GRID-F01 as HOLD and return to Stage 0

Finalize Issue #104 as **`HOLD_EU_GRID_F01_SOURCE_OR_IDENTITY_SUPPORT`**. Preserve the outcome-blind source-operability result without opening effect values. E-OBS support alone is insufficient: the preregistered ENTSO-E structural/identity route did not satisfy the gate for any frozen country, and frozen-country cross-border support was absent.

Do not open EU-GRID effect testing, substitute countries or source routes post hoc inside F01, or interpret this HOLD as evidence against the substantive grid-stress relationship. Return to Stage 0 portfolio control. Any EU-grid descendant must be separately preregistered and establish a reproducible machine-executable ENTSO-E source/identity route before effect values are opened.

Incremental monetary cost remains **0 USD**.
''', encoding='utf-8')

with claim_ledger.open('a', encoding='utf-8') as f:
    f.write('\n| `CLM-147` | EU-GRID-F01 outcome-blind source-operability gate resolves to HOLD: every frozen country had 0/16 structurally supported ENTSO-E anchors and 0/8 frozen countries had structural cross-border support; E-OBS metadata support alone cannot advance the gate. / EU-GRID-F01 source-operability HOLD. | `OBSERVED/DERIVED/VALIDATED` | `V3_PREREGISTERED_SOURCE_GATE` | Run `34578713017`; `research/EU-GRID-F01/RESULT.md`; `SOURCE_PANEL_MANIFEST.json` | 2026-09-12 | active |\n')

with decision_log.open('a', encoding='utf-8') as f:
    f.write('\n- [DEC-145](DEC-145.md): finalize EU-GRID-F01 as source/identity-support HOLD; block effect testing and return to Stage 0. / F01 HOLD 확정·효과시험 차단·Stage 0 복귀.\n')

readme_path = R / 'README.md'
readme = readme_path.read_text(encoding='utf-8')
assert 'state: ACTIVE_SOURCE_OPERABILITY_FEASIBILITY' in readme
readme = readme.replace('state: ACTIVE_SOURCE_OPERABILITY_FEASIBILITY', 'state: COMPLETED_HOLD', 1)
readme += '''

## Final disposition / 최종 종결

- gate: **`HOLD_EU_GRID_F01_SOURCE_OR_IDENTITY_SUPPORT`**
- claim: `CLM-147`
- decision: `DEC-145`
- effect testing: **blocked**
- canonical restart: **Stage 0 portfolio control**

This is a source-operability/identity HOLD only. It is not a negative finding about the substantive EU grid-stress relationship.
'''
readme_path.write_text(readme, encoding='utf-8')

status = '''---
checkpoint_id: CHK-20260912-EU-GRID-F01-HOLD-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 104
last_completed_research: EU-GRID-F01
last_decision: DEC-145
updated: 2026-09-12
---

# Project Status / 프로젝트 상태

**State / 상태:** `EU_GRID_F01_HOLD__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

EU-GRID-F01 completed outcome-blind with `HOLD_EU_GRID_F01_SOURCE_OR_IDENTITY_SUPPORT`. Every frozen country (`FR, BE, NL, ES, PT, PL, AT, CZ`) had `0/16` structurally supported fixed-anchor ENTSO-E pages; `0/8` frozen countries had structural cross-border support to another frozen country. E-OBS v33.0e / 1950–2025 / TG / regular-grid metadata support was available. No load, forecast, physical-flow or weather magnitudes and no relationship/effect model were opened.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio control. Compare independent alternatives and any separately preregistered source-route redesign on marginal information value before opening a new research issue. Do not open EU-GRID effect testing from F01.

Incremental monetary cost remains **0 USD**.
'''
(ROOT / 'STATUS.md').write_text(status, encoding='utf-8')

(ROOT / 'context' / 'SESSION_HANDOFF.md').write_text('''---
checkpoint_id: CHK-20260912-EU-GRID-F01-HOLD-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 104
last_completed_research: EU-GRID-F01
last_decision: DEC-145
updated: 2026-09-12
---

# Session Handoff / 세션 인수인계

EU-GRID-F01 is complete with **`HOLD_EU_GRID_F01_SOURCE_OR_IDENTITY_SUPPORT`**. Run `34578713017` completed successfully as an execution, but the preregistered research gate did not pass. For all eight frozen countries (`FR, BE, NL, ES, PT, PL, AT, CZ`), structural ENTSO-E support was `0/16` fixed anchors; `0/8` frozen countries had structural cross-border support to another frozen country. E-OBS v33.0e / 1950–2025 / TG / regular-grid metadata support was available.

Outcome-blind boundary was preserved: no load, forecast, physical-flow or weather magnitudes were opened or persisted, and no effect/relationship model was computed. This is a source-operability/identity HOLD, not evidence against the substantive grid-stress hypothesis.

Canonical restart: **Stage 0 portfolio control**. Do not automatically repair/re-run F01 or open EU-GRID effect testing. Any descendant that changes source route, registration assumption, country set or identity mapping must be separately preregistered before outcomes are opened. Incremental monetary cost: **0 USD**.
''', encoding='utf-8')

(ROOT / 'context' / 'checkpoint.json').write_text(json.dumps({
    'checkpoint_id': 'CHK-20260912-EU-GRID-F01-HOLD-PORTFOLIO-RETURN',
    'active_issue': 'none',
    'active_research': 'NONE',
    'last_completed_issue': 104,
    'last_completed_research': 'EU-GRID-F01',
    'last_decision': 'DEC-145',
    'updated': '2026-09-12'
}, indent=2) + '\n', encoding='utf-8')

print(json.dumps({
    'gate': gate,
    'claim': 'CLM-147',
    'decision': 'DEC-145',
    'return': 'Stage 0',
    'incremental_monetary_cost_usd': 0
}))
