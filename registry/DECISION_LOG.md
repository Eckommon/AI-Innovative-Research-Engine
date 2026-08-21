# Decision Log / 의사결정 로그

| Decision ID | Date | Decision / 결정 | Rationale / 근거 | Related / 관련 | Status |
|---|---|---|---|---|---|
| `DEC-001` | 2026-08-21 | GitHub is the persistent Source of Truth; GPT sessions are workspaces. / GitHub를 지속 Source of Truth로, GPT 세션을 작업공간으로 사용. | Reconstructable project state and version history. / 재구성 가능한 상태·버전 이력. | Governance | active |
| `DEC-002` | 2026-08-21 | `LANG-001` mandatory bilingual Korean-English output for major artifacts. / 주요 산출물 한·영 병기 의무화. | Cross-session readability and fidelity. / 세션간 가독성·의미 충실성. | `docs/LANGUAGE_POLICY.md` | active |
| `DEC-003` | 2026-08-22 | Close Issue #5 as completed feasibility with `HOLD` outcome; do not promote localized KPX grid model. / #5를 HOLD 결과의 완료 feasibility로 종료하고 지역귀속 모델 승격 금지. | Current public identifier mapping not established; safety boundary. / 현행 공개 mapping 미확립·안전 경계. | Issue #5 | active |
| `DEC-004` | 2026-08-22 | Use `C-EU-002` aggregate decoupling as first post-Wave1 controlled experiment. / 첫 post-Wave1 통제실험으로 EU 산업배출–GVA decoupling 사용. | Open, non-sensitive, authoritative cross-dataset relationship suitable for workflow calibration. / 공개·비민감·권위 있는 cross-dataset 관계. | Issue #6 | completed |
| `DEC-005` | 2026-08-22 | Separate empirical validation from novelty. `EU-IEE-E01` = `VALIDATED` empirical, `LOW / NOT NOVEL` novelty. / 실증검증과 신규성 분리. | Avoid forced innovation. / 혁신 강제 금지. | Issue #6 | active |
| `DEC-006` | 2026-08-22 | For `EU-IEE-F02`, allow sector/product normalization only with explicit mapping; hold generic facility denominator. / 명시 mapping된 sector/product 정규화만 허용하고 일반 시설분모는 HOLD. | EEA precedent exists at aggregated steel/product level; plant production denominator is generally unavailable. / EEA sector 선례 존재, plant 생산분모 일반 부재. | Issue #7 | active |
| `DEC-007` | 2026-08-22 | Introduce Obsidian as a navigation/knowledge-graph layer over the GitHub repository, not a parallel authority. / Obsidian을 병렬 권위 저장소가 아닌 GitHub 위 탐색·지식그래프 레이어로 도입. | Avoid duplicated truth while adding MOC/backlinks/tags/graph. / 중복 Source of Truth 없이 탐색성 향상. | `KM-001` | active |
| `DEC-008` | 2026-08-22 | Make `READ-001` and durable GitHub project memory mandatory for material work. / 실질 작업에 선읽기와 GitHub 지속 메모리를 의무화. | Reduce hallucination, stale-context errors, and cross-session drift. / 환각·구버전·세션 드리프트 감소. | `docs/HALLUCINATION_CONTROL_PROTOCOL.md` | active |
| `DEC-009` | 2026-08-22 | Finalize `EU-STEEL-R01` as `HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`; do not substitute current `DS-059359` for discontinued legacy `DS-066342`, and do not convert PRODCOM `null` values to zero. / `EU-STEEL-R01`을 `HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`로 확정하고 현행 `DS-059359`를 폐지된 `DS-066342` 대신 사용하거나 `null`을 0으로 처리하지 않는다. | Frozen gate requires matched reproducible inputs. EEA current figure CSV also conflicts with the historical narrative (`-41.43%` from current CSV vs `-36%` narrative), while the exact legacy 2017 denominator is no longer disseminated through tested official APIs. / 고정 게이트상 matched input 재현이 필요하며 현행 EEA CSV와 과거 서술도 충돌하고 exact legacy 분모를 현행 공식 API에서 복구할 수 없음. | Issue #8; `research/EU-STEEL-R01/REPRODUCTION_RESULT.md`; `CLM-010..013` | active |

## Maintenance / 유지

Material direction changes receive a stable decision ID. Superseded decisions remain visible with a superseding reference rather than being deleted. / 중요 방향 변경은 안정적 Decision ID를 부여하며 대체된 결정은 삭제하지 않고 superseding 참조를 남긴다.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
