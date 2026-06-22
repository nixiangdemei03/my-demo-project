# 05 — Git 工作流

> 阶段性成果提交和推送规范。

## 流程

```
阶段性工作完成
  → git reset HEAD（清残留 staged）
  → git add -A（全量 stage 当前文件结构）
  → git status（确认变更）
  → git commit（Conventional Commits 格式）
  → git push（正常推送 / force push 项目重置时）
```

## Commit Message 规范

```
{type}: {简短描述}

- {变更点 1}
- {变更点 2}

BREAKING: {破坏性变更说明}（如有）

Co-Authored-By: Claude <noreply@anthropic.com>
```

| type | 用法 |
|------|------|
| `feat:` | 新功能 |
| `fix:` | 修 bug |
| `docs:` | 文档 |
| `chore:` | 工程类 |
| `refactor:` | 重构 |

## Force Push 时机

仅在以下情况使用 `--force`：

- 项目完全重置（如 RBT → APEX）
- 仓库结构大规模重组后需要覆盖远程
- 确认远程无他人提交

正常日常提交用普通 `git push`。

## 常用命令

```bash
# 标准提交流程
rtk git status
git add -A
rtk git status          # 再次确认
git commit -m "..." 
git push origin main

# 覆盖式推送（项目重置/大规模重组）
git push --force origin main
```

## 经验教训

1. **git mv 残留** — 用 `git mv` 移文件后如果又手动移了，先 `git reset HEAD` 清掉再 `git add -A`
2. **CRLF 警告** — Windows 下 LF→CRLF 转换警告不影响功能，忽略
3. **提交前必须确认** — `git status` 看两次：add 前一次、add 后一次
