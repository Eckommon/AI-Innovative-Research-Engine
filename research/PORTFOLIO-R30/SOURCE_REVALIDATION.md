# PORTFOLIO-R30 Source Revalidation / 공식 source 재검증

Date: 2026-09-16

This note records only source/access/identity and literature-overlap facts used for portfolio scoring. No candidate outcome magnitudes or candidate relationships were opened.

## US-FDA-MD-001

- FDA states its Inspection Classification Database contains final `NAI`, `VAI`, `OAI` classifications but is not a comprehensive listing of all inspections.
- FDA's current Inspections Data Dashboard offers an `Entire Inspections Dataset` download and identifies inspection classification by Project Area. API access now uses credentials, but the dashboard exposes downloadable public data; F01 must verify the exact zero-cost machine-readable route rather than assume it.
- FDA's Data Dashboard glossary defines FEI as the unique FDA Establishment Identifier.
- Current CDRH Regulatory Reliance guidance explicitly instructs users to search medical-device manufacturing facilities by facility name, address, or **FEI** and filter by medical-device inspection type.
- openFDA Device Recall exposes native `firm_fei_number`, recall initiation/created/posted dates and product/recall identities. An API key is not required for ordinary openFDA use, although rate limits apply.
- Current search found related inspection-classification studies and case-specific device inspection/recall histories, but did not establish a near-identical public FEI-level prospective classification→later-recall study. This is not proof of novelty.

## US-CMS-NH-001

- CMS PBJ Daily Nurse Staffing is public/free, quarterly updated, and provides daily facility staffing observations.
- CMS Health Deficiencies is public/free, exposes CCN, inspection date, citation tag/description, scope/severity and correction date, with API/download access.
- A 2023 JAMA Network Open/PubMed study used 14,717 nursing homes and merged PBJ, Nursing Home Care Compare and related data; staffing instability was evaluated against quality outcomes including deficiency citations.
- Earlier national/panel studies also directly analyzed staffing levels against regulatory deficiencies. Therefore exact-data availability is strong but marginal novelty/information gain is low.

## US-PIPE-001

Carry forward R29 without rescue:
- public PHMSA accident/incident and annual mileage/facility data remain useful;
- unrestricted national NPMS pipeline-line GIS may not be assumed for the general public;
- original line-resolved hydrologic exposure concept therefore has weakened public join defensibility;
- direct hydrologic/pipeline-incident overlap remains high.

## Boundary

These facts support only portfolio scoring. They do not establish that FDA inspection classifications predict recalls, that staffing instability causes deficiencies, or that hydrologic stress causes pipeline incidents.
