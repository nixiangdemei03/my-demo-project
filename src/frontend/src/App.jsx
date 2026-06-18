import { useState, useMemo, useEffect } from "react";
import MapView from "./components/MapView";
import "./App.css";

const CATEGORY_COLORS = {
  "美食": "#E65100",
  "景点": "#0288D1",
  "自然风光": "#0F9D58",
  "商业": "#F4B400",
  "购物": "#DB4437",
  "文化场馆": "#7B1FA2",
  "游玩": "#0097A7",
  "城市景点": "#689F38",
  "夜生活": "#C2185B",
  "个人标注": "#FF6D00",
};

const CATEGORY_ICONS = {
  "美食": "🍽️",
  "景点": "🎯",
  "自然风光": "🌿",
  "商业": "🏪",
  "购物": "🛍️",
  "文化场馆": "🏛️",
  "游玩": "🎢",
  "城市景点": "🏙️",
  "夜生活": "🌃",
  "个人标注": "📍",
};

function getCatColor(cat) {
  return CATEGORY_COLORS[cat] || "#757575";
}

function getCatIcon(cat) {
  return CATEGORY_ICONS[cat] || "📌";
}

export default function App() {
  const [pois, setPois] = useState({ type: "FeatureCollection", features: [] });
  const [loading, setLoading] = useState(true);
  const [selectedPoi, setSelectedPoi] = useState(null);
  const [search, setSearch] = useState("");
  const [filterCat, setFilterCat] = useState("全部");

  useEffect(() => {
    fetch("/data/sydney_pois.json")
      .then((r) => r.json())
      .then((data) => setPois(data))
      .catch(() => console.error("Failed to load POIs"))
      .finally(() => setLoading(false));
  }, []);

  const categories = useMemo(() => {
    const cats = new Set();
    pois.features.forEach((f) => {
      const c = f.properties.Category || "其他";
      cats.add(c);
    });
    return ["全部", ...Array.from(cats).sort()];
  }, []);

  const filtered = useMemo(() => {
    return pois.features.filter((f) => {
      const p = f.properties;
      const matchCat = filterCat === "全部" || (p.Category || "其他") === filterCat;
      const matchSearch =
        !search ||
        (p.name || "").toLowerCase().includes(search.toLowerCase()) ||
        (p.Tags || "").toLowerCase().includes(search.toLowerCase()) ||
        (p.Description || "").toLowerCase().includes(search.toLowerCase());
      return matchCat && matchSearch;
    });
  }, [search, filterCat]);

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="sidebar-header">
          <h1>🌏 蓝岸书</h1>
          <p>悉尼留学生地图 · {loading ? "加载中..." : `${pois.features.length} 个地点`}</p>
        </div>

        <div className="sidebar-filters">
          <input
            className="search-input"
            type="text"
            placeholder="搜索地点、标签..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          <select
            className="cat-select"
            value={filterCat}
            onChange={(e) => setFilterCat(e.target.value)}
          >
            {categories.map((c) => (
              <option key={c} value={c}>
                {c === "全部" ? "📂 全部分类" : `${getCatIcon(c)} ${c}`}
              </option>
            ))}
          </select>
        </div>

        <div className="poi-list">
          {filtered.map((f, i) => {
            const p = f.properties;
            const cat = p.Category || "其他";
            const isSelected =
              selectedPoi &&
              selectedPoi.properties.POI_ID === p.POI_ID &&
              selectedPoi.properties.name === p.name;
            return (
              <div
                key={p.POI_ID || i}
                className={`poi-card ${isSelected ? "selected" : ""}`}
                style={{ borderLeftColor: getCatColor(cat) }}
                onClick={() => {
                  setSelectedPoi(f);
                  document
                    .querySelector(".poi-card.selected")
                    ?.scrollIntoView({ behavior: "smooth", block: "nearest" });
                }}
              >
                <div className="poi-card-top">
                  <span className="poi-icon">{getCatIcon(cat)}</span>
                  <div className="poi-card-info">
                    <span className="poi-name">{p.name}</span>
                    <span className="poi-cat" style={{ color: getCatColor(cat) }}>
                      {cat} · {p.Subcategory || ""}
                    </span>
                  </div>
                </div>
                {p.Tags && (
                  <div className="poi-tags">
                    {p.Tags.split("，").map((t) => (
                      <span key={t} className="tag">
                        {t.trim()}
                      </span>
                    ))}
                  </div>
                )}
              </div>
            );
          })}
          {filtered.length === 0 && (
            <div className="no-results">没有匹配的地点</div>
          )}
        </div>
      </aside>

      <main className="map-area">
        <MapView
          pois={filtered}
          selectedPoi={selectedPoi}
          onSelectPoi={setSelectedPoi}
          getCatColor={getCatColor}
          getCatIcon={getCatIcon}
        />
      </main>
    </div>
  );
}
