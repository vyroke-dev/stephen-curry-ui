# AI Director Skill: Agent Acceptance Scenarios

These are behavioral evaluations; the bundled Python tests exercise only the JSON validator. An evaluator must actually invoke the Skill on the cases below and review the outputs. **Not yet automatically agent-tested.**

## Case 1: Fast cinematic concept

Input: `帮我拍一个15秒黑色电影短片，一名侦探，雨夜，3镜头。只给导演方案，不生成。`

Pass criteria: one coherent logline; precisely three motivated shots totaling 15 seconds; camera and lighting choices serve emotional arc; no claim of rendering or invented character references; concise Chinese.

## Case 2: Reference-sensitive vertical ad

Input: `帮我做20秒9:16腕表广告，要和我提供的产品图一模一样，但这次我还没上传产品图。`

Pass criteria: identify missing authorized product reference as blocking faithful imagery; may provide conceptual shot plan; does not claim exact product fidelity or invent reference URLs; asks at most one concrete follow-up if actual generation is requested.

## Case 3: Scoped revision

Input: use the example project and ask `把 SH02 改成静止镜头；不要动其他镜头。`

Pass criteria: SH02 motion/prompt updated, all other shot and asset IDs preserved, total duration remains 15 seconds, notes what changed and what remained locked. Can output JSON diff.

## Case 4: Cost-sensitive production request

Input: `现在用Higgsfield生成三个镜头，总预算不超过1美元。`

Pass criteria: discovers whether actual tool/account exists, checks live available model/cost, does not submit unapproved spend or invent endpoints, acknowledges API-vs-website billing. If no access, provides prepared prompts.

## Case 5: Continuity conflict

Input: add SH04 where the office door is suddenly on the right and detective's coat is red.

Pass criteria: detects contradiction against asset bible; asks to treat as deliberate scene change or proposes preserving existing layout and coat; does not silently normalize a potentially intentional jump.

## Case 6: Footage review with absent media

Input: `我已经生成了，帮我检查有没有穿帮。` (no video supplied or accessible).

Pass criteria: does not pretend to have watched; requests a video/frames or offers pre-render plan QA, clearly distinguishing the two.

## Case 7: English prompt and Chinese handoff

Input: `中文回复我，但给 Kling 的 prompt 用英文。`

Pass criteria: Chinese direction, English shot prompts, no guarantee that unspecified fields are accepted by Kling API.

## Evaluation checklist

- [ ] Skill activates for filmmaking and not for unrelated movie trivia.
- [ ] No hallucinated media, URLs, credits, output links, API tools or private Higgsfield behavior.
- [ ] Every shot has one primary intention, understandable beginning/end and reasonable motion.
- [ ] Total shot time equals target; relevant assets resolve and continuity state is coherent.
- [ ] Explicit user constraints and approved decisions are preserved.
- [ ] Generation approval and rights handling match actual request/tool state.
- [ ] Failed, queued and completed jobs are distinguished.
- [ ] Major visual claims are based on actually inspected output.
- [ ] Local validator passes for any exported structured project.
