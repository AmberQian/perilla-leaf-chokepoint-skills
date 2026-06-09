#!/usr/bin/env python3
"""生成紫苏叶咽喉分析 Markdown 草稿。"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


TEMPLATE = """# {name} - 紫苏叶咽喉分析简报

生成日期：{today}

## 摘要

- 核心投资论点：
- 供应链咽喉：
- 评分 / 置信度：
- 主要上行驱动：
- 主要失败路径：
- 下一步需要的证据：

## 目标定义

- 公司 / 股票代码 / 主题：{name}
- 产品或组件：
- 声称的供应链角色：
- 地域：
- 时间周期：

## 供应链地图

```mermaid
flowchart LR
  A["云厂商 / OEM 需求"] --> B["系统架构"]
  B --> C["模块或子系统"]
  C --> D["关键组件"]
  D --> E["材料 / 设备 / 工艺咽喉"]
```

## 咽喉评分

| 分项 | 0-10 分 | 权重 | 说明 |
|---|---:|---:|---|
| 上游杠杆 |  | 15 |  |
| 供应集中度 |  | 15 |  |
| 替代难度 |  | 15 |  |
| 产能稀缺 |  | 10 |  |
| 价值捕获 |  | 10 |  |
| 需求拉动 |  | 10 |  |
| 证据质量 |  | 10 |  |
| 资产负债表与稀释 |  | 10 |  |
| 时间点与催化剂 |  | 5 |  |

总分：
置信度：

## 证据表

| 主张 | 来源 | 日期 | 置信度 | 矛盾 / 缺口 |
|---|---|---:|---|---|
|  |  |  |  |  |

## 稀释与资本结构

- 现金跑道：
- 债务 / 可转债：
- ATM 或 shelf 文件：
- 近期股权融资：
- 好稀释情景：
- 坏稀释情景：

## 催化剂时间线

| 时间窗口 | 催化剂 | 观察点 | 对投资论点的影响 |
|---|---|---|---|
| 0-3 个月 |  |  |  |
| 3-12 个月 |  |  |  |
| 12-24 个月 |  |  |  |
| 2027 年以后 |  |  |  |

## 反方观点

- 技术失败：
- 客户 / 认证失败：
- 竞争 / 双供失败：
- 资本结构失败：
- 宏观 / 地缘失败：
- 估值失败：

## 监控计划

- 公告：
- 财报关键词：
- 客户或伙伴信号：
- 行业报告：
- 技术论文 / 标准：
- 供货协议：
- 内部人 / 机构变化：

## 底线结论

"""


def slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value.strip())
    return "-".join(part for part in cleaned.split("-") if part) or "咽喉分析简报"


def main() -> None:
    parser = argparse.ArgumentParser(description="生成紫苏叶咽喉分析 Markdown 草稿。")
    parser.add_argument("name", help="要分析的股票代码、公司、组件或主题。")
    parser.add_argument("--output-dir", default=".", help="生成 Markdown 文件的目录。")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{slugify(args.name)}-咽喉分析简报.md"
    path.write_text(TEMPLATE.format(name=args.name, today=date.today().isoformat()), encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()
