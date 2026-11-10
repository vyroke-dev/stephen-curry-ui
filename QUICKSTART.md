# Stephen Curry UI 4.2 · Quickstart

1. Unzip locally and run `python3 install.py --global --upgrade`.
2. Restart Codex and verify `$stephen-curry-ui` is discoverable.
3. In a project, request: `$stephen-curry-ui 请先研究，再调用实际内置图像工具生成七张 Design System 视觉板，评审并让我批准；然后生成三套桌面/手机的高保真网页图片，评审获批后才允许写实现代码。禁止任何 code 生成设计。`
4. If no real built-in image generator is available, the design stage **stops**. Use an explicit image-generation handoff, not a code mockup.

No Canvas application or separate API key required by the Skill itself. Real image tool and independent agent availability depend on your installed Codex host.
