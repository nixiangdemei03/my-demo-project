# Issue 08: Supplier Page + Manual Verification + Warranty Policy

**Labels**: `feat` `p0` `backend` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

供应商需要展示主页以建立采购商信任。按 PRD §3 用户故事 SUP-09/10 和 §4.1 供应商上架流程，实现供应商详情 API、主页模板、人工资质审核。v1.0 使用人工审核（营业执照 + 实店照片 + 销售许可证），不接入天眼查 OCR。

## 用户故事

- 作为供应商（SUP-09），我想使用固定模板搭建主页（Logo、公司介绍、资质证书、联系方式），以便采购商信任我的公司。
- 作为供应商（SUP-10），我想在产品页写明保修期和退换政策，以便减少售后纠纷。
- 作为管理员（ADM-01），我想人工审核供应商上传的证照，以便防止虚假供应商入驻。

## 任务清单

- [ ] `GET /api/suppliers/:id` — 返回公司信息、Logo、资质缩略图、产品数、主营品牌
- [ ] 注册时接受额外字段：Logo、公司介绍、主营品牌、资质证书上传、联系方式
- [ ] 管理员审核队列：查看证照 → Approve / Reject / Request More Info
- [ ] supplier_documents 表 verify_status：pending / approved / rejected
- [ ] 产品表单含 warranty 和 return_policy 字段
- [ ] 写 `test_supplier.py` 覆盖详情查询、审核状态流转、保修字段

## 验收标准

- `GET /api/suppliers/:id` → 含 company_name、logo_url、description、main_brands、verified、product_count
- 资质文件上传后 verify_status=pending → 管理员 Approve → verified=true
- Reject 需附 review_note 原因
- 产品详情页展示保修期和退换政策（从 products.warranty / return_policy 读取）

## 相关

- PRD §3：SUP-09/10、ADM-01 | PRD §4.1 供应商上架流程 | 依赖：Issue 03（Auth）
