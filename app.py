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
    
    # İl/ilçe ve okul türü istatistikleri
    st.sidebar.subheader("Genel İstatistikler")

    # En az okul sayısı olan il/ilçe
    en_az_okul_il_ilce = filtrelenmis_okullar["IL_ADI"].value_counts().idxmin()
    en_az_okul_sayısı_il_ilce = filtrelenmis_okullar["IL_ADI"].value_counts().min()
    st.sidebar.write(f"En az okul sayısı olan il/ilçe: **{en_az_okul_il_ilce}** ({en_az_okul_sayısı_il_ilce} okul)")

    # En fazla okul sayısı olan il/ilçe
    en_fazla_okul_il_ilce = filtrelenmis_okullar["IL_ADI"].value_counts().idxmax()
    en_fazla_okul_sayısı_il_ilce = filtrelenmis_okullar["IL_ADI"].value_counts().max()
    st.sidebar.write(f"En fazla okul sayısı olan il/ilçe: **{en_fazla_okul_il_ilce}** ({en_fazla_okul_sayısı_il_ilce} okul)")

    # En fazla okul türü
    en_fazla_okul_türü = filtrelenmis_okullar["KURUM_TUR_ADI"].value_counts().idxmax()
    en_fazla_okul_türü_sayısı = filtrelenmis_okullar["KURUM_TUR_ADI"].value_counts().max()
    st.sidebar.write(f"En fazla okul türü: **{en_fazla_okul_türü}** ({en_fazla_okul_türü_sayısı} okul)")

    # En az okul türü
    en_az_okul_türü = filtrelenmis_okullar["KURUM_TUR_ADI"].value_counts().idxmin()
    en_az_okul_türü_sayısı = filtrelenmis_okullar["KURUM_TUR_ADI"].value_counts().min()
    st.sidebar.write(f"En az okul türü: **{en_az_okul_türü}** ({en_az_okul_türü_sayısı} okul)")
    
    # Grafik: Okul türlerine göre dağılım
    st.subheader("Okul Türü Dağılımı")
    okul_turu_dağılımı = filtrelenmis_okullar["KURUM_TUR_ADI"].value_counts()
    st.bar_chart(okul_turu_dağılımı)

    # Grafik: İlçelerdeki okul sayıları
    st.subheader("İlçelerdeki Okul Sayıları")
    ilce_okul_sayıları = filtrelenmis_okullar["ILCE_ADI"].value_counts()
    st.bar_chart(ilce_okul_sayıları)

    # Okulları tablo olarak göster
    st.dataframe(filtrelenmis_okullar.drop(columns='geometry'))  # Geometri sütununu göstermemek için
else:
    st.write("Seçilen filtrelerle okul bulunamadı.")
