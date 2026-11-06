# 🏀 Stephen Curry UI 2.0

**一套可安装、面向极致整站体验的 OpenCodex 前端设计 Skill。** 不依赖独立 Claude Code。OpenCodex 默认选用 Opus 5.5 时直接运行；偶尔切换 GPT 文本模型也可以。GPT Image 2.5 与 Higgsfield 在实际工具可用、适合需求且获得必要授权时才使用。

> **命名声明：** Stephen Curry UI 是独立个人 Skill 的工作名称，不代表获得运动员或其团队授权或代言。

## 与 v1 的最大区别

v2 不再把“最高设计品质”理解为 Hero 图 + 极端字体 + 炫技动画。它把**整个网站的首次进入、所有章节、相互转场、用户参与、不同页面、结尾与移动端**视为一个整体作品。先研究，画出完整体验蓝图，实测难度最高的互动，再制作全站，最后进行六视角、全旅程 QA。

## 安装

解压 ZIP，保留整个 `stephen-curry-ui` 文件夹。通用 Agent Skills 常见路径：

- 个人：`~/.agents/skills/stephen-curry-ui/SKILL.md`
- 项目：`<项目根目录>/.agents/skills/stephen-curry-ui/SKILL.md`

**OpenCodex 是第三方 GitHub Fork，不同版本可能有不同的 Skills 路径或启动方式。** 若技能没被发现，请查看 Fork 的 Skills 文档并手动确认完整文件夹已复制。Skill 名称：`stephen-curry-ui`。

## 一条真正适合旗舰项目的调用示例

```text
$stephen-curry-ui
为这个品牌制作世界级的完整网站体验。我提供的标准参考有
sondaven.com/en、silencio.es、why.zero.university、unseen.co，
这些只是最低创意参照，不是可以照抄的视觉模板。

必须先研究相关优秀网站的全部旅程，不只首屏。
基于品牌创造独立的世界观，写完整 Experience Blueprint：
入口、叙事章节、互动高潮、跨章节转场、内页、结尾和 CTA。
先做最关键互动的可运行原型和桌面/手机视觉方案，再正式实现。
动画、WebGL、Shaders、视频、声音、光影等按艺术方向自由选用。
有意义时才使用 GPT Image / Higgsfield 生成素材；不必强行使用。
最后用真实浏览器检查每个章节、所有关键交互、移动端、性能，
执行六专业视角 QA，并修复发现的问题。不要只把 Hero 做漂亮。
```

## 建议操作流程

1. 先打开 [深度研究报告](RESEARCH.zh-CN.md)，理解四个标杆的共同结构与证据限制。
2. 阅读主 [SKILL.md](SKILL.md) 的七个执行 Gate。其余内容采用引用文件按需读取。
3. 安装后先试运行一个有 3–5 个章节、至少两个不同交互状态的概念网站，并用浏览器记录结果。
4. 运行质量检查脚本，结合手动观测补足脚本无法判断的“艺术指导和动效手感”。

## 内置浏览器检查工具

需要 Python、Playwright 和可用的 Chrome/Chromium。仅在你已启动的网站/本地预览上运行：

```bash
python -m pip install playwright
python -m playwright install chromium

python scripts/experience_audit.py \
  --url http://localhost:3000 \
  --paths /,/work,/about,/contact \
  --views desktop,tablet,mobile \
  --out .scui-audit

# 额外测试减少动画模式
python scripts/experience_audit.py \
  --url http://localhost:3000 \
  --views desktop,mobile --reduced-motion \
  --out .scui-audit-reduced

# 可选：编辑 JSON 以检查某些真实交互状态
python scripts/experience_audit.py \
  --url http://localhost:3000 \
  --interactions examples/interaction-manifest.json \
  --out .scui-audit-actions
```

脚本产出 `report.json`、`report.md` 和首中尾截图（对可滚动页面）。它**不会自动证明**动画足够流畅、网站符合 WCAG、视觉达到奖项水准、真实 CWV 达标，或者某个复杂 WebGL 按住关卡已真正完成。极端复杂的虚拟滚动需要额外手动/交互脚本测试。

## 可选 Higgsfield

详细见 [media-and-higgsfield.md](references/media-and-higgsfield.md)。只有电影感视频、动态背景、视觉素材、3D 初始模型等可以**真正提高整体结果**时才启用。实时交互必须由浏览器代码实现。生成内容可能消耗额度；费用需核实并确认。ChatGPT 的 Higgsfield 连接不会自动变成 OpenCodex 的本地插件。

## 文件结构

```text
stephen-curry-ui/
├── SKILL.md                       # 核心 Skill 与 7 Gate
├── README.zh-CN.md                # 本文
├── RESEARCH.zh-CN.md              # 四个标杆研究与 v2 设计论证
├── references/                    # 深入的经验编排、动画、特效、QA 与素材规则
├── templates/                     # 参考、体验蓝图、互动契约、QA 等模板
├── scripts/
│   ├── experience_audit.py        # Playwright 实际网站截图与交互动作检查
│   └── validate_package.py       # Skill 格式和文件链接检查
├── examples/
│   └── interaction-manifest.json  # 可编辑的互动动作样例
└── tests/                         # 自动化静态测试和浏览器测试夹具
```

## 安装后实战验证

```bash
python -m unittest discover -s tests -v
python scripts/validate_package.py
```

这是包内容和测试工具的验证，**不是**你自己的 OpenCodex + Opus 5.5 + GPT Image 2.5/Higgsfield 真实完整集成测试。真实表现还必须用实际项目测试。

## 设计原则

“极致”不是把所有东西叠到最大，而是在完整体验中做到**创意原创、视觉和动效统一、深度交互、每一幕都有价值、真实性能和可访问性都能经受检验**。
