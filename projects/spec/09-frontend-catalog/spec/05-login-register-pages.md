# 09-05: Login + Register Pages

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

用户需要登录和注册的前端页面。实现表单验证、错误提示、注册角色选择。

## 用户故事

作为采购商（BUY-01），我想在浏览器上注册和登录。

## 任务清单

- [ ] 登录页 `/auth/login` — 邮箱+密码，错误提示（"密码错误"/"邮箱未注册"）
- [ ] 注册页 `/auth/register` — 角色选择（Buyer/Supplier 切换）+ 公司信息+联系人
- [ ] 密码实时强度提示（≥8 位 / 含字母 / 含数字）
- [ ] 注册成功 → 跳转登录；登录成功 → 存 token → 跳转 Dashboard
- [ ] 响应式

## 验收标准

- 密码 <8 位 → 红色提示 "至少 8 位"
- 重复 email 注册 → 提示 "Email already registered"
- 登录成功 → localStorage 存 token → 跳转

## 相关

PRD §3 BUY-01, SUP-01 | 依赖：03（Auth API） | 父 Issue：[09-frontend-catalog](../acceptance-criteria.md)
