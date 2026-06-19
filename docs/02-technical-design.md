# APEX — 技术设计

## 架构概览

```
┌─────────────────────────────────────────────────┐
│                    Cloudflare                     │
│  ┌──────────────┐  ┌──────────────┐  ┌────────┐ │
│  │  Pages       │  │  Workers     │  │   R2   │ │
│  │ (React SPA)  │  │ (FastAPI)    │  │(Images)│ │
│  └──────┬───────┘  └──────┬───────┘  └───┬────┘ │
└─────────┼─────────────────┼──────────────┼───────┘
          │                 │              │
    ┌─────▼──┐       ┌──────▼──────┐      │
    │ CDN    │       │  PostgreSQL │      │
    └────────┘       └─────────────┘      │
                                          │
    Frontend ←→ API ←→ Database ←→ Storage
```

## 技术选型

| 层 | 技术 | 理由 |
|----|------|------|
| Backend | FastAPI | 异步支持、自动 OpenAPI 文档、Pydantic 校验 |
| ORM | SQLAlchemy 2.0 + asyncpg | 异步数据库操作，成熟稳定 |
| Migration | Alembic | 数据库版本控制 |
| Auth | JWT (python-jose + passlib) | 无状态认证，适合 API |
| Frontend | React 18 + Vite 5 | 快速 HMR，构建速度快 |
| Router | React Router v6 | 嵌套路由、懒加载 |
| State | React Context + useReducer | 轻量，无需 Redux |
| Image Storage | Cloudflare R2 | S3 兼容、零出站费 |
| Deploy | Cloudflare Pages + Workers | 全球 CDN、免费额度够用 |

## 安全设计

| 区域 | 措施 |
|------|------|
| 密码 | bcrypt 哈希，最小 8 位，要求字母+数字 |
| JWT | Access Token 30min，Refresh Token 7 天 |
| API 鉴权 | 中间件验证 JWT，失败返回 401 |
| 数据所有权 | 供应商只能编辑自己的产品；采购商看自己的订单 |
| 图片上传 | 类型白名单 (jpg/png/webp)，最大 5MB |
| CORS | 仅允许生产域名 + localhost:5173 |
| SQL 注入 | ORM 参数化查询 |
| XSS | React 默认转义 + CSP Header |
| 环境变量 | .env 在 .gitignore，不提交密钥 |

## 前端路由设计

### 公开页面
| 路径 | 页面 |
|------|------|
| `/` | 首页 |
| `/products` | 产品目录 |
| `/products/:id` | 产品详情 |
| `/auth/login` | 登录 |
| `/auth/register` | 注册 |

### 供应商后台 (/dashboard/*)
| 路径 | 页面 |
|------|------|
| `/dashboard` | 工作台 |
| `/dashboard/products` | 产品管理 |
| `/dashboard/products/new` | 添加产品 |
| `/dashboard/products/:id/edit` | 编辑产品 |
| `/dashboard/orders` | 订单列表 |
| `/dashboard/orders/:id` | 订单详情 |
| `/dashboard/inquiries` | 询盘 |
| `/dashboard/profile` | 个人资料 |

### 采购商后台
| 路径 | 页面 |
|------|------|
| `/dashboard/orders` | 我的订单 |
| `/dashboard/orders/:id` | 订单详情(含货运) |
| `/dashboard/inquiries` | 询盘 |
| `/dashboard/profile` | 个人资料 |

### 管理后台 (/admin/*)
| 路径 | 页面 |
|------|------|
| `/admin` | 控制台 |
| `/admin/users` | 用户管理 |
| `/admin/products` | 产品管理 |
| `/admin/orders` | 订单管理 |
| `/admin/categories` | 类别管理 |
| `/admin/freight` | 货运公司管理 |
