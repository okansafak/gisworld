import streamlit as st

def main():
    st.title("Geospatial Data Sciences Bootcamp Başvuru Formu")
    st.write("Lütfen aşağıdaki formu doldurarak başvurunuzu tamamlayın.")

    # Ad Soyad
    full_name = st.text_input("Adınız Soyadınız")

    # E-posta
    email = st.text_input("E-posta Adresiniz")

    # Telefon Numarası
    phone = st.text_input("Telefon Numaranız")

    # Mesaj
    message = st.text_area("Mesajınız", height=150)

    # Başvuru Gönderme Butonu
    if st.button("Başvuru Gönder"):
        # Burada başvuru işlemleri yapılabilir, örneğin veritabanına kaydedilebilir.
        st.success("Başvurunuz başarıyla gönderildi! Teşekkür ederiz.")

if __name__ == "__main__":
    main()
