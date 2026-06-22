# Issue 15: Inquiry → Order Conversion

**Labels**: `feat` `p0` `backend` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

APEX 核心差异化：采购商先询问再下单。按 PRD §3 用户故事 BUY-04/12 和 §4.1 询问转单流程，实现询问→订单转换（下单/取消两个按钮）、inquiries 表完整 schema、两层消息系统（轻量 message + 重量 inquiry）。

## 用户故事

- 作为采购商（BUY-12），我想提交结构化询问（含 OEM、图片、车型信息），在供应商确认后可一键转为正式订单，以便先确认库存和价格再下单。
- 作为采购商（BUY-04），我想给供应商发轻量消息，以便简单咨询。

## 任务清单

- [ ] inquiries 表完整 schema（inquiry_type: message/inquiry, status: open/replied/converted/cancelled）
- [ ] `POST /api/inquiries` — buyer 发送询盘（区分 message / inquiry 类型）
- [ ] `GET /api/inquiries` — 收/发件箱，按 type + status 筛选
- [ ] `PATCH /api/inquiries/:id/read` — 标记已读
- [ ] `POST /api/inquiries/:id/convert-to-order` — 仅 buyer + inquiry 类型，自动带入信息生成订单
- [ ] `PATCH /api/inquiries/:id/cancel` — buyer/supplier 均可取消
- [ ] 前端询问单界面含「下单」和「取消」两个按钮
- [ ] 写 `test_inquiries.py`

## 验收标准

- `POST /api/inquiries` type=inquiry → 201，含 OEM/VIN/图片字段
- type=message → 201，仅文本字段
- `POST /api/inquiries/:id/convert-to-order` → 生成 order_number，inquiry.status→converted_to_order
- message 类型尝试转单 → 400
- 取消后双方端均保留记录（status=cancelled）
- 供应商拒绝 → 平台推荐同类产品

## 相关

- PRD §3：BUY-04/12 | PRD §4.1 询问转单流程 | 数据模型：`docs/03-data-model.md` inquiries 表 | 依赖：Issue 06（Orders）
