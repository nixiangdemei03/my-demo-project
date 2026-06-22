# Issue 15: Inquiry → Order Conversion

**Label**: `phase-2` `P0`

## 验收标准

- [ ] `POST /api/inquiries/:id/convert-to-order` — 询问转正式订单
  - 仅 inquiry_type = `inquiry` 的询盘可转单
  - 仅 buyer 可发起转单
  - 自动带入询问中的 product_id、quantity、oem_number、vin
  - 生成正式 order_number（APEX-YYYYMMDD-NNNN）
  - 询问状态变为 `converted_to_order`，记录 converted_order_id
- [ ] `PATCH /api/inquiries/:id/cancel` — 取消询问
  - buyer 或 supplier 均可取消
  - 状态变为 `cancelled`
  - 双方端均保留询问记录
- [ ] 询问单界面（前端）含两个按钮：
  - 「下单」→ 调用 convert-to-order → 跳转至订单详情
  - 「取消」→ 调用 cancel → 询问列表显示"已取消"
- [ ] 取消后平台推荐同类产品（供应商拒绝时触发）
- [ ] inquiries 表完整 schema（见 `docs/03-data-model.md`）
- [ ] 所有端点测试通过

## 关联

- PRD BUY-12 询问订单流程
- 前端原型：buyer/03-product-detail.html 询问表单
- 数据模型见 `docs/03-data-model.md` inquiries 表
- API 设计见 `docs/04-api-design.md` Inquiries 段
