# APEX — Workflow 记录

> 项目从零到 v1.0 开发过程中沉淀的工作流。每条流程均经过实战验证。

| # | 流程 | 触发场景 | 关键产出 |
|:--:|------|------|------|
| 01 | [PRD 工作流](01-prd-workflow.md) | 有新想法 → 需要结构化文档 | PRD v1.0 + 复审 Q&A + 修复记录 |
| 02 | [原型工作流](02-prototype-workflow.md) | PRD 完成后 → 需要低保真页面 | 14 页灰度线框图 + 校准报告 |
| 03 | [Spec 工作流](03-spec-workflow.md) | PRD 就绪 → 开始编码前 | 15 Issues → 10 Epics → 37 子 Issues |
| 04 | [周报工作流](04-report-workflow.md) | 每周结束 → 需要提交报告 | 结构化周报（7 板块） |
| 05 | [Git 工作流](05-git-workflow.md) | 阶段性成果 → 需要推送 | Conventional Commits + force push |

## 流程关系

```
想法 → [01 PRD] → [02 原型] → [03 Spec] → 编码
                                    ↓
                              [04 周报] ← 每周同步
                              [05 Git]  ← 随时提交
```
