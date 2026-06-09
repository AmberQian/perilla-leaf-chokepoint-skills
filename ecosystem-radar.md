# 生态雷达

本文件记录与 Serenity / 白毛股神 / 紫苏叶理论 / 供应链咽喉研究相关，或能辅助本项目扩展的开源技能和项目。用户询问扩展、集成、对标、建库或产品化时读取本文件。

## 集成原则

- 未审查许可证前，不直接复制或内置第三方代码。
- 直接相关的 Serenity 档案只能作为灵感和参照，不应视为事实真理。
- 核心技能保持独立：证据质量、资料校验和反方压力测试比单一账号的注意力更重要。
- 实时数据后续通过 MCP / 数据适配器接入；当前仓库先保持为轻量可安装技能。
- 区分“发现候选”和“投资决策”。雷达信号只用于生成待研究标的。

## 最有用的 20 个相关项目

| 排名 | 项目 | 类别 | 为什么重要 | 怎么用于本项目 |
|---:|---|---|---|---|
| 1 | [aleabito-serenity-skills](https://github.com/lanfuli/aleabito-serenity-skills) | 直接相关 | 将公开 Serenity 内容整理成技能和仪表盘。 | 参考档案结构、双语提示词和提及追踪。 |
| 2 | [serenity-radar](https://claudeatlas.com/skills/lanfuli/serenity-radar/) | 直接相关 | 跟踪 Serenity 提及热度和主题轮动。 | 添加“注意力雷达 -> 咽喉评分”的候选生成流程。 |
| 3 | [serenity-skill](https://github.com/muxuuu/serenity-skill) | 直接相关 | 同类 Serenity 风格瓶颈研究技能。 | 对比清单和输出体验。 |
| 4 | [cc-equity-research](https://github.com/prof-little-bear/cc-equity-research) | 研究技能 | 权益研究智能体、MCP 和个性化层。 | 参考多技能研究套件结构。 |
| 5 | [OctagonAI skills](https://github.com/OctagonAI/skills) | 研究技能 | 金融技能库，覆盖公告、财报和市场数据。 | 接入证据表、催化剂和稀释分析。 |
| 6 | [LangAlpha](https://github.com/ginlix-ai/langalpha) | 研究工作台 | 完整金融 Agent 产品与可视化工作台。 | 作为产品架构灵感。 |
| 7 | [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) | 研究智能体 | 开源金融 AI 智能体平台。 | 借鉴智能体分工和报告流程。 |
| 8 | [financial-research-analyst-agent](https://github.com/gsaini/financial-research-analyst-agent) | 研究智能体 | 多智能体股票分析、RAG 和 UI。 | 借鉴辩论、矛盾检测和 Streamlit / API 模式。 |
| 9 | [china-stock-research-skills](https://github.com/spikeHongg/china-stock-research-skills) | 区域研究 | 中文优先、引用优先的 A 股研究技能。 | 扩展中国供应商和政策风险工作流。 |
| 10 | [OpenBB](https://github.com/OpenBB-finance/OpenBB) | 数据平台 | 面向分析师、量化和 AI 智能体的金融数据平台。 | 未来作为市场与基本面数据底座。 |
| 11 | [octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server) | MCP 数据 | 公告、电话会、指标和股票数据 MCP。 | 作为实时证据采集后端。 |
| 12 | [Equibles](https://github.com/daniel3303/Equibles) | MCP 数据 | 自托管迷你 Bloomberg。 | 本地优先的公告、持仓、内部人和做空数据栈。 |
| 13 | [sec-api-python](https://github.com/SEC-API-io/sec-api-python) | 公告文件 | SEC / EDGAR SDK。 | 自动化稀释、13F 和内部人检查。 |
| 14 | [stockscope-mcp](https://github.com/Stewyboy1990/stockscope-mcp) | MCP 数据 | 免费 SEC MCP 工具。 | 轻量无付费密钥数据适配器。 |
| 15 | [PageIndex](https://github.com/VectifyAI/PageIndex) | RAG 检索 | 面向长文档的推理式检索。 | 做公告、报告和论文的证据定位。 |
| 16 | [edgarParser](https://github.com/rsljr/edgarParser) | 公告文件 | 抽取 10-K 关键章节。 | 拉取风险因素和 MD&A 进入反方观点。 |
| 17 | [stockpulse-ai](https://github.com/amitpatole/stockpulse-ai) | 监控告警 | 全天候股票新闻监控。 | 监控稀释、客户赢单和供货协议。 |
| 18 | [stocks-insights-ai-agent](https://github.com/vinay-gatech/stocks-insights-ai-agent) | RAG 应用 | 股票数据和新闻的 Agentic RAG。 | 学习新闻摄取与网页搜索回退。 |
| 19 | [Tulip](https://github.com/Tulip-Dev/tulip) | 图谱可视化 | 大型图分析和可视化框架。 | 将供应链图从 Mermaid 升级为大型图谱。 |
| 20 | [SkillCheck-Free](https://github.com/olgasafonova/SkillCheck-Free) | 技能质检 | Skill 结构和语义校验。 | 发布前检查 SKILL.md。 |

## 推荐路线图

1. 保持当前仓库为干净的技能包。
2. 使用 `ecosystem.json` 作为机器可读生态注册表。
3. 使用本地产品页浏览生态雷达。
4. 后续增加可选适配器：SEC 公告、市场数据、Serenity 档案、图谱导出。
5. 页面和命名确认后，再创建新的 GitHub 仓库。

## 候选仓库名

- `perilla-leaf-chokepoint-skills`
- `serenity-style-chokepoint-analyst`
- `perilla-leaf-ai-analyst`
- `chokepoint-supply-chain-skills`
- `ai-infra-chokepoint-radar`

推荐：`perilla-leaf-chokepoint-skills`。这个名字描述清晰，不冒充 Serenity 本人，也方便扩展为更广义的研究框架。
