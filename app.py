import streamlit as st
import pandas as pd
import json
import pydeck as pdk
import matplotlib.pyplot as plt

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
data = pd.DataFrame({"HAT_TURU": hat_turu_counts.index, "Count": hat_turu_counts, "Percentage": percentages})

# Plot the pie chart using matplotlib
fig, ax = plt.subplots()
patches, texts, _ = ax.pie(data["Count"], labels=data["HAT_TURU"], autopct="%1.1f%%", startangle=90)
ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

# Convert pie chart patches to labels for Streamlit selectbox
labels = [f"{p.get_label()} ({int(data.loc[i, 'Count'])})" for i, p in enumerate(patches)]

# Allow user to select HAT_TURU
selected_hat_turu = st.selectbox("Select HAT_TURU", labels)

# Filter DataFrame based on selected HAT_TURU
selected_hat_turu = selected_hat_turu.split(" ")[0]  # Extract HAT_TURU from label
filtered_df = df[df["properties.HAT_TURU"] == selected_hat_turu]

# Create a PyDeck map
map = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(latitude=41.0082, longitude=28.9784, zoom=10),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=filtered_df,
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

# Display the filtered data table
st.write("## Filtered Data", filtered_df)
