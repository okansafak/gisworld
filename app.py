import streamlit as st
import pydeck as pdk
import geopandas as gpd

# İstanbul'un GeoJSON dosyasını yükle
istanbul_geojson = 'istanbul.geojson'
istanbul_data = gpd.read_file(istanbul_geojson)

# Pydeck için GeoJsonLayer oluştur
geojson_layer = pdk.Layer(
    'GeoJsonLayer',
    data=istanbul_data,
    get_fill_color=[200, 30, 0, 160],  # Rengi belirle (RGB formatında)
    get_line_color=[255, 255, 255],  # Kenar çizgisinin rengi
    lineWidthMinPixels=1,  # Kenar çizgisi kalınlığı
)

# Popup verileri için ColumnLayer oluştur
popup_layer = pdk.Layer(
    "ColumnLayer",
    data=istanbul_data,
    get_position=["geometry.coordinates[0]", "geometry.coordinates[1]"],
    get_elevation=1000,
    get_fill_color=[255, 0, 0],
    auto_highlight=True,
    pickable=True
)

# Harita yapısı oluştur
view_state = pdk.ViewState(
    latitude=41.0082,
    longitude=28.9784,
    zoom=10,
    pitch=40.5,
) 

# Pydeck Haritasını oluştur
r = pdk.Deck(layers=[geojson_layer, popup_layer], initial_view_state=view_state, tooltip={"text": "Bu bir nokta"})

# Streamlit ile göster
st.pydeck_chart(r)
