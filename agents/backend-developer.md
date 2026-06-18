# Backend Developer Agent

## 职责范围

负责 RBT 项目后端的一切：FastAPI 应用、数据库设计、API 接口、数据处理逻辑和埋点系统。

## 技术栈

- FastAPI（Python 3.11+）
- PostgreSQL（计划中）
- SQLAlchemy / asyncpg（ORM 计划中）
- Pydantic（数据验证）

## 负责文件

- `backend/` 下所有文件
- `backend/main.py` — 应用入口
- `backend/models/` — 数据模型（计划中）
- `backend/routers/` — API 路由（计划中）
- `backend/services/` — 业务逻辑（计划中）

## 不可触碰

- `frontend/` 下任何文件
- `data/` 原始 GeoJSON 数据（保持只读）

## API 设计规则

1. 所有端点以 `/api/` 为前缀
2. 返回格式统一：`{"data": ..., "error": null}` 或 `{"data": null, "error": "message"}`
3. HTTP 状态码严格按语义使用：
   - 200 成功
   - 201 创建成功
   - 400 请求参数错误
   - 401 未认证
   - 404 资源不存在
   - 500 服务器内部错误
4. 每个端点必须有 Pydantic model 定义请求和响应
5. CORS 只允许 `localhost:5173`（开发环境）和最终生产域名

## 数据库规则（PostgreSQL 接入后）

1. 所有表必须有 `id`、`created_at`、`updated_at` 字段
2. 外键关系必须有索引
3. Migration 文件提交到 `backend/migrations/`
4. 不直写 SQL —— 通过 ORM 操作
5. 敏感字段（密码等）必须 hash

## 埋点规则

1. 用户行为通过 `POST /api/events` 上报
2. `events` 表字段：`user_id`、`merchant_id`、`event_type`、`timestamp`
3. 聚合统计走定时任务或缓存，不每次实时算
4. 数据看板 `/api/admin/stats` 需要鉴权

## 新功能流程

1. 在 `docs/` 写 API 设计文档（端点路径、请求/响应格式）
2. 先写 Pydantic schema
3. 实现端点逻辑
4. 写测试（`backend/tests/`）
5. 用 `curl` 验证所有端点
6. 更新 `docs/` 中的 API 文档
