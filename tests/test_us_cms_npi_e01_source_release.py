"""Offline regression tests for E01 source release preflight; never use real provider rows."""
from copy import deepcopy
import unittest

from tools.verify_us_cms_npi_e01_source_release import (
    PASS, CONTRACT, URL, validate_records
)

OLD = {
    "token": "100526_101126", "start": "2026-10-05", "end": "2026-10-11",
    "href": "https://download.cms.gov/nppes/NPPES_Data_Dissemination_100526_101126_Weekly_V2.zip",
}
FIRST = {
    "token": "101226_101826", "start": "2026-10-12", "end": "2026-10-18",
    "href": "https://download.cms.gov/nppes/NPPES_Data_Dissemination_101226_101826_Weekly_V2.zip",
}
LATER = {
    "token": "101926_102526", "start": "2026-10-19", "end": "2026-10-25",
    "href": "https://download.cms.gov/nppes/NPPES_Data_Dissemination_101926_102526_Weekly_V2.zip",
}
HASH = "a" * 64


def fixture():
    candidate = {
        "research": "US-CMS-NPI-E01",
        "contract_sha": CONTRACT,
        "type": "FIRST_OBSERVED_SOURCE_CANDIDATE_METADATA_ONLY",
        "disposition": "SOURCE_CANDIDATE_OBSERVED_US_CMS_NPI_E01",
        "source_page": {"url": URL, "http_status": 200},
        "earliest_observed_qualifying": dict(FIRST),
        "weekly_listings": [dict(OLD), dict(FIRST)],
        "qualifying_count": 1,
        "scientific_first_published_weekly_adjudicated": False,
        "requires_explicit_issue_marker_before_experiment": True,
        "zip_body_opened": False,
        "future_membership_opened": False,
    }
    release = {
        "research": "US-CMS-NPI-E01",
        "issue": 203,
        "contract_sha": CONTRACT,
        "candidate_sha256": HASH,
        "decision": PASS,
        "first_publication_adjudication": "PASS",
        "prior_week_exclusion_reviewed": True,
        "zip_body_opened": False,
        "future_membership_opened": False,
        "incremental_monetary_cost_usd": 0,
        "evidence_refs": [
            "research/US-CMS-NPI-E01/evidence/source-preflight-03.json",
            "research/US-CMS-NPI-E01/evidence/source-candidate-01.json",
        ],
        "review_notes": "Official CMS post-contract chronological listing verified; no earlier eligible weekly was published in inspected official snapshots.",
        "approved_source": dict(FIRST),
    }
    live = {"qualifying_count": 1, "earliest_observed_qualifying": dict(FIRST)}
    prior = {
        "contract_sha": CONTRACT,
        "disposition": "WAIT_SOURCE_US_CMS_NPI_E01",
        "preflight": 3, "metadata_only": True,
        "zip_body_opened": False, "future_membership_opened": False,
    }
    cp = {
        "checkpoint_id": "CHK-20261013-US-CMS-NPI-E01-ACTIVE",
        "active_issue": 203, "active_research": "US-CMS-NPI-E01",
        "last_decision": "DEC-318",
    }
    return [candidate, release, live, HASH, prior, cp]


class ReleaseLockTests(unittest.TestCase):
    def test_valid_released_first_week(self):
        x = fixture()
        self.assertEqual(validate_records(*x)["disposition"], PASS)

    def test_wrong_candidate_hash_rejected(self):
        x = fixture()
        x[1]["candidate_sha256"] = "b" * 64
        with self.assertRaises(ValueError): validate_records(*x)

    def test_no_independent_review_rejected(self):
        x = fixture()
        x[1]["first_publication_adjudication"] = "UNKNOWN"
        with self.assertRaises(ValueError): validate_records(*x)

    def test_missing_lineage_provenance_rejected(self):
        x = fixture()
        x[1]["evidence_refs"] = []
        with self.assertRaises(ValueError): validate_records(*x)

    def test_outcome_opened_rejected(self):
        x = fixture()
        x[0]["zip_body_opened"] = True
        with self.assertRaises(ValueError): validate_records(*x)

    def test_later_live_week_cannot_replace_frozen_candidate(self):
        x = fixture()
        x[2]["earliest_observed_qualifying"] = dict(LATER)
        with self.assertRaises(ValueError): validate_records(*x)

    def test_original_candidate_cannot_select_later_week(self):
        x = fixture()
        x[0]["weekly_listings"].append(dict(LATER))
        x[0]["qualifying_count"] = 2
        x[0]["earliest_observed_qualifying"] = dict(LATER)
        x[1]["approved_source"] = dict(LATER)
        with self.assertRaises(ValueError): validate_records(*x)

    def test_unofficial_source_domain_rejected(self):
        x = fixture()
        x[1]["approved_source"]["href"] = x[1]["approved_source"]["href"].replace("download.cms.gov", "evil.example")
        with self.assertRaises(ValueError): validate_records(*x)

    def test_weekly_identity_must_match_zip_path(self):
        x = fixture()
        x[1]["approved_source"]["href"] = LATER["href"]
        with self.assertRaises(ValueError): validate_records(*x)

    def test_active_issue_checkpoint_required(self):
        x = fixture()
        x[5]["active_issue"] = 204
        with self.assertRaises(ValueError): validate_records(*x)

    def test_not_prospective_if_old_week(self):
        x = fixture()
        x[1]["approved_source"] = deepcopy(OLD)
        with self.assertRaises(ValueError): validate_records(*x)


if __name__ == "__main__":
    unittest.main()
