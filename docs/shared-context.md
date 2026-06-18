# RBT - Shared Context (Codex & Claude)

## 项目定位
RBT 是一个综合性项目，为用户提供前后端一体化解决方案，面向开发者团队。

## 技术栈
- Backend: FastAPI + PostgreSQL
- Frontend: React + Vite
- Deploy: Cloudflare Pages + Workers

## 目录结构
```
RBT/
├── frontend/               # 前端代码
├── backend/                # 后端代码
├── docs/                   # 共享文档
├── 模板/                   # 模板文件
├── makedown/               # Markdown 文档
├── 技术使用说明文件/        # 技术使用说明文档
├── weekly-report/          # 周报文件夹
├── AGENT.md                # Agent 指令
└── CLAUDE.md               # Claude Code 入口配置
```

## 通用约定
- 使用 Conventional Commits（feat:, fix:, docs:, chore:）
- 所有 API 端点必须包含测试
- PR 合并前需通过 CI 检查
- 代码风格遵循项目已有规范，保持一致性

## 环境变量
待补充。

## 本地开发
待补充。
