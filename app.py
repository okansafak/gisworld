import streamlit as st
import pandas as pd
import re

def is_valid_email(email):
    # E-posta adresinin geçerli olup olmadığını kontrol et
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

def is_valid_phone(phone):
    # Telefon numarasının geçerli olup olmadığını kontrol et
    phone_regex = r'^0\d{10}$'
    return re.match(phone_regex, phone)

def main():
    st.title("Geospatial Data Sciences Bootcamp Başvuru Formu")
    st.sidebar.title("Eğitim İçeriği")
    # Eğitim içeriği buraya eklenecek...

    st.write("Lütfen aşağıdaki formu doldurarak başvurunuzu tamamlayın.")

    # KVKK Metni ve Onay Kutusu
    kvkk_approval = st.checkbox("Kisisel Verilerin Korunması Kanunu (KVKK) kapsamında verilerinizin gizliliği önemlidir. "
                                "Bu form aracılığıyla gönderilen bilgiler sadece başvurunuzu değerlendirmek amacıyla kullanılacaktır. "
                                "KVKK metnini okudum ve kabul ediyorum.")

    if kvkk_approval:
        # Kişisel Bilgiler
        st.header("Kişisel Bilgiler")
        full_name = st.text_input("Adınız Soyadınız")
        if not full_name:
            st.warning("Adınız soyadınızı giriniz.")

        # E-posta
        email = st.text_input("E-posta Adresiniz")
        if email and not is_valid_email(email):
            st.warning("Lütfen geçerli bir e-posta adresi giriniz.")

        # Telefon Numarası
        phone = st.text_input("Telefon Numaranız", max_chars=11)
        if phone and not is_valid_phone(phone):
            st.warning("Lütfen geçerli bir telefon numarası giriniz. Örnek: 05XXXXXXXXX")

        # Eğitim Durumu
        st.header("Eğitim Durumu")
        graduate_status = st.radio("Mezun Durumu", ("Mezun", "Mezun Değil"))

        if graduate_status == "Mezun":
            university = st.text_input("Mezun Olduğunuz Üniversite")
            department = st.text_input("Mezun Olduğunuz Bölüm")
            grade = st.text_input("Mezuniyet Dereceniz")
            employment_status = st.radio("Çalışma Durumu", ("Çalışıyor", "Çalışmıyor"))

            if employment_status == "Çalışıyor":
                company = st.text_input("Çalıştığınız Kurum")
            else:
                company = None
        else:
            university = st.text_input("Üniversite")
            department = st.text_input("Bölüm")
            grade = st.text_input("Sınıf")
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

            st.success("Başvurunuz başarıyla gönderildi! Teşekkür ederiz. Başvurunuz alınmıştır. Eğitimde görüşmek üzere.")
    else:
        st.warning("Başvurunuz için KVKK metnini kabul etmelisiniz.")

if __name__ == "__main__":
    main()
