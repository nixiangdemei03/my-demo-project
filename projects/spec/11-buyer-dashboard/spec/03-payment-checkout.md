# 11-03: Payment Checkout Page

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商确认订单后需要支付。实现支付页面：订单摘要、支付方式选择、跳转网关、成败处理。

## 用户故事

作为采购商，我想支付订单，以便完成交易。

## 任务清单

- [ ] `/checkout/:orderId` — 订单摘要（产品、数量、金额）
- [ ] 支付方式选择（PayPal / Stripe / 支付宝国际版）
- [ ] 支付按钮 → 调用 `/api/payments/checkout` → 跳转支付 URL（v1.0 模拟直接成功）
- [ ] 支付成功 → 跳回订单详情（status=paid）
- [ ] 支付失败 → 显示原因 + 重试按钮
- [ ] 24h 倒计时提醒（超时自动取消）

## 验收标准

- 选择 Stripe → 点击 Pay → 模拟成功 → 跳回 order（status=paid）
- 支付失败 → 页面显示失败原因 + "Try Again"
- 倒计时到期 → 提示 "Order has been cancelled"

## 相关

PRD §4.1 支付状态模型 | 依赖：06+13 | 父 Issue：[11-buyer-dashboard](../acceptance-criteria.md)
