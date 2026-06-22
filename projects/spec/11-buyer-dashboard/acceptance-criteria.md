# Issue 11: Frontend — Buyer Dashboard

**Label**: `phase-2` `P0`

## 验收标准

### 工作台 `/dashboard`
- [ ] 我的订单概览（按状态统计：pending/confirmed/paid/shipped/delivered）

### 订单列表 `/dashboard/orders`
- [ ] 订单卡片列表（分页）
- [ ] 状态标签（颜色区分：灰=pending、蓝=confirmed、绿=paid、橙=shipped、绿=delivered、红=cancelled）
- [ ] 点击进入订单详情

### 订单详情 `/dashboard/orders/:id`
- [ ] 产品信息（名称、图片、数量、单价、总价）
- [ ] 供应商信息（公司名、联系人）→ 点击跳转供应商页
- [ ] 订单时间线（状态变更历史，垂直时间轴）
- [ ] 货运追踪（tracking events 时间线 + 当前状态）
  - 显示：事件描述、地点、时间
  - 货运公司名称 + 运单号
- [ ] 支付状态显示
- [ ] 已收货 → "确认收货"按钮

### 支付页面 `/checkout/:orderId`
- [ ] 订单摘要（产品、数量、金额）
- [ ] 支付方式选择（PayPal / Stripe / 支付宝国际版）
- [ ] 支付按钮 → 跳转支付网关
- [ ] 支付成功 → 跳回订单详情（状态已变为 paid）
- [ ] 支付失败 → 显示失败原因 + 重试按钮

### 询盘 `/dashboard/inquiries`
- [ ] 已发送询盘列表
- [ ] 供应商回复详情

### 个人资料 `/dashboard/profile`
- [ ] 查看/编辑个人信息（联系人、电话、国家、语言偏好）

### 响应式
- [ ] PC：侧边栏
- [ ] 移动端：Tab 导航
