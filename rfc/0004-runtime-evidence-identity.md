# RFC-0004 — Runtime Evidence Identity and Provenance

**Status:** Draft  
**Target RES version:** 1.0

## Purpose

This RFC defines the identity and provenance information required to distinguish one governed evidence formation from another and to inspect how evidence-bearing objects relate.

## Current Evidence Run identity

A Current Evidence Run (CER) MUST contain:

- `run_id`;
- `canonical_runtime_id`;
- qualified source reference(s);
- governing contract/version manifest;
- deterministic-scope declaration;
- formation status;
- provenance graph or equivalent relation set;
- evidence status and missingness summary; and
- version identity.

## Runtime Evidence Record identity

A Runtime Evidence Record (RER) MUST contain:

- `evidence_record_id`;
- `run_id`;
- canonical runtime reference;
- evidence-bearing object inventory;
- bounded finding references;
- provenance/derivation relations;
- status and missingness state;
- governing version manifest; and
- integrity references over declared scopes where available.

## Provenance relations

RES defines the following minimum relation vocabulary:

- `supplied_as`
- `qualified_from`
- `canonicalized_from`
- `computed_from`
- `derived_from`
- `projected_from`
- `challenged_by`
- `countered_by`
- `reviewed_by`
- `superseded_by`
- `sealed_by`
- `preserved_as`
- `redacted_from`

Implementations MAY extend this vocabulary, but extension terms MUST NOT redefine the semantics of core relations.

## Digest semantics

A digest MUST identify its algorithm and exact declared scope. A digest without a scope declaration MUST NOT be treated as proof that all associated material is covered.

## Identity does not imply truth

Stable identity, provenance completeness, replayability, or digest agreement establish evidence continuity properties only. They do not establish that the original source was truthful, complete, authentic, unbiased, or scientifically valid.
