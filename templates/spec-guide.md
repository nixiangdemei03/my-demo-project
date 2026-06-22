# Spec 规范 — Issue 书写 & Epic 拆分标准

> 适用：APEX 项目下所有 `projects/spec/` 中的 Issue 定义。

---

## 1. Issue 标准模板

每个 Issue 文件必须包含以下字段和段落：

```markdown
# {编号} {一句话 Title}

**Labels**: `{type}` `{priority}` `{module}` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

[为什么要做这件事。引用 PRD 哪个章节/哪条用户故事。1-3 句足够。]

## 用户故事

作为 {角色}，我想 {动作}，以便 {目的}。

## 任务清单

- [ ] {可执行的具体任务 1}
- [ ] {可执行的具体任务 2}

## 验收标准

- {条件 1} → {预期结果}（含 HTTP 状态码 / 响应格式 / UI 表现）
- {条件 2} → {预期结果}

## 相关

PRD §{章节} | 依赖：{前置 Issue} | 父 Issue：[{名称}](../acceptance-criteria.md)
```

---

## 2. 字段规范

### 2.1 Labels（每个 Issue ≥ 1 type + 1 priority + 1 module）

**type（类型）**：

| Label | 用法 |
|-------|------|
| `feat` | 新功能（默认） |
| `fix` | 修 bug |
| `chore` | 工程类（依赖更新、配置） |
| `docs` | 纯文档 |
| `refactor` | 重构（不改行为） |
| `test` | 纯测试 |

**priority（优先级）**：

| Label | 含义 |
|-------|------|
| `p0` | 阻塞上线，必须这版做 |
| `p1` | 重要但可延后 |
| `p2` | 锦上添花 |

**module（模块）**：

| Label | 范围 |
|-------|------|
| `backend` | API / 数据库 / 服务端逻辑 |
| `frontend` | 页面 / 组件 / 交互 |
| `infra` | 部署 / CI / 存储 / 环境 |
| `ux` | 用户可见的界面或流程 |

**示例**：纯后端 API → `feat` `p0` `backend`；前后端都涉及 → `feat` `p0` `backend` `frontend` `ux`

### 2.2 Milestone

所有 v1.0 Issue 统一 `Milestone: v1.0`。

### 2.3 Assignee

统一 `Assignee: nixiangdemei03`（本项目单人开发）。

---

## 3. 验收标准写法规则

验收标准必须**可被自动验证**——包含具体的数字、文件、URL、响应码，不含模糊词（"好用""快速""正常"）。

| ❌ 反例 | ✅ 正例 |
|---------|--------|
| 注册功能正常 | `POST /api/auth/register` 合法入参 → 201，不含 password_hash |
| 搜索快 | `GET /api/search?q=刹车片` → 200，响应时间 < 500ms |
| 图片上传好使 | jpg → 201 `{"image_url":"https://..."}` ；gif → 400 |
| 页面能看 | PC ≥1024px 侧边栏 / <768px 顶部搜索 |

---

## 4. 大功能作为 Epic 拆分规范

### 4.1 判定标准

满足以下 **≥2 条**，即为大功能，必须作为 Epic 拆分：

| 条件 | 说明 |
|------|------|
| 跨模块 | 同时涉及 backend + frontend |
| 多用户故事 | 覆盖 ≥2 条 PRD 用户故事 |
| 工作量 >2 天 | 单人无法在 2 天内完成 |
| 可独立交付 | 上线后用户能直接感知到价值 |

### 4.2 拆分规则

1. 保留原 Issue 文件在 `{大功能}/acceptance-criteria.md`（作为 Epic 总览）
2. 在 `{大功能}/spec/` 下创建子 Issue，编号 `{01,02,03...}`
3. 每个子 Issue：
   - 可在 **1-2 天内独立完成**
   - 有自己的 labels + milestone + assignee
   - 子 Issue 的 `## 相关` 指向父 Issue `../acceptance-criteria.md`
4. 子 Issue 之间如有依赖，在 `## 相关` 中标注

### 4.3 目录结构

```
projects/spec/
├── 03-user-auth/                  ← Epic（大功能）
│   ├── acceptance-criteria.md     ← Epic 总览（原 Issue，保留）
│   └── spec/
│       ├── 01-register-api.md     ← 子 Issue
│       ├── 02-login-token-api.md
│       ├── 03-email-verification.md
│       └── 04-auth-middleware-pages.md
├── 04-product-crud/
│   ├── acceptance-criteria.md
│   └── spec/
│       ├── 01-create-read-api.md
│       ├── 02-update-delete-api.md
│       ├── 03-image-upload-r2.md
│       └── 04-vehicle-fitment-binding.md
...
```

### 4.4 拆分粒度参考

| Epic 规模 | 子 Issue 数 | 示例 |
|:--:|:--:|------|
| 小 | 2-3 | 纯后端 CRUD |
| 中 | 3-4 | 多端点 API + 前端 |
| 大 | 4-5 | 全栈页面组（多页面 + 多 API） |

### 4.5 拆分检查清单

拆分完成后逐条检查：

- [ ] 每个子 Issue 能独立完成（不依赖未拆的工作）
- [ ] 每个子 Issue 有可自动验证的验收标准
- [ ] Labels（type + priority + module）完整
- [ ] 子 Issue 间依赖关系在 `## 相关` 中标明
- [ ] 父 Issue（acceptance-criteria.md）覆盖所有子 Issue 的验收标准
- [ ] 非大功能的 Issue（基础设施/支撑）不需要建 `spec/` 子文件夹

---

## 5. 完整示例

### 大功能 Issue（Epic 总览）

```markdown
# Issue 03: User Registration & Login API (JWT)

**Labels**: `feat` `p0` `backend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景
供应商和采购商需要注册登录。按 PRD §3 SUP-01/BUY-01 和 §4.4 安全设计。

## 用户故事
- 作为供应商（SUP-01），我想用中文注册账号。
- 作为采购商（BUY-01），我想用邮箱登录。

## 任务清单
- [ ] Register API
- [ ] Login + JWT Token
- [ ] Email Verification
- [ ] Auth Middleware + Frontend Pages

## 验收标准
见各子 Issue：`spec/01-register-api.md` ~ `spec/04-auth-middleware-pages.md`

## 相关
PRD §3 SUP-01, BUY-01 | PRD §4.4 | 依赖：Issue 02（Database）
```

### 子 Issue

```markdown
# 03-01: Register API

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景
供应商和采购商首先需要能注册。实现 `POST /api/auth/register`。

## 用户故事
作为供应商（SUP-01），我想用中文注册账号。

## 任务清单
- [ ] 写 RegisterRequest Pydantic schema
- [ ] 密码强度校验：≥8 位、含字母+数字
- [ ] 实现 POST /api/auth/register — bcrypt 存储

## 验收标准
- 合法入参 → 201，不含 password_hash
- 重复 email → 400
- 密码 Ab1 → 400；Test1234 → 201

## 相关
PRD §3 SUP-01 | 父 Issue：[03-user-auth](../acceptance-criteria.md)
```
