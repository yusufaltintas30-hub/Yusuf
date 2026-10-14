import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(page_title="Ayşe Tekniği - SMC İşlem Asistanı", page_icon="📊", layout="centered")

st.title("📊 Ayşe Tekniği & SMC Asistanı")
st.write("Order Block (OB), FVG ve Likidite konseptleriyle harmanlanmış **%1.0 Kar Hedefli** Günlük İşlem Planı.")

st.markdown("---")

# Kullanıcı Girdi Alanları
hisse_adi = st.text_input("Hisse Kodu / Varlık", value="BIMAS").upper()
mevcut_fiyat = st.number_input("Anlık Fiyat (TL)", value=408.00, step=0.01)

strateji_tipi = st.selectbox(
    "Price Action / Kurumsal Bölge (SMC)",
    (
        "Order Block (OB) - Kurumsal Alım Bölgesi",
        "Fair Value Gap (FVG) - Dengesizlik Bölgesi",
        "Likidite Süpürmesi (Sweep) Sonrası",
        "Normal / Standart Kademe"
    )
)

# Hesaplama Butonu
if st.button("🚀 Profesyonel İşlem Planını Hesapla"):
    # SMC Kurallarına göre giriş noktası esnetme mantığı
    if "Order Block" in strateji_tipi:
        giris_fiyati = mevcut_fiyat * 0.996  # OB seviyesine geri çekilme payı
        not_aciklama = "Kurumsal emir bloğundan (OB) tepki alması bekleniyor. Güvenli kademeden giriş planlandı."
    elif "Fair Value Gap" in strateji_tipi:
        giris_fiyati = mevcut_fiyat * 0.997  # FVG dolgu seviyesi
        not_aciklama = "Fiyat dengesizliği (FVG) bölgesinden test edip yukarı yönelmesi öngörülüyor."
    elif "Likidite" in strateji_tipi:
        giris_fiyati = mevcut_fiyat          # Likidite süpürüldü, anlık devam
        not_aciklama = "Stoplar patlatıldı (Sweep), ana yön hareketine başlandı. Anlık giriş uygundur."
    else:
        giris_fiyati = mevcut_fiyat
        not_aciklama = "Standart piyasa koşulları ve kademe analizi baz alındı."

    # Kesin %1.0 Kar Hedefi (Take Profit)
    kar_hedefi = giris_fiyati * 1.01
    
    # Risk Yönetimi / Stop Seviyesi
    stop_seviyesi = giris_fiyati * 0.985

    # Sonuçların Ekran Yansıtılması
    st.success(f"### 🎯 {hisse_adi} İçin Günlük İşlem Raporu")
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric(label="Önerilen Giriş Fiyatı", value=f"{giris_fiyati:.2f} TL")
    with c2:
        st.metric(label="Hedef (%1.0 Kar Al)", value=f"{kar_hedefi:.2f} TL", delta="%1.0")

    st.warning(f"🛑 **Stop-Loss (Destek Altı):** {stop_seviyesi:.2f} TL")
    st.info(f"💡 **SMC & Price Action Notu:** {not_aciklama}")

st.markdown("---")
st.caption("Ayşe Tekniği v2.0 - Smart Money Concepts Entegrasyonu © 2026")
