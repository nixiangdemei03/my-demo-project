# 13-04: Settlement Statement Generation

**Labels**: `feat` `p0` `backend` `frontend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

结算后需要生成结算单供供应商查看/下载。含订单明细、退款明细、抽成计算过程、最终到账金额。

## 用户故事

作为供应商，我想查看和下载结算单，以便财务对账。作为管理员，我想手动触发结算。

## 任务清单

- [ ] 结算单数据：供应商信息 + 订单明细列表（订单号/产品/数量/金额/收货日期）+ 退款明细 + 抽成计算 + 到账金额
- [ ] `GET /api/settlements` — 供应商查看自己的结算单列表
- [ ] `GET /api/settlements/:id` — 结算单详情
- [ ] `POST /api/settlements/generate` — 管理员手动触发结算
- [ ] Admin 结算管理页：结算单列表/详情

## 验收标准

- 结算单含完整订单明细（订单号、产品、数量、金额）
- 退款明细含退款原因和金额
- 抽成计算过程可追溯
- Admin 点击 "Generate Settlement" → 当月结算单生成

## 相关

PRD §4.1 平台结算模型 | 依赖：13-03 | 父 Issue：[13-payment-settlement](../acceptance-criteria.md)
