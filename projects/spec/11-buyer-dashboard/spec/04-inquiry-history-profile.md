# 11-04: Inquiry History + Profile

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商需要查看已发送的询盘和编辑个人信息。实现询盘历史列表和资料编辑页。

## 用户故事

作为采购商（BUY-04/12），我想查看我的询盘历史和供应商回复。

## 任务清单

- [ ] 已发送询盘列表（按时间/状态筛选）
- [ ] 供应商回复详情
- [ ] 个人资料页：查看/编辑（联系人、电话、国家、语言偏好）

## 验收标准

- 询盘状态标签：open / replied / converted / cancelled
- converted 询盘显示对应订单号链接
- 编辑资料 → 保存 → API PUT 成功

## 相关

PRD §3 BUY-04/12 | 依赖：15（Inquiry API） | 父 Issue：[11-buyer-dashboard](../acceptance-criteria.md)
