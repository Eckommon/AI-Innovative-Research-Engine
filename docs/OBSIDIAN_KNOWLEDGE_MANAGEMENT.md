# Obsidian Knowledge Management / Obsidian 지식관리 규약

**Policy ID / 규약 ID:** `KM-001`  
**Status / 상태:** `ACTIVE`  
**Effective / 시행일:** 2026-08-22

## 1. Purpose / 목적

**한국어**  
GitHub 저장소 자체를 Obsidian Vault로 열 수 있도록 구성하여, Git의 버전·증거 추적성과 Obsidian의 링크·백링크·태그·Graph·MOC(Map of Content) 탐색성을 결합한다. Obsidian은 별도의 Source of Truth가 아니라 **동일 Markdown 기록을 탐색하는 지식 그래프 레이어**다.

**English**  
Structure the GitHub repository so it can be opened directly as an Obsidian Vault, combining Git version/evidence traceability with Obsidian links, backlinks, tags, graph navigation, and Maps of Content (MOCs). Obsidian is not a separate source of truth; it is a **knowledge-graph navigation layer over the same Markdown record**.

## 2. Authority / 권한

- GitHub committed Markdown remains authoritative. / GitHub에 commit된 Markdown이 공식 기준이다.
- Obsidian local UI state, workspace layout, cache and plugin state are not authoritative. / Obsidian 로컬 UI·workspace·cache·plugin 상태는 공식 기록이 아니다.
- No critical fact should exist only inside an Obsidian-specific view. / 중요한 사실을 Obsidian 화면에만 존재하게 하지 않는다.

## 3. Vault / Vault 구성

Recommended / 권장:

```text
AI-Innovative-Research-Engine/   ← Open this repository root as Vault / 저장소 루트를 Vault로 열기
  README.md
  STATUS.md
  docs/
  registry/
  research/
  context/
  knowledge/
  templates/
```

## 4. Navigation Model / 탐색 모델

### Maps of Content / MOC
- `knowledge/00_HOME.md` — 시작 허브 / start hub
- `knowledge/MOC_RESEARCH.md` — 연구 객체 / research objects
- `knowledge/MOC_DATASETS.md` — 데이터셋·소스 / datasets and sources
- `knowledge/MOC_EXPERIMENTS.md` — feasibility·experiment / feasibility and experiments
- `knowledge/MOC_DECISIONS.md` — 결정·HOLD·REJECTED·VALIDATED / decisions and terminal/hold outcomes

### Link rule / 링크 규칙
GitHub 호환성을 위해 **표준 Markdown 상대 링크를 canonical**로 사용한다. Obsidian의 backlinks/graph는 Markdown links도 인식한다. `[[wikilink]]`는 개인 로컬 노트에서 사용할 수 있으나 공식 산출물의 유일 링크로 사용하지 않는다.  
Use **standard relative Markdown links as canonical** for GitHub compatibility. Obsidian can build backlinks/graphs from Markdown links. `[[wikilinks]]` may be used locally but must not be the sole link form in official artifacts.

## 5. Metadata / 메타데이터

새로운 주요 knowledge/research note는 가능한 경우 YAML frontmatter를 사용한다. / New major knowledge/research notes should use YAML frontmatter where practical.

```yaml
---
id: EU-IEE-E01
type: experiment
state: VALIDATED
evidence_class: VALIDATED
region: eu
domain: industry
tags:
  - type/experiment
  - state/validated
  - evidence/validated
  - region/eu
  - domain/industry
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/WAVE1-EU/README.md
---
```

## 6. Tag Discipline / 태그 규율

태그는 탐색용이며 사실 자체의 저장소가 아니다. / Tags are navigation metadata, not evidence themselves.

Controlled namespaces / 통제 namespace:
- `type/*` — `dataset`, `source`, `hypothesis`, `experiment`, `decision`, `moc`, `memory`
- `state/*` — `discovered`, `screening`, `candidate`, `feasibility`, `experiment`, `validated`, `rejected`, `inconclusive`, `hold`, `archived`
- `evidence/*` — `observed`, `derived`, `hypothesized`, `validated`, `rejected`, `inconclusive`
- `region/*` — `us`, `kr`, `eu`, `jp`, `uk`, `sg`, `global`, etc.
- `domain/*` — `manufacturing`, `grid`, `energy`, `industry`, `climate`, `logistics`, `minerals`, etc.
- `wave/*` — `wave0`, `wave1`, `wave2`, `wave3`
- `priority/*` — `p0`, `p1`, `a`, `b`, etc.
- `risk/*` — `data-gap`, `mapping`, `classification`, `license`, `safety`, `freshness`

Do not create synonym tags casually. / 동의어 태그를 임의로 증식하지 않는다.

## 7. Note Granularity / 노트 단위

- One durable research object per stable research ID. / 하나의 안정적 research ID당 하나의 지속 연구 객체.
- Sources/datasets may have dedicated profiles when reused across projects. / 여러 연구에서 재사용되는 소스·데이터셋은 별도 profile 가능.
- Decisions that materially change direction belong in the Decision Log, not only in prose. / 방향을 바꾸는 결정은 본문뿐 아니라 Decision Log에 기록.
- Temporary scratch notes are not promoted until evidence/state is classified. / 임시 메모는 증거·상태 분류 전 공식 승격 금지.

## 8. Maintenance / 유지관리

At material session end / 실질 세션 종료 시:
1. update relevant MOC links if a durable object was added / 지속 객체 추가 시 관련 MOC 링크 갱신;
2. normalize new tags against `knowledge/TAG_TAXONOMY.md` / 새 태그 정규화;
3. update `context/SESSION_HANDOFF.md` / 세션 인수인계 갱신;
4. update claim/decision ledgers when applicable / claim·decision ledger 필요 시 갱신;
5. do not commit machine-specific `.obsidian` workspace/cache state. / 기기별 `.obsidian` 상태는 commit 금지.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
