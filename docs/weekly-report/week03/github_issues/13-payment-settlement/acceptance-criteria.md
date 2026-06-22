# Issue 13: Platform Payment & Monthly Settlement

**Label**: `phase-2` `P0`

## 验收标准

### 统一收银台（后端）
- [ ] `POST /api/payments/create` — buyer 鉴权
  - 入参：order_id, payment_method (paypal/stripe/alipay)
  - 调用支付网关创建订单
  - 返回支付跳转 URL
- [ ] `POST /api/payments/webhook` — 支付网关回调
  - 验证 webhook 签名
  - 更新 order.payment_status = paid, order.status = paid
  - 写入 order_timeline
- [ ] `GET /api/payments/status/:orderId` — 查询支付状态

### 支付方式支持
- [ ] PayPal（REST API v2）
- [ ] Stripe（Checkout Session）
- [ ] 支付宝国际版（跨境支付 API）
- [ ] 支付网关配置通过环境变量注入（API Key / Secret / Webhook URL）

### 月度结算
- [ ] 结算计算逻辑：
  - 每月 1 日 00:00 自动结算上月（已收货订单）
  - 月总销售额 = Σ 所有 delivered 订单金额
  - 退款扣减 = Σ 结算周期内退款订单金额
  - 结算基数 = 月总销售额 - 退款扣减
  - 平台抽成 = 结算基数 × 2%
  - 供应商到账 = 结算基数 × 98%
- [ ] 结算单数据包含：
  - 供应商信息
  - 订单明细列表（订单号、产品、数量、金额、收货日期）
  - 退款明细列表（订单号、退款金额、退款原因）
  - 抽成计算过程
  - 最终到账金额
- [ ] 供应商可查看/下载结算单（PDF）

### 退款处理（结算中）
- [ ] 采购商申请退货 → 供应商确认收货
  - 供应商决定是否需要检测报告
  - 不需要 → 直接确认 → 退款金额进入当月扣减
  - 需要 → 检测定损 → 确认 → 退款金额进入当月扣减
- [ ] 退款不单独打款，从供应商当月结算基数中扣除

### 合规
- [ ] 支付网关对接持牌机构（参考支付宝海外付合规分账方案）
- [ ] 资金流向记录完整（order → payment → settlement → payout）
- [ ] 每笔结算留痕（settlement 表：id, supplier_id, period, total_sales, refunds, base, commission, net_amount, status, created_at）

### 测试
- [ ] `test_payment.py` 覆盖：创建支付、webhook 回调、支付状态查询、重复回调幂等
- [ ] `test_settlement.py` 覆盖：结算计算、退款扣减、结算单生成
