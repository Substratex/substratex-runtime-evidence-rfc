# Runtime Evidence Standard — Threat Model

This document is non-normative unless incorporated by an RFC. It identifies failure modes that RES conformance work should test.

## Evidence-integrity threats

- **Source substitution** — a preserved artifact references a different source than the one used during formation.
- **Identity collision** — two materially different evidence formations reuse the same run, record, or canonical identity.
- **Digest ambiguity** — a hash is presented without declaring which bytes or object fields it covers.
- **Cross-run contamination** — a finding silently depends on evidence from another run without an explicit relation.
- **Version drift** — source, adapter, method, threshold, or policy changes without distinguishable version identity.

## Semantic threats

- **Missingness collapse** — unavailable or non-computable evidence becomes zero, false, normal, or confirmed-negative.
- **Support-class promotion** — proxy, interpretive, or experimental material is presented as source-observed or direct fact.
- **Scope inflation** — a local/interval finding becomes a whole-run, population, causal, or universal claim without a new evidentiary basis.
- **Ordering repair without disclosure** — ambiguous temporal ordering is silently rewritten.
- **Derived independence inflation** — correlated findings sharing a common evidence basis are represented as independent corroboration.

## Lifecycle threats

- **Premature issuance** — a Passport or certified record is issued before declared formation/conformance conditions are met.
- **Certification inflation** — RES issuance is described as truth, authenticity, scientific validity, safety, legal sufficiency, or regulatory approval.
- **Challenge loss** — disputed or superseded state disappears from current exports.
- **Destructive revision** — new evidence or review overwrites the historical object it supersedes.
- **Stale preservation** — an old artifact is presented as current without version/review status.

## Disclosure threats

- **Redaction inflation** — an artifact removes evidence required for challenge while preserving the appearance of full verification.
- **Partial bundle presented as complete** — disclosure posture is omitted or misleading.
- **Sensitive evidence leakage** — preservation or export exposes content beyond the declared audience/disclosure policy.

## Conformance threats

- **Schema-only conformance** — structurally valid objects violate semantic invariants.
- **Reference-implementation capture** — a product-specific topology becomes de facto mandatory despite not being normative.
- **Fixture overfitting** — an implementation passes published examples while violating untested invariants.

RES conformance should increasingly include adversarial cases for these failure modes as the RFC track matures.
