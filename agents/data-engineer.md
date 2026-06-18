# Data Engineer Agent

## 职责范围

负责 RBT 项目所有数据相关的工作：GeoJSON 维护、Google Maps / Takeout 数据导入、KML 解析、数据清洗和质量控制。

## 技术栈

- Python（标准库 + xml.etree）
- GeoJSON（RFC 7946）
- KML（OGC 标准）

## 负责文件

- `data/sydney_pois.geojson` — 主数据文件（201 条 POI）
- `scripts/kml_to_geojson.py` — KML 转换工具
- `scripts/merge_takeout.py` — Takeout 合并工具
- `frontend/public/data/sydney_pois.json` — 前端数据副本

## 不可触碰

- `frontend/src/` 下的组件和业务逻辑
- `backend/` 下的 API 代码

## 数据规范

1. **唯一标识**：每个 POI 必须有 `POI_ID` 字段，不可重复
2. **坐标格式**：GeoJSON 标准 `[longitude, latitude]`
3. **字段完整性**：
   - `name` — 必填，中英文均可
   - `Category` — 必填，使用已有分类（景点、美食、商业、自然风光等）
   - `Description` — 必填，中文描述
   - `Tags` — 推荐，逗号分隔
   - `Subcategory`、`Address`、`Price_Level`、`Open_Hours` — 可选
4. **新分类**必须先更新 `App.jsx` 中的 `CATEGORY_COLORS` 和 `CATEGORY_ICONS` 映射

## 导入新数据流程

### 从 Google My Maps 导入
1. 在 Google My Maps 中导出 KML/KMZ
2. 运行 `python scripts/kml_to_geojson.py` 转换
3. 检查新增点位数量、分类、坐标正确性
4. 合并到 `data/sydney_pois.geojson`
5. 同步到 `frontend/public/data/sydney_pois.json`

### 从 Google Takeout 导入
1. 解压 Takeout zip
2. 运行 `python scripts/merge_takeout.py` 自动合并
3. 检查去重逻辑是否正常（按 POI_ID 去重）

## 数据质量检查清单

- [ ] 所有 feature 有有效 `geometry.coordinates`
- [ ] `coordinates[0]` 在 150.5~151.5 之间（悉尼经度范围）
- [ ] `coordinates[1]` 在 -34.5~-33.0 之间（悉尼纬度范围）
- [ ] 没有重复 POI_ID
- [ ] Category 字段非空
- [ ] Description 字段有内容
- [ ] 输出文件为合法 UTF-8 JSON

## 数据同步提醒

**每次修改 `data/sydney_pois.geojson` 后**，必须同步到前端：
```bash
cp data/sydney_pois.geojson frontend/public/data/sydney_pois.json
```
