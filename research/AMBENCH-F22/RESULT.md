---
id: AMBENCH-F22-RESULT
type: feasibility-result
state: COMPLETED_PARTIAL_ALL_FOUR_IMMUTABLE_BYTES_READY_SCHEMA_HEADER_HOLD
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F22/README.md
  - research/AMBENCH-F22/AMENDMENT-01.md
  - research/AMBENCH-F22/AMENDMENT-02.md
  - Issue #40
---

# AMBENCH-F22 Result — `mds2-3761` NERDm Immutable Source Recovery
# AMBENCH-F22 결과 — `mds2-3761` NERDm 불변 source 회수

**Final descriptive gate / 최종 기술 판정:** **`PARTIAL_F22_ALL_FOUR_IMMUTABLE_BYTES_READY__SCHEMA_HEADER_HOLD`**

## 1. Executive result / 핵심 결과

**KO:** F15/F16에서 미해결이었던 `mds2-3761` source-integrity 문제는 크게 진전됐다. Current NIST NERDm은 네 registered ZIP 모두에 대해 exact component identity, official downloadURL, size, SHA-256을 제공한다. Public standard GitHub-hosted runner에서 네 ZIP을 transient하게 회수했고 네 local SHA-256이 NERDm hash와 모두 정확히 일치했다. 또한 각 ZIP은 valid하며 정확히 250개 CSV, `L0001.csv`–`L0250.csv` layer coverage를 갖는다. 따라서 **all-four immutable source bytes는 준비 상태**다.

그러나 preregistration은 textual 40-column CSV header를 요구했는데 실제 CSV는 headerless였다. Part 1 workflow가 이를 예상하지 못해 첫 numerical row를 header로 오인하여 제한적 numerical exposure를 발생시켰다. 이 사실은 `AMENDMENT-01`에 기록했고 current-facing result에서는 값 자체를 제거했다. 원래 full PASS의 header/schema 조건은 충족되지 않았으므로 full PASS로 보고하지 않는다.

**EN:** The `mds2-3761` source-integrity blocker from F15/F16 is materially reduced. Current NIST NERDm provides exact component identity, official downloadURL, size, and SHA-256 for all four registered ZIPs. All four ZIPs were transiently recovered on a public standard GitHub-hosted runner, and every local SHA-256 exactly matched NERDm. Each ZIP is valid and contains exactly 250 CSVs with deterministic `L0001.csv`–`L0250.csv` coverage. Thus **all-four immutable source bytes are ready**.

However, the preregistration required a textual 40-column CSV header, while the actual files are headerless. The Part 1 workflow misinterpreted the first numerical row as a header, causing limited numerical exposure. This is recorded in `AMENDMENT-01`, and current-facing files no longer reproduce the values. Because the original full PASS header/schema condition is unmet, F22 is not reported as full PASS.

## 2. Current authoritative dataset / 현재 권위 dataset
- identifier: `ark:/88434/mds2-3761`;
- NIST registered X4 dataset;
- public distributions: `part1.zip`, `part02.zip`, `part03.zip`, `part04.zip`;
- NIST AMS 100-69 remains the authoritative semantic/schema description.

## 3. Immutable component evidence / 불변 component 증거

| component | size bytes | NERDm SHA-256 | local SHA-256 match |
|---|---:|---|---|
| `part1.zip` | 87,041,995 | `0bf229f5a04d181f4c79549fa6357a1bfe3095437b26bb660de5e86b35bb2ec3` | YES |
| `part02.zip` | 85,261,726 | `bf72d9e160d94094f9268fcf3f76a532c8a29fb64aff1afbec20256acaee178e` | YES |
| `part03.zip` | 83,521,608 | `89e9e1afadca22b9c34177d82972272a4e73789b19388f0c83d62a9ebd53d878` | YES |
| `part04.zip` | 81,225,258 | `6c3f655a1482001119c54d1f1e404a34eb401f386fffc06147628b36c7c8d7c5` | YES |

All were retrieved through official NIST downloadURLs discovered from NERDm. No raw ZIP was committed, cached, or stored as an artifact.

## 4. Archive inventory / archive inventory

All four archives:
- ZIP integrity test: PASS;
- file members: exactly 250;
- CSV members: exactly 250;
- first layer file: `L0001.csv` under the corresponding part directory;
- last layer file: `L0250.csv`;
- parsed unique layer count: 250;
- exact layer coverage 1..250: YES.

This independently confirms the documented four-part × 250-layer hierarchy at the archive level.

## 5. Headerless serialization discovery / headerless serialization 발견
The original F22 schema check assumed each CSV began with a textual header. Part 1 showed this assumption was false: CSVs are headerless.

Consequences:
- textual-header check = NOT PASSED;
- original `PASS_F22_REGISTERED_X4_IMMUTABLE_SOURCE_READY` = FAIL as written;
- do not infer column semantics from raw positions without the authoritative AMS 100-69 map;
- a separate schema/serialization qualification is required before modeling.

## 6. Limited numerical pre-exposure / 제한적 numerical 사전노출
`AMENDMENT-01` records an unintended numerical exposure during the attempted header check.

Current state:
**`NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED`**.

Known scope:
- workflow read the first line of each Part 1 CSV while attempting to parse headers;
- only the first CSV's parsed line was persisted as the purported canonical header in the initial result;
- current-facing result was redacted so those values are not repeated;
- no correlations, aggregation, ranking, model, feature selection, or process↔XCT statistic was computed;
- Parts 2–4 verification read zero CSV content lines.

Future experiments may proceed only with explicit disclosure that pristine outcome blindness was lost in this limited way.

## 7. Frozen gate application / frozen gate 적용

### Original full PASS
`PASS_F22_REGISTERED_X4_IMMUTABLE_SOURCE_READY`
- all-four exact component identity: PASS;
- all-four authoritative SHA-256: PASS;
- all-four local byte/hash verification: PASS;
- all-four valid 250-layer archive inventory: PASS;
- textual 40-column header/schema verification: **FAIL / structurally inapplicable because files are headerless**.

Result: **FAIL**.

### Amendment 02 descriptive gate
`PARTIAL_F22_ALL_FOUR_IMMUTABLE_BYTES_READY__SCHEMA_HEADER_HOLD`
- all-four immutable source-byte readiness: PASS;
- deterministic archive hierarchy: PASS;
- original textual-header condition unresolved: PASS condition;
- no modeling authorized: PASS.

Result: **PASS**.

## 8. Scientific interpretation / 과학적 해석
Supported now:
- exact immutable bytes for all four registered X4 part archives are reproducible;
- archive-level 4 × 250-layer structure is reproducible;
- F15/F16 source-access uncertainty is no longer the dominant blocker.

Not yet supported:
- numerical registered process↔XCT association;
- pristine outcome-blind status;
- raw-file positional column semantics without a separately frozen authoritative schema map;
- statistical independence of rows/layers/parts.

## 9. Consequence / 후속
Do not start modeling yet.

Next highest-leverage work is a separately preregistered **headerless serialization/schema mapping gate**:
1. freeze the exact 40-column order from NIST AMS 100-69;
2. verify headerless CSV field count structurally with numerical values suppressed;
3. confirm deterministic mapping from raw column positions 1..40 to documented feature semantics;
4. explicitly carry `VIOLATED_LIMITED` pre-exposure into any later experiment;
5. only after that may a low-degree-of-freedom registered process/melt-pool ↔ XCT experiment be preregistered.

## 10. Cost / 비용
Incremental monetary cost: `0 USD`. Public standard GitHub-hosted runners only. No paid API/source, larger runner, artifact storage, or cache was used.
