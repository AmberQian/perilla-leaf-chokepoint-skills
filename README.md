# 紫苏叶供应链咽喉分析技能

这是一个面向 AI 基础设施、半导体与先进制造供应链研究的本地 AI 技能项目。它把“紫苏叶理论 / 咽喉理论”的研究方式整理成可复用的技能、评分表、报告模板和产品预览页。

核心目标不是追逐最显眼的“卖铲人”，而是沿着 AI 资本开支和硬件架构反向拆解供应链，寻找那些市场规模不大、却能限制下游巨大投入推进的上游窄节点。

本项目仅用于研究辅助，不构成投资建议。

## 项目内容

| 路径 | 用途 |
|---|---|
| `SKILL.md` | 主技能说明，告诉 AI 如何执行紫苏叶式咽喉分析。 |
| `references/scoring-rubric.md` | 0-100 分咽喉评分规则。 |
| `references/report-template.md` | 完整分析备忘录模板。 |
| `references/source-hygiene.md` | 资料校验、防幻觉和证据分级规则。 |
| `references/ecosystem-radar.md` | 20 个相关开源项目与可借鉴技能。 |
| `data/ecosystem.json` | 机器可读的生态项目清单。 |
| `scripts/create_analysis_brief.py` | 一键生成 Markdown 分析草稿。 |
| `product/index.html` | 本地可看的紫苏叶选股工作台原型。 |

## 快速开始

生成一个空白分析草稿：

```bash
python3 scripts/create_analysis_brief.py AXTI --output-dir reports
```

在 AI 里调用本技能：

```text
使用 $perilla-leaf-chokepoint 分析 AXTI 是否构成 InP 衬底供应链咽喉。
```

本地预览产品页：

```bash
python3 -m http.server 4173 --directory product
```

然后打开：

```text
http://127.0.0.1:4173
```

## 推荐研究流程

1. 输入股票代码、公司、组件、材料或 AI 基础设施主题。
2. 从下游需求和资本开支开始，反向拆解系统架构与物料链。
3. 找出最窄的上游节点。
4. 用 `references/scoring-rubric.md` 打分。
5. 用 `references/source-hygiene.md` 校验证据。
6. 用 `references/report-template.md` 输出研究备忘录。
7. 在做任何投资判断前，先完成反方压力测试。

## 产品原型

`product/index.html` 不是项目目录页，而是一个可操作的选股工作台：

- 左侧：候选池、主题筛选、搜索。
- 顶部：紫苏叶方法论 5 步流程，新手能先理解怎么用。
- 中间：咽喉总分、雷达图、机会矩阵、供应链反推图、可调评分拆解、证据 / 催化剂 / 监控标签页。
- 右侧：新手引导、紫苏叶过滤器、反方压力测试、下一步动作、可复制研究指令。

当前候选池使用示例数据，目的是跑通方法论产品化流程。后续可接入 SEC 公告、财报电话会、新闻、技术论文、行业报告和 Serenity 提及档案。

## 部署

仓库已经准备好 GitHub Pages 自动部署：

- 根目录 `index.html` 会自动跳转到 `product/index.html`。
- `.github/workflows/deploy-pages.yml` 会在推送到 `main` 后发布静态页面。
- `.nojekyll` 会避免 GitHub Pages 对静态文件做 Jekyll 处理。

如果本机已安装并登录 GitHub CLI，可在仓库目录运行：

```bash
gh repo create perilla-leaf-chokepoint-skills --public --source . --push
```

推送后，在 GitHub 仓库的 `Settings → Pages` 中确认 Source 为 `GitHub Actions`。工作流跑完后，仓库首页会显示 Pages 网址。

## 推荐仓库名

```text
perilla-leaf-chokepoint-skills
```

这个名字强调“紫苏叶 + 供应链咽喉 + AI 技能”，同时避免冒充 Serenity / @aleabitoreddit 本人。

## 许可协议

MIT。
