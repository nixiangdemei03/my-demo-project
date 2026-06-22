# 13-01: Payment Checkout + Webhook (Mock)

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

平台统一收银是商业模式基础。v1.0 使用模拟占位 API，真实支付网关后期接入。实现 checkout 创建支付和 webhook 回调更新订单。

## 用户故事

作为采购商，我想通过平台支付订单，以便安全完成交易。

## 任务清单

- [ ] `POST /api/payments/checkout` — buyer 鉴权，入参 order_id + payment_method，v1.0 模拟直接返回成功
- [ ] `POST /api/payments/webhook` — 支付网关回调占位，更新 order.payment_status=paid, order.status=confirmed
- [ ] `GET /api/payments` — 支付流水列表（按角色过滤）
- [ ] webhook 幂等（重复回调不重复更新）

## 验收标准

- `POST /checkout` → 200，order.payment_status → paid
- 同一 order 重复 webhook → 不创建重复记录
- `GET /api/payments` → buyer 只看自己的流水

## 相关

PRD §4.1 支付状态模型 | 依赖：06-01 | 父 Issue：[13-payment-settlement](../acceptance-criteria.md)
