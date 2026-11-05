# 🏀 Stephen Curry UI · v1.0

一个为 **OpenCodex** 编写的前端设计 Skill，目标是让默认使用 Claude Opus 5.5 的 Codex 具备适应不同项目的艺术指导、参考研究、视觉生成、创意工程及全面 QA 工作流。也兼容偶尔切换的 GPT 文本模型。

**定位**：跨品类的 Adaptive Creative Director，不固定一种网站风格。注重极致设计、动画、特效和真正可用的产品体验。

> 此名称是独立 Skill 的工作名称，与篮球运动员 Stephen Curry 没有关联或代言关系。

## 安装

下载 ZIP 后解压，保留整个 `stephen-curry-ui` 文件夹。将其放入下列任一位置：

- **个人通用安装**：`~/.agents/skills/stephen-curry-ui/SKILL.md`
- **单个项目**：`<你的项目>/.agents/skills/stephen-curry-ui/SKILL.md`

这些是 Agent Skills / Codex 常见标准路径。**GitHub OpenCodex Fork 的路径、Skill 发现机制和工具能力可能有所不同**，如无法识别，请以你当前 Fork 文档为准。重启 OpenCodex 或刷新 Skills 列表（视具体版本而定）。

技能格式依据 [Agent Skills Specification](https://agentskills.io/specification) 和 [OpenAI Codex Skill 文档](https://learn.chatgpt.com/docs/build-skills)；这些资料并不能保证某个第三方 OpenCodex Fork 实现了所有选项。

## 使用示例

在 OpenCodex 中输入（支持 Skill 选择器时）：

```text
$stephen-curry-ui 为一个高端建筑设计公司制作网站。
先研究优秀真实网站，建立 Reference Brief，提出有原创性的视觉方向。
使用可用的图像生成工具先做桌面和手机概念图，再实现网站。
根据项目需要使用高质量动画/3D，并执行六角色审查和浏览器截图修正。
```

如果当前 Fork 无法识别 `$` Skill 语法，可直接请求它阅读本文件的 `SKILL.md` 并依照工作流执行。

## 文件结构

```text
stephen-curry-ui/
├── SKILL.md                     # 主工作流与 12 条核心规则
├── README.zh-CN.md              # 中文安装与使用
├── references/
│   ├── research-and-creative.md # 参考研究、创意探索、审批
│   ├── visual-first-and-assets.md # 视觉先行、图片素材
│   ├── motion-and-engineering.md  # 动效、技术自由度与实现
│   ├── quality-gates.md          # 六角色质量审查
│   └── memory-and-privacy.md     # 知识库、隐私与隔离
├── assets/                       # 任务、参考、QA、知识模板
├── tests/                        # 静态契约测试与人工场景测试
└── scripts/                      # 包检查辅助脚本
```

## 重要限制

1. **模型关系**：OpenCodex 是执行环境。Opus 5.5 是默认文字模型，GPT 文字模型可替代，不存在必需的独立 Claude Code 进程。
2. **图片生成**：Skill 不会自动安装 GPT Image 2.5 服务，必须当前 OpenCodex 已有可用的图片工具或集成才能调用。不可用时会记录限制并采用诚实的替代设计流程。
3. **多角色审查**：当前 Fork 支持子代理才可以并行执行；否则用同一个模型分六个专业视角顺序审核。
4. **记忆**：Skill 是指令与资源文件，不是会自动训练的模型。项目记录会写到当前项目的文档路径；只有用户授权、系统可写、经过验证且去敏的通用经验才能进入共享知识库。
5. **参考网站**：只有能够通过浏览器或研究工具实际访问时，才能进行实时参考研究。无法访问时须记录为 `BLOCKED`；不可编造研究结果。
6. **作品品质**：这是可执行的质量工作流，但不能承诺一定获得 Awwwards 奖项，或在没有运行测试时宣称某项目已经达到获奖水平。

## 自测

```bash
python -m unittest discover -s tests -v
python scripts/validate_package.py
```

静态检查验证文件与规则是否完整，**不等价于** 在你的 OpenCodex + Opus 5.5 + GPT Image 2.5 环境中进行真实端到端测试。正式使用时建议至少试跑一次新网站和一次既有项目的小修改。
