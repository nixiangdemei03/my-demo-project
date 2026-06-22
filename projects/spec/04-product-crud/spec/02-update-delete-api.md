# 04-02: Product Update + Delete API

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

供应商需要编辑和上下架产品。实现 `PUT` 部分更新和 `DELETE` 软删除，仅本人可操作。

## 用户故事

作为供应商（SUP-03/06），我想编辑产品信息和管理上下架，以便保持信息准确、避免超卖。

## 任务清单

- [ ] `PUT /api/products/:id` — 部分更新（只改传了的字段），非本人 → 403
- [ ] `DELETE /api/products/:id` — 软删除（status=deleted），非本人 → 403
- [ ] 产品含 warranty 和 return_policy 字段（SUP-10）

## 验收标准

- `PUT` 只传 `{"sell_price":22}` → 200，仅该字段变更
- `PUT` 非本人 → 403
- `DELETE` → status=deleted，GET 列表不再返回

## 相关

PRD §3 SUP-03/06/10 | 依赖：04-01 | 父 Issue：[04-product-crud](../acceptance-criteria.md)
