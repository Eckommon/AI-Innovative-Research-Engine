# US-WATERWAY-F01 Source Route Diagnostic

Outcome-blind diagnostic only. No delay or hydrology magnitudes were parsed.

## Current routes
- NDC_LOCKS: HTTP=ERROR final=`` bytes= error=`HTTPError: HTTP Error 403: Forbidden` signals={}
- CORPS_HOME: HTTP=200 final=`https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home` bytes=40593 error=`` signals={'annual_usage': True, 'average_delay': False, 'delay': True, 'processing_time': False, '2016': True, '2025': True, 'xlsx': False, 'csv': False, 'download': False, 'apex': True}
- ANNUAL_USAGE: HTTP=200 final=`https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home` bytes=40591 error=`` signals={'annual_usage': True, 'average_delay': False, 'delay': True, 'processing_time': False, '2016': True, '2025': True, 'xlsx': False, 'csv': False, 'download': False, 'apex': True}

## Digital Library search
- totalResults: 1
- known item 2958: {'status': 200, 'title': None, 'date': None, 'find': None, 'filename': '2959.xlsx', 'format': None, 'resource': None, 'type': None, 'fullrsEnabled': False}
- matched titles: Public lock reports: Public lock commodity, public lock unavailability, public lock usage, public lock report glossary

## National Lock Characteristics layer
- layer name: Lock
- feature count returned: 234
- non-null geometry count: 234
- metadata/query errors:  

This diagnostic is not a PASS/HOLD decision. It only resolves the current public source routes for the next bounded F01 step.

Incremental monetary cost: **0 USD**.
