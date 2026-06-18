# Project: RBT v0 — 留学生地图服务平台

## 项目目标

RBT 是一个面向悉尼留学生的地图服务平台，旨在帮助留学生更好地融入当地生活。项目的核心目标是：

1. **美食地图**：提供悉尼地区的美食地点标注与导航，留学生可直接在地图上查找餐厅、咖啡馆等餐饮场所，并浏览其他留学生的真实评价与评分。
2. **服务市场**：搭建一个生活服务供需匹配平台，留学生可以在平台上发布需求（如搬家、维修电脑、接机等），也可以浏览已有服务并接单，实现留学生之间的互助。
3. **社区归属感**：通过真实评价与服务互助，降低留学生在异国他乡的信息壁垒，构建可信的留学生本地生活社区。

## 项目工作流

### 周报流程
每周五按 `模板/report.md` 模板撰写周报，存放路径 `weekly-report/weekXX/report.md`（XX 为周数，如 week01）。写完后执行：
```bash
git add weekly-report/weekXX/
git commit -m "docs: add weekXX report"
git push
```

### 日常开发流程
1. **需求确认**：所有新功能需先在 `docs/` 目录下创建对应的 PRD 或设计文档，明确功能边界与验收标准。
2. **分支管理**：基于 `main` 分支创建功能分支，命名遵循 `feat/<功能名>` 或 `fix/<问题描述>` 格式。
3. **后端开发**：在 `backend/` 中实现 API 接口，遵循 FastAPI 最佳实践，每个端点必须包含单元测试。
4. **前端开发**：在 `frontend/` 中实现页面与组件，遵循 React + Vite 技术栈，确保与后端 API 的数据契约一致。
5. **联调测试**：使用 `make dev` 同时启动前后端进行本地联调，确认功能正常运行。
6. **代码审查**：PR 提交前需自查代码质量，确保 CI 流水线全部通过后方可合并至 `main` 分支。
7. **部署上线**：合并后使用 `make deploy` 将前端部署至 Cloudflare Pages，后端部署至 Cloudflare Workers。

### 数据与接口规范
- 所有 API 接口需返回标准 JSON 格式，包含明确的成功/错误状态码。
- 数据库变更需同步更新 `docs/` 中的 Schema 文档。
- 地图相关数据（地点坐标、评价内容）需经过内容审核后方可发布。

## 项目结构
- `backend/` - FastAPI 后端应用
- `frontend/` - React 前端应用
- `docs/` - 共享文档、PRD、设计笔记
- `makedown/` - Markdown 项目文档
- `模板/` - 模板文件
- `技术使用说明文件/` - 技术说明文档

## 技术栈
- Backend: FastAPI + PostgreSQL
- Frontend: React + Vite
- Map: Leaflet / Mapbox
- Deploy: Cloudflare Pages + Workers

## 命令
- `make dev` - 本地同时启动前后端
- `make test` - 运行全部测试
- `make deploy` - 部署至 Cloudflare

## 开发约定
- 使用 Conventional Commits（feat:, fix:, docs:, chore:, refactor:）
- 所有 API 端点必须包含测试用例
- PR 合并前需 CI 绿灯
- 代码注释使用中文，变量与函数命名使用英文

## 文件修改边界

**严格限制**：所有文件创建、修改、删除操作仅限在当前 RBT 项目目录（`D:\claude-code-demo\RBT\`）内进行。不允许修改以下范围之外的任何文件或目录：

- ✅ 允许：`D:\claude-code-demo\RBT\` 下所有子目录与文件
- ✅ 允许：RBT 项目关联的 Git 仓库操作（commit、push、branch 等）
- ❌ 禁止：修改系统文件、用户目录下其他项目文件、全局配置文件

Git 仓库操作同样仅限于 RBT 项目的本地仓库，不得对非本项目的 Git 仓库执行任何操作。

## 当前阶段
V0 — 项目脚手架搭建与核心功能规划阶段。
