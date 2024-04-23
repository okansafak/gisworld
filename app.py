import streamlit as st
import folium

def main():
    # Title of the app
    st.title("Railway Stations on Map")

    # Load GeoJSON data
    with open("rayli_sistem_istasyon_poi_verisi.geojson", "r") as f:
        geojson_data = f.read()

    # Create a folium map centered at a location of your choice
    m = folium.Map(location=[41.0058, 28.8817], zoom_start=10)

    # Add GeoJSON data to the map
    folium.GeoJson(geojson_data).add_to(m)

    # Display the map using folium_static
    st.folium_static(m)

if __name__ == "__main__":
    main()
