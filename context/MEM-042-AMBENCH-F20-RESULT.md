---
id: MEM-042-AMBENCH-F20-RESULT
type: memory
state: ACTIVE
created: 2026-08-23
source_of_truth: github
---

# MEM-042 — AMBENCH-F20 result / F20 결과

F20 completed with `PASS_F20_WORKBOOK_IMMUTABLE_SCHEMA_READY`.

Durable facts:
- `mds2-2514/OverhangX16_ImageHistograms.xlsx` NERDm SHA-256 = `7cc48fc8aa7a86af4e00c24bfcf91373ef15a8bc1e10d404e61ba8f4d29c422f`;
- transient authoritative workbook local SHA-256 matched exactly;
- schema-only inspection found `Plots` + exactly sixteen `Part1_1`…`Part4_4` sheets; each part sheet `A1:B256`, formula count 0;
- numerical XCT cell values were not emitted or analyzed;
- `mds2-2309/XYPT_L101-L125.zip` current NERDm SHA-256 = `b5f6c58540799f57c64b59ab4c0770f1aad8ac32b6bfb3161babdf244e32ff31`, size 157616390 bytes, official NIST URL established;
- direct XYPT sidecar/ZIP retrieval still failed, so local XYPT checksum and numerical F19 segmentation validation remain pending;
- F19 segmentation methodology remains frozen and unchanged;
- E19 numerical process↔XCT work is not yet active. Before E19, freeze authoritative semantics for workbook columns A/B/XCT endpoint and verify retrieved XYPT bytes against the NERDm hash.

Cost: 0 USD incremental. Public standard GitHub-hosted runners only; no artifacts/cache/larger runners/paid source or API.
