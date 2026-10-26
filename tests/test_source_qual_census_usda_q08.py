"""Q08 synthetic no-network 2023/24 county GEOID only safeguards."""
import io
import json
import hashlib
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest import mock
import zipfile
from tools import qualify_source_census_usda_q08 as q

def fixture(ids, label="CENSUS_2023_COUNTIES", duplicate=False):
    member=q.SOURCES[label][2]
    content=(b"USPS\tGEOID\tNAME\tALAND\n"+
      b"".join(b"ST\t"+x+b"\tSECRET_COUNTY\tSECRET_AREA\n" for x in ids)+
      (b"ST\t"+ids[0]+b"\tSECRET_COUNTY\tSECRET_AREA\n" if duplicate else b""))
    out=io.BytesIO()
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as arc:
        arc.writestr(member,content)
    return out.getvalue(),len(content)

def specs(blobs, lengths):
    return {name:(len(raw),hashlib.sha256(raw).hexdigest(),q.SOURCES[name][2],lengths[name])
            for name,raw in blobs.items()}

class Q08SyntheticTests(unittest.TestCase):
    def test01_leading_zero_fips_stays_string(self):
        self.assertEqual(q.validate_key(b" 01001\n"),b"01001")
        self.assertIsNone(q.validate_key(b"1001"))
    def test02_disallow_invalid_codes(self):
        for value in (b"00000",b"01000",b"01999",b"AA001",b"01-001",b""):
            self.assertIsNone(q.validate_key(value))
    def test03_exact_2023_zip_member_and_field_projection(self):
        name="CENSUS_2023_COUNTIES";raw,length=fixture([b"01001",b"01003"],name)
        with mock.patch.dict(q.SOURCES,{name:(len(raw),hashlib.sha256(raw).hexdigest(),q.SOURCES[name][2],length)}):
            keys,stats=q.read_only_geoid(raw,name)
        self.assertEqual(keys,{b"01001",b"01003"})
        self.assertEqual(stats["invalid_rows"],0)
        self.assertNotIn("SECRET_COUNTY",json.dumps(stats))
    def test04_repeated_key_fails_closed(self):
        name="CENSUS_2024_COUNTIES";raw,length=fixture([b"01001"],name,duplicate=True)
        with mock.patch.dict(q.SOURCES,{name:(len(raw),hashlib.sha256(raw).hexdigest(),q.SOURCES[name][2],length)}):
            with self.assertRaises(q.UnexpectedKeyGrain):q.read_only_geoid(raw,name)
    def test05_bad_zip_member_not_repaired(self):
        raw,_=fixture([b"01001"],"CENSUS_2024_COUNTIES")
        with self.assertRaises(ValueError):q.read_only_geoid(raw,"CENSUS_2023_COUNTIES")
    def test06_original_sha_mismatch_fails_before_rows(self):
        name="CENSUS_2023_COUNTIES"
        with self.assertRaises(q.SourceVintageChanged):
            q.check_original(name,b"wrong",{"bytes":5,"sha256":hashlib.sha256(b"wrong").hexdigest()})
    def test07_3000_identical_50_prefixes_passes_syntax_only(self):
        keys={f"{s:02d}{c:03d}".encode() for s in range(1,51) for c in range(1,61)}
        result,decision=q.summarize(keys,keys,{"invalid_rows":0,"duplicate_rows":0},
            {"invalid_rows":0,"duplicate_rows":0})
        self.assertEqual(len(keys),3000)
        self.assertEqual(decision,q.HOLD_SUPPORT) # 2024 is not frozen 3222
        self.assertFalse("boundary_equivalence" in json.dumps(result))
    def test08_exact_3222_threshold_with_50_prefixes(self):
        keys={f"{s:02d}{c:03d}".encode() for s in range(1,51) for c in range(1,65)}
        keys|={b"51065",b"51066",b"51067",b"51068",b"51069",b"51070",b"51071",b"51072",b"51073",b"51074",b"51075",b"51076",b"51077",b"51078",b"51079",b"51080",b"51081",b"51082",b"51083",b"51084",b"51085",b"51086"}
        self.assertEqual(len(keys),3222)
        metrics,decision=q.summarize(keys,keys,{"invalid_rows":0,"duplicate_rows":0},
            {"invalid_rows":0,"duplicate_rows":0})
        self.assertEqual(decision,q.PASS)
        self.assertEqual(metrics["distinct_geoid_overlap"],3222)
    def test09_semantic_not_outcome_even_if_overlap_full(self):
        keys={b"01001"}
        metrics,_=q.summarize(keys,keys,{"invalid_rows":0,"duplicate_rows":0},
            {"invalid_rows":0,"duplicate_rows":0})
        self.assertNotIn("individual_geoids",metrics)
        self.assertNotIn("01001",json.dumps(metrics))
    def test10_invalid_rows_prevent_pass(self):
        keys={f"{s:02d}{c:03d}".encode() for s in range(1,51) for c in range(1,65)}
        keys|={f"51{c:03d}".encode() for c in range(65,87)}
        _,decision=q.summarize(keys,keys,{"invalid_rows":1,"duplicate_rows":0},
            {"invalid_rows":0,"duplicate_rows":0})
        self.assertEqual(decision,q.HOLD_SUPPORT)
    def test11_one_synthetic_success_produces_aggregate_only(self):
        names=list(q.SOURCES)
        a,n1=fixture([b"01001"],names[0]);b,n2=fixture([b"01001"],names[1])
        blobs={names[0]:a,names[1]:b}; length={names[0]:n1,names[1]:n2}
        specs_fixed=specs(blobs,length)
        def fake_fetch(name):
            raw=blobs[name]
            return raw,{"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}
        with TemporaryDirectory() as d:
            dest=Path(d)/"evidence/attempt-01.json"
            with mock.patch.object(q,"verify_context"),mock.patch.dict(q.SOURCES,specs_fixed):
                receipt=q.run(fetch=fake_fetch,out=dest)
            self.assertEqual(receipt["disposition"],q.HOLD_SUPPORT)
            self.assertTrue(receipt["raw_original_shas_verified"])
            self.assertNotIn("01001",dest.read_text())
            self.assertNotIn("SECRET_COUNTY",dest.read_text())
            with self.assertRaises(RuntimeError):q.run(fetch=fake_fetch,out=dest)
    def test12_synthetic_network_error_yields_redacted_hold(self):
        with TemporaryDirectory() as d:
            dest=Path(d)/"evidence/attempt-01.json"
            with mock.patch.object(q,"verify_context"):
                def fail(name):raise ValueError("SECRET_COUNTY_01001")
                receipt=q.run(fetch=fail,out=dest)
            self.assertEqual(receipt["disposition"],"HOLD_Q08_SOURCE_ACCESS_OR_SCHEMA")
            self.assertNotIn("SECRET_COUNTY",dest.read_text())
            self.assertFalse(receipt["science_f01_authorized"])

if __name__=="__main__":unittest.main()
