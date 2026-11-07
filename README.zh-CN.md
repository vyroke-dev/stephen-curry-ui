# 🏀 Stephen Curry UI 3.1

> OpenCodex 的自适应极致 Web Design / Creative Engineering Skill。
>
> **不指定默认文字模型**：在 OpenCodex 及其他兼容 Agent 环境中，由当前可用模型执行相同的设计工作流。任何可用图像模型按需生成视觉资产；Higgsfield 是可选媒体制作工具，**不是网页互动引擎**。

## 下载后安装

解压包，保留整个 `stephen-curry-ui` 目录：

```text
~/.agents/skills/stephen-curry-ui/SKILL.md
```

这是常见的 Codex / Agent Skills 安装路径。如果你的 GitHub OpenCodex Fork 有自己的 Skills 目录或刷新方式，以 Fork 的说明为准。重启/刷新 Skills 后尝试：

```text
$stephen-curry-ui 为一个高端实验性设计公司做完整网站。
先研究已上线优秀作品（首屏、中段、底部、交互、手机端），创建参考档案。
开发前比较 2–3 个真正不同的整站创意方向；选定后绘制 Scene Map 和 DESIGN.md。
为复杂交互做可运行的原型，按章节实现全部网页与跨页转场。
最后对设计、动效、WebGL/特效、UX、性能和工程进行六角色检查，必须检查中段、结尾、鼠标/触屏/键盘以及减少动画设置，并提供证据。
```

## 3.0 相比 2.0 的实质升级

| 部分 | 3.0 新能力 | 文件 |
| --- | --- | --- |
| 创意探索 | 可离线运行、可切换方向/手机版的 HTML Design Explorer | `scripts/style_explorer.py` |
| 专项研究 | 11 个外部项目的优缺点与合法借鉴边界 | `references/external-skill-findings.md` |
| 整站导演 | 场景表、跨章节视觉线索、情绪节奏与状态恢复 | `references/cinematic-system.md` + `templates/scene-map.md` |
| 设计治理 | 可维护的 DESIGN.md 模板、CSS Token 偏差工具 | `templates/DESIGN.template.md` + `scripts/design_guard.py` |
| 动画检查 | 时间序列截图 + 机器本地 rAF 帧间隔诊断 | `scripts/motion_evidence.py` |
| 视觉测量 | 颜色比例、明度、边缘密度和同尺寸像素差异 | `scripts/visual_metrics.py` |
| 整站覆盖 | 将待验收场景/状态与浏览器截图证据对照 | `scripts/experience_matrix.py` |
| 独立盲审 | 创建不包含开发说明的本地证据包供审查者使用 | `scripts/blind_jury.py` |
| 规范审查 | Vercel Web Interface Guidelines 及时更新与离线基线 | `references/interface-guidelines.md` |

## 工具使用（从 Skill 根目录执行）

### 1. 打开本地设计探索对比页

```bash
python scripts/style_explorer.py --input templates/directions.example.json --out /tmp/scui-explorer.html
```

使用浏览器打开 `/tmp/scui-explorer.html`。这是**设计方向对比工具**，不是实际功能网站或最终的 Awwwards 成品。实际项目要替换 JSON 中的示例内容和色彩。

### 2. 生成真实页面的截图与状态证据

```bash
python scripts/experience_audit.py --url http://localhost:3000 --paths /,/work --views desktop,mobile --out /tmp/scui-audit
python scripts/experience_matrix.py --plan templates/experience-plan.example.json --audit /tmp/scui-audit/report.json --out /tmp/scui-coverage.md
```

### 3. 分析真实动画与视觉截图

```bash
python scripts/motion_evidence.py --url http://localhost:3000 --trigger scroll --frames 6 --duration-ms 2400 --out /tmp/scui-motion
# 如果只有可独立运行的本地 HTML 原型：
python scripts/motion_evidence.py --html-file examples/creative-explorer.html --frames 6 --out /tmp/scui-motion-offline
python scripts/visual_metrics.py /tmp/scui-audit/home-desktop-full.png --out /tmp/scui-visual-metrics.json
```

截图路径需要与实际输出一致。像素变化与机器 rAF 数据都不等同于设计质量或真实用户的 Core Web Vitals。

### 4. 核对设计契约与生成盲审证据包

```bash
python scripts/design_guard.py --contract templates/design-contract.example.json --css path/to/your.css --strict
python scripts/blind_jury.py --audit /tmp/scui-audit/report.json --out /tmp/scui-jury
```

盲审包只存于本地；**不会自动调用独立模型**。它可能包含品牌、客户截图等敏感内容，不能上传到公共网站。

## 依赖与模型

- Python 3.10+；最基本的文本/JSON/HTML 生成工具没有第三方 Python 依赖。
- 浏览器录制/检查需要 `playwright` 与浏览器（可安装：`python -m pip install playwright` 和 `python -m playwright install chromium`）。环境有浏览器不代表一定能访问网站。
- `visual_metrics.py` 需要 `Pillow`：`python -m pip install pillow`。
- GPT Image / Higgsfield 只有在你本地 OpenCodex 真正连接了相关工具且允许使用时才启用；任何可能消耗额度的生成动作先按你的授权处理。
- **文字模型完全中立**：Opus、GPT 或其他具备所需能力的模型均可使用；不自动选择、推荐或切换某个模型。并行子代理、浏览器控制、图像生成工具是否可用，以**当前实际运行环境**为准。

## 验证

```bash
python -m unittest discover -s tests -v
python scripts/validate_package.py
```

这只能验证 Skill 包的合同和脚本部分行为。**不能因此保证它已在你的 OpenCodex 中被正确激活，或能产出获奖设计。** 真正评估要让 3.0 在同一个 Brief 上制作完整网站，与 2.0 的成品对照检查。完整的对照测试方案见 `tests/agent-evaluation.md`。

## 使用边界

- 学习了 Auteur、Huashu Design、Awwwards Web Design、Awwwards/Jury、Website Analyzer/Premium Builder、Baoyu Design、Awwwards Motion/3D、Vercel Guidelines，以及你购买的 OIL UI Pro 所体现的**方法**。
- **没有复制或打包它们的专有代码、设计素材、字体或购买文件**。不同开源仓库的许可也不被合并为本 Skill 的整体许可。
- Skill 名称是独立工作名称，不代表 Stephen Curry 本人参与、授权或代言。

完整研究映射见 [外部 Skill 优点](references/external-skill-findings.md)，执行准则见 [核心 SKILL.md](SKILL.md)。
