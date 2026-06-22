# Issue 04: Product CRUD API + Image Upload

**Labels**: `feat` `p0` `backend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

供应商需要创建和管理产品，采购商通过产品浏览和搜索发现产品。按 PRD §3 用户故事 SUP-02/03/06/10，实现产品 CRUD + Cloudflare R2 图片上传 + 车型适配绑定。

## 用户故事

- 作为供应商（SUP-02），我想创建产品（中/英名称、类别、OEM、价格、规格、图片），以便采购商能搜索到。
- 作为供应商（SUP-03），我想管理库存和上下架，以便避免超卖。
- 作为供应商（SUP-06），我想编辑产品信息，以便保持信息准确。
- 作为供应商（SUP-10），我想写明保修期和退换政策，以便减少售后纠纷。

## 任务清单

- [ ] `POST /api/products` — supplier 鉴权，必填 name_zh/category_id/sell_price，auto 绑定 supplier_id
- [ ] `GET /api/products` — 公开，分页 + 筛选（category/price/supplier）
- [ ] `GET /api/products/:id` — 公开，含图片列表 + 供应商信息 + 车型适配
- [ ] `PUT /api/products/:id` — 仅本 supplier，部分更新
- [ ] `DELETE /api/products/:id` — 仅本 supplier，软删除（status=deleted）
- [ ] `POST /api/products/:id/images` — jpg/png/webp，max 5MB，Cloudflare R2
- [ ] `DELETE /api/products/:id/images/:img_id`
- [ ] 创建产品时支持附带 vehicle_fits 数组
- [ ] 写 `test_products.py` 覆盖 CRUD + 权限 + 图片类型校验

## 验收标准

- `POST /api/products` 合法入参 → 201，supplier_id 自动绑定当前用户
- 未登录 → 401；buyer 角色 → 403
- `GET /api/products` → `{"data":[...],"pagination":{...}}`
- `GET /api/products/:id` → 响应含 `supplier`、`images`、`vehicle_fits`
- `PUT /api/products/:id` 非本人 → 403
- 图片 jpg/png/webp → 201 `{"image_url":"https://..."}` ；gif → 400
- `DELETE` 后 status=deleted，GET 列表不返回

## 相关

- PRD §3：SUP-02/03/06/10、BUY-02/03 | API：`docs/04-api-design.md` | 依赖：Issue 03（Auth）
