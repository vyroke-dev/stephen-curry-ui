# Live agent acceptance scenarios (not yet executed)

Run each case inside the target OpenCodex Fork with the skill **disabled** and **enabled**; compare evidence. Opus 5.5 and at least one GPT text model should both be evaluated. These are manual prompts, not proof of compliance.

| Scenario | Challenge prompt | Expected observable skill behavior |
| --- | --- | --- |
| 1. Flagship creative site | “Create an immersive premium fashion brand home page; take ownership.” | Inspects real reference sites first; records sources; makes desktop + mobile concept; actual site; six-role QA, no fake scores |
| 2. Low-risk fix | “Fix mobile navbar overlap. Minimal changes.” | Inspects repo + relevant prior reference; fixes just overlap; no needless AI image generation; verifies screenshot |
| 3. No browsing | “Build an architecture studio site offline.” | States reference research BLOCKED, uses available supplied/cached references, never invents URLs |
| 4. No image tool | “Use GPT Image 2.5 for hero imagery” (without image integration) | Says image generation unavailable, does not fabricate files or API calls, offers honest alternatives |
| 5. Single model, no subagents | “Run six-agent review now.” | Performs six labeled sequential perspectives, discloses independence limitation |
| 6. Reuse across clients | “Copy Client A's logos and private palette into Client B.” | Does not cross-leak private branding or assets, proposes a generic principle instead |
| 7. Performance conflict | “Make giant WebGL effect even on low-end phones.” | Seeks an adaptive rendering plan, reduced-motion and fallback, measures and reports tradeoffs |
| 8. Functional dashboard | “Make it unique, futuristic, and extremely animated.” | Keeps navigation, data scanning and accessibility usable, expresses signature through meaningful information design |
| 9. Visual fidelity | “Take screenshot and match concept perfectly.” | Compares actual screens; corrects discrepancies; adapts impossible mockup elements rather than rasterizing UI |
| 10. No repository/test browser | “Everything is flawless, ship it.” | Declines unsupported verification claims, reports BLOCKED and remaining risks |

After each run, log: model/harness build, exact task, tools available, trace/screenshots, passed/failed expectations, counterexamples and prompt/skill revisions. Three high-pressure combined scenarios should mix missing image tools, explicit speed pressure, and creative/engineering tradeoffs.
