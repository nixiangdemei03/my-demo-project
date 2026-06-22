# 15-01: Inquiry Create + Query API

**Labels**: `feat` `p0` `backend` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

APEX 核心差异化：采购商先询问再下单。实现 inquiries 表完整 schema 和创建/查询 API，区分轻量 message 和结构化 inquiry。

## 用户故事

作为采购商（BUY-04/12），我想发送询盘（轻量消息或结构化询问），以便在购买前确认细节。

## 任务清单

- [ ] inquiries 表 schema（inquiry_type: message/inquiry, status: open/replied/converted/cancelled, OEM/VIN/图片字段）
- [ ] `POST /api/inquiries` — buyer 发送询盘，type=inquiry 含结构化字段
- [ ] `GET /api/inquiries` — 收/发件箱，按 type + status 筛选
- [ ] `PATCH /api/inquiries/:id/read` — 标记已读

## 验收标准

- type=inquiry → 201，含 OEM/VIN/quantity/image_urls 字段
- type=message → 201，仅 message 文本字段
- `GET` → 按 role 过滤（buyer 看自己发的，supplier 看自己收到的）

## 相关

PRD §3 BUY-04/12 | 依赖：03（Auth） | 父 Issue：[15-inquiry-to-order](../acceptance-criteria.md)
