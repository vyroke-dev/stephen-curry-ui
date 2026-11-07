# Stephen Curry UI — Creative Web Experience Skill

**Version 3.1.0 · Model-agnostic**

A reusable skill for premium whole-site experience design, from creative research and art direction through interaction, motion, WebGL, production engineering, and evidence-based QA. No default AI text model is required.

## Use with Codex / OpenCodex

Install the skill from this repository at `~/.agents/skills/stephen-curry-ui/` or your compatible agent's skill directory, preserving its references, templates, scripts and tests. The main entry is [SKILL.md](SKILL.md).

For plugin-aware Codex distributions:

```sh
codex plugin marketplace add vyroke-dev/stephen-curry-ui
```

Then install **Stephen Curry UI** from the marketplace if supported by your distribution. Capability support depends on the host.

## Optional Claude Code plugin

```sh
claude plugin marketplace add vyroke-dev/stephen-curry-ui
claude plugin install stephen-curry-ui@stephen-curry-marketplace
```

No Claude Code dependency is required. Model choice is determined by the host: GPT, Claude, Gemini, DeepSeek and other capable agents can use the same instructions.

See [中文使用指南](README.zh-CN.md), [研究报告](RESEARCH.zh-CN.md), and [changelog](CHANGELOG.md).

This is an independent project and is not affiliated with or endorsed by Stephen Curry.
