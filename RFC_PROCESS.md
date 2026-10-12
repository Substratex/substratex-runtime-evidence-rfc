# RES RFC Process

The Runtime Evidence Standard is developed through a public Request for Comment process.

The goal of the RFC track is not to treat publication as validation. It is to make the architecture inspectable early enough that implementers can identify ambiguity, contradictions, interoperability problems, and untestable requirements before a stable release.

## RFC statuses

- **Draft** — active proposal; breaking changes permitted.
- **Review** — normative shape is substantially complete; comments and implementation feedback requested.
- **Candidate** — intended semantics are frozen except for defects discovered by conformance or interoperability testing.
- **Accepted** — incorporated into a stable RES release.
- **Superseded** — replaced by a later RFC or stable specification.
- **Withdrawn** — removed from consideration while retained for history.

No RFC becomes an established standard merely because it appears in this repository.

## Required information

Every RFC MUST identify:

- RFC number and title;
- status;
- target RES version;
- authorship/origin;
- scope;
- normative requirements;
- non-goals;
- object or vocabulary changes;
- conformance implications;
- backward-compatibility implications where applicable;
- security/privacy or disclosure considerations where relevant;
- open questions; and
- change history.

## Acceptance threshold

A normative RFC SHOULD NOT move to Candidate unless:

1. its normative objects can be represented in the RES interchange model;
2. required failure states are explicit;
3. pass/fail conformance cases exist for each MUST-level requirement that is mechanically testable;
4. at least one implementation exercises the proposal; and
5. no unresolved contradiction exists with an Accepted or Candidate RFC.

A stable RES release SHOULD require at least two independently developed implementations for the core interchange and conformance semantics. Implementations sharing the same codebase or generated logic do not count as independent merely because they are packaged separately.

## Change control

Normative behavior MUST change through an RFC, erratum, or versioned specification update. Editorial corrections MAY be merged without a new RFC when they do not change semantics.

A change that alters object identity, missingness meaning, support-class semantics, conformance outcome, issuance conditions, or preservation requirements is normative.
