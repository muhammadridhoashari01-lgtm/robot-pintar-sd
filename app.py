import streamlit as st
import requests

# 1. Atur Judul dan Konfigurasi Halaman Web
st.set_page_config(page_title="Robot Pintar", page_icon="🤖", layout="centered")

st.title("🤖 Robot Pintar")
st.caption("Powered by NVIDIA AI & Cloudflare Workers")
st.write("Halo Teman Kecil! 👋 Aku Robot Pintar. Kamu mau tanya apa hari ini? 🚀🌈")

# 2. Masukkan URL Cloudflare Worker Anda yang sudah sukses CORS & API Key kemarin
WORKER_URL = "https://calm-fire-e809.muhammadridhoashari01.workers.dev"

# 3. Inisialisasi Memori Chat (Agar riwayat obrolan tidak hilang saat halaman di-refresh)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Tampilkan Riwayat Obrolan di Layar
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Fitur Kotak Input Chat (Tempat User Mengetik)
if user_input := st.chat_input("Tanya Robot di sini..."):
    
    # Tampilkan chat yang diketik user di layar
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Simpan ke memori riwayat
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Tampilkan animasi loading saat robot berpikir
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("*Robot sedang berpikir... ⚡*")
        
        # Susun data JSON yang akan dikirim ke Cloudflare Worker
        payload = {
            "model": "meta/llama-3.1-405b-instruct", # Sesuaikan dengan model Nvidia pilihan Anda
            "messages": st.session_state.messages,
            "temperature": 0.5,
            "max_tokens": 1024,
            "stream": False
        }
        
        headers = {
            "Content-Type": "application/json"
        }

        try:
            # Tembak data ke Cloudflare Worker
            response = requests.post(WORKER_URL, json=payload, headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                # Ambil teks balasan dari struktur data Nvidia
                bot_reply = result["choices"][0]["message"]["content"]
                
                # Tampilkan balasan asli robot di layar
                message_placeholder.markdown(bot_reply)
                
                # Simpan balasan robot ke memori riwayat
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            else:
                message_placeholder.markdown(f"❌ Yah, koneksi terputus... (Error: {response.status_code})")
                
        except Exception as e:
            message_placeholder.markdown(f"❌ Gagal terhubung ke server. Pastikan internetmu aktif ya! ({str(e)})")
