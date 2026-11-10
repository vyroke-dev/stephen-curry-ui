# Stephen Curry UI 4.2 · Image-Only Design Skill

**Every visual design must be created with actual built-in image generation. No code-created design.**

This local, standalone Codex/OpenCodex skill enforces:

1. Research and verified user/project requirements.
2. **Seven genuine image-generated Design System visual boards** (brand, color, typography, layout, components, responsive, motion) with review and actual approval.
3. **Three distinct image-generated high-fidelity website concept sets**, desktop and mobile, with independent review and approval.
4. **Only then** Codex implements the approved visual designs in code, with accessible responsive behavior and actual browser QA.

HTML/CSS/React/SVG/Python/coded screenshots must **never** produce visual designs. Code is an implementation tool only after image approval. If the installed Codex host does not expose a callable built-in image generator, the skill **stops** and requests a user-visible handoff to a supported image tool; it never fabricates an image call or silently uses code.

The package includes **10 native Skills**, **4 role-specific reviewer configs**, offline evidence contract checkers and post-implementation QA scripts. Independent agents and real image tools depend on actual host capabilities; this repo cannot grant them.

## Install / upgrade

Download repository (or standalone ZIP), then run from its root:

```bash
python3 install.py --global --upgrade
```

To include project-local reviewer TOML and contracts:

```bash
python3 install.py --project /path/to/your/website --upgrade
```

The installer backs up recognized older Skill directories before replacement and does not overwrite unrelated files. Check installed Skill discovery in your actual Codex distribution.

## Marketplace/plugin

For compatible Codex plugin hosts:

```sh
codex plugin marketplace add vyroke-dev/stephen-curry-ui
```

Install **Stephen Curry UI** from the marketplace as supported by that host. Full bundled plugin content lives in [`plugins/stephen-curry-ui/`](plugins/stephen-curry-ui/); manifests are version **4.2.0**. For non-plugin Codex, use the native Skill install path above.

No separate API key or Canvas is required by this Skill. Your logged-in Codex account does not guarantee the image tool is available. Web/AI requests may use the host's normal network service.

[中文说明](README.zh-CN.md) · [安装说明](docs/INSTALLATION.zh-CN.md) · [变更记录](CHANGELOG.md)

*Independent project. Not affiliated with or endorsed by Stephen Curry.*
