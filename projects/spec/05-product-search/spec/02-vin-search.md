# 05-02: VIN Search API

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商输入 17 位 VIN 车架号查找适配配件。用 vin_pattern 前缀匹配 product_vehicle_fits 表，命中返回车辆信息+配件列表，未命中返回 matched=false。

## 用户故事

作为采购商（BUY-09），我想输入 VIN 搜索适配配件，以便精确找到我车型的配件。

## 任务清单

- [ ] `POST /api/search/vin` — 入参 `{"vin":"JTELV71J800012345"}`
- [ ] vin_pattern 前缀匹配 product_vehicle_fits
- [ ] 命中 → `{"matched":true,"vehicle":{...},"products":[...]}`
- [ ] 未命中 → `{"matched":false,"vin":"..."}`
- [ ] VIN 长度校验（≠17 → 400）

## 验收标准

- 命中 VIN → 返回 vehicle（make/model/year/engine）+ products 列表
- 未命中 VIN → `{"matched":false}`，采购商仍可下单附带 VIN
- 非法 VIN → 400

## 相关

PRD §3 BUY-09 | PRD §4.1 方式 1 | 依赖：04-04 | 父 Issue：[05-product-search](../acceptance-criteria.md)
