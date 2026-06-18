# RBT 项目进度

> 最后更新：2026-06-18

## 进度总览

- 🟢 已完成
- 🟡 代码已有但未跑通验证
- ⚪ 未开始

---

## 模块进度

| 模块 | 状态 | 说明 |
|------|:----:|------|
| 🏗️ 项目脚手架 | 🟢 | `git init`、GitHub 仓库、目录结构 |
| 📄 项目文档 | 🟢 | CLAUDE.md / AGENTS.md / README.md / shared-context / makedown V0 |
| 🔧 hello-world | 🟢 | FastAPI `/api/hello` + React + Vite proxy，端到端通过 |
| 📋 工作流 | 🟢 | 开发流程 + 周报流程写入文档 |
| 📝 Week01 周报 | 🟢 | 按模板完成，已推送 |
| 📝 Week02 周报 | 🟢 | 按模板完成，已推送 |
| 🗺️ 地图 | 🟢 | Mapbox 前端完成：201 POI、搜索筛选、marker 弹窗、flyTo |
| 📊 POI 数据 | 🟢 | Google My Maps + Takeout 合并 201 条，KML→GeoJSON 工具链 |
| 🤖 Agent 体系 | 🟢 | 5 个专用 agent 定义（frontend/backend/data/devops/reviewer） |
| 👤 用户系统 | ⚪ | 注册 / 登录，未开始 |
| 🛠️ 服务市场 | ⚪ | 需求发布 / 接单，未开始 |
| 📊 数据看板 | ⚪ | 埋点方案已有，未实现 |
| 🗄️ 数据库 | ⚪ | PostgreSQL 已选型，未接入 |
| 📱 PWA | ⚪ | 已列入平台目标，未配置 |
| 🚀 部署 | ⚪ | Cloudflare 选型完成，未跑通 |

---

## GitHub 仓库

`github.com/nixiangdemei03/my-demo-project` — 12 commits，已推送到 `main`

---

## 下一步

1. 接入 PostgreSQL，创建 users + merchants + events 基础表
2. 写用户注册/登录 API
3. 把 Mapbox 前端部署到 Cloudflare Pages，获得公开 URL
