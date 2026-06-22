# 15-03: Inquiry Cancel + Frontend Buttons

**Labels**: `feat` `p0` `backend` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

询问可能被取消（买方不想买了/供应商无法供货）。实现取消端点和前端「下单」「取消」两个按钮。

## 用户故事

作为采购商，我想取消不再需要的询问。作为供应商，我想对无法供货的询问点取消。

## 任务清单

- [ ] `PATCH /api/inquiries/:id/cancel` — buyer 或 supplier 均可取消
- [ ] 状态变 cancelled，记录 cancelled_by（buyer/supplier）
- [ ] 双方端均保留询问记录
- [ ] 前端询问单界面：「下单」→ 调用 convert-to-order / 「取消」→ 调用 cancel
- [ ] 取消后平台推荐同类产品
- [ ] 写 `test_inquiries.py`

## 验收标准

- 取消 → status=cancelled，双方 inquiry 列表仍可见
- 「下单」→ 跳转订单详情；「取消」→ 列表显示 cancelled 标签
- supplier 拒绝 → 采购商收到通知 + 推荐同类产品

## 相关

PRD §4.1 询问转单流程 | 依赖：15-01, 15-02 | 父 Issue：[15-inquiry-to-order](../acceptance-criteria.md)
