# Issue 14: Refund & Return Flow

**Label**: `phase-2` `P1`

## 验收标准

- [ ] `POST /api/refunds` — 采购商发起退款申请
  - 必填：order_id、reason
  - 可选：attach images（退货照片/凭证）
  - 返回 refund 记录，状态为 `requested`
- [ ] `PATCH /api/refunds/:id` — 供应商处理退款
  - 可选动作：approve / reject / request_inspection
  - approve → refund_status 变为 `approved`，进入退款结算
  - reject → 附原因，采购商可申请平台客服介入
  - request_inspection → 供应商收货检测后再定损
- [ ] `GET /api/refunds` — 退款列表（按角色过滤）
  - buyer 看自己发起的退款
  - supplier 看自己产品的退款
- [ ] orders 表 `refund_status` 字段状态正确流转：
  - none → requested → approved → completed
  - none → requested → rejected
- [ ] 退款金额从供应商当月结算中自动扣除
- [ ] 协商失败时，任一方可申请平台客服介入（v1.0 为人工流程，无自动仲裁）
- [ ] 所有端点测试通过

## 关联

- 从 Issue 13（Payment & Settlement）拆分
- 数据模型见 `docs/03-data-model.md` orders.refund_status
- API 设计见 `docs/04-api-design.md` Refunds 段
