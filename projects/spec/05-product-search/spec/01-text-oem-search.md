# 05-01: Text + OEM Search API

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商最常用的搜索方式：输入关键词或 OEM 编号找配件。实现 `GET /api/search?q=` 全文搜索和 `?oem=` 精确匹配。

## 用户故事

作为采购商（BUY-10），我想输入 OEM 编号或关键词搜索，以便快速定位特定部件。

## 任务清单

- [ ] `GET /api/search?q=` — 全文搜索 name_zh/name_en/oem_number，支持组合筛选
- [ ] `GET /api/search?oem=` — 精确+部分匹配，大小写不敏感
- [ ] 空结果 → `{"data":[],"pagination":{"total":0}}`
- [ ] 写 `test_search.py` 覆盖中文搜索、OEM 精确、OEM 部分、空结果

## 验收标准

- `?q=刹车片` → 200 + 分页结果
- `?q=xyznonexistent` → total=0
- `?oem=04465-0K090` 与 `?oem=04465-0k090` 结果一致
- `?oem=04465` 匹配到 `04465-0K090` 和 `04465-0K120`

## 相关

PRD §3 BUY-10 | PRD §4.1 方式 2 | 依赖：04-01 | 父 Issue：[05-product-search](../acceptance-criteria.md)
