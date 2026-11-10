# Independent creative jury: review the work that shipped

For a major or high-impact release, use an independent review when it can change the decision. Freeze the artifact and share rendered screenshots, observed interactions, viewport labels, and technical measurements. Keep the first visual review blind to internal concepts and the builder's rationale where practical.

The local `scripts/blind_jury.py` creates a private, de-identified file-named packet from browser audit evidence. It does not call reviewers or upload the packet. Screenshots can still contain client or customer information; store and share them only with proper authorization.

## Review lenses

- Art direction: visual identity, composition, typography, and the quality of the full journey.
- Motion and creative technology: transitions, interaction response, runtime cost, and fallbacks.
- UX and accessibility: task clarity, keyboard/focus/touch, motion preferences, media controls, and forms.
- Performance and engineering: measured loading, asset weight, errors, security, source correctness, and responsive behavior.

These are concerns, not proof of independent reviewers. Use four real separate agents only when the project requires that jury; otherwise label a single-agent or sequential role review accurately.

## Findings

1. Inspect the states and routes relevant to scope; a hero alone cannot establish whole-site quality.
2. Provide precise evidence, reproduction steps, severity, audience impact, rationale, and confidence.
3. Separate subjective art direction from factual accessibility and engineering checks. Do not claim awards certification or real-user validation from an agent review.
4. Fix high-impact root causes, retest affected states, and preserve unresolved limitations.
5. Still screenshots cannot establish motion or interaction. Mark those claims unverified until actual playback or browser observation.

See [whole-experience QA](whole-experience-qa.md) for a full-site evidence matrix.
