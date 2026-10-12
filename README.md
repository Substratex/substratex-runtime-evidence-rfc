# Runtime Evidence Standard (RES) — Request for Comment

**An implementation-neutral specification for reconstructable, claim-bounded computational evidence**

> **Runtime evidence should remain identifiable, inspectable, bounded, challengeable, and preservable across its full lifecycle.**

The **Runtime Evidence Standard (RES)** defines a common evidence substrate for systems that reconstruct computational activity across runtime and need that evidence to survive computation, review, export, challenge, and preservation without silent semantic inflation.

This repository is the public **Request for Comment (RFC) track for RES 1.0**.

**Status:** `RFC Draft 1.0`  
**Target:** `Runtime Evidence Standard 1.0`  
**Namespace:** `urn:substratex:res:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®  
**Research and engineering lineage:** 2024–2026

RES is implementation-neutral. No product, observatory, instrument suite, interface, scientific model, or vendor implementation defines conformance by itself.

## Scope

RES standardizes the minimum evidence architecture required to form and preserve Runtime Evidence:

```text
qualified source
  -> canonical runtime
  -> current evidence run
  -> runtime evidence record
  -> bounded findings
  -> certified runtime evidence record
  -> runtime evidence passport + evidence seal
  -> preservation artifact
  -> challenge / revision / supersession without historical erasure
```

The standard defines:

1. **Source qualification** — identity, preservation or referenceability, adapter identity, transformation provenance, role/event mapping, completeness and missingness.
2. **Canonical runtime** — stable event identities, ordering, supported temporal coordinates, source-span relationships, version identity.
3. **Runtime Evidence identity** — run/evidence identifiers, canonical digests, governing versions, provenance graph, deterministic scope.
4. **Evidence status** — source-observed, computed, derived, proxy, interpretive, experimental.
5. **Missingness** — not supplied, not observed, unavailable, not eligible, not computable, withheld, partial, conflicting.
6. **Bounded findings** — evidence dependencies, method identity, support class, scope, status, claim-boundary reference, challenge state.
7. **Lifecycle objects** — Current Evidence Run, Runtime Evidence Record, Certified Runtime Evidence Record, Runtime Evidence Passport, Evidence Seal, Preservation Artifact.
8. **Challenge and revision** — challenge, counterevidence, review, supersession, history retention.
9. **Preservation and interchange** — identifiers, schemas, provenance, integrity references, disclosure/redaction state, export/re-import fidelity.
10. **Conformance** — schema, identity, lineage, missingness, lifecycle, issuance, preservation, and EGC handoff conformance.

## What RES does not standardize

RES does **not** require or define a particular:

- AI model, agent architecture, benchmark, or provider;
- scientific theory of computational behavior;
- instrument suite or metric catalogue;
- user interface, dashboard, observatory, or workflow;
- causal model or root-cause method;
- safety, legal, regulatory, or truth certification system;
- cryptographic trust root; or
- claim-admission engine.

A conforming system may implement any of those separately, provided its Runtime Evidence objects satisfy the applicable RES profile.

## RES and Evidence-Governed Computation™

RES and EGC are complementary but distinct.

```text
RES defines:
  evidence identity
  source relationship
  support class
  method relationship
  missingness
  scope
  lineage
  challenge state
  preservation

EGC defines:
  claim admissibility
  authority policy
  bounded projection
  surface binding
  egress closure
```

A Runtime Evidence artifact can exist without EGC. An EGC-aware implementation can consume RES objects as evidence inputs. RES therefore defines the metadata required for an evidence-to-claim handoff without making EGC conformance a prerequisite for basic RES object conformance.

## RFC set

| RFC | Title | Status |
| --- | --- | --- |
| RFC-0000 | RES RFC Process and Status Model | Draft |
| RFC-0001 | RES Core Architecture and Invariants | Draft |
| RFC-0002 | Source Qualification | Draft |
| RFC-0003 | Canonical Runtime | Draft |
| RFC-0004 | Runtime Evidence Identity and Provenance | Draft |
| RFC-0005 | Evidence Status, Support Classes, and Missingness | Draft |
| RFC-0006 | Bounded Findings | Draft |
| RFC-0007 | Evidence Lifecycle Objects and Issuance | Draft |
| RFC-0008 | Challenge, Counterevidence, Review, and Supersession | Draft |
| RFC-0009 | Preservation and Interchange | Draft |
| RFC-0010 | Conformance Profiles and Test Requirements | Draft |
| RFC-0011 | RES / EGC Handoff Boundary | Draft |
| RFC-0012 | JSON Interchange Profile | Draft |

## Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, and **MAY** indicate normative requirements when written in uppercase.

## Core principle

**Missing evidence is not a negative finding.**

A system MUST preserve absence, ineligibility, conflict, withholding, and non-computability as evidence states. It MUST NOT silently convert those states into zero, false, normal, absent-event, confirmed-negative, or any stronger evidentiary proposition.

## Licensing and provenance

This repository uses the same split-license model as SubstrateX EGC Web™:

- executable software, validators, tests, and developer tooling: **PolyForm Perimeter License 1.0.1**;
- specifications and documentation: **CC BY-SA 4.0**;
- SubstrateX®, Runtime Evidence Standard (RES), Runtime Evidence™, Evidence-Governed Computation™, certification language, and related marks: reserved.

See [`LICENSE.md`](./LICENSE.md), [`NOTICE.md`](./NOTICE.md), and [`TRADEMARK_POLICY.md`](./TRADEMARK_POLICY.md).

Copyright © 2026 Arjay Asadi. All rights reserved except as expressly licensed.
