# 03-02: Login + JWT Token API

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

用户注册后需登录获取 JWT。实现 login + refresh + /me 端点。Access Token 30min / Refresh Token 7d。

## 用户故事

作为采购商（BUY-01），我想用邮箱登录，以便浏览产品和下单。

## 任务清单

- [ ] 写 JWT 工具函数（create_access_token, create_refresh_token, decode_token）
- [ ] `POST /api/auth/login` — bcrypt 验证，返回 access_token + refresh_token + user
- [ ] `POST /api/auth/refresh` — 用 refresh_token 换新 access_token
- [ ] `GET /api/auth/me` — JWT 鉴权，返回当前用户
- [ ] `PUT /api/auth/me` — 更新 contact_name, phone, company_name

## 验收标准

- 正确密码 → 200 `{"access_token":"...","refresh_token":"...","user":{...}}`
- 错误密码 → 401
- 无 token → 401；过期 token → 401
- refresh → 200，返回新 access_token

## 相关

PRD §3 SUP-01, BUY-01 | PRD §4.4 安全设计 | 依赖：03-01 | 父 Issue：[03-user-auth](../acceptance-criteria.md)
