import unittest
from email.message import Message
from urllib.error import HTTPError, URLError
from tools import inspect_us_faa_air_f01_source_head as m

class Response:
    status = 200
    def __init__(self, url):
        self.url = url
        self.headers = Message()
        self.headers['Content-Length'] = '1234'
    def geturl(self): return self.url
    def __enter__(self): return self
    def __exit__(self, *args): return None

class MockOpener:
    def __init__(self, response=None, error=None):
        self.response = response
        self.error = error
    def open(self, request, timeout=0):
        self.method = request.get_method()
        if self.error: raise self.error
        return self.response

class FAAHeadTests(unittest.TestCase):
    def test_exact_whitelist_rejects_external(self):
        with self.assertRaises(ValueError):
            m.probe_head('https://example.org/mirror.zip')
    def test_uses_head_not_get(self):
        url = m.SOURCES['current_aircraft_zip']
        stub = MockOpener(Response(url))
        r = m.probe_head(url, stub)
        self.assertEqual(stub.method, 'HEAD')
        self.assertEqual(r['body_read_bytes'], 0)
    def test_http200_does_not_prove_body(self):
        url = m.SOURCES['current_aircraft_zip']
        r = m.probe_head(url, MockOpener(Response(url)))
        self.assertEqual(r['result'], 'HEAD_METADATA_ACCESSIBLE_NOT_BODY_PROVEN')
    def test_http_error_does_not_prove_absence(self):
        url = m.SOURCES['historical_2020_zip']
        hdr = Message()
        hdr['Location'] = 'https://www.faa.gov/office'
        r = m.probe_head(url, MockOpener(error=HTTPError(url, 302, 'redirect', hdr, None)))
        self.assertEqual(r['http_status'], 302)
        self.assertEqual(r['redirect_location'], 'https://www.faa.gov/office')
        self.assertEqual(r['result'], 'HEAD_NOT_VERIFIED_NO_FINAL_ABSENCE_INFERENCE')
    def test_transport_failure_inconclusive(self):
        url = m.SOURCES['official_dictionary']
        r = m.probe_head(url, MockOpener(error=URLError('dns')))
        self.assertIsNone(r['http_status'])
        self.assertEqual(r['error_type'], 'URLError')
    def test_no_redirect_follow(self):
        self.assertIsNone(m.BlockRedirect().redirect_request(None, None, 302, '', {}, 'https://evil.net/'))
    def test_any_missing_historical_holds(self):
        report = {k: {'http_status': 200} for k in m.SOURCES}
        report['historical_2020_zip']['http_status'] = 302
        self.assertEqual(m.classify(report), 'HOLD_FAA_F01_SOURCE_TRANSPORT_OR_LINEAGE_NOT_VERIFIED')
    def test_all200_still_no_science_pass(self):
        self.assertEqual(m.classify({k: {'http_status': 200} for k in m.SOURCES}), 'CONTINUE_FAA_F01_BODY_ACCESS_NOT_YET_PROVEN')

if __name__ == '__main__':
    unittest.main()
