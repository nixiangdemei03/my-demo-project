# 03-03: Email Verification (SendGrid)

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

注册后需验证邮箱真实性。集成 SendGrid 发送验证邮件。未验证用户登录时拒绝。

## 用户故事

作为平台运营方，我希望注册用户的邮箱经过验证，以便减少虚假账号。

## 任务清单

- [ ] 注册成功后调用 SendGrid API 发送验证邮件（含唯一 token 链接）
- [ ] `GET /api/auth/verify?token=xxx` — 验证 token，设置 verified=true
- [ ] 登录时检查 verified 状态（未验证 → 403）

## 验收标准

- 注册 → SendGrid 发送邮件（含验证链接）
- 点击链接 → verified=true
- 未验证用户登录 → 403 `"Email not verified"`

## 相关

PRD §3 BUY-01 | 依赖：03-01 | 父 Issue：[03-user-auth](../acceptance-criteria.md)
