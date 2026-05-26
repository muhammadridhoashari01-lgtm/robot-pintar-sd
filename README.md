# robot-pintar-sd
# 🤖 Robot Pintar - Media Pembelajaran Interaktif Seluruh Pelajaran SD (Kelas 1 - 6)

Aplikasi Web Chatbot berbasis Artificial Intelligence (AI) yang dirancang khusus sebagai media pembelajaran interaktif untuk siswa Sekolah Dasar (SD) dari kelas 1 hingga kelas 6 di Indonesia. Aplikasi ini mampu menjawab berbagai pertanyaan materi kurikulum SD dengan gaya bahasa yang ceria, ramah anak, dan mudah dipahami.

## 🚀 Link Aplikasi
Anda dapat mengakses aplikasi ini secara langsung melalui tautan berikut:
🔗 **[ujicobaaisd.streamlit.app](https://ujicobaaisd.streamlit.app/)**

---

## ✨ Fitur Utama
- **Multimateri SD:** Menguasai seluruh materi sekolah seperti IPAS (IPA/IPS), Matematika, Sejarah Indonesia, Pendidikan Pancasila, Bahasa Indonesia, hingga Seni Budaya.
- **Ramah Anak (Kid-Friendly UI/UX):** Menggunakan *System Prompt* khusus yang memaksa AI menjawab dengan gaya bahasa guru SD yang ceria, penuh semangat, dan dilengkapi banyak emoji lucu.
- **Penjelasan Konkret:** Materi Matematika dijelaskan langkah demi langkah menggunakan analogi benda nyata (buah, kue, permen), sedangkan materi Sejarah disampaikan lewat metode mendongeng yang seru.
- **Responsif Seluler:** Tampilan web otomatis menyesuaikan layar HP sehingga sangat nyaman digunakan oleh siswa melalui ponsel orang tua masing-masing.

---

## 🛠️ Arsitektur Sistem & Teknologi

Proyek ini dibangun menggunakan infrastruktur modern yang 100% gratis namun memiliki performa skala profesional:

1. **Frontend:** [Streamlit Cloud](https://streamlit.io/) & Python — Menyediakan antarmuka (UI) chat yang bersih, modern, dan responsif ala ChatGPT.
2. **Reverse Proxy / Jembatan Keamanan:** [Cloudflare Workers](https://workers.cloudflare.com/) — Berfungsi sebagai jembatan untuk menyembunyikan API Key dari publik dan menangani masalah keamanan CORS browser.
3. **Brain AI (LLM Provider):** [OpenRouter.ai](https://openrouter.ai/) — Menyediakan akses ke model kecerdasan buatan gratis selamanya (`openai/gpt-oss-120b:free`) yang dioptimalkan untuk kebutuhan edukasi.

---

## 📦 Cara Menjalankan Secara Lokal (Local Deployment)

Jika Anda ingin mencoba menjalankan aplikasi ini di komputer/laptop sendiri, ikuti langkah berikut:

1. **Clone Repositori Ini:**
   ```bash
   git clone [https://github.com/USERNAME-ANDA/robot-pintar-sd.git](https://github.com/USERNAME-ANDA/robot-pintar-sd.git)
   cd robot-pintar-sd
Install Library yang Dibutuhkan:
Pastikan Anda sudah menginstal Python, lalu jalankan perintah:

Bash
pip install -r requirements.txt

Jalankan Aplikasi:

Bash
streamlit run app.py

📂 Struktur File
app.py : Kode utama aplikasi Streamlit (Frontend & Logika Chat).

requirements.txt : Daftar library Python pendukung yang wajib diinstal oleh server (streamlit & requests).

README.md : Dokumentasi lengkap mengenai proyek aplikasi.

📋 Proyek ini dikembangkan sebagai inovasi media pembelajaran digital guna meningkatkan motivasi belajar dan menanamkan karakter positif pada siswa Sekolah Dasar.
