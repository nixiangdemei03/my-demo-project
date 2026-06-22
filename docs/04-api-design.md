# APEX — API 设计

## 统一响应格式

```json
{"data": {...}, "error": null}
```

状态码：200 成功，201 创建，400 参数错误，401 未认证，403 无权限，404 不存在，500 服务端错误。

## Auth — `/api/auth`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| POST | `/api/auth/register` | 用户注册 | - |
| POST | `/api/auth/login` | 登录，返回 JWT | - |
| POST | `/api/auth/refresh` | 刷新令牌 | Refresh Token |
| GET | `/api/auth/me` | 当前用户信息 | JWT |
| PUT | `/api/auth/me` | 更新个人信息 | JWT |

## Products — `/api/products`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| GET | `/api/products` | 产品列表（分页/筛选） | - |
| GET | `/api/products/:id` | 产品详情 | - |
| POST | `/api/products` | 创建产品 | supplier |
| PUT | `/api/products/:id` | 更新产品 | supplier (本人) |
| DELETE | `/api/products/:id` | 下架产品 | supplier (本人) |
| POST | `/api/products/:id/images` | 上传图片 | supplier (本人) |
| DELETE | `/api/products/:id/images/:img_id` | 删除图片 | supplier (本人) |

**筛选参数**: `?q=关键词&oem=OEM编号&category_id=X&make=Toyota&model=Hilux&year=2020&price_min=X&price_max=X&supplier_id=X&page=1&page_size=20`

### 搜索端点 — `/api/search`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| POST | `/api/search/vin` | 车架号搜索：输入 VIN，返回适配配件列表 | - |
| GET | `/api/search` | 文字搜索 + 车型浏览合并端点 | - |

**VIN 搜索请求**:
```json
{"vin": "JTELV71J800012345"}
```

**VIN 搜索响应**:
```json
{
  "vehicle": {"make":"Toyota","model":"Land Cruiser Prado","year":2008,"engine":"1GR-FE"},
  "confidence": "high",
  "products": [...]
}
```

**文字/车型搜索参数**: `?q=刹车片&make=Toyota&model=Hilux&year=2020&category_id=X&oem=04465-0K090`

### 供应商 — `/api/suppliers`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| GET | `/api/suppliers/:id` | 供应商详情页（公司信息、资质缩略图、产品数、响应率） | - |

## Orders — `/api/orders`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| POST | `/api/orders` | 创建订单 | buyer |
| GET | `/api/orders` | 订单列表（按角色过滤） | JWT |
| GET | `/api/orders/:id` | 订单详情 | JWT |
| PATCH | `/api/orders/:id/status` | 更新状态 | JWT |
| POST | `/api/orders/:id/ship` | 发货（关联货运+运单号） | supplier |
| POST | `/api/orders/:id/cancel` | 取消订单 | JWT |

## Freight — `/api/freight`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| GET | `/api/freight-companies` | 货运公司列表 | JWT |
| POST | `/api/freight-companies` | 添加货运公司 | admin |
| GET | `/api/shipments/:id/tracking` | 追踪事件列表 | JWT |
| POST | `/api/shipments/:id/events` | 添加追踪事件 | supplier/admin |

## Categories — `/api/categories`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| GET | `/api/categories` | 类别树 | - |
| POST | `/api/categories` | 创建类别 | admin |
| PUT | `/api/categories/:id` | 编辑类别 | admin |

## Admin — `/api/admin`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| GET | `/api/admin/users` | 用户列表 | admin |
| PATCH | `/api/admin/users/:id/verify` | 审核供应商 | admin |
| GET | `/api/admin/stats` | 平台统计 | admin |
| GET | `/api/admin/orders` | 全局订单视图 | admin |

## Inquiries — `/api/inquiries`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| POST | `/api/inquiries` | 发送询盘（type: message / inquiry） | buyer |
| GET | `/api/inquiries` | 收/发件箱（按 type 过滤） | JWT |
| PATCH | `/api/inquiries/:id/read` | 标记已读 | JWT |
| POST | `/api/inquiries/:id/convert-to-order` | 询问转正式订单 | buyer |
| PATCH | `/api/inquiries/:id/cancel` | 取消询问（双方均可） | JWT |

**inquiry_type 区分**：
- `message` — BUY-04 轻量消息，自由文本，不可转单
- `inquiry` — BUY-12 结构化询盘，含 OEM/VIN/图片/数量，可转单

## Payments — `/api/payments`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| POST | `/api/payments/checkout` | 创建支付（返回支付网关 URL 或模拟响应） | buyer |
| POST | `/api/payments/webhook` | 支付网关回调（v1.0 为模拟占位） | - |
| GET | `/api/payments` | 支付流水列表（按角色过滤） | JWT |

> v1.0 支付网关为模拟 API——`checkout` 直接返回 `payment_status=paid`，webhook 端点预留。

## Settlements — `/api/settlements`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| GET | `/api/settlements` | 结算单列表（按角色过滤） | JWT |
| GET | `/api/settlements/:id` | 结算单详情 | JWT |
| POST | `/api/settlements/generate` | 手动触发月度结算 | admin |

> 月度结算于每月 1 日自动生成（定时任务），同时支持管理员手动触发。

## Refunds — `/api/refunds`

| 方法 | 路径 | 说明 | 鉴权 |
|------|------|------|:--:|
| POST | `/api/refunds` | 发起退款申请 | buyer |
| PATCH | `/api/refunds/:id` | 处理退款（供应商审核/平台介入） | JWT |
| GET | `/api/refunds` | 退款列表（按角色过滤） | JWT |

> v1.0 退款为模拟占位 API，用于验证流程。真实退款对接在支付网关接入后完成。

## 分页格式

```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total": 150,
    "total_pages": 8
  }
}
```
