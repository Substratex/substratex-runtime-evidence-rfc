# RFC-0012 — JSON Interchange Profile

**Status:** Draft  
**Target RES version:** 1.0

## Purpose

This RFC defines the initial JSON interchange profile for RES objects.

## Encoding

JSON representations MUST be valid UTF-8 JSON and SHOULD validate against the corresponding JSON Schema 2020-12 schema published in `schemas/1.0-draft/`.

## Common envelope

All top-level RES JSON objects MUST include:

- `res_version`;
- `object_type`;
- `id`;
- `version`;
- `created_at` or a declared creation-event reference where wall-clock time is unavailable; and
- `provenance` or a provenance reference when the object participates in an evidence chain.

## Identifiers

Identifiers MUST be stable within the declared evidence lifecycle. Global uniqueness is RECOMMENDED for exported artifacts.

The provisional RES namespace is:

`urn:substratex:res:1.0:`

Implementations MAY use URIs, UUIDs, content-addressed identifiers, or other stable identifier schemes, provided identity semantics are declared and round-trip preservation is possible.

## Extension fields

Implementations MAY add namespaced extension fields. Extensions MUST NOT redefine core RES fields or silently change their semantics.

## Unknown extensions

A conforming consumer SHOULD preserve unknown extension fields during round-trip operations unless it explicitly declares lossy transformation.
