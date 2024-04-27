import streamlit as st
import geopandas as gpd
import pandas as pd
import pydeck as pdk

# Function to read GeoJSON, KML, and Shapefile
def read_file(file):
    if file.type == "application/vnd.google-earth.kml+xml":
        gdf = gpd.read_file(file)
    elif file.type == "application/geo+json":
        gdf = gpd.read_file(file)
    elif file.type == "application/octet-stream":
        gdf = gpd.read_file(file)
    return gdf

# Function to read CSV with X and Y coordinates
def read_csv(file, x_col, y_col, epsg):
    df = pd.read_csv(file)
    geometry = gpd.points_from_xy(df[x_col], df[y_col])
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:" + str(epsg))
    return gdf

# Başlık
st.title("Harita ve Veri İçe Aktarma")

# Seçenekler
file_type = st.sidebar.selectbox("Dosya Türü Seçin", ["GeoJSON", "KML", "Shapefile", "CSV"])
uploaded_file = st.sidebar.file_uploader("Dosyayı Yükleyin")

if uploaded_file is not None:
    if file_type == "CSV":
        x_col = st.sidebar.selectbox("X Koordinat Sütunu Seçin", df.columns)
        y_col = st.sidebar.selectbox("Y Koordinat Sütunu Seçin", df.columns)
        epsg = st.sidebar.number_input("EPSG Kodu Girin", value=4326)
        gdf = read_csv(uploaded_file, x_col, y_col, epsg)
    else:
        gdf = read_file(uploaded_file)



    # PyDeck harita oluşturma
    view_state = pdk.ViewState(latitude=gdf.geometry.centroid.y.mean(), longitude=gdf.geometry.centroid.x.mean(), zoom=10)
    layer = pdk.Layer("ScatterplotLayer", data=gdf, get_position="[geometry.x, geometry.y]", get_color=[255, 0, 0], get_radius=100)
    map_ = pdk.Deck(map_style="mapbox://styles/mapbox/light-v9", initial_view_state=view_state, layers=[layer])

    # Haritayı görüntüleme
    st.pydeck_chart(map_)
