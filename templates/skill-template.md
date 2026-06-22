# Skill 模板 — 格式规范

> 来源：Superpowers skill 标准格式。每个自定义 skill 必须按此模板编写。

---

## Front-matter 字段

```yaml
---
name: draft-issue                    # skill 名字，会被识别为 /<name>
description: 一句话说明这个 skill 干什么    # 用于 skill 列表展示
trigger: when the user wants to...   # 什么时候 Claude 应考虑自动调用此 skill（推荐）
---
```

| 字段 | 作用 | 必须 |
|------|------|:--:|
| `name` | skill 的名字，会被识别为 `/<name>` | ✅ |
| `description` | 一句话说明这个 skill 干什么 | ✅ |
| `trigger` | 什么时候 Claude 应该考虑自动调用这个 skill | 推荐 |

> **trigger 字段很关键**。写得好，Claude 会在合适的时机主动建议用这个 skill；写得差，它只会在你显式 `/draft-issue` 时才用。

---

## Body 结构

```markdown
# /{name}

## 这个 skill 做什么
[一句话 + 一段话说明核心功能]

## 输入
- 输入项 1
- 输入项 2

## 输出格式
[输出内容的模板/结构]

## 必须遵守
- 规则 1
- 规则 2
- 规则 3

## 反模式
- 不要做的事 1
- 不要做的事 2
```

---

## 完整示例

```markdown
---
name: draft-issue
description: 把一段 PRD 片段或粗略需求描述，转成符合本项目规范的 GitHub Issue 草稿。
trigger: when the user wants to draft a new GitHub issue from PRD text or a feature idea
---

# /draft-issue

## 这个 skill 做什么
读用户提供的 PRD 片段或需求描述，输出符合本项目规范的 issue 草稿。

## 输入
- 一段 PRD 文本，或一句话需求描述

## 输出格式
```
## 背景
[引用 PRD 哪一节]
## 用户故事
作为 [X]，我想 [Y]，以便 [Z]。
## 任务清单
- [ ] ...
## 验收标准
- ...
labels: feat / backend / p1
milestone: v1.0
```

## 必须遵守
- 验收标准必须可被自动 review 验证（数字/文件/URL/响应码）
- label 必须含：类型 + 模块 + 优先级
- 不能编造 PRD 里没有的需求
- 信息不足时反问用户，不要编

## 反模式
- 输出"实现一下登录功能"这种空洞描述
- 把多个用户故事塞到一个 issue
- 用"让体验更好"、"提升性能"这种模糊语言
```
