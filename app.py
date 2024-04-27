import streamlit as st
import pandas as pd
import geopandas as gpd
import pydeck as pdk

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

    # PyDeck harita oluşturma
    view_state = pdk.ViewState(
        latitude=gdf.geometry.centroid.y.mean(),
        longitude=gdf.geometry.centroid.x.mean(),
        zoom=10
    )

    layer = pdk.Layer(
        "GeoJsonLayer",
        data=gdf,
        get_fill_color=[0, 255, 0, 100],  # RGB ve alpha değeri
        get_line_color=[255, 0, 0],
        lineWidthScale=5,
        filled=True,
        stroked=True,
    )

    # Haritayı görüntüleme
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=view_state,
        layers=[layer],
    ))
