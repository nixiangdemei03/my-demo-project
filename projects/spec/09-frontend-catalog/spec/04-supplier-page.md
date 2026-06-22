# 09-04: Supplier Detail Page

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商需要了解供应商资质和产品。实现 Logo、公司介绍、品牌标签、资质缩略图、产品列表。

## 用户故事

作为采购商（BUY-03），我想查看供应商详情，以便决定是否信任并下单。

## 任务清单

- [ ] Logo + 公司名 + verified 状态徽章
- [ ] 公司介绍 + 主营品牌标签
- [ ] 资质证书缩略图
- [ ] 该供应商产品列表（分页）
- [ ] 响应式

## 验收标准

- `/suppliers/:id` → 含 Logo、company_name、verified、description、main_brands、product_count
- 点击产品 → 跳转 `/products/:id`

## 相关

PRD §3 BUY-03, SUP-09 | 依赖：08（Supplier Page API） | 父 Issue：[09-frontend-catalog](../acceptance-criteria.md)
