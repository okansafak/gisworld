import streamlit as st
import json
from streamlit_folium import folium_static
import folium

# Read the GeoJSON file
with open("istanbul.geojson", "r") as f:
    geojson_data = json.load(f)

# Extract coordinates and properties
features = geojson_data["features"]
coordinates = [(feature["geometry"]["coordinates"][1], feature["geometry"]["coordinates"][0]) for feature in features]
properties = [feature["properties"] for feature in features]

# Create a Streamlit map
st.title("Points on Map")
m = folium.Map(location=[41, 29], zoom_start=10)  # Set initial location and zoom level

# Add points to the map
for coord, prop in zip(coordinates, properties):
    popup = folium.Popup("<b>{}</b><br>{}".format(prop["KURUM_ADI"], prop["ADRES"]), parse_html=True)
    folium.Marker(location=coord, popup=popup).add_to(m)

# Display the map
folium_static(m)
