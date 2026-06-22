# Week 3 Report — nixiangdemei03

## 1. 本周做了什么（事实清单）

### 立项与 PRD

- 将 RBT 留学生地图项目完全重置，重新立项为 **APEX（Auto Parts EXport）**——中国汽配供应商对海外采购商的 B2B 平台
- 与 Claude 进行 8 轮 Brainstorming，产出结构化 PRD：28 条用户故事（"作为 X，我想 Y，以便 Z"）、9 条数据流、6 条边界处理
- 产出 6 份配套文档：product-brief、PRD、technical-design、data-model、api-design、roadmap
- PRD 经 Claude 交叉复审（PRD ↔ 5 配套文档），发现 **14 个问题**（3 Critical：询问/支付/供应商主页缺字段），逐条讨论修复，形成 [prd-review-qa.md](prd-review-qa.md)
- PRD 重构为 **5 板块标准格式**（目标 / 非目标 / 用户故事 / 验收标准 / 风险），符合课程要求

### 原型

- 出 **14 页低保真灰度线框图**（Buyer 7 + Supplier 4 + Admin 2 + 导航首页），覆盖全部 28 条用户故事
- 原型对照最新 PRD 完成校准（9 处修改：天眼查→人工审核、费率 2%→3%/7%、加 24h 倒计时、VIN 未命中更新等）
- 首页加入中英文切换器（中文/EN 按钮 + localStorage 记忆）

### Spec 体系

- 将 PRD 拆分为 **15 个 Issue**，每个按标准模板重写（背景+用户故事+任务清单+验收标准+labels+milestone+assignee）
- 判定 10 个大功能为 Epic，进一步拆分为 **37 个子 Issue**（`spec/` 子文件夹，每子 Issue 独立可测）
- Labels 规范化：每个 Issue ≥1 type（feat/fix/chore）+ 1 priority（p0/p1/p2）+ 1 module（backend/frontend/infra/ux）
- 写了 [spec-guide.md](../../templates/spec-guide.md)（Spec 书写规范）和 [skill-template.md](../../templates/skill-template.md)（Skill 模板）

### Skills

- 写了 **3 个 custom skill**：
  - `/5905` — SSH Lab 分析 + 刷题生成（修安全漏洞：sshpass -p → SSHPASS 环境变量）
  - `/check-prd` — PRD 审查（板块完整性 + 验收标准可测性 + 配套文档一致性）
  - `/spec` — PRD → Issues 结构化拆分（两次分解：所有功能→大功能→子 Issue）
- 5905 按 skill 模板重构（front-matter name/description/trigger + body 六段结构）

### 代码

- **Phase 1 脚手架已启动**：`projects/origin/apex-app/` 下 27 个文件
  - FastAPI `/api/hello` + React + Vite + proxy + Makefile（Issue 01）
  - 5 张核心表 SQLAlchemy 模型 + async engine（Issue 02）
  - JWT Auth API：register/login/refresh/me + bcrypt + Pydantic 校验（Issue 03）
- 验收标准汇总：[tests/issues验收标准.md](../../tests/issues验收标准.md)

### 工程

- 沉淀 **5 条 workflow**（PRD / 原型 / Spec / 周报 / Git），每条含流程步骤 + 模板 + 经验教训
- 全量覆盖式推送到 GitHub（2 次 force push），仓库从 RBT 完全切换为 APEX

## 2. 本周学到了什么（知识 + 反思）

- **PRD 不是写出来的，是问出来的**：8 轮 brainstorm 每轮只聚焦一个维度（支付→退款→VIN→供应链）。R5 从"平台不碰钱"翻盘到"统一收银"是整个迭代最重要的转折。
- **AI 复审能发现人忽略的系统性问题**：我自评 8.8，Claude 交叉比对 6 份文档给了 6.5——支付/询问/结算三块缺失我完全没意识到。人脑很难同时追踪 PRD↔数据模型↔API↔Issues 四层一致性。
- **我最 aha 的瞬间**：担心月度结算挤压供应商现金流，Claude 指出汽配行业提前一年备货、海外直发不经过供应商仓库。我之前用 B2C 经验套 B2B，完全错了。
- **我之前以为原型做完就完了**——这周发现原型必须和 PRD 校准。PRD 改 14 处，原型跟着改 9 处。不校准的话原型就是"上一版 PRD 的图"。
- **Spec 拆分有方法论**：大功能→Epic→子 Issue 的两层拆分让每个 Issue 变成"1-2 天可完成"的粒度。37 个子 Issue 比 15 个大块头可执行得多。
- **我还没完全搞懂的**：支付网关商务对接——找谁聊、聊什么、协议模板、跨境合规。这是 Phase 1 需要并行启动的非技术卡点。

## 3. AI 协作记录

- **最爽的一次**：把 PRD + 5 份文档丢给 Claude 做交叉一致性审查，30 秒内发现支付系统在 PRD 写了但 API 和数据模型完全没设计——这是我自己看了两天没看出来的。
- **最坑的一次**：R2 时 Claude 写了"平台自动解析 VIN"，文档漂亮但实际不存在免费全球 VIN API。教训：**AI 会默认互联网上存在它想象出来的 API**，涉及外部数据源的方案必须亲自验证。
- **个人套路升级**：脑暴→评估→修改→确认→写入 PRD → **交叉复审** → **Epic 拆分**。这周建立了"改了文档必改关联文件"的肌肉记忆，以及"大 Issue 必须拆到可独立交付"的纪律。

## 4. 决策记录

| 决策 | 选了 | 放弃了 | 理由 |
|------|------|--------|------|
| 支付模型 | 平台统一收银 | OCR 截图验真 | 统一收银才有抽成；OCR 验真 30% 失败率 |
| VIN 解码 | vin_pattern + 供应商兜底 | 平台自动解码 | 无免费全球 VIN API |
| 佣金模型 | 前 40 供应商 3%，后续 7% | 统一 2% | 梯度激励冷启动 |
| 供应商审核 | 人工审核（执照+实店照片+许可证） | 天眼查 OCR | API 非免费公开，OCR 不稳定 |
| 车型数据库 | 人工输入 + 交易后纠正闭环 | 购买 TecDoc | 年费 €5000，v1 用不起 |
| 消息系统 | 轻量 message + 重量 inquiry 两层 | 统一消息 | 自由咨询和正式询盘字段需求不同 |
| Issue 格式 | 标准模板（背景+故事+任务+AC+labels） | 自由格式 | 可自动 review 验证 |

## 5. 下周打算（W4 预告）

> W4 正式进入数据库 schema 设计 + 后端骨架 + TDD。

1. **ER 图 + Migration** — 让 AI 基于 spec 画 ER 图、写 Alembic migration，spec-driven 的 schema 段
2. **TDD 节奏** — AI 先写测试（red）→ 再写实现（green）→ 跑通 refactor。从 Issue 03 Auth 的 pytest 开始
3. **GitHub Actions CI** — 每次 push 自动跑测试，CI 绿灯成为 merge 门槛
4. **引入 Backend Agent** — 给 AI 角色化上下文，让它专注后端开发
5. **Issue Backlog 驱动** — W2 拆的 15 个 Issue 作为 backlog，完成一个 close 一个，朝 v1.0 milestone 推进

## 6. 资源沉淀

- [APEX PRD v1.0](../../01-prd.md) — 8 轮迭代 + 14 条修复，5 板块结构，28 条用户故事，梯度佣金模型
- [PRD 复审 Q&A](prd-review-qa.md) — Claude 发现 14 个问题 + 逐条回复 + 落实情况
- [PRD 详细分析报告](../superpowers/specs/2026-06-22-prd-review.md) — 6 维度评分（综合 8.4）
- [低保真原型](../../projects/prototypes/index.html) — 14 页灰度线框图，中英文切换，浏览器直接打开
- [Spec 规范](../../templates/spec-guide.md) — Issue 书写标准 + Epic 拆分规则
- [Skill 模板](../../templates/skill-template.md) — front-matter + body 六段结构
- [Workflow 文档](../../workflow/) — 5 条流程（PRD/原型/Spec/周报/Git）
- [Cloudflare R2](https://developers.cloudflare.com/r2/) — S3 兼容对象存储，零出站费

## 7. 求助 / 卡点

- 支付网关商务对接——PRD 写了方向（Stripe/PayPal/支付宝国际版），但具体对接步骤（找谁、聊什么、协议模板、跨境合规要求）完全空白。需要 Phase 1 期间并行突破。
