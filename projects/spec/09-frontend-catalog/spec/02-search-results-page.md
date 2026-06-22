# 09-02: Search Results Page

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商搜索后需要浏览结果。实现列表/网格切换、左侧筛选、产品卡片、分页、URL 参数同步。

## 用户故事

作为采购商（BUY-02），我想按类别/价格/供应商筛选搜索结果，以便快速找到目标配件。

## 任务清单

- [ ] 列表/网格视图切换
- [ ] 左侧筛选栏：类别树、价格区间、供应商
- [ ] 产品卡片（缩略图、名称、OEM、价格、MOQ、供应商 verified 徽章）
- [ ] 分页组件
- [ ] URL 参数同步（`?q=刹车片&make=Toyota&page=1`）
- [ ] 响应式（PC 侧边栏 / 移动端顶部弹出筛选）

## 验收标准

- URL `?q=刹车片&make=Toyota` → 筛选条件自动选中
- 切换网格/列表 → 视图变化但筛选保持
- 空结果 → 显示 "No products found"

## 相关

PRD §3 BUY-02 | 依赖：05（Search API） | 父 Issue：[09-frontend-catalog](../acceptance-criteria.md)
