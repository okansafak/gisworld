import streamlit as st
import pandas as pd
import folium

# Veri yükleyici fonksiyon
@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Ana uygulama fonksiyonu
def main():
    st.title('CBS Harita Uygulaması')

    # Veri yükleme
    file_path = st.file_uploader("Lütfen bir CSV dosyası yükleyin", type=["csv"])
    if file_path is not None:
        data = load_data(file_path)
        st.write(data)

        # Harita oluşturma
        st.subheader("Harita Görüntüleme")
        map_data = data[['Latitude', 'Longitude']] # Varsayılan olarak 'Latitude' ve 'Longitude' sütunlarını kullanıyoruz
        map_center = [map_data['Latitude'].mean(), map_data['Longitude'].mean()] # Harita merkezini veri noktalarının ortalaması olarak ayarlıyoruz
        my_map = folium.Map(location=map_center, zoom_start=10)

        # Her veri noktasını haritaya ekleme
        for index, row in map_data.iterrows():
            folium.Marker(location=[row['Latitude'], row['Longitude']]).add_to(my_map)

        # Haritayı görüntüleme
        folium_static(my_map)

if __name__ == "__main__":
    main()
