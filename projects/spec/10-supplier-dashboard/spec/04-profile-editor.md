# 10-04: Supplier Profile Editor + Inquiries

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

供应商需要编辑主页信息和回复询盘。实现模板表单+实时预览，以及询盘收件箱。

## 用户故事

作为供应商（SUP-09），我想编辑公司主页信息并实时预览，以及回复采购商的询盘。

## 任务清单

- [ ] 主页编辑表单：Logo 上传、公司介绍、主营品牌多选、资质证书上传、联系方式
- [ ] 右侧实时预览（供应商详情页效果）
- [ ] 询盘收件箱：未读标记、时间排序
- [ ] 询盘详情 + 回复框

## 验收标准

- 编辑表单 → 右侧实时同步更新预览
- Logo 上传 → 预览显示新 Logo
- 询盘未读 → 加粗 + 红点标记

## 相关

PRD §3 SUP-09, BUY-04/12 | 原型：[supplier/04-profile.html](../../../projects/prototypes/supplier/04-profile.html) | 依赖：08+15 | 父 Issue：[10-supplier-dashboard](../acceptance-criteria.md)
