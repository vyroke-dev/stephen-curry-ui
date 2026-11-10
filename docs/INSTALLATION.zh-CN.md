# Stephen Curry UI 4.2 · 安装与升级

从 ZIP 解压的根目录运行：

```bash
python3 install.py --global --upgrade
```

它会在 `~/.agents/skills/` 中安装 10 个 Skill，并且在覆盖已识别的旧版目录之前备份到 `~/.agents/skills/.stephen-curry-ui-backups/`。对于未知同名目录，拒绝覆盖。不会修改 Canvas 项目。

如果只对特定网站仓库启用评审 TOML 和辅助契约工具：

```bash
python3 install.py --project /绝对路径/你的项目 --upgrade
```

不会自动合并目标仓库的 `AGENTS.md`，项目中请审阅后自行合并。重新启动/刷新 Codex，确认 `$stephen-curry-ui` 能被识别。

## Image-Only 视觉门槛
1. Research。
2. 真实内置图片生成制作七张 Design System 视觉板，审核并由用户审批。
3. 真实内置图片生成制作三套不同的网页高保真视觉图，各 Desktop/Mobile，审核并由用户审批。
4. 将获批视觉决策转成可执行 tokens / components，Codex 实现、浏览器 QA。

**禁止任何代码产出设计。** 工具缺失时停止并采用显式图片生成交接，不得用 HTML/CSS/SVG/React 替代。

## 离线结构与证据检查
```bash
python3 tools/scui.py check-suite
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s .agents/skills/stephen-curry-ui/tests -v
```
安装后 Skill 中附带 `support/`。某些契约验证使用 `jsonschema`，可选依赖参见 `requirements-contracts.txt`。

这些检查仅验证文件与证据结构，无法证明真实图像工具输出、四 Agent 独立运行或用户授权；需要实际运行时另行验收。
