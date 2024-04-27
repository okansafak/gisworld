import streamlit as st
import pandas as pd
import json
import pydeck as pdk

st.set_page_config(page_title="Demo Page",
                   page_icon=":globe_showing_europe_africa:",
                   layout="wide")

# Load the GeoJSON file containing school data
with open("okullar.geojson", "r", encoding="utf-8") as f:
    school_data = json.load(f)

# Convert GeoJSON features to DataFrame
features = school_data["features"]
df = pd.json_normalize(features)

# Extract unique districts for the sidebar filter
unique_ilce = df["properties.ILCE_ADI"].unique()

# Sidebar for filters
st.sidebar.header("FILTERS")
il = st.sidebar.selectbox("İl Seçiniz", options=df["properties.IL_ADI"].unique())
ilce = st.sidebar.multiselect("İlçe Seçiniz", options=unique_ilce)

# Filter DataFrame based on selected ilce and il if they are not empty
if ilce:
    df_selection = df[df["properties.ILCE_ADI"].isin(ilce)]
    if il:
        df_selection = df_selection[df_selection["properties.IL_ADI"] == il]
    st.write("Filtered DataFrame", df_selection)
else:
    df_selection = df
    if il:
        df_selection = df_selection[df_selection["properties.IL_ADI"] == il]

# Define a custom layer for the map
custom_layer = pdk.Layer(
    "ScatterplotLayer",
    data=df_selection,
    get_position="[properties.MERKEZ_Y, properties.MERKEZ_X]",
    get_radius=200,
    get_fill_color=[255, 0, 0],
    pickable=True
)

# Create a PyDeck map
map = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(latitude=41.0082, longitude=28.9784, zoom=10),
    layers=[custom_layer]
)

# Display the map using Streamlit
st.write("## Map")
st.pydeck_chart(map)

# Display filtered data if ilce is selected
if ilce or il:
    st.write("Filtered DataFrame", df_selection)
