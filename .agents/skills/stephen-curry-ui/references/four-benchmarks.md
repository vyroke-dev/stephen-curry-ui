# Four user-selected benchmarks: deep structural research

Research snapshot: **2026-11-07**. Benchmarks are a **quality floor**, not permission to clone. Confidence tiers: `DIRECT TEXT` = website text extracted via search/web, `CREATOR TECHNICAL` = first-party engineering write-up, `THIRD-PARTY` = cited external analysis or award listing, `NOT LIVE-OBSERVED` = mouse/scroll behavior not reproduced in an interactive browser in this research environment. Do not invent the latter.

## 1. Son Daven — https://sondaven.com/en

**Observed via direct site text:** an investment-oriented resort experience unfolding through prologue, cultural/architectural concept, geographic context and neighboring attractions, wellness, food, activity, arts/family/traditions and investment action. The site's copy connects the mountain/Hutsul tradition narrative to a commercial investment outcome rather than a disconnected gallery. The presence of a “hold and move” prompt is directly shown in extracted page text; actual gesture timing/response is **NOT LIVE-OBSERVED**.

**Independent technical/award listing** reports WebGL, scrolling, GSAP, micro-interactions, storytelling and immersive 3D. These are metadata and editorial characterizations, not proof that this research browser reproduced them.

**Lesson:** build a continuous *meaningful story spine*, where each location/product/story section contributes to the next and supports a clear business goal. Study how content density rises and falls over the full length. Build meaningful transitions between narrative/culture -> product offering -> trust -> CTA.

**Don't copy:** the specific mountain mythology, hospitality photography, scene layouts, UI details, or investment claims. An immersive site must not hide material business information.

**Source:** https://sondaven.com/en ; https://globalwebdesignawards.com/sites/son-daven

## 2. Silencio — https://silencio.es/

**Observed via direct site text:** the studio sells services as “digital products,” with store/retail packaging language, barcode, product references, receipt-style information, “ingredients,” “purchased,” “click to scan,” and separate product chapters for branding, visual languages, interactive websites and communications. Its portfolio is a distinct browsing experience at https://portfolio.silencio.es with “Scroll & click to open project.”

**Secondary visual evidence** (CSS Winner imagery) shows an expressive oversized editorial composition and product-container motifs; audio/precise animations have not been independently played. Claims about scroll sound effects exist in external critiques but are **NOT LIVE-OBSERVED** here.

**Lesson:** design a **conceptual interaction metaphor**, not merely an aesthetic. Carry that metaphor through labels, objects, navigation, microcopy, interaction states and interior pages. The value comes from consistency and surprise, not random kinetic elements.

**Don't copy:** their barcode/receipt system or exact commercial look for unrelated brands. A metaphor must remain usable by screen-reader and keyboard visitors.

**Sources:** https://silencio.es/ ; https://portfolio.silencio.es/ ; https://www.csswinner.com/details/silencio-digital-products/17129

## 3. Why Zero — https://why.zero.university/

**Direct text limitation:** the site yielded almost no readable content to this research interface (`99`), therefore full direct runtime inspection is **BLOCKED**. Stronger evidence is available from the **creator/development team** in their July 17, 2026 Codrops postmortem.

**CREATOR TECHNICAL evidence:** a story divided into **six stages and five interactive gates**, including “draw a zero” to enter, press-and-hold glass shattering, movement through a tunnel and exploration of a navigable city. The team uses an internally coordinated virtual-progress signal to drive scene lifecycles, shader states, content overlays, sound and gestures. They describe optimizing more than 1GB of source 3D material into a delivered experience under 10MB, with adaptive quality, texture atlases, idle/prewarmed GPU uploads and tuned post-processing. Performance claims in that article are the team's measurements, not independently reproduced here.

**Lesson:** the truly advanced move is **architecture for continuity**. Screen-to-screen timing, gestures, effects, story logic and audio belong to one experience system with reliable state restoration and deterministic progress, not 12 unrelated GSAP snippets. Prototype the highest-risk gesture early; test on a budget device. A gate needs alternate access when needed.

**Don't copy:** mandatory draw/hold gates or custom virtual scroll by default. Those choices may create keyboard, accessibility and discoverability costs. Use only if the project's story earns the friction, with alternate paths.

**Sources:** https://why.zero.university/ ; https://tympanus.net/codrops/2026/07/17/zero-the-engineering-behind-a-defiant-interactive-narrative/ ; https://bunqlabs.com/studio

## 4. Unseen Studio — https://unseen.co/

**Observed via direct site text:** an entrance with an audio/no-audio option, `Drag to explore our world`, `Click & Hold`, sound toggle, a toggleable menu, an exploratory “world,” project filtering, work gallery, and a clear contact close. The site addresses sound consent explicitly rather than forcing audio. The linked Unseen World also repeats its exploratory navigation invitation.

**Independent historical awards/screenshots** document an immersive portfolio world, navigation contrasting a 3D environment with editorial menus, and floating project thumbnails; do not confuse historical screenshot design with the currently live variant.

**Lesson:** a studio site can use **spatial exploration as an information architecture**, not merely a decorative 3D object. It still requires obvious exits, filters, project navigation, contact routes, and non-gesture alternatives. Consider a short “learn how to explore” affordance and accessible list view.

**Don't copy:** exact spatial world, projects/artwork, icon motifs or patented behavior. Do not auto-play sound without meaningful opt-in.

**Sources:** https://unseen.co/ ; https://unseen.co/world/ ; https://www.awwwards.com/sites/unseen-studio

## Shared DNA of the four benchmarks

1. **The experience embodies the subject.** Nature/investment, purchasable design systems, learning-through-action, and a studio world. The thesis shapes both visual and interactive vocabulary.
2. **Motion carries meaning.** The user is not simply watching decorative entrances; navigation and story transformations are meaningful.
3. **Transitions are designed as scenes.** Sections form chapters with motivated connections; there is a designed beginning, middle and ending.
4. **A signature interaction is integrated into the architecture.** It cannot be added as an unrelated post-production widget.
5. **Craft is technical.** Synchronized sound, consistent progress, stable input response, preloaded effects, device-aware fallbacks, tested performance.
6. **Business/content remains visible.** Even an immersive showcase must help visitors learn, filter, navigate, contact, buy or apply.

## How Stephen Curry UI should exceed the baseline

- Create an **original** experience premise relevant to each new product, not the same look-and-feel remixed.
- Demand a cohesive **whole-site storyboard** with transitions and a real visitor journey, rather than three screenshots.
- Design a **live interaction proof** before the rest of the polished interface, including touch/keyboard/reduced-motion paths.
- Control **emotional pacing** and distinguish deliberate quiet moments from unfinished blank sections.
- Bake **mobile device and accessibility parity** into the intended experience, not into a low-quality fallback after desktop is finished.
- Reject effects that have no user-facing value, even if technically spectacular.

## Evidence caveat

The research stage confirmed sites and first-party technical notes, but **did not have a live interactive browser recording of the four sites**. All timing, gesture feel, direct before/after and exact mobile behavior require the user's current OpenCodex/browser environment to inspect afresh. This file is *not* a substitute for new per-project reference research.
