# 10-03: Supplier Order Management

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

供应商需要处理收到的订单。实现订单列表（状态颜色区分）、订单详情（采购商信息+询问内容+操作按钮）、确认/拒绝/发货操作。

## 用户故事

作为供应商（SUP-04/05），我想查看订单详情并确认/拒绝/发货。

## 任务清单

- [ ] 订单列表：状态标签颜色区分、筛选、分页
- [ ] 订单详情：采购商信息（公司名/联系人/国家）、产品信息、询问内容（OEM/图片/车型）
- [ ] 操作按钮：确认订单 / 拒绝（附原因弹窗）
- [ ] 已确认订单：发货按钮 → 下拉选货运公司 + 输入运单号 → 提交
- [ ] 订单时间线展示
- [ ] 未付款订单标注「⚠️ 未付款」

## 验收标准

- 拒绝 → 弹出原因输入框 → 确认后 status=cancelled
- 发货 → 选货运公司 + 填运单号 → status=shipped
- 时间线显示状态变更历史

## 相关

PRD §3 SUP-04/05 | 原型：[supplier/03-order-management.html](../../../projects/prototypes/supplier/03-order-management.html) | 依赖：06+07 | 父 Issue：[10-supplier-dashboard](../acceptance-criteria.md)
