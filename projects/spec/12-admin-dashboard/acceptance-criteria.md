# Issue 12: Admin Dashboard & Management

**Labels**: `feat` `p1` `frontend` `backend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

管理员需要全局视图来审核供应商、管理内容和监控运营。按 PRD §3 用户故事 ADM-01~06，实现控制台统计、用户审核、产品/订单/类别/货运/结算管理。

## 用户故事

- 作为管理员（ADM-01），我想审核供应商上传的证照并决定通过或退回。
- 作为管理员（ADM-04），我想查看平台统计数据，以便掌握运营状况。
- 作为管理员（ADM-05），我想管理产品类别树，以便保持分类合理。

## 任务清单

- [ ] 控制台 `/admin` — 统计卡片 + 待审核队列 + 最近订单
- [ ] 用户管理 `/admin/users` — 列表 + 审核队列（查看证照 → Approve/Reject 附原因）
- [ ] 产品管理 `/admin/products` — 全局列表 + 违规下架
- [ ] 订单管理 `/admin/orders` — 全局视图
- [ ] 类别管理 `/admin/categories` — CRUD 类别树
- [ ] 货运公司管理 `/admin/freight` — CRUD
- [ ] 结算管理 `/admin/settlements` — 结算单列表/详情、手动触发结算

## 验收标准

- 控制台统计卡片数据来自 `GET /api/admin/stats`
- 审核队列：点击 Approve → supplier.verified=true；Reject → 弹出原因输入框
- 类别管理：添加子类别 → 类别树实时更新
- 违规产品下架 → 确认弹窗 + 原因记录 → product.status=deleted
- 结算单含订单明细、退款扣减、抽成计算、到账金额

## 相关

- PRD §3：ADM-01~06 | 依赖：Issue 03+04+06+07+13（Auth + Products + Orders + Freight + Payment API）
