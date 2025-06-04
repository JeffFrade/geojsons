import json
import geopandas as gpd
from shapely.geometry import Polygon
from pathlib import Path

# Caminho do arquivo original
input_file = "BAIRRO.json"
output_file = "diadema_bairros.geojson"

# Abrir o arquivo JSON
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

features = data["features"]
records = []

# Extrair e converter os dados
for feature in features:
    attrs = feature["attributes"]
    geometry_data = feature.get("geometry")

    if geometry_data and "rings" in geometry_data:
        for ring in geometry_data["rings"]:
            polygon = Polygon(ring)
            records.append({
                "cod_bairro": attrs.get("cod_bairro"),
                "bairro": attrs.get("bairro"),
                "geometry": polygon
            })

# Criar GeoDataFrame
gdf = gpd.GeoDataFrame(records, crs="EPSG:31983")

# Reprojetar para WGS 84
gdf = gdf.to_crs("EPSG:4326")

# Exportar para GeoJSON
gdf.to_file(output_file, driver="GeoJSON")

print(f"GeoJSON gerado com sucesso: {Path(output_file).resolve()}")
