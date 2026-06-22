# 04-01: Product Create + Read API

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

供应商需要创建产品，采购商需要浏览产品。实现 `POST /api/products`（创建）和 `GET /api/products`（列表）+ `GET /api/products/:id`（详情）。

## 用户故事

作为供应商（SUP-02），我想创建产品并让采购商能搜索到。作为采购商（BUY-02/03），我想浏览和查看产品详情。

## 任务清单

- [ ] `POST /api/products` — supplier 鉴权，必填 name_zh/category_id/sell_price，自动绑定 supplier_id
- [ ] `GET /api/products` — 公开，分页 `?page=1&page_size=20`，筛选 `?category_id=X&price_min=X&price_max=X`
- [ ] `GET /api/products/:id` — 公开，含图片列表 + 供应商信息 + 车型适配
- [ ] 统一分页响应格式 `{"data":[...],"pagination":{...}}`

## 验收标准

- `POST /api/products` → 201，supplier_id 自动绑定当前用户
- 未登录 → 401；buyer → 403
- `GET /api/products` → 分页格式正确
- `GET /api/products/:id` → 响应含 `supplier`、`images`、`vehicle_fits`

## 相关

PRD §3 SUP-02, BUY-02/03 | 依赖：03-04（Auth Middleware） | 父 Issue：[04-product-crud](../acceptance-criteria.md)
