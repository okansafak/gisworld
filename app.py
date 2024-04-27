import streamlit as st
import pandas as pd
import geopandas as gpd
import folium

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

    # Haritayı oluşturma
    m = folium.Map(location=[gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()], zoom_start=10)

    # GeoDataFrame'i haritaya ekleme
    folium.GeoJson(gdf).add_to(m)

    # Haritayı görüntüleme
    folium_static(m)
