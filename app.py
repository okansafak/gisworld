import streamlit as st
import pandas as pd
import json
import pydeck as pdk

st.set_page_config(page_title="Demo Page",
                   page_icon=":globe_showing_europe_africa:",
                   layout="wide")

# Load the GeoJSON file containing station data
with open("okullar.geojson", "r", encoding="utf-8") as f:
    station_data = json.load(f)

# Convert GeoJSON features to DataFrame
features = station_data["features"]
df = pd.json_normalize(features)

st.sidebar.header("FILTERS")
ilce = st.sidebar.multiselect(
    "İlçe Seçiniz",
    options=df["properties.ILCE_ADI"].unique(),  # Use unique values for options
    default=None  # Default value is None
)

# Filter DataFrame based on selected ilce if ilce is not empty
if ilce:
    df_selection = df[df["properties.ILCE_ADI"].isin(ilce)]
    st.write("Filtered DataFrame", df_selection)
else:
    df_selection = df

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
if ilce:
    st.write("Filtered DataFrame", df_selection)
