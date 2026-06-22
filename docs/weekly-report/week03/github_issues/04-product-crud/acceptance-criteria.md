# Issue 04: Product CRUD API + Image Upload

**Label**: `phase-1` `P0`

## 验收标准

### 产品 CRUD
- [ ] `POST /api/products` — supplier 鉴权
  - 必填：name_zh, category_id, sell_price(USD)
  - 可选：name_en, oem_number, original_price(CNY), description_zh, description_en, specs(JSON), stock, moq
  - 自动绑定 supplier_id → 当前用户，返回 201
- [ ] `GET /api/products` — 公开
  - 分页参数：`?page=1&page_size=20`
  - 筛选：`?category_id=X&price_min=X&price_max=X&supplier_id=X`
  - 返回 `{"data":[...],"pagination":{"page":1,"page_size":20,"total":150,"total_pages":8}}`
- [ ] `GET /api/products/:id` — 公开
  - 返回产品详情 + 图片列表 + 供应商信息（company_name, contact_name, verified）+ 车型适配列表
- [ ] `PUT /api/products/:id` — 仅本 supplier
  - 部分更新（只改传了的字段）
  - 非本人 → 403
- [ ] `DELETE /api/products/:id` — 仅本 supplier，软删除（status=deleted）

### 图片上传
- [ ] `POST /api/products/:id/images` — supplier 鉴权
  - 类型白名单：jpg/png/webp，最大 5MB
  - 上传至 Cloudflare R2，生成唯一文件名
  - 返回 `{"data":{"id":"...","image_url":"https://..."}}`
  - 支持 `sort_order` 和 `is_cover` 参数
  - 非图片格式 → 400 `{"error":"Invalid file type"}`
- [ ] `DELETE /api/products/:id/images/:img_id` — 删除图片（含 R2 文件）

### 车型适配绑定
- [ ] 创建产品时可同时提交 vehicle_fits 数组：
  ```json
  {"vehicle_fits": [{"make":"Toyota","model":"Hilux","year_start":2015,"year_end":2022,"engine":"1GD-FTV","vin_pattern":"MR0*"}]}
  ```

### 测试
- [ ] `test_products.py` 覆盖：创建/查询/更新/删除、权限拒绝、图片上传类型校验
