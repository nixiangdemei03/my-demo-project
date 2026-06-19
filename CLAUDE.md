# Project: APEX — Auto Parts EXport Platform

## What this is
面向海外汽车配件采购商与中国供应商的 B2B 平台。供应商发布产品（原价、售价、图片、规格），采购商浏览下单，订单对接货运公司实现全程追踪。

## Target users
- 🏭 **Supplier** — 国内汽配厂/贸易商，中文优先，需要快速上架产品
- 🌍 **Buyer** — 海外汽配批发商/分销商，英文优先，需要找到高性价比货源
- 🔧 **Admin** — 平台运营，审核供应商，管理内容

## Core features (v1.0)
- 📦 **产品目录** — 分类浏览、关键词搜索、OEM 编号查询、多图展示
- 👤 **用户系统** — 双角色注册（供应商/采购商）、JWT 认证、邮箱验证
- 📋 **订单管理** — 下单→确认→发货→收货 全流程，状态时间线
- 🚢 **货运对接** — 供应商发货时选货运公司+填运单号，采购商追踪物流
- 🖼️ **图片管理** — 多图上传、排序、封面设置，存储至 Cloudflare R2

## Tech stack
- Backend: FastAPI + PostgreSQL + SQLAlchemy + Alembic
- Frontend: React + Vite + React Router v6
- Storage: Cloudflare R2 (product images)
- Auth: JWT (python-jose + passlib/bcrypt)
- Deploy: Cloudflare Pages + Workers

## Project structure
- `projects/apex-app/` — 主项目（backend + frontend）
- `agents/` — 专用 Agent 定义（backend/frontend/devops/reviewer/reporter）
- `docs/` — PRD + 技术设计 + API 文档
- `templates/` — 模板文件
- `evidence/` — 截图 + 日志
- `weekly-report/` — 周报

## Commands
- `make dev` — 同时启动前后端
- `make test` — 运行全部测试
- `make deploy` — 部署到 Cloudflare

## Conventions
- Conventional Commits (feat:, fix:, docs:, chore:)
- All endpoints require tests
- PRs need green CI before merge
- Variables/functions in English, comments in Chinese
