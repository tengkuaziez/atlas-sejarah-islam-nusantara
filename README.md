# Atlas Sejarah Kerajaan Islam Nusantara
### *Sistem Informasi Geografis (WebGIS) Interaktif, Poligon Historis, Situs Cagar Budaya, & Integrasi NKRI*

Sebuah aplikasi **WebGIS Sejarah Murni Sisi Klien (Client-Side Historical WebGIS)** komprehensif yang memetakan perkembangan Islam di kepulauan Nusantara (Indonesia), mulai dari bukti awal epigrafi abad ke-11 M (Leran 1082 M), kemunculan emporium maritim kesultanan, poligon kedaulatan temporal, para penguasa, situs cagar budaya (masjid kuno, keraton, makam, benteng, pelabuhan), hingga peristiwa kemerdekaan 1945 dan proses integrasi kerajaan-kerajaan swapraja ke dalam **Negara Kesatuan Republik Indonesia (NKRI)**.

Website dirancang dengan estetika **Historical Digital Atlas** (perpaduan nuansa kartografi kuno, tipografi klasik *Cinzel* & modern *Plus Jakarta Sans*, aksen emas bakar dan zamrud Islam), sepenuhnya dioptimalkan secara responsif untuk smartphone (anti-tumpang-tindih dengan sliding bottom-sheet & multi-row timeline), serta tanpa ketergantungan API berbayar sehingga dapat langsung dipublikasikan melalui **GitHub Pages**.

---

## 🌟 Fitur Utama Sistem

1. **Peta Interaktif 2D Berbasis Leaflet.js**:
   - Memetakan 36 kerajaan dan kesultanan Islam di 6 zona geografis kepulauan: **Sumatera, Jawa, Kalimantan, Sulawesi, Maluku & Papua, dan Nusa Tenggara**.
   - Penanda (*marker*) kustom dengan simbol ornamen islami, mahkota keemasan, dan lencana peninggalan budaya.
   - **Pemetaan Poligon Wilayah Historis Temporal (Historical Territory Mapping)**: 13 lapisan batas kedaulatan spasial (*core*, *controlled*, *influence*) berbasis atlas sejarah akademik otoritatif (Robert Cribb 2000, Anthony Reid, Claude Guillot).
   - **Lapisan Titik Situs Cagar Budaya Bersejarah (Historical Sites Layer)**: Memetakan 26 situs arkeologis (masjid bersejarah, keraton/istana, makam diraja, benteng maritim, dan pelabuhan transito kuno) berkoordinat presisi tinggi.
   - Pilihan multi-basemap (100% Gratis & Tanpa API Key): **OpenStreetMap Standard** (default), **Esri National Geographic** (gaya atlas sejarah klasik bernuansa kartografi kuno), **OpenTopoMap** (relief kontur & elevasi), dan **Citra Satelit Esri World Imagery**.

2. **Linimasa Kronologis Dinamis Lintas Zaman (Interactive Timeline 1082–1956 M)**:
   - Slider rentang tahun dari tahun 1082 M (Nisan Leran) hingga 1956 M (Tidore & Perjuangan Irian Barat).
   - Tombol **Play / Pause** otomatis untuk animasi pergerakan sejarah per tahun.
   - Pilihan lompatan abad cepat (*Century Quick Jump*): 1082 (Leran), 1267 (Pasai), 1400, 1475 (Demak), 1526 (Banten/Banjar), 1575 (Ternate), 1625 (Puncak Keemasan), 1670 (Makassar), 1755 (Giyanti), 1825 (Perang Diponegoro), 1900 (Kolonial), 1945 (Kemerdekaan RI), dan 1956 (Irian Barat).
   - Penyesuaian serentak (*quad-sync*): memperbarui status kerajaan, poligon wilayah aktif, situs sejarah yang telah berdiri, dan statistik secara *real-time*.
   - **Deteksi Era Kemerdekaan & NKRI**: Menandai periode 1945–1956 M dengan aksen Merah Putih khusus pada linimasa.

3. **Status Integrasi ke Negara Kesatuan Republik Indonesia (NKRI)**:
   - Mendokumentasikan secara historiografis proses peralihan kedaulatan kerajaan ke Republik Indonesia:
     - **Amanat 5 September 1945**: Sri Sultan Hamengkubuwono IX & KGPAA Paku Alam VIII (Daerah Istimewa Yogyakarta).
     - **Maklumat 1 September 1945**: Kasunanan Surakarta & Mangkunegaran.
     - **Proklamasi Siak 1945**: Sultan Syarif Kasim II menyerahkan 13 juta gulden & mahkota diraja kepada Presiden Soekarno.
     - **Integrasi Swapraja Kalimantan & Indonesia Timur**: Kesultanan Pontianak (Sultan Hamid II perancang lambang Garuda Pancasila), Kutai Kartanegara, Buton, Luwu (Andi Djemma), Ternate, Bima, dan Tidore (Sultan Zainal Abidin Syah sebagai Gubernur Pertama Irian Barat 1956).
     - Transformasi swapraja menjadi kabupaten/kota otonom (1950–1960) dan kelestarian keraton sebagai lembaga pemangku adat & cagar budaya.

4. **Panel Detail Multi-Entitas (Kerajaan, Sultan, & Situs Cagar Budaya)**:
   - **Detail Kerajaan**: Profil lengkap, variasi nama (*alternate names*), pendiri, ibu kota, koordinat GPS, banner era keemasan, dropdown sultan dinamis, inventaris tinggalan, historiografi kepastian, rujukan akademik, dan kartu integrasi NKRI.
   - **Detail Situs Sejarah**: Kurun pembangunan, status cagar budaya nasional, signifikansi peradaban Islam, kondisi fisik kontemporer, dan relasi dinasti.

5. **Panel Kronologi Peristiwa Sejarah (1082–1956 M)**:
   - Menampilkan 25 peristiwa penting: awal bukti Islam, konversi penguasa, pembangunan masjid raya, hegemoni maritim, perlawanan kolonial, perjanjian partisi (Bongaya, Giyanti), hingga pembentukan NKRI.

6. **Desain Mobile Anti-Tumpang-Tindih & Bottom Sheet**:
   - Layout mobile bebas tabrakan visual:
     - Header ringkas dengan tombol aksi berjarak ergonomis.
     - Filter pulau (*floating glass pills*) ramping tanpa kartu putih tebal yang menghalangi peta Sumatera.
     - Linimasa multi-baris mobile: tahun `1636 M` dipastikan satu baris utuh (`white-space: nowrap`), slider 100% lebar layar, playback dan century jump berjajar rapi.
     - Tombol *Collapse Timeline* untuk menyusutkan linimasa menjadi bilah tipis 38px saat menjelajah peta.
     - Modal *Kontrol Lapisan & Filter* untuk memilih basemap dan switch layer pada layar sentuh.

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
│   │   └── style.css           # Desain visual atlas responsif & layout mobile multi-row
│   └── js/
│       ├── app.js              # Orchestrator utama, pemuatan data paralel & modal controller
│       ├── map.js              # Leaflet engine, custom SVG markers, territory & sites layers
│       ├── timeline.js         # Pengontrol linimasa (1082–1956 M), animasi & status NKRI
│       ├── detail.js           # Drawer detail kerajaan, sultan, situs cagar budaya & integrasi NKRI
│       └── filters.js          # Pengelola filter wilayah, pencarian, mode & kategori situs
├── data/
│   ├── kingdoms.json           # Database 36 kesultanan/kerajaan Islam Nusantara + metadata NKRI
│   ├── sultans.json            # Database 101 sultan dengan biografi & tahun takhta
│   ├── sites.json              # Database 26 situs cagar budaya (masjid, keraton, makam, benteng, pelabuhan)
│   ├── events.json             # Database 25 peristiwa sejarah dari 1082 M hingga 1956 M
│   ├── sources.json            # Database 23 referensi akademik & dokumen arsip primer
│   ├── historical-map-sources.json # Metadata kartografis, georeferensi GCP & lisensi peta
│   └── historical-territories.geojson # 13 Feature Poligon temporal berstandar WGS84 (EPSG:4326)
└── scripts/
    ├── process_historical_maps.py # Pipeline validasi geometri & ekspor GeoJSON tergeoreferensi
    └── generate_sites_and_events.py # Pipeline kompilasi sites.json, events.json & integrasi NKRI
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
