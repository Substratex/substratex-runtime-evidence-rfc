#!/usr/bin/env python3
"""Validate RES 1.0 RFC example objects against the draft JSON Schemas."""

from __future__ import annotations

import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas" / "1.0-draft"
EXAMPLES = ROOT / "examples"

MAPPING = {
    "01-qualified-source.json": "urn:substratex:res:1.0:schema:qualified-source",
    "02-canonical-runtime.json": "urn:substratex:res:1.0:schema:canonical-runtime",
    "03-current-evidence-run.json": "urn:substratex:res:1.0:schema:current-evidence-run",
    "04-runtime-evidence-record.json": "urn:substratex:res:1.0:schema:runtime-evidence-record",
    "05-bounded-finding.json": "urn:substratex:res:1.0:schema:bounded-finding",
    "06-certified-runtime-evidence-record.json": "urn:substratex:res:1.0:schema:certified-runtime-evidence-record",
    "07-runtime-evidence-passport.json": "urn:substratex:res:1.0:schema:runtime-evidence-passport",
    "08-evidence-seal.json": "urn:substratex:res:1.0:schema:evidence-seal",
    "09-challenge.json": "urn:substratex:res:1.0:schema:challenge",
    "10-review.json": "urn:substratex:res:1.0:schema:review",
    "11-preservation-artifact.json": "urn:substratex:res:1.0:schema:preservation-artifact",
}


def main() -> int:
    store = {}
    for path in SCHEMAS.glob("*.json"):
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        store[schema["$id"]] = schema

    registry = Registry().with_resources(
        [(uri, Resource.from_contents(schema)) for uri, schema in store.items()]
    )

    failures = 0
    for filename, schema_id in MAPPING.items():
        schema = store[schema_id]
        instance = json.loads((EXAMPLES / filename).read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
        errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
        if errors:
            failures += 1
            print(f"FAIL {filename}")
            for error in errors:
                print(f"  - {error.message}")
        else:
            print(f"PASS {filename}")

    report_schema = store["urn:substratex:res:1.0:schema:conformance-report"]
    report = json.loads((ROOT / "conformance" / "conformance-report.example.json").read_text(encoding="utf-8"))
    report_errors = list(Draft202012Validator(report_schema, format_checker=FormatChecker()).iter_errors(report))
    if report_errors:
        failures += 1
        print("FAIL conformance-report.example.json")
        for error in report_errors:
            print(f"  - {error.message}")
    else:
        print("PASS conformance-report.example.json")

    print(f"\nRES RFC example validation: {'PASS' if failures == 0 else 'FAIL'}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
