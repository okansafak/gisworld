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
            # Başvuru bilgilerini bir veri çerçevesine aktar
            data = {'Ad Soyad': [full_name], 'E-posta': [email], 'Telefon': [phone], 'Mesaj': [message]}
            df = pd.DataFrame(data)

            # Veri çerçevesini Excel dosyasına yaz
            df.to_excel("basvurular.xlsx", index=False)
            
            st.success("Başvurunuz başarıyla gönderildi! Teşekkür ederiz.")
    else:
        st.warning("Başvurunuz için KVKK metnini kabul etmelisiniz.")

if __name__ == "__main__":
    main()
