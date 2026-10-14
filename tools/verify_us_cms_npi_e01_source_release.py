#!/usr/bin/env python3
"""Operational-only pre-experiment source release lock for US-CMS-NPI-E01.

No scientific definition, exposed/control matching, result threshold or frozen
experiment runner is changed. Fetches the CMS HTML listing only, not a ZIP.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path
from urllib.parse import urlparse
import hashlib
import json
import re

from tools.watch_us_cms_npi_e01_first_weekly import (
    URL, CONTRACT, BASELINE, EVIDENCE, classify_html, fetch_html
)

CANDIDATE = EVIDENCE / "source-candidate-01.json"
RELEASE = EVIDENCE / "source-release-authorization-01.json"
CHECKPOINT = Path(__file__).resolve().parents[1] / "context/checkpoint.json"
IDENTITY_FIELDS = ("token", "start", "end", "href")
PASS = "PASS_US_CMS_NPI_E01_SOURCE_RELEASE_LOCK"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def source_identity(value):
    require(isinstance(value, dict), "Source is not a record")
    require(all(isinstance(value.get(k), str) and value[k] for k in IDENTITY_FIELDS),
            "Source has missing identity fields")
    start = date.fromisoformat(value["start"])
    end = date.fromisoformat(value["end"])
    require(start >= BASELINE and end > BASELINE and start <= end,
            "Source outside preregistered future-week window")
    target = urlparse(value["href"])
    require(target.scheme == "https" and target.netloc == "download.cms.gov",
            "Source is not exact official CMS HTTPS")
    require(target.path.startswith("/nppes/") and target.path.lower().endswith(".zip")
            and not target.query and not target.fragment,
            "Official ZIP path is unexpected")
    require(value["token"] in target.path and re.fullmatch(r"\d{6}_\d{6}", value["token"]),
            "Source href does not match weekly date token")
    return tuple(value[k] for k in IDENTITY_FIELDS)


def validate_records(candidate, release, live, candidate_sha, prior, checkpoint):
    require(checkpoint.get("checkpoint_id") == "CHK-20261013-US-CMS-NPI-E01-ACTIVE"
            and checkpoint.get("active_issue") == 203
            and checkpoint.get("active_research") == "US-CMS-NPI-E01"
            and checkpoint.get("last_decision") == "DEC-318",
            "Canonical project state not at E01 active checkpoint")
    require(prior.get("contract_sha") == CONTRACT
            and prior.get("disposition") == "WAIT_SOURCE_US_CMS_NPI_E01"
            and prior.get("preflight") == 3 and prior.get("metadata_only") is True
            and prior.get("zip_body_opened") is False
            and prior.get("future_membership_opened") is False,
            "Prior source snapshot is invalid")
    require(candidate.get("contract_sha") == CONTRACT
            and candidate.get("research") == "US-CMS-NPI-E01"
            and candidate.get("type") == "FIRST_OBSERVED_SOURCE_CANDIDATE_METADATA_ONLY"
            and candidate.get("disposition") == "SOURCE_CANDIDATE_OBSERVED_US_CMS_NPI_E01"
            and candidate.get("scientific_first_published_weekly_adjudicated") is False
            and candidate.get("requires_explicit_issue_marker_before_experiment") is True
            and candidate.get("zip_body_opened") is False
            and candidate.get("future_membership_opened") is False,
            "First candidate evidence is invalid")
    require(isinstance(candidate.get("source_page"), dict)
            and candidate["source_page"].get("url") == URL
            and candidate["source_page"].get("http_status") == 200,
            "Candidate official listing HTTP source invalid")
    require(isinstance(candidate.get("weekly_listings"), list)
            and isinstance(candidate.get("qualifying_count"), int),
            "Candidate observed listing missing")
    candidate_rows = candidate["weekly_listings"]
    eligible = sorted((r for r in candidate_rows
                       if date.fromisoformat(r["start"]) >= BASELINE
                       and date.fromisoformat(r["end"]) > BASELINE),
                      key=lambda r: (r["start"], r["end"], r["token"]))
    require(candidate["qualifying_count"] == len(eligible) and len(eligible) >= 1,
            "Candidate's eligible-week count is inconsistent")
    chosen = candidate.get("earliest_observed_qualifying")
    locked_identity = source_identity(chosen)
    require(locked_identity == source_identity(eligible[0]),
            "Candidate is not earliest eligible observed weekly")
    require(re.fullmatch(r"[0-9a-f]{64}", candidate_sha) is not None,
            "Candidate hash unavailable")
    require(release.get("research") == "US-CMS-NPI-E01"
            and release.get("issue") == 203
            and release.get("contract_sha") == CONTRACT
            and release.get("decision") == PASS
            and release.get("candidate_sha256") == candidate_sha,
            "Release authorization is absent or mismatched to immutable candidate")
    require(release.get("first_publication_adjudication") == "PASS"
            and release.get("prior_week_exclusion_reviewed") is True
            and release.get("zip_body_opened") is False
            and release.get("future_membership_opened") is False
            and release.get("incremental_monetary_cost_usd") == 0,
            "First-publication determination and scientific firewall absent")
    require(isinstance(release.get("evidence_refs"), list)
            and len(release["evidence_refs"]) >= 2
            and all(isinstance(s, str) and s.startswith("research/US-CMS-NPI-E01/evidence/")
                    for s in release["evidence_refs"]),
            "Independent release review provenance incomplete")
    require(isinstance(release.get("review_notes"), str)
            and len(release["review_notes"].strip()) >= 40,
            "Explicit source lineage rationale required")
    require(source_identity(release.get("approved_source")) == locked_identity,
            "Release record points at a different source")
    require(isinstance(live, dict)
            and live.get("qualifying_count", 0) >= 1,
            "No currently qualifying CMS source")
    require(source_identity(live.get("earliest_observed_qualifying")) == locked_identity,
            "Live CMS earliest source diverges from locked, released candidate")
    return {"disposition": PASS, "approved_source": dict(zip(IDENTITY_FIELDS, locked_identity)),
            "candidate_sha256": candidate_sha,
            "live_qualifying_count": live["qualifying_count"],
            "zip_body_opened": False, "future_membership_opened": False}


def main():
    if not CANDIDATE.exists() or not RELEASE.exists():
        raise RuntimeError("SOURCE_WAIT: first candidate AND reviewed immutable release authorization both required")
    prior = json.loads((EVIDENCE / "source-preflight-03.json").read_text(encoding="utf-8"))
    candidate_raw = CANDIDATE.read_bytes()
    candidate = json.loads(candidate_raw)
    release = json.loads(RELEASE.read_text(encoding="utf-8"))
    cp = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    html, source_meta = fetch_html()  # CMS HTML metadata only, never the ZIP.
    live = classify_html(html, source_meta["url"])
    record = validate_records(candidate, release, live, hashlib.sha256(candidate_raw).hexdigest(), prior, cp)
    print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    main()
