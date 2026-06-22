# 13-02: Payment Records + Flow Table

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

需要 payments 表记录所有支付流水，供应商/采购商/平台三方各可查账。按日生成流水记录。

## 用户故事

作为供应商，我想查看已支付订单的流水记录，以便对账。

## 任务清单

- [ ] 创建 payments 表（order_id, payer_id, amount, currency, payment_method, gateway_tx_id, status, paid_at）
- [ ] 创建 settlements 表（user_id, user_role, period_start, period_end, total_sales, platform_fee, refunds_deducted, net_payout, status）
- [ ] 支付成功后自动写入 payments 记录
- [ ] 日流水自动汇总（supplier/buyer/platform 三方各持一份）

## 验收标准

- 支付成功 → payments 表新增一条 status=success 记录
- 每日流水 → settlements 表每日一条三方记录

## 相关

PRD §4.1 平台结算模型 | 依赖：13-01 | 父 Issue：[13-payment-settlement](../acceptance-criteria.md)
