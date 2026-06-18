"""Convert Google My Maps KML export to GeoJSON for Mapbox."""
import xml.etree.ElementTree as ET
import json
import os

KML_NS = "http://www.opengis.net/kml/2.2"

def find_folder(elem):
    """Walk up the tree to find enclosing Folder name."""
    for parent in ET.ElementTree(elem).iter():
        pass  # Not using iterancestors — walk the whole tree manually
    # Instead, track folder via a recursive approach
    return None


def parse_kml(kml_path):
    tree = ET.parse(kml_path)
    root = tree.getroot()

    features = []
    folder_stack = []

    def walk(el):
        nonlocal folder_stack
        tag = el.tag.split("}")[-1] if "}" in el.tag else el.tag

        if tag == "Folder":
            name_el = el.find(f"{{{KML_NS}}}name")
            folder_name = name_el.text if name_el is not None else ""
            folder_stack.append(folder_name)

        if tag == "Placemark":
            name_el = el.find(f"{{{KML_NS}}}name")
            name = name_el.text if name_el is not None else ""

            desc_el = el.find(f"{{{KML_NS}}}description")
            desc = desc_el.text.strip() if desc_el is not None and desc_el.text else ""

            style_el = el.find(f"{{{KML_NS}}}styleUrl")
            style = style_el.text if style_el is not None else ""

            # Parse coordinates
            coords_el = el.find(f".//{{{KML_NS}}}coordinates")
            lon = lat = None
            if coords_el is not None and coords_el.text:
                parts = coords_el.text.strip().split(",")
                if len(parts) >= 2:
                    try:
                        lon, lat = float(parts[0]), float(parts[1])
                    except ValueError:
                        pass

            # Parse ExtendedData
            props = {
                "name": name,
                "styleUrl": style,
                "Description": desc,
                "folder": folder_stack[-1] if folder_stack else "Root",
            }
            for data in el.findall(f".//{{{KML_NS}}}Data"):
                key = data.get("name", "")
                val_el = data.find(f"{{{KML_NS}}}value")
                val = val_el.text if val_el is not None else ""
                if key:
                    props[key] = val

            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat],
                } if lon is not None else None,
                "properties": props,
            })

        for child in el:
            walk(child)

        if tag == "Folder":
            folder_stack.pop()

    walk(root)
    return features


def main():
    kml_path = os.path.join(os.path.dirname(__file__), "..", "temp_kml", "doc.kml")
    features = parse_kml(kml_path)

    # Stats
    categories = {}
    for f in features:
        cat = f["properties"].get("Category", "Unknown")
        categories[cat] = categories.get(cat, 0) + 1

    valid = sum(1 for f in features if f["geometry"] is not None)

    print(f"Total Placemarks: {len(features)}")
    print(f"With valid coordinates: {valid}")
    print(f"\nCategories:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")

    # Show samples
    print(f"\nSample entries:")
    for f in features[:10]:
        p = f["properties"]
        coords = f["geometry"]["coordinates"] if f["geometry"] else None
        print(f"  [{p.get('Category','?')}] {p['name']} @ {coords}")

    # Write GeoJSON
    geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    out_path = os.path.join(os.path.dirname(__file__), "..", "data", "sydney_pois.geojson")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"\nGeoJSON written to: {out_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
