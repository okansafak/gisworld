import streamlit as st
import pydeck as pdk
import json

# Load the GeoJSON file containing station data
with open("rayli_sistem_istasyon_poi_verisi.geojson", "r", encoding="utf-8") as f:
    station_data = json.load(f)

# Extract unique station names
station_names = list(set(feature["properties"]["ISTASYON"] for feature in station_data["features"]))

# Allow user to select station(s)
selected_stations = st.multiselect("Select station(s)", station_names)

# Filter station data for the selected station(s)
filtered_station_data = {
    "type": "FeatureCollection",
    "features": [feature for feature in station_data["features"] if feature["properties"]["ISTASYON"] in selected_stations]
}

# Create a PyDeck map
map = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(latitude=41.0082, longitude=28.9784, zoom=10),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=filtered_station_data["features"],
            get_position="geometry.coordinates",
            get_radius=100,
            get_fill_color=[255, 0, 0],
            pickable=True,
            tooltip={"text": "{ISTASYON}\n{PROJE_ADI}\n{PROJE_ASAMA}\n{HAT_TURU}\n{MUDURLUK}"}
        )
    ]
)

# Display the map using Streamlit
st.pydeck_chart(map)
