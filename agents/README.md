# RBT Agents

项目专用 Claude Code 子代理（Agent）定义。每个 agent 负责项目的不同模块，自动加载对应规则，确保各模块在专业边界内工作。

## 使用方式

在 Claude Code 中通过 Agent 工具调用，指定 `subagent_type` 为对应 agent 名称：

```
/frontend    — 前端开发任务
/backend     — 后端开发任务
/data        — 数据处理任务
/devops      — 部署 & CI 任务
/review      — 代码审查
```

## Agent 清单

| Agent | 文件 | 负责范围 |
|-------|------|----------|
| Frontend Developer | [frontend-developer.md](frontend-developer.md) | React / Vite / Mapbox / PWA |
| Backend Developer | [backend-developer.md](backend-developer.md) | FastAPI / PostgreSQL / API |
| Data Engineer | [data-engineer.md](data-engineer.md) | GeoJSON / KML / 数据管道 |
| DevOps Engineer | [devops-engineer.md](devops-engineer.md) | Cloudflare / CI / Makefile |
| Code Reviewer | [code-reviewer.md](code-reviewer.md) | PR Review / 代码质量 |

## 调用规则

1. **前端变更** → 始终用 frontend agent，不允许修后端文件
2. **后端变更** → 始终用 backend agent，不允许修前端文件
3. **数据文件** → 用 data agent，确保 GeoJSON 结构不被破坏
4. **跨模块任务** → 先用 architect 规划，再分派到各 agent
5. **合并前** → 必须经过 reviewer agent 审查
