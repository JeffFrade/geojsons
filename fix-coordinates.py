import geopandas as gpd

input_file = "distritos-sa.geojson"
output_file = "distritos-sa.corrigido.geojson"

print("Lendo arquivo...")
gdf = gpd.read_file(input_file)

print("CRS original:", gdf.crs)

print("Sobrescrevendo CRS para EPSG:32723 (UTM zona 23S) sem alterar geometria...")
gdf = gdf.set_crs(epsg=32723, allow_override=True)

print("Convertendo para EPSG:4326 (WGS84)...")
gdf = gdf.to_crs(epsg=4326)

print(f"Salvando arquivo corrigido em {output_file}...")
gdf.to_file(output_file, driver="GeoJSON")

print("Pronto!")