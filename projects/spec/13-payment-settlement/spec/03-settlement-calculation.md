# 13-03: Monthly Settlement Calculation

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

每月 1 日自动结算上月已收货订单。梯度佣金：前 40 供应商 3%，后续 7%。退款金额从结算基数扣除。

## 用户故事

作为供应商，我想每月收到结算单，以便清楚知道到账金额和抽成明细。

## 任务清单

- [ ] 结算计算逻辑：Σ delivered 订单 - 退款扣减 = 结算基数
- [ ] 梯度佣金判定：前 40 供应商 ×3%，后续 ×7%
- [ ] 每月 1 日自动触发（v1.0 用 Cron/APScheduler）
- [ ] 退款不单独打款，从当月结算基数扣除
- [ ] 写 `test_settlement.py` 验证计算示例

## 验收标准

- 计算示例验证：$50,000 - $3,000 退款 = $47,000，前 40 供应商 3% → 抽成 $1,410，到账 $45,590
- 第 41 个供应商同金额 → 抽成 $3,290
- 每月 1 日 00:00 自动生成上月结算记录

## 相关

PRD §4.1 平台结算模型 | 依赖：13-02 | 父 Issue：[13-payment-settlement](../acceptance-criteria.md)
