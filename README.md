# Atlas Sejarah Kerajaan Islam Nusantara
### *Sistem Informasi Geografis (WebGIS) Interaktif & Kronologi Kesultanan Nusantara*

Sebuah aplikasi **WebGIS Sejarah Murni Sisi Klien (Client-Side Historical WebGIS)** yang memetakan persebaran pusat pemerintahan kerajaan dan kesultanan Islam di seluruh kepulauan Nusantara (Indonesia), mulai dari fase awal islamisasi maritim (abad ke-13 M) hingga integrasi ke dalam Negara Kesatuan Republik Indonesia (1945 M).

Website dirancang dengan estetika **Historical Digital Atlas** (perpaduan nuansa kartografi kuno, tipografi klasik *Cinzel* & modern *Plus Jakarta Sans*, aksen emas bakar dan zamrud Islam), sepenuhnya responsif untuk perangkat desktop maupun ponsel, serta tanpa ketergantungan API berbayar sehingga dapat langsung dipublikasikan melalui **GitHub Pages**.

---

## 🌟 Fitur Utama Sistem

1. **Peta Interaktif 2D Berbasis Leaflet.js**:
   - Memetakan 36 kerajaan dan kesultanan Islam di 6 zona geografis kepulauan: **Sumatera, Jawa, Kalimantan, Sulawesi, Maluku & Papua, dan Nusa Tenggara**.
   - Penanda (*marker*) kustom dengan simbol ornamen islami, mahkota keemasan, dan lencana peninggalan budaya.
   - Pilihan multi-basemap: **CartoDB Positron** (peta kartografis terang beresolusi tinggi), **CartoDB Dark Matter** (mode malam atlas digital), **OpenStreetMap Standard**, dan **Citra Satelit Esri World Imagery**.

2. **Linimasa Kronologis Dinamis (Interactive Timeline 1200–1950 M)**:
   - Slider rentang tahun dari tahun 1200 M hingga 1950 M.
   - Tombol **Play / Pause** otomatis untuk animasi pergerakan sejarah per tahun.
   - Pilihan lompatan abad cepat (*Century Quick Jump*): 1267 (Pasai), 1400, 1475 (Demak), 1526 (Banten/Banjar), 1575 (Ternate), 1625 (Puncak Keemasan), 1670 (Makassar), 1755 (Giyanti), 1825 (Perang Diponegoro), 1900, dan 1945 (Kemerdekaan RI).
   - Status marker berubah otomatis mengikuti tahun yang dipilih:
     - **Sedang Dalam Era Keemasan (Golden Age)**: Marker emas berpendar dengan animasi denyut (*pulsing halo*).
     - **Aktif & Berdaulat**: Marker hijau zamrud dengan bulan sabit Islam.
     - **Fase Kemunduran / Tekanan Perang**: Marker terakota oranye.
     - **Telah Berintegrasi ke NKRI**: Marker biru safir simbolik.
     - **Bertahan sebagai Lembaga Adat/Kultural**: Simbol pilar cagar budaya.
     - **Telah Runtuh / Dilebur**: Marker abu-abu pudar.
     - **Belum Berdiri**: Tersembunyi (dalam mode aktif) atau abu-abu transparan.

3. **Panel Detail Kerajaan (Sliding Detail Drawer)**:
   - Profil lengkap, variasi nama (*alternate names*), pendiri, ibu kota, dan koordinat GPS situs cagar budaya.
   - Banner Era Keemasan dengan penjelasan historis mengenai faktor ekonomi, militer, dan intelektualnya.
   - **Dropdown Interaktif Silsilah Sultan**: Pemilihan sultan yang menampilkan masa kekuasaan, biografi ringkas, dan daftar pencapaian/kebijakan utama. Dilengkapi deteksi otomatis: jika tahun pada linimasa sesuai dengan masa jabatan seorang sultan, sistem akan menandai *"[Sedang Memerintah pada Tahun Ini]"*.
   - Kronologi peristiwa penting (*key historical events*).
   - Inventaris peninggalan arkeologis & cagar budaya (masjid kuno, keraton, makam, naskah, mata uang dirham/koin emas).
   - Catatan historiografi & status kepastian data (*certainty level*).
   - Daftar sumber rujukan akademik yang mendukung narasi kerajaan tersebut.

4. **Penyaringan & Pencarian Komprehensif**:
   - Pencarian teks instan berdasarkan nama kesultanan, variasi nama lokal, maupun nama ibu kota.
   - Filter cepat wilayah kepulauan: Semua, Sumatera, Jawa, Kalimantan, Sulawesi, Maluku & Papua, Nusa Tenggara.
   - Tombol filter khusus **Era Keemasan** (menyorot kesultanan yang sedang berada di masa puncak).
   - Beralih mode: **Mode Kronologis Aktif** vs **Mode Semua Titik Terpetakan**.

5. **Panel Sumber Sejarah Akademik & Cagar Budaya**:
   - Modal bibliografi yang memuat 20 literatur akademik, buku sejarah standar (Ricklefs, De Graaf & Pigeaud, Anthony Reid, Leonard Andaya, Marwati Poesponegoro), naskah primer (*Bo' Sangaji Kai*, *Suma Oriental* Tome Pires, *Rihlah* Ibnu Battuta), dan Sistem Registrasi Nasional Cagar Budaya Kemendikbudristek RI.

---

## 🏛️ Metodologi Geospasial Historis

Mengapa memetakan **titik koordinat pusat kekuasaan (istana/keraton/pelabuhan)**, bukan poligon wilayah?
Sesuai konsensus sejarawan Asia Tenggara (teori formasi politik *Mandala* oleh Prof. O.W. Wolters), kedaulatan kerajaan pra-modern di Nusantara berkarakter jaringan patronase maritim, aliran komoditas upeti, dan kesetiaan dinasti, bukan perbatasan garis teritorial administratif statis seperti negara bangsa modern Eropa pasca-Perjanjian Westphalia.

Oleh sebab itu, pembuatan poligon wilayah pengaruh dinilai berpotensi anakronistis dan menyesatkan. Pendekatan ilmiah yang sahih adalah menempatkan **titik pusat kedudukan politik (pusat istana/keraton)** berdasarkan koordinat situs arkeologis nyata yang telah terverifikasi oleh balai pelestarian kebudayaan.

---

## 📂 Struktur Repositori & Berkas

```
webgis-islamic-history/
├── index.html                  # Halaman utama aplikasi WebGIS
├── README.md                   # Dokumentasi proyek, struktur data, dan panduan
├── .gitignore                  # Berkas pengecualian Git
├── assets/
│   ├── css/
│   │   └── style.css           # Desain visual atlas sejarah responsif
│   └── js/
│       ├── app.js              # Inisialisasi utama, orchestrator & modal controller
│       ├── map.js              # Modul peta Leaflet, custom SVG marker & popup generator
│       ├── timeline.js         # Pengontrol linimasa slider, animasi play/pause & century jump
│       ├── detail.js           # Panel detail kerajaan & interaksi dropdown sultan
│       └── filters.js          # Pengelola filter wilayah, pencarian, & status keemasan
└── data/
    ├── kingdoms.json           # Database 36 kesultanan/kerajaan Islam Nusantara
    ├── sultans.json            # Database 101 sultan dengan biografi & tahun takhta
    └── sources.json            # Database 20 referensi akademik & pustaka primer
```

---

## 📊 Dokumentasi Skema Struktur Data JSON

### 1. `data/kingdoms.json`
Setiap objek kerajaan memiliki struktur data:
```json
{
  "id": "samudera-pasai",
  "name": "Kesultanan Samudera Pasai",
  "alternate_names": ["Samudera Shalihat", "Pasai", "Samudra"],
  "region": "Sumatera",
  "year_founded": 1267,
  "year_founded_display": "c. 1267 M",
  "year_ended": 1521,
  "year_ended_display": "1521 M (Ditaklukkan Portugis & diserap ke Aceh Darussalam)",
  "status_timeline_type": "ended",
  "founder": "Meurah Silu (Sultan Malik as-Saleh)",
  "capital_city": "Geudong / Samudera, Aceh Utara",
  "coordinates": {
    "lat": 5.1278,
    "lng": 97.2098
  },
  "golden_age": {
    "start_year": 1350,
    "end_year": 1400,
    "leader": "Sultan Ahmad Malik az-Zahir & Sultan Zainal Abidin I",
    "description": "Menjadi episentrum perdagangan internasional dan transmisi intelektual Islam di Selat Malaka..."
  },
  "historical_summary": "Kesultanan Samudera Pasai merupakan kerajaan Islam pertama di Nusantara...",
  "key_events": [
    { "year": 1267, "event": "Meurah Silu memeluk Islam dan mendirikan Kesultanan..." }
  ],
  "relics_and_heritage": [
    "Kompleks Makam Sultan Malik as-Saleh di Beuringen, Geudong",
    "Mata Uang Emas Kuno 'Deureuham' berlafaz Arab"
  ],
  "verification_status": "Terverifikasi Akademik",
  "data_certainty_level": "Tinggi",
  "certainty_notes": "Tahun berdirinya kesultanan sekitar 1267 M didukung kuat oleh kronologi epigrafi nisan...",
  "sources_ids": ["ricklefs-2008", "poesponegoro-notosusanto-2008", "alfian-1999"],
  "sultans_count": 6
}
```

### 2. `data/sultans.json`
Setiap objek sultan terhubung ke kerajaan melalui `kingdom_id`:
```json
{
  "id": "aceh-3",
  "kingdom_id": "aceh-darussalam",
  "order": 3,
  "name": "Sultan Iskandar Muda (Meukuta Alam)",
  "reign_start": 1607,
  "reign_end": 1636,
  "reign_display": "1607 – 1636 M",
  "biography": "Penguasa terbesar dalam sejarah Kesultanan Aceh Darussalam...",
  "key_achievements": [
    "Memperluas kedaulatan Aceh meliputi pesisir barat-timur Sumatera hingga Semenanjung Melayu",
    "Menyusun konstitusi dan tata hukum negara terpadu Adat Meukuta Alam"
  ],
  "is_golden_age_ruler": true,
  "reference_notes": "Ditetapkan sebagai Pahlawan Nasional Indonesia berdasarkan Keppres No. 077/TK/1993."
}
```

### 3. `data/sources.json`
Bibliografi referensi rujukan ilmiah:
```json
{
  "id": "ricklefs-2008",
  "title": "Sejarah Indonesia Modern 1200–2008",
  "authors": "M.C. Ricklefs",
  "publisher": "Penerbit Serambi, Jakarta",
  "year": 2008,
  "type": "Buku Akademik",
  "url": "https://www.perpusnas.go.id",
  "claims_supported": "Periodisasi islamisasi Nusantara sejak 1200 M, pembentukan kesultanan maritim..."
}
```

---

## 💻 Panduan Menjalankan Secara Lokal

Website ini merupakan aplikasi web statis murni (*zero external build step*), sehingga tidak memerlukan instalasi Node.js build pipeline yang rumit. Anda cukup menyajikan direktori proyek menggunakan web server lokal:

### Cara 1: Menggunakan Python (Rekomendasi Cepat)
Buka terminal/PowerShell di direktori proyek ini, lalu jalankan:
```bash
# Untuk Python 3
python -m http.server 8000
```
Buka peramban (*browser*) Anda dan kunjungi:
👉 **`http://localhost:8000/`**

### Cara 2: Menggunakan Node.js `serve` / `npx`
```bash
npx serve -l 8000 .
```
Kunjungi **`http://localhost:8000/`**.

### Cara 3: Menggunakan Ekstensi VS Code (Live Server)
Klik kanan pada berkas `index.html` di VS Code, lalu pilih **"Open with Live Server"**.

---

## 🚀 Panduan Publikasi ke GitHub Pages

Situs ini 100% kompatibel dan siap di-deploy langsung ke **GitHub Pages**:

1. **Buat Repository Baru di Akun GitHub Anda**:
   - Beri nama repository, misalnya `atlas-islam-nusantara` atau `webgis-islamic-history`.
   - Pilih visibilitas *Public*.

2. **Hubungkan dan Dorong Berkas dari Komputer Lokal**:
   Buka terminal di folder proyek ini:
   ```bash
   git init
   git add .
   git commit -m "feat: inisialisasi Atlas Sejarah Kerajaan Islam Nusantara"
   git branch -M main
   git remote add origin https://github.com/USERNAME-ANDA/NAMA-REPO-ANDA.git
   git push -u origin main
   ```

3. **Aktifkan Fitur GitHub Pages**:
   - Buka halaman repository di GitHub browser.
   - Masuk ke tab **Settings** &gt; **Pages** (di bilah navigasi kiri).
   - Pada bagian **Build and deployment** &gt; **Source**, pilih **Deploy from a branch**.
   - Pada bagian **Branch**, pilih cabang `main` dan folder `/ (root)`.
   - Klik **Save**.
   - Tunggu sekitar 1–2 menit, situs Anda akan aktif di URL:
     `https://USERNAME-ANDA.github.io/NAMA-REPO-ANDA/`

---

## 🔍 Ringkasan Pengujian & Keterbatasan Data

### Fitur yang Telah Diuji & Berfungsi:
- [x] **Pemuatan Peta & Multi-Basemap**: Berfungsi sempurna pada CartoDB Positron, Dark Matter, OSM, dan Esri Satellite.
- [x] **Koordinat & Bounding Box**: Seluruh 36 koordinat pusat kerajaan diverifikasi berada di dalam batas lintang-bujur kepulauan Indonesia.
- [x] **Sinkronisasi Linimasa**: Slider tahun dari 1200 M hingga 1950 M memperbarui status marker, label era, dan statistik aktif secara *real-time*.
- [x] **Dropdown Sultan Dinamis**: Dropdown sultan berganti sesuai kerajaan yang dipilih, menampilkan biografi, prestasi, dan lencana masa pemerintahan yang sinkron dengan tahun yang sedang aktif.
- [x] **Pencarian & Filter Wilayah**: Filter wilayah (Sumatera, Jawa, Kalimantan, Sulawesi, Maluku & Papua, Nusa Tenggara) dan kotak pencarian teks berfungsi instan.
- [x] **Responsivitas Layar**: Diuji pada resolusi desktop maupun layar ponsel kecil (panel detail menyusut rapi menjadi *bottom sheet/sliding panel*).

### Keterbatasan Data & Arahan Riset Lanjutan:
1. **Ketidakpastian Tanggal Awal Dinasti**: Beberapa kesultanan memiliki tradisi lisan naskah lokal yang menyebutkan tahun berdiri jauh lebih awal daripada bukti arkeologis tertulis tertua (misalnya: Perlak naskah lokal 840 M vs verifikasi nisan dan catatan Marco Polo 1292 M; Demak 1475 M status kadipaten vs 1500 M kemerdekaan penuh). Ketidakpastian ini telah dicatat secara transparan pada bagian *Historiografi & Tingkat Kepastian* di setiap kartu kerajaan.
2. **Kelengkapan Silsilah Kerajaan Timur**: Beberapa petuanan kepulauan di kawasan Papua Barat (Misool, Rumbati, Patipi) memiliki silsilah dinasti lokal yang sebagian besar masih dirawat secara lisan oleh para tetua marga/klan (seperti klan Umkabu dan Bauw), sehingga silsilah sultan yang dicantumkan baru mencakup tokoh-tokoh yang telah tercatat dalam arsip ekspedisi kolonial dan publikasi Balai Arkeologi.
