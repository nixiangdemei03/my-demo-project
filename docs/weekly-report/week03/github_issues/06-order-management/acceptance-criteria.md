# Issue 06: Order Management API

**Label**: `phase-2` `P0`

## 验收标准

### 创建订单
- [ ] `POST /api/orders` — buyer 鉴权
  - 入参：product_id, quantity, notes(optional)
  - 自动计算 total_price = product.sell_price × quantity
  - 自动生成 order_number：`APEX-YYYYMMDD-NNNN`
  - 初始状态：pending, payment_status: unpaid
  - 返回 201 + 订单详情

### 查询
- [ ] `GET /api/orders` — JWT 鉴权
  - buyer 只返回自己的订单
  - supplier 只返回自己产品的订单
  - admin 返回全部
  - 支持 `?status=pending&page=1&page_size=20`
- [ ] `GET /api/orders/:id` — JWT 鉴权
  - 返回订单详情 + order_timeline + shipment 信息
  - 非本人/非关联方 → 403

### 状态流转
- [ ] `PATCH /api/orders/:id/status`
  - 合法流转：
    ```
    pending → confirmed (supplier)
    confirmed → paid (payment callback)
    paid → shipped (supplier, 需同时填 freight_company_id + tracking_number)
    shipped → delivered (buyer 确认 or supplier 标记)
    任意状态 → cancelled (buyer/supplier，需 cancel_reason)
    ```
  - 非法流转 → 400 `{"error":"Invalid status transition"}`
- [ ] 每次状态变更自动写入 `order_timeline`（order_id, status, note, created_by, created_at）

### 超时处理
- [ ] 48h 未支付 → 发送提醒通知
- [ ] 72h 未支付 → 自动取消，写入 cancel_reason="timeout"

### 测试
- [ ] `test_orders.py` 覆盖：创建订单、状态流转、非法流转拒绝、权限隔离、超时取消逻辑
