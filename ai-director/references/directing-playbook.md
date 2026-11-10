# Cinematic Directing Playbook

Read when turning an idea into concrete visual storytelling. These are filmmaking principles, not claims that a generation model supports real lenses or camera hardware.

## Story-to-screen logic

1. Ask what the audience knows before the shot, learns in the shot, and feels after it.
2. Let the action drive framing. An establishing wide orients geography; a close-up pays attention; a cutaway can conceal or reveal information.
3. Stage blocking (where actor and camera move), eyelines, props and transitions before adding effects.
4. Design an emotional arc through visual contrast (stillness vs motion, distance vs intimacy, light vs absence).
5. Match pacing to story events: a 3-second shot cannot realistically show a lengthy series of independent actions.

## Useful vocabulary

| Choice | Purpose | Avoid |
| --- | --- | --- |
| Extreme wide / wide | Scale, location, loneliness, physical geography | Losing the principal action in small mobile formats |
| Medium | Dialogue, relationships, believable performance | Crowded composition with no dominant action |
| Close-up / insert | Thought, touch, product detail, revelation | Overusing shallow focus when a key prop must stay readable |
| Low / high angle | Subjective power or vulnerability | Arbitrary angles with no story purpose |
| Eye-level | Human perspective, neutrality, intimacy | Fake neutrality when blocking contradicts the beat |
| Locked-off | Tension, observation, calm | Static for no reason when spatial information is missing |
| Dolly in / push in | Rising attention, discovery | Using zoom as if it were an identical optical move |
| Lateral tracking | Discover geography, match a traveling subject | Violating screen direction inadvertently |
| Pan / tilt | Reveal or follow subject | Conflicting simultaneous movement requests |
| Handheld | Urgency, embodied perspective | Jitter that obscures faces or products |
| Orbit | Relationship, dramatic recontextualization | Unmotivated full orbit that breaks continuity |

## Lens and focus intents

- Wide focal lengths (roughly 18–35mm full-frame equivalent) emphasize geography, near/far depth and movement; beware distorted close faces.
- Normal (roughly 40–55mm) maintains balanced spatial perspective.
- Telephoto (roughly 75–135mm) isolates subjects and compresses apparent depth; useful for distance, secrecy, attention.
- Small `f` number is a shallow depth-of-field **intention**; large `f` number is deeper focus **intention**. Generation systems may interpret these as looks rather than physical calculations.
- “Anamorphic”, “35mm film”, “grain” or “halation” are style instructions unless the target provider exposes real controls. Do not promise exact optical simulation.
- Protect focus during critical actions, text, product labels and two-subject interactions.

## Lighting

Declare a motivated source (window, practical lamp, sun, streetlight), direction, contrast, softness and color temperature. Night scenes should have a believable source and readable key actions. Specify continuity of source direction between cuts. Prevent contradictory prompts (“pitch black” and “every detail brightly lit”).

## Geography, time and cutting

- Establish an axis of action and screen direction. In a chase, specify left-to-right movement and preserve it across cuts unless a crossing or repositioning shot earns the change.
- Use a clear screen map (door left, desk center, window right) for dialogue and action scenes.
- Match props, hand positions, wardrobe, wounds, weather, time of day and light direction between overlapping shots.
- Match-on-action means the exit state of shot N must be compatible with the entry state of shot N+1. Deliberate time jumps must be labeled.
- Sound can bridge a cut (J-cut/L-cut) without implying that a video model automatically mixes multitrack audio.

## Anti-patterns

- Empty “epic, cinematic, masterpiece, 8K” adjective chains.
- A single 5-second prompt containing 12 separate actions and three incompatible camera moves.
- Invented physical parameters without model support.
- Sudden face/wardrobe/prop changes across shots.
- Demanding an exact copyrighted film scene or exact imitation of a specific living artist's creative identity instead of describing transferable cinematic principles.
- Referring to uncreated `@character` handles as if they exist in a provider.
