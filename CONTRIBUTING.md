# Contributing to the Runtime Evidence Standard RFC Track

Contributions are welcome as technical criticism, implementation reports, issue cases, interoperability proposals, schema changes, or full RFCs.

## Preferred contributions

Useful feedback includes:

- a MUST-level requirement that cannot be tested;
- an ambiguous evidence state;
- an implementation that would satisfy the text while violating the intended invariant;
- an important source or runtime representation the current schemas cannot express;
- a missing failure or refusal state;
- a round-trip preservation defect;
- incompatible interpretations of a support class or authority field;
- evidence that two nominally equivalent implementations produce incompatible identifiers or lifecycle states; and
- a proposal that reduces implementation coupling without weakening evidentiary guarantees.

## RFC proposals

New normative proposals should use `process/RFC_TEMPLATE.md`.

Do not bundle product-specific functionality into the RES core. A proposal that requires a particular instrument, scientific model, interface, metric, provider, or product should normally be expressed as an implementation profile rather than a core requirement.

## Attribution

By contributing documentation or specification text, you agree that accepted contributions will be distributed under the repository's documentation license. Contributions do not grant rights to SubstrateX trademarks or certification marks.
