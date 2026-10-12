# RFC-0000 — RES RFC Process and Status Model

**Status:** Draft  
**Target RES version:** 1.0  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®  
**Created:** 2026-10-12

## Summary

This RFC defines the process by which proposals enter, change, and leave the Runtime Evidence Standard RFC track.

## Normative status model

An RES RFC MUST have exactly one status: `draft`, `review`, `candidate`, `accepted`, `superseded`, or `withdrawn`.

An RFC MUST identify the RES version it targets. Accepted RFCs MUST remain addressable after supersession.

Normative behavior MUST NOT be silently changed by editorial revision. Semantic changes require a versioned RFC revision, erratum, or superseding RFC.

## Standards maturity

`accepted` means accepted into the SubstrateX RES specification process. It does not mean recognition by an external standards body, universal adoption, or third-party validation.

## Implementation evidence

A Candidate RFC SHOULD have mechanically testable conformance cases where its requirements permit mechanical testing. Core interchange semantics SHOULD be exercised by at least two independently developed implementations before a stable RES release.
