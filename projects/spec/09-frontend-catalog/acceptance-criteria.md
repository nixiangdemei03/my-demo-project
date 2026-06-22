# Issue 09: Frontend — Homepage, Product Catalog & Detail Pages

**Labels**: `feat` `p0` `frontend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

采购商需要一个可浏览、可搜索的产品目录来发现配件。按 PRD §3 用户故事 BUY-02/03 和原型线框图，实现首页（三种搜索入口）、产品目录（筛选+分页）、产品详情（图片+规格+供应商+询问入口）、供应商详情页、登录注册页。

## 用户故事

- 作为采购商（BUY-02），我想浏览产品目录并按类别/价格/供应商筛选，以便快速找到目标配件。
- 作为采购商（BUY-03），我想查看产品详情（图片、规格、价格、MOQ、供应商信息），以便做出采购决策。

## 任务清单

- [ ] 首页 `/` — 三条搜索入口（VIN / OEM / 车型浏览）+ 热门类别
- [ ] 搜索结果页 `/search` — 列表/网格切换、左侧筛选、分页、URL 参数同步
- [ ] 产品详情页 `/products/:id` — 多图轮播、规格表、车型适配、供应商卡片、保修政策、询问按钮
- [ ] 供应商详情页 `/suppliers/:id` — Logo、介绍、品牌标签、证书、产品列表
- [ ] 登录 `/auth/login` + 注册 `/auth/register` — 表单验证、错误提示
- [ ] PC + 移动端响应式布局

## 验收标准

- 首页输入 VIN → 跳转 `/search?vin=...`
- `/search?q=刹车片&make=Toyota` → URL 参数驱动筛选结果
- `/products/:id` 展示 ≥3 张可切换图片、规格键值表、车型适配列表
- 点击供应商卡片 → 跳转 `/suppliers/:id`
- 注册表单密码 <8 位 → 实时提示 "至少 8 位"
- PC（≥1024px）侧边栏 / 移动端（<768px）顶部搜索

## 相关

- PRD §3：BUY-02/03/04/12 | 原型：`projects/prototypes/buyer/` | 依赖：Issue 04+05（Products + Search API）
