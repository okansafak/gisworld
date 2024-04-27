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

# İl seçimini yap
secili_il = st.selectbox("Lütfen bir il seçin:", list(il_ilce_listesi.keys()))

# "Tümü" seçeneği ekleyerek ilçe seçimini yap
secili_ilce = st.selectbox("Lütfen bir ilçe seçin:", ["Tümü"] + il_ilce_listesi[secili_il])

# Seçilen il ve ilçeye göre okulları filtrele
if secili_ilce == "Tümü":
    filtrelenmis_okullar = okullar_gdf[okullar_gdf["IL_ADI"] == secili_il]
else:
    filtrelenmis_okullar = okullar_gdf[(okullar_gdf["IL_ADI"] == secili_il) & 
                                       (okullar_gdf["ILCE_ADI"] == secili_ilce)]

# Filtrelenmiş okulları göster
if not filtrelenmis_okullar.empty:
    st.write(f"Seçilen il ve ilçede toplam {len(filtrelenmis_okullar)} okul bulunmaktadır.")
    # Okulları tablo olarak göster
    st.dataframe(filtrelenmis_okullar.drop(columns='geometry'))  # Geometri sütununu göstermemek için
else:
    st.write("Seçilen il ve ilçeye ait okul bulunamadı.")
