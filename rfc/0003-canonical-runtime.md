# RFC-0003 — Canonical Runtime

**Status:** Draft  
**Target RES version:** 1.0

## Purpose

The Canonical Runtime provides an implementation-neutral, ordered representation of qualified computational activity from which Runtime Evidence can be formed.

## Canonical Runtime requirements

A Canonical Runtime MUST provide:

- `canonical_runtime_id`;
- `source_id` or source-set references;
- canonicalization contract identifier and version;
- stable canonical event/record identifiers;
- declared ordering semantics;
- supported temporal coordinate system(s);
- source-span or source-record relationships where available;
- role/event mapping provenance;
- declared exclusions and unresolved ambiguities; and
- a canonical digest over the evidence-bearing scope when deterministic hashing is supported.

## Canonical event

A canonical event MUST contain:

- `event_id`;
- `event_type`;
- `order_index` or equivalent ordering coordinate;
- source reference(s);
- role/actor reference when applicable;
- payload or payload reference;
- temporal coordinates when supplied or derived under a declared method; and
- status/missingness metadata when a field is unavailable or ambiguous.

## Ordering

Ordering MUST be explicit. A system MUST distinguish at minimum:

- source-declared order;
- canonical order;
- wall-clock timestamp when available;
- logical/symbolic coordinate when used; and
- unknown or conflicting order.

A canonicalizer MUST NOT fabricate a temporal coordinate solely to satisfy a schema requirement.

## Source-span relationship

Where a canonical event is derived from a bounded region of source material, the canonical representation SHOULD retain a source span, source record identifier, or equivalent locator sufficient for later inspection.

## Deterministic scope

A system claiming deterministic canonicalization MUST declare which inputs, versions, normalization rules, precision rules, and excluded volatile state participate in the deterministic identity.
