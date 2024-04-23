import streamlit as st
import pandas as pd
import geopandas as gpd
import folium

# GeoJSON dosyasını içe aktar
@st.cache
def load_data(file_path):
    data = gpd.read_file(file_path)
    return data

# Ana uygulama
def main():
    st.title("GeoJSON Verisi Görselleştirme Uygulaması")
    
    # GeoJSON dosyasını içe aktar
    file_path = st.file_uploader("Lütfen bir GeoJSON dosyası yükleyin", type=["geojson"])
    if file_path is not None:
        # Veriyi yükle
        gdf = load_data(file_path)
        
        # Haritayı göster
        st.subheader("Harita Görüntüleme")
        st.map(gdf)
        
        # Veriyi tablo olarak görüntüle
        st.subheader("Veri Tablosu")
        st.write(gdf)

if __name__ == "__main__":
    main()
