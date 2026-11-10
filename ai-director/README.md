# AI Director Skill (v1.0.0)

一套受公开影视生成工作流启发的、**独立开发**的 AI 导演 Skill。提供自然语言导演式对话、创意发展、镜头规划、角色/场景/道具连续性、分镜文字预演、视频生成提示词、审查与局部迭代。

**不是** Higgsfield 官方产品、其私有 AI Director 的复制品，也不附带付费视频生成权限。没有外部工具时仍可独立完成导演方案、shot list 和 prompt pack。有可用视频工具时，先检索其真实能力并遵循 `SKILL.md` 中的授权和费用检查点。

## 安装

将整个 `ai-director/` 文件夹复制到所用 Agent 支持的 **Skills 目录**，确保根目录下是 `SKILL.md`（不是嵌套两层）。安装位置及是否支持自动加载由 Agent/IDE 版本决定，请查看宿主平台文档。

对于支持 Skills 标准的 Claude 系环境，一般可将此文件夹加入个人或项目 Skills 目录；在其他 Agent 中，也可直接加载 `SKILL.md` 及其引用文件作为工作规范。**这不等于该 Agent 自动拥有 Higgsfield API 权限。**

## 快速体验

以中文或英文输入：

> 用 AI Director 为我设计一支 20 秒的雨夜科幻悬疑预告片，9:16，一名人物，要求角色外观一致。先给导演方案、分镜和生成 prompts，不要实际花费 credits。

或：

> Act as my AI Director. Turn this product concept into a 15-second commercial with three coherent shots. Please give camera, lens, lighting and continuity instructions.

## 包内文件

- `SKILL.md`：触发条件、行为原则、模式选择、工作流、交付及质量关卡。
- `references/`：导演知识、连续性、对话协议、provider 集成、研究来源。
- `assets/project.schema.json`：独立于提供商的 JSON Schema（Draft 2020-12）。
- `assets/project-template.json`：可复制起步模板。
- `assets/example-noir-project.json`：可验证的黑色电影三镜头示例。
- `assets/prompt-templates.md`：分镜、静帧、视频和审查提示词模板。
- `scripts/validate_project.py`：Python 标准库离线项目检查器，无第三方依赖。
- `tests/test_validator.py`：自动化测试。
- `tests/acceptance-cases.md`：实际 Agent 行为测试情景和验收判据。

## 验证

```bash
python3 scripts/validate_project.py assets/example-noir-project.json
python3 -m unittest discover -s tests -v
```

验证器检查必要字段、数据类型、时长之和、ID 引用、屏幕方向及项目内重复 ID。它不能代替真实影片视觉检查和真人试映。

## Integration 边界

官方文档在 2026-11-11 显示 Higgsfield API 使用 `https://platform.higgsfield.ai`、`Authorization: Key ID:SECRET`、异步提交/状态轮询。不同视频模型的 payload 不通用；这里**不**提供未经验证的“通用视频生成 endpoint”。调用前需按当时模型目录进行模型专属配置并获得用户授权。网站订阅与 API 收费体系不同。

## Sources

研究与原始官方链接见 `references/research-notes.md`。内容按公开能力重新设计，不包含第三方源代码或专有提示词。
