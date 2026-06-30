# Week 4 Report — nixiangdemei03

## 1. 本周做了什么（事实清单）

### 全栈技术迁移：Python → TypeScript / Cloudflare Native

- 将整个 APEX 后端技术栈从 **FastAPI (Python) + PostgreSQL + SQLAlchemy** 迁移到 **Hono (TypeScript) + Cloudflare D1 (SQLite) + Drizzle ORM**
- 核心原因：Cloudflare Workers 不支持 Python 运行时，且 D1 是 Cloudflare 生态唯一的免费数据库
- 迁移范围 6 份文档全覆盖：
  - [CLAUDE.md](../../../CLAUDE.md) — Tech stack 段落更新，新增 Email/MailChannels
  - [01-prd.md](../../01-prd.md) — §4.3 技术栈表全部替换 + §4.4 安全设计重写 + 新增 §6 MVP 三阶段定义 + §5 风险表新增 D1 兼容性等 3 条
  - [02-technical-design.md](../../02-technical-design.md) — 架构图重绘（同域部署）、技术选型表替换、安全设计扩展（含完整认证流程图）
  - [03-data-model.md](../../03-data-model.md) — 13 张表的所有 DECIMAL→INTEGER（分）、JSONB→TEXT、新增 D1 兼容性说明
  - [04-api-design.md](../../04-api-design.md) — Auth 章节重写（Cookie-based JWT + CSRF + 邮箱验证 + 登出）、登录/登出响应示例

### 认证系统重设计

- JWT 从 **Bearer token（响应体返回）→ httpOnly Cookie**（Set-Cookie 写入，JS 不可读）
- 安全升级：
  - Access Token：30min → **15min**
  - CSRF 保护：`SameSite=Lax` + 修改操作校验 `X-CSRF-Token` header
  - 登出实现：清空三个 Cookie + DB 标记 refresh_token revoked
  - 邮箱验证：注册必须验证邮箱，MailChannels 发送 10 分钟有效一次性链接
- 核心洞察：Cloudflare Workers 无状态 → JWT 仍优于 Session（免每次请求查 D1，省读配额）

### MVP 分阶段规划

- PRD 新增 §6，将 15 个 Issue 分入三个 Phase：
  - **MVP-1（Week 1-2）**：产品目录——供应商上架 + 采购商搜索，不含交易
  - **MVP-2（Week 3-4）**：交易闭环——下单 + 支付 + 货运 + 退款
  - **v1.0 完整版（Week 5-6）**：管理后台 + 通知 + 国际化 + 部署
- 每个 Phase 明确了"做什么"和"明确不做"，防止范围蔓延

### Skills

- 写了 **`/9044_lab_exp`** skill：CSE 远程做题助手——从课程网页抓取 Tutorial 题目 + SSH 获取 CSE 已有实验代码，分析知识点/易错点/易考察点，输出 10 道练习题（简3/中4/难3），存到 `~/Desktop/9044/`
- 删除了旧的 `/5905_tut` skill（功能合并/重组）

### D1 数据模型适配

- 所有金额字段改为 INTEGER 存分（如 ¥123.45 → 12345），废除 DECIMAL 类型
- JSON 字段（specs、shipping_routes、image_urls）改为 TEXT 存 JSON 字符串
- ENUM 替代：VARCHAR + 应用层 CHECK 约束
- 风险表新增：D1 SQLite 兼容性、Workers 冷启动延迟、MailChannels 免费额度变更

## 2. 本周学到了什么（知识 + 反思）

- **技术选型要倒推约束**：我之前以为选 FastAPI 是因为"Python 熟"，这周被提醒 Cloudflare Workers 不支持 Python 时才发现——部署环境决定了语言，不是反过来。先定部署目标（免费套餐上线），再倒推技术栈。
- **Cookie-based JWT 比我以为的复杂**：httpOnly Cookie + CSRF + refresh revocation 三者必须同时做，缺一环就不安全。直接返回 token 给 JS 看似简单，实际埋了 XSS 隐患。
- **D1 SQLite 是妥协不是降级**：DECIMAL→INTEGER、JSONB→TEXT 看起来是"功能退步"，但对 MVP 来说完全够用。D1 免费 5GB + 500 万读行/天，足够支撑几百个供应商的 B2B 场景。
- **分 Phase 才是真正的 MVP 思维**：上周我写"v1.0 = 15 个 Issue"，这周发现应该先问"哪些 Issue 不做系统还能跑？"——答案只有产品目录。交易闭环是 Phase 2。
- **我还未完全搞懂的**：Drizzle Kit migration 在 Workers 环境的具体部署流程——本地跑 migration 还是 Worker 启动时自动跑？这个话题留到 Phase 1 实际写代码时解决。

## 3. AI 协作记录

- **最爽的一次**：让 Claude 对比 FastAPI vs Hono 在 Cloudflare Workers 上的差异，它直接给了六个维度对照表（运行时/路由/校验/ORM/Auth/迁移），我照着改完 6 份文档只用了不到 2 小时。
- **最坑的一次**：第一次让它重写 Auth 章节时，它写了 Set-Cookie 但没写 CSRF 保护。我追问"CSRF 怎么办？"它才补上 `SameSite=Lax` + `X-CSRF-Token` 校验。教训：**安全设计不能只说 happy path，必须追问攻击面**。
- **个人套路升级**：提需求 → AI 出方案 → **我追问"少了什么"** → AI 补全 → 写入文档。这个"追问缺失"环节比第一版方案更有价值。

## 4. 决策记录

| 决策 | 选了 | 放弃了 | 理由 |
|------|------|--------|------|
| 后端语言 | Hono (TypeScript) | FastAPI (Python) | Workers 不支持 Python；TS 前后端统一语言 |
| 数据库 | D1 (SQLite) | PostgreSQL | D1 是 Cloudflare 生态唯一免费数据库 |
| Token 传输 | httpOnly Cookie | 响应体返回 token | XSS 防护；前端无需管理 token |
| Access Token 时长 | 15min | 30min | 缩短窗口期，refresh 透明刷新 |
| 金额存储 | INTEGER（分） | DECIMAL | D1/SQLite 无 DECIMAL 类型 |
| CSRF | SameSite=Lax + X-CSRF-Token | 仅 SameSite | 纵深防御，修改操作额外校验 |
| 邮箱验证 | MailChannels（免费） | Resend / Brevo | 零成本，Workers 原生集成 |

## 5. 下周打算（W5 预告）

> W5 正式进入代码编写——从文档设计切换为 TDD 实现。

1. **MVP-1 代码启动** — 按 Hono + D1 + Drizzle 新栈搭建脚手架，`/api/hello` 在 Workers 跑通
2. **TDD 节奏推进** — 从 Auth 模块开始：先写测试（red）→ 实现（green）→ 重构。每个 Issue 独立可测
3. **CI 上线** — GitHub Actions 自动跑测试，CI 绿灯成为 merge 门槛
4. **Week05 周报按时交** — 不等到最后一刻

## 6. 资源沉淀

- [APEX PRD v1.1](../../01-prd.md) — 新增 §6 MVP 三阶段定义 + 技术栈迁移 + 风险更新
- [技术设计 v1.1](../../02-technical-design.md) — 同域部署架构 + Cookie-based Auth 完整流程
- [数据模型 v1.1](../../03-data-model.md) — D1 SQLite 适配（INTEGER 分 / TEXT JSON）
- [API 设计 v1.1](../../04-api-design.md) — Auth 章节重写（Cookie + CSRF + 邮箱验证 + 登出）
- [`/9044_lab_exp` skill](../../../skills/9044_lab_exp/SKILL.md) — 课程网页抓取 + SSH + 知识点分析 + 刷题生成

## 7. 求助 / 卡点

- Drizzle Kit migration 在 Cloudflare Workers 上的最佳实践——本地跑 `drizzle-kit push` 还是 Worker 启动时自动 migrate？社区方案不一，需要确定一个合适的方式。
- Workers 本地开发体验（`wrangler dev`）与 D1 local 的对齐程度——如果本地和线上差异太大，TDD 会很难做。
