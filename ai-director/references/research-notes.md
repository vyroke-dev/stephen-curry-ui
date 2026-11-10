# Research Notes and Evidence Map

Research baseline: **2026-11-11**. Sources below are public. The production behavior in this package is an original synthesis, **not** an assertion about Higgsfield's private source code or hidden prompts.

## Official evidence

1. **Cinema Studio 4.0 Complete Guide** (Higgsfield, published Oct 27, 2026): https://higgsfield.ai/blog/cinema-studio-4-0-complete-guide  
   Documents genre, era, tempo, camera, lens, aperture, movement, emotion, color, lighting, references, up to 30 seconds and 1080p **for Cinema Studio 4.0**. Those limits must not be assumed for every API model.
2. **Meet Cinema Studio 4.0** (Higgsfield, published Aug 12, 2026): https://higgsfield.ai/blog/cinema-studio-4-0  
   Discusses evolution from 3.5, tempo, optical looks, references, creative control, collaboration.
3. **How to Use Supercomputer** (Higgsfield, published Aug 1, 2026): https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-supercomputer  
   Confirms chat-based multi-step planning, multiple generative model routing, revisions, connectors and skills. Does **not** say it always uses Claude; multiple LLM families may be selected.
4. **Official API introduction and lifecycle**: https://docs.higgsfield.ai/docs/how-to/introduction  
   Confirms official API base URL, authorization, status values and cancellation method. **Model-specific bodies require separate validation.**
5. **Video API pipeline and billing**: https://higgsfield.ai/blog/generate-ai-videos-higgsfield-api  
   Confirms asynchronous request pattern, separate website/API billing and output retention caveat. Prices are time-sensitive and deliberately not hardcoded in this Skill.
6. **Agent Skills overview / authoring practices** (Anthropic): https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview and https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices  
   Confirms required `SKILL.md`, YAML `name`/`description`, progressive disclosure, and recommended authoring checks.

## Independent third-party observation (lower confidence)

- TerraCode, Higgsfield review: https://terracode.hu/en/blog/higgsfield-ai-videogyartas  
  Describes a Claude-assisted “director” in older Cinema Studio-era workflows, with script → elements → shot prompts. Treat specific product identity and internals as **third-party descriptions**, not authenticated proprietary architecture.

## Confirmed vs designed

| Item | Status |
| --- | --- |
| Cinema Studio 4.0 exposes creative settings | Confirmed by official docs |
| Supercomputer chats, routes tasks among multiple models and allows adjustments | Confirmed by official docs |
| Higgsfield API uses asynchronous request lifecycle | Confirmed by official docs |
| AI Director uses our specific JSON schema, continuity checks or approval gates | **Our design**, not a Higgsfield claim |
| Every project can generate 30-second clips at 1080p | **Not established**; provider/model-specific |
| Direct API implementation with arbitrary model ID, prompt, duration, resolution | **Not verified**; discover schema live |
| User automatically has API quota when they have website subscription | **False** according to official docs |
| Rendered clips are high-quality or characters are consistent | **Not proven** until actual output QA |

## Study and design rationale

- Use a specialized director conversation layer to bridge vague creative intent and filmable camera directions.
- Preserve a visual bible/continuity ledger so repeated characters and objects have stable cross-shot constraints.
- Make generation model-agnostic: `project.json` owns narrative semantics, while adapters own provider payloads.
- Use validation and controlled revisions to reduce accidental drift and repeat spending.
- Keep the Skill lean and link deeper references, per Agent Skills progressive disclosure.
