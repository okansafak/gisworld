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

    # KVKK Metni
    st.markdown("Kisisel Verilerin Korunması Kanunu (KVKK) kapsamında verilerinizin gizliliği önemlidir. "
                "Bu form aracılığıyla gönderilen bilgiler sadece başvurunuzu değerlendirmek amacıyla kullanılacaktır.")

    # Onay Kutusu
    kvkk_approval = st.checkbox("KVKK metnini okudum ve kabul ediyorum.")

    if kvkk_approval:
        # Kişisel Bilgiler
        st.header("Kişisel Bilgiler")
        full_name = st.text_input("Adınız Soyadınız")

        # E-posta
        email = st.text_input("E-posta Adresiniz")
        if email and not is_valid_email(email):
            st.warning("Lütfen geçerli bir e-posta adresi giriniz.")

        # Telefon Numarası
        phone = st.text_input("Telefon Numaranız")
        if phone and not is_valid_phone(phone):
            st.warning("Lütfen geçerli bir telefon numarası giriniz. Örnek: 0XXX XXX XX XX")

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
                                               ["Python", "R", "JavaScript", "C++", "Java", "Diğer"],
                                               default=["Python", "R"])

        # Kullandığı Programlar
        st.header("Kullandığınız Coğrafi Bilgi Sistemleri ve Veritabanları")
        gis_software = st.multiselect("Kullandığınız Coğrafi Bilgi Sistemleri ve Veritabanları", 
                                      ["QGIS", "ArcGIS", "PostgreSQL", "MapInfo", "Diğer"])

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

            # Veri çerçevesini Excel dosyasına yaz
            df.to_excel("basvurular.xlsx", index=False)

            st.success("Başvurunuz başarıyla gönderildi! Teşekkür ederiz.")
    else:
        st.warning("Başvurunuz için KVKK metnini kabul etmelisiniz.")

if __name__ == "__main__":
    main()
