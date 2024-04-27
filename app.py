import streamlit as st
import pandas as pd
import geopandas as gpd
from streamlit_folium import folium_static
from streamlit_leaflet import st_leaflet

# Veri yüklemesi
@st.cache
def load_data():
    # Okulların GeoJSON dosyasını yükle
    schools_gdf = gpd.read_file("turkiye.geojson")
    return schools_gdf

schools_gdf = load_data()

# İl ve İlçe seçimi
selected_province = st.sidebar.selectbox("İl Seçin", schools_gdf["IL_ADI"].unique())
selected_districts = schools_gdf[schools_gdf["IL_ADI"] == selected_province]["ILCE_ADI"].unique()
selected_district = st.sidebar.selectbox("İlçe Seçin", selected_districts)

# Seçilen il ve ilçeye göre veriyi filtrele
filtered_schools = schools_gdf[(schools_gdf["IL_ADI"] == selected_province) & (schools_gdf["ILCE_ADI"] == selected_district)]

# Haritayı oluştur
m = st_leaflet(width=800, height=600)

# Okul noktalarını haritaya ekle
for idx, row in filtered_schools.iterrows():
    popup_html = f"<b>Okul Adı:</b> {row['KURUM_ADI']}"
    m.add_marker((row.geometry.y, row.geometry.x), popup=popup_html)

# Haritayı görüntüle
st.subheader("Türkiye Genelinde Okulların Isı Haritası ve Noktaları")
folium_static(m)
