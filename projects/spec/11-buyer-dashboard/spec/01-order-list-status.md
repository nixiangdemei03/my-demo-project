# 11-01: Buyer Order List + Status Display

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商需要查看所有订单。实现订单卡片列表（状态颜色区分）、按状态筛选、分页。

## 用户故事

作为采购商（BUY-05/07），我想查看所有订单状态，以便跟踪采购进度。

## 任务清单

- [ ] 工作台概览：按状态统计（pending/confirmed/paid/shipped/delivered/cancelled）
- [ ] 订单卡片列表：产品缩略图、订单号、供应商、金额、状态标签
- [ ] 状态颜色：灰=pending、蓝=confirmed、绿=paid、橙=shipped、深绿=delivered、红=cancelled
- [ ] 筛选：按状态筛选 + 分页
- [ ] unpaid 订单显示 24h 倒计时 `⏳ HH:MM:SS`

## 验收标准

- 状态标签颜色与规范一致
- 24h 倒计时实时更新
- 点击卡片 → 跳转订单详情

## 相关

PRD §3 BUY-05/07 | 原型：[buyer/07-dashboard.html](../../../projects/prototypes/buyer/07-dashboard.html) | 依赖：06（Orders API） | 父 Issue：[11-buyer-dashboard](../acceptance-criteria.md)
