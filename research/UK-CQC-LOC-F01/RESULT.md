---
id: UK-CQC-LOC-F01-RESULT
type: structural-feasibility-result
created: 2026-09-29
issue: 171
research: UK-CQC-LOC-F01
disposition: HOLD
attempt_02_commit: 854afb9dd926fb46afb886ed5d6c2c1a51d56e8e
workflow_run: 36525513701
contract_commit: 99c7782cabc384ce7c4817a91b5cb1bdc105012c
gate: HOLD_UK_CQC_LOC_F01_EXACT_LOCATION_REGISTRATION_END_DESIGN_NOT_READY
---

# UK-CQC-LOC-F01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_UK_CQC_LOC_F01_EXACT_LOCATION_REGISTRATION_END_DESIGN_NOT_READY`**

Attempt 02 correctly resolves the baseline data header and provides decisive frozen-contract failures. The exact F01 is therefore terminal HOLD. N01 and E01 are not authorized.

Attempt 02는 실제 baseline data header를 올바르게 판독한 뒤 고정 계약의 핵심 support gate가 실패했음을 확인했습니다. 따라서 이 exact F01은 terminal HOLD이며 N01/E01은 허가하지 않습니다.

## Decisive frozen failures / 결정적 실패

The terminal decision does **not** depend on the archive-parser defect recorded at Gate 15. Four independent scientific gates already make 18/18 PASS impossible:

- **Gate 6 — exact Location-ID syntax:** only **1,770 / 57,069 = 3.1015087%** of nonblank active Location IDs satisfy the prospectively frozen ASCII-alphanumeric token rule, far below **99.90%**.
- **Gate 7 — active exact-ID support:** **1,770** distinct qualified baseline Location IDs, below **20,000**.
- **Gate 9 — ratings exact-link support:** **456** exact-qualified baseline Location IDs link to ratings rows, below **10,000**.
- **Gate 11 — historical deactivated support:** **3,441** distinct exact-qualified deactivated Location IDs, below **5,000**.

These failures are consequences of the frozen identity rule, not evidence that CQC lacks location identifiers. Most source-native CQC Location IDs contain characters outside the preregistered ASCII-alphanumeric-only rule. The rule may not now be relaxed to admit punctuation such as hyphens because that would be post-observation redesign.

이 실패는 CQC에 Location ID가 없다는 뜻이 아니라, **사전에 고정한 exact-token 규칙과 실제 source representation이 맞지 않았다는 뜻**입니다. 결과를 본 뒤 하이픈 등을 허용하도록 ID 규칙을 바꾸는 것은 금지합니다.

## Structural facts that passed / 통과한 구조 사실

- official CQC landing page and all three frozen 01-Sep-2026 selectors: PASS
- official CQC-owned ODS file resolution: PASS
- filters directory schema: PASS after parser correction
- ratings schema: PASS
- deactivated schema: PASS
- historical deactivated end-date parseability: **3,441 / 3,441 = 100%**
- administrative-transition semantics: PASS
  - CQC states deactivated/archived does not necessarily mean service closure;
  - official metadata describes linked organisations and re-registration/legal-structure/address-change cases.
- identity-conflict evaluation after exact parsing: **0 unresolved exact Location-ID/provider conflicts**
- future post-2026-09-28 inactive/deactivated rows opened: **0**
- future event membership opened: **false**
- incremental monetary cost: **0 USD**

These are structural-source facts only. They do not establish a registration-end relationship, closure probability, provider quality effect, ranking, causal effect or novelty.

## Attempt provenance / 실행 계보

### Attempt 01

Commit `4b26cfc6c31f38a36a19b908a45c1ca9cb67f030` / Run `36525105345` is preserved unchanged. Its runner incorrectly selected README narrative text as the filters-file header, creating an artificial empty baseline. Canonical adjudication therefore treated Attempt 01 as implementation-nonconforming rather than terminal scientific evidence.

### Attempt 02

Implementation-only correction `6d7abac0041866e841389c6d30e003e5bf68a02c` and runner commit `567d1b02f91030c6625bfab287a2a628e48dd06e` changed no scientific threshold, source snapshot, identity rule, event semantics or future firewall.

Attempt 02 at commit `854afb9dd926fb46afb886ed5d6c2c1a51d56e8e` / Run `36525513701` correctly selected the actual filters data header and exposed the decisive frozen support failures above.

Gate 15 also recorded an archive-page parser defect (`html_lib` NameError). That defect is **non-decisive**: even a corrected Gate 15 PASS cannot overcome Gates 6, 7, 9 and 11. Therefore no further implementation run is authorized merely to improve the recorded gate count.

## Consequence / 후속 조치

Do not authorize `UK-CQC-LOC-N01`. Do not rescue this branch by:

- permitting hyphen/punctuation after observing source IDs;
- lowering the 99.90%, 20,000, 10,000 or 5,000 frozen thresholds;
- substituting provider ID for Location ID;
- using name/address/postcode/fuzzy/geospatial/manual continuity;
- treating all deactivated rows as closures;
- opening post-2026-09-28 inactive/deactivated membership.

Return to an independent outcome-blind Stage-0 portfolio reselection.

독립적인 Stage-0 portfolio reselection으로 복귀합니다. CQC branch는 향후 후보선정에서 terminal negative evidence로만 사용합니다.

Incremental monetary cost: **0 USD**.
