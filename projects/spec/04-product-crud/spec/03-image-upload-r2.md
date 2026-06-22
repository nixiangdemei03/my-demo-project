# 04-03: Image Upload to Cloudflare R2

**Labels**: `feat` `p0` `backend` `infra` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

产品需要多图展示。实现图片上传至 Cloudflare R2，支持 jpg/png/webp，max 5MB，可排序设封面。

## 用户故事

作为供应商（SUP-02），我想上传产品图片并设封面，以便采购商查看产品外观。

## 任务清单

- [ ] Cloudflare R2 客户端配置（boto3，环境变量注入 key/secret/endpoint/bucket）
- [ ] `POST /api/products/:id/images` — supplier 鉴权，类型白名单 jpg/png/webp，max 5MB
- [ ] 生成唯一文件名，上传至 R2，保存 URL 到 product_images 表
- [ ] 支持 `sort_order` 和 `is_cover` 参数
- [ ] `DELETE /api/products/:id/images/:img_id` — 删除图片（含 R2 文件）

## 验收标准

- jpg/png/webp → 201 `{"image_url":"https://..."}`
- gif → 400 `"Invalid file type"`
- 超 5MB → 400
- 首张上传图片自动 is_cover=true

## 相关

PRD §4.1 图片上传流程 | 依赖：04-01 | 父 Issue：[04-product-crud](../acceptance-criteria.md)
