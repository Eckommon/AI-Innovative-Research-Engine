# PORTFOLIO-R30 Scorecard / 점수표

Scoring uses the frozen R26–R29 Mission-ROI rubric, 0–5 each, total /45. Candidate outcomes remain unopened.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **US-FDA-MD-001 inspection classification → later device recall** | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 3 | **41** |
| US-CMS-NH-001 staffing instability → later health deficiencies | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 0 | **36** |

## Scoring rationale / 점수 근거

### US-FDA-MD-001 — 41/45

- **Mission bottleneck 5:** manufacturing quality surveillance and downstream product recall are directly decision-relevant regulatory/industrial quality signals.
- **Cross-source 5:** inspection-classification source and device-recall source are separate FDA data products with distinct event semantics.
- **Direct outcome 5:** a recall event is a direct regulated product-quality/safety action, though not necessarily caused by the inspected facility condition.
- **Independent-unit prospect 4:** FEI is an exact facility key, but inspections are risk/for-cause selected and facilities may have repeated inspections/project areas. A prospective F01/N01 must freeze one baseline inspection identity and repeated-unit rules.
- **Practical value 5:** a validated bounded signal could support quality-risk prioritization and due-diligence workflows.
- **Zero-cost operability 5:** public dashboard/download and openFDA routes are free; F01 must verify the actual current downloadable inspection route and stay within public rate limits.
- **Join defensibility 4:** FDA defines FEI as a unique establishment identifier, CDRH guidance supports FEI search for device manufacturers, and Device Recall exposes `firm_fei_number`. One point is withheld because the public inspection database is explicitly non-comprehensive and the actual downloaded inspection schema must still be confirmed.
- **Next-gate information gain 5:** one outcome-blind F01 can decisively resolve downloadable inspection schema, CDRH/project-area filtering, FEI cardinality, temporal coverage and exact recall-FEI overlap without reading recall incidence by classification.
- **Low overlap / novelty risk 3:** related inspection and recall work exists, but current search did not establish a near-identical public FEI-level prospective inspection-classification→later-recall design. This is not a novelty claim.

### US-CMS-NH-001 — 37/45

Source quality and exact CCN join are excellent, but direct published work has already linked PBJ staffing instability to deficiency citations. Therefore Next-gate information gain = 2 and Low-overlap/novelty = 0 despite otherwise strong operability.

### US-PIPE-001 — 36/45

Carry forward R29 exactly: public incident/mileage sources remain strong, but unrestricted line-resolved NPMS geometry cannot be assumed, so Join defensibility = 3. Direct overlap remains high, Low-overlap/novelty = 0.

## Frozen selection

`US-FDA-MD-001` leads outright at **41/45**, so no tie-break is needed.

R30 authorizes only a separate outcome-blind FDA medical-device source/identity feasibility gate. It does not authorize opening recall incidence by inspection class or computing a relationship.
