import streamlit as st
from textblob import TextBlob
import pandas as pd
import altair as alt

# Sayfa Ayarları
st.set_page_config(page_title="Vibe Check - Duygu Analizi", page_icon="🎭")

# Başlık ve Açıklama
st.title("🎭 Vibe Check: Metin Duygu Analizi")
st.write("Yazdığınız İngilizce metnin duygusal tonunu (Pozitif, Negatif, Nötr) anında analiz edin.")

# Sol Menü
with st.sidebar:
    st.header("Hakkında")
    st.info("Bu uygulama TextBlob kütüphanesi kullanılarak NLP (Doğal Dil İşleme) teknikleriyle hazırlanmıştır.")
    st.write("---")
    st.write("Developed by Sen 🚀")

# Ana Alan - Metin Girişi
text_input = st.text_area("Analiz edilecek metni buraya girin (İngilizce):", height=150, placeholder="I love coding so much! It makes me happy.")

if st.button("Analiz Et 🔍"):
    if text_input:
        blob = TextBlob(text_input)
        polarity = blob.sentiment.polarity  # -1 (Negatif) ile +1 (Pozitif) arası
        subjectivity = blob.sentiment.subjectivity # 0 (Nesnel) ile 1 (Öznel) arası
        
        # Sonuçları Göster
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Duygu Skoru")
            if polarity > 0:
                st.success(f"Pozitif 😊 ({polarity:.2f})")
            elif polarity < 0:
                st.error(f"Negatif 😠 ({polarity:.2f})")
            else:
                st.warning(f"Nötr 😐 ({polarity:.2f})")
                
        with col2:
            st.markdown("### Öznellik")
            st.info(f"{subjectivity:.2f} (0: Nesnel, 1: Öznel)")

        st.write("---")
        
        # Görselleştirme
        st.subheader("📊 Görsel Analiz")
        
        # Veri Hazırlama
        data = pd.DataFrame({
            'Metrik': ['Mutluluk/Pozitiflik', 'Öznellik/Kişisellik'],
            'Skor': [polarity, subjectivity]
        })
        
        # Bar Grafiği
        chart = alt.Chart(data).mark_bar().encode(
            x=alt.X('Metrik', axis=None),
            y=alt.Y('Skor', scale=alt.Scale(domain=[-1, 1])),
            color='Metrik',
            tooltip=['Metrik', 'Skor']
        ).properties(height=300)
        
        st.altair_chart(chart, use_container_width=True)
        
    else:
        st.warning("Lütfen analiz için bir metin girin.")