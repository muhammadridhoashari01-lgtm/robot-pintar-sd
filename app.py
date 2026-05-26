import streamlit as st
import requests

# 1. Konfigurasi Tampilan Halaman Web
st.set_page_config(page_title="Robot Pintar", page_icon="🤖", layout="centered")

st.title("🤖 Robot Pintar")
st.caption("Media Pembelajaran Interaktif - OpenRouter Gratis Selamanya")
st.write("Halo Teman Kecil! 👋 Aku Robot Pintar. Kamu mau tanya apa hari ini? Yuk, belajar bareng! 🚀🌈")

# =========================================================================
# 2. ALAMAT WORKER BARU ANDA
# Ganti URL di dalam tanda kutip di bawah ini dengan alamat URL Cloudflare Worker baru Anda
# =========================================================================
WORKER_URL = "ttps://calm-fire-e809.muhammadridhoashari01.workers.dev/v1/chat/completions."
# =========================================================================

# 3. Inisialisasi Memori Chat agar Riwayat Tidak Hilang
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Tampilkan Riwayat Obrolan di Layar
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Fitur Kotak Input Chat Pengguna
if user_input := st.chat_input("Tanya Robot di sini..."):
    
    # Tampilkan chat pengguna di layar
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Simpan ke dalam memori riwayat
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Tampilkan animasi loading saat robot merespon
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("*Robot sedang berpikir... ⚡*")
        
        # Susun payload JSON khusus untuk Model Gratis OpenRouter pilihan Anda
        payload = {
            "model": "nvidia/nemotron-3-super:free",
            "messages": st.session_state.messages,
            "temperature": 0.5,
            "max_tokens": 512
        }
        
        headers = {
            "Content-Type": "application/json",
            "HTTP-Referer": "https://streamlit.io",
            "X-Title": "Robot Pintar SD"
        }

        try:
            # Mengirim data langsung menggunakan variabel WORKER_URL yang sudah pasti didefinisikan
            response = requests.post(WORKER_URL, json=payload, headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                # Ambil teks jawaban hasil olahan AI
                bot_reply = result["choices"][0]["message"]["content"]
                
                # Munculkan jawaban robot di layar
                message_placeholder.markdown(bot_reply)
                
                # Simpan jawaban robot ke memori riwayat
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            else:
                message_placeholder.markdown(f"❌ Yah, robotnya agak lelah... (Error Status: {response.status_code})")
                st.caption("Tips: Pastikan Cloudflare Worker Anda sudah di-deploy dengan API Key OpenRouter yang benar.")
                
        except Exception as e:
            message_placeholder.markdown(f"❌ Gagal terhubung ke server. Pastikan internetmu aktif ya! ({str(e)})")
