import streamlit as st
import pandas as pd
import json

# Load the GeoJSON file containing station data
with open("rayli_sistem_istasyon_poi_verisi.geojson", "r", encoding="utf-8") as f:
    station_data = json.load(f)

# Convert GeoJSON features to DataFrame
features = station_data["features"]
df = pd.json_normalize(features)

# Display a text input for filtering
filter_text = st.text_input("Filter by station name")

# Filter the DataFrame based on the input text
filtered_df = df[df["properties.name"].str.contains(filter_text, case=False)]

# Display the filtered GeoJSON data as a table
st.write("Filtered GeoJSON Data", filtered_df)
