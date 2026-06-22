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
orders 1──N payments             payment records per order
shipments N──1 freight_companies
shipments 1──N tracking_events
products 1──N inquiries
users 1──N supplier_documents
users 1──N settlements (supplier) settlements per supplier
users 1──N settlements (buyer)   settlements per buyer
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
| logo_url | VARCHAR(500) | 供应商 Logo |
| established_year | INT | 成立年份 |
| main_brands | VARCHAR(500) | 主营品牌（逗号分隔） |
| description | TEXT | 公司介绍 |
| address | VARCHAR(500) | 公司地址 |
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
| warranty | VARCHAR(200) | 保修期（如 "12 months / 50,000 km"） |
| return_policy | VARCHAR(200) | 退换政策（如 "30-day return, buyer pays return shipping"） |
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
| status | VARCHAR(20) | pending→confirmed→paid→shipped→delivered→cancelled |
| payment_status | VARCHAR(20) | unpaid / paid / verified，默认 unpaid |
| cancel_reason | VARCHAR(100) | supplier_rejected / buyer_cancelled / other |
| cancel_note | TEXT | 取消原因说明 |
| refund_status | VARCHAR(20) | none / requested / approved / rejected / completed，默认 none |
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
- `categories` — 产品类别树（name_zh, name_en, parent_id），按汽配行业标准树组织
- `product_images` — 产品图片（product_id, image_url, sort_order, is_cover）
- `product_vehicle_fits` — **P0** 车型适配（product_id, make, model, year_start, year_end, engine, vin_pattern）
- `order_timeline` — 订单状态变更记录
- `supplier_documents` — 供应商资质文件（supplier_id, doc_type, file_url, verify_status, review_note, reviewed_by, verified_at）
- `inquiries` — 询盘消息
- `refresh_tokens` — JWT Refresh Token

### supplier_documents（资质文件）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID PK | |
| supplier_id | UUID FK → users | |
| doc_type | VARCHAR(50) | business_license / export_license / certificate / store_photo |
| file_url | VARCHAR(500) | |
| verify_status | VARCHAR(20) | pending / approved / rejected |
| review_note | TEXT | 管理员审核备注 |
| reviewed_by | UUID FK → users | 审核管理员 ID |
| verified_at | TIMESTAMPTZ | |
| uploaded_at | TIMESTAMPTZ | |

### product_vehicle_fits（车型适配）— P0

| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID PK | |
| product_id | UUID FK → products | |
| make | VARCHAR(100) | 品牌（Toyota） |
| model | VARCHAR(100) | 车型（Hilux） |
| year_start | INT | 起始年份 |
| year_end | INT | 截止年份 |
| engine | VARCHAR(100) | 发动机型号（1GD-FTV） |
| vin_pattern | VARCHAR(50) | VIN 匹配模式（如 JTELV71J*） |

### payments（支付流水）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID PK | |
| order_id | UUID FK → orders | |
| payer_id | UUID FK → users | 采购商 |
| amount | DECIMAL(12,2) | 支付金额 |
| currency | VARCHAR(3) | USD / EUR / GBP |
| payment_method | VARCHAR(50) | stripe / paypal / alipay |
| gateway_tx_id | VARCHAR(255) | 支付网关返回的交易 ID |
| status | VARCHAR(20) | pending / success / failed / refunded |
| paid_at | TIMESTAMPTZ | |
| created_at | TIMESTAMPTZ | |

### settlements（结算记录）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID PK | |
| user_id | UUID FK → users | 供应商或采购商 |
| user_role | VARCHAR(20) | supplier / buyer / platform |
| period_start | DATE | 结算周期起始 |
| period_end | DATE | 结算周期结束 |
| total_sales | DECIMAL(12,2) | 周期内总销售额 |
| platform_fee | DECIMAL(12,2) | 平台抽成 |
| refunds_deducted | DECIMAL(12,2) | 退款扣减 |
| net_payout | DECIMAL(12,2) | 实际到账 |
| status | VARCHAR(20) | pending / confirmed / paid |
| generated_at | TIMESTAMPTZ | 结算单生成时间 |
| confirmed_at | TIMESTAMPTZ | 供应商确认时间 |

注：平台方 settlement（user_role = 'platform'）用于对账——与供应商/采购商的结算单三方交叉验证。

### inquiries（询盘消息）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | UUID PK | |
| buyer_id | UUID FK → users | 采购商 |
| supplier_id | UUID FK → users | 供应商 |
| product_id | UUID FK → products | 关联产品（可选） |
| inquiry_type | VARCHAR(20) | message（轻量消息） / inquiry（结构化询盘） |
| message | TEXT | 消息正文 |
| oem_number | VARCHAR(100) | OEM 编号（inquiry 类型） |
| vin | VARCHAR(17) | 车架号（inquiry 类型） |
| quantity | INT | 需求数量 |
| image_urls | JSONB | 需求图片 URL 数组 |
| status | VARCHAR(20) | open / replied / converted_to_order / cancelled |
| converted_order_id | UUID FK → orders | 询盘转单后的订单 ID |
| read_at | TIMESTAMPTZ | |
| created_at | TIMESTAMPTZ | |
