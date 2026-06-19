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

**筛选参数**: `?q=关键词&category_id=X&price_min=X&price_max=X&supplier_id=X&page=1&page_size=20`

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
| POST | `/api/inquiries` | 发送询盘 | buyer |
| GET | `/api/inquiries` | 收/发件箱 | JWT |
| PATCH | `/api/inquiries/:id/read` | 标记已读 | JWT |

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
