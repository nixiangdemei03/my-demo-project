# 15-02: Inquiry → Order Conversion API

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

结构化询问确认后可一键转为正式订单。实现 convert-to-order 端点，自动带入询问中的 product_id/quantity/OEM/VIN。

## 用户故事

作为采购商（BUY-12），我想在供应商确认后一键将询问转为正式订单。

## 任务清单

- [ ] `POST /api/inquiries/:id/convert-to-order` — 仅 buyer + inquiry 类型
- [ ] 自动带入 product_id, quantity, oem_number, vin
- [ ] 生成正式 order_number，inquiry.status→converted_to_order
- [ ] 记录 converted_order_id

## 验收标准

- 合法 inquiry → 转单成功，返回 order_number
- message 类型 → 400
- 非本人 buyer → 403
- converted 后 inquiry 不可再次转单

## 相关

PRD §4.1 询问转单流程 | 依赖：15-01, 06-01 | 父 Issue：[15-inquiry-to-order](../acceptance-criteria.md)
