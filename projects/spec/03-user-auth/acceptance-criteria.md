# Issue 03: User Registration & Login API (JWT)

**Labels**: `feat` `p0` `backend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

供应商和采购商需要注册登录才能使用平台。按 PRD §3 用户故事 SUP-01、BUY-01 和 §4.4 安全设计，实现 JWT 认证（Access 30min / Refresh 7d）、bcrypt 密码哈希、邮箱验证。

## 用户故事

- 作为供应商（SUP-01），我想用中文注册账号并上传公司资质，以便通过审核后开始销售。
- 作为采购商（BUY-01），我想用邮箱注册并登录，以便浏览产品和下单。

## 任务清单

- [ ] `POST /api/auth/register` — 密码 bcrypt，最小 8 位字母+数字
- [ ] `POST /api/auth/login` — 返回 access_token + refresh_token + user
- [ ] `POST /api/auth/refresh` — refresh_token 换新 access_token
- [ ] `GET /api/auth/me` — JWT 鉴权，返回当前用户
- [ ] `PUT /api/auth/me` — 更新个人信息
- [ ] SendGrid 邮箱验证（注册后发邮件，点击链接 verified=true）
- [ ] 写 `test_auth.py` 覆盖 6 个场景

## 验收标准

- `POST /api/auth/register` 合法入参 → 201，响应不含 password_hash
- 重复 email → 400 `"Email already registered"`
- 密码 <8 位 / 无字母 / 无数字 → 400
- `POST /api/auth/login` 正确密码 → 200 + tokens；错误 → 401
- `GET /api/auth/me` 无 token → 401；过期 token → 401
- pytest 覆盖：注册成功、重复注册、登录成功、密码错误、Token 过期、权限拒绝

## 相关

- PRD §3：SUP-01、BUY-01 | PRD §4.4 安全设计 | 依赖：Issue 02（Database）
