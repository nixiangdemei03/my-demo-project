# Issue 07: Freight & Shipment Tracking

**Labels**: `feat` `p0` `backend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

供应商发货后，采购商需要追踪物流。按 PRD §3 用户故事 SUP-05、BUY-06 和 §4.1 发货追踪流程，实现货运公司管理、发货操作、追踪事件记录。

## 用户故事

- 作为供应商（SUP-05），我想发货时选择货运公司并填入运单号，以便采购商能追踪。
- 作为采购商（BUY-06），我想追踪订单货运状态，以便知道货物到哪了。

## 任务清单

- [ ] `GET /api/freight-companies` — JWT 鉴权，返回货运公司列表
- [ ] `POST /api/freight-companies` — admin 鉴权，创建货运公司
- [ ] `PUT /api/freight-companies/:id` / `DELETE` — admin 鉴权
- [ ] `POST /api/orders/:id/ship` — supplier 发货（freight_company_id + tracking_number）
- [ ] `GET /api/shipments/:id/tracking` — 追踪事件列表（event_time 倒序）
- [ ] `POST /api/shipments/:id/events` — supplier/admin 手动添加追踪事件
- [ ] 写 `test_freight.py` 覆盖 CRUD + 发货 + 追踪 + 权限

## 验收标准

- `POST /api/freight-companies` admin → 201；非 admin → 403
- `POST /api/orders/:id/ship` 合法入参 → 创建 shipment（status=in_transit），订单 status→shipped
- 非本订单 supplier 发货 → 403
- `GET /api/shipments/:id/tracking` 返回事件按时间倒序
- `POST /api/shipments/:id/events` → 201，source 字段 ="manual"
- shipment.status: in_transit → delivered → order.status 自动 → delivered

## 相关

- PRD §3：SUP-05、BUY-06 | API：`docs/04-api-design.md` Freight 段 | 依赖：Issue 06（Orders）
