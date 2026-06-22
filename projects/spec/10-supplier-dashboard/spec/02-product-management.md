# 10-02: Product Management (List + Add + Edit)

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

供应商需要管理产品。实现产品列表（搜索/分页/状态筛选）、添加表单（图片拖拽上传+车型绑定+保修字段）、编辑（预填充）、下架。

## 用户故事

作为供应商（SUP-02/03/06/10），我想在一个界面管理所有产品。

## 任务清单

- [ ] 产品列表：搜索、分页、按 active/inactive 筛选
- [ ] 添加表单：名称中/英、类别下拉、OEM、CNY 原价/USD 售价、MOQ、库存
- [ ] 规格键值对动态添加行
- [ ] 车型适配绑定（品牌/车型/年份起止/发动机/VIN pattern 动态行）
- [ ] 图片拖拽上传（预览、排序、设封面）
- [ ] 保修期 + 退换政策字段
- [ ] 编辑页：预填充所有字段，可增删图片
- [ ] 下架确认弹窗

## 验收标准

- 拖拽图片 → 缩略图预览 → 拖动排序
- 车型适配可添加/删除多行
- 编辑页所有字段预填充
- 下架 → 确认弹窗 → product.status=deleted

## 相关

PRD §3 SUP-02/03/06/10 | 原型：[supplier/02-product-form.html](../../../projects/prototypes/supplier/02-product-form.html) | 依赖：04（Products API） | 父 Issue：[10-supplier-dashboard](../acceptance-criteria.md)
