# Issue 10: Frontend — Supplier Dashboard

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

供应商需要一个工作台来管理产品和订单。按 PRD §3 用户故事 SUP-02/03/04/05/06/08/09/10 和原型线框图，实现产品管理（含图片上传+车型绑定）、订单管理（确认/拒绝/发货）、供应商主页编辑、询盘管理。

## 用户故事

- 作为供应商（SUP-04），我想在 Dashboard 查看和确认/拒绝订单。
- 作为供应商（SUP-05），我想在订单中一键选择货运公司并发货。
- 作为供应商（SUP-09），我想编辑公司主页信息并实时预览。

## 任务清单

- [ ] 工作台 `/dashboard` — 概览卡片（产品数、待处理订单、本月销售额）
- [ ] 产品列表 + 添加表单 `/dashboard/products/new`（含图片拖拽、车型绑定、保修字段）
- [ ] 编辑产品 `/dashboard/products/:id/edit`（预填充、可增删图片）
- [ ] 订单列表 + 详情（采购商信息、询问内容、确认/拒绝/发货操作）
- [ ] 供应商主页编辑 `/dashboard/profile`（模板表单 + 实时预览）
- [ ] 询盘收件箱 `/dashboard/inquiries`（未读标记、回复框）
- [ ] PC 侧边栏 + 移动端底部 Tab

## 验收标准

- 添加产品表单：图片拖拽上传 → 预览缩略图，可拖动排序
- 车型绑定：可动态添加/删除品牌-车型-年份行
- 订单详情显示采购商公司名、国家、OEM 号、需求图片
- 拒绝订单 → 弹出原因输入框 → 确认后订单 status=cancelled
- 发货按钮 → 下拉选择货运公司 + 输入运单号 → 订单 status→shipped
- 主页编辑 → 左侧表单编辑 → 右侧实时预览

## 相关

- PRD §3：SUP-02/03/04/05/06/08/09/10 | 原型：`projects/prototypes/supplier/` | 依赖：Issue 04+07（Products + Freight API）
