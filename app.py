import streamlit as st
import pydeck as pdk
import geopandas as gpd

# İstanbul'un GeoJSON dosyasını yükle
istanbul_geojson = 'istanbul.geojson'
istanbul_data = gpd.read_file(istanbul_geojson)

# Pydeck için GeoJsonLayer oluştur
layer = pdk.Layer(
    'GeoJsonLayer',
    data=istanbul_data,
    get_fill_color=[200, 30, 0, 160],  # Rengi belirle (RGB formatında)
    get_line_color=[255, 255, 255],  # Kenar çizgisinin rengi
    lineWidthMinPixels=1,  # Kenar çizgisi kalınlığı
)

# Harita yapısı oluştur
view_state = pdk.ViewState(
    latitude=41.0082,
    longitude=28.9784,
    zoom=10,
    pitch=40.5,
)

# Pydeck Haritasını oluştur
r = pdk.Deck(layers=[layer], initial_view_state=view_state)

# Streamlit ile göster
st.pydeck_chart(r)
