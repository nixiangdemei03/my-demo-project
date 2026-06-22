# 01 — PRD 工作流

> 从模糊想法到结构化 PRD，含复审和修复闭环。

## 流程

```
想法 → /brainstorming（8轮）
     → 产出 6 份文档（product-brief / PRD / tech-design / data-model / api-design / roadmap）
     → Claude 交叉复审（PRD ↔ 5 配套文档 ↔ Issues ↔ 原型）
     → 输出问题列表（14 条）
     → 用户逐条回复（prd_repair.txt）
     → 修复 PRD + 全部配套文档
     → 形成 Q&A 记录（prd-review-qa.md）
     → 再次复审验证（评分 8.4）
```

## PRD 必须包含的 5 个板块

| # | 板块 | 写什么 |
|:--:|------|------|
| 1 | 目标 | 解决什么问题、给谁解决、衡量指标 |
| 2 | 非目标 | 明确不做什么（防 scope creep） |
| 3 | 用户故事 | "作为 X，我想 Y，以便 Z" |
| 4 | 验收标准 | 做到什么样算完成 |
| 5 | 风险 | 已知会卡的 + 不确定的 |

## 复审维度

| 维度 | 说明 |
|------|------|
| 完整度 | PRD ↔ 数据模型 ↔ API 设计 ↔ Issues 四层一致性 |
| 边界 | 说了"不做"的有没有偷偷做；说了"做"的有没有落地 |
| 可执行性 | 按当前文档直接写代码会踩哪些坑 |
| 商业合理性 | 模式有没有逻辑漏洞或风险 |

## 关键文件

- PRD 模板：[templates/report.md](../templates/report.md)
- 当前 PRD：[docs/01-prd.md](../docs/01-prd.md)
- 配套文档：[docs/00-product-brief.md](../docs/00-product-brief.md) ~ [docs/05-roadmap.md](../docs/05-roadmap.md)
- 复审 Q&A：[projects/spec/prd-review-qa.md](../projects/spec/prd-review-qa.md)

## 经验教训

1. **PRD 不是写出来的，是问出来的** — 8 轮 brainstorm 每轮只聚焦一个维度，逐个消除模糊
2. **AI 复审 PRD 能发现人忽略的系统性问题** — 自评 8.8，复审 6.5，修复后 8.4
3. **AI 会默认互联网上存在它想象的 API** — 涉及外部数据源的方案必须亲自验证
4. **改了 PRD 之后必须同步改所有关联文件** — 原型/数据模型/API 设计/Issues 四向对齐
