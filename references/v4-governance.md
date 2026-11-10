# Stephen Curry UI 4.1 governance

## Scope and gates

Use a focused path for contained fixes, a feature path for bounded journeys, and the full gates for new sites, broad redesigns, or work whose impact warrants them. Record only gates that affect the decision or release.

For a full experience, the sequence is: inspect; decision-relevant research; experience architecture; Brand DNA and Design System; approved design rules; concept selection; four independent reviewers; implementation; browser QA; release evidence. An existing approved Design System or user-selected direction can satisfy its respective gate with evidence. The full track still records a concept-selection decision and requires the four-role jury. A status field cannot.

Full-experience release evidence includes explicit checks for Design System approval, concept selection, the independent jury, browser verification, and accessibility review. The offline quality checker enforces these checks. Smaller scopes declare only the gates they actually need.

Track an applicable gate as `pending | passed | blocked | failed | waived`. A waiver must be explicitly authorized by the user and recorded with scope and reason. Critical accessibility, security, privacy, and core-journey failures are not waived. A blocked check blocks only decisions or release steps that depend on it.

## Approval

The assistant may make routine, reversible design and engineering choices within the user's brief. Ask before an unapproved consequential brand/system decision, material spend, external data sharing, destructive action, or scope expansion. A specific user message in the current conversation can approve a design artifact; a log records that consent but does not create it. Follow any additional approval enforced by the host or external service.

## Evidence and arbitration

Keep research evidence, user-supplied facts, assistant judgment, assumptions, and approved choices distinguishable. Use real browser output, test results, and cited references for objective claims. For subjective direction, explain the reasoning and relevant trade-offs. Do not fabricate benchmarks, usability studies, accessibility certification, or agent independence.

Critical objective defects override aesthetic scores. For high-impact work, resolve findings against reproducible evidence rather than simple votes. Preserve the last stable version, record the before/after evidence, and stop when repairs stall or regress.

## Retained material

The earlier whole-experience references and Python utilities remain useful craft and evidence tools. Apply their detailed procedures when the task warrants them; do not turn a focused maintenance task into a full-site release process.
