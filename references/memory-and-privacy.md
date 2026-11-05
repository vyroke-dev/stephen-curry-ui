# Design memory, verification and privacy

## Two-tier architecture

**Project-local, private by default**: store the creative brief, reference log, user decisions, design tokens, assets with rights, screenshots and QA records under `docs/stephen-curry-ui/<project-slug>/` when appropriate for the repository. Follow existing repo security/ignore rules; never commit credentials, customer records or copyrighted source materials without permission.

**Shared, carefully curated**: with user **consent**, place only verified, generalizable craft knowledge in a separately writable shared library such as `~/.agents/stephen-curry-ui/knowledge/`. This folder is illustrative; detect actual filesystem availability before writing, never assume sync or persistence. Do not automatically mix private client information into shared knowledge.

## Promotion rule

An entry qualifies for the shared library only if it is:

- **Verified** by a real observation, test or measured result, with date and scope.
- **Generalizable**: a portable technique/principle, not a client-specific brand system.
- **Private-data-free**: redact logos, strategy, proprietary code, private URLs, client identifiers, assets and secrets unless explicitly cleared.
- **Traceable**: public reference URL or local non-sensitive evidence path, conditions, known limitations and reuse guidance.
- **Non-prescriptive**: future projects still perform fresh reference research and independent art direction.

## Lifecycle

1. Save project notes after verified QA; include failures and rejected approaches, not only successes.
2. Propose reusable general lessons for optional promotion; default is local-only unless the user has already established explicit standing consent.
3. Avoid duplicate patterns; revise existing knowledge when reliable new evidence contradicts it, preserving a brief change note.
4. If the shared store cannot be written, report `BLOCKED` and do not claim memory was saved.
5. For private or client projects, respect their existing retention, access-control and isolation requirements; access to one project does not grant authorization to share its details elsewhere.

Use [learning entry template](../assets/learning-entry.template.md) only for evidence-backed lessons. Neither the skill nor the model "automatically learns" by existing: persistence must be implemented and verified.
