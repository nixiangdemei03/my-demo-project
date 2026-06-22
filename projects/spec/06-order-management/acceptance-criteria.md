# Issue 06: Order Management API

**Labels**: `feat` `p0` `backend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

采购商下单是平台核心交易闭环的起点。按 PRD §3 用户故事 BUY-05、SUP-04 和 §4.1 采购商下单流程，实现订单创建、状态流转、超时自动取消。订单状态驱动后续支付和发货。

## 用户故事

- 作为采购商（BUY-05），我想下单并查看订单状态，以便跟踪采购进度。
- 作为供应商（SUP-04），我想查看收到的订单并确认/拒绝，以便及时处理采购需求。

## 任务清单

- [ ] `POST /api/orders` — buyer 鉴权，自动计算 total_price，生成 order_number
- [ ] `GET /api/orders` — 按角色过滤（buyer 看自己 / supplier 看自己产品 / admin 看全部）
- [ ] `GET /api/orders/:id` — 订单详情含 order_timeline + shipment
- [ ] `PATCH /api/orders/:id/status` — 状态流转（pending→confirmed→paid→shipped→delivered / →cancelled）
- [ ] 每次状态变更自动写入 order_timeline
- [ ] 24h 未支付 → 自动取消，写入 cancel_reason="timeout"
- [ ] 写 `test_orders.py` 覆盖 CRUD + 状态流转 + 权限隔离 + 超时逻辑

## 验收标准

- `POST /api/orders` 合法入参 → 201，order_number 格式 `APEX-YYYYMMDD-NNNN`
- 初始状态 pending，payment_status unpaid
- buyer 的 `GET /api/orders` 只能看到自己的订单
- `GET /api/orders/:id` 非关联方 → 403
- pending→delivered 跳过中间状态 → 400 `"Invalid status transition"`
- cancelled 状态需 cancel_reason
- 状态变更后 order_timeline 新增一条记录

## 相关

- PRD §3：BUY-05、SUP-04 | PRD §4.1 采购商下单流程 | 依赖：Issue 04（Products）
