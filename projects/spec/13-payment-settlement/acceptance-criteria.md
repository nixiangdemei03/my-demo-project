# Issue 13: Platform Payment & Monthly Settlement

**Labels**: `feat` `p0` `backend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

平台统一收银是商业模式的基础——没有支付就没有抽成。按 PRD §4.1 支付状态模型和平台结算模型，v1.0 使用模拟占位 API（真实支付网关后期接入），实现支付创建、webhook 回调、月度结算计算。

## 用户故事

- 作为采购商，我想通过平台统一收银台支付订单，以便安全完成交易。
- 作为供应商，我想每月收到结算单，以便清楚知道到账金额和抽成明细。
- 作为管理员，我想查看和触发月度结算，以便管理平台资金流。

## 任务清单

- [ ] `POST /api/payments/checkout` — buyer 鉴权，v1.0 模拟返回支付成功
- [ ] `POST /api/payments/webhook` — 支付网关回调占位，更新 order.payment_status=paid
- [ ] `GET /api/payments` — 支付流水列表（按角色过滤）
- [ ] 月度结算计算逻辑：Σ delivered 订单 - 退款扣减 = 结算基数
- [ ] 梯度佣金：前 40 供应商 3%，后续 7%
- [ ] 每月 1 日自动生成结算单（含订单明细 + 退款明细 + 抽成计算 + 到账金额）
- [ ] 写 `test_payment.py` + `test_settlement.py`

## 验收标准

- `POST /api/payments/checkout` → 200，order.payment_status → paid，order.status → confirmed
- webhook 回调幂等（重复回调不重复更新）
- 结算计算示例验证：月销 $50,000 - 退款 $3,000 = $47,000，前 40 供应商 3% → 抽成 $1,410，到账 $45,590
- 结算单含订单明细列表（订单号、产品、数量、金额、收货日期）
- 供应商可查看自己的结算单
- pytest 覆盖：支付创建、webhook 回调、结算计算、退款扣减

## 相关

- PRD §4.1 支付状态模型 + 平台结算模型 | 依赖：Issue 06（Orders）
