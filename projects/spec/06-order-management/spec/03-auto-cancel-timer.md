# 06-03: 24h Auto-Cancel Timer

**Labels**: `feat` `p0` `backend` `frontend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

下单后 24h 未支付自动取消。前端显示倒计时，后端定时检查。

## 用户故事

作为平台运营方，我希望超时未付订单自动取消，以便释放库存。

## 任务清单

- [ ] 前端订单详情显示 24h 倒计时 timer（`⏳ HH:MM:SS`）
- [ ] 供应商端订单列表标注「⚠️ 未付款」
- [ ] 后端 24h 检查逻辑（v1.0 用 APScheduler/Cron 轮询）
- [ ] 超时自动 cancel，写入 cancel_reason="timeout"

## 验收标准

- unpaid 订单 → 前端显示实时倒计时
- 24h 到期 → order.status=cancelled, cancel_reason="timeout"
- 供应商端看到「⚠️ 未付款」标签

## 相关

PRD §4.1 支付状态模型 | 依赖：06-02 | 父 Issue：[06-order-management](../acceptance-criteria.md)
