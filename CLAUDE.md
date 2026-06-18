# Project: RBT — 留学生地图服务平台

## What this is
面向悉尼留学生的地图服务平台。留学生可以直接在地图上查找美食地址、浏览真实评价，也可以在平台上发布或接单搬家、维修电脑等生活服务。后端埋点追踪用户行为和商家点击量，积累数据后用于商业合作谈判。

## Target platforms
- 🌐 Web（React SPA）— 主要入口
- 📱 PWA — 可安装到手机桌面，离线可用，推送通知

## Core features
- 🗺️ **美食地图** — Mapbox 交互地图，悉尼美食地点标注，留学生真实评价
- 🛠️ **服务市场** — 发布需求 / 接单（搬家、维修电脑、接机等）
- 👤 **用户系统** — 留学生身份认证、评价记录
- 📊 **数据看板** — 用户使用次数、商家点击量统计，可视化图表，支撑商业合作

## Tech stack
- Backend: FastAPI + PostgreSQL
- Frontend: React + Vite
- Map: Mapbox GL JS
- Charts: ECharts / Chart.js
- Deploy: Cloudflare Pages + Workers

## Data tracking
- 用户维度：DAU、使用次数、活跃时段
- 商家维度：详情页点击量、评价数、收藏数
- 埋点方案：后端 API 层记录 + 前端事件上报
- 数据看板：`/admin/dashboard` 独立页面，仅内部访问

## Project structure
- `backend/` - FastAPI app
- `frontend/` - React app
- `docs/` - shared docs
- `模板/` - templates
- `weekly-report/` - 周报

## Commands
- `make dev` - run all locally
- `make test` - run all tests
- `make deploy` - deploy to Cloudflare

## Conventions
- Conventional Commits (feat:, fix:, docs:, chore:)
- All endpoints require tests
- PRs need green CI before merge
