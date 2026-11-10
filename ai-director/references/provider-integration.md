# Provider Integration: truth-first contract

## Independent execution boundary

A Skill supplies direction, prompts and checks. Tools supply actual media generation. Without tools/API credentials, output a handoff; do not describe unseen clips as produced. Obtain the user's approval before paid generation when costs are not already authorized.

## Provider-independent job mapping

1. `project.json` and shot IDs are the source of truth for creative and narrative data.
2. Query provider tools/catalog at run time for supported `model_id`, dimensions, durations, cost and reference slots.
3. Compile each shot's semantic prompt and reference URIs into *that provider's* current schema. Track the mapping `shot_id → provider_job_id` and asset ref IDs.
4. Store each submitted job's request ID, status URL if supplied, model version, cost estimate/actual cost and outputs. Never put secrets in exported projects.
5. Poll only authenticated, provider-returned status URLs (or receive verified webhooks). Set finite retries, timeouts, explicit failure states; log the existing request ID before retrying submission.
6. Persist authorized outputs to permitted user storage and verify access; re-check output URLs rather than assuming indefinite retention.
7. Feed actual frames/video into QA. Rerender only impacted shots and only within authorized budgets.

## Higgsfield public API facts (verified on 2026-11-11)

- Official documentation: https://docs.higgsfield.ai/docs/how-to/introduction
- Base API URL in documentation: `https://platform.higgsfield.ai`
- Header format shown: `Authorization: Key {api_key}:{api_key_secret}`. Keep credentials server-side and out of logs.
- Submit: `POST https://platform.higgsfield.ai/{model_id}` with **model-dependent JSON body**.
- Poll: `GET https://platform.higgsfield.ai/requests/{request_id}/status`.
- Cancel pending queue item: `POST https://platform.higgsfield.ai/requests/{request_id}/cancel`; cancellation is documented for `queued`, not for `in_progress`.
- Observed/documented statuses: `queued`, `in_progress`, `nsfw`, `failed`, `completed`. A successful response may include `video.url` or `images[].url`.
- Official Higgsfield guide says API and web subscriptions have separate billing, asynchronous jobs use polling/webhooks, and outputs should be saved before expiration: https://higgsfield.ai/blog/generate-ai-videos-higgsfield-api

**Do not copy generic pseudo-code or sample schemas from an external article into production.** Current official API docs differ from some older examples circulating online (`api.higgsfield.ai` vs `platform.higgsfield.ai`, and `succeeded` vs `completed`). Verify individual model endpoint and request body using current model catalog documentation or a real tool definition. The project schema's `fps`, `duration_s`, `lens_mm`, `aperture_f` and reference IDs are planning metadata, **not presumed accepted API fields**.

## Cost gate

Show a price estimate only if an actual current model price is known; mark estimates conditional. Explain video regeneration increases spend. Website plan credits and API balances are distinct. Respect permissions and hard budget ceilings. Do not silently submit multiple expensive variants.

## Model routing guidelines (suggested design, not secret Higgsfield rules)

- Asset/still generation: quality and consistency of reference images first.
- Image-to-video: when exact appearance continuity matters and model supports input frames.
- Text-to-video: when appearance constraints are looser or no reference source is available.
- Audio/music: generate separately only when requested and rights/permissions allow.
- Multi-shot provider generation: use when supported and predictable; otherwise create separate clips and recommend editing/assembly.

## Failure handling

`not_available`: no compatible tool/model, provide prompts.  
`unverified_schema`: model docs missing, do not guess request shape.  
`over_budget`: stop before submission.  
`queued / in_progress`: report observed status, not result.  
`failed / nsfw`: report provider's outcome, avoid unjustified retries; no invented output.  
`completed`: verify media URI and ideally inspect before claiming visual quality.
