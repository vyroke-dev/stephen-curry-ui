# 4.2 Verification scope

- Package contains 10 standalone Skills, four role-specific reviewer configs, image-only board and concept manifests, a static evidence checker, and legacy post-implementation QA utilities.
- No Canvas integration or API key is bundled.
- Offline tests check static structure, actual image bytes/signatures, evidence files and fail-closed scenarios.
- Offline tests cannot authenticate generator provenance, validate image aesthetics, confirm user approval, run four independent model agents or test live browser sessions.
- Codex's built-in image generation availability must be discovered in the user's host; a logged-in account does not imply an exposed image tool.
