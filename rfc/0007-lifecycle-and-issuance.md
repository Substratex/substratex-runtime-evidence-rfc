# RFC-0007 — Evidence Lifecycle Objects and Issuance

**Status:** Draft  
**Target RES version:** 1.0

## Purpose

This RFC defines the canonical lifecycle object roles used by RES. Implementations MAY combine these roles internally, but exports claiming the corresponding RES object type MUST satisfy the role's normative requirements.

## Current Evidence Run (CER)

The active evidence authority during formation. A CER binds source qualification, canonical runtime, governing versions, evidence-bearing computations, missingness, lineage, and current status.

A CER is mutable only through declared lifecycle operations and MUST retain version distinguishability.

## Runtime Evidence Record (RER)

A structured machine-readable snapshot of governed evidence state. It MAY include observations, computations, bounded findings, markers, statuses, lineage, and review metadata.

An RER does not by itself establish issuance, truth, authenticity, or scientific validity.

## Certified Runtime Evidence Record (CRER)

An RER that has passed a declared RES issuance profile and whose issuance conditions are recorded.

`certified` in this context means **certified to the declared conformance and integrity scope**. It MUST NOT be represented as certifying source truth, causal correctness, safety, legal sufficiency, or universal scientific validity.

## Runtime Evidence Passport

A portable identity and disclosure envelope for an issued evidence record.

A Passport MUST identify:

- passport identifier;
- CRER/evidence record identifier;
- run identifier;
- canonical runtime identifier;
- source qualification reference;
- governing version manifest;
- issuance profile and result;
- evidence/integrity references;
- disclosure/redaction state;
- claim-boundary or scope summary;
- explicit non-certifications; and
- issuance timestamp or event identity where applicable.

## Evidence Seal

An Evidence Seal is an integrity reference over a declared evidence-bearing scope. It MUST identify:

- seal identifier;
- covered object(s);
- digest algorithm;
- digest value;
- exact scope declaration; and
- creation/version conditions.

A Seal MUST NOT be represented as proving the truth or authenticity of every covered upstream observation.

## Preservation Artifact

A Preservation Artifact carries an authorized representation of Runtime Evidence beyond the active system. It MUST preserve or explicitly disclose the loss of identity, lineage, status, missingness, boundaries, review state, and redaction/disclosure state.
