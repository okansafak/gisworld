import streamlit as st
import pandas as pd
import re

def is_valid_email(email):
    # E-posta adresinin geçerli olup olmadığını kontrol et
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

def is_valid_phone(phone):
    # Telefon numarasının geçerli olup olmadığını kontrol et
    phone_regex = r'^0[1-9][0-9]{2}[ ]?[0-9]{3}[ ]?[0-9]{2}[ ]?[0-9]{2}$'
    return re.match(phone_regex, phone)

def main():
    st.title("Geospatial Data Sciences Bootcamp Başvuru Formu")
    st.write("Lütfen aşağıdaki formu doldurarak başvurunuzu tamamlayın.")

    # KVKK Metni ve Onay Kutusu
    kvkk_approval = st.checkbox("Kisisel Verilerin Korunması Kanunu (KVKK) kapsamında verilerinizin gizliliği önemlidir. "
                                "Bu form aracılığıyla gönderilen bilgiler sadece başvurunuzu değerlendirmek amacıyla kullanılacaktır. "
                                "KVKK metnini okudum ve kabul ediyorum.")

    if kvkk_approval:
        # Kişisel Bilgiler
        st.header("Kişisel Bilgiler")
        full_name = st.text_input("Adınız Soyadınız", required=True)

        # E-posta
        email = st.text_input("E-posta Adresiniz", required=True)
        if email and not is_valid_email(email):
            st.warning("Lütfen geçerli bir e-posta adresi giriniz.")

        # Telefon Numarası
        phone = st.text_input("Telefon Numaranız", required=True)
        if phone and not is_valid_phone(phone):
            st.warning("Lütfen geçerli bir telefon numarası giriniz. Örnek: 0XXX XXX XX XX")

        # Eğitim Durumu
        st.header("Eğitim Durumu")
        graduate_status = st.radio("Mezun Durumu", ("Mezun", "Mezun Değil"), index=1)

        if graduate_status == "Mezun":
            university = st.text_input("Mezun Olduğunuz Üniversite", required=True)
            department = st.text_input("Mezun Olduğunuz Bölüm", required=True)
            grade = st.text_input("Mezuniyet Dereceniz", required=True)
            employment_status = st.radio("Çalışma Durumu", ("Çalışıyor", "Çalışmıyor"))

            if employment_status == "Çalışıyor":
                company = st.text_input("Çalıştığınız Kurum")
            else:
                company = None
        else:
            university = st.text_input("Üniversite", required=True)
            department = st.text_input("Bölüm", required=True)
            grade = st.text_input("Sınıf", required=True)
            company = None

        # Programlama Bilgileri
        st.header("Programlama Bilgileri")
        programming_languages = st.multiselect("Kullandığınız Programlama Dilleri", 
                                               ["Python", "R", "SQL", "JavaScript", "C++", "Java", "Diğer"],
                                               default=["Python", "R"])

        # Kullandığı Programlar
        st.header("Kullandığınız Coğrafi Bilgi Sistemleri ve Veritabanları")
        gis_software = st.multiselect("Kullandığınız Coğrafi Bilgi Sistemleri ve Veritabanları", 
                                      ["QGIS", "ArcGIS", "NetCAD", "Autocad", "PostgreSQL", "MapInfo", "Diğer"])

        # Mesaj
        st.header("Eklemek İstediğiniz Mesaj")
        message = st.text_area("Mesajınızı buraya yazabilirsiniz", height=150)

        # Başvuru Gönderme Butonu
        if st.button("Başvuru Gönder"):
            # Başvuru bilgilerini bir veri çerçevesine aktar
            data = {'Ad Soyad': [full_name], 'E-posta': [email], 'Telefon': [phone],
                    'Üniversite': [university], 'Bölüm': [department], 'Sınıf': [grade],
                    'Çalıştığı Kurum': [company], 'Programlama Dilleri': [", ".join(programming_languages)],
                    'Kullandığı Programlar': [", ".join(gis_software)],
                    'Mesaj': [message]}
            df = pd.DataFrame(data)

            # Varolan verileri oku veya yeni bir dosya oluştur
            try:
                existing_data = pd.read_excel("basvurular.xlsx")
                df = pd.concat([existing_data, df], ignore_index=True)
            except FileNotFoundError:
                pass

            # Veri çerçevesini Excel dosyasına yaz
            df.to_excel("basvurular.xlsx", index=False)

            st.success("Başvurunuz başarıyla gönderildi! Teşekkür ederiz.")
    else:
        st.warning("Başvurunuz için KVKK metnini kabul etmelisiniz.")

    # Eğitim İçeriği
    st.sidebar.header("Eğitim İçeriği")
    st.sidebar.subheader("Hafta 1: Coğrafi Bilgi Sistemleri (GIS) Temelleri")
    st.sidebar.write("""
    - Gün 1: Giriş ve Temel Kavramlar
        - Coğrafi Bilgi Sistemleri (GIS) Nedir?
        - Coğrafi Verilerin Temel Kavramları: Nokta, Çizgi, Alan
        - Koordinat Sistemleri ve Coğrafi Referans Sistemleri (CRS)
    - Gün 2: Temel GIS Yazılımları
        - QGIS ve Temel Fonksiyonlar
        - Diğer GIS Yazılımları ve Uygulamaları
    - Gün 3: Coğrafi Veri Toplama ve Dönüşüm
        - Coğrafi Veri Toplama Yöntemleri: Sahada Veri Toplama, Veri Kaynakları
        - Veri Formatları: Shapefile, GeoJSON, KML
        - Coğrafi Veri Dönüşümleri ve Projeksiyonlar
    """)
    st.sidebar.subheader("Hafta 2: Coğrafi Veri Analizi ve Modelleme")
    st.sidebar.write("""
    - Gün 4: Raster Analizler
        - Raster Veri Yapısı ve Temel İşlemler
        - Raster Referanslama
        - Raster Veri Analizi: Bakı , Eğim..
    - Gün 5: Vector Analizler
        - Vector Veri Yapısı ve Temel İşlemler
        - Vector Veri Analizi: Mekansal İlişkiler, Tampon, Kesişim ..
    """)
    st.sidebar.subheader("Hafta 3: Mekansal Veri İşleme ve Uygulamaları")
    st.sidebar.write("""
    - Gün 7: Geoserver ve Web Harita Uygulamaları
        - Geoserver Nedir ve Nasıl Kurulur?
        - Veri Yayınlama ve Servis Oluşturma
        - Temel Harita Uygulamaları Geliştirme Leaflet ve OpenLayers ile 
    """)
    st.sidebar.subheader("Hafta 4: Uygulamalar ve Projeler")
    st.sidebar.write("""
    - Gün 8: Coğrafi Veri Görselleştirme ve Proje Sunumları
        - Harita Tasarımı İlkeleri
        - Grafikler ve Grafiksel Gösterimler
        - Katılımcıların Temel Seviye Proje Sunumları ve Değerlendirmeleri
    """)

if __name__ == "__main__":
    main()
