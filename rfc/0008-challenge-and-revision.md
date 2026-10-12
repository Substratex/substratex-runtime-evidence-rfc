# RFC-0008 — Challenge, Counterevidence, Review, and Supersession

**Status:** Draft  
**Target RES version:** 1.0

## Purpose

Runtime Evidence must remain contestable without allowing review to rewrite the historical record.

## Challenge

A Challenge MUST include:

- `challenge_id`;
- target object identifier;
- challenge type;
- reason;
- challenger identity or declared anonymous/system source where appropriate;
- creation time/event;
- optional counterevidence references;
- status; and
- provenance.

Minimum challenge types SHOULD include `source`, `identity`, `method`, `scope`, `status`, `finding`, `missingness`, `integrity`, and `preservation`.

## Counterevidence

Counterevidence MUST itself be identifiable evidence material. It MUST NOT acquire authority merely by being attached to a challenge.

## Review

A Review object MUST identify:

- the challenge(s) reviewed;
- reviewer identity/role;
- evidence considered;
- method or policy applied;
- outcome;
- reasoning/reference where disclosure permits; and
- version/time.

Minimum review outcomes are `upheld`, `rejected`, `partially_upheld`, `unresolved`, and `superseded`.

## Supersession

Supersession creates a new authoritative version or object relationship. It MUST NOT delete or mutate the historical object being superseded.

A supersession record MUST identify predecessor, successor, reason, effective time/version, and retained challenge history.

## Propagation

A preserved artifact or downstream system claiming current-state fidelity MUST carry or resolve the active challenge and supersession state applicable to its exported findings.
