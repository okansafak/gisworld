import streamlit as st
import pandas as pd
import geopandas as gpd
from keplergl import KeplerGl

# Başlık
st.title("GeoJSON Verilerini Harita Üzerinde Görüntüleme")

# GeoJSON dosyasını yükleme
uploaded_file = st.file_uploader("Lütfen GeoJSON dosyasını yükleyin", type=["geojson"])

if uploaded_file is not None:
    # GeoDataFrame oluşturma
    gdf = gpd.read_file(uploaded_file)

    # GeoDataFrame'i görselleştirme
    st.subheader("GeoJSON Verileri")
    st.write(gdf)

    # KeplerGl harita oluşturma
    map_ = KeplerGl(height=600)
    map_.add_data(data=gdf, name='geojson_data')

    # Haritayı görüntüleme
    st.write(map_)
