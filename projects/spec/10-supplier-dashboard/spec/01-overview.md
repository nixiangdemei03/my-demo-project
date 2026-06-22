# 10-01: Supplier Dashboard Overview

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

供应商登录后需要工作台概览。实现统计卡片（产品数/待处理订单/本月销售额）+ 最近订单列表 + 快捷入口。

## 用户故事

作为供应商（SUP-04/08），我想在 Dashboard 看到业务概览，以便快速掌握经营状况。

## 任务清单

- [ ] 概览卡片：产品总数、待处理订单数、本月销售额、预估平台费
- [ ] 最近订单列表（前 5 条）
- [ ] 快捷入口按钮：+添加产品、待处理订单、编辑主页
- [ ] PC 侧边栏导航 / 移动端底部 Tab

## 验收标准

- 概览数据来自 API（products count + orders count + sales sum）
- 点击"待处理订单"→ 跳转订单管理页
- 侧边栏导航所有子页面

## 相关

PRD §3 SUP-04/08 | 原型：[supplier/01-dashboard.html](../../../projects/prototypes/supplier/01-dashboard.html) | 依赖：04+06（Products + Orders API） | 父 Issue：[10-supplier-dashboard](../acceptance-criteria.md)
