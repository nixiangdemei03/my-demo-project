# Issue 03: User Registration & Login API (JWT)

**Label**: `phase-1` `P0`

## 验收标准

### 注册
- [ ] `POST /api/auth/register`
  - 入参：email, password, role (supplier/buyer), company_name, contact_name
  - 密码 bcrypt 哈希，最小 8 位，字母+数字
  - 返回 201 + user 信息（不含 password_hash）
  - email 重复 → 400 `{"error":"Email already registered"}`
  - 必填字段缺失 → 400 `{"error":"Missing required fields"}`

### 登录
- [ ] `POST /api/auth/login`
  - 入参：email, password
  - 返回：`{"data":{"access_token":"...","refresh_token":"...","user":{...}}}`
  - 密码错误 → 401
  - 邮箱未验证 → 403 `{"error":"Email not verified"}`

### Token
- [ ] `POST /api/auth/refresh` — 用 refresh_token 换新 access_token
- [ ] `GET /api/auth/me` — JWT 鉴权，返回当前用户信息
- [ ] `PUT /api/auth/me` — 更新 contact_name, phone, company_name
- [ ] Access Token 30min 过期，Refresh Token 7 天过期

### 邮箱验证
- [ ] 注册后通过 SendGrid 发送验证邮件（含验证链接）
- [ ] 点击链接 → `GET /api/auth/verify?token=xxx` → verified=true

### 测试
- [ ] `test_auth.py` 覆盖：注册成功、重复注册、登录成功、密码错误、Token 过期、权限拒绝
