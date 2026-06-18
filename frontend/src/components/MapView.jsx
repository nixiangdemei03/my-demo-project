import { useEffect, useRef, useState } from "react";
import mapboxgl from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";

const SYDNEY_CENTER = [151.2093, -33.8688]; // Sydney CBD

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

function getColor(cat) {
  return CATEGORY_COLORS[cat] || "#757575";
}

export default function MapView({ pois, selectedPoi, onSelectPoi, getCatColor, getCatIcon }) {
  const mapContainer = useRef(null);
  const mapRef = useRef(null);
  const markersRef = useRef([]);
  const popupRef = useRef(null);
  const [tokenMissing, setTokenMissing] = useState(false);

  // Init map
  useEffect(() => {
    const token = import.meta.env.VITE_MAPBOX_TOKEN;
    if (!token || token === "pk.your_token_here") {
      setTokenMissing(true);
      return;
    }
    mapboxgl.accessToken = token;

    const map = new mapboxgl.Map({
      container: mapContainer.current,
      style: "mapbox://styles/mapbox/light-v11",
      center: SYDNEY_CENTER,
      zoom: 12,
      attributionControl: false,
    });

    map.addControl(new mapboxgl.NavigationControl(), "top-right");
    map.addControl(
      new mapboxgl.AttributionControl({ compact: true }),
      "bottom-right"
    );

    mapRef.current = map;

    return () => map.remove();
  }, []);

  // Update markers when pois change
  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;

    // Clear old markers
    markersRef.current.forEach((m) => m.remove());
    markersRef.current = [];

    // Add new markers
    pois.forEach((feature) => {
      const [lng, lat] = feature.geometry.coordinates;
      if (!lng || !lat) return;

      const p = feature.properties;
      const cat = p.Category || "其他";
      const color = getCatColor ? getCatColor(cat) : getColor(cat);
      const icon = getCatIcon ? getCatIcon(cat) : "📌";

      const el = document.createElement("div");
      el.className = "custom-marker";
      el.innerHTML = `<div class="marker-dot" style="background:${color}">
        <span class="marker-icon">${icon}</span>
      </div>`;
      el.style.cursor = "pointer";

      el.addEventListener("click", () => {
        onSelectPoi(feature);
        if (popupRef.current) popupRef.current.remove();

        const desc = p.Description || "";
        const shortDesc = desc.length > 200 ? desc.slice(0, 200) + "..." : desc;

        // Build tags HTML separately to avoid nested template literal issues
        let tagsHtml = "";
        if (p.Tags) {
          const tags = p.Tags.split("，").map(
            (t) =>
              '<span style="display:inline-block;background:#eee;padding:1px 6px;border-radius:4px;font-size:11px;margin:2px">' +
              t.trim() +
              "</span>"
          );
          tagsHtml = '<p style="margin:4px 0">' + tags.join(" ") + "</p>";
        }

        const html =
          '<div style="font-family:system-ui,sans-serif;max-height:300px;overflow-y:auto">' +
          '<h3 style="margin:0 0 4px;font-size:15px">' + p.name + "</h3>" +
          '<span style="display:inline-block;background:' + color +
          ';color:#fff;padding:2px 8px;border-radius:10px;font-size:11px;margin-bottom:6px">' +
          cat + " · " + (p.Subcategory || "") + "</span>" +
          (shortDesc
            ? '<p style="margin:6px 0;font-size:13px;color:#555;line-height:1.5">' + shortDesc + "</p>"
            : "") +
          (p.Address
            ? '<p style="margin:4px 0;font-size:12px;color:#888">📍 ' + p.Address + "</p>"
            : "") +
          tagsHtml +
          (p.Price_Level
            ? '<p style="margin:2px 0;font-size:12px">💰 ' + p.Price_Level + "</p>"
            : "") +
          (p.Open_Hours
            ? '<p style="margin:2px 0;font-size:12px">🕐 ' + p.Open_Hours + "</p>"
            : "") +
          "</div>";

        const popup = new mapboxgl.Popup({
          offset: 25,
          closeButton: true,
          maxWidth: "320px",
        })
          .setLngLat([lng, lat])
          .setHTML(html)
          .addTo(map);

        popupRef.current = popup;
      });

      const marker = new mapboxgl.Marker({ element: el })
        .setLngLat([lng, lat])
        .addTo(map);

      markersRef.current.push(marker);
    });
  }, [pois, onSelectPoi, getCatColor, getCatIcon]);

  // Fly to selected POI
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !selectedPoi) return;

    const [lng, lat] = selectedPoi.geometry.coordinates;
    if (!lng || !lat) return;

    map.flyTo({ center: [lng, lat], zoom: 15, duration: 1200 });
  }, [selectedPoi]);

  if (tokenMissing) {
    return (
      <div className="map-placeholder">
        <div className="map-placeholder-box">
          <h2>🗺️ Mapbox Token 未配置</h2>
          <ol>
            <li>前往 <a href="https://account.mapbox.com/access-tokens/" target="_blank">mapbox.com → Account → Access Tokens</a></li>
            <li>复制默认 public token（以 <code>pk.</code> 开头）</li>
            <li>粘贴到 <code>frontend/.env</code> 替换 <code>pk.your_token_here</code></li>
            <li>重启 <code>npm run dev</code></li>
          </ol>
          <p style={{marginTop:16,color:'#888'}}>当前显示 {pois.length} 个地点（地图加载中...）</p>
        </div>
      </div>
    );
  }

  return <div ref={mapContainer} className="map-container" />;
}
