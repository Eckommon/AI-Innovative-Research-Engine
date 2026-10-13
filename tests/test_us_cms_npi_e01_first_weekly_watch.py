"""Offline fixture tests: no network/ZIP requests, no E01 outcomes."""
import unittest
from tools.watch_us_cms_npi_e01_first_weekly import URL, classify_html


def page(*labels):
    return "<html><body>" + "".join(
        '<a href="NPPES_Data_Dissemination_' + token + '_Weekly_V2.zip">'
        'NPPES Data Dissemination V.2 - Weekly Update - ' + token + '</a>'
        for token in labels
    ) + "</body></html>"


class SourceWatchTests(unittest.TestCase):
    def test_historical_week_only_wait(self):
        result = classify_html(page("100526_101126"), URL)
        self.assertEqual(result["qualifying_count"], 0)
        self.assertIsNone(result["earliest_observed_qualifying"])
        self.assertTrue(result["historical_anchor_still_visible"])

    def test_first_future_week_selected(self):
        result = classify_html(page("100526_101126", "101926_102526", "101226_101826"), URL)
        self.assertEqual(result["qualifying_count"], 2)
        self.assertEqual(result["earliest_observed_qualifying"]["token"], "101226_101826")

    def test_historical_anchor_may_rotate_off_live_page(self):
        # Preflight 03 immutable source has already established the official anchor.
        result = classify_html(page("101226_101826"), URL)
        self.assertEqual(result["qualifying_count"], 1)
        self.assertFalse(result["historical_anchor_still_visible"])

    def test_monthly_file_never_substitutes(self):
        html = ('<a href="NPPES_Data_Dissemination_October_2026_V2.zip">'
                'NPPES Data Dissemination V.2 - Monthly Update - 101226_101826</a>'
                + page("100526_101126"))
        result = classify_html(html, URL)
        self.assertEqual(result["qualifying_count"], 0)

    def test_untrusted_zip_domain_rejected(self):
        html = ('<a href="https://attacker.example/NPPES_101226_101826_Weekly_V2.zip">'
                'NPPES V.2 - Weekly Update - 101226_101826</a>')
        with self.assertRaises(ValueError):
            classify_html(html, URL)

    def test_non_official_redirect_rejected(self):
        with self.assertRaises(ValueError):
            classify_html(page("100526_101126"), "https://example.com/other")

    def test_ambiguous_duplicate_tokens_rejected(self):
        html = page("100526_101126") + (
            '<a href="NPPES_100526_101126_Weekly_V2.zip">'
            'NPPES Data Dissemination V.2 - Weekly Update - 100526_101126</a>')
        with self.assertRaises(ValueError):
            classify_html(html, URL)


if __name__ == "__main__":
    unittest.main()
