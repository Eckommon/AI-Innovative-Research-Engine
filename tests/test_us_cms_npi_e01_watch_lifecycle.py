"""Offline, configuration-only regression checks for first-source watcher lifecycle."""
from pathlib import Path
import re
import unittest

WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/watch-us-cms-npi-e01-source.yml"


class WatchLifecycleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = WORKFLOW.read_text(encoding="utf-8")

    def test_six_hour_utc_distribution(self):
        self.assertIn("cron: '37 0,6,12,18 * * *'", self.content)

    def test_still_only_free_standard_runner(self):
        self.assertIn("runs-on: ubuntu-latest", self.content)
        self.assertNotIn("runs-on: ubuntu-latest-8-cores", self.content)
        self.assertNotIn("actions/upload-artifact", self.content)

    def test_no_automatic_experiment_execution(self):
        self.assertNotIn("python tools/run_us_cms_npi_e01.py", self.content)
        self.assertNotIn("gh workflow run", self.content)
        self.assertNotIn("gh issue edit", self.content)

    def test_issue_marker_is_read_only(self):
        marker = "EXECUTE_US_CMS_NPI_E01_ATTEMPT_01"
        self.assertEqual(self.content.count(marker), 1)
        self.assertIn("grep -Fxq '" + marker + "'", self.content)

    def test_dormant_after_candidate_or_attempt_or_issue_closed(self):
        self.assertIn("source-candidate-01.json; then", self.content)
        self.assertIn("attempt-01.json; then", self.content)
        self.assertIn('if test "$issue_state" != OPEN; then', self.content)
        self.assertGreaterEqual(self.content.count("monitor=false"), 4)

    def test_source_network_and_commit_steps_gated(self):
        for name in (
            "Recheck official CMS HTML listing only",
            "Save one-time monitored WAIT bootstrap receipt (no repeats)",
            "Validate candidate evidence if first seen",
            "Commit the first source candidate exactly once",
        ):
            self.assertIn(
                "- name: " + name + "\n        if: steps.gate.outputs.monitor == 'true'",
                self.content,
            )

    def test_candidate_notice_is_only_after_commit(self):
        self.assertIn('candidate_committed=true', self.content)
        self.assertIn("if: steps.persist.outputs.candidate_committed == 'true'", self.content)
        self.assertIn("gh issue comment 203", self.content)
        self.assertLess(
            self.content.index("git push origin HEAD:main"),
            self.content.index("candidate_committed=true"),
        )

    def test_candidate_notice_requires_review(self):
        self.assertIn("independent first-publication lineage review and source-release authorization required", self.content)
        self.assertIn("This is NOT an E01 statistical result", self.content)
        self.assertIn("issues: write", self.content)


if __name__ == "__main__":
    unittest.main()
