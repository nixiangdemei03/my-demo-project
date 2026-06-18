"""Merge Takeout data: two KMZ versions + labelled places → combined GeoJSON."""
import xml.etree.ElementTree as ET
import json
import os

KML_NS = "http://www.opengis.net/kml/2.2"


def parse_kml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    features = []
    folder_stack = []

    def walk(el):
        tag = el.tag.split("}")[-1] if "}" in el.tag else el.tag
        if tag == "Folder":
            n = el.find(f"{{{KML_NS}}}name")
            folder_stack.append(n.text if n is not None else "")

        if tag == "Placemark":
            name_el = el.find(f"{{{KML_NS}}}name")
            name = name_el.text if name_el is not None else ""

            desc_el = el.find(f"{{{KML_NS}}}description")
            desc = desc_el.text.strip() if desc_el is not None and desc_el.text else ""

            coords_el = el.find(f".//{{{KML_NS}}}coordinates")
            lon = lat = None
            if coords_el is not None and coords_el.text:
                parts = coords_el.text.strip().split(",")
                if len(parts) >= 2:
                    try:
                        lon, lat = float(parts[0]), float(parts[1])
                    except ValueError:
                        pass

            props = {
                "name": name,
                "Description": desc,
                "folder": folder_stack[-1] if folder_stack else "Root",
                "source_file": os.path.basename(path),
            }
            for data in el.findall(f".//{{{KML_NS}}}Data"):
                key = data.get("name", "")
                v = data.find(f"{{{KML_NS}}}value")
                props[key] = v.text if v is not None else ""

            features.append({
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [lon, lat]} if lon else None,
                "properties": props,
            })

        for child in el:
            walk(child)

        if tag == "Folder":
            folder_stack.pop()

    walk(root)
    return features


def main():
    base = os.path.join(os.path.dirname(__file__), "..")

    # Parse both KMZ versions
    f1 = parse_kml(os.path.join(base, "temp_kmz1", "doc.kml"))
    f2 = parse_kml(os.path.join(base, "temp_kmz2", "doc.kml"))

    print(f"Blue Coast Book (original):           {len(f1)} placemarks")
    print(f"Blue Coast Book (Int'l students):     {len(f2)} placemarks")

    # Merge by POI_ID, preferring the version with more data
    seen = {}
    for f in f2 + f1:  # Int'l students first (has more data), then original
        pid = f["properties"].get("POI_ID", "") or f["properties"]["name"]
        if pid not in seen:
            seen[pid] = f
        else:
            # Merge: fill empty fields from the other version
            existing = seen[pid]["properties"]
            new = f["properties"]
            for k, v in new.items():
                if k in existing and not existing[k] and v:
                    existing[k] = v

    merged = list(seen.values())
    print(f"After dedup:                          {len(merged)} unique placemarks")

    # Add labelled places from Takeout (user's personal saved places)
    labelled_path = os.path.join(base, "temp_takeout", "Takeout", "Maps",
                                 "My labelled places", "Labelled places.json")
    labelled = []
    if os.path.exists(labelled_path):
        with open(labelled_path, "r") as f:
            data = json.load(f)
        for feat in data.get("features", []):
            feat["properties"]["source_file"] = "labelled_places"
            feat["properties"]["Category"] = "个人标注"
            labelled.append(feat)
        print(f"Labelled places added:                {len(labelled)}")

    all_features = merged + labelled

    # Stats
    cats = {}
    for f in all_features:
        cat = f["properties"].get("Category", "Unknown") or "Unknown"
        cats[cat] = cats.get(cat, 0) + 1

    print(f"\nFinal total: {len(all_features)} features")
    print(f"Categories:")
    for cat, n in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {n}")

    # Write output
    out_path = os.path.join(base, "data", "sydney_pois.geojson")
    geojson = {"type": "FeatureCollection", "features": all_features}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)
    print(f"\nWritten: {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")


if __name__ == "__main__":
    main()
