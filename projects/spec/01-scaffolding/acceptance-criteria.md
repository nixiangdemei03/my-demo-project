# Issue 01: Project Scaffolding — FastAPI + React

**Label**: `phase-1` `P0`

## 验收标准

- [ ] `projects/apex-app/` 目录结构建立
  ```
  apex-app/
  ├── backend/
  │   ├── main.py
  │   ├── requirements.txt
  │   └── app/
  ├── frontend/
  │   ├── index.html
  │   ├── package.json
  │   ├── vite.config.js
  │   └── src/
  ├── data/
  ├── scripts/
  └── Makefile
  ```
- [ ] FastAPI `/api/hello` 端点返回 `{"msg":"hello"}`
- [ ] React 前端调用 `/api/hello` 并在页面显示返回值
- [ ] Vite proxy 配置 `/api` → `localhost:8000`
- [ ] `Makefile` 含 `make dev`（同时启动 uvicorn + vite）
- [ ] `vite build` 无错误
- [ ] `.gitignore` 含 `node_modules/` `__pycache__/` `*.pyc` `.env` `venv/` `dist/` `.claude/`
- [ ] `curl localhost:5173/api/hello` → `{"msg":"hello"}`
