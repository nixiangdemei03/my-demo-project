# 03-04: Auth Middleware + Login/Register Pages

**Labels**: `feat` `p0` `backend` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

统一的 JWT 鉴权中间件供所有受保护端点使用，以及前端登录/注册页面。

## 用户故事

- 作为开发者，我想用一行 `Depends(get_current_user)` 给端点加鉴权。
- 作为采购商，我想在浏览器上注册和登录。

## 任务清单

- [ ] 写 `get_current_user` 依赖注入（提取 JWT → 查 DB → 返回 User）
- [ ] 前端登录页 `/auth/login` — 邮箱+密码，错误提示
- [ ] 前端注册页 `/auth/register` — 角色选择+公司信息，密码实时校验
- [ ] 注册成功跳转登录；登录成功存 token 到 localStorage

## 验收标准

- 保护端点无 token → 401；buyer 访问 supplier-only → 403
- 注册页密码 <8 位 → 实时红色提示
- 登录成功 → 跳转 Dashboard

## 相关

依赖：03-01, 03-02 | 父 Issue：[03-user-auth](../acceptance-criteria.md)
