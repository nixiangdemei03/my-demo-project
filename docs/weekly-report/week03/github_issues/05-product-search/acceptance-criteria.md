# Issue 05: Product Search — VIN / OEM / Vehicle Browse

**Label**: `phase-1` `P0`

## 验收标准

### 文字搜索
- [ ] `GET /api/search?q=刹车片`
  - 全文搜索 name_zh, name_en, oem_number
  - 支持组合参数：`&make=Toyota&model=Hilux&year=2020&category_id=X`
  - 返回分页结果
  - 空结果 → `{"data":[],"pagination":{"total":0}}`

### OEM 精确搜索
- [ ] `GET /api/search?oem=04465-0K090`
  - 精确匹配 oem_number 字段
  - 大小写不敏感
  - 支持部分匹配（如 `04465` 匹配 `04465-0K090` 和 `04465-0K120`）

### VIN 搜索
- [ ] `POST /api/search/vin`
  - 入参：`{"vin":"JTELV71J800012345"}`
  - 用 `vin_pattern` 前缀匹配 `product_vehicle_fits` 表
  - 命中 → 返回 `{"matched":true,"vehicle":{"make":"Toyota","model":"Land Cruiser Prado",...},"products":[...]}`
  - 未命中 → 返回 `{"matched":false,"vin":"JTELV71J8..."}`（后续透传询问订单）

### 车型浏览
- [ ] `GET /api/search?make=Toyota&model=Hilux&year=2020`
  - 通过 product_vehicle_fits 筛选产品
  - 支持只传 make（返回该品牌所有适配产品）

### 类别树
- [ ] `GET /api/categories` — 返回层级类别树
  ```json
  [{"id":"...","name_zh":"制动系统","name_en":"Brake System","children":[...]},...]
  ```

### 测试
- [ ] `test_search.py` 覆盖：中文搜索、OEM 精确匹配、OEM 部分匹配、VIN 命中、VIN 未命中、车型筛选、空结果
