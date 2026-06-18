# Project: RBT — 留学生地图服务

## What this is
面向悉尼留学生的地图服务平台。留学生可以直接在地图上查找美食地址、浏览真实评价，也可以在平台上发布或接单搬家、维修电脑等生活服务。

## Core features
- 🗺️ 地图浏览 — 悉尼美食地点标注，留学生真实评价
- 🛠️ 服务市场 — 发布需求 / 接单（搬家、维修等）
- 👤 用户系统 — 留学生身份认证、评价记录

## Tech stack
- Backend: FastAPI + PostgreSQL
- Frontend: React + Vite
- Map: Leaflet / Mapbox
- Deploy: Cloudflare Pages + Workers

## Project structure
- `backend/` - FastAPI app
- `frontend/` - React app
- `docs/` - shared docs
- `模板/` - templates

## Commands
- `make dev` - run all locally
- `make test` - run all tests
- `make deploy` - deploy to Cloudflare

## Conventions
- Conventional Commits (feat:, fix:, docs:, chore:)
- All endpoints require tests
- PRs need green CI before merge
