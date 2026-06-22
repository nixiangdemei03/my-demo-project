# 06-01: Order Create + Query API

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商下单是交易闭环起点。实现订单创建（自动计算总价+生成编号）和按角色查询（buyer 看自己/supplier 看自己产品）。

## 用户故事

作为采购商（BUY-05），我想下单并查看订单状态，以便跟踪采购进度。

## 任务清单

- [ ] `POST /api/orders` — buyer 鉴权，入参 product_id + quantity，自动计算 total_price
- [ ] 自动生成 order_number：`APEX-YYYYMMDD-NNNN`
- [ ] 初始状态 pending，payment_status unpaid
- [ ] `GET /api/orders` — 按角色过滤，支持 `?status=&page=&page_size=`
- [ ] `GET /api/orders/:id` — 含 order_timeline + shipment，非关联方→403

## 验收标准

- `POST` → 201，order_number 格式 `APEX-20260622-0001`
- buyer 的 `GET /api/orders` 看不到别人的订单
- supplier 只能看到自己产品的订单
- 非关联方 `GET /api/orders/:id` → 403

## 相关

PRD §3 BUY-05, SUP-04 | 依赖：04-01（Products） | 父 Issue：[06-order-management](../acceptance-criteria.md)
