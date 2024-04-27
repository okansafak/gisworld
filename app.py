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
        "HeatmapLayer",
        data=gdf,
        get_position=["geometry.coordinates[0]", "geometry.coordinates[1]"],
        opacity=0.8,  # Opacity (transparency) of the heatmap layer
        aggregation='"MEAN"',  # Aggregation method for data points within a radius
        get_weight=1,  # Weight for each data point
        radius_scale=20,  # Scaling factor for the radius of each data point
    )

    # Haritayı görüntüleme
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=view_state,
        layers=[layer],
    ))
