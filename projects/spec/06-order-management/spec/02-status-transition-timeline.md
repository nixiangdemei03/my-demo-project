# 06-02: Order Status Transition + Timeline

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

订单需要状态流转（pending→confirmed→paid→shipped→delivered）和变更记录。实现状态机 + 自动写 timeline。

## 用户故事

作为供应商（SUP-04），我想确认或拒绝订单；作为采购商（BUY-05），我想知道订单进度。

## 任务清单

- [ ] `PATCH /api/orders/:id/status` — 状态流转校验
- [ ] 合法流转：pending→confirmed, confirmed→paid, paid→shipped, shipped→delivered, 任意→cancelled
- [ ] 非法流转 → 400
- [ ] 每次状态变更自动写入 order_timeline（order_id, status, note, created_by, created_at）
- [ ] cancelled 需 cancel_reason
- [ ] 写 `test_orders.py` 覆盖合法/非法流转

## 验收标准

- `PATCH` pending→confirmed → 200，timeline 新增记录
- `PATCH` pending→delivered（跳状态）→ 400 `"Invalid status transition"`
- cancel 无 reason → 400

## 相关

PRD §3 SUP-04, BUY-05 | 依赖：06-01 | 父 Issue：[06-order-management](../acceptance-criteria.md)
