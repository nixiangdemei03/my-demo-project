# APEX PRD v1.0 — 详细分析报告

> 分析日期：2026-06-22 | 分析范围：PRD + Product Brief + Technical Design + Data Model + API Design + Roadmap + 15 Issues + 14 Prototypes

---

## 一、项目概览

APEX（Auto Parts EXport）是一个 B2B 平台，连接中国汽车配件供应商与海外采购商。v1.0 覆盖 28 条用户故事（Supplier 10 + Buyer 12 + Admin 6），技术栈为 FastAPI + React + PostgreSQL + Cloudflare R2。

---

## 二、维度评分

### 2.1 用户故事完整性 — 9.0/10

三角色覆盖均匀，P0/P1/P2 梯度合理。每个故事可独立验证。

**亮点**：
- Supplier 故事从注册→上架→接单→发货→追踪形成闭环
- Buyer 三条搜索路径（VIN/OEM/车型浏览）覆盖汽配采购的全部入口
- Admin 故事克制，仅覆盖审核和统计，未过度设计

**缺位**：无。28 条故事 + 15 个 Issue 的验收标准一一对应。

### 2.2 数据流设计 — 8.5/10

PRD 包含 9 条数据流：三种搜索、供应商上架、采购商下单（询问制）、支付状态、平台结算、供应商拒绝、纠纷退款、图片上传。

**亮点**：
- VIN 搜索命中/未命中双路径务实——没有假装有免费 VIN API
- 供应商纠正闭环（采购商输入→供应商纠正→系统记录）是零成本数据积累策略
- 支付超时自动取消（24h timer）逻辑清晰
- 询问转单流程（下单/取消两个按钮）简洁明确

**可改进**：
- 日流水→月流水→半年度风控的自动化链路目前依赖手动触发，缺少调度设计细节
- 多币种汇率转换的更新频率未定义（实时？每日固定汇率？）

### 2.3 商业模式与结算 — 8.0/10

```
前 40 供应商 3% 抽成 → 第 41 起 7% → 每月 1 日结算 → 半年度风险评估
```

**亮点**：
- 梯度佣金兼顾冷启动激励和长期盈利
- 汽配行业"提前备货+海外直发"的特性分析准确——月度结算不挤压供应商现金流
- 半年度风控（过低推流帮助+过高防洗钱）是成熟平台的思考方式
- 退款扣减逻辑已嵌入结算示例

**风险点**：
- "前 40 个"按 UUID 判定——UUID 不是自增数字，无法直接排序。需要额外创建自增序列号字段
- 半年度风控的"推流帮助"和"异常检查"目前只有方向没有操作流程

### 2.4 技术架构 — 7.5/10

| 层 | 评分 | 说明 |
|----|:--:|------|
| Backend | 8 | FastAPI + SQLAlchemy 2.0 + Alembic，选型成熟 |
| Auth | 8 | JWT (Access 30min + Refresh 7d)，安全设计覆盖 8 条 |
| Data Model | 8 | 5 核心表 + 7 辅助表 + payments/settlements/inquiries，ER 图完整 |
| API Design | 7 | RESTful 风格，7 组端点，统一分页格式。Payments/Settlements/Refunds 为占位 API |
| Frontend | 7 | React + Vite + React Router v6，路由设计覆盖三角色 |
| Storage | 8 | Cloudflare R2 零出站费，适合图片托管 |
| Deploy | 7 | Cloudflare Pages + Workers，但 Workers 跑 FastAPI 需要适配层 |

**关键缺口**：
- 后台定时任务（月度结算生成、订单超时取消）未设计调度方案
- 通知系统（邮件/站内）仅有 SendGrid 验证邮件，无统一推送基础设施

### 2.5 安全设计 — 8.5/10

技术文档中安全措施覆盖完整：bcrypt 密码策略、JWT 过期策略、数据所有权鉴权、图片类型白名单、CORS、ORM 防注入、XSS 防护（React + CSP）、环境变量管理。

**缺位**：支付 webhook 签名验证未提及（Stripe/PayPal 依赖 webhook signature verification 防伪造回调）。

### 2.6 低保真原型 — 8.0/10

14 个灰度 HTML 页面覆盖全部 28 条用户故事。采购商搜索→下单→追踪三条核心路径可视化。

**亮点**：
- 产品详情页的询盘表单字段（OEM、VIN、数量、图片上传）与 PRD BUY-12 对齐
- VIN 搜索结果同时展示命中路径和未命中兜底提示
- Admin 供应商审核页做了天眼查 API 对照（现在改为人工审核后需更新）

---

## 三、Issue 覆盖矩阵

| # | Issue | Phase | 覆盖 PRD 故事 | 状态 |
|:--:|-------|:--:|------|:--:|
| 1 | Scaffolding | 1 | 基础设施 | 已定义 |
| 2 | DB Models | 1 | 全部表 | 已定义 |
| 3 | User Auth | 1 | SUP-01, BUY-01 | 已定义 |
| 4 | Product CRUD | 1 | SUP-02/03/06/10 | 已定义 |
| 5 | Search | 1 | BUY-09/10/11 | 已定义 |
| 6 | Order API | 2 | BUY-05, SUP-04 | 已定义 |
| 7 | Freight | 2 | SUP-05, BUY-06 | 已定义 |
| 8 | Supplier Page | 1 | SUP-09 | 已定义 |
| 9 | Frontend Catalog | 1 | BUY-02/03 | 已定义 |
| 10 | Supplier Dashboard | 1 | SUP-04/08 | 已定义 |
| 11 | Buyer Dashboard | 2 | BUY-05/06/07 | 已定义 |
| 12 | Admin Dashboard | 3 | ADM-01~06 | 已定义 |
| 13 | Payment & Settlement | 2 | 结算模型 | 已定义 |
| 14 | Refund Flow | 2 | 退款流程 | 已定义 |
| 15 | Inquiry→Order | 2 | BUY-04/12 | 已定义 |

---

## 四、PRD vs 配套文档一致性

| 交叉比对 | 结果 |
|----------|:--:|
| PRD ↔ Product Brief | 通过 — 佣金已统一（3%/7%梯度），定位一致 |
| PRD ↔ Data Model | 通过 — users/products/orders 字段已对齐，新增 payments/settlements/inquiries |
| PRD ↔ API Design | 通过 — 7 组端点覆盖全部流程，payments/settlements/refunds 占位 |
| PRD ↔ Roadmap | 通过 — Phase 1-3 分工清晰，季度指标已定义 |
| PRD ↔ Prototypes | 通过 — 14 页覆盖 28 条故事 |
| PRD ↔ Issues | 通过 — 15 个 Issue 一一对应 |

---

## 五、遗留问题清单

| # | 问题 | 严重度 | 建议 |
|---|------|:--:|------|
| 1 | UUID 无法排序——"前 40 个供应商"判定需自增序列号 | Medium | users 表加 `registration_seq` 自增字段 |
| 2 | 后台定时任务无调度方案（月度结算、订单超时取消） | Medium | Phase 2 前确定方案（Cloudflare Workers Cron / APScheduler） |
| 3 | 通知系统仅有 SendGrid 验证邮件，无统一推送层 | Medium | Phase 3 设计通知表 + 推送通道 |
| 4 | Payment webhook 签名验证未提及 | Medium | 接入真实支付网关时必须加 |
| 5 | 汇率更新频率未定义 | Low | 建议每日固定汇率（中国银行牌价），避免实时波动引发纠纷 |
| 6 | Admin 供应商审核原型仍显示天眼查对照（已改为人工审核） | Low | 更新 admin/02-supplier-review.html |
| 7 | 供应商纠正 VIN 数据的"推流奖励公式"标记为 TBD | Low | Phase 2 末期定义 |

---

## 六、总评

| 维度 | 分数 | 一句话 |
|------|:--:|------|
| 用户故事 | 9.0 | 三角色覆盖均匀，P0/P1/P2 梯度合理 |
| 数据流 | 8.5 | 9 条流覆盖核心路径，VIN 双路径务实 |
| 商业模式 | 8.0 | 梯度佣金+半年度风控，冷启动激励有效 |
| 技术架构 | 7.5 | 选型成熟，定时任务/通知待补 |
| 安全设计 | 8.5 | 8 条措施完整，需补 webhook 验签 |
| 文档一致性 | 9.0 | PRD ↔ 5 份配套文档 + 15 Issues + 14 Prototypes 对齐 |
| **综合** | **8.4** | **可以进入 Phase 1 开发** |

---

## 七、修订历史

| 日期 | 事件 | 分数变化 |
|------|------|:--:|
| 2026-06-19 | PRD v1.0 初版，自评 8.8 | 8.8 |
| 2026-06-22 | 首次复审（发现支付/询问/结算三块缺失） | 6.5 |
| 2026-06-22 | 根据 prd_repair.txt 修复 14 条问题 | 8.0 |
| 2026-06-22 | 本报告——全面评估 | 8.4 |
