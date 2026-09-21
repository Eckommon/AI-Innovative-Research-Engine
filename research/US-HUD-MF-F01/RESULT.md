---
id: US-HUD-MF-F01-RESULT
type: structural-feasibility-result
created: 2026-09-21
issue: 168
research: US-HUD-MF-F01
disposition: PASS
attempt_03_commit: 355e329cd3b6fb5cfbef2ff2c0249b9e7e753af8
workflow_run: 35615168948
contract_commit: 73eec2f714f3e1c89d0441ffb9f746721bda3443
gate: PASS_US_HUD_MF_F01_EXACT_PROJECT_ADVERSE_TERMINATION_DESIGN_READY
---

# US-HUD-MF-F01 Result / 결과

## Terminal disposition / 최종 판정

**`PASS_US_HUD_MF_F01_EXACT_PROJECT_ADVERSE_TERMINATION_DESIGN_READY`**

Immutable Attempt 03 passes **18/18** frozen structural requirements under the unchanged pre-Issue contract. HUD's frozen historical multifamily sources support exact FHA-project identity, current termination reason/date semantics, exact project→property linkage, exact property→inspection linkage and a still-sealed future adverse-termination source.

Attempt 03는 사전고정 계약을 변경하지 않고 **18/18** 구조 gate를 통과했습니다. 향후 adverse termination membership은 계속 봉인되어 있습니다.

## Structural support / 구조적 support

- active mortgage rows: **15,632**
- nonblank FHA Project Number rows: **15,632**
- exact qualified 8-digit FHA IDs: **15,632 / 15,632 = 100%**
- distinct active qualified FHA IDs: **15,632**
- historical terminated qualified FHA rows: **58,780**
- historical termination date parseability: **58,774 / 58,780 = 99.9898%**
- historical termination reason/code completeness: **58,773 / 58,780 = 99.9881%**
- official source-native routine termination labels include **Prepayment, Maturity, Voluntary**
- official source-native claim/adverse-capable labels include **Coinsurance CLAIM, Risk Share Claim, PARTIAL PAYMENT OF CLAIM** and other claim-bearing categories
- property-source distinct property IDs: **17,734**
- active FHA IDs exact-linked to property: **15,425 / 15,632 = 98.6758%**
- inspection-source property IDs with at least one pre-cutoff inspection: **25,912**
- active FHA projects exact-linked through property ID to a pre-2026-09-21 inspection: **9,434**
- future post-2026-09-21 terminated rows opened: **0**
- future adverse membership opened: **false**
- incremental monetary cost: **0 USD**

These figures establish structural feasibility only. They are not evidence that inspection condition, mortgage structure, project size, geography or any other exposure predicts or causes later adverse termination.

## Implementation-correction provenance / 구현 보정 계보

### Attempt 01
Commit `73ce4cfe7f475bb177186ab7d38ce7374f5e8fee` / Run `35612698293` is preserved as implementation-blocked. It exposed three parser issues: missing `HUD PROJECT NUMBER` alias, premature terminated-header detection and legacy `.xls` inspection parsing.

### Attempt 02
Commit `0dcd10db85848957ae950b592a13ed83348c1964` / Run `35614642101` is preserved unchanged. Its nominal 13/18 HOLD was an implementation nonconformity because the source itself exposed `AMORITIZED PRINCIPAL BALANCE`, while the parser failed to recognize HUD's source spelling and therefore skipped the entire active cohort. Gates 7, 8, 13 and 15 mechanically inherited that artificial empty cohort.

### Attempt 03
Parser-only correction `4f59cc6e0b705e2ccbd91f2324a3a99ea70b73b7` added the exact observed source alias without changing a scientific threshold, snapshot, identity rule or firewall. Attempt 03 then computed the active cohort and passed all 18 frozen gates.

No correction used future event feedback.

## Termination-semantics boundary / termination 의미 경계

F01 proves that the historical terminated source contains source-native termination type/description, Claim/Non Claim structure and termination date with sufficient completeness to support a later preregistered adverse-event hierarchy.

F01 does **not** authorize treating every claim-bearing text substring as adverse in a future outcome definition. A descendant N01 must prospectively freeze the exact source-native event hierarchy, including explicit handling of partial-claim/re-engineering, assignment, acquired, conveyance, cancellation, correction and other ambiguous categories before future membership is opened.

## Future-outcome firewall / 미래 outcome 방화벽

- post-2026-09-21 terminated workbook rows opened: **0**
- future adverse membership opened: **false**
- future entity-body bytes consumed: **0**
- relationship/prediction/ranking/causal metric computed: **false**
- name/address/fuzzy/geospatial/manual identity repair: **false**

## Consequence / 후속 조치

This PASS authorizes **only** a separately preregistered outcome-blind `US-HUD-MF-N01` design stage.

Before any post-baseline terminated membership is opened, N01 must freeze:

1. one non-tautological historical exposure from the active/project/inspection structure;
2. baseline cohort and eligibility/exclusion rules;
3. exact project/property/inspection deduplication;
4. matching/stratification/comparator rules and balance/support gates;
5. exact adverse-vs-routine termination hierarchy, including ambiguous historical reason labels;
6. future monthly-snapshot cadence and first-event adjudication;
7. minimum future event support and primary statistical gate.

E01 is not authorized by this F01 alone.

Incremental monetary cost: **0 USD**.
