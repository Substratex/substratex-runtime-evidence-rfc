# RFC-0010 — Conformance Profiles and Test Requirements

**Status:** Draft  
**Target RES version:** 1.0

## Purpose

RES conformance is profile-based. An implementation MUST state exactly which profile and version it satisfies.

## Profiles

### RES-Core

Requires object identity, version distinguishability, support classes, missingness preservation, and baseline provenance semantics.

### RES-Formation

Includes RES-Core plus Source Qualification, Canonical Runtime, Current Evidence Run, deterministic-scope declarations, and source-to-canonical traceability.

### RES-Finding

Includes RES-Core plus Bounded Finding semantics, method/dependency disclosure, scope preservation, and challenge-state carriage.

### RES-Issuance

Includes RES-Formation and RES-Finding plus Runtime Evidence Record, Certified Runtime Evidence Record, Passport, Evidence Seal, and scoped issuance semantics.

### RES-Preservation

Includes RES-Core plus preservation envelope, disclosure/redaction state, challenge history, and round-trip requirements.

### RES-Full

Requires RES-Formation, RES-Finding, RES-Issuance, and RES-Preservation.

## Conformance dimensions

A conformance report MUST distinguish:

- `schema_conformance`
- `identity_conformance`
- `lineage_conformance`
- `missingness_conformance`
- `scope_conformance`
- `lifecycle_conformance`
- `issuance_conformance`
- `preservation_conformance`
- `egc_handoff_conformance` when claimed

## Minimum test families

Candidate RES 1.0 SHOULD include test families for:

1. source-to-canonical traceability;
2. canonical identity repeatability within declared deterministic scope;
3. version separation after source/method/configuration change;
4. missingness differentiation;
5. support-class non-promotion;
6. bounded-finding dependency completeness;
7. scope non-broadening;
8. challenge and supersession retention;
9. scoped Passport/Seal issuance;
10. export/re-import round trip;
11. redaction disclosure; and
12. malformed or cross-run reference rejection.

## Conformance is not certification

Passing RES conformance tests establishes conformance to the tested specification profile. It does not establish truth, safety, authenticity, regulatory approval, scientific validity, or SubstrateX certification.
