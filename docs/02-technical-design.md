# APEX — 技术设计

## 架构概览

```
┌──────────────────────────────────────────────────────┐
│                    Cloudflare 免费套餐                   │
│  ┌──────────────────────────────────────┐             │
│  │         Pages (apex.pages.dev)       │             │
│  │  ┌──────────────┐  ┌──────────────┐ │  ┌────────┐ │
│  │  │  React SPA   │  │  Hono API    │ │  │   R2   │ │
│  │  │  /*          │  │  /api/*      │ │  │(Images)│ │
│  │  └──────────────┘  └──────┬───────┘ │  └───┬────┘ │
│  └────────────────────────────┼─────────┘      │      │
│                               │                │      │
│                     ┌─────────▼────┐           │      │
│                     │     D1       │           │      │
│                     │  (SQLite)    │           │      │
│                     └──────────────┘           │      │
└──────────────────────────────────────────────────────┘
          │                          │
    ┌─────▼──┐                ┌──────▼──────┐
    │  CDN   │                │ MailChannels│
    └────────┘                │  (邮件发送)   │
                              └─────────────┘

  同域部署: apex.pages.dev/* → Pages 静态资源
           apex.pages.dev/api/* → Workers (Hono)
```

> **同域部署**：前端与 API 运行在同一域名下，通过 `_routes.json` 将 `/api/*` 路由到 Worker。好处：无需 CORS 配置、Cookie 直接生效、无跨域 Cookie 烦恼。

## 技术选型

| 层 | 技术 | 理由 |
|----|------|------|
| Backend | **Hono** (TypeScript) | FastAPI 风格路由，原生支持 Cloudflare Workers |
| Database | **Cloudflare D1** | 免费 5GB / 500 万读行/天，SQLite 兼容，Workers 原生集成 |
| ORM | **Drizzle ORM** | TypeScript-first，原生支持 D1，类 SQL 语法 |
| 校验 | **Zod** | 端到端类型安全，与 Hono 深度集成 |
| Migration | **Drizzle Kit** | Drizzle 自带迁移工具 |
| Auth | JWT (**jose** + **bcryptjs**) → httpOnly Cookie | Workers 原生 Web Crypto API，零额外依赖；Cookie 免前端 token 管理，浏览器自动携带 |
| 邮件 | **MailChannels** + Workers | 免费发送邮箱验证邮件 |
| Frontend | React 18 + Vite 5 | 快速 HMR，构建速度快 |
| Router | React Router v6 | 嵌套路由、懒加载 |
| State | React Context + useReducer | 轻量，无需 Redux |
| Image Storage | Cloudflare R2 | S3 兼容、零出站费 |
| Deploy | Cloudflare Pages + Workers | 全球 CDN、免费额度覆盖 MVP |

## 安全设计

| 区域 | 措施 |
|------|------|
| 密码 | bcryptjs 哈希，最小 8 位，要求字母+数字 |
| JWT | jose HS256 签名，Workers Web Crypto API；Access Token 15min，Refresh Token 7d |
| Token 传输 | 登录/注册时通过 `Set-Cookie` 写入 httpOnly Cookie（JS 不可读），后续请求浏览器自动携带 |
| CSRF | `SameSite=Lax`（同域）+ 修改操作（POST/PUT/PATCH/DELETE）校验 `X-CSRF-Token` header |
| 邮箱验证 | 注册必须验证邮箱，MailChannels 发送 10 分钟有效一次性链接 |
| API 鉴权 | Hono 中间件读 Cookie 中 access_token，失败返回 401 |
| 登出 | 后端清空 Cookie（Max-Age=0）+ 标记 refresh_token 为 revoked |
| 数据所有权 | 供应商只能编辑自己的产品；采购商看自己的订单 |
| 图片上传 | 类型白名单 (jpg/png/webp)，最大 5MB |
| CORS | 同域部署 `/api/*`，无需额外 CORS 配置 |
| SQL 注入 | ORM 参数化查询 |
| XSS | React 默认转义 + CSP Header |
| 环境变量 | `.dev.vars` / Workers Secrets，不提交密钥 |

### 认证流程

```
注册
  POST /api/auth/register { email, password }
  → 创建用户（email_verified=false）
  → 发送验证邮件（MailChannels，10min 有效）
  → 用户点击验证链接 → GET /api/auth/verify-email?token=xxx
  → email_verified = true

登录
  POST /api/auth/login { email, password }
  → 验证密码（bcryptjs.compare）
  → 签发 Access Token (15min) + Refresh Token (7d)
  → Set-Cookie: access_token=<jwt>; HttpOnly; Secure; SameSite=Lax; Path=/
  → Set-Cookie: refresh_token=<jwt>; HttpOnly; Secure; SameSite=Lax; Path=/api/auth
  → Set-Cookie: csrf_token=<random>; Secure; SameSite=Lax; Path=/（JS 可读）
  → 响应体: { data: { user } }   ← 不含 token

后续请求
  → 浏览器自动带 access_token Cookie
  → Hono 中间件 c.req.cookie('access_token') 验证
  → 修改操作校验 X-CSRF-Token header == csrf_token Cookie

Token 刷新
  → Access Token 过期返回 401
  → 前端 fetch wrapper 自动调 POST /api/auth/refresh
    （浏览器自动带 refresh_token Cookie）
  → 签发新 Access Token → Set-Cookie 更新

登出
  POST /api/auth/logout
  → Set-Cookie: access_token=; Max-Age=0（清空三个 Cookie）
  → refresh_token 在 DB 标记 revoked
  → 响应体: { data: { ok: true } }
```

> **为什么还是 JWT 而不是纯 Session**：Cloudflare Workers 是无状态的，用 Session 需要每次请求查 D1（慢 + 读配额消耗）。JWT 自包含身份信息（user_id、role），中间件验证签名即可，零数据库查询。Cookie 只负责传输，JWT 只负责身份——各司其职。

## 前端路由设计

### 公开页面
| 路径 | 页面 |
|------|------|
| `/` | 首页：搜索入口（VIN/OEM/车型浏览三条路径） |
| `/search` | 搜索结果页（列表/网格，按车型/类别过滤） |
| `/products/:id` | 产品详情（含车型适配列表） |
| `/suppliers/:id` | 供应商详情页 |
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
