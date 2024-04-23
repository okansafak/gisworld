import streamlit as st
import pandas as pd
import json
import pydeck as pdk

# Load the GeoJSON file containing station data
with open("rayli_sistem_istasyon_poi_verisi.geojson", "r", encoding="utf-8") as f:
    station_data = json.load(f)

# Convert GeoJSON features to DataFrame
features = station_data["features"]
df = pd.json_normalize(features)

# Get value counts of HAT_TURU column
hat_turu_counts = df["properties.HAT_TURU"].value_counts()

# Calculate percentages
percentages = (hat_turu_counts / hat_turu_counts.sum()) * 100

# Create a DataFrame with counts and percentages
data = pd.DataFrame({"Count": hat_turu_counts, "Percentage": percentages})

# Plot the pie chart using streamlit.pyplot
st.write("## Distribution of HAT_TURU")
fig, ax = st.pyplot()
ax.pie(data["Count"], labels=data.index, autopct="%1.1f%%", startangle=90)
ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the data table
st.write("## HAT_TURU Data", data)

# Create a PyDeck map
map = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(latitude=41.0082, longitude=28.9784, zoom=10),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=station_data["features"],
            get_position="[geometry.coordinates[0], geometry.coordinates[1]]",
            get_radius=200,
            get_fill_color=[255, 0, 0],
            pickable=True
        )
    ]
)

# Display the map using Streamlit
st.write("## Map")
st.pydeck_chart(map)
