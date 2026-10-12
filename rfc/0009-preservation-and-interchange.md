# RFC-0009 — Preservation and Interchange

**Status:** Draft  
**Target RES version:** 1.0

## Purpose

This RFC defines minimum requirements for moving Runtime Evidence across process, system, organizational, or temporal boundaries without silently losing the information needed to inspect its evidentiary state.

## Preservation envelope

A preservation envelope MUST preserve or securely reference:

- artifact identifier and version;
- source inventory/qualification references;
- canonical runtime identity;
- run and evidence record identities;
- bounded findings included in the artifact;
- governing contracts and versions;
- provenance relations;
- support classes and statuses;
- missingness, conflict, and not-computable states;
- challenge/review/supersession state;
- disclosure and redaction declarations;
- integrity references and their scopes; and
- replay or recomputation requirements where supported.

## Disclosure postures

An artifact SHOULD explicitly declare one of the following disclosure postures or a compatible extension:

- `metadata_only`
- `derived_evidence_only`
- `redacted_source`
- `complete_source`

Disclosure posture describes what material is present. It MUST NOT be used as a synonym for reproducibility or truth.

## Redaction

Redaction MAY protect confidentiality, privacy, security, or licensing restrictions. A redacted artifact MUST identify that redaction occurred and SHOULD identify which verification, replay, or challenge operations are no longer possible.

## Round-trip fidelity

An implementation claiming round-trip conformance MUST demonstrate that export followed by re-import preserves:

- stable identifiers or declared equivalence mappings;
- object type and version;
- status and support class;
- missingness;
- lineage;
- challenge/review state;
- integrity scope declarations; and
- explicit loss disclosures.
