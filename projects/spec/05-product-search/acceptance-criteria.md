# Issue 05: Product Search — VIN / OEM / Vehicle Browse

**Labels**: `feat` `p0` `backend` `ux` | **Milestone**: v1.0 | **Assignee**: nixiangdemei03

---

## 背景

采购商需要三种方式找到配件：VIN 车架号搜索、OEM 编号精确查找、品牌→车型→年份逐级浏览。按 PRD §3 用户故事 BUY-09/10/11 和 §4.1 配件搜索流程实现。

## 用户故事

- 作为采购商（BUY-09），我想输入 VIN 搜索适配配件，以便精确找到我车型的配件。
- 作为采购商（BUY-10），我想输入 OEM 编号或关键词搜索，以便快速定位特定部件。
- 作为采购商（BUY-11），我想按品牌→车型→年份浏览，以便不熟悉 OEM 号也能找配件。

## 任务清单

- [ ] `GET /api/search?q=` — 全文搜索 name_zh/name_en/oem_number，支持组合筛选
- [ ] `GET /api/search?oem=` — OEM 精确 + 部分匹配，大小写不敏感
- [ ] `POST /api/search/vin` — vin_pattern 前缀匹配，命中/未命中双路径
- [ ] `GET /api/search?make=&model=&year=` — 车型浏览
- [ ] `GET /api/categories` — 层级类别树
- [ ] 写 `test_search.py` 覆盖 7 个场景

## 验收标准

- `GET /api/search?q=刹车片` → 200 + 分页结果
- 无匹配 → `{"data":[],"pagination":{"total":0}}`
- `GET /api/search?oem=04465-0K090` 与 `?oem=04465-0k090` 结果一致
- `?oem=04465` 匹配到 `04465-0K090` 和 `04465-0K120`
- `POST /api/search/vin` 命中 → `{"matched":true,"vehicle":{...},"products":[...]}`
- `POST /api/search/vin` 未命中 → `{"matched":false,"vin":"..."}`
- `GET /api/categories` → 层级树，每节点含 name_zh/name_en/children

## 相关

- PRD §3：BUY-09/10/11 | PRD §4.1 配件搜索流程 | 依赖：Issue 04（Products）
