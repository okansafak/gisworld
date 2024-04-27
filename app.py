import streamlit as st
import pydeck as pdk
import geopandas as gpd

# Function to read GeoJSON file
def read_geojson(file):
    gdf = gpd.read_file(file)
    return gdf

# Başlık
st.title("Harita ve Heatmap Editörü")

# Sidebar for uploading GeoJSON file
uploaded_file = st.sidebar.file_uploader("Lütfen GeoJSON dosyasını yükleyin", type=["geojson"])

# Sidebar for heatmap style editor
opacity = st.sidebar.slider("Opaklık", 0.0, 1.0, 0.8)
radius_scale = st.sidebar.slider("Yarıçap Ölçeği", 1, 100, 20)

# PyDeck harita oluşturma
view_state = pdk.ViewState(
    latitude=0,
    longitude=0,
    zoom=2
)

# Map layer
map_layer = pdk.Layer(
    "ScatterplotLayer",
    data=None,
    opacity=opacity,
    get_position="[0, 0]",
    get_radius=radius_scale,
    radius_min_pixels=1,
    get_fill_color=[255, 0, 0],
)

# Map object
map_ = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=view_state,
    layers=[map_layer],
)

# Display the map
st.pydeck_chart(map_)

# Display GeoJSON data if uploaded
if uploaded_file is not None:
    # Read GeoJSON file
    gdf = read_geojson(uploaded_file)

    # Show GeoJSON data
    st.subheader("GeoJSON Verileri")
    st.write(gdf)

    # Update map layer with GeoJSON data
    map_layer.data = gdf.geometry.apply(lambda geom: [geom.x, geom.y]).tolist()
