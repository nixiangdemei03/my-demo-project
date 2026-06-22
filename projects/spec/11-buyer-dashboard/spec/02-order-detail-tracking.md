# 11-02: Order Detail + Tracking Display

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商需要订单详情和物流追踪。实现时间线、货运追踪事件、供应商信息、确认收货。

## 用户故事

作为采购商（BUY-06），我想追踪订单货运状态，以便知道货物到哪了。

## 任务清单

- [ ] 产品信息（名称、图片、数量、单价、总价）
- [ ] 供应商信息（公司名、联系人）→ 可跳转
- [ ] 订单时间线（状态变更历史，垂直时间轴）
- [ ] 货运追踪（tracking events 时间线：事件描述 + 地点 + 时间）
- [ ] 货运公司名称 + 运单号
- [ ] 支付状态显示
- [ ] 已收货 → "确认收货"按钮

## 验收标准

- 时间线从最早→最新排列
- 货运追踪事件按时间倒序
- 确认收货 → status→delivered

## 相关

PRD §3 BUY-06 | 依赖：06+07 | 父 Issue：[11-buyer-dashboard](../acceptance-criteria.md)
