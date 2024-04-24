import streamlit as st
import pydeck as pdk

# GeoJSON data
geojson_data = {
    "type": "FeatureCollection",
    "name": "istanbul",
    "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
    "features": [
        { "type": "Feature", "properties": { "Kurum_Arama": None, "Table": None, "IL_ADI": "İSTANBUL", "ILCE_ADI": "ADALAR", "KURUM_ADI": "ADALAR ANADOLU İMAM HATİP LİSESİ", "ADRES": "MADEN MAH. CEMAL YENER TOSYALI SK.  NO: 2  İÇ KAPI NO: 1 ADALAR / İSTANBUL", "TEL": "(216) 382 55 76", "FAX": "(216) 382 55 76", "MERNIS_ADRES_KODU": 2338909985, "WEB_ADRES": "adalarimamhatiplisesi.meb.k12.tr", "KURUM_TUR_ADI": "İmam Hatip Lisesi", "KURUM_TUR_KODU": 66, "X": 40.86777563, "Y": 29.132224841, "ZOOM": 20 }, "geometry": { "type": "Point", "coordinates": [ 29.132224841, 40.86777563 ] } },
        { "type": "Feature", "properties": { "Kurum_Arama": None, "Table": None, "IL_ADI": "İSTANBUL", "ILCE_ADI": "ADALAR", "KURUM_ADI": "ADALAR BİLİM VE SANAT MERKEZİ", "ADRES": "HEYBELİADA MAH. TURGUT REİS SK.  NO: 23  İÇ KAPI NO: 1 ADALAR / İSTANBUL", "TEL": None, "FAX": None, "MERNIS_ADRES_KODU": 2434306813, "WEB_ADRES": "769309.meb.k12.tr", "KURUM_TUR_ADI": "BİLSEM (Üstün veya Özel Yetenekliler)", "KURUM_TUR_KODU": 136, "X": 40.875043395, "Y": 29.098123066, "ZOOM": 20 }, "geometry": { "type": "Point", "coordinates": [ 29.098123066, 40.875043395 ] } },
        { "type": "Feature", "properties": { "Kurum_Arama": None, "Table": None, "IL_ADI": "İSTANBUL", "ILCE_ADI": "ADALAR", "KURUM_ADI": "ADALAR HALK EĞİTİMİ MERKEZİ", "ADRES": "MADEN MAH. BAŞLALA SK. NO: 19 ADALAR / İSTANBUL", "TEL": "(216) 382 56 66", "FAX": "(216) 382 86 71", "MERNIS_ADRES_KODU": 4076214776, "WEB_ADRES": "adalarhem.meb.k12.tr", "KURUM_TUR_ADI": "Halk Eğitimi Merkezi", "KURUM_TUR_KODU": 69, "X": 40.877794317000003, "Y": 29.095291423, "ZOOM": 20 }, "geometry": { "type": "Point", "coordinates": [ 29.095291423, 40.877794317 ] } },
        { "type": "Feature", "properties": { "Kurum_Arama": None, "Table": None, "IL_ADI": "İSTANBUL", "ILCE_ADI": "ADALAR", "KURUM_ADI": "BURGAZADA ÖĞRETMENEVİ VE AKŞAM SANAT OKULU", "ADRES": "BURGAZADASI MAH. GÖNÜLLÜ CAD.  NO: 61  İÇ KAPI NO: 1 ADALAR / İSTANBUL", "TEL": "(216) 381 27 21", "FAX": "(216) 381 29 66", "MERNIS_ADRES_KODU": 2602001204, "WEB_ADRES": "burgazadaogretmenevi.meb.k12.tr", "KURUM_TUR_ADI": "Akşam Sanat Okulu (DHGM)", "KURUM_TUR_KODU": 185, "X": 40.884575623000003, "Y": 29.065038301000001, "ZOOM": 20 }, "geometry": { "type": "Point", "coordinates": [ 29.065038301, 40.884575623 ] } }
    ]
}

# Create the GeoJsonLayer
geojson_layer = pdk.Layer(
    'GeoJsonLayer',
    data=geojson_data,
    get_fill_color=[200, 30, 0, 160],
    get_line_color=[255, 255, 255],
    lineWidthMinPixels=1,
    pickable=True
)

# Popup verileri için ColumnLayer oluştur
popup_layer = pdk.Layer(
    "ColumnLayer",
    data=geojson_data['features'],
    get_position=["geometry.coordinates[0]", "geometry.coordinates[1]"],
    get_elevation=1000,
    get_fill_color=[255, 0, 0],
    auto_highlight=True,
    pickable=True,
    extruded=True,
    radius=100,
)

# Harita yapısı oluştur
view_state = pdk.ViewState(
    latitude=40.86777563,
    longitude=29.132224841,
    zoom=10,
    pitch=40.5,
)

# Pydeck Haritasını oluştur
r = pdk.Deck(layers=[geojson_layer, popup_layer], initial_view_state=view_state, tooltip={"text": "{ILCE_ADI}\n{KURUM_ADI}\n{ADRES}\n{TEL}\n{WEB_ADRES}\n{KURUM_TUR_ADI}"})

# Streamlit ile göster
st.pydeck_chart(r)
