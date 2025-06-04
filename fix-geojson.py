import json
import codecs

def corrigir_geojson(entrada, saida):
    with codecs.open(entrada, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if data.get("type") != "FeatureCollection":
        raise Exception("Não é FeatureCollection")

    novas_features = []
    for feature in data.get("features", []):
        if feature.get("type") != "Feature":
            continue
        geometry = feature.get("geometry", {})
        if not geometry.get("type") or not geometry.get("coordinates"):
            continue
        novas_features.append(feature)

    with codecs.open(saida, 'w', encoding='utf-8') as f:
        json.dump({
            "type": "FeatureCollection",
            "features": novas_features
        }, f, ensure_ascii=False, separators=(',', ':'))

corrigir_geojson("distritos-sa.geojson", "distritos-sa_corrigido.geojson")
corrigir_geojson("distritos-sbc.geojson", "distritos-sbc_corrigido.geojson")