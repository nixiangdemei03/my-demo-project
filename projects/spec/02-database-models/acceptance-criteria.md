# Issue 02: PostgreSQL + Database Models

**Label**: `phase-1` `P0`

## 验收标准

- [ ] PostgreSQL 数据库创建完成，连接串写入 `backend/.env`
- [ ] SQLAlchemy 2.0 + asyncpg 配置，异步引擎可用
- [ ] Alembic 初始化，首次 `alembic upgrade head` 成功
- [ ] 5 张核心表建表通过：
  - `users`（id UUID PK, email UNIQUE, password_hash, role, company_name, contact_name, phone, country, language, verified, created_at, updated_at）
  - `products`（id UUID PK, supplier_id FK→users, category_id FK→categories, name_zh, name_en, oem_number, description_zh, description_en, original_price DECIMAL, sell_price DECIMAL, moq, stock, specs JSONB, status, created_at, updated_at）
  - `categories`（id UUID PK, name_zh, name_en, parent_id FK→categories, sort_order）
  - `orders`（id UUID PK, order_number UNIQUE, buyer_id FK→users, supplier_id FK→users, product_id FK→products, quantity, unit_price, total_price, currency, status, payment_status, cancel_reason, notes, created_at, updated_at）
  - `product_vehicle_fits`（id UUID PK, product_id FK→products, make, model, year_start, year_end, engine, vin_pattern）
- [ ] `backend/.env.example` 含 `DATABASE_URL` 模板
- [ ] 数据库连接失败时有明确错误日志
