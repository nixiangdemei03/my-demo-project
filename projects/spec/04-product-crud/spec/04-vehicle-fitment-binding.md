# 04-04: Vehicle Fitment Binding

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

产品需要绑定适配车型，VIN 搜索才能命中。创建产品时可同时提交 vehicle_fits 数组。

## 用户故事

作为供应商，我想标注产品适配哪些车型（品牌/车型/年份/发动机），以便采购商通过 VIN 和车型浏览找到。

## 任务清单

- [ ] 创建产品时接受 `vehicle_fits` 数组参数
- [ ] 写入 product_vehicle_fits 表（make, model, year_start, year_end, engine, vin_pattern）
- [ ] 产品详情返回 vehicle_fits 列表

## 验收标准

- 创建产品附带 `[{"make":"Toyota","model":"Hilux","year_start":2015,"year_end":2022,"engine":"1GD-FTV","vin_pattern":"MR0*"}]` → 201，product_vehicle_fits 表有对应记录
- 产品详情 vehicle_fits 数组非空

## 相关

PRD §4.1 配件搜索流程 | 依赖：04-01 | 父 Issue：[04-product-crud](../acceptance-criteria.md)
