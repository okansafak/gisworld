import streamlit as st
import folium

def main():
    st.title("Harita Üzerinde Çizim Yapma Uygulaması")

    # Haritayı oluştur
    mymap = folium.Map(location=[51.5074, 0.1278], zoom_start=10)

    # Koordinatları al
    lat = st.number_input("Enlem:")
    lon = st.number_input("Boylam:")

    # Marker ekle
    folium.Marker([lat, lon]).add_to(mymap)

    # Streamlit'de haritayı göster
    st.write(mymap)

if __name__ == "__main__":
    main()
