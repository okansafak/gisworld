import json
import streamlit as st
import geopandas as gpd

# Okullar GeoJSON dosyasını yükle
with open("okullar.geojson", encoding="utf-8") as f:
    okullar_geojson = json.load(f)

# İl ve ilçe listesi JSON dosyasını yükle
with open("il_ilce_listesi.json", encoding="utf-8") as f:
    il_ilce_listesi = json.load(f)

# Geopandas DataFrame'i oluştur
okullar_gdf = gpd.GeoDataFrame.from_features(okullar_geojson["features"])

# Streamlit uygulamasını oluştur
st.title("Okul Bilgi Uygulaması")

# Filtreler için sidebar oluştur
st.sidebar.title("Filtreler")

# İl seçimini sidebar'a ekle
secili_il = st.sidebar.selectbox("İl Seçin", list(il_ilce_listesi.keys()))

# İlçe seçimini sidebar'a ekle
secili_ilce = st.sidebar.selectbox("İlçe Seçin", ["Tümü"] + il_ilce_listesi[secili_il])

# KURUM_TUR_ADI seçimini sidebar'a ekle
kurum_turleri = okullar_gdf["KURUM_TUR_ADI"].unique()
secili_kurum_turu = st.sidebar.selectbox("Okul Türü Seçin", ["Tümü"] + list(kurum_turleri))

# Seçilen il ve ilçeye göre okulları filtrele
if secili_ilce == "Tümü":
    filtrelenmis_okullar = okullar_gdf[okullar_gdf["IL_ADI"] == secili_il]
else:
    filtrelenmis_okullar = okullar_gdf[(okullar_gdf["IL_ADI"] == secili_il) & 
                                       (okullar_gdf["ILCE_ADI"] == secili_ilce)]

# KURUM_TUR_ADI'na göre filtrele
if secili_kurum_turu != "Tümü":
    filtrelenmis_okullar = filtrelenmis_okullar[filtrelenmis_okullar["KURUM_TUR_ADI"] == secili_kurum_turu]

# Filtrelenmiş okulları göster
if not filtrelenmis_okullar.empty:
    st.write(f"Seçilen filtrelerle toplam {len(filtrelenmis_okullar)} okul bulunmaktadır.")
    # Okulları tablo olarak göster
    st.dataframe(filtrelenmis_okullar.drop(columns='geometry'))  # Geometri sütununu göstermemek için
else:
    st.write("Seçilen filtrelerle okul bulunamadı.")
