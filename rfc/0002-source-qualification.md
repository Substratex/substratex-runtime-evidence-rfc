# RFC-0002 — Source Qualification

**Status:** Draft  
**Target RES version:** 1.0

## Purpose

Source qualification establishes the first evidentiary boundary. It records what material was supplied, how it was identified, how it was interpreted structurally, and what limitations are already known before canonical formation.

## Qualified Source object

A Qualified Source MUST include:

- `source_id` — stable identifier within the evidence run;
- `source_type` — declared media/record type or adapter-facing type;
- `source_reference` or preserved source material;
- `adapter_id` and `adapter_version` when an adapter is used;
- `qualification_status`;
- `acquired_at` when acquisition time is relevant and available;
- `source_digest` when raw bytes or a stable canonical source representation are available;
- `transformation_provenance` for any pre-canonical transformation;
- role/event mapping declarations when roles or event types are normalized;
- completeness and coverage declarations where knowable; and
- explicit missingness, ambiguity, or conflicts discovered during qualification.

## Qualification status

The minimum status vocabulary is:

- `qualified`
- `qualified_with_limitations`
- `incomplete`
- `conflicting`
- `unsupported`
- `rejected`

`qualified` means the source is structurally eligible for the declared canonicalization contract. It MUST NOT imply that source assertions are true or complete.

## Transformation provenance

Any transformation performed before canonical runtime formation that can alter identity, ordering, role, timestamp, or content MUST be recorded with:

- transformation identifier;
- version;
- input reference;
- output reference;
- declared purpose; and
- loss or normalization disclosures.

## Role and event mapping

A source adapter MAY normalize roles and event classes. It MUST preserve enough provenance to distinguish source role, adapter role, canonical role, and operator correction where those differ.

## Failure rule

A source that cannot satisfy the declared adapter or qualification requirements MUST NOT be silently promoted to a qualified source. A system MAY preserve it as unsupported or incomplete evidence material.
