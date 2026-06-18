# Week 2 Report — nixiangdemei03

## 1. 本周做了什么（事实清单）

- 从 Google My Maps 抓取了蓝岸书 KML 数据，写 Python 脚本（`kml_to_geojson.py`）解析 → 178 条 POI 转成标准 GeoJSON
- 又从 Google Takeout 导出拿了两版 KMZ（原始版 + 国际学生版），写脚本合并去重 → 最终 201 条 POI 入库 `data/sydney_pois.geojson`
- 搭了前端 Mapbox 地图页面：左侧搜索+分类筛选栏 + 右侧 Mapbox GL JS 地图，201 个 marker 按分类分颜色，点 marker 弹详情，点列表飞地图
- 注册了 Mapbox 账号拿 token，配到 `.env`，写了 `.env.example` 模板
- 做了 5 个专用的 Agent 定义文件（frontend / backend / data / devops / reviewer），每个都标了负责范围和不可触碰的边界
- 确认地图方案用 Mapbox GL JS（不用 Leaflet），最终平台目标加 PWA
- 写完 `docs/progress.md` 进度文件，所有模块一目了然
- 完成 6 次 commit，全部推送到 GitHub

## 2. 本周学到了什么（知识 + 反思）

- Google Takeout 导出的 My Maps 数据是 KMZ（压缩版 KML），直接用 `unzip` 解压就能拿到标准 KML。之前以为是个什么私有格式，结果很简单。
- KML 里的 ExtendedData 字段可以很丰富——蓝岸书每条 POI 有 POI_ID、Category、Subcategory、Tags、Price_Level、Open_Hours 甚至 Feedback 链接。这个数据结构直接决定了我 GeoJSON 的 properties 设计。
- Mapbox GL JS 在 Vite 里构建出来 bundle 有 1.99MB（gzipped 560KB），是目前最大的依赖。后续如果做 PWA 需要考虑按需加载。
- 最 aha 的瞬间：Vite 里 `.geojson` 文件不能直接 import，因为 Vite 不认识这个扩展名。试了直接 import 报错之后，改成放到 `public/data/` 下用 `fetch()` 加载，反而更好——数据文件能独立更新，不用重新构建。
- 还没完全搞懂的：Mapbox popup 的 HTML 用模板字符串拼接 handlebars 风格代码，嵌套 backtick 会报 Syntax Error，最后用字符串拼接 `+` 替代模板字符串才过了 Vite 构建。

## 3. AI 协作记录

- 最爽的一次：我说"抓取 Google My Maps"，Claude 直接找到 KML 导出接口（`?mid=xxx` → `/kml?mid=xxx`），curl 下载 → unzip 解压 → Python 解析 → GeoJSON 输出，一条龙。我只需要把 My Maps 链接贴进去，剩下全自动。
- 最坑的一次：Claude 写的 MapView popup 用了嵌套模板字符串 \`\${... \`...\` ...}\`，Vite build 直接报 Syntax Error。我发现错误后指出来，Claude 改成了字符串 `+` 拼接的方案。问题本质是它没考虑到 Vite/esbuild 对嵌套模板字符串的处理。
- 个人套路成形了：描述需求 → Claude 生成文件 → 我审查代码 → Claude build 验证 → 一起 commit。遇到报错把 error log 贴给 Claude，它基本能自己修。

## 4. 决策记录

- 选了 Mapbox 而非 Leaflet：Leaflet 免费但需要自己配 tile 和样式，Mapbox 有 Studio 可视化编辑 + 免费 50k 次/月够了。关键是自定义 marker 样式和商业使用许可更好。
- PWA 作为最终平台目标而非 React Native：当前 React 代码能 80% 复用，先 PWA 验证需求，有必要再 RN。
- Agent 按模块拆分（frontend/backend/data/devops/reviewer）而不是按功能拆分：因为模块边界比功能边界更稳定，跨模块改动是 bug 高发区，agent 文件里直接标了"不可触碰"范围。

## 5. 下周打算

1. 接入 PostgreSQL，创建 users + merchants + events 三张基础表
2. 写用户注册/登录 API（/api/auth/register + /api/auth/login）
3. 把 Mapbox 前端部署到 Cloudflare Pages，给一个公开可访问的 URL

## 6. 资源沉淀

- [Mapbox GL JS Docs](https://docs.mapbox.com/mapbox-gl-js/guides/) — 看完了 marker、popup、flyTo 三个核心 API
- [Google Takeout](https://takeout.google.com/) — Maps 数据导出入口，注意选"Maps (your places)"+ "My Maps"，只导出地图相关数据
- [GeoJSON RFC 7946](https://datatracker.ietf.org/doc/html/rfc7946) — 确认了坐标顺序是 `[longitude, latitude]` 不是反过来的

## 7. 求助 / 卡点

- Cloudflare Pages 部署流程还没跑过。这周只写了 Makefile 占位和 devops agent 的规划。下周目标是把前端至少部署到一个公开 URL。
- Vite build 时 Mapbox 占了 560KB gzipped，后续 PWA 离线缓存需要考虑按需加载策略。
