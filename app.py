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

# Filter station data for the selected station(s)
filtered_station_data = {
    "type": "FeatureCollection",
    "features": [feature for feature in station_data["features"] if feature["properties"]["ISTASYON"] in selected_stations]
}

# Calculate the bounding box of the filtered points
if filtered_station_data["features"]:
    min_lon, min_lat, max_lon, max_lat = float("inf"), float("inf"), float("-inf"), float("-inf")
    for feature in filtered_station_data["features"]:
        lon, lat = feature["geometry"]["coordinates"]
        min_lon = min(min_lon, lon)
        min_lat = min(min_lat, lat)
        max_lon = max(max_lon, lon)
        max_lat = max(max_lat, lat)
    
    # Calculate the center and zoom level based on the extent
    center_lat = (min_lat + max_lat) / 2
    center_lon = (min_lon + max_lon) / 2
    lat_distance = max_lat - min_lat
    lon_distance = max_lon - min_lon
    zoom = math.floor(12 - math.log2(max(lat_distance, lon_distance) * 111.32)) + 1  # Adjust for padding
else:
    # Default view if no points are filtered
    center_lat, center_lon, zoom = 41.0082, 28.9784, 10

# Create a PyDeck map
map = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(latitude=center_lat, longitude=center_lon, zoom=zoom),
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
