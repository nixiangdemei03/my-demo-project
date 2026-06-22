# Issue 14: Refund & Return Flow

**Labels**: `feat` `p1` `backend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

采购商收货后可能发起退货退款。按 PRD §4.1 纠纷/退款流程，v1.0 实现退款申请、供应商处理、结算扣减。退款不单独打款，从供应商当月结算基数中扣除。v1.0 为模拟 API（真实退款在支付网关接入后完成）。

## 用户故事

- 作为采购商，我想对不满意的订单发起退款申请，以便拿回款项。
- 作为供应商，我想决定是否需要检测报告后再处理退款，以便合理定损。

## 任务清单

- [ ] `POST /api/refunds` — buyer 发起退款（order_id + reason + 可选图片）
- [ ] `PATCH /api/refunds/:id` — supplier 处理（approve / reject / request_inspection）
- [ ] `GET /api/refunds` — 按角色过滤
- [ ] orders.refund_status 状态流转实现
- [ ] 退款金额从当月结算扣除
- [ ] 写 `test_refunds.py`

## 验收标准

- `POST /api/refunds` 合法入参 → 201，status=requested
- `PATCH /api/refunds/:id` approve → refund_status=approved → 进入结算扣减
- reject → 附原因，采购商可申请客服介入
- request_inspection → 供应商收货检测后再定损
- orders.refund_status 流转：none→requested→approved→completed 或 none→requested→rejected
- 协商失败 → 平台客服介入入口（v1.0 人工流程）

## 相关

- PRD §4.1 纠纷/退款流程 | 从 Issue 13 拆分 | 依赖：Issue 13（Payment & Settlement）
