import streamlit as st
import geopandas as gpd

def main():
    st.title("Okullar Harita Uygulaması")

    # Veriyi yükle
    okullar_data = gpd.read_file("okullar.geojson")

    # İl ve ilçelerin verileri
    iller_ilceler = {}
    for index, row in okullar_data.iterrows():
        il = row['IL_ADI']
        ilce = row['ILCE_ADI']
        if il not in iller_ilceler:
            iller_ilceler[il] = []
        if ilce not in iller_ilceler[il]:
            iller_ilceler[il].append(ilce)

    # İl seçme kutusu
    secilen_il = st.sidebar.selectbox("Bir il seçin", list(iller_ilceler.keys()))

    # Seçilen ilin ilçeleri
    secilen_ilceler = iller_ilceler[secilen_il]

    # Seçilen ilin ilçelerini göster
    secilen_ilce = st.sidebar.selectbox("Bir ilçe seçin", secilen_ilceler)

if __name__ == "__main__":
    main()
