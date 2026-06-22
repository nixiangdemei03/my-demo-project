# 05-03: Vehicle Browse + Category Tree

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

不熟悉 OEM 号的采购商可通过品牌→车型→年份逐级浏览，以及类别树按配件类型筛选。实现车型浏览和层级类别树 API。

## 用户故事

作为采购商（BUY-11），我想按品牌→车型→年份浏览配件，以便不熟悉 OEM 号也能找到。

## 任务清单

- [ ] `GET /api/search?make=&model=&year=` — 车型浏览，支持只传 make
- [ ] `GET /api/categories` — 层级类别树（name_zh/name_en/children）

## 验收标准

- `?make=Toyota&model=Hilux&year=2020` → 仅返回该车型适配产品
- `?make=Toyota` → 返回所有 Toyota 适配产品
- `GET /api/categories` → `[{"name_zh":"制动系统","name_en":"Brake System","children":[...]}]`

## 相关

PRD §3 BUY-11 | 依赖：04-04 | 父 Issue：[05-product-search](../acceptance-criteria.md)
