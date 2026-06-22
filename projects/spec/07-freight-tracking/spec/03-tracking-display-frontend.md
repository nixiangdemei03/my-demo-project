# 07-03: Tracking Display (Frontend)

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商和供应商都需要在订单详情中看到货运追踪。实现在 Buyer Dashboard 和 Supplier Dashboard 中嵌入追踪时间线。

## 用户故事

作为采购商（BUY-06），我想在订单详情中看到物流追踪时间线。

## 任务清单

- [ ] Buyer 订单详情：货运追踪时间线（事件描述+地点+时间）
- [ ] 显示货运公司名称 + 运单号
- [ ] Supplier 订单详情：同样的追踪视图 + "添加追踪事件"按钮
- [ ] 估计送达日期展示

## 验收标准

- 追踪事件按时间倒序排列
- "添加追踪事件" → 输入框 + 提交 → 列表实时更新
- 无追踪事件 → 显示 "No tracking events yet"

## 相关

PRD §3 BUY-06, SUP-07 | 依赖：07-02, 11-02, 10-03 | 父 Issue：[07-freight-tracking](../acceptance-criteria.md)
