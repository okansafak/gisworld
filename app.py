import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Generate data for metro station locations
metro_stations = {
    "Station": ["Station 1", "Station 2", "Station 3"],
    "Latitude": [41.0082, 41.0447, 41.0175],
    "Longitude": [28.9784, 28.9576, 28.9754],
}

# Generate data for hourly user counts
station_names = metro_stations["Station"]
num_stations = len(station_names)
hours = np.arange(24)

# Repeat station names, latitude, and longitude for each hour
stations = np.repeat(station_names, len(hours))
latitudes = np.repeat(metro_stations["Latitude"], len(hours))
longitudes = np.repeat(metro_stations["Longitude"], len(hours))

# Generate random user counts for each hour and station
user_counts = np.random.randint(100, 1000, size=len(station_names) * len(hours))

# Create the data dictionary
data = {
    "Station": stations,
    "lat": latitudes,  # Change 'Latitude' to 'lat'
    "lon": longitudes,  # Change 'Longitude' to 'lon'
    "Hour": np.tile(hours, num_stations),
    "User_Count": user_counts
}

# Convert data dictionary to DataFrame
df = pd.DataFrame(data)

# Allow user to select multiple stations
selected_stations = st.multiselect("Select Stations", station_names, default=station_names)

# Filter the DataFrame based on selected stations
filtered_df = df[df['Station'].isin(selected_stations)]

# Set default viewport if no stations are selected
if filtered_df.empty:
    viewport = {"latitude": 41.0082, "longitude": 28.9784, "zoom": 10}
else:
    # Create a PyDeck scatter plot layer for the markers
    layer = pdk.Layer(
        "ScatterplotLayer",
        filtered_df,
        get_position='[lon, lat]',
        get_radius=1000,
        get_fill_color=[0, 0, 255],
        pickable=True
    )

    # Set the map viewport to center on the first station
    viewport = pdk.data_utils.compute_view(filtered_df[['lon', 'lat']])

# Create the map
map = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=viewport,
    layers=[layer] if not filtered_df.empty else [],
    tooltip={"text": "{Station}\nHour: {Hour}\nUser Count: {User_Count}"}
)

# Display the map using Streamlit
st.pydeck_chart(map)
