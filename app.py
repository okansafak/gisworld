import streamlit as st
import geopandas as gpd
import folium

def main():
    st.title("İstanbul'daki Okulların Haritası")

    # GeoJSON dosyasını yükle
    gdf = gpd.read_file("okullar.geojson")

    # İstanbul'daki okulları filtrele
    istanbul_gdf = gdf[gdf['IL_ADI'] == 'KARS']

    # Merkezi noktayı hesapla
    center_lat = istanbul_gdf.geometry.centroid.y.mean()
    center_lon = istanbul_gdf.geometry.centroid.x.mean()

    # Folium haritası oluştur
    m = folium.Map(location=[center_lat, center_lon], zoom_start=10, control_scale=True)

    # İstanbul'daki okul konumlarını haritaya ekle
    for idx, row in istanbul_gdf.iterrows():
        folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row["Okul Adı"]).add_to(m)

    # Streamlit ile haritayı görüntüle
    st.write("İstanbul'daki okulların haritası:")
    folium_static(m)

if __name__ == "__main__":
    main()
