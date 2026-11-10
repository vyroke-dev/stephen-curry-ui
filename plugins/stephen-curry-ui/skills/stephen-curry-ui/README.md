# Stephen Curry UI 4.1

An agent- and model-agnostic suite for distinctive website design and frontend engineering. It contains one master orchestrator and nine focused skills for research, brand, experience architecture, Design Systems, creative direction, assets and motion, implementation, visual QA, and evaluation.

The workflow scales from a focused fix to a complete website. It preserves whole-journey craft for substantial work while avoiding full research, three concepts, or a multi-agent jury when a task does not benefit from them.

## Install the complete suite

Install all ten folders together so the relative skill references resolve:

    git clone https://github.com/vyroke-dev/stephen-curry-ui.git
    mkdir -p ~/.codex/skills
    cp -R stephen-curry-ui/plugins/stephen-curry-ui/skills/stephen-curry-* ~/.codex/skills/

Use the host's documented skill directory if it differs. Refresh or restart the host if it does not discover newly installed skills. Plugin-aware hosts can use the marketplace manifests in this repository when supported.

Invoke the master with `$stephen-curry-ui`. Specialist skills can be used separately when their scope applies. Tool availability, approval behavior, and integrations depend on the active host.

## Package checks

From the installed or cloned `stephen-curry-ui` skill directory:

    python3 scripts/validate_package.py
    python3 support/tools/scui.py check-suite
    python3 -m unittest discover -s tests -v

The offline contracts require Python 3.11+; strict JSON Schema checks use `support/requirements-contracts.txt`. Some evidence scripts and tests have additional optional dependencies. Passing package checks does not prove host activation, visual quality, production readiness, or real-user outcomes.

See [中文使用指南](README.zh-CN.md), [research notes](RESEARCH.zh-CN.md), and [changelog](CHANGELOG.md).

This independent project is not affiliated with or endorsed by Stephen Curry.
