# APEX — 数据模型

## ER 关系

```
users 1──N products              supplier owns products
users 1──N orders (buyer)        buyer places orders
users 1──N orders (supplier)     supplier receives orders
products N──1 categories
products 1──N product_images
orders 1──N order_timeline
orders 1──1 shipments
shipments N──1 freight_companies
shipments 1──N tracking_events
products 1──N inquiries
users 1──N supplier_documents
```

## 核心表

### users
| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID PK | |
| email | VARCHAR(255) UNIQUE | 登录邮箱 |
| password_hash | VARCHAR(255) | bcrypt |
| role | VARCHAR(20) | supplier / buyer / admin |
| company_name | VARCHAR(255) | 公司名称 |
| contact_name | VARCHAR(100) | 联系人 |
| phone | VARCHAR(50) | |
| country | VARCHAR(100) | 采购商所在国 |
| language | VARCHAR(10) | zh / en，默认 zh |
| verified | BOOLEAN | 供应商审核状态 |
| created_at | TIMESTAMPTZ | |
| updated_at | TIMESTAMPTZ | |

### products
| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID PK | |
| supplier_id | UUID FK → users | |
| category_id | UUID FK → categories | |
| name_zh | VARCHAR(255) | 中文名 |
| name_en | VARCHAR(255) | 英文名 |
| oem_number | VARCHAR(100) | OEM 编号 |
| description_zh | TEXT | |
| description_en | TEXT | |
| original_price | DECIMAL(12,2) | 国内原价 CNY |
| sell_price | DECIMAL(12,2) | 出口售价 USD |
| moq | INT | 最小起订量 |
| stock | INT | 库存 |
| specs | JSONB | 规格键值对 |
| status | VARCHAR(20) | active / inactive / deleted |
| created_at | TIMESTAMPTZ | |
| updated_at | TIMESTAMPTZ | |

### orders
| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID PK | |
| order_number | VARCHAR(30) UNIQUE | APEX-YYYYMMDD-NNNN |
| buyer_id | UUID FK → users | |
| supplier_id | UUID FK → users | |
| product_id | UUID FK → products | |
| quantity | INT | > 0 |
| unit_price | DECIMAL(12,2) | 下单时单价 |
| total_price | DECIMAL(12,2) | |
| currency | VARCHAR(3) | 默认 USD |
| status | VARCHAR(20) | pending→confirmed→shipped→delivered→cancelled |
| notes | TEXT | |
| created_at | TIMESTAMPTZ | |
| updated_at | TIMESTAMPTZ | |

### freight_companies
| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID PK | |
| name_zh | VARCHAR(200) | 中文名 |
| name_en | VARCHAR(200) | 英文名 |
| contact_person | VARCHAR(100) | |
| phone | VARCHAR(50) | |
| email | VARCHAR(255) | |
| shipping_routes | JSONB | ["China-US","China-EU","China-SEA"] |

### shipments
| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID PK | |
| order_id | UUID FK → orders | |
| freight_company_id | UUID FK → freight_companies | |
| tracking_number | VARCHAR(200) | |
| estimated_delivery | DATE | |
| actual_delivery | DATE | |
| status | VARCHAR(20) | pending / in_transit / delivered / exception |

### tracking_events
| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID PK | |
| shipment_id | UUID FK → shipments | |
| event | VARCHAR(500) | "货物已出关" |
| location | VARCHAR(200) | |
| event_time | TIMESTAMPTZ | |
| source | VARCHAR(20) | manual / api |

### 辅助表
- `categories` — 产品类别树（name_zh, name_en, parent_id）
- `product_images` — 产品图片（product_id, image_url, sort_order, is_cover）
- `order_timeline` — 订单状态变更记录
- `supplier_documents` — 供应商资质文件
- `inquiries` — 询盘消息
- `refresh_tokens` — JWT Refresh Token
