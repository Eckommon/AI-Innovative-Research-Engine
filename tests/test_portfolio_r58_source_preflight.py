import unittest
from email.message import Message
from urllib.error import HTTPError, URLError
from tools import inspect_portfolio_r58_official_sources as p


class MockResponse:
    status = 200
    def __init__(self, url, data, content_type="application/zip"):
        self.url = url
        self.data = data
        self.read_pos = 0
        self.headers = Message()
        self.headers["Content-Type"] = content_type
    def read(self, n):
        part = self.data[self.read_pos:self.read_pos+n]
        self.read_pos += len(part)
        return part
    def geturl(self):
        return self.url
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return None


class MockOpener:
    def __init__(self, res=None, err=None):
        self.res, self.err = res, err
    def open(self, req, timeout):
        self.method = req.get_method()
        if self.err:
            raise self.err
        return self.res


class SourcePreflight(unittest.TestCase):
    def test_only_frozen_exact_urls(self):
        with self.assertRaises(ValueError):
            p.inspect("https://other.example/quarterly.zip", "zip")

    def test_no_redirect(self):
        self.assertIsNone(p.NoRedirect().redirect_request(None, None, 302, "", {}, "https://other.example/"))

    def test_zip_reads_exact_four_bytes(self):
        url = p.SOURCES["NHTSA_campaign_zip"][0]
        res = MockResponse(url, b"PK\x03\x04" + b"FORBIDDEN_OUTCOME_RECORDS")
        stub = MockOpener(res)
        x = p.inspect(url, "zip", stub)
        self.assertEqual(stub.method, "GET")
        self.assertEqual(x["bytes_read"], 4)
        self.assertEqual(res.read_pos, 4)
        self.assertTrue(x["prefix_format_verified"])
        self.assertFalse(x["outcome_or_case_rows_parsed"])

    def test_html_with_200_does_not_prove_zip(self):
        url = p.SOURCES["Census_CBP_2023_county_zip"][0]
        x = p.inspect(url, "zip", MockOpener(MockResponse(url, b"<html>not ZIP</html>", "text/html")))
        self.assertFalse(x["prefix_format_verified"])

    def test_404_is_not_file_absence(self):
        url = p.SOURCES["NOAA_StormEvents_2023_gzip"][0]
        x = p.inspect(url, "gzip", MockOpener(err=HTTPError(url, 404, "missing", Message(), None)))
        self.assertEqual(x["status"], "HTTP_UNVERIFIED_NOT_ABSENCE")
        self.assertEqual(x["bytes_read"], 0)

    def test_http403_is_not_access_proof(self):
        url = p.SOURCES["NHTSA_quarterly_zip"][0]
        x = p.inspect(url, "zip", MockOpener(err=HTTPError(url, 403, "blocked", Message(), None)))
        self.assertEqual(x["http_status"], 403)

    def test_dictionary_html_fails_closed(self):
        url = p.SOURCES["NHTSA_quarterly_dictionary"][0]
        x = p.inspect(url, "text_dictionary", MockOpener(MockResponse(url, b"<html>replaced</html>", "text/html")))
        self.assertEqual(x["status"], "DICTIONARY_FORMAT_NOT_VERIFIED")

    def test_bls_header_only_and_no_first_data_row(self):
        url = p.SOURCES["BLS_QCEW_2024_county_csv_header"][0]
        data = b"area_fips,industry_code,year,qtr\n" + b"01001,10,2024,1,CONFIDENTIAL"
        res = MockResponse(url, data, "text/csv")
        x = p.inspect(url, "csv_header", MockOpener(res))
        self.assertEqual(x["status"], "CSV_HEADER_ONLY_ACCESSED")
        self.assertNotIn("CONFIDENTIAL", x["csv_header"])
        self.assertEqual(res.read_pos, len(b"area_fips,industry_code,year,qtr\n"))

    def test_nonjoinable_no_promotion(self):
        outcomes = {k: {"status": "PREFIX_MATCH_BODY_UNINSPECTED"}
                    for k in p.SOURCES}
        outcomes["NHTSA_campaign_dictionary"]["status"] = "DICTIONARY_PREFIX_ACCESSED_ONLY"
        outcomes["NHTSA_quarterly_dictionary"]["status"] = "DICTIONARY_PREFIX_ACCESSED_ONLY"
        outcomes["BLS_QCEW_2024_county_csv_header"]["status"] = "CSV_HEADER_ONLY_ACCESSED"
        value = p.assess(outcomes)
        self.assertEqual(value["NHTSA"], "METADATA_PREFIX_READY_NO_JOIN_PROOF")
        self.assertEqual(value["CBP_QCEW"], "METADATA_ACCESS_ONLY_NO_JOIN_PROOF")

    def test_transport_unavailable_holds(self):
        url = p.SOURCES["NHTSA_campaign_zip"][0]
        x = p.inspect(url, "zip", MockOpener(err=URLError("offline")))
        self.assertEqual(x["status"], "TRANSPORT_INCONCLUSIVE")

if __name__ == "__main__":
    unittest.main()
