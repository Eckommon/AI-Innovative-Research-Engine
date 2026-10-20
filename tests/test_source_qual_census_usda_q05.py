"""Q05 no-network identifier-only source-grain & frozen SHA synthetic fixtures."""
import hashlib
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest import mock
import zipfile
from tools import qualify_source_census_usda_q05 as q

def make_census(geos):
    raw="USPS\tGEOID\tNAME\n"+"".join("01\t"+geo+"\tSECRET_NAME\n" for geo in geos)
    content=raw.encode()
    buff=io.BytesIO()
    with zipfile.ZipFile(buff,"w",zipfile.ZIP_DEFLATED) as z:
        z.writestr(q.CENSUS_MEMBER,content)
    return buff.getvalue(),len(content)

def make_usda(ids):
    return q.USDA_HEADER+b"\n"+b"".join(code.encode()+b",SECRET_STATE,SECRET_COUNTY,Secret_Attribute,SECRET_VALUE\n" for code in ids)

class TestSourceQ05(unittest.TestCase):
    def test01_literal_fixed_width_code(self):
        self.assertEqual(q.norm_key(b" 01001\r"),b"01001")
        for val in (b"1001",b"0101",b"XX001",b"00000",b"01000",b"01999"):
            self.assertIsNone(q.norm_key(val))
    def test02_census_reads_only_exact_geoid(self):
        raw,n=make_census(["01001","01003"])
        k,c=q.read_census_keys(raw,expected_uncompressed=n)
        self.assertEqual(k,{b"01001",b"01003"})
        self.assertEqual(c["census_duplicate_key_rows"],0)
        self.assertNotIn("SECRET_NAME",json.dumps(c))
    def test03_repeated_census_key_is_hard_hold(self):
        raw,n=make_census(["01001","01001"])
        with self.assertRaises(q.UnexpectedCensusGrain):
            q.read_census_keys(raw,expected_uncompressed=n)
    def test04_usda_long_grain_deduplicates_only_code(self):
        keys,count=q.read_usda_keys(make_usda(["01001","01001","01003","XX888"]))
        self.assertEqual(keys,{b"01001",b"01003"})
        self.assertEqual(count["usda_duplicate_fips_rows"],1)
        self.assertEqual(count["invalid_usda_key_rows"],1)
        self.assertNotIn("SECRET_VALUE",json.dumps(count))
    def test05_usda_exact_frozen_header_required(self):
        with self.assertRaises(ValueError):
            q.read_usda_keys(b"FIPS,State,RUCC\n01001,TEST,9\n")
    def test06_support_threshold_pass_only_syntax(self):
        keys={f"{s:02d}{c:03d}".encode() for s in range(1,51) for c in range(1,61)}
        x,v=q.metrics(keys,keys,{"invalid_census_key_rows":0,"census_duplicate_key_rows":0},
                      {"invalid_usda_key_rows":0,"usda_duplicate_fips_rows":1})
        self.assertEqual(v,"PASS_Q05_SOURCE_NATIVE_FIPS_SYNTAX_SUPPORT_ONLY__GEOGRAPHY_VINTAGE_UNVERIFIED")
        self.assertEqual(x["distinct_key_overlap"],3000)
    def test07_threshold_insufficient_overlap(self):
        keys={f"01{c:03d}".encode() for c in range(1,60)}
        _,v=q.metrics(keys,keys,{"census_duplicate_key_rows":0},{"usda_duplicate_fips_rows":1})
        self.assertEqual(v,"HOLD_Q05_INSUFFICIENT_NATIVE_FIPS_SUPPORT")
    def test08_wrong_source_hash_fails_before_ids(self):
        raw=b"TEST"
        with mock.patch.object(q,"EXPECTED",{"CENSUS_2024_COUNTIES":(4,"f"*64)}):
            with self.assertRaises(q.RotatedSource):
                q.require_original("CENSUS_2024_COUNTIES",raw,{"full_body_bytes":4,"full_body_sha256":"f"*64})
    def test09_two_source_bad_digest_yields_one_persistable_hold(self):
        raw,n=make_census(["01001"])
        usda=make_usda(["01001"])
        bodies={"CENSUS_2024_COUNTIES":raw,"USDA_2023_RUCC":usda}
        m={k:(len(v),hashlib.sha256(v).hexdigest()) for k,v in bodies.items()}
        m["USDA_2023_RUCC"]=(len(usda),"f"*64)
        with TemporaryDirectory() as folder:
            target=Path(folder)/"evidence/attempt-01.json"
            calls=[]
            def fetch(label,url):
                calls.append(label)
                x=bodies[label]
                return x,{"full_body_bytes":len(x),"full_body_sha256":hashlib.sha256(x).hexdigest()}
            with mock.patch.object(q,"EXPECTED",m),mock.patch.object(q,"verify_context"):
                result=q.run(fetch=fetch,out=target)
            self.assertEqual(result["disposition"],"HOLD_Q05_SOURCE_VINTAGE_CHANGED")
            self.assertEqual(calls,["CENSUS_2024_COUNTIES","USDA_2023_RUCC"])
            self.assertIsNone(result["aggregated_source_native_support"])
            self.assertNotIn("01001",target.read_text())
    def test10_valid_bodies_dont_store_individual_code(self):
        census,n=make_census(["01001","01003"])
        usda=make_usda(["01001","01001","01003"])
        bodies={"CENSUS_2024_COUNTIES":census,"USDA_2023_RUCC":usda}
        expected={k:(len(v),hashlib.sha256(v).hexdigest()) for k,v in bodies.items()}
        with TemporaryDirectory() as folder:
            target=Path(folder)/"evidence/attempt-01.json"
            def fetch(label,url):
                raw=bodies[label]
                return raw,{"full_body_bytes":len(raw),"full_body_sha256":hashlib.sha256(raw).hexdigest()}
            original=q.read_census_keys
            with mock.patch.object(q,"EXPECTED",expected),mock.patch.object(q,"verify_context"),mock.patch.object(q,"read_census_keys",side_effect=lambda raw:original(raw,expected_uncompressed=n)):
                result=q.run(fetch=fetch,out=target)
            self.assertEqual(result["disposition"],"HOLD_Q05_INSUFFICIENT_NATIVE_FIPS_SUPPORT")
            self.assertNotIn("01001",target.read_text())
            self.assertNotIn("SECRET_",target.read_text())
            self.assertFalse(result["science_f01_authorized"])
            with self.assertRaises(RuntimeError):
                q.run(fetch=fetch,out=target)
    def test11_no_outcome_values_from_invalid_member(self):
        bio=io.BytesIO()
        with zipfile.ZipFile(bio,"w") as z:
            z.writestr("../wrong.txt",b"GEOID\n01001\n")
        with self.assertRaises(ValueError):
            q.read_census_keys(bio.getvalue(),expected_uncompressed=12)
if __name__=="__main__":
    unittest.main()
