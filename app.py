import json
import streamlit as st
import geopandas as gpd
import pandas as pd
import plotly.express as px




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
    st.sidebar.subheader("İstatistikler")
    
    if secili_ilce != "Tümü":
        ilce_okul_sayisi = len(okullar_gdf[okullar_gdf["ILCE_ADI"] == secili_ilce])
        st.sidebar.write(f"Seçilen İlçedeki Toplam Okul Sayısı: **{ilce_okul_sayisi}**")
    
    if secili_il != "Tümü":
        il_okul_sayisi = len(okullar_gdf[okullar_gdf["IL_ADI"] == secili_il])
        st.sidebar.write(f"Seçilen İldeki Toplam Okul Sayısı: **{il_okul_sayisi}**")
    
    if secili_il != "Tümü":
        en_fazla_okul_turu = filtrelenmis_okullar["KURUM_TUR_ADI"].value_counts().idxmax()
        en_fazla_okul_sayisi = filtrelenmis_okullar["KURUM_TUR_ADI"].value_counts().max()
        st.sidebar.write(f"En Fazla Okul Türü: **{en_fazla_okul_turu}** ({en_fazla_okul_sayisi} okul)")
        
        en_az_okul_turu = filtrelenmis_okullar["KURUM_TUR_ADI"].value_counts().idxmin()
        en_az_okul_sayisi = filtrelenmis_okullar["KURUM_TUR_ADI"].value_counts().min()
        st.sidebar.write(f"En Az Okul Türü: **{en_az_okul_turu}** ({en_az_okul_sayisi} okul)")
    
    # Grafik: Okul türlerine göre dağılım
    st.subheader("Okul Türü Dağılımı")
    okul_turu_dağılımı = filtrelenmis_okullar["KURUM_TUR_ADI"].value_counts()
    fig1 = px.bar(okul_turu_dağılımı, x=okul_turu_dağılımı.index, y=okul_turu_dağılımı.values)
    fig1.update_layout(xaxis_title="Okul Türü", yaxis_title="Okul Sayısı", title="Okul Türü Dağılımı")
    st.plotly_chart(fig1, use_container_width=True)

    # Grafik: İlçelerdeki okul sayıları
    st.subheader("İlçelerdeki Okul Sayıları")
    ilce_okul_sayıları = filtrelenmis_okullar["ILCE_ADI"].value_counts()
    fig2 = px.bar(ilce_okul_sayıları, x=ilce_okul_sayıları.index, y=ilce_okul_sayıları.values)
    fig2.update_layout(xaxis_title="İlçe", yaxis_title="Okul Sayısı", title="İlçelerdeki Okul Sayıları")
    st.plotly_chart(fig2, use_container_width=True)

    # Okulları tablo olarak göster
    st.dataframe(filtrelenmis_okullar.drop(columns='geometry'))  # Geometri sütununu göstermemek için
else:
    st.write("Seçilen filtrelerle okul bulunamadı.")