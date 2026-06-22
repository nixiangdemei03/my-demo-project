# 09-01: Homepage + Search Entry

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

## 背景

采购商落地首页需要三条搜索入口。实现平台名称+定位、VIN/OEM/车型浏览三入口、热门类别快捷入口。

## 用户故事

作为采购商（BUY-02/09/10/11），我想在首页选择搜索方式，以便快速找到配件。

## 任务清单

- [ ] 平台名称 + 一句话定位（中英文）
- [ ] VIN 搜索框（输入→跳转 `/search?vin=...`）
- [ ] OEM/文字搜索框（输入→跳转 `/search?q=...`）
- [ ] 车型浏览入口（品牌→车型→年份级联下拉）
- [ ] 热门类别快捷入口（制动/发动机/悬挂/灯光）
- [ ] 响应式（PC 三栏 / 移动端堆叠）

## 验收标准

- 输入 VIN → 跳转 `/search?vin=JTEHT05JX02...`
- 输入关键词 → 跳转 `/search?q=brake+pad`
- PC 三栏并排、移动端垂直堆叠

## 相关

PRD §3 BUY-02/09/10/11 | 原型：[buyer/01-homepage.html](../../../projects/prototypes/buyer/01-homepage.html) | 依赖：05（Search API） | 父 Issue：[09-frontend-catalog](../acceptance-criteria.md)
