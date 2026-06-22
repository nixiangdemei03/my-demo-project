# APEX v1.0 — Issues 验收标准

> 基于 `projects/spec/` 下 15 个 Issue 的验收标准汇总。按 Phase 分组。

---

## Phase 1: 基础平台

### Issue 01: Project Scaffolding — FastAPI + React

- [ ] `projects/apex-app/` 目录结构：backend/(main.py, requirements.txt, app/), frontend/(index.html, package.json, vite.config.js, src/), data/, scripts/, Makefile
- [ ] FastAPI `/api/hello` → `{"msg":"hello"}`
- [ ] React 前端调用 `/api/hello` 并显示返回值
- [ ] Vite proxy `/api` → `localhost:8000`
- [ ] `make dev` 同时启动 uvicorn + vite
- [ ] `vite build` 无错误
- [ ] `.gitignore` 含 `node_modules/` `__pycache__/` `*.pyc` `.env` `venv/` `dist/` `.claude/`
- [ ] `curl localhost:5173/api/hello` → `{"msg":"hello"}`

### Issue 02: PostgreSQL + Database Models

- [ ] PostgreSQL 数据库创建，连接串写入 `backend/.env`
- [ ] SQLAlchemy 2.0 + asyncpg 异步引擎可用
- [ ] Alembic 初始化，`alembic upgrade head` 成功
- [ ] 5 张核心表建表：users, products, categories, orders, product_vehicle_fits（字段完整）
- [ ] `backend/.env.example` 含 `DATABASE_URL` 模板
- [ ] 连接失败有明确错误日志

### Issue 03: User Registration & Login API (JWT)

- [ ] `POST /api/auth/register` — 注册（bcrypt 哈希，min 8 位字母+数字），重复 email→400，缺字段→400
- [ ] `POST /api/auth/login` — 返回 access_token + refresh_token + user，密码错→401，未验证→403
- [ ] `POST /api/auth/refresh` — 刷新 token
- [ ] `GET /api/auth/me` — JWT 鉴权，无 token→401
- [ ] `PUT /api/auth/me` — 更新个人信息
- [ ] Access Token 30min / Refresh Token 7d 过期
- [ ] SendGrid 验证邮件，`GET /api/auth/verify?token=xxx` → verified=true
- [ ] pytest 覆盖：注册成功、重复注册、登录成功、密码错误、Token 过期、权限拒绝

### Issue 04: Product CRUD API + Image Upload

- [ ] `POST /api/products` — supplier 鉴权，必填 name_zh/category_id/sell_price，自动绑定 supplier_id
- [ ] `GET /api/products` — 公开，分页+筛选（category/price/supplier）
- [ ] `GET /api/products/:id` — 详情含图片+供应商+车型适配
- [ ] `PUT /api/products/:id` — 仅本人，部分更新，非本人→403
- [ ] `DELETE /api/products/:id` — 仅本人，软删除
- [ ] `POST /api/products/:id/images` — jpg/png/webp, max 5MB, Cloudflare R2
- [ ] `DELETE /api/products/:id/images/:img_id`
- [ ] 创建产品时可绑定 vehicle_fits 数组
- [ ] pytest 覆盖：CRUD、权限拒绝、图片类型校验

### Issue 05: Product Search — VIN / OEM / Vehicle Browse

- [ ] `GET /api/search?q=` — 全文搜索 name_zh/name_en/oem_number，支持组合筛选，空结果→total=0
- [ ] `GET /api/search?oem=` — 精确匹配，大小写不敏感，支持部分匹配
- [ ] `POST /api/search/vin` — vin_pattern 前缀匹配，命中→vehicle+products，未命中→matched=false
- [ ] `GET /api/search?make=&model=&year=` — 车型浏览
- [ ] `GET /api/categories` — 层级类别树（name_zh/name_en/children）
- [ ] pytest 覆盖：中文搜索、OEM 精确/部分、VIN 命中/未命中、空结果

### Issue 08: Supplier Page + Warranty Policy

- [ ] `GET /api/suppliers/:id` — 返回公司信息、Logo、资质证书缩略图、产品数、主营品牌
- [ ] 注册时接受额外字段：Logo、公司介绍、主营品牌、资质证书、联系方式
- [ ] 人工审核：管理员查看执照/实店照片/销售许可证 → Approve/Reject/Request More Info
- [ ] 产品表单含 warranty_period 和 return_policy 字段
- [ ] 产品详情页展示保修/退换政策
- [ ] pytest 覆盖

### Issue 09: Frontend — Homepage, Catalog & Detail Pages

- [ ] 首页 `/` — 三条搜索入口（VIN/OEM/车型浏览）、热门类别入口
- [ ] 搜索结果 `/search` — 列表/网格切换、左侧筛选、分页、URL 参数同步
- [ ] 产品详情 `/products/:id` — 多图轮播、规格表、车型适配、供应商卡片、保修政策、"发送询问"按钮
- [ ] 供应商详情 `/suppliers/:id` — Logo、介绍、品牌标签、证书、产品列表
- [ ] 登录 `/auth/login` + 注册 `/auth/register` — 表单验证、错误提示
- [ ] PC + 移动端响应式

### Issue 10: Frontend — Supplier Dashboard

- [ ] 工作台 `/dashboard` — 产品数/待处理订单/本月销售额概览
- [ ] 产品管理 `/dashboard/products` — 列表、添加表单（含图片拖拽、车型绑定、保修字段）、编辑（预填充）、下架
- [ ] 订单管理 `/dashboard/orders` — 列表、详情（采购商信息+产品+询问内容）、确认/拒绝、发货操作
- [ ] 供应商主页 `/dashboard/profile` — 模板表单 + 实时预览
- [ ] 询盘 `/dashboard/inquiries` — 收件箱、详情+回复
- [ ] PC + 移动端响应式

---

## Phase 2: 订单与货运

### Issue 06: Order Management API

- [ ] `POST /api/orders` — buyer 鉴权，自动计算 total_price，生成 APEX-YYYYMMDD-NNNN，初始 pending
- [ ] `GET /api/orders` — 按角色过滤（buyer 看自己/supplier 看自己产品/admin 看全部）
- [ ] `GET /api/orders/:id` — 详情含 timeline + shipment，非关联方→403
- [ ] `PATCH /api/orders/:id/status` — 合法流转：pending→confirmed→paid→shipped→delivered，任意→cancelled，非法→400
- [ ] 状态变更写入 order_timeline
- [ ] 24h 未付自动取消，前端显示倒计时 timer
- [ ] pytest 覆盖

### Issue 07: Freight & Shipment Tracking

- [ ] `GET/POST/PUT/DELETE /api/freight-companies` — admin CRUD 货运公司
- [ ] `POST /api/orders/:id/ship` — supplier 发货（freight_company_id + tracking_number）
- [ ] `GET /api/shipments/:id/tracking` — tracking_events 倒序
- [ ] `POST /api/shipments/:id/events` — supplier/admin 手动添加追踪事件
- [ ] shipment 状态：in_transit → delivered/exception
- [ ] pytest 覆盖

### Issue 11: Frontend — Buyer Dashboard

- [ ] 工作台 `/dashboard` — 订单按状态统计概览
- [ ] 订单列表 `/dashboard/orders` — 状态标签颜色区分、分页
- [ ] 订单详情 `/dashboard/orders/:id` — 产品信息、供应商信息、时间线、货运追踪事件、支付状态、确认收货按钮
- [ ] 支付页 `/checkout/:orderId` — 订单摘要、支付方式选择（PayPal/Stripe/支付宝）、成败处理
- [ ] 询盘 `/dashboard/inquiries` — 已发送列表、回复详情
- [ ] 个人资料 `/dashboard/profile`
- [ ] PC + 移动端响应式

### Issue 13: Platform Payment & Monthly Settlement

- [ ] `POST /api/payments/checkout` — buyer 鉴权，调用支付网关，返回跳转 URL（v1.0 模拟）
- [ ] `POST /api/payments/webhook` — 支付网关回调，验证签名，更新 order.payment_status=paid
- [ ] `GET /api/payments` — 支付流水列表
- [ ] 每月 1 日自动结算：Σ delivered 订单 - 退款扣减 = 结算基数，前 40 供应商抽 3%，后续 7%
- [ ] 结算单含订单明细、退款明细、抽成计算、到账金额
- [ ] 供应商可查看/下载结算单
- [ ] pytest + pytest 覆盖

### Issue 14: Refund & Return Flow

- [ ] `POST /api/refunds` — buyer 发起退款（order_id + reason + 可选图片）
- [ ] `PATCH /api/refunds/:id` — supplier 处理：approve / reject / request_inspection
- [ ] `GET /api/refunds` — 按角色过滤
- [ ] orders.refund_status 流转：none→requested→approved→completed / none→requested→rejected
- [ ] 退款金额从当月结算扣除
- [ ] 协商失败可申请平台客服介入
- [ ] v1.0 退款为模拟 API

### Issue 15: Inquiry → Order Conversion

- [ ] `POST /api/inquiries/:id/convert-to-order` — 仅 buyer + inquiry 类型可转单，自动带入 product_id/quantity/oem/vin
- [ ] `PATCH /api/inquiries/:id/cancel` — buyer/supplier 均可取消，状态变 cancelled，双方保留记录
- [ ] 前端询问单界面含「下单」和「取消」两个按钮
- [ ] 取消后平台推荐同类产品
- [ ] inquiries 表完整 schema（type: message/inquiry, status: open/replied/converted/cancelled）
- [ ] pytest 覆盖

---

## Phase 3: 完善

### Issue 12: Admin Dashboard & Management

- [ ] 控制台 `/admin` — 统计卡片（供应商/产品/订单/GMV）、待审核队列、最近订单
- [ ] 用户管理 `/admin/users` — 列表、审核队列（查看资质文件→通过/拒绝附原因）
- [ ] 产品管理 `/admin/products` — 全局列表、违规下架
- [ ] 订单管理 `/admin/orders` — 全局视图
- [ ] 类别管理 `/admin/categories` — CRUD 类别树
- [ ] 货运公司管理 `/admin/freight` — CRUD
- [ ] 结算管理 `/admin/settlements` — 结算单列表/详情、手动触发结算

---

## 优先级总览

| Phase | Issues | P0 | P1 |
|:--:|------|:--:|:--:|
| 1 | 01,02,03,04,05,08,09,10 | 8 | — |
| 2 | 06,07,11,13,14,15 | 6 | — |
| 3 | 12 | — | 1 |

**共 15 个 Issue，P0 14 个，P1 1 个。**
