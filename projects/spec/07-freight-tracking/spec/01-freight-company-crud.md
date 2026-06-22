# 07-01: Freight Company CRUD

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

供应商发货时需要选择货运公司。实现货运公司 CRUD（admin 管理）。

## 用户故事

作为管理员（ADM-03），我想管理货运公司列表，以便供应商发货时有选项可选。

## 任务清单

- [ ] `GET /api/freight-companies` — JWT 鉴权，返回列表
- [ ] `POST /api/freight-companies` — admin 鉴权，创建
- [ ] `PUT /api/freight-companies/:id` — admin 鉴权，编辑
- [ ] `DELETE /api/freight-companies/:id` — admin 鉴权

## 验收标准

- `POST` admin → 201；非 admin → 403
- 列表含 name_zh/name_en/contact_person/phone/email/shipping_routes

## 相关

PRD §3 ADM-03 | 依赖：03-04 | 父 Issue：[07-freight-tracking](../acceptance-criteria.md)
