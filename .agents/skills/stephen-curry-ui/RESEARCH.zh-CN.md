# Stephen Curry UI 2.0 · 深度研究与设计论证

**研究日期：2026-11-07**  
**目标：**打造一个跨网站类型、整站级的高创造力 Web Design Skill。用户给出的 Son Daven、Silencio、Why Zero、Unseen Studio 是最低体验参考线，不是视觉模板，也不是能保证超越的量化评分。

> **证据边界：** 此研究通过 Web 内容、第三方获奖记录与开发者第一手文章查阅了四个网站，但当前研究环境**无法在真实浏览器里完整操作这四个网站的所有滚动、声音、手势和移动端动效**。因此明确区分“站点文字可证实”“创作者技术复盘”“第三方描述”和“待真实浏览器验证”。不要把它误当成四站的完整录屏审查。实际项目里仍须每次重新查阅相关优秀作品。

## 核心结论（先看这一段）

想超过这些作品，不能继续增加精美 Hero 和组件 Prompt，而要同时建立 **5 个能落地的系统**：

1. **Experience Direction（整站导演）**：页面从进入到退出的叙事、情绪与商业意图。
2. **Interaction Choreography（互动编排）**：每种输入背后的响应、反馈、完成、逆转和替代路径。
3. **Effects Architecture（效果工程）**：一个可扩展、可同步、可中断、性能自适应的动画与 Shader 系统。
4. **Motion-First Prototyping（先跑起来）**：视觉概念 + 可交互原型，而不是先画一张不可能实现的大图。
5. **Whole-Journey QA（全旅程评审）**：每个段落、转场、路由、设备和交互状态都需要证据。

### 一、四个标杆的真正价值

| 标杆网站 | 值得研究的“设计语言” | v2 应借鉴的方法 | 不要机械复制 |
| --- | --- | --- | --- |
| **Son Daven** | 地域文化、建筑、生态与投资转化交织的长篇叙事 | 用完整章节引导情绪和理解，把商业 CTA 融入故事节奏 | 山脉题材、具体视觉场景、无条件的视差/3D |
| **Silencio** | 把“设计服务”转译成“数字商品”世界观，标签、成分表、条码、购买语言贯穿各个章节 | 从核心品牌隐喻生长出 UI、文案、对象、导航与动画 | 直接套用零售包装、收据、条码设计 |
| **Why Zero** | 把“学习需要亲身参与”变成画圆、按住、破碎、世界探索的行动式叙事 | 全站共享状态/进度、互动关卡、场景生命周期、声音同步、低端性能工程 | 对所有网站都强制画圈、按住、截断滚轮 |
| **Unseen** | 进入方式、声音选择、拖动探索空间、作品过滤、联系方式构成一个完整空间导航系统 | 让空间交互真正承担信息架构；提供可达的退出/列表/筛选/联系路径 | 3D 地球、漂浮作品和视觉结构原样复刻 |

**Son Daven：** 官网直接可查到 prologue、About、Concept、Location、Infrastructure、Wellness、Cuisine 等连续段落，以及 Invest in Son Daven / Consultation 等行动引导。独立奖项记录提到 WebGL、GSAP、Motion、Storytelling，属于外部评价，不等于本研究在浏览器完整验证了运动效果。参考：https://sondaven.com/en 和 https://globalwebdesignawards.com/sites/son-daven。

**Silencio：** 官网可查到自我定义为 Visual Languages 的设计工作室，并反复使用 digital products、条码、ingredients 和 product references 等语言。其作品站有“Scroll & click to open project”。这个案例说明：**创意隐喻必须延伸到细节**，不是只有第一屏一个好看的 3D 物体。参考：https://silencio.es/ 和 https://portfolio.silencio.es/。

**Why Zero：** 这是证据最扎实的技术案例。开发团队 2026-07-17 的 Codrops 文章逐步说明：六个阶段、五个交互关卡；进入时画零；按住玻璃破碎；穿越隧道和城市探索；统一虚拟进度驱动 GLSL/3D/音效/章节；将 1GB+ 制作素材压到 10MB 以下；采用贴图图集、压缩、按需预热 Shader、空闲时 GPU 纹理上传、分级渲染。开发团队报告低端安卓设备流畅运行。这些数字是**作者陈述**，本研究没有独立测量。重要启发是“让复杂度服从一致的体验架构”。参考：https://tympanus.net/codrops/2026/07/17/zero-the-engineering-behind-a-defiant-interactive-narrative/。

**Unseen：** 目前网站可查到 Enter/Enter without audio、Toggle Sound、Drag to explore our world、Click & Hold、项目分类 Filter、联系方式。Awwwards 有该工作室较早版本的视觉记录，不能假定旧版截图等同当前实时版本。启发：极致表现力与**用户的自主权**（选择音效、随时找作品和联系）并不冲突。参考：https://unseen.co/、https://unseen.co/world/ 和 https://www.awwwards.com/sites/unseen-studio。

### 二、深度研究发现：“效果数量”不是天花板

好的网站会有 **高潮、安静、转折和结束**。如果每一屏都 3D、粒子和强视觉冲击，用户反而失去注意力焦点。v2 会让每个重要页面交付：

- **完整体验地图：** 不止 Hero，还包括中段如何递进、何时让用户参与、如何过渡到下一章、最后怎样收尾与行动。
- **Motion Score：** 动画如何通过统一的轨迹、材质和节奏形成整体，不是每个模块各自调用 fade-in。
- **Interaction Contract：** `用户输入 → 实时反馈 → 高潮/完成 → 状态变化 → 可取消/可重进 → 手机和键盘替代方案`。
- **Proof of Concept：** 先实现最困难、最有个性的一个动作，并在浏览器里感受，而不是只看设计图。
- **完整质量矩阵：** 六个角色检查每个页面的首、中、尾、关键转场和主要互动状态。任何“中间偷懒”的地方都是设计缺陷。

### 三、Higgsfield 的真正定位

通过当前已连接的 Higgsfield 工具目录进行**只读核查**，确认平台有：

- GPT Image 2.5 等图片生成/编辑模型。
- 多种从文字、图片等生成视频的工具，适合电影感视频素材、镜头探索、氛围片段。
- 生成或转换 GLB 的 3D 工具，适合作为可交互 3D 原型的素材起点。

但请区分：**素材生成 ≠ 浏览器里的实时互动**。一个 5 秒视频可以带来极好的电影质感，却不能直接实现随着鼠标拖拽而即时改变几何的场景。因此我们不强制每个项目使用 Higgsfield，而是新增**媒体适用性判断**：

| 需求 | 首选工具/实现 | Higgsfield 的价值 |
| --- | --- | --- |
| 创意概念/美术素材 | GPT Image 2.5（若当前环境可用）或真实授权照片 | 平台可能提供模型入口，可按需用 |
| 电影感动态背景/场景片段 | 视频生成 + 后期处理 | **高价值**，需检查循环、体积、质量 |
| 真实的鼠标/滚动驱动变形 | DOM / GSAP / Canvas / WebGL | 生成素材可用于贴图，**不能代替交互** |
| 3D 物体原型 | Blender/GLB/Three.js | 可先生成粗模，但要优化拓扑/贴图 |
| SaaS 操作界面与按钮交互 | 原生 HTML/CSS/JS | **没有明显核心价值，不使用** |

生成额度可能收费且模型、输出支持会变化，必须预先检查能力与费用并取得授权。当前 ChatGPT 的 Higgsfield 连接不代表用户电脑里的 OpenCodex 自动拥有相同接口。**v2 是 Optional Higgsfield，不是 Higgsfield-dependent。** 相关官方说明：https://higgsfield.ai/ 、https://higgsfield.ai/ai-video-editor 。

### 四、技术与性能依据

1. GSAP ScrollTrigger 有 `scrub`、`pin`、`snap` 等控制；但并非所有创意网站都必须使用它。Why Zero 的创作者在特定项目选择了自建虚拟进度，而不是 ScrollTrigger，说明技术应由场景结构决定。参考：https://gsap.com/docs/v3/Plugins/ScrollTrigger/ 。
2. 将大量场景合并时，GPU 纹理上传、Shader 编译、音频/画面同步、场景清理、流畅度管理，都是比单个 animation 更重要的生产问题。Why Zero 的作者详细记录了这些解决方案，需按项目情况验证可迁移性。
3. Google 的 Core Web Vitals 目标仍是 LCP ≤2.5s、INP ≤200ms、CLS ≤0.1，以真实用户访问的第 75 百分位统计为准。不要拿本地一次截图宣称通过真实用户的 CWV。参考：https://web.dev/articles/vitals 。
4. 真实动效需要视频/浏览器 Trace，不是仅靠 screenshots。Playwright 可产生截图、交互与 Trace；Chrome Performance 可分析卡顿。参考：https://playwright.dev/docs/trace-viewer 和 https://developer.chrome.com/docs/devtools/performance 。
5. 极致体验需要照顾键盘、触摸、感官敏感用户和降低动画偏好。参考：https://www.w3.org/TR/WCAG22/ 和 https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion 。

### 五、从 v1 到 v2 的实质改变

| 维度 | v1 主要做法 | v2 必须完成 |
| --- | --- | --- |
| 研究 | 参考优秀作品、记录视觉原则 | 研究整站首中尾、路由、输入行为和工程取舍 |
| 视觉概念 | Desktop/Mobile 静态概念先行 | 静态概念 + 动画分镜 + **运行中的互动原型** |
| 设计 | 关注 Hero、排版、素材和 Signature Element | **整站 Experience Blueprint**、情绪节奏、完整剧情式章节衔接 |
| 动效 | 根据项目选择复杂度 | **共享运动语法、交互契约、场景生命周期、动作中断与恢复** |
| 3D/特效 | 允许 Three.js/GSAP/WebGL | **资源预算、贴图/Shader预热、移动端降级、GPU问题检查** |
| Higgsfield | 未专门评估 | 确认对电影镜头/3D素材有价值，按项目可选，绝不把视频冒充实时交互 |
| QA | 六角色设计/性能评审 | **route × chapter × state × viewport × input** 全旅程覆盖，发现最弱一章并优先修复 |
| 验证 | 静态契约测试 | 加入可运行的 Playwright 整站截图/动作脚本及测试（仍须人工视觉评审） |

### 六、判断 “2.0 是否真的够资格”

一个新的高端网站最终至少要有：**完整体验蓝图、来源明确的参考、核心可玩原型、跨页面动效逻辑、移动端重新设计、真实浏览器整站截图、关键交互录屏/复测、六角色 QA**。任何缺失都不能声称“整站体验通过”。

同时，**没有一个 Skill 能保证必然成为世界顶尖或获奖网站**。我们能控制的是研究深度、审美判断、完整的创意开发过程，以及严格的可验证审查。让上限不断提高，而不是用空泛的“100%完美”替代证据。

---

## 3.0 追加研究：外部 Skill 的互补能力（2026-11-07）

本版新增完整比较文档 `references/external-skill-findings.md`。研究对象涵盖 Auteur、Awwwards Web Design、Awwwards/Jury、Huashu Design、Baoyu Design、Website Analyzer、Premium Website Builder、Awwwards Motion、Awwwards 3D、Vercel Web Design Guidelines，以及用户提供的 OIL UI Pro 付费 Skill。

**核心结论：** 不把这些 Skill 的固定视觉风格、强制技术版本或原始代码一起搬进来；只融合有意义的专业方法。方向探索必须比较整站体验而不是换肤；动画必须关注时间/手势/返回/中断；盲审必须避免审查者被作者意图左右；实测数据只能证明可测指标，不能替代艺术判断。

可执行新工具包括离线方向比较、运动证据采样、视觉图片统计、设计 Token 检查、全站覆盖矩阵及本地盲审证据包。它们为**人工及 AI 审查提供可追溯证据**，不构成网站完美度的自动认证。
