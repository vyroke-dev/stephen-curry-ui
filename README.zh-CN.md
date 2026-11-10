# Stephen Curry UI 4.1｜网站设计与工程套件

这是一套与模型和 Agent 宿主无关的网站设计与前端工程技能：包含一个主编排 skill，以及研究、品牌、体验架构、设计系统、创意方向、素材与动效、实现、视觉 QA、评估九个专业 skill。

流程会按任务规模调整：小修复只检查相关代码和状态；页面或功能任务聚焦相关旅程；新网站、重大改版及高影响项目才使用完整研究、概念、审批、评审和全程 QA。大型项目仍要求完整体验，不只打磨首屏。

## 安装完整套件

九个专业 skill 通过相对路径连接到主 skill。首次安装或升级时，请把 `plugins/stephen-curry-ui/skills/` 下的十个目录一起复制到同一个 skills 目录：

    git clone https://github.com/vyroke-dev/stephen-curry-ui.git
    mkdir -p ~/.codex/skills
    cp -R stephen-curry-ui/plugins/stephen-curry-ui/skills/stephen-curry-* ~/.codex/skills/

如果宿主使用其他 Skills 路径，请按其文档替换 `~/.codex/skills/`。复制后按需刷新或重启宿主。支持插件市场的宿主也可以使用仓库内的 marketplace manifest；具体安装能力取决于宿主版本。

主入口：`$stephen-curry-ui`。需要时也可以单独调用相应的专业 skill。模型、浏览器、图像生成、子代理和其他集成均以当前运行环境实际可用能力为准。

## 工作流与工具

- 大型项目的常见证据包括研究、体验架构、Brand DNA、Design System、创意方向、评审、QA 与版本记录。小改动无需为了形式创建整套文档。
- `support/contracts/schemas/` 保存可选离线结构合同；`support/tools/scui.py` 可检查合同及质量报告。该工具不会认证用户同意、启动 Agent、运行浏览器或判断设计优劣。
- `scripts/` 保留了本地截图审计、体验覆盖、设计探索、动效取样、图像度量、CSS Token 检查和盲审证据整理工具。它们是证据辅助工具，不是自动评审 Agent。
- 媒体服务与具体模型名称会变化；实际使用前需检测当前工具与权限。不得未经授权花费额度，也不能把生成素材视为事实、授权或已优化成品。

## 验证

在完整 skill 目录中运行：

    python3 scripts/validate_package.py
    python3 support/tools/scui.py check-suite
    python3 -m unittest discover -s tests -v

离线合同工具要求 Python 3.11+；完整 JSON Schema 检查需安装 `support/requirements-contracts.txt`。部分证据脚本和测试另有可选依赖。检查通过不等于宿主已激活技能，也不代表网站的视觉质量、生产就绪或真实用户效果。

更多背景见 [研究笔记](RESEARCH.zh-CN.md) 与 [更新记录](CHANGELOG.md)。

本项目为独立工具，与 Stephen Curry 本人无隶属、授权或代言关系。
