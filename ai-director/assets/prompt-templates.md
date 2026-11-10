# Reusable Prompt Templates

These are **semantic prompt templates** to adapt after inspecting the actual provider's model rules. Curly variables are placeholders; they are not vendor-supported SDK parameters.

## Treatment

`A {duration_s}-second {format} for {audience}. Protagonist/subject: {subject}. Desire: {goal}. Obstacle/tension: {conflict}. Emotional movement: {emotion_start} → {emotion_end}. Visual thesis: {visual_idea}. Final image: {final_image}. Constraints: {hard_constraints}.`

## Character / element reference still

`One consistent {character_or_object} reference image, {identity_traits}, {wardrobe_or_materials}, {key_props}, {neutral_pose_and_angle}, {controlled_light}, {plain_uncluttered_background}. Preserve proportions, texture and recognizable defining details; no extra objects, no text unless supplied.`

## Cinematic anchor frame

`{shot_size} framing of {subject_id} in {location_id}. Precise composition: {foreground_midground_background}. Moment: {single_story_action}. Motivated light from {light_source} {light_direction}; {palette}; {camera_angle} and {lens_intent}. Keep locked reference features {locked_traits}. Intended emotion: {emotion}.`

## Video shot (positive instructions first)

`SHOT {shot_id} ({duration_s}s). LOCATION/STATE: {location_and_time}; consistent with {asset_refs}. FRAME: {shot_size}, {composition}, {lens_intent}, {focus}. ACTION IN ORDER: (1) {start_pose}, (2) {single_clear_action}, (3) {end_pose}. CAMERA: {one_primary_move}, {direction_and_speed}; horizon {horizon_note}. LIGHT: {source_quality_direction}; COLOR: {palette}. PERFORMANCE: {emotion_and_specific_action}. AUDIO: {sound_request_or_none}. CONTINUITY: enter {entry}, exit {exit}; screen direction {screen_direction}. AVOID: {only_targeted_issues}.`

## Provider handoff

`Target capability: {text_to_video | image_to_video | reference_consistent_video}. Shot: {shot_id}. Requested output: {duration_s}s, {aspect_ratio}, {resolution} (only if model supports). Approved references: {reference_uris}. Project brief: {logline}. Shot-specific prompt: {shot_prompt}. Constraints and limitations: {locked_traits}; {supported_features}.`

## Video QA

`Review ACTUAL provided video evidence, not the intended prompt. For each finding return {timecode, shot_id, severity, observed_symptom, evidence, likely_cause, smallest_fix}. Check identity, wardrobe, prop state, screen direction, blocking, camera movement, lighting, color, legibility, duration, crop, artifacts and sound. Mark not_observed where evidence is absent. Never say passed if media cannot be inspected.`

## Refinement

`Preserve all approved project decisions and asset IDs. Change ONLY {changed_shot_ids} and explicit dependencies. Requested difference: {user_revision}. Recompute impacted timing and continuity. Return before/after and a version increment, noting any render cost. Do not silently generate media.`
