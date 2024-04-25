import streamlit as st
import pandas as pd

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
        email = st.text_input("E-posta Adresiniz")
        phone = st.text_input("Telefon Numaranız")

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
        programming_languages = st.multiselect("Kullandığınız Programlama Dilleri", ["Python", "R", "JavaScript", "C++", "Java", "Diğer"])

        # Mesaj
        st.header("Eklemek İstediğiniz Mesaj")
        message = st.text_area("Mesajınızı buraya yazabilirsiniz", height=150)

        # Başvuru Gönderme Butonu
        if st.button("Başvuru Gönder"):
            # Başvuru bilgilerini bir veri çerçevesine aktar
            data = {'Ad Soyad': [full_name], 'E-posta': [email], 'Telefon': [phone],
                    'Üniversite': [university], 'Bölüm': [department], 'Sınıf': [grade],
                    'Çalıştığı Kurum': [company], 'Programlama Dilleri': [", ".join(programming_languages)],
                    'Mesaj': [message]}
            df = pd.DataFrame(data)

            # Veri çerçevesini Excel dosyasına yaz
            df.to_excel("basvurular.xlsx", index=False)

            st.success("Başvurunuz başarıyla gönderildi! Teşekkür ederiz.")
    else:
        st.warning("Başvurunuz için KVKK metnini kabul etmelisiniz.")

if __name__ == "__main__":
    main()
