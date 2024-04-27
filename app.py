import streamlit as st
import geopandas as gpd
import folium

def main():
    st.title("Okullar Haritası")

    # GeoJSON dosyasını yükle
    gdf = gpd.read_file("okullar.geojson")

    # Merkezi noktayı hesapla
    center_lat = gdf.geometry.centroid.y.mean()
    center_lon = gdf.geometry.centroid.x.mean()

    # Folium haritası oluştur
    m = folium.Map(location=[center_lat, center_lon], zoom_start=10, control_scale=True)

    # Okul konumlarını haritaya ekle
    for idx, row in gdf.iterrows():
        folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row["Okul Adı"]).add_to(m)

    # Streamlit ile haritayı görüntüle
    folium_static(m)

if __name__ == "__main__":
    main()
