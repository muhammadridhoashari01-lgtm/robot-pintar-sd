import streamlit as st
import requests

# 1. Konfigurasi Tampilan Halaman Web
st.set_page_config(page_title="Robot Pintar SD", page_icon="🤖", layout="centered")

st.title("🤖 Robot Pintar")
st.caption("Media Pembelajaran Interaktif Seluruh Pelajaran SD (Kelas 1 - 6)")
st.write("Halo Teman Kecil! 👋 Aku Robot Pintar, guru sekaligus sahabat belajarmu! Kamu mau tanya materi apa hari ini? Matematika, IPA, Sejarah, atau Bahasa? Yuk, kita bahas bareng-bareng! 🚀🌈")

# 2. URL Cloudflare Worker Sukses Anda
WORKER_URL = "https://calm-fire-e809.muhammadridhoashari01.workers.dev/v1/chat/completions"

# 3. Inisialisasi Memori Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Tampilkan Riwayat Obrolan di Layar
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 5. Kotak Input Chat Pengguna
if user_input := st.chat_input("Tanya rumus, materi IPA, atau sejarah di sini..."):
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("*Robot sedang mencari materi di buku pintar... ⚡📚*")
        
        # --- MASTER SYSTEM PROMPT: PINTAR SEMUA MATERI SD ---
        system_instruction = (
            "Kamu adalah 'Robot Pintar', seorang guru virtual sekaligus sahabat belajar interaktif "
            "untuk siswa Sekolah Dasar (SD) dari kelas 1 sampai kelas 6 di Indonesia. "
            "Kamu menguasai SEMUA materi kurikulum SD (Merdeka/K-13), termasuk IPAS, IPA, IPS, Sejarah, Matematika, "
            "Bahasa Indonesia, Pendidikan Pancasila (PPKn), Seni Budaya (SBdP), dan Bahasa Inggris.\n\n"
            
            "IKUTI ATURAN KHUSUS INI DALAM MENJAWAB:\n"
            "1. GAYA BAHASA: Sangat ceria, ramah, penuh semangat, dan menggunakan kata-kata yang mudah dipahami anak SD. "
            "Gunakan sapaan hangat seperti 'Wah, pertanyaan bagus sekali!', 'Yuk, kita cari tahu!', 'Teman Pintar, tahu tidak?'.\n"
            "2. MATERI MATEMATIKA: Jika ditanya rumus atau hitungan, jangan langsung beri jawaban akhir. "
            "Jelaskan langkah-langkahnya pelan-pelan dengan analogi konkret (misal: menggunakan contoh buah, permen, atau kue).\n"
            "3. MATERI SEJARAH & IPS: Ceritakan tokoh-tokoh pahlawan atau kerajaan kuno seperti mendongengkan kisah seru "
            "agar anak-anak kagum dan tertanam karakter Cinta Tanah Air.\n"
            "4. MATERI IPA/IPAS: Berikan contoh nyata yang bisa mereka lihat di rumah atau di sekolah (misal: proses fotosintesis disamakan dengan memasak di dapur).\n"
            "5. VISUAL: Gunakan banyak emoji lucu di setiap paragraf (🚀, ✨, 🌈, 🧠, 🍎, 📐, 📜) dan gunakan format tulisan tebal (bold) pada kata kunci penting agar mudah dibaca.\n"
            "6. PENUTUP: Selalu akhiri jawaban dengan kalimat motivasi belajar yang seru!"
        )
        
        full_messages = [{"role": "system", "content": system_instruction}] + st.session_state.messages

        payload = {
            "model": "openai/gpt-oss-120b:free",
            "messages": full_messages,
            "temperature": 0.7,
            "max_tokens": 600  # Token sedikit dinaikkan agar penjelasan materi matematika/sejarah bisa tuntas dan jelas
        }
        
        headers = {
            "Content-Type": "application/json",
            "HTTP-Referer": "https://streamlit.io",
            "X-Title": "Robot Pintar SD"
        }

        try:
            response = requests.post(WORKER_URL, json=payload, headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                bot_reply = result["choices"][0]["message"]["content"]
                
                message_placeholder.markdown(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            else:
                message_placeholder.markdown(f"❌ Yah, robotnya agak lelah... (Error Status: {response.status_code})")
                
        except Exception as e:
            message_placeholder.markdown(f"❌ Gagal terhubung ke server. ({str(e)})")
