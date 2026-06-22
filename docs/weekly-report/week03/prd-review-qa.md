# APEX PRD v1.0 — 复审问答记录

> 2026-06-22 · Claude Code 复审 PRD → nixiangdemei03 逐条回复

---

## Q1: "询问订单"流程 — PRD 描述了一套流程，API 和数据模型都没落地

**🔍 Claude 复审发现**：PRD 花了大量篇幅描述询问制（采购商提交询问→供应商确认→生成正式订单），但 API 没有询问转单端点，数据模型 inquiries 表字段未定义，Issue 无覆盖。

**💬 回复**：

1. 目前没有 API 等数据，等待后期补齐
2. 数据模型需要一个健全且庞大的数据库支撑，架构参考大大汽配网平台或自己设计
3. Issues 补充一个询问→转单转换逻辑：在询问单界面有两个按钮——**下单**（询问完成后直接在当前供应商下单）和**取消**（询问取消，双方端均保留记录，显示为"已取消"）

> ✅ 已落实：Issue 15（Inquiry→Order Conversion）+ inquiries 表完整 schema + `POST /api/inquiries/:id/convert-to-order`

---

## Q2: 支付系统 — PRD 商业模式完全依赖支付，但 API/数据模型为零

**🔍 Claude 复审发现**：PRD 详细描述了平台统一收银、Stripe/PayPal/支付宝对接，但 API 设计无支付端点，数据模型无 payments 表，无 webhook。整个商业模型（2% 抽成）建立在支付闭环上，但支付系统在技术设计中完全不存在。

**💬 回复**：

1. 目前还没有涉及落实支付的环节，只需要模拟一个不存在的 API 就好，后期会加上
2. 加 payments 表——采购商、供应商、平台三方均有流水表，方便查账
3. 加上 webhook 端点进入 PRD 记录
4. settlements 表——供应商、采购商、平台三方各持一份，平台用作对比。根据每天实际成交情况生成日流水，月度汇总生成月度流水用于结算与平台抽成。平台每半年根据流水评估供应商风险：
   - **过低** → 与供应商沟通低销售额原因，提供推流帮助
   - **过高** → 检查采购商与供应商双方，防止洗钱或资产转移风险

> ✅ 已落实：API 新增 Payments / Settlements / Refunds 三组端点（v1.0 占位），数据模型新增 payments + settlements 表，PRD 新增半年度风险评估

---

## Q3: 供应商主页数据模型缺字段

**🔍 Claude 复审发现**：SUP-09 要求展示 Logo、成立年份、主营品牌、公司介绍、联系方式，但 users 表缺少这些字段。

**💬 回复**：补充字段即可。

> ✅ 已落实：users 表新增 logo_url、established_year、main_brands、description、address

---

## Q4: BUY-04 "站内消息" 和 BUY-12 "询问订单" 概念重叠、边界不清

**🔍 Claude 复审发现**：BUY-04 听起来像自由聊天，BUY-12 像结构化表单，但 API 只有一个 `/api/inquiries`，无法区分"随便问个问题"和"有明确 OEM 号和图片的正式询盘"。

**💬 回复**：明确为两层——轻量 **message**（自由文本，不可转单）+ 重量 **inquiry**（结构化含 OEM/图片/车型，可转订单）。

> ✅ 已落实：inquiries 表新增 inquiry_type 字段（message / inquiry），PRD 用户故事表加注释区分

---

## Q5: 48h/72h 自动催付/取消 — 无后台任务基础设施

**🔍 Claude 复审发现**：PRD 写了自动提醒和自动取消，但技术设计中没有任何调度机制（Celery/APScheduler/Workers Cron）。

**💬 回复**：

1. 订单下单未付款界面显示后，自动加一个 **timer 计时器**，**24 小时内未付款自动取消**
2. 订单下单后给供应商的订单上需要明确显示「**未付款**」字样，提醒供应商对方暂未付款，供应商可在平台上自行联系采购商询问情况

> ✅ 已落实：PRD 支付状态模型改为 24h timer，供应商端订单列表加「⚠️ 未付款」标注

---

## Q6: VIN 未命中后的"供应商回复"路径是断头路

**🔍 Claude 复审发现**：VIN 未命中→透传给供应商→供应商解码→回复采购商——但"回复"没有 API 端点、没有 UI、没有 Issue 覆盖。

**💬 回复**：改变形式——

1. 采购商下单时填写车架号，数据库中有之前供应商提供的数据才显示，没有就不显示
2. 提交给供应商后供应商自己去查找
3. 数据库中没有的车架号，在订单交易完成后或咨询结束后**弹窗要求供应商填写完善数据库**
4. 对填写了的供应商提供**推流奖励**，具体奖励参数公式之后再说

> ✅ 已落实：PRD VIN 搜索流程改为"下单时附带 VIN + 交易后弹窗完善库 + 推流奖励"，原型新增 Post-Transaction Enrichment 区块

---

## Q7: Product Brief 说"初始免费" vs PRD 从 Day 1 抽 2%

**🔍 Claude 复审发现**：两处矛盾——如果 v1.0 免费引流，结算系统可以后做；如果 v1.0 就抽成，支付+结算必须是 P0。

**💬 回复**：开始就需要抽取佣金，但是佣金比例只有销售额的 **3%**，作为对先愿意使用的供应商的回馈。后期随着供应商加入量增加，只保留**前 40 个供应商 3%** 不变，后续供应商采取 **7%** 抽成结算。供应商 ID 在后端数据库中作为主键，数字部分方便查询前 40 个。

> ✅ 已落实：PRD 结算模型改为梯度佣金（前 40 供应商 3%，后续 7%），Product Brief 费用行同步更新

---

## Q8: 退款流程是叙事不是设计

**🔍 Claude 复审发现**：PRD 退款流程有 4 个分支（需不需要检测、定损确认、客服介入），但 orders 表没有 refund_status，没有 refund API，Issue 13 提到退款扣减但没有独立 Issue。

**💬 回复**：

1. orders 表创建 **refund_status 字段**
2. refund 相关 API 端点后续补充，现在可以模拟一个不存在的 API 占位
3. 为 Issue 13 的验收标准提到退款扣减创建**独立 Issue**

> ✅ 已落实：orders 表新增 refund_status（none/requested/approved/rejected/completed），API 新增 Refunds 组，创建 Issue 14（Refund & Return Flow）

---

## Q9: inquiries 表没有 schema

**🔍 Claude 复审发现**：数据模型文件只列出表名，字段为零。

**💬 回复**：目前还没有数据支撑，暂时先这样。

> ✅ 已落实：inquiries 表完整 schema 已定义（含 inquiry_type, message, oem_number, vin, quantity, image_urls, status, converted_order_id 等 15 个字段）

---

## Q10: Supplier 注册 OCR → 天眼查流程过度依赖第三方

**🔍 Claude 复审发现**：天眼查 API 需要企业认证才能调用，OCR 识别中国营业执照准确率不稳定。如果这个链路失败率超过 20%，供应商注册就卡死了。

**💬 回复**：取消天眼查 OCR 自动验证，改用营业执照、实体店拍照、销售许可证等相关证件的照片与扫描件进行**人工审核**。

> ✅ 已落实：PRD 供应商上架流程改为人工审核，supplier_documents 表去 ocr_data 字段，原型 Admin 审核页改为逐文件人工审查

---

## Q11: 没有通知系统设计

**🔍 Claude 复审发现**：SUP-08 提醒、48h 催付都依赖通知，但技术设计仅有 SendGrid 验证邮件，无统一推送基础设施。

**💬 回复**：通知系统放在之后细节处理。

> ⏳ 延后至 Phase 3

---

## Q12: 多币种 — 定价 CNY+USD，但未讨论买家是否能用 EUR/GBP 支付

**🔍 Claude 复审发现**：Stripe/PayPal 支持多币种，但 PRD 只讨论了 CNY 原价 + USD 售价。

**💬 回复**：供应商以 CNY 上传定价，系统根据**中国银行实时汇率**进行换算。采购商端可自行选择支付币种（USD/EUR/GBP 等）。

> ✅ 已落实：PRD 新增多币种支持段，原型产品详情页加币种选择器（USD/EUR/GBP）

---

## Q13: 成功指标无时间维度

**🔍 Claude 复审发现**："注册供应商 ≥ 20" 是一个月还是一年？没有时间限定。

**💬 回复**：对创业项目需要多维度指标设计。以一个**季度**为准——供应商 ≥ 20、采购商 ≥ 50 才算及格。

> ✅ 已落实：Roadmap 成功指标改为季度制（Q1 目标）

---

## Q14: 冷启动策略缺失

**🔍 Claude 复审发现**：Phase 1 期望供应商和采购商从天而降，没有任何获取策略。

**💬 回复**：冷启动是开发团队需要自行寻找受众。

> ✅ 已落实：Roadmap 新增冷启动策略段（联系国内厂商 + LinkedIn/展会触达海外采购商 + 前 40 供应商 3% 低佣金激励）

---

## 总结

| 问题 | 严重度 | 处理 |
|------|:--:|:--:|
| Q1 询问订单流程 | Critical | Issue 15 + inquiries schema + convert-to-order API |
| Q2 支付系统缺失 | Critical | Payments/Settlements/Refunds API + payments/settlements 表 |
| Q3 供应商主页缺字段 | Critical | users 表 +5 字段 |
| Q4 消息/询盘边界不清 | High | inquiry_type: message / inquiry 两层 |
| Q5 自动催付无调度 | High | 24h timer + 未付款标注 |
| Q6 VIN 回复断头路 | High | 交易后弹窗完善库 + 推流奖励 |
| Q7 佣金矛盾 | Medium | 梯度 3%/7% |
| Q8 退款无设计 | Medium | refund_status + Issue 14 |
| Q9 inquiries 无 schema | Medium | 15 字段完整定义 |
| Q10 OCR/天眼查依赖 | Medium | 人工审核 |
| Q11 通知系统 | Low | 延后 |
| Q12 多币种 | Low | 实时汇率 + 币种选择器 |
| Q13 指标无时间 | Low | 季度制 |
| Q14 冷启动 | Low | 自行寻找受众 |

**14 个问题全部处理：12 个已落实，2 个延后。**
