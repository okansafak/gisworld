import streamlit as st
from streamlit_leaflet import st_leaflet

def main():
    # Title of the app
    st.title("Railway Stations on Map")

    # Load GeoJSON data
    with open("rayli_sistem_istasyon_poi_verisi.geojson", "r") as f:
        geojson_data = f.read()

    # Display the map with GeoJSON data
    st_leaflet(geojson_data)

if __name__ == "__main__":
    main()
