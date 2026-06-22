# 03 — Spec 工作流

> PRD → Issues（第一次分解）→ 大功能 → Epic 子 Issues（第二次分解）。

## 流程

```
PRD §3 用户故事 + §4 验收标准
  │
  ▼ 第一次分解
所有功能 → 编号文件夹 → acceptance-criteria.md（15 个）
  │  每个含: Title + Labels + 背景 + 用户故事 + 任务清单 + 验收标准 + 相关
  │
  ▼ 判定大功能（≥2 条件）
  │  · 跨模块（backend + frontend）
  │  · 多用户故事（≥2 条）
  │  · 工作量 >2 天
  │  · 可独立交付用户价值
  │
  ▼ 第二次分解
大功能 → spec/ 子文件夹 → 2-5 个子 Issue
  子 Issue 格式同父 Issue，指向 ../acceptance-criteria.md
```

## Issue 标准模板

```markdown
# Issue {编号}: {一句话 Title}

**Labels**: `{type}` `{priority}` `{module}` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景
[为什么要做，引用 PRD 章节]

## 用户故事
作为 {角色}，我想 {动作}，以便 {目的}。

## 任务清单
- [ ] {可执行任务}

## 验收标准
- {条件} → {预期结果}（含 HTTP 状态码 / 响应格式 / UI 表现）

## 相关
PRD §{章节} | 依赖：{前置 Issue}
```

## Labels 规范

| 维度 | 可选值 | 规则 |
|------|------|------|
| type | `feat` `fix` `chore` `docs` `refactor` `test` | ≥1 |
| priority | `p0` `p1` `p2` | ≥1 |
| module | `backend` `frontend` `infra` `ux` | ≥1 |

## 验收标准规则

✅ 可自动验证：含 HTTP 状态码 / 响应格式 / 文件路径 / 具体数字  
❌ 禁止模糊词："好用""快速""正常"

## 目录结构

```
projects/spec/
├── 03-user-auth/              ← 大功能 (Epic)
│   ├── acceptance-criteria.md ← Epic 总览
│   └── spec/
│       ├── 01-register-api.md
│       ├── 02-login-token-api.md
│       ├── 03-email-verification.md
│       └── 04-auth-middleware-pages.md
├── 01-scaffolding/            ← 基础设施（不拆分）
│   └── acceptance-criteria.md
└── 08-supplier-page/          ← 支撑功能（不拆分）
    └── acceptance-criteria.md
```

## 当前拆分结果

| 类型 | 数量 | 
|:--|:--:|
| Issue 总数 | 15 |
| 大功能 (Epic) | 10 |
| 子 Issue | 37 |
| 基础设施/支撑 | 5 |

## 关键文件

- Spec 规范：[templates/spec-guide.md](../templates/spec-guide.md)
- Spec 产出：[projects/spec/](../projects/spec/)
- Spec Skill：[.claude/skills/spec/SKILL.md](../.claude/skills/spec/SKILL.md)
