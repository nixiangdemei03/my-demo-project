# RBT — 悉尼留学生地图服务平台

> 一张地图，连接悉尼留学生的美食与生活服务。

## 目标用户

在悉尼生活的中国留学生，需要快速找到可靠的美食去处和生活服务（搬家、维修、接机等），并信任来自留学生社区的真实评价。

## v1.0 核心功能

| 功能 | 描述 |
|------|------|
| 🗺️ **美食地图** | Mapbox 交互地图，悉尼美食地点标注，按菜系/评分/距离筛选，留学生真实评价 |
| 🛠️ **服务市场** | 发布生活服务需求（搬家、维修电脑、接机等），或浏览已发布的服务并接单 |
| 👤 **用户社区** | 留学生身份认证、个人评价记录、信用评分体系 |
| 📊 **数据看板** | 用户使用频次、商家点击量埋点统计，ECharts 可视化，积累数据用于商家合作谈判 |

## 技术栈

- **Backend**: FastAPI + PostgreSQL
- **Frontend**: React + Vite
- **Map**: Mapbox GL JS
- **Charts**: ECharts
- **Deploy**: Cloudflare Pages + Workers

## 快速开始

```bash
# 克隆仓库
git clone git@github.com:nixiangdemei03/my-demo-project.git
cd my-demo-project

# 安装依赖
cd backend && pip install -r requirements.txt
cd ../frontend && npm install
cd ..

# 本地运行
make dev

# 运行测试
make test

# 部署
make deploy
```

## 项目结构

```
RBT/
├── backend/          FastAPI 后端
├── frontend/         React 前端
├── docs/             共享文档
├── makedown/         Markdown 文档
├── 模板/             模板文件
└── .github/          CI 配置（计划中）
```

## 开发约定

- Conventional Commits（`feat:`, `fix:`, `docs:`, `chore:`）
- 所有 API 端点需包含测试
- PR 合并前需 CI 通过

## 版本

**v0** — 项目脚手架搭建与核心功能规划阶段。

## 许可

MIT
