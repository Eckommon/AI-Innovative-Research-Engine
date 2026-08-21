---
id: MOC-DECISIONS
type: moc
state: ACTIVE
tags:
  - type/moc
  - domain/governance
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# Decisions MOC / 의사결정 MOC

## Durable Decision Records / 지속 의사결정 기록
- [Decision Log / 의사결정 로그](../registry/DECISION_LOG.md)
- [Claim Ledger / 주장·증거 레저](../registry/CLAIM_LEDGER.md)
- [Project Memory / 프로젝트 메모리](../context/PROJECT_MEMORY.md)
- [Session Handoff / 세션 인수인계](../context/SESSION_HANDOFF.md)

## Current Key Decisions / 현재 핵심 결정
- GitHub is the source of truth; Obsidian is a navigation layer. / GitHub가 기준 기록이고 Obsidian은 탐색 레이어.
- `LANG-001` is mandatory. / 한·영 병기는 의무.
- `C-KR-001` localized/asset attribution remains `HOLD`. / 한국 계통 후보의 지역·설비 귀속은 HOLD.
- `EU-IEE-E01` empirical result is `VALIDATED`, but novelty is `LOW / NOT NOVEL`. / 실증 검증과 신규성은 분리.
- Facility-level emissions-per-output must not be created from country/sector denominators by arbitrary allocation. / 국가·sector 생산분모를 임의 배분해 시설 효율지표를 만들지 않음.
- `EU-STEEL-R01` is `HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`; current replacement data or `null→0` assumptions must not be used to force historical reproduction. / historical 재현을 맞추기 위해 현행 replacement나 결측=0 가정을 사용하지 않음.
- Snapshot/version lineage is now a first-class reproducibility gate; `reproduction_risk` remains a modifier before any IPS reweighting. / snapshot/version 계보를 1급 재현성 게이트로 두고 IPS 재가중 전 별도 modifier로 운용.

## Governance / 거버넌스
- [Governance](../docs/GOVERNANCE.md)
- [Hallucination Control Protocol](../docs/HALLUCINATION_CONTROL_PROTOCOL.md)
- [GPT ↔ GitHub Sync Protocol](../docs/GPT_GITHUB_SYNC_PROTOCOL.md)
- [Normalized Metadata Schema v0.3](../docs/METADATA_SCHEMA.md)

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
