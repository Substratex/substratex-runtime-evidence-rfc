# RFC-0011 — RES / EGC Handoff Boundary

**Status:** Draft  
**Target RES version:** 1.0

## Purpose

This RFC prevents conflation of evidence formation with claim authorization.

## Division of responsibility

RES defines and carries:

- evidence identity;
- source relationship;
- support class;
- method relationship;
- missingness;
- scope;
- lineage;
- challenge/review state;
- integrity references; and
- preservation state.

Evidence-Governed Computation (EGC) may consume those properties to evaluate:

- claim admissibility;
- authority policy;
- bounded projection;
- surface binding; and
- egress closure.

## EGC handoff object

An RES object claiming EGC-handoff conformance MUST expose sufficient machine-readable metadata to construct an evidence input without reconstructing evidentiary semantics from presentation text.

At minimum the handoff MUST expose:

- evidence object identity;
- relevant source/canonical references;
- method identity;
- support class;
- scope;
- status;
- missingness/uncertainty state;
- lineage/dependencies;
- claim-boundary reference when present;
- challenge/review/supersession state; and
- version information.

## Independence

RES conformance MUST NOT require EGC conformance unless the implementation explicitly claims an EGC-integrated profile.

EGC conformance MUST NOT be inferred merely because an object is a conforming RES artifact.
