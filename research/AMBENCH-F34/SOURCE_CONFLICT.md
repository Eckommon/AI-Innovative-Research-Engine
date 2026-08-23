---
id: AMBENCH-F34-SOURCE-CONFLICT
type: source-integrity-record
state: ACTIVE
created: 2026-08-23
source_of_truth: official-nist-sources
candidate_outcomes_inspected: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-F34 Source Conflict — M32044 Part Count / Strategy Route
# AMBENCH-F34 Source 충돌 — M32044 Part 수 / Strategy Route

## Conflict / 충돌
Two current/authoritative NIST surfaces do not state the experiment part count consistently:

1. NIST AMMT `Datasets` summary describes the Three-Dimensional Scan Strategies dataset as **ten rectangular IN625 parts** with replicated geometry and varied scan strategies.
2. The linked NIST Journal of Research data-description article `10.6028/jres.124.033` explicitly labels **Part 1 through Part 12**, states that each part uses a unique scan strategy, and states that the melt-pool-monitoring selection cycle repeats every **12 layers**.

F34 does not silently normalize `10` to `12` or vice versa. For experiment-design semantics, the data-description article is more detailed, but the public-summary discrepancy remains a source-integrity caveat until an authoritative correction or direct immutable command-file inventory resolves it.

## Metadata.zip finding / Metadata.zip 결과
Checksum-verified `Metadata.zip` does not resolve the conflict or provide the part→scan-strategy assignment:
- `2018_AMMTLaserScanAngles.txt` contains laser-incidence-angle calibration tables only;
- bounded token inspection found zero occurrences of `part`, `cube`, `gcode`, `strategy`, `layer`, `mpm`, `camera`, or `trigger`;
- remaining metadata members are material certificates, powder composition/PSD, and a layer-camera dot-grid calibration image.

Exact scan-strategy descriptions are documented as directory/file labels inside `Build Command Data.zip`, which F34 deliberately did not download/open because it is ~7.42 GB and outside the frozen metadata-only source gate.

## Consequence / 결과
- Do not claim a clean replicated-strategy design from the metadata-only surface.
- Do not treat layers or MPM frames as independent physical replicates of a scan strategy.
- Do not claim exact part→strategy assignment until the build-command source is separately cost/scope-qualified.
- This conflict does not invalidate the PDR identity or the fact that scan strategy was deliberately varied; it blocks a full F34 PASS under the frozen route/replication requirements.
