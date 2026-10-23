# MODUL PELATIHAN PRAKTIKUM: PENGEMBANGAN SISTEM INFORMASI GEOGRAFIS BERBASIS WEB (WEBGIS) TEMATIK MENGGUNAKAN EKOSISTEM ARTIFICIAL INTELLIGENCE
*Panduan Komprehensif: Ekstraksi Data Spasial Otomatis, Protokol Validasi Geodesi Anti-Halusinasi, Perancangan Antarmuka Responsif, Pemrograman Otonom, hingga Publikasi Terbuka di GitHub Pages (Alokasi: 120 Menit)*

---

## DAFTAR ISI
1. [Bagian I: Pendahuluan & Landasan Teori](#bagian-i-pendahuluan--landasan-teori)
2. [Bagian II: Alokasi Waktu & Silabus Pelatihan (120 Menit)](#bagian-ii-alokasi-waktu--silabus-pelatihan-120-menit)
3. [Bagian III: Ekstraksi Data Spasial (AI Web Scraping)](#bagian-iii-ekstraksi-data-spasial-ai-web-scraping)
4. [Bagian IV: Protokol Validasi Geospasial (Anti-Hallucination)](#bagian-iv-protokol-validasi-geospasial-anti-hallucination)
5. [Bagian V: Panduan Melampirkan Dataset Mandiri Peserta (Ujian Praktikum)](#bagian-v-panduan-melampirkan-dataset-mandiri-peserta-ujian-praktikum)
6. [Bagian VI: Perancangan UI & Pemrograman Otonom (Agentic Coding)](#bagian-vi-perancangan-ui--pemrograman-otonom-agentic-coding)
7. [Bagian VII: Publikasi Terbuka di GitHub Pages](#bagian-vii-publikasi-terbuka-di-github-pages)
8. [Bagian VIII: Lembar Evaluasi & Rubrik Penilaian Ujian Praktikum](#bagian-viii-lembar-evaluasi--rubrik-penilaian-ujian-praktikum)
9. [Bagian IX: Glosarium Istilah & Rujukan Akademik](#bagian-ix-glosarium-istilah--rujukan-akademik)

---

## Bagian I: Pendahuluan & Landasan Teori

### 1.1 Transformasi Paradigma Geospasial di Era AI
Sistem Informasi Geografis Berbasis Web (WebGIS) telah menjadi media paling efektif dalam mendemokratisasikan data geospasial kepada publik. Melalui peramban web tanpa memerlukan instalasi perangkat lunak GIS desktop yang berat, pengguna awam dapat mengeksplorasi data sebaran, pola keruangan, hingga analisis temporal.

Pengembangan WebGIS konvensional menuntut keahlian kartografi geodesi, struktur data GeoJSON/WGS84, frontend HTML/CSS/JavaScript, pustaka Leaflet.js, serta administrasi server. Hadirnya **Generative AI** dan **Agentic AI Coding Assistant** mentransformasi pengembang menjadi **Arsitek Sistem (System Architect)** dan **Kurator Kualitas Data (Quality Assurer)**, sementara AI mengotomasi penulisan kode sintaksis dan perbaikan bug.

### 1.2 Capaian Pembelajaran Workshop (Learning Outcomes)
- **Capaian Kognitif:** Memahami arsitektur ekosistem multi-AI dan prinsip mitigasi halusinasi toponimi.
- **Capaian Psikomotorik:** Mampu mengekstrak data tabel web, mengoreksi koordinat (lat/lng inversion), merakit Leaflet responsif mobile, dan mempublikasikan kode ke GitHub Pages.
- **Capaian Afektif:** Menjunjung etika integritas data ilmiah dengan menyertakan sumber referensi, lisensi terbuka, dan skor kepastian data (*confidence level*).

---

## Bagian II: Alokasi Waktu & Silabus Pelatihan (120 Menit)

| Waktu | Durasi | Materi Pelatihan & Langkah Kerja | Keluaran (Output) Peserta |
| :--- | :--- | :--- | :--- |
| **00:00 - 00:15** | 15 menit | **Pengantar Paradigma & Ekosistem 3 Pilar AI:** Konsep WebGIS spasial temporal, peran ChatGPT, Google AI Studio, dan Antigravity. | Pemahaman arsitektur sistem |
| **00:15 - 00:40** | 25 menit | **Fase 1: AI Web Scraping & Ekstraksi Data:** Teknik mengambil data tabel web/Wikipedia dan konversi ke format JSON WGS84. | Berkas data mentah terstruktur |
| **00:40 - 01:00** | 20 menit | **Fase 2: Validasi Geospasial & Anti-Halusinasi:** Verifikasi koordinat (anti Lat/Lng flip), validasi toponimi citra satelit, dan penyusunan dataset ujian mandiri. | Dataset bersih terverifikasi |
| **01:00 - 01:35** | 35 menit | **Fase 3: Agentic Coding (Leaflet Engine):** Merakit peta Leaflet, popup foto lazy-loading, drawer informasi responsif seluler, dan filter pencarian. | Aplikasi WebGIS aktif di server lokal |
| **01:35 - 01:50** | 15 menit | **Fase 4: Otomasi Publikasi ke GitHub Pages:** Perintah Git otomatis via AI dan peluncuran website publik. | URL aktif WebGIS peserta |
| **01:50 - 02:00** | 10 menit | **Fase 5: Evaluasi Mandiri & Pengumpulan Ujian:** Pengujian WebGIS di smartphone dan review hasil ujian praktikum. | Penilaian proyek mandiri |

---

## Bagian III: Ekstraksi Data Spasial (AI Web Scraping)

### 3.1 Metode AI Table & Text Parsing (Tanpa Koding)
Peserta dapat menyalin tabel dari halaman web/Wikipedia, kemudian memberikan prompt terstruktur:

```text
"Anda adalah Data Extraction Specialist. Berikut teks daftar cagar budaya yang saya salin:
[TEMPELKAN TEKS / TABEL DARI WEBSITE]

Tugas:
1. Ekstrak menjadi format JSON array murni tanpa narasi pembuka/penutup.
2. Setiap objek wajib memuat atribut: id, nama_objek, kategori, tahun_pembangunan, latitude, longitude, deskripsi, sumber_referensi.
3. Estimasi koordinat geografis dalam sistem proyeksi CRS WGS84 (EPSG:4326).
4. Verifikasi bahwa nilai Latitude bernilai negatif untuk wilayah Indonesia (0 s/d -11) dan Longitude berkisar antara 95 s/d 141 BT."
```

### 3.2 Metode Otomasi Python Scraping
Untuk data berskala besar, AI dapat mengenerate skrip Python dengan pustaka `BeautifulSoup` dan `requests` guna mengekspor baris tabel web langsung ke berkas `data/sites.json`.

---

## Bagian IV: Protokol Validasi Geospasial (Anti-Hallucination)

> [!CAUTION]
> **Peringatan Kritis tentang Halusinasi AI dalam GIS:**
> Model bahasa besar (LLM) bekerja memprediksi probabilitas kata berikutnya dan rentan mengarang angka koordinat desimal. Seluruh data spasial hasil AI **WAJIB** melalui protokol pengujian sebelum dimasukkan ke peta.

### 4.1 Uji Inversi Koordinat (Latitude / Longitude Flip Test)
Wilayah Indonesia berada pada batas koordinat (*Bounding Box*):
- **Latitude ($\phi$):** $+6^\circ	ext{ LU}$ (Sabang) hingga $-11^\circ	ext{ LS}$ (Rote).
- **Longitude ($\lambda$):** $+95^\circ	ext{ BT}$ hingga $+141^\circ	ext{ BT}$.

*Aturan Baku:* Jika nilai latitude bernilai positif di atas $6$ atau bernilai lebih dari $90$ (misal $110.36$), berarti koordinat tertukar dengan longitude!

### 4.2 Verifikasi Toponimi Fisik vs Administrasi Modern
Pastikan titik koordinat mengarah langsung pada tapak fisik cagar budaya sebenarnya (melalui citra satelit OpenStreetMap / Google Maps), bukan sekadar kantor pemerintahan kecamatan setempat.

### 4.3 Penetapan Tingkat Kepastian Data (Confidence Level)
- **Tinggi:** Objek cagar budaya memiliki wujud fisik utuh dan terdaftar resmi di Kemendikbudristek / BPCB.
- **Sedang:** Sisa reruntuhan fondasi arkeologis ditemukan dan didukung laporan arsip.
- **Interpretatif:** Hanya bersumber dari teks naskah kuno/babad tanpa sisa arsitektur fisik yang definitif.

---

## Bagian V: Panduan Melampirkan Dataset Mandiri Peserta (Ujian Praktikum)

Peserta menyusun berkas `data/dataset_mandiri.csv` dengan struktur kolom:

| id | nama_objek | kategori | latitude | longitude | tahun_awal | tahun_akhir | foto_url | sumber_data |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `obj-01` | Masjid Agung Demak | ibadah | -6.8946 | 110.6373 | 1479 | 9999 | https://commons.../Demak.jpg | BPCB Jawa Tengah |
| `obj-02` | Benteng Somba Opu | benteng | -5.1897 | 119.3982 | 1525 | 1669 | https://commons.../Somba.jpg | Balai Cagar Budaya Sulsel |

Instruksi ke Antigravity:
```text
"Saya telah menyiapkan dataset mandiri untuk ujian praktikum di 'data/dataset_mandiri.csv'.
Tolong validasi koordinatnya, konversikan ke 'data/sites.json' berstandar WGS84, dan integrasikan layernya ke WebGIS Leaflet lengkap dengan penanda kustom dan popup foto."
```

---

## Bagian VI: Perancangan UI & Pemrograman Otonom (Agentic Coding)

- **Desain Mobile-First:** Tata letak disesuaikan dengan layar smartphone (viewport 360–400px) menggunakan *floating timeline bar* dan *interactive bottom sheet*.
- **Arsitektur Modular:** Pemisahan logika kode ke dalam `map.js` (Leaflet), `timeline.js` (waktu), `detail.js` (drawer & foto), dan `filters.js` (kategori).
- **Optimasi Performa Media:** Menerapkan `loading="lazy"` pada gambar foto dokumentasi untuk mencegah lag dan konsumsi memori berlebih di perangkat mobile.

---

## Bagian VII: Publikasi Terbuka di GitHub Pages

1. Pastikan seluruh kode telah di-push ke repositori GitHub pada branch `main`.
2. Buka menu **Settings** di repositori GitHub &rarr; pilih menu **Pages**.
3. Di bagian *Branch*, pilih `main` dan folder `/ (root)` &rarr; klik **Save**.
4. Website aktif dan live di alamat: `https://[username].github.io/[nama-repo]/`.

---

## Bagian VIII: Lembar Evaluasi & Rubrik Penilaian Ujian Praktikum

| Komponen Penilaian | Bobot | Indikator Keberhasilan (Kriteria Objektif) |
| :--- | :--- | :--- |
| **1. Integritas Data & Validasi Spasial** | **30%** | Bebas lat/lng inversion; koordinat presisi di Indonesia; format JSON WGS84 valid; memiliki label confidence level. |
| **2. Fungsionalitas Peta & Interaktivitas** | **25%** | Basemap Leaflet berfungsi; marker interaktif; filter pencarian dan kategori bekerja normal. |
| **3. Kualitas UI/UX & Responsif Mobile** | **25%** | Tidak tumpang tindih di viewport 360px; drawer dapat digeser; gambar dokumentasi menerapkan lazy loading. |
| **4. Publikasi & Continuous Deployment** | **20%** | WebGIS sukses tayang di GitHub Pages tanpa galat 404; riwayat commit Git terdokumentasi rapi. |

---

## Bagian IX: Glosarium Istilah & Rujukan Akademik

- **CRS (Coordinate Reference System):** Sistem proyeksi matematis penentuan posisi di permukaan bumi.
- **WGS84 (EPSG:4326):** Datum geodetik standar Leaflet dan GPS dengan format lintang bujur desimal.
- **GeoJSON:** Format pertukaran data geografis terbuka berbasis JSON.
- **Lat/Lng Inversion:** Galat tertukarnya lintang dan bujur yang melempar titik ke samudra antah berantah.
- **Agentic AI:** AI otonom yang mampu menggunakan perkakas terminal, membaca file, dan memperbaiki kode secara mandiri.

---
*Modul Pelatihan & Ujian Praktikum: Pengembangan WebGIS Tematik Menggunakan Ekosistem Multi-AI (2026).*
