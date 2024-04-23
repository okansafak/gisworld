import streamlit as st
import pydeck as pdk
import json
import math

# Load the GeoJSON file containing station data
with open("rayli_sistem_istasyon_poi_verisi.geojson", "r", encoding="utf-8") as f:
    station_data = json.load(f)

# Extract unique station names
station_names = list(set(feature["properties"]["ISTASYON"] for feature in station_data["features"]))

# Allow user to select station(s)
selected_stations = st.multiselect("Select station(s)", station_names)

# Initialize default values for center latitude, center longitude, and zoom
center_lat = 41.0082
center_lon = 28.9784
zoom = 10

# Filter station data for the selected station(s)
filtered_station_data = {
    "type": "FeatureCollection",
    "features": [feature for feature in station_data["features"] if feature["properties"]["ISTASYON"] in selected_stations]
}

# Calculate the extent of selected stations if there are selected stations
if selected_stations:
    if len(selected_stations) == 1:
        # If only one station is selected, set zoom level to 17
        zoom = 17
    else:
        # If multiple stations are selected, calculate extent and zoom to it
        min_lat = min(feature["geometry"]["coordinates"][1] for feature in filtered_station_data["features"])
        max_lat = max(feature["geometry"]["coordinates"][1] for feature in filtered_station_data["features"])
        min_lon = min(feature["geometry"]["coordinates"][0] for feature in filtered_station_data["features"])
        max_lon = max(feature["geometry"]["coordinates"][0] for feature in filtered_station_data["features"])
        
        # Calculate the center and zoom level based on the extent
        center_lat = (min_lat + max_lat) / 2
        center_lon = (min_lon + max_lon) / 2
        lat_distance = max_lat - min_lat
        lon_distance = max_lon - min_lon
        zoom = math.floor(12 - math.log2(max(lat_distance, lon_distance) * 111.32)) + 1  # Adjust for padding

# Create a PyDeck map
map = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(latitude=center_lat, longitude=center_lon, zoom=zoom),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=filtered_station_data["features"],
            get_position="[geometry.coordinates[0], geometry.coordinates[1]]",
            get_radius=100,
            get_fill_color=[255, 0, 0],
            pickable=True
        )
    ]
)

# Display the map using Streamlit
st.pydeck_chart(map)
