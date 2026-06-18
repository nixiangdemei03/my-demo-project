# Claude Code 插件与技能使用指南

> 涵盖 RTK、Git/GitHub、Superpowers、Gstack、CodraGraph 六大插件体系的使用说明

---

## 目录

1. [RTK — Token 优化 Shell 代理](#1-rtk--token-优化-shell-代理)
2. [Git + GitHub 技能体系](#2-git--github-技能体系)
3. [Superpowers — 开发工作流技能](#3-superpowers--开发工作流技能)
4. [Gstack — 角色化工程团队](#4-gstack--角色化工程团队)
5. [CodraGraph (codegreph) — 代码智能图谱](#5-codragraph-codegreph--代码智能图谱)
6. [协同使用场景](#6-协同使用场景)

---

## 1. RTK — Token 优化 Shell 代理

### 概述

RTK 是一个 token 感知型 shell 代理，能将常见开发命令的 token 消耗降低 60-90%。在 Windows 上以 CLAUDE.md 注入模式运行。

### 基本用法

| 命令 | 作用 |
|------|------|
| `rtk --version` | 查看版本 |
| `rtk git status` | 代理执行 git 命令（自动压缩输出） |
| `rtk init -g --claude-md` | 初始化并注入 CLAUDE.md（已完成） |

### 工作原理

- **自动生效**：Claude Code 会话启动时自动加载 RTK 指令
- **透明代理**：`git status`、目录列表等命令的输出自动压缩
- **按需放行**：调试场景下自动放行完整输出

### 常用场景

| 场景 | 效果 |
|------|------|
| 大型仓库 `git status` | 压缩冗长输出，仅保留关键变更 |
| 目录浏览 `ls` / `dir` | 过滤无关文件，展示核心结构 |
| 构建日志 | 截取错误和警告，省略编译进度 |
| 测试输出 | 保留失败详情，折叠通过用例 |

### 注意事项

- Windows 原生不支持 hook 自动重写（回退到 CLAUDE.md 模式）
- 如需完整 hook 支持，推荐在 **WSL** 中使用
- 重新运行 `rtk init -g --claude-md` 可更新配置

---

## 2. Git + GitHub 技能体系

### 已安装组件

| 组件 | 来源 | 覆盖领域 |
|------|------|----------|
| `commit-commands` | 官方市场 | Git 提交工作流 |
| `github` | 官方市场 | GitHub CLI 集成 |
| CodraGraph git-* 技能 (6个) | CodraGraph | Git 高级操作 |
| CodraGraph gh-* 技能 (4个) | CodraGraph | GitHub 工作流 |

### Git 操作技能表

| 技能 | 触发场景 | 核心功能 |
|------|----------|----------|
| `codragraph-git-bisect` | 回归 bug 排查 | 二分法定位引入 bug 的 commit |
| `codragraph-git-force-push` | 强制推送前确认 | `--force-with-lease` 安全检查 + 恢复指南 |
| `codragraph-git-history-rewrite` | 整理提交历史 | squash/拆分/删除敏感信息/改作者 |
| `codragraph-git-rebase-vs-merge` | 分支整合决策 | rebase vs merge vs squash-merge 选择指南 |
| `codragraph-git-recovery` | 丢失工作恢复 | reflog 探索 + stash 恢复 + 悬空 commit 找回 |
| `codragraph-git-worktree` | 并行分支开发 | `git worktree` 设置 + 最佳实践 |

### GitHub 工作流技能表

| 技能 | 触发场景 | 核心功能 |
|------|----------|----------|
| `codragraph-gh-pr-workflow` | PR 创建/管理 | draft PR、审查请求、CI 检查、合并策略 |
| `codragraph-gh-issue-workflow` | Issue 管理 | 创建、分类、标签、分配、关联 PR |
| `codragraph-gh-actions-debug` | CI 失败排查 | 运行检查、重跑、手动触发、密钥管理 |
| `codragraph-gh-release-workflow` | 版本发布 | semver 升级、标签、发布说明、附件上传 |

### 常用操作示例

```bash
# 使用 GitHub CLI 创建 PR
gh pr create --title "feat: add user auth" --body "Implements OAuth login"

# 二分查找引入 bug 的 commit（对 Claude 说）
"帮我用 git bisect 找到引入这个 bug 的 commit"

# 恢复误删的分支（对 Claude 说）
"我不小心 hard reset 丢了代码，帮我从 reflog 恢复"
```

---

## 3. Superpowers — 开发工作流技能

### 概述

Superpowers 提供一套严格的开发纪律流程：需求探索 → 计划编写 → TDD 实现 → 代码审查 → 验证完成。**在开始任何开发任务前自动触发相应技能。**

### 核心技能表 (14个)

#### 规划阶段

| 技能 | 何时使用 | 说明 |
|------|----------|------|
| `brainstorming` | **任何创造性工作前必须使用** | 探索用户意图、需求和设计方案 |
| `writing-plans` | 多步骤任务，动手写代码之前 | 编写实现计划，明确步骤和风险 |

#### 开发阶段

| 技能 | 何时使用 | 说明 |
|------|----------|------|
| `test-driven-development` | 实现功能或修复 bug 前 | RED-GREEN-REFACTOR 循环 |
| `using-git-worktrees` | 需要隔离的功能开发 | 创建独立 workspace 不干扰主干 |
| `subagent-driven-development` | 执行实现计划中的独立任务 | 派发并行子代理执行 |
| `dispatching-parallel-agents` | 2+ 个互不依赖的任务 | 并行处理加速开发 |
| `executing-plans` | 已有写好的实现计划 | 在独立会话中执行计划 + 审查检查点 |

#### 验证阶段

| 技能 | 何时使用 | 说明 |
|------|----------|------|
| `systematic-debugging` | 遇到任何 bug / 测试失败 | 四阶段系统化调试（始终先于修复提案） |
| `requesting-code-review` | 完成任务 / 实现重要功能 / 合并前 | 验证工作满足需求 |
| `receiving-code-review` | 收到审查反馈后，实施修改前 | 技术严谨性验证，不盲目执行 |
| `verification-before-completion` | **声称完成前必须使用** | 运行验证命令，确认输出后才做成功断言 |
| `finishing-a-development-branch` | 实现完成且测试通过后 | 引导完成分支工作（合并/PR/清理） |

#### 元技能

| 技能 | 说明 |
|------|------|
| `writing-skills` | 创建/编辑技能文件 |
| `using-superpowers` | 查看所有可用技能 |

### 典型工作流

```
brainstorming → writing-plans → (git worktree) → TDD → requesting-code-review
    → receiving-code-review → verification-before-completion → finishing-a-development-branch
```

### 使用示例

```
# 开始新功能前（对 Claude 说）
"帮我用 TDD 实现用户登录功能"

# Claude 会自动：
# 1. 触发 brainstorming 探索需求
# 2. 触发 writing-plans 写实现计划
# 3. 触发 test-driven-development 写测试再写代码
# 4. 触发 verification-before-completion 验证完成
```

---

## 4. Gstack — 角色化工程团队

### 概述

Gstack 将 Claude Code 转换成专属角色代理团队，通过 `/skill-name` 调用不同的工程角色。**53 个技能文件，覆盖规划、设计、开发、测试、发布、安全全流程。**

### 角色技能表

#### 规划与策略

| 技能 | 角色 | 职责 |
|------|------|------|
| `plan-ceo-review` | CEO / 创始人 | 产品愿景、完整性思考、"Boil the Lake" 穷举思维 |
| `plan-eng-review` | 工程经理 | 架构审查、数据流、时序图、边界条件 |
| `plan-design-review` | 设计评审 | 设计稿评审 |
| `plan-devex-review` | 开发者体验 | DX 评审 |
| `plan-tune` | 计划调优 | 优化和调整已有计划 |
| `office-hours` | YC 办公时间 | 六个强制问题重塑产品思路 |

#### 开发与代码

| 技能 | 角色 | 职责 |
|------|------|------|
| `review` | 高级工程师 | 偏执型结构审计，检查 bug 和 N+1 查询 |
| `devex-review` | DX 工程师 | 开发者体验和代码质量 |
| `investigate` | 安全/调试专家 | 深度调查和根因分析 |

#### 测试与质量

| 技能 | 角色 | 职责 |
|------|------|------|
| `qa` | QA 工程师 | 系统化测试、健康评分、问题报告 |
| `qa-only` | 纯测试模式 | 仅测试，不做修复 |
| `browse` | 浏览器测试 | 无头浏览器自动化 + 可视化验证 |
| `health` | 健康检查 | 项目健康状态检查 |

#### 发布与部署

| 技能 | 角色 | 职责 |
|------|------|------|
| `ship` | 发布工程师 | 发布卫生：同步、测试、推送、PR |
| `land-and-deploy` | 部署工程师 | 一键部署上线 |
| `landing-report` | 上线报告 | 生成上线后状态报告 |
| `document-generate` | 文档生成 | 自动生成项目文档 |
| `document-release` | 发布文档 | 生成发布文档 |

#### 安全与控制

| 技能 | 触发条件 | 作用 |
|------|----------|------|
| `careful` | 执行危险命令前 | 警告确认：`rm -rf`、`git push --force` 等 |
| `freeze` | 需要锁定编辑范围 | 限制文件修改到指定目录 |
| `guard` | 需要全面安全保护 | careful + freeze 组合 |
| `cso` | 安全审查 | 安全审计和漏洞排查 |

#### 设计

| 技能 | 用途 |
|------|------|
| `design-consultation` | 设计咨询 |
| `design-review` | 设计评审 |
| `design-html` | HTML 原型设计 |
| `design-shotgun` | 多方案发散设计 |

### 使用示例

```
# CEO 视角审查计划（对 Claude 说）
"用 gstack plan-ceo-review 审查这个功能方案"

# 发布前审查（对 Claude 说）
"用 gstack review 审查这次改动，然后 gstack ship 发布"

# 安全模式（对 Claude 说）
"启用 gstack guard 模式，接下来只修改 src/auth/ 目录"
```

---

## 5. CodraGraph (codegreph) — 代码智能图谱

### 概述

CodraGraph 提供代码图谱感知上下文，为每次编辑展示变更影响范围、调用者和流程参与。**32 个专业技能 + MCP 工具 + PreToolUse/PostToolUse Hooks。**

### 快速起步

```bash
# 在任意 git 仓库中建立索引
cd your-project
codragraph analyze

# 之后在 Claude Code 中自动激活
```

### MCP 工具参考

| 工具 | 用途 | 典型场景 |
|------|------|----------|
| `query` | 流程分组的代码智能 | 相关概念的完整执行流 |
| `context` | 360° 符号视图 | 分类引用 + 参与的处理流程 |
| `impact` | 符号影响半径 | 深度 1/2/3 的影响分析 + 置信度 |
| `detect_changes` | Git diff 影响 | 当前未提交变更影响什么 |
| `rename` | 多文件协同重命名 | 带置信度标记的批量重命名 |
| `feature_clusters` | 产品/领域功能地图 | 定向上下文加载 |
| `feature_context` | 单个功能详情 | 成员、行号范围、依赖、流程 |
| `cypher` | 原始图查询 | 直接查询代码图谱 |
| `list_repos` | 已索引仓库 | 发现所有可查询的仓库 |

### 技能分类速查

#### 🔍 理解与探索

| 技能 | 触发场景 |
|------|----------|
| `codragraph-exploring` | "这个功能怎么实现的？" "调用链是什么？" |
| `codragraph-onboarding` | "我是新来的，帮我熟悉这个代码库" |
| `codragraph-guide` | "CodraGraph 有哪些工具？怎么用？" |

#### 🛡️ 影响分析

| 技能 | 触发场景 |
|------|----------|
| `codragraph-impact-analysis` | "改这里会破坏什么？" "安全吗？" |
| `codragraph-cross-repo-impact` | "哪些服务依赖这个库？" |
| `codragraph-migration-tracking` | "迁移进度如何？还剩什么没迁？" |

#### 🐛 调试与排错

| 技能 | 触发场景 |
|------|----------|
| `codragraph-debugging` | "为什么 X 失败了？错误从哪来的？" |
| `codragraph-dead-code` | "哪些代码没用可以删？" |

#### 🔧 重构

| 技能 | 触发场景 |
|------|----------|
| `codragraph-refactoring` | "重命名这个函数" "把这个类拆开" |
| `codragraph-api-surface` | "我们的公共 API 有哪些？" |

#### 🔒 安全与审计

| 技能 | 触发场景 |
|------|----------|
| `codragraph-security-audit` | "审计认证绕过" "未验证的输入路径" |
| `codragraph-supply-chain-audit` | "依赖风险审计" "去掉 X 会怎样？" |
| `codragraph-config-audit` | "审计环境变量" "未使用的配置项" |

#### 📊 质量与性能

| 技能 | 触发场景 |
|------|----------|
| `codragraph-test-coverage` | "哪些代码路径没有测试？" |
| `codragraph-perf-hotspots` | "性能热点在哪些函数？" |
| `codragraph-observability-coverage` | "哪些函数没有日志/指标？" |

#### 📋 PR 与审查

| 技能 | 触发场景 |
|------|----------|
| `codragraph-pr-review` | "审查这个 PR" "#42 改了什么？" |
| `codragraph-data-lineage` | "这个字段的数据从哪来？" |
| `codragraph-sql-tracing` | "这个 SQL 在哪定义的？谁在调用？" |
| `codragraph-notebook-context` | "这些 Jupyter notebook 做了什么？" |
| `codragraph-project-switcher` | "切换到仓库 X" "我有多少个项目？" |

### 使用示例

```
# 分析变更影响（对 Claude 说）
"分析一下我当前改动的影响范围"

# 代码库探索（对 Claude 说）
"帮我理解这个项目的认证流程是怎么实现的"

# 安全审查（对 Claude 说）
"审计一下有没有未验证的用户输入路径"

# 重构（对 Claude 说）
"把 OldPaymentService 重命名为 LegacyPaymentGateway，安全地更新所有引用"
```

---

## 6. 协同使用场景

### 场景一：新功能开发

| 阶段 | 使用工具 | 做什么 |
|------|----------|--------|
| 需求探索 | **Superpowers** brainstorming | 澄清需求，探索方案 |
| 方案设计 | **Superpowers** writing-plans | 编写实现计划 |
| CEO 审查 | **Gstack** plan-ceo-review | 从产品视角审查完整性 |
| 架构审查 | **Gstack** plan-eng-review | 从工程视角审查架构 |
| 环境准备 | **Superpowers** using-git-worktrees | 创建隔离开发分支 |
| 代码实现 | **Superpowers** TDD | RED → GREEN → REFACTOR |
| 影响分析 | **CodraGraph** impact-analysis | 确认修改不破坏其他功能 |
| 代码审查 | **Superpowers** requesting-code-review | 请求全面代码审查 |
| 发布 | **Gstack** ship | 同步、测试、推送、创建 PR |
| 验证 | **Superpowers** verification-before-completion | 最终验证确认 |

### 场景二：Bug 修复

| 阶段 | 使用工具 | 做什么 |
|------|----------|--------|
| 排查 | **Superpowers** systematic-debugging | 四阶段系统化调试 |
| 深度调查 | **Gstack** investigate | 根因追踪 |
| 二分定位 | **CodraGraph** git-bisect | 定位引入 bug 的 commit |
| 追踪调用链 | **CodraGraph** debugging | 追溯 bug 的完整调用路径 |
| 修复实现 | **Superpowers** TDD | 先写失败测试，再修复 |
| 安全保护 | **Gstack** guard | 确保修复不波及其他模块 |

### 场景三：代码重构

| 阶段 | 使用工具 | 做什么 |
|------|----------|--------|
| 影响分析 | **CodraGraph** impact-analysis | 确定重构影响范围 |
| 死代码清理 | **CodraGraph** dead-code | 找出可删除的无用代码 |
| 安全重构 | **CodraGraph** refactoring | 多文件协同重构 |
| 测试覆盖 | **CodraGraph** test-coverage | 确认重构后的测试覆盖 |
| 代码审查 | **Gstack** review | 偏执型结构审计 |
| 发布 | **Gstack** ship | 安全发布重构变更 |

### 场景四：日常 Git 操作

| 操作 | 使用工具 |
|------|----------|
| 并行开发多个功能 | **CodraGraph** git-worktree |
| 整理 commit 历史 | **CodraGraph** git-history-rewrite |
| 误操作恢复 | **CodraGraph** git-recovery |
| 强制推送安全检查 | **CodraGraph** git-force-push |
| CI 失败排查 | **CodraGraph** gh-actions-debug |
| 创建和管理 PR | **CodraGraph** gh-pr-workflow |

---

## 快速参考卡片

### 一句话总结

| 插件 | 一句话 |
|------|--------|
| **RTK** | 压缩命令输出，节省 60-90% token |
| **Git/GitHub** | 全流程版本控制 + CI/CD 集成 |
| **Superpowers** | 严格开发纪律：规划 → TDD → 审查 → 验证 |
| **Gstack** | 角色化 AI 工程团队（CEO/工程师/QA/发布） |
| **CodraGraph** | 代码图谱智能：影响分析 + 调试 + 重构 |

### 常用触发词

| 需求 | 对 Claude 说 |
|------|-------------|
| 理解代码 | "帮我理解 X 的实现" |
| 影响分析 | "改 X 会破坏什么？" |
| 调试 | "为什么 X 失败了？" |
| 重构 | "把 X 重命名为 Y" |
| 审查 | "审查这次的改动" |
| 发布 | "准备发布" |
| 安全 | "开启 guard 模式" |
| TDD | "用 TDD 实现 X" |

---

> 安装日期: 2026-06-12
> Claude Code 版本: 2.1.174
