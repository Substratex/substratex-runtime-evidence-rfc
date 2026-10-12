# RFC-0006 — Bounded Findings

**Status:** Draft  
**Target RES version:** 1.0

## Purpose

A Bounded Finding is a versioned evidence-bearing output produced from a Runtime Evidence Record under a declared method and limited to a declared scope.

A Bounded Finding is not required to be a scientific instrument output. It can represent a measurement, classification, detected condition, reconstruction result, or other evidence-bound result.

## Required fields

A Bounded Finding MUST include:

- `finding_id`;
- `evidence_record_id`;
- evidence dependency references;
- `method_id` and `method_version`;
- `support_class`;
- `scope`;
- `status`;
- `claim_boundary_ref` or equivalent declared limitation object;
- missingness/uncertainty disclosures when applicable;
- challenge/review state;
- derivation/provenance relations; and
- version identity.

## Scope

Scope SHOULD be decomposable into relevant dimensions such as:

- temporal scope;
- operational scope;
- population or cohort scope;
- source scope;
- audience/disclosure scope where relevant.

A downstream representation MUST NOT silently broaden a finding beyond its declared scope.

## Claim-boundary reference

RES does not require a claim-admission engine, but every finding intended for authoritative downstream use MUST expose a machine-readable or stably addressable boundary describing what the finding does and does not support.

## Dependency disclosure

Agreement among findings sharing source fields, methods, or parent computations MUST NOT be represented as independent corroboration unless an explicit independence criterion is separately satisfied.
