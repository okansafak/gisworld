import streamlit as st
import pandas as pd
import json

# Load the GeoJSON file containing station data
with open("rayli_sistem_istasyon_poi_verisi.geojson", "r", encoding="utf-8") as f:
    station_data = json.load(f)

# Convert GeoJSON features to DataFrame
features = station_data["features"]
df = pd.json_normalize(features)

# Display the GeoJSON data as a table
st.write("GeoJSON Data", df)
