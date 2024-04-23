import streamlit as st
import pandas as pd
import numpy as np

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

# Display map
st.map(df)
