# Issue 07: Freight & Shipment Tracking

**Label**: `phase-2` `P0`

## 验收标准

### 货运公司管理
- [ ] `GET /api/freight-companies` — JWT 鉴权
  - 返回：id, name_zh, name_en, contact_person, phone, email, shipping_routes
- [ ] `POST /api/freight-companies` — admin 鉴权
  - 入参：name_zh, name_en, contact_person, phone, email, shipping_routes(JSON)
  - 返回 201
- [ ] `PUT /api/freight-companies/:id` — admin 鉴权
- [ ] `DELETE /api/freight-companies/:id` — admin 鉴权

### 发货
- [ ] `POST /api/orders/:id/ship` — supplier 鉴权
  - 入参：freight_company_id, tracking_number, estimated_delivery(optional)
  - 创建 shipment 记录，状态 = in_transit
  - 订单状态自动更新为 shipped
  - 非本订单 supplier → 403

### 追踪
- [ ] `GET /api/shipments/:id/tracking`
  - 返回 tracking_events 列表（按 event_time 倒序）
  - 采购商可查看自己订单的货运
  - 供应商可查看自己产品的货运
- [ ] `POST /api/shipments/:id/events` — supplier/admin
  - 入参：event, location(optional), event_time(optional, 默认 now)
  - source 字段自动标记为 "manual"
  - 返回 201 + 事件详情

### 发货状态
- [ ] shipment.status 流转：
  ```
  in_transit → delivered（到货）/ exception（异常）
  ```
- [ ] 到货后 order.status 自动更新为 delivered

### 测试
- [ ] `test_freight.py` 覆盖：CRUD 货运公司、发货、追踪事件添加、权限隔离
