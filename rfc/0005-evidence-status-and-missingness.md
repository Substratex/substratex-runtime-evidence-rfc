# RFC-0005 — Evidence Status, Support Classes, and Missingness

**Status:** Draft  
**Target RES version:** 1.0

## Purpose

This RFC separates the relationship of evidence material to its source and method from claim authority, validation state, and presentation status.

## Support classes

The normative support classes are:

- `source_observed` — directly located, parsed, counted, or recorded from qualified source material;
- `computed` — produced by a declared computation over eligible evidence without adding interpretive meaning beyond the defined computation;
- `derived` — produced through a declared derivation from evidence or admitted parent objects;
- `proxy` — a bounded indicator standing in for a construct that is not directly observed;
- `interpretive` — an interpretation over evidence under a declared method or ontology;
- `experimental` — a research-stage measurement or interpretation whose validation status is explicitly limited.

A support class describes **what kind of relationship an object has to evidence**. It does not by itself determine truth, validity, admissibility, or publication authority.

## Evidence status

Objects MAY additionally carry lifecycle/evaluation status such as:

- `active`
- `candidate`
- `confirmed`
- `conditional`
- `disputed`
- `superseded`
- `withdrawn`
- `not_applicable`

Status vocabularies used by a domain MUST define their transition rules.

## Missingness

The normative missingness vocabulary is:

- `not_supplied`
- `not_observed`
- `unavailable`
- `not_eligible`
- `not_computable`
- `withheld`
- `partial`
- `conflicting`

### Missingness preservation rule

A missingness value MUST NOT be silently rendered or exported as:

- numeric zero;
- boolean false;
- normal state;
- absence of an event;
- confirmed negative;
- successful computation; or
- direct observation.

A zero is a measurement. `not_computable` is an evidence relationship. They are not interchangeable.

## Authority separation

RES MAY carry authority metadata for interoperability, but it does not define a universal support-class-to-authority ordering. A proxy may be fully authorized **as a proxy**. A source-observed value may still be irrelevant, misleading, incomplete, or inadmissible for a particular claim.
