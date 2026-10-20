# Atlas Sejarah Kerajaan Islam Nusantara
### *Sistem Informasi Geografis (WebGIS) Interaktif & Kronologi Kesultanan Nusantara*

Sebuah aplikasi **WebGIS Sejarah Murni Sisi Klien (Client-Side Historical WebGIS)** yang memetakan persebaran pusat pemerintahan kerajaan dan kesultanan Islam di seluruh kepulauan Nusantara (Indonesia), mulai dari fase awal islamisasi maritim (abad ke-13 M) hingga integrasi ke dalam Negara Kesatuan Republik Indonesia (1945 M).

Website dirancang dengan estetika **Historical Digital Atlas** (perpaduan nuansa kartografi kuno, tipografi klasik *Cinzel* & modern *Plus Jakarta Sans*, aksen emas bakar dan zamrud Islam), sepenuhnya responsif untuk perangkat desktop maupun ponsel, serta tanpa ketergantungan API berbayar sehingga dapat langsung dipublikasikan melalui **GitHub Pages**.

---

## 🌟 Fitur Utama Sistem

1. **Peta Interaktif 2D Berbasis Leaflet.js**:
   - Memetakan 36 kerajaan dan kesultanan Islam di 6 zona geografis kepulauan: **Sumatera, Jawa, Kalimantan, Sulawesi, Maluku & Papua, dan Nusa Tenggara**.
   - Penanda (*marker*) kustom dengan simbol ornamen islami, mahkota keemasan, dan lencana peninggalan budaya.
   - **Pemetaan Poligon Wilayah Historis Temporal (Historical Territory Mapping)**: Lapisan batas pengaruh spasial (*core*, *controlled*, *influence*) yang berbasis atlas sejarah akademik, tersinkronisasi linimasa, dan dapat diaktifkan/dinonaktifkan secara independen.
   - Pilihan multi-basemap (100% Gratis & Tanpa API Key): **OpenStreetMap Standard** (default), **Esri National Geographic** (gaya atlas sejarah klasik bernuansa kartografi kuno), **OpenTopoMap** (relief kontur & elevasi), dan **Citra Satelit Esri World Imagery**.

2. **Linimasa Kronologis Dinamis (Interactive Timeline 1200–1950 M)**:
   - Slider rentang tahun dari tahun 1200 M hingga 1950 M.
   - Tombol **Play / Pause** otomatis untuk animasi pergerakan sejarah per tahun.
   - Pilihan lompatan abad cepat (*Century Quick Jump*): 1267 (Pasai), 1400, 1475 (Demak), 1526 (Banten/Banjar), 1575 (Ternate), 1625 (Puncak Keemasan), 1670 (Makassar), 1755 (Giyanti), 1825 (Perang Diponegoro), 1900, dan 1945 (Kemerdekaan RI).
   - Penyesuaian ganda (*dual sync*): memperbarui status titik marker sekaligus geometri poligon wilayah historis yang aktif di tahun terpilih.
   - Status marker berubah otomatis mengikuti tahun yang dipilih:
     - **Sedang Dalam Era Keemasan (Golden Age)**: Marker emas berpendar dengan animasi denyut (*pulsing halo*).
     - **Aktif & Berdaulat**: Marker hijau zamrud dengan bulan sabit Islam.
     - **Fase Kemunduran / Tekanan Perang**: Marker terakota oranye.
     - **Telah Berintegrasi ke NKRI**: Marker biru safir simbolik.
     - **Bertahan sebagai Lembaga Adat/Kultural**: Simbol pilar cagar budaya.
     - **Telah Runtuh / Dilebur**: Marker abu-abu pudar.
     - **Belum Berdiri**: Tersembunyi (dalam mode aktif) atau abu-abu transparan.

3. **Panel Detail Kerajaan & Bottom-Sheet Responsif**:
   - Profil lengkap, variasi nama (*alternate names*), pendiri, ibu kota, dan koordinat GPS situs cagar budaya.
   - Banner Era Keemasan dengan penjelasan historis mengenai faktor ekonomi, militer, dan intelektualnya.
   - **Informasi Kartografi & Poligon Wilayah**: Menampilkan rujukan atlas sejarah, klasifikasi wilayah, metode digitasi, tingkat keyakinan (*confidence level*), serta catatan batas interpretatif. Jika kerajaan belum memiliki sumber kartografi terverifikasi, sistem menampilkan *disclaimer* transparan yang menegaskan ketiadaan batas fiktif.
   - **Dropdown Interaktif Silsilah Sultan**: Pemilihan sultan yang menampilkan masa kekuasaan, biografi ringkas, dan daftar pencapaian/kebijakan utama. Dilengkapi deteksi otomatis: jika tahun pada linimasa sesuai dengan masa jabatan seorang sultan, sistem akan menandai *"[Sedang Memerintah pada Tahun Ini]"*.
   - Kronologi peristiwa penting (*key historical events*).
   - Inventaris peninggalan arkeologis & cagar budaya (masjid kuno, keraton, makam, naskah, mata uang dirham/koin emas).
   - Catatan historiografi & status kepastian data (*certainty level*).
   - Daftar sumber rujukan akademik yang mendukung narasi kerajaan tersebut.

4. **Penyaringan, Pencarian & Kontrol Visual**:
   - Pencarian teks instan terpadu (desktop dan overlay mobile) berdasarkan nama kesultanan, variasi nama lokal, maupun nama ibu kota.
   - Tombol sakelar poligon (*Toggle Territories*) dengan indikator jumlah poligon aktif.
   - Filter cepat wilayah kepulauan: Semua, Sumatera, Jawa, Kalimantan, Sulawesi, Maluku & Papua, Nusa Tenggara.
   - Tombol filter khusus **Era Keemasan** (menyorot kesultanan yang sedang berada di masa puncak).
   - Beralih mode: **Mode Kronologis Aktif** vs **Mode Semua Titik Terpetakan**.

5. **Pengalaman Mobile Native-Grade**:
   - Desain responsif fleksibel dari layar ponsel kecil (360×800, 390×844) hingga tablet (768×1024) dan monitor ultrawide.
   - *Bottom-Sheet Drawer* dengan drag handle ergonomis di layar ponsel: peta tetap leluasa dijelajahi tanpa tertutup panel samping kaku.
   - Fitur *Collapse Timeline* untuk memaksimalkan bidang pandang peta di smartphone.
   - Target sentuh ergonomis minimal 44×44 px serta dukungan CSS `env(safe-area-inset)` untuk layar berponi (*notch/island*).

5. **Panel Sumber Sejarah Akademik & Cagar Budaya**:
   - Modal bibliografi yang memuat 20 literatur akademik, buku sejarah standar (Ricklefs, De Graaf & Pigeaud, Anthony Reid, Leonard Andaya, Marwati Poesponegoro), naskah primer (*Bo' Sangaji Kai*, *Suma Oriental* Tome Pires, *Rihlah* Ibnu Battuta), dan Sistem Registrasi Nasional Cagar Budaya Kemendikbudristek RI.

---

## 🏛️ Metodologi Geospasial Historis & Rekonstruksi Kartografis

### 1. Titik Koordinat Pusat Pemerintahan (Capital Markers)
Sesuai konsensus sejarawan Asia Tenggara (teori formasi politik *Mandala* oleh Prof. O.W. Wolters), kedaulatan kerajaan pra-modern di Nusantara berkarakter jaringan patronase maritim, aliran komoditas upeti, dan kesetiaan dinasti. Karena itu, jangkar utama pemetaan adalah **titik pusat kedudukan politik (pusat istana/keraton/pelabuhan)** berdasarkan koordinat situs arkeologis nyata yang telah terverifikasi oleh balai pelestarian cagar budaya dan kepustakaan ilmiah.

### 2. Rekonstruksi Poligon Wilayah Temporal (Historical Territory Mapping)
Untuk merepresentasikan dinamika spasial secara ilmiah tanpa menciptakan klaim anakronistis (seperti batas administratif garis tegas ala negara-bangsa modern), poligon wilayah pada sistem ini dibangun mengikuti prinsip ketat:
- **Hanya Berdasarkan Sumber Kartografi Akademik Teruji**: Bersumber dari atlas sejarah otoritatif, yaitu Robert Cribb (*Historical Atlas of Indonesia*, 2000), Anthony Reid (*An Indonesian Frontier: Acehnese & Other Histories of Sumatra*, 2005), Claude Guillot (*Banten: Sejarah dan Peradaban*, 1990), H.J. de Graaf (*De Regering van Sultan Agung*, 1958), dan Leonard Andaya (*The Heritage of Arung Palakka*, 1981).
- **Zonasi Kedaulatan Berjenjang**:
  - `core` (Wilayah Inti/Negaragung): Pusat ibu kota, kraton, dan tanah lungguh inti dinasti.
  - `controlled` (Wilayah Mancanegara/Vasalisasi Efektif): Daerah taklukan yang dipimpin bupati/gubernur militer kerajaan.
  - `influence` (Wilayah Pengaruh/Mitra Dagang Protektorat): Jaringan proteksi laut, pelabuhan sekutu, dan pengirim upeti berkala.
- **Dinamika Temporal Multi-Fase**: Wilayah kerajaan yang berekspansi atau menyusut dipetakan dengan geometri berbeda sesuai kurun waktu (misalnya: Mataram era puncak hegemoni Sultan Agung 1613–1645 vs era pecahan *Vorstenlanden* pasca-Perjanjian Giyanti 1755–1830).
- **Integritas Ilmiah & Disclaimer**: Kerajaan yang tidak memiliki atlas kartografis sejarah yang memadai **TIDAK dibuatkan poligon buatan (dilarang menggunakan buffer atau convex hull spekulatif)**. Kerajaan tersebut tetap direpresentasikan melalui penanda titik dengan catatan epistemologis transparan di panel detail.

---

## 📂 Struktur Repositori & Berkas

```
webgis-islamic-history/
├── index.html                  # Halaman utama aplikasi WebGIS responsif
├── README.md                   # Dokumentasi proyek, struktur data, dan panduan
├── .gitignore                  # Berkas pengecualian Git
├── assets/
│   ├── css/
│   │   └── style.css           # Desain visual atlas sejarah responsif & mobile bottom sheet
│   └── js/
│       ├── app.js              # Inisialisasi utama, orchestrator, controller poligon & mobile UI
│       ├── map.js              # Modul Leaflet, custom SVG marker, territory layer & popups
│       ├── timeline.js         # Pengontrol linimasa slider, animasi play/pause & century jump
│       ├── detail.js           # Panel detail kerajaan, dropdown sultan & historiografi kartografis
│       └── filters.js          # Pengelola filter wilayah, pencarian, & status keemasan
├── data/
│   ├── kingdoms.json           # Database 36 kesultanan/kerajaan Islam Nusantara
│   ├── sultans.json            # Database 101 sultan dengan biografi & tahun takhta
│   ├── sources.json            # Database 20 referensi akademik & pustaka primer
│   ├── historical-map-sources.json # Metadata kartografis, georeferensi GCP & lisensi peta
│   └── historical-territories.geojson # 13 Feature Poligon temporal berstandar WGS84 (EPSG:4326)
└── scripts/
    └── process_historical_maps.py # Pipeline Python validasi geometri, CRS WGS84 & kompilasi GeoJSON
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

### 4. `data/historical-territories.geojson`
FeatureCollection GeoJSON standar RFC 7946 (WGS84 / EPSG:4326) yang memuat poligon kedaulatan temporal berjenjang:
```json
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[110.15, -7.50], [110.65, -7.40], ...]]
  },
  "properties": {
    "polygon_id": "mataram-core-1613-1645",
    "kingdom_id": "mataram-islam",
    "kingdom_name": "Kesultanan Mataram Islam",
    "historical_period": "Puncak Kejayaan Sultan Agung",
    "year_start": 1613,
    "year_end": 1645,
    "territory_type": "core",
    "source_title": "Historical Atlas of Indonesia (Map 3.23: The expansion of Mataram, 1588-1645)",
    "source_url": "https://monoskop.org/images/9/90/Cribb_Robert_Historical_Atlas_of_Indonesia_2000.pdf",
    "source_publisher": "Curzon Press / Routledge, London & New York",
    "map_publication_year": 2000,
    "georeferencing_method": "Georeferenced to WGS84 based on recognizable geographic control points (estuaries, capes, mountains) with affine transformation",
    "digitization_method": "Manual vector digitization following academic cartographic boundaries published in historical atlas",
    "confidence_level": "Tinggi",
    "uncertainty_notes": "Batas darat mencerminkan batas hegemoni efektif Negaragung di lembah Kedu, Mataram, dan Pajang."
  }
}
```

### 5. `data/historical-map-sources.json`
Metadata kartografi lengkap yang mencatat ground control points (GCP), transformasi koordinat, penerbit, dan lisensi:
```json
{
  "source_id": "cribb-2000-mataram",
  "kingdom_id": "mataram-islam",
  "map_title": "The expansion of Mataram, 1588–1645 (Map 3.23)",
  "represented_year_range": "1588–1645 M",
  "author_cartographer": "Robert Cribb",
  "publisher": "Curzon Press / Routledge",
  "publication_year": 2000,
  "isbn": "978-0700709854",
  "georeferencing": {
    "crs_original": "Geographic projection (Cylindrical Equidistant / WGS84)",
    "gcp_count": 8,
    "transformation": "1st Order Polynomial (Affine)",
    "target_crs": "EPSG:4326 (WGS84)"
  },
  "digitization": {
    "tool": "QGIS & Python GeoJSON pipeline",
    "method": "Vector boundary digitization of shaded territorial areas"
  },
  "license_and_usage": "Academic Fair Use for non-commercial educational atlas",
  "uncertainty_and_limitations": "Historical frontiers in pre-colonial Java were dynamic zones of shifting loyalty rather than modern administrative fences."
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
- [x] **Pemuatan Peta & Multi-Basemap (Tanpa API Key)**: Berfungsi lancar pada OpenStreetMap, Esri NatGeo (Atlas Sejarah), OpenTopoMap, dan Esri Satellite.
- [x] **Koordinat & Bounding Box**: Seluruh 36 koordinat pusat kerajaan diverifikasi berada di dalam batas lintang-bujur kepulauan Indonesia.
- [x] **Pemetaan Poligon Wilayah Temporal (Historical Territory Layer)**: 13 poligon georeferensi WGS84 untuk Mataram Islam (era Sultan Agung 1613–1645 & Vorstenlanden 1755–1830), Aceh Darussalam (era Iskandar Muda 1607–1636), Banten (era Sultan Ageng Tirtayasa 1651–1683), dan Gowa-Tallo (era Sultan Hasanuddin 1636–1667) teruji tampil dengan pembedaan warna zonasi (`core`, `controlled`, `influence`).
- [x] **Hierarki Lapisan Spasial (Leaflet Panes)**: Poligon dirender di `territoriesPane` (z-index 350) di bawah penanda titik kerajaan (`markerPane`, z-index 600), sehingga penanda selalu dapat diklik tanpa terhalang bidang poligon.
- [x] **Tombol Sakelar Poligon (Territory Toggle)**: Menghidupkan/mematikan tampilan poligon secara instan beserta indikator jumlah wilayah aktif.
- [x] **Sinkronisasi Linimasa**: Slider tahun dari 1200 M hingga 1950 M memperbarui status marker, label era, poligon temporal, dan statistik aktif secara *real-time*.
- [x] **Dropdown Sultan Dinamis**: Dropdown sultan berganti sesuai kerajaan yang dipilih, menampilkan biografi, prestasi, dan lencana masa pemerintahan yang sinkron dengan tahun yang sedang aktif.
- [x] **Pencarian & Filter Wilayah**: Filter wilayah (Sumatera, Jawa, Kalimantan, Sulawesi, Maluku & Papua, Nusa Tenggara) dan kotak pencarian teks (desktop dan overlay mobile) berfungsi instan.
- [x] **Responsivitas Layar & Bottom Sheet Mobile**: Diuji pada resolusi desktop (1366×768, 1920×1080), tablet (768×1024), dan layar ponsel pintar (360×800, 390×844) tanpa *horizontal overflow*. Panel detail bertransformasi mulus menjadi *bottom sheet drawer* dengan *drag handle* dan fitur *collapse timeline*.

### Keterbatasan Data & Arahan Riset Lanjutan:
1. **Ketidakpastian Tanggal Awal Dinasti**: Beberapa kesultanan memiliki tradisi lisan naskah lokal yang menyebutkan tahun berdiri jauh lebih awal daripada bukti arkeologis tertulis tertua (misalnya: Perlak naskah lokal 840 M vs verifikasi nisan dan catatan Marco Polo 1292 M; Demak 1475 M status kadipaten vs 1500 M kemerdekaan penuh). Ketidakpastian ini telah dicatat secara transparan pada bagian *Historiografi & Tingkat Kepastian* di setiap kartu kerajaan.
2. **Kelengkapan Silsilah Kerajaan Timur**: Beberapa petuanan kepulauan di kawasan Papua Barat (Misool, Rumbati, Patipi) memiliki silsilah dinasti lokal yang sebagian besar masih dirawat secara lisan oleh para tetua marga/klan (seperti klan Umkabu dan Bauw), sehingga silsilah sultan yang dicantumkan baru mencakup tokoh-tokoh yang telah tercatat dalam arsip ekspedisi kolonial dan publikasi Balai Arkeologi.
