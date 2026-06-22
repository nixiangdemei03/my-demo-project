# Issue 01: Project Scaffolding — FastAPI + React hello-world

**Labels**: `feat` `p0` `backend` `frontend` `infra` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

APEX 项目从零启动。需要搭建 FastAPI + React + Vite 项目骨架，跑通前后端联调，确保开发环境可用。对应 Roadmap Phase 1 第一项。

## 用户故事

作为开发者，我想有一条命令启动前后端开发环境，以便后续所有功能都在这个骨架上迭代。

## 任务清单

- [ ] 创建 `projects/apex-app/` 完整目录结构（backend/ + frontend/ + data/ + scripts/ + Makefile）
- [ ] 后端 FastAPI 初始化，`/api/hello` 返回 `{"msg":"hello"}`
- [ ] 前端 React + Vite 初始化，调用 `/api/hello` 并显示返回值
- [ ] Vite proxy 配置 `/api` → `localhost:8000`
- [ ] 写 `Makefile`（`make dev` 同时启动 uvicorn + vite）
- [ ] 写 `.gitignore`
- [ ] `vite build` 验证无错误

## 验收标准

- `curl localhost:8000/api/hello` → 200 `{"msg":"hello"}`
- 浏览器 `localhost:5173` → 页面显示 "Backend says: hello"
- `make dev` 一条命令同时启动前后端
- `vite build` 退出码 0
- `.gitignore` 含 `node_modules/` `__pycache__/` `*.pyc` `.env` `venv/` `dist/` `.claude/`

## 相关

- Roadmap Phase 1 | 依赖：无（项目起点）
