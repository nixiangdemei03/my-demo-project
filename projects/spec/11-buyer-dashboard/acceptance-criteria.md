# Issue 11: Frontend — Buyer Dashboard

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

采购商需要一个工作台来管理订单、追踪物流、支付和询盘。按 PRD §3 用户故事 BUY-05/06/07 和原型线框图，实现订单列表（状态颜色区分）、订单详情（时间线+货运追踪）、支付页面、询盘历史。

## 用户故事

- 作为采购商（BUY-05），我想在 Dashboard 查看所有订单状态，以便跟踪采购进度。
- 作为采购商（BUY-06），我想追踪订单货运状态，以便知道货物到哪了。
- 作为采购商（BUY-07），我想查看订单历史，以便对账和复购。

## 任务清单

- [ ] 工作台 `/dashboard` — 订单按状态统计概览
- [ ] 订单列表 `/dashboard/orders` — 状态标签颜色区分 + 分页
- [ ] 订单详情 `/dashboard/orders/:id` — 产品信息、供应商信息、时间线、货运追踪、支付状态、24h 倒计时
- [ ] 支付页 `/checkout/:orderId` — 订单摘要、支付方式选择、成败处理
- [ ] 询盘 `/dashboard/inquiries` — 已发送列表、回复详情
- [ ] 个人资料 `/dashboard/profile` — 查看/编辑
- [ ] PC 侧边栏 + 移动端 Tab 导航

## 验收标准

- 订单卡片状态标签颜色：灰=pending、蓝=confirmed、绿=paid、橙=shipped、深绿=delivered、红=cancelled
- 订单详情含垂直时间轴（状态变更历史）
- 货运追踪展示 tracking_events 时间线（事件描述 + 地点 + 时间）
- unpaid 订单显示 24h 倒计时 timer + ⏳ 图标
- 已收货 → "确认收货"按钮 → order.status→delivered
- `/checkout/:orderId` 支付成功 → 跳回订单详情（status=paid）
- 支付失败 → 显示原因 + 重试按钮

## 相关

- PRD §3：BUY-05/06/07 | 原型：`projects/prototypes/buyer/07-dashboard.html` | 依赖：Issue 06+07（Orders + Freight API）
