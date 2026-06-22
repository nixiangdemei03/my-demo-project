# 07-02: Shipment + Tracking Events API

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

供应商发货后创建 shipment 记录，后续手动添加追踪事件。实现发货端点和追踪事件 CRUD。

## 用户故事

作为供应商（SUP-05），我想发货时填入运单号；作为采购商（BUY-06），我想追踪物流。

## 任务清单

- [ ] `POST /api/orders/:id/ship` — supplier 发货（freight_company_id + tracking_number）
- [ ] 创建 shipment（status=in_transit），order.status→shipped
- [ ] `GET /api/shipments/:id/tracking` — 事件倒序
- [ ] `POST /api/shipments/:id/events` — supplier/admin 手动添加事件
- [ ] shipment.status：in_transit→delivered（order 自动 delivered）/ exception

## 验收标准

- 发货 → shipment 创建，order.status→shipped
- 非本订单 supplier → 403
- 添加事件 `{"event":"已出关","location":"上海港"}` → 201，source=manual
- delivered → order.status 自动 → delivered

## 相关

PRD §3 SUP-05, BUY-06 | 依赖：07-01, 06-02 | 父 Issue：[07-freight-tracking](../acceptance-criteria.md)
