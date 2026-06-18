# Claude Code CLI 核心参数参考

## 🟢 日常最常用

| 参数 | 作用 |
|------|------|
| `-p "<query>"` | 非交互模式，执行一次查询就退出 |
| `-c` / `--continue` | 恢复当前目录最近一次对话 |
| `-r <id>` | 按 ID 或名称恢复指定会话 |
| `-n <name>` | 给会话起个名字，方便后续 `-r` 找回 |
| `--model <model>` | 指定模型：`opus` / `sonnet` / `haiku` |
| `--max-turns <n>` | 限制 agent 循环轮数（仅 -p 模式） |
| `--max-budget-usd <amount>` | 限制 API 花费上限（仅 -p 模式） |

## 🟡 权限控制

| 参数 | 作用 |
|------|------|
| `--permission-mode <mode>` | 权限模式：`default` / `acceptEdits` / `plan` / `auto` / `bypassPermissions` |
| `--dangerously-skip-permissions` | 跳过所有权限提示（CI 环境常用） |
| `--allowedTools <patterns>` | 白名单工具，无需确认即可执行 |
| `--disallowedTools <patterns>` | 黑名单工具 |

## 🔵 目录 & 工作区

| 参数 | 作用 |
|------|------|
| `--cwd <path>` | 指定工作目录 |
| `--add-dir <dirs>` | 添加额外目录供 Claude 读写 |
| `-w <name>` / `--worktree` | 在隔离的 git worktree 中启动 |
| `--output-format <format>` | 输出格式：`text` / `json` / `stream-json` |
| `--json-schema <schema>` | 指定 JSON Schema 获得结构化输出（-p 模式） |

## 🟠 MCP

| 参数 | 作用 |
|------|------|
| `--mcp-config <paths>` | 加载 MCP 服务器配置 |
| `--strict-mcp-config` | 只用指定的 MCP，忽略其他所有 MCP 配置 |

## 🔴 调试 & 系统

| 参数 | 作用 |
|------|------|
| `--debug` | 调试模式 |
| `--verbose` | 显示完整的逐轮输出 |
| `--version` / `-v` | 版本号 |
| `--system-prompt <text>` | 替换系统提示词 |
| `--append-system-prompt <text>` | 追加到系统提示词末尾 |
| `--bare` | 极简启动，跳过钩子/技能/插件/MCP |
| `--safe-mode` | 安全模式，禁用所有自定义配置排查故障 |

## ⚪ 其他

| 参数 | 作用 |
|------|------|
| `--bg` | 后台 agent 模式启动 |
| `--agent <name>` | 指定 agent |
| `--agents <json>` | 动态定义自定义子代理 |
| `--settings <path>` | 加载自定义 settings.json |
| `--ide` | 自动连接 IDE |
| `--no-session-persistence` | 不保存会话到磁盘 |

## 子命令

| 命令 | 作用 |
|------|------|
| `claude update` | 更新 Claude Code |
| `claude auth login/logout/status` | 账号认证管理 |
| `claude mcp` | MCP 服务器管理 |
| `claude plugin` | 插件管理 |
| `claude stop <id>` | 停止后台会话 |
| `claude attach <id>` | 附加到后台会话终端 |

---

> 生成日期: 2026-06-11
