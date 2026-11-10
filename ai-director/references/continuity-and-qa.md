# Continuity Bible and Evidence-Based QA

## Reference hierarchy

1. User-approved reference image/video or supplied script/brand guide (highest priority).
2. User-approved asset bible in `project.json`.
3. User's latest explicit revision for the affected shots.
4. Director defaults (lowest priority; never override locked details).

Track an `asset_id`, `kind`, `description`, `locked_traits`, `reference_uris` for each asset. A description is not proof of generation; empty `reference_uris` means no actual reference media is present. External handles are provider-specific and must be mapped at render time.

## Continuity ledger

For recurring character: face and hair, garment colors, footwear, held objects and hands, emotional state, spatial placement, action start/end, dialogue and voice. For props: identity, placement, orientation, condition. For locations: topology, windows/doors, weather, time, motivated light, camera axis. For sound: ambience, continuity bridges, speech location.

Use each shot's `continuity.entry` and `continuity.exit` as short state descriptions. A cut may transform the state, but document an intentional transition or time jump. `screen_direction` is `left-to-right`, `right-to-left`, `stationary`, or `unspecified`. Use `stationary` for a static subject, not for a moving character whose direction is unknown.

## Review rubric

| Class | Example | Required action |
| --- | --- | --- |
| Blocker | wrong identity or product claims, unauthorized asset, no video, broken key moment | Stop publish / fix and verify |
| Major | action continuity break, impossible camera route, face drift, unusable audio, unreadable CTA | Repair targeted shot(s), rerender if approved |
| Minor | slight exposure fluctuation, inconsequential background artifact | Note or repair based on budget |
| Subjective | alternative framing or pacing with valid artistic rationale | Compare options; do not force consensus |

### Pre-render QA (plan evidence)

- The shot has one primary visual event, a purpose, and a readable start/end.
- Asset IDs resolve; named character traits match bible.
- Durations add up, and cut patterns match intended tempo.
- Prompts give positive actions, source of light and realistic movement; no prompt conflict.
- User is aware of any real cost, rights issue, and model limitations.

### Post-render QA (actual pixels/audio)

- Inspect every generated output or note if the footage could not be opened.
- Identify shot ID/timecode, symptom and evidence, not unsupported confidence scores.
- Review identity and garments across all visible shots, key prop state, continuity, screen geography, facial consistency, lighting, text/label clarity, motion artifacts, audio sync, resolution and crop.
- Return a minimal repair proposal preserving successful shots. Record actual tool result, `request_id`, output URI and review status.
- Automated structure checks cannot establish visual quality; user testing cannot be claimed if not conducted.

## Safe revision discipline

A user command such as “只把 SH02 改成缓慢推近” changes camera motion and, if necessary, the SH02 prompt. It does not implicitly change story, other shots, identities, or reference assets. If the new shot disrupts continuity, flag the dependency and propose the smallest coordinated adjustment. Preserve pre-change data or an explicit diff.
