# Issue 08: Supplier Page + Tax Verification + Warranty Policy

**Label**: `phase-1` `P0`

## 验收标准

### 供应商详情 API
- [ ] `GET /api/suppliers/:id`
  - 返回：company_name, contact_name, country, verified, created_at
  - Logo URL（product_images 中首张）
  - 资质证书列表（supplier_documents 缩略图）
  - 已上架产品数、主营品牌
  - 公司介绍（description）

### 供应商主页模板（注册时）
- [ ] `POST /api/auth/register` 时接受额外字段：
  - Logo 上传（1 张，jpg/png）
  - 公司介绍（TEXT）
  - 主营品牌（多选，如 Toyota/Honda/Nissan/BMW/...）
  - 资质证书上传（多图：营业执照、出口资质、实体店照片、第三方公证书）
  - 联系方式（电话、邮箱、地址）

### 税号 OCR 验证
- [ ] 营业执照上传后自动 OCR 提取：
  - 统一社会信用代码
  - 公司名称
- [ ] 调用天眼查/企查查 API 匹配企业名（¥0.1/次）
  - 匹配成功 → verified = true, verify_status = matched
  - 匹配失败 → verified = false, verify_status = mismatch → 标记人工审核
- [ ] supplier_documents 表 ocr_data JSONB 存储提取结果
- [ ] verify_status 枚举：pending / matched / mismatch / manual_review

### 保修/退换政策
- [ ] 产品创建/编辑表单含：
  - warranty_period（保修期，如"12个月"）
  - return_policy（退换政策，TEXT）
- [ ] 产品详情页对采购商展示保修/退换政策

### 测试
- [ ] `test_supplier.py` 覆盖：供应商详情查询、OCR 提取（mock API）、验证状态流转、保修政策字段
