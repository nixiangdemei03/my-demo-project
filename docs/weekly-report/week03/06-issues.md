# APEX v1.0 — GitHub Issues

> 基于 `docs/01-prd.md` 拆分。每个 Issue 含验收标准，可直接用于 GitHub。

---

## Issue 1: Project Scaffolding — FastAPI + React hello-world

**Label**: `phase-1` `P0`

### 验收标准
- [ ] `projects/apex-app/` 目录结构建立（backend/ + frontend/ + data/ + scripts/）
- [ ] FastAPI `/api/hello` 端点返回 `{"msg":"hello"}`
- [ ] React 前端调用 `/api/hello` 并显示返回值
- [ ] `Makefile` 含 `make dev`（同时启动前后端）
- [ ] `vite build` 无错误
- [ ] `.gitignore` 含 node_modules/、__pycache__/、.env、dist/

---

## Issue 2: PostgreSQL + Database Models

**Label**: `phase-1` `P0`

### 验收标准
- [ ] PostgreSQL 数据库创建完成
- [ ] SQLAlchemy 2.0 + asyncpg 配置
- [ ] Alembic 初始化并创建首次 migration
- [ ] 以下 5 张核心表建表成功：
  - `users`（id, email, password_hash, role, company_name, contact_name, verified）
  - `products`（id, supplier_id, category_id, name_zh, name_en, oem_number, sell_price, original_price, specs, stock）
  - `categories`（id, name_zh, name_en, parent_id）
  - `orders`（id, order_number, buyer_id, supplier_id, product_id, quantity, total_price, status, payment_status）
  - `product_vehicle_fits`（id, product_id, make, model, year_start, year_end, engine, vin_pattern）
- [ ] `backend/.env.example` 含 `DATABASE_URL` 模板

---

## Issue 3: User Registration & Login API (JWT Auth)

**Label**: `phase-1` `P0`

### 验收标准
- [ ] `POST /api/auth/register` — 注册（email + password + role + company_name + contact_name）
  - 密码 bcrypt 哈希，最小 8 位，要求字母+数字
  - 返回 201 + 用户信息（不含 password_hash）
  - 重复 email 返回 400
- [ ] `POST /api/auth/login` — 登录（email + password）
  - 返回 Access Token（30min）+ Refresh Token（7d）
  - 密码错误返回 401
- [ ] `POST /api/auth/refresh` — 刷新令牌
- [ ] `GET /api/auth/me` — 需要 JWT，返回当前用户信息
- [ ] `PUT /api/auth/me` — 更新个人信息
- [ ] 邮箱验证邮件（SendGrid）：注册后发送，点击链接激活账号
- [ ] 所有端点测试通过（pytest）

---

## Issue 4: Product CRUD API + Image Upload

**Label**: `phase-1` `P0`

### 验收标准
- [ ] `POST /api/products` — 创建产品（supplier 鉴权）
  - 必填：name_zh、category_id、sell_price
  - 可选：name_en、oem_number、original_price、description、specs、stock、moq
  - 自动生成 `created_at`、`updated_at`
- [ ] `GET /api/products` — 产品列表（分页 + 筛选）
  - 支持 `?q=&category_id=&price_min=&price_max=&supplier_id=&page=&page_size=`
- [ ] `GET /api/products/:id` — 产品详情（含图片、供应商信息、车型适配列表）
- [ ] `PUT /api/products/:id` — 更新产品（仅本供应商）
- [ ] `DELETE /api/products/:id` — 下架产品（仅本供应商，软删除）
- [ ] `POST /api/products/:id/images` — 上传图片至 Cloudflare R2
  - 白名单：jpg/png/webp，最大 5MB
  - 返回图片 URL
- [ ] `DELETE /api/products/:id/images/:img_id` — 删除图片
- [ ] 产品创建时可绑定 `product_vehicle_fits`（make/model/year_start/year_end/engine/vin_pattern）
- [ ] 所有端点测试通过

---

## Issue 5: Product Search — VIN / OEM / Vehicle Browse

**Label**: `phase-1` `P0`

### 验收标准
- [ ] `GET /api/search?q=&oem=&make=&model=&year=&category_id=` — 全文搜索
  - 搜索范围：name_zh、name_en、oem_number
  - 支持车型参数组合过滤
- [ ] `POST /api/search/vin` — VIN 搜索
  - 入参：`{"vin": "JTE..."}`
  - 平台用 vin_pattern 前缀匹配 product_vehicle_fits
  - 命中 → 返回 vehicle info + 适配配件列表
  - 未命中 → 返回 `{"matched": false, "vin": "..."}`（后续透传询问订单）
- [ ] `GET /api/categories` — 类别树（支持 parent_id 层级）
- [ ] `GET /api/search?category_id=X&make=Toyota&model=Hilux` — 车型浏览模式
- [ ] 分页结果格式统一

---

## Issue 6: Order Management API (Inquiry → Payment → Status)

**Label**: `phase-2` `P0`

### 验收标准
- [ ] `POST /api/orders` — 创建正式订单（buyer 鉴权）
  - 必填：product_id、quantity
  - 自动计算 total_price = unit_price × quantity
  - 生成 order_number（APEX-YYYYMMDD-NNNN）
  - 初始状态：pending
- [ ] `GET /api/orders` — 订单列表（按角色过滤）
  - buyer 只能看自己的订单
  - supplier 只能看自己产品的订单
- [ ] `GET /api/orders/:id` — 订单详情（含时间线、货运信息）
- [ ] `PATCH /api/orders/:id/status` — 更新状态
  - 状态流转：pending → confirmed → paid → shipped → delivered → cancelled
- [ ] `POST /api/orders/:id/ship` — 发货（supplier）
  - 必填：freight_company_id、tracking_number
- [ ] 订单状态变更自动记录到 order_timeline
- [ ] 48h 未支付自动提醒采购商，72h 未付自动取消
- [ ] 所有端点测试通过

---

## Issue 7: Freight & Shipment Tracking

**Label**: `phase-2` `P0`

### 验收标准
- [ ] `GET /api/freight-companies` — 货运公司列表
- [ ] `POST /api/freight-companies` — 添加货运公司（admin 鉴权）
- [ ] `POST /api/orders/:id/ship` — 发货时创建 shipment 记录（关联 freight_company + tracking_number）
- [ ] `GET /api/shipments/:id/tracking` — 获取追踪事件列表
- [ ] `POST /api/shipments/:id/events` — 手动添加追踪事件（supplier/admin）
  - 字段：event、location、event_time
- [ ] 追踪事件按时间倒序排列
- [ ] 所有端点测试通过

---

## Issue 8: Supplier Page + Product Warranty Policy

**Label**: `phase-1` `P0`

### 验收标准
- [ ] `GET /api/suppliers/:id` — 供应商详情页数据
  - 返回：Logo、公司名、成立年份、主营品牌、公司介绍、资质证书缩略图、已上架产品数
- [ ] 供应商注册后可使用固定模板搭建主页
  - 模板字段：Logo(1张)、公司名、成立年份、主营品牌(多选)、公司介绍、资质证书(多图)、联系方式(电话+邮箱+地址)
- [ ] `POST /api/auth/register` 时上传 supplier_documents
  - OCR 提取统一社会信用代码 → 天眼查 API 匹配企业名
  - 匹配成功 → verified = true
  - 匹配失败 → verified = false，标记人工审核
- [ ] 产品创建/编辑表单含保修期、退换货政策字段
- [ ] 产品详情页对采购商展示保修/退换政策

---

## Issue 9: Frontend — Homepage, Product Catalog & Detail Pages

**Label**: `phase-1` `P0`

### 验收标准
- [ ] 首页：平台介绍 + 搜索入口（VIN/OEM/车型浏览三条路径）
- [ ] 产品目录页 `/products`
  - 列表/网格视图切换
  - 按类别、价格区间、供应商筛选
  - 搜索框（支持 OEM、关键词）
  - 分页
- [ ] 产品详情页 `/products/:id`
  - 图片轮播
  - 规格表、价格（CNY 原价 + USD 售价）、MOQ
  - 车型适配列表（product_vehicle_fits）
  - 供应商信息卡片
  - 保修/退换政策展示
  - "发送询问"按钮
- [ ] 供应商详情页 `/suppliers/:id`
- [ ] 登录页 `/auth/login` + 注册页 `/auth/register`
- [ ] 响应式布局（PC + 移动端）

---

## Issue 10: Frontend — Supplier Dashboard (Product & Order Management)

**Label**: `phase-1` `P0`

### 验收标准
- [ ] 供应商工作台 `/dashboard`
  - 概览：产品数、待处理订单数、本月销售额
- [ ] 产品管理 `/dashboard/products`
  - 产品列表（可搜索、分页）
  - 添加产品表单（含图片拖拽上传、车型适配绑定）
  - 编辑产品（预填充）
  - 下架/删除产品
- [ ] 订单管理 `/dashboard/orders`
  - 收到的询问/订单列表
  - 订单详情（采购商信息、产品信息、车型信息）
  - 确认/拒绝订单
  - 发货操作（选择货运公司+填运单号）
- [ ] 供应商主页编辑 `/dashboard/profile`
  - 模板表单（Logo、介绍、资质、联系方式）
- [ ] 询盘管理 `/dashboard/inquiries`

---

## Issue 11: Frontend — Buyer Dashboard (Orders & Tracking)

**Label**: `phase-2` `P0`

### 验收标准
- [ ] 采购商工作台 `/dashboard/orders`
  - 订单列表（状态标签：pending/confirmed/paid/shipped/delivered/cancelled）
  - 订单详情 `/dashboard/orders/:id`
    - 产品信息、供应商信息
    - 订单时间线（状态变更记录）
    - 货运追踪（tracking events 时间线）
    - 支付状态
- [ ] 询盘历史 `/dashboard/inquiries`
- [ ] 个人资料 `/dashboard/profile`

---

## Issue 12: Admin Dashboard & Management

**Label**: `phase-3` `P1`

### 验收标准
- [ ] 管理后台 `/admin`
  - 统计概览：供应商数、产品数、订单数、GMV
- [ ] 用户管理 `/admin/users`
  - 列表（可搜索、按角色/审核状态筛选）
  - 审核供应商（需人工审核的资质文件列表）
- [ ] 产品管理 `/admin/products`（全局视图，可下架违规产品）
- [ ] 订单管理 `/admin/orders`（全局视图）
- [ ] 类别管理 `/admin/categories`（CRUD 类别树）
- [ ] 货运公司管理 `/admin/freight`（CRUD）

---

## Issue 13: Platform Payment & Monthly Settlement

**Label**: `phase-2` `P0`

### 验收标准
- [ ] 平台统一收银台页面（支持 PayPal / Stripe / 支付宝国际版）
- [ ] 支付成功后订单状态自动变为 `paid`
- [ ] 支付失败/取消 → 订单保持 `unpaid`，显示原因
- [ ] 后端结算计算逻辑：
  - 月总销售额 = Σ 上月已收货订单
  - 平台抽成 = 月总销售额 × 2%
  - 供应商实际到账 = 月总销售额 × 98%
- [ ] 每月 1 日自动生成结算单（含订单明细、退款扣减、抽成金额）
- [ ] 结算单含退款处理：退货→供应商确认→从当月结算基数扣除
- [ ] 供应商可查看/下载结算单
- [ ] 手动触发结算（管理员）

---

## 优先级总览

| # | Issue | Label | Phase |
|---|-------|-------|-------|
| 1 | Scaffolding: FastAPI + React hello-world | P0 | 1 |
| 2 | PostgreSQL + Database Models | P0 | 1 |
| 3 | User Registration & Login API (JWT) | P0 | 1 |
| 4 | Product CRUD API + Image Upload | P0 | 1 |
| 5 | Product Search (VIN/OEM/Vehicle) | P0 | 1 |
| 6 | Order Management API | P0 | 2 |
| 7 | Freight & Shipment Tracking | P0 | 2 |
| 8 | Supplier Page + Warranty Policy | P0 | 1 |
| 9 | Homepage + Catalog + Detail Pages | P0 | 1 |
| 10 | Supplier Dashboard | P0 | 1 |
| 11 | Buyer Dashboard | P0 | 2 |
| 12 | Admin Dashboard | P1 | 3 |
| 13 | Payment & Settlement | P0 | 2 |
