import json
import streamlit as st
import geopandas as gpd

# Okullar GeoJSON dosyasını yükle
with open("okullar.geojson", encoding="utf-8") as f:
    okullar_geojson = json.load(f)

# İl ve ilçe listesi JSON dosyasını yükle
with open("il_ilce_listesi.json", encoding="utf-8") as f:
    il_ilce_listesi = json.load(f)

# Kontrol: İl/ilçe verileri boş mu?
if not il_ilce_listesi:
    st.error("İl ve ilçe verisi bulunamadı. Lütfen veri dosyalarını kontrol edin.")
    st.stop()

# Geopandas DataFrame'i oluştur
okullar_gdf = gpd.GeoDataFrame.from_features(okullar_geojson["features"])

# Streamlit uygulamasını oluştur
st.title("Okul Bilgi Uygulaması")

# Filtreler için sidebar oluştur
st.sidebar.title("Filtreler")

# İl seçimini sidebar'a ekle
secili_iller = st.sidebar.multiselect("İl Seçin", list(il_ilce_listesi.keys()), ["Tümü"])

# Seçilen illere göre ilçe listesini hazırla
secili_ilceler = []
for il in secili_iller:
    secili_ilceler.extend(il_ilce_listesi.get(il, []))

# İlçe seçimini sidebar'a ekle
secili_ilce = st.sidebar.selectbox("İlçe Seçin", ["Tümü"] + secili_ilceler)

# KURUM_TUR_ADI seçimini sidebar'a ekle
kurum_turleri = okullar_gdf["KURUM_TUR_ADI"].unique()
secili_kurum_turleri = st.sidebar.multiselect("Okul Türü Seçin", list(kurum_turleri), ["Tümü"])

# Seçilen il ve ilçelere göre okulları filtrele
filtrelenmis_okullar = okullar_gdf.copy()

if "Tümü" not in secili_iller:
    filtrelenmis_okullar = filtrelenmis_okullar[filtrelenmis_okullar["IL_ADI"].isin(secili_iller)]

if secili_ilce != "Tümü":
    filtrelenmis_okullar = filtrelenmis_okullar[filtrelenmis_okullar["ILCE_ADI"] == secili_ilce]

if "Tümü" not in secili_kurum_turleri:
    filtrelenmis_okullar = filtrelenmis_okullar[filtrelenmis_okullar["KURUM_TUR_ADI"].isin(secili_kurum_turleri)]

# Filtrelenmiş okulları göster
if not filtrelenmis_okullar.empty:
    st.write(f"Seçilen filtrelerle toplam {len(filtrelenmis_okullar)} okul bulunmaktadır.")
    # Okulları tablo olarak göster
    st.dataframe(filtrelenmis_okullar.drop(columns='geometry'))  # Geometri sütununu göstermemek için
else:
    st.write("Seçilen filtrelerle okul bulunamadı.")
