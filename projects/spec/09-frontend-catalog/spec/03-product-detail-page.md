# 09-03: Product Detail Page

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商需要产品详情来做购买决策。实现多图轮播、规格表、车型适配、供应商卡片、保修政策、询问按钮。

## 用户故事

作为采购商（BUY-03），我想查看产品详情（图片、规格、价格、MOQ、供应商信息），以便做出采购决策。

## 任务清单

- [ ] 多图轮播（点击放大）
- [ ] 名称（中/英）+ OEM + 描述
- [ ] 价格：CNY 原价 + USD 售价 + MOQ + 币种选择
- [ ] 规格表（specs JSONB → 键值对渲染）
- [ ] 车型适配列表（品牌/车型/年份/发动机）
- [ ] 供应商卡片（Logo、公司名、verified 徽章）→ 可点击跳转
- [ ] 保修/退换政策展示
- [ ] "发送询问"按钮 → 跳转询盘表单
- [ ] 响应式

## 验收标准

- 图片 ≥3 张可左右切换，点击放大
- 车型适配列表 ≥1 行
- CNY 原价 + USD 售价 + 币种下拉切换
- 点击供应商卡片 → 跳转 `/suppliers/:id`

## 相关

PRD §3 BUY-03/04/12 | 原型：[buyer/03-product-detail.html](../../../projects/prototypes/buyer/03-product-detail.html) | 依赖：04,08 | 父 Issue：[09-frontend-catalog](../acceptance-criteria.md)
