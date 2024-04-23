import streamlit as st
import pydeck as pdk
import json

# Load the GeoJSON file containing station data
with open("rayli_sistem_istasyon_poi_verisi.geojson", "r", encoding="utf-8") as f:
    station_data = json.load(f)

# Create a PyDeck map
map = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(latitude=41.0082, longitude=28.9784, zoom=10),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=station_data["features"],
            get_position="[geometry.coordinates[0], geometry.coordinates[1]]",
            get_radius=100,
            get_fill_color=[255, 0, 0],
            pickable=True
        )
    ]
)

# Display the map using Streamlit
st.pydeck_chart(map)
