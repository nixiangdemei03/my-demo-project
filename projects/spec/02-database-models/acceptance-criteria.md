# Issue 02: PostgreSQL + Database Models

**Labels**: `feat` `p0` `backend` `infra` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

APEX 需要持久化存储。按 Data Model（`docs/03-data-model.md`）建 5 张核心表 + Alembic 迁移，支撑用户注册、产品上架、订单管理。对应 PRD §3 用户故事 SUP-01/02、BUY-01/05。

## 用户故事

作为开发者，我想有版本化的数据库 schema，以便所有 API 都能读写持久化数据，且 schema 变更有迹可循。

## 任务清单

- [ ] PostgreSQL 数据库创建，连接串写入 `backend/.env`
- [ ] SQLAlchemy 2.0 + asyncpg 异步引擎配置
- [ ] 定义 5 张核心表 ORM 模型（users, products, categories, orders, product_vehicle_fits）
- [ ] Alembic 初始化 + 首次 migration
- [ ] `alembic upgrade head` 建表成功
- [ ] 写 `backend/.env.example` 含 `DATABASE_URL` 模板
- [ ] 连接失败时输出明确错误日志

## 验收标准

- `alembic upgrade head` 后在 PostgreSQL 中可查到 5 张表
- users.email 含 UNIQUE 约束
- products.supplier_id → users.id 外键生效
- categories.parent_id → categories.id 自引用外键生效
- `backend/.env.example` 含 `DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/apex`

## 相关

- PRD §3：SUP-01/02、BUY-01/05 | 数据模型：`docs/03-data-model.md` | 依赖：Issue 01
