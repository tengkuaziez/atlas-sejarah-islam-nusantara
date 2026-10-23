# MODUL PELATIHAN PRAKTIKUM: PENGEMBANGAN SISTEM INFORMASI GEOGRAFIS BERBASIS WEB (WEBGIS) TEMATIK MENGGUNAKAN EKOSISTEM ARTIFICIAL INTELLIGENCE & PARADIGMA ZERO-MANUAL DEPLOYMENT
*Panduan Lengkap Alur Kerja: Ekstraksi Data Spasial Otomatis, Protokol Validasi Geodesi Anti-Halusinasi, Perancangan Antarmuka Responsif, hingga Publikasi Terbuka Tanpa Perlu Deploy Ulang Manual ke GitHub (Alokasi: 120 Menit)*

---

## DAFTAR ISI
1. [Bagian I: Pendahuluan & Landasan Teori](#bagian-i-pendahuluan--landasan-teori)
2. [Bagian II: Alokasi Waktu & Silabus Pelatihan (120 Menit)](#bagian-ii-alokasi-waktu--silabus-pelatihan-120-menit)
3. [Bagian III: Ekstraksi Data Spasial (AI Web Scraping)](#bagian-iii-ekstraksi-data-spasial-ai-web-scraping)
4. [Bagian IV: Protokol Validasi Geospasial (Anti-Hallucination)](#bagian-iv-protokol-validasi-geospasial-anti-hallucination)
5. [Bagian V: Panduan Melampirkan Dataset Mandiri Peserta (Ujian Praktikum)](#bagian-v-panduan-melampirkan-dataset-mandiri-peserta-ujian-praktikum)
6. [Bagian VI: Perancangan UI & Pemrograman Otonom (Agentic Coding)](#bagian-vi-perancangan-ui--pemrograman-otonom-agentic-coding)
7. [Bagian VII: Pilar Simplisitas — Zero-Manual Deployment & Otomasi DevOps Penuh](#bagian-vii-pilar-simplisitas--zero-manual-deployment--otomasi-devops-penuh)
8. [Bagian VIII: Lembar Evaluasi & Rubrik Penilaian Ujian Praktikum](#bagian-viii-lembar-evaluasi--rubrik-penilaian-ujian-praktikum)
9. [Bagian IX: Glosarium Istilah & Rujukan Akademik](#bagian-ix-glosarium-istilah--rujukan-akademik)

---

## Bagian I: Pendahuluan & Landasan Teori

### 1.1 Mengapa Alur Kerja Ini Menawarkan Simplisitas Nyata?
Tantangan paling menyita waktu dan kerap menjadi momok bagi peserta pelatihan WebGIS non-IT adalah **Friksi DevOps dan Deployment**. Secara tradisional, setiap kali seorang peneliti ingin memperbaiki satu baris koordinat atau mengganti foto cagar budaya di peta, ia diwajibkan melewati prosedur manual yang rumit:
1. Membuka terminal Git Bash atau command line.
2. Mengetik sintaks terminal yang rawan salah: `git status`, `git add .`, `git commit -m "update"`, dan `git push origin main`.
3. Jika terjadi konflik atau galat otentikasi Git, pemula kerap frustrasi dan terpaksa melakukan metode darurat: mengunduh ZIP, menghapus repositori, atau menyeret file satu-per-satu (*drag and drop*) ke antarmuka web GitHub.
4. Mengulangi kembali konfigurasi hosting dan menunggu pengecekan ulang.

Melalui paradigma **Agentic AI (Google Antigravity)**, seluruh friksi administratif ini **dihapuskan secara total**. Pengembang tidak perlu lagi membuka terminal, tidak perlu mengetik perintah Git, dan tidak perlu mengunggah berkas ulang ke peramban. AI bertindak sebagai teknisi DevOps otonom yang memproses, memeriksa sintaksis, melakukan commit, dan mengeksekusi push ke GitHub hanya berdasarkan satu kalimat instruksi santai.

### 1.2 Capaian Pembelajaran Workshop (Learning Outcomes)
- **Capaian Kognitif:** Menguasai konsep dasar arsitektur multi-AI geospasial serta mekanisme *Continuous Deployment (CD)* otomatis berbasis GitHub Pages.
- **Capaian Psikomotorik:** Mampu melakukan scraping data tabel web menjadi GeoJSON, memvalidasi koordinat anti-halusinasi, merakit antarmuka Leaflet mobile, dan memperbarui website live secara instan via instruksi AI.
- **Capaian Afektif:** Memiliki etika integritas data ilmiah (atribusi lisensi terbuka dan indikator *confidence level*) serta kepercayaan diri membangun solusi geospasial modern tanpa hambatan koding rumit.

---

## Bagian II: Alokasi Waktu & Silabus Pelatihan (120 Menit)

| Waktu | Durasi | Materi Pelatihan & Langkah Kerja | Keluaran (Output) Peserta |
| :--- | :--- | :--- | :--- |
| **00:00 - 00:15** | 15 menit | **Pengantar Paradigma & Ekosistem 3 Pilar AI:** Konsep WebGIS spasial temporal, peran ChatGPT, Google AI Studio, dan Antigravity. | Pemahaman arsitektur sistem |
| **00:15 - 00:40** | 25 menit | **Fase 1: AI Web Scraping & Ekstraksi Data:** Teknik mengambil data tabel web/Wikipedia dan konversi ke skema data JSON WGS84. | Berkas data mentah terstruktur |
| **00:40 - 01:00** | 20 menit | **Fase 2: Validasi Geospasial & Anti-Halusinasi:** Verifikasi koordinat (anti Lat/Lng flip), validasi toponimi citra satelit, dan penyusunan dataset ujian mandiri. | Dataset bersih terverifikasi |
| **01:00 - 01:35** | 35 menit | **Fase 3: Agentic Coding (Leaflet Engine):** Merakit peta Leaflet, popup foto lazy-loading, drawer informasi responsif seluler, dan filter pencarian. | Aplikasi WebGIS aktif di server lokal |
| **01:35 - 01:50** | 15 menit | **Fase 4: Zero-Manual Deployment ke GitHub Pages:** Instruksi AI untuk auto-push Git, aktivasi Pages 1x klik, dan penerbitan website live global. | URL aktif WebGIS (dapat dibuka di HP) |
| **01:50 - 02:00** | 10 menit | **Fase 5: Evaluasi Mandiri & Uji Live Update:** Mendemonstrasikan pembaruan instan (*one-prompt live update*) dan penilaian ujian praktikum. | Penilaian proyek mandiri |

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

---

## Bagian IV: Protokol Validasi Geospasial (Anti-Hallucination)

> [!CAUTION]
> **Peringatan Kritis tentang Halusinasi AI dalam GIS:**
> Model bahasa besar (LLM) bekerja memprediksi probabilitas kata berikutnya dan rentan mengarang angka koordinat desimal. Seluruh data spasial hasil AI **WAJIB** melalui protokol pengujian sebelum dimasukkan ke peta.

### 4.1 Uji Inversi Koordinat (Latitude / Longitude Flip Test)
Wilayah Indonesia berada pada rentang batas koordinat geografis (*Bounding Box*):
- **Latitude (&phi;):** Antara $+6^\circ	ext{ LU}$ (Sabang) hingga $-11^\circ	ext{ LS}$ (Rote).
- **Longitude (&lambda;):** Antara $+95^\circ	ext{ BT}$ hingga $+141^\circ	ext{ BT}$.

*Aturan Baku:* Jika nilai latitude bernilai positif di atas $6$ atau bernilai lebih dari $90$ (misal $110.36$), berarti koordinat tertukar dengan longitude!

### 4.2 Penetapan Tingkat Kepastian Data (Confidence Level)
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

## Bagian VII: Pilar Simplisitas — Zero-Manual Deployment & Otomasi DevOps Penuh

> [!IMPORTANT]
> **KEUNGGULAN UTAMA: TANPA DEPLOY ULANG MANUAL KE GITHUB**
> Pengembang **tidak perlu lagi menyentuh terminal Git, tidak perlu membuka halaman upload GitHub, dan tidak perlu men-deploy ulang server setiap kali ada revisi data atau bug**. Seluruh proses audit kode, commit pesan deskriptif, dan pengiriman ke server GitHub dieksekusi secara otonom oleh AI Agent langsung dari percakapan.

### Perbandingan Alur Kerja Tradisional vs Agentic AI:
| Aktivitas / Skenario | Metode Konvensional (Manual) | Metode Agentic AI (Otonom) |
| :--- | :--- | :--- |
| **Menambah 5 Titik Data Baru** | Buka file JSON manual, ketik kurung kurawal, buka terminal, ketik git add, commit, push. | Cukup katakan: *"Tolong tambahkan 5 data ini dan langsung update ke GitHub."* AI mengedit dan mengeksekusi push otomatis. |
| **Memperbaiki Bug CSS di HP** | Cari file CSS baris demi baris, uji browser, buka git bash, commit ulang, push ulang. | Cukup katakan: *"Tombol zoom ketutupan drawer di HP, tolong perbaiki posisi dan deploy sekarang."* Selesai dalam 30 detik. |
| **Penanganan Galat Git** | Pengembang bingung memecahkan pesan galat terminal (merge conflict, head detached). | AI membaca output log terminal, menganalisis status repositori, dan menyelesaikan sinkronisasi branch secara otomatis. |

### Konsep "Set Once, Continuous Auto-Deploy Forever":
Aktivasi GitHub Pages hanya dilakukan **satu kali saja di awal** (hanya 30 detik):
1. Buka repositori GitHub di browser &rarr; menu **Settings** &rarr; menu **Pages**.
2. Pada bilah *Build and deployment* &rarr; *Branch*: pilih `main` dan direktori `/ (root)` &rarr; Klik **Save**.

Setelah itu, seluruh pembaruan berjalan secara **live otomatis**:
- AI menjalankan perintah `git commit` dan `git push origin main` di latar belakang.
- Server GitHub mendeteksi perubahan melalui *GitHub Actions Webhook*.
- Dalam tempo 30–60 detik, alamat website publik (`https://username.github.io/repo/`) otomatis terbarui secara global tanpa perlu me-refresh server atau mengunggah berkas apa pun lagi.

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

- **Zero-Manual Deployment:** Pola pengembangan web di mana pengembang tidak perlu lagi menjalankan perintah terminal Git atau mengunggah berkas secara manual ke server hosting; seluruh siklus kompilasi dan pengiriman kode ditangani secara mandiri oleh Agentic AI.
- **CRS (Coordinate Reference System):** Sistem proyeksi matematis penentuan posisi di permukaan bumi.
- **WGS84 (EPSG:4326):** Datum geodetik standar Leaflet dan GPS dengan format lintang bujur desimal.
- **GeoJSON:** Format pertukaran data geografis terbuka berbasis JSON.
- **Lat/Lng Inversion:** Galat tertukarnya lintang dan bujur yang melempar titik ke samudra antah berantah.
- **Agentic AI:** AI otonom yang mampu menggunakan perkakas terminal, membaca file, dan memperbaiki kode secara mandiri.

---
*Modul Pelatihan & Ujian Praktikum: Pengembangan WebGIS Tematik Menggunakan Ekosistem Multi-AI & Paradigma Zero-Manual Deployment (2026).*
