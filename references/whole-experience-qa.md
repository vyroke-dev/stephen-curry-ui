# Whole-Experience Quality Assurance — six roles, every state

**No hero-only sign-off.** The QA unit is not a single screenshot. It is a **route × chapter × state × viewport × input mode** matrix, sampled intelligently but covering all critical journeys and major interactions.

## Required coverage dimensions

1. **Route:** home, project list, project detail, about, contact/checkout/signup, errors, any other critical route.
2. **Chapter:** opening (0–15%), early, middle (roughly 30–70%), final/reveal, footer; plus the transition between consecutive chapters.
3. **State:** idle, hover/focus, active/dragging/holding, completed, cancelled, loading, error, empty, back-navigation, replay/skip when applicable.
4. **Viewport:** desktop, narrow/mobile, tablet when layout warrants; portrait/landscape where world navigation changes; touch and keyboard.
5. **Mode:** standard visual, reduced-motion, audio muted, slow network/device and GPU-disabled/fallback when relevant.

Create an evidence trail, not thousands of redundant screenshots. Every meaningful chapter and critical user path must have *at least one verified state*. Confirm that transitions **between chapters** were tested, not only static snapshots at their endpoints.

## Six professional audit roles

| Role | Scope | Reject if... | Evidence |
| --- | --- | --- | --- |
| **Art Director** | Identity, originality, typography, art direction, editorial rhythm, section consistency, entire narrative composition | Hero dazzles but mid/ending are filler, clichés dominate, concept is inconsistent | Annotated full-page and sectional screenshots, comparison rationale |
| **Motion Director** | Temporal rhythm, gesture response, staging, transitions, scroll speed, animation curves, handoff between effects, sonic sync | Same reveal everywhere, incoherent cuts, dead transitions, effects fight each other | Interaction recording, timing states, interruption tests |
| **Creative Technologist** | Canvas/3D/shaders/video/audio, visual stability, asset/scene transitions, render resource lifecycle | Context loss, broken shader, blurry/aliased scene, nonresponsive pre-render masquerading as interaction | GPU/console output, device clips, effect fallbacks |
| **UX Auditor** | Navigation, interaction discoverability, state recovery, keyboard, screen reader basics, accessibility, tasks and CTA | Mandatory gate blocks users, unclear exit, dead CTA, focus trap, missing equivalent input | Task runs, keyboard path, reduced-motion, semantic checks |
| **Performance Engineer** | Startup, media costs, runtime frame pacing, shader compilation/upload, responsiveness, memory and network | Unexplained stalls, blocking video/assets, memory growth, layout shift, severe input lag | Trace/field CWV when available; test device and conditions |
| **Engineering Reviewer** | Real implementation, code correctness, state determinism, security, cleanup, routes, build/tests, asset rights | Failing core functionality, missing routes, broken code, false media/source claims | Build/test output, reproducible errors, code review |

**Implementation:** parallel reviewers only when independent tools/agents really exist. Otherwise run six disciplined **sequential** passes, checking against common evidence. A combined reviewer is not six independent opinions.

## High-signal critique checklist

- Does every section contribute a new idea? Is there a **weakest section** that should be redesigned or removed?
- Is there a coherent signature behavior running through the **whole site** rather than one hero trick?
- Are the mid-page transitions art-directed, or just scroll fades? Does the site arrive at a meaningful ending?
- Do visual and interactive effects respond on actual devices? Can each gesture be cancelled/reversed or bypassed appropriately?
- Can users complete key goals if they never notice the custom cursor or cannot use a gesture?
- Are audio and autoplay respectful of user preferences?
- Does the lowest-performance mode maintain content clarity and core interaction?
- Did code or asset shortcuts misrepresent real products/brands or break cross-page consistency?

## Severity and release decisions

Each finding has: `ID | role | route/section/state | viewport/input | steps | expected/actual | evidence | severity | fix | verification status`.

- `P0`: data loss, serious security/privacy flaw, core site inaccessible; **do not ship**.
- `P1`: blocked primary journey, major scene/route failure, severe crash/critical accessibility barrier; **do not ship**.
- `P2`: obvious mid-page visual mismatch, distracting motion, broken secondary interaction, performance regression; repair before flagship handoff if possible.
- `P3`: optional polish; decide by meaningful improvement.

Status: `PASS` = observed and meets criterion; `FAIL` = repro evidence; `BLOCKED` = cannot test, reason explicit; `N/A` = genuine inapplicability with reason. Never equate `BLOCKED` with `PASS`.

## Iteration loop

1. Run browser; collect screenshots for **top/middle/bottom and every critical chapter/state**, optional video/trace. Use `scripts/experience_audit.py` for repeatable initial coverage.
2. Critique **as an experience**, then six domains. Consolidate findings by root cause, not by screenshot count.
3. Fix critical/high-impact defects. Preserve approved art direction unless evidence shows it should change.
4. Re-run affected states and route transitions; retest mobile/reduced-motion and adjacent scenes.
5. Stop only when release gates pass or explicit blockers are reported. Avoid infinite cosmetic iteration without objective gain.

## Minimum evidence before claiming completion

- Actual website screenshots after load at opening, at least one middle section, and closing/footer, on desktop + mobile; full-page screenshots for editorial review when applicable.
- At least one **recorded or live-observed** execution for each signature interaction, including completion and interruption.
- Required key journeys and route transitions tested with real controls.
- Audio controls, reduced-motion and non-pointer alternative where relevant.
- Browser errors, network failures, test/build commands and device/performance conditions reported.
- A completed six-role status table with concrete evidence; no unsupported “100/100 Awwwards” claim.

Useful sources: https://playwright.dev/docs/test-snapshots ; https://playwright.dev/docs/trace-viewer ; https://developer.chrome.com/docs/devtools/performance
