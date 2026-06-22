# 03-01: Register API

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

供应商和采购商需要注册账号。实现 `POST /api/auth/register`，含 bcrypt 哈希 + Pydantic 校验。对应原 Issue 03 注册部分。

## 用户故事

作为供应商（SUP-01），我想用中文注册账号并上传公司资质，以便通过审核后开始销售。

## 任务清单

- [ ] 写 `RegisterRequest` Pydantic schema（email, password, role, company_name, contact_name）
- [ ] 密码强度校验：≥8 位、含字母、含数字
- [ ] 实现 `POST /api/auth/register` — bcrypt 哈希存储
- [ ] 重复 email → 400；缺必填 → 400

## 验收标准

- 合法入参 → 201，响应不含 password_hash
- 重复 email → 400 `"Email already registered"`
- 密码 `Ab1` → 400；`Test1234` → 201

## 相关

PRD §3 SUP-01, BUY-01 | 父 Issue：[03-user-auth](../acceptance-criteria.md)
