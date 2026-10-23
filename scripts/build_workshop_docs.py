import os
import subprocess
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))
HTML_PATH = os.path.join(DOCS_DIR, "MODUL_PANDUAN_WORKSHOP_WEBGIS.html")
PDF_PATH = os.path.join(DOCS_DIR, "MODUL_PANDUAN_WORKSHOP_WEBGIS.pdf")
DOCX_PATH = os.path.join(DOCS_DIR, "MODUL_PANDUAN_WORKSHOP_WEBGIS.docx")
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

print(f"Target Directory: {DOCS_DIR}")

# ==============================================================================
# 1. GENERATE PROFESSIONAL HTML WITH EMBEDDED SVG DIAGRAMS & PRINT CSS
# ==============================================================================
html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Modul Workshop: Pemanfaatan Multi-AI dalam Pembuatan WebGIS Sebaran</title>
<style>
  @page {
    size: A4 portrait;
    margin: 18mm 15mm 20mm 15mm;
    @bottom-right {
      content: counter(page);
      font-size: 9pt;
      color: #64748b;
    }
  }

  * { box-sizing: border-box; }
  
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.55;
    color: #1e293b;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }

  /* COVER PAGE */
  .cover-page {
    page-break-after: always;
    min-height: 92vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 30px 20px;
    border: 3px solid #0f4c3a;
    border-radius: 8px;
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
    position: relative;
  }

  .cover-badge {
    align-self: flex-start;
    background: #0f4c3a;
    color: #fde68a;
    font-size: 9pt;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 4px;
    border-left: 4px solid #d97706;
  }

  .cover-title-group {
    margin-top: 40px;
  }

  .cover-title {
    font-size: 26pt;
    font-weight: 800;
    color: #0f4c3a;
    line-height: 1.2;
    margin: 0 0 16px 0;
  }

  .cover-subtitle {
    font-size: 13pt;
    color: #475569;
    line-height: 1.45;
    margin-bottom: 25px;
    border-left: 4px solid #d97706;
    padding-left: 14px;
  }

  .cover-illustration {
    margin: 30px 0;
    text-align: center;
  }

  .cover-meta {
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 16px 20px;
    font-size: 9.5pt;
    color: #334155;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }

  .cover-meta strong {
    color: #0f4c3a;
  }

  /* HEADINGS & TYPOGRAPHY */
  h1, h2, h3, h4 {
    color: #0f4c3a;
    font-weight: 700;
    page-break-after: avoid;
  }

  h1 {
    font-size: 16pt;
    border-bottom: 2px solid #0f4c3a;
    padding-bottom: 6px;
    margin-top: 30px;
    margin-bottom: 14px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  h2 {
    font-size: 13pt;
    color: #1a5d48;
    margin-top: 22px;
    margin-bottom: 10px;
  }

  h3 {
    font-size: 11pt;
    color: #334155;
    margin-top: 16px;
    margin-bottom: 6px;
  }

  p {
    margin: 0 0 10px 0;
    text-align: justify;
  }

  ul, ol {
    margin: 0 0 12px 0;
    padding-left: 22px;
  }

  li {
    margin-bottom: 4px;
  }

  /* TABLES */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 9pt;
    page-break-inside: avoid;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 8px 10px;
    text-align: left;
    vertical-align: top;
  }

  th {
    background-color: #0f4c3a;
    color: #ffffff;
    font-weight: 700;
    letter-spacing: 0.3px;
  }

  tr:nth-child(even) td {
    background-color: #f8fafc;
  }

  /* CALLOUTS */
  .callout {
    padding: 12px 14px;
    border-radius: 6px;
    margin: 14px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
  }

  .callout-tip {
    background: #ecfdf5;
    border-left: 4px solid #059669;
    color: #065f46;
  }

  .callout-warning {
    background: #fffbeb;
    border-left: 4px solid #d97706;
    color: #92400e;
  }

  .callout-caution {
    background: #fef2f2;
    border-left: 4px solid #dc2626;
    color: #991b1b;
  }

  .callout-title {
    font-weight: 700;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  /* CODE BLOCKS */
  pre {
    background: #0f172a;
    color: #e2e8f0;
    padding: 12px 14px;
    border-radius: 6px;
    font-family: Consolas, "Courier New", monospace;
    font-size: 8.5pt;
    line-height: 1.4;
    overflow-x: auto;
    margin: 12px 0;
    page-break-inside: avoid;
  }

  code {
    font-family: Consolas, "Courier New", monospace;
    background: #f1f5f9;
    color: #0f4c3a;
    padding: 2px 4px;
    border-radius: 3px;
    font-size: 9pt;
  }

  pre code {
    background: transparent;
    color: inherit;
    padding: 0;
  }

  /* DIAGRAM WRAPPER */
  .diagram-box {
    margin: 16px 0;
    text-align: center;
    page-break-inside: avoid;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 14px;
  }

  .diagram-caption {
    font-size: 8.5pt;
    color: #64748b;
    font-style: italic;
    margin-top: 8px;
  }

  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover-page">
  <div class="cover-badge">Modul Panduan Praktikum & Ujian Workshop (Durasi 2 Jam)</div>
  
  <div class="cover-title-group">
    <h1 class="cover-title">Pemanfaatan Ekosistem Multi-AI dalam Pembuatan WebGIS Sebaran Tematik</h1>
    <div class="cover-subtitle">
      Alur Kerja Komprehensif: AI Web Scraping, Validasi Spasial Anti-Halusinasi, Prototyping UI, Agentic Coding Antigravity, hingga Hosting Gratis di GitHub Pages
    </div>
  </div>

  <div class="cover-illustration">
    <!-- SVG ILLUSTRATION: 3-PILLAR ECOSYSTEM -->
    <svg width="600" height="150" viewBox="0 0 600 150" xmlns="http://www.w3.org/2000/svg">
      <!-- Step 1: ChatGPT -->
      <rect x="10" y="25" width="125" height="100" rx="8" fill="#10a37f" opacity="0.9" />
      <text x="72" y="55" fill="#ffffff" font-weight="bold" font-size="12" text-anchor="middle">1. ChatGPT</text>
      <text x="72" y="75" fill="#ffffff" font-size="9" text-anchor="middle">Scraping Data &</text>
      <text x="72" y="90" fill="#ffffff" font-size="9" text-anchor="middle">Prompt Engineering</text>
      <text x="72" y="110" fill="#e6fffa" font-size="8" text-anchor="middle">(The Brain)</text>

      <!-- Arrow 1 -->
      <path d="M 140 75 L 165 75" stroke="#d97706" stroke-width="3" fill="none" marker-end="url(#arrow)" />
      
      <!-- Step 2: Google AI Studio -->
      <rect x="170" y="25" width="125" height="100" rx="8" fill="#1a73e8" opacity="0.9" />
      <text x="232" y="55" fill="#ffffff" font-weight="bold" font-size="12" text-anchor="middle">2. AI Studio</text>
      <text x="232" y="75" fill="#ffffff" font-size="9" text-anchor="middle">UI Prototyping &</text>
      <text x="232" y="90" fill="#ffffff" font-size="9" text-anchor="middle">Mobile Layout</text>
      <text x="232" y="110" fill="#e8f0fe" font-size="8" text-anchor="middle">(The Designer)</text>

      <!-- Arrow 2 -->
      <path d="M 300 75 L 325 75" stroke="#d97706" stroke-width="3" fill="none" />

      <!-- Step 3: Google Antigravity -->
      <rect x="330" y="25" width="125" height="100" rx="8" fill="#0f4c3a" />
      <text x="392" y="55" fill="#fde68a" font-weight="bold" font-size="12" text-anchor="middle">3. Antigravity</text>
      <text x="392" y="75" fill="#ffffff" font-size="9" text-anchor="middle">Agentic Coding &</text>
      <text x="392" y="90" fill="#ffffff" font-size="9" text-anchor="middle">Git Automation</text>
      <text x="392" y="110" fill="#fef08a" font-size="8" text-anchor="middle">(The Engineer)</text>

      <!-- Arrow 3 -->
      <path d="M 460 75 L 485 75" stroke="#d97706" stroke-width="3" fill="none" />

      <!-- Step 4: GitHub Pages -->
      <rect x="490" y="25" width="100" height="100" rx="8" fill="#24292e" />
      <text x="540" y="55" fill="#ffffff" font-weight="bold" font-size="11" text-anchor="middle">4. GitHub</text>
      <text x="540" y="75" fill="#ffffff" font-size="9" text-anchor="middle">Hosting Gratis &</text>
      <text x="540" y="90" fill="#ffffff" font-size="9" text-anchor="middle">Auto Deployment</text>
      <text x="540" y="110" fill="#4ade80" font-size="8" text-anchor="middle">(Live WebGIS)</text>
    </svg>
  </div>

  <div class="cover-meta">
    <div>
      <strong>Sasaran Peserta:</strong> Mahasiswa, Peneliti, Praktisi GIS, & Dosen<br>
      <strong>Durasi Pelatihan:</strong> 2 Jam (120 Menit Intensif Hands-on)<br>
      <strong>Studi Kasus:</strong> WebGIS Atlas Sejarah Kerajaan Islam Nusantara
    </div>
    <div>
      <strong>Penyusun Modul:</strong> Senior GIS & Agentic AI Specialist<br>
      <strong>Lingkungan Pengembangan:</strong> Leaflet.js, CRS WGS84, GitHub Pages<br>
      <strong>Edisi Modul:</strong> 2026 Ready
    </div>
  </div>
</div>

<!-- SECTION 1 -->
<h1>1. Latar Belakang & Paradigma Baru Pengembangan GIS</h1>
<p>
  Secara konvensional, pembuatan aplikasi WebGIS memerlukan penguasaan mendalam di berbagai bidang: kartografi geodesi, struktur data geospasial (GeoJSON, WGS84), pemrograman frontend web (HTML/CSS/JS), library peta Leaflet, serta administrasi server. Akibatnya, kurva pembelajaran pembuatan WebGIS menjadi sangat terjal bagi pemula.
</p>
<p>
  Hadirnya era <strong>Agentic AI (AI Otonom)</strong> dan <strong>Generative AI Multimodal</strong> mengubah paradigma ini. Pengembang kini tidak lagi harus mengetik ratusan baris kode JavaScript secara manual, melainkan bertindak sebagai <strong>Arsitek Sistem (System Architect)</strong> dan <strong>Kurator Kualitas Data (Quality Assurer)</strong>. AI mengambil alih pekerjaan repetitif penulisan skrip dan perbaikan bug, sementara manusia memegang kendali atas validitas data, metodologi keilmuan, dan logika spasial.
</p>

<!-- SECTION 2 -->
<h1>2. Rundown Workshop Intensif 2 Jam (120 Menit)</h1>
<p>
  Pelatihan ini dirancang dengan metode <em>Action Learning</em> di mana peserta langsung menghasilkan karya WebGIS sebaran yang live di internet pada akhir sesi:
</p>

<table>
  <thead>
    <tr>
      <th style="width: 15%;">Waktu</th>
      <th style="width: 12%;">Durasi</th>
      <th style="width: 43%;">Materi & Aktivitas Hands-On</th>
      <th style="width: 30%;">Output Peserta</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>00:00 - 00:15</strong></td>
      <td>15 menit</td>
      <td><strong>Pengantar & Paradigma 3 Pilar AI:</strong> Konsep WebGIS spasial temporal, peran ChatGPT, Google AI Studio, dan Antigravity.</td>
      <td>Pemahaman alur kerja modern</td>
    </tr>
    <tr>
      <td><strong>00:15 - 00:40</strong></td>
      <td>25 menit</td>
      <td><strong>Sesi 1 — AI Web Scraping & Ekstraksi Data:</strong> Mengambil tabel data dari web/Wikipedia dan mengubahnya menjadi format JSON/GeoJSON.</td>
      <td>Dataset mentah terstruktur</td>
    </tr>
    <tr>
      <td><strong>00:40 - 01:00</strong></td>
      <td>20 menit</td>
      <td><strong>Sesi 2 — Validasi Koordinat & Anti-Halusinasi:</strong> Verifikasi koordinat (anti Lat/Lng flip), penetapan tingkat keyakinan, dan penyiapan dataset ujian mandiri.</td>
      <td>Dataset bersih & terverifikasi</td>
    </tr>
    <tr>
      <td><strong>01:00 - 01:35</strong></td>
      <td>35 menit</td>
      <td><strong>Sesi 3 — Agentic Coding di Antigravity:</strong> Merakit Leaflet WebGIS, drawer informasi, thumbnail foto, filter kategori, dan responsive mobile.</td>
      <td>Aplikasi WebGIS aktif di server lokal</td>
    </tr>
    <tr>
      <td><strong>01:35 - 01:50</strong></td>
      <td>15 menit</td>
      <td><strong>Sesi 4 — Otomasi Publikasi ke GitHub Pages:</strong> Perintah Git otomatis via AI dan peluncuran URL website publik gratis.</td>
      <td>WebGIS tayang secara online</td>
    </tr>
    <tr>
      <td><strong>01:50 - 02:00</strong></td>
      <td>10 menit</td>
      <td><strong>Evaluasi Ujian & Penutupan:</strong> Uji buka WebGIS di smartphone masing-masing peserta dan review hasil ujian.</td>
      <td>Penilaian proyek mandiri</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<!-- SECTION 3 -->
<h1>3. Fase 1: AI Web Scraping & Ekstraksi Data Spasial</h1>
<p>
  Banyak informasi geospasial tematik (situs bersejarah, cagar budaya, fasilitas kesehatan, atau potensi wisata) tersebar dalam bentuk artikel narasi, tabel HTML Wikipedia, atau dokumen berita yang tidak menyediakan tombol ekspor data spasial.
</p>

<h3>A. Metode Parsing Cepat Menggunakan AI (Tanpa Koding)</h3>
<p>
  Peserta dapat menyalin teks atau tabel dari peramban web, lalu memberikan prompt terstruktur kepada ChatGPT atau Google Gemini:
</p>

<pre><code>"Bertindaklah sebagai Data Extraction Specialist. 
Berikut adalah teks daftar objek peninggalan bersejarah yang saya salin dari internet:
[TEMPELKAN TEKS / TABEL DARI SITUS WEB DI SINI]

Tugasmu:
1. Ekstrak entitas tersebut ke dalam format JSON array yang rapi.
2. Setiap objek wajib memiliki atribut: id, nama_objek, tipe_kategori, tahun_pembangunan, kota_kabupaten, latitude, longitude, deskripsi_ringkas, sumber_referensi.
3. Estimasi koordinat latitude dan longitude (CRS WGS84) titik fisik objek tersebut.
4. Pastikan koordinat berada di wilayah Indonesia (Latitude antara 6 LU s/d 11 LS, Longitude antara 95 BT s/d 141 BT)."</code></pre>

<h3>B. Metode Otomasi Python Scraping (Untuk Halaman Berulang)</h3>
<p>
  Untuk data yang memiliki ratusan baris, AI dapat diminta membuatkan skrip Python ringan menggunakan pustaka <code>BeautifulSoup</code> dan <code>requests</code>:
</p>

<pre><code>import requests
from bs4 import BeautifulSoup
import json

url = "https://id.wikipedia.org/wiki/Daftar_cagar_budaya_di_Indonesia"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Logika ekstraksi baris tabel tr/td dipandu oleh AI untuk ekspor ke data.json</code></pre>

<!-- SECTION 4 -->
<h1>4. Fase 2: Koreksi & Pemeriksaan Keakuratan Data (Anti-Hallucination)</h1>

<div class="callout callout-caution">
  <div class="callout-title">⚠️ PERINGATAN KRITIS TENTANG HALUSINASI AI DALAM GIS</div>
  Model AI generatif dapat mengarang nilai desimal koordinat jika tidak memiliki data spasial primer. Peserta workshop <strong>wajib</strong> memverifikasi data sebelum diintegrasikan ke WebGIS.
</div>

<div class="diagram-box">
  <!-- SVG DIAGRAM: 4-STEP VERIFICATION -->
  <svg width="550" height="90" viewBox="0 0 550 90" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="15" width="120" height="60" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" />
    <text x="70" y="42" fill="#0369a1" font-size="9" font-weight="bold" text-anchor="middle">1. Cek Lat/Lng Flip</text>
    <text x="70" y="58" fill="#0284c7" font-size="8" text-anchor="middle">(Lintang vs Bujur)</text>

    <path d="M 130 45 L 145 45" stroke="#64748b" stroke-width="2" />

    <rect x="145" y="15" width="120" height="60" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2" />
    <text x="205" y="42" fill="#92400e" font-size="9" font-weight="bold" text-anchor="middle">2. Validasi Satelit</text>
    <text x="205" y="58" fill="#b45309" font-size="8" text-anchor="middle">(Cek Google Maps / OSM)</text>

    <path d="M 265 45 L 280 45" stroke="#64748b" stroke-width="2" />

    <rect x="280" y="15" width="120" height="60" rx="6" fill="#f3e8ff" stroke="#7c3aed" stroke-width="2" />
    <text x="340" y="42" fill="#6b21a8" font-size="9" font-weight="bold" text-anchor="middle">3. Validasi Kronologi</text>
    <text x="340" y="58" fill="#7c3aed" font-size="8" text-anchor="middle">(Tahun Logis & Sumber)</text>

    <path d="M 400 45 L 415 45" stroke="#64748b" stroke-width="2" />

    <rect x="415" y="15" width="125" height="60" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2" />
    <text x="477" y="42" fill="#15803d" font-size="9" font-weight="bold" text-anchor="middle">4. Confidence Level</text>
    <text x="477" y="58" fill="#16a34a" font-size="8" text-anchor="middle">(Tinggi / Interpretatif)</text>
  </svg>
  <div class="diagram-caption">Gambar 1: Alur 4 Tahap Verifikasi Keakuratan Data Geospasial</div>
</div>

<ol>
  <li>
    <strong>Antisipasi Lat/Lng Inversion (Tertukar Lintang dan Bujur):</strong><br>
    Kesalahan paling jamak pemula: menaruh nilai bujur (misal: 110.36) pada kolom latitude dan nilai lintang (-7.80) pada longitude. Akibatnya, titik peta terlempar ke Samudera Hindia atau kutub.
  </li>
  <li>
    <strong>Verifikasi Toponimi Kuno vs Modern:</strong><br>
    Nama tempat bersejarah seringkali berbeda dengan batas administratif modern. Pastikan koordinat mengarah langsung pada tapak fisik cagar budaya, bukan sekadar kantor kecamatan setempat.
  </li>
  <li>
    <strong>Klasifikasi Tingkat Keyakinan (Confidence Level):</strong>
    <ul>
      <li><code>Tinggi</code>: Objek memiliki bukti fisik cagar budaya nasional, terdaftar di Kemendikbudristek/BPCB, dan koordinat diverifikasi GPS/satelit.</li>
      <li><code>Sedang / Interpretatif</code>: Objek bersumber dari teks naskah kuno/babad di mana sisa fondasi fisik belum ditemukan secara utuh.</li>
    </ul>
  </li>
</ol>

<div class="page-break"></div>

<!-- SECTION 5 -->
<h1>5. Fase 3: Panduan Melampirkan Dataset Mandiri Peserta (Untuk Ujian)</h1>
<p>
  Untuk menguji kompetensi mandiri, setiap peserta diwajibkan menyiapkan data tematik mereka sendiri (misal: sebaran kuliner khas, cagar budaya kota asal, puskesmas, atau titik rawan bencana).
</p>

<h3>Format Template Spreadsheet (Excel / CSV) Ujian Peserta:</h3>
<table>
  <thead>
    <tr>
      <th>id</th>
      <th>nama_objek</th>
      <th>kategori</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>tahun_awal</th>
      <th>tahun_akhir</th>
      <th>foto_url</th>
      <th>sumber_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>obj-01</code></td>
      <td>Masjid Agung Demak</td>
      <td>ibadah</td>
      <td>-6.8946</td>
      <td>110.6373</td>
      <td>1479</td>
      <td>9999</td>
      <td>https://...jpg</td>
      <td>BPCB Jawa Tengah</td>
    </tr>
    <tr>
      <td><code>obj-02</code></td>
      <td>Benteng Somba Opu</td>
      <td>benteng</td>
      <td>-5.1897</td>
      <td>119.3982</td>
      <td>1525</td>
      <td>1669</td>
      <td>https://...jpg</td>
      <td>Balai Cagar Budaya Sulsel</td>
    </tr>
  </tbody>
</table>

<h3>Cara Integrasi File Peserta Melalui Antigravity:</h3>
<p>
  Peserta cukup menyimpan file spreadsheet tersebut sebagai <code>data/dataset_mandiri.csv</code> di dalam workspace proyek, lalu mengirimkan perintah ke Antigravity:
</p>
<pre><code>"Saya sudah melampirkan file data mandiri saya di data/dataset_mandiri.csv.
Tolong baca file tersebut, verifikasi integritas koordinatnya, konversikan menjadi file data/sites.json berstandar WGS84, dan hubungkan ke dalam WebGIS Leaflet kita lengkap dengan penanda kustom dan popup foto."</code></pre>

<!-- SECTION 6 -->
<h1>6. Fase 4: Prototyping UI Cepat di Google AI Studio</h1>
<p>
  Sebelum menginstruksikan Antigravity melakukan coding, peserta menggunakan <strong>Google AI Studio</strong> untuk merancang identitas visual yang profesional:
</p>
<ul>
  <li><strong>Eksplorasi Skema Warna Tematik:</strong> Hijau zamrud (<code>#0f4c3a</code>) dan aksen emas (<code>#d97706</code>) untuk sejarah Islam; Biru bahari untuk data maritim/perikanan.</li>
  <li><strong>Desain Mobile-First:</strong> Menginstruksikan AI Studio untuk merancang <em>Bottom Sheet</em> interaktif dan kartu detail foto agar tidak memakan ruang pandang peta di layar handphone (viewport 360px).</li>
</ul>

<!-- SECTION 7 -->
<h1>7. Fase 5: Eksekusi Kode Otonom di Google Antigravity & Debugging</h1>
<p>
  Antigravity bertindak sebagai rekan <em>pair programming</em> otonom yang bekerja langsung di dalam komputer peserta:
</p>
<ol>
  <li><strong>Membaca Basis Kode Proyek:</strong> Antigravity membaca seluruh file di workspace secara kontekstual.</li>
  <li><strong>Penyusunan Modul Modular:</strong> Membagi kode menjadi modul terpisah: <code>map.js</code> (manajemen Leaflet), <code>timeline.js</code> (slider temporal), dan <code>detail.js</code> (panel drawer).</li>
  <li><strong>Optimasi Performa Gambar (Anti-Lag):</strong> Menerapkan <code>loading="lazy"</code> pada foto agar WebGIS tetap ringan dan cepat saat diakses di perangkat seluler.</li>
  <li><strong>Penyempurnaan Bug Responsif:</strong> Memperbaiki konflik tata letak (misal tombol zoom yang tertutup panel bawah) secara instan.</li>
</ol>

<!-- SECTION 8 -->
<h1>8. Fase 6: Otomasi Publikasi & Hosting Gratis di GitHub Pages</h1>
<p>
  Peserta tidak perlu menginstal Git GUI atau mengetik perintah terminal rumit. Cukup minta Antigravity:
</p>
<pre><code>"Tolong push semua perubahan kode dan data terbaru ke repositori GitHub saya di branch main."</code></pre>

<h3>Langkah Aktivasi GitHub Pages (Sekali Klik):</h3>
<ol>
  <li>Buka repositori GitHub Anda di web browser.</li>
  <li>Masuk ke menu <strong>Settings</strong> &rarr; pilih bilah <strong>Pages</strong>.</li>
  <li>Pada opsi <em>Branch</em>, pilih <code>main</code> dan folder <code>/ (root)</code> &rarr; Klik <strong>Save</strong>.</li>
  <li>Dalam 1–2 menit, WebGIS Anda resmi mengudara secara global di: <code>https://username.github.io/nama-repo/</code>.</li>
</ol>

<div class="callout callout-tip">
  <div class="callout-title">💡 KEUNGGULAN SINKRONISASI OTOMATIS</div>
  Setiap kali peserta meminta Antigravity menambah data baru atau memperbaiki fitur, Antigravity akan otomatis melakukan commit dan push. Website online peserta akan ter-update secara otomatis tanpa perlu deployment manual!
</div>

<!-- SECTION 9 -->
<h1>9. Rekomendasi Alat AI Lain & Ekosistem Google</h1>
<p>
  Bagi pengguna yang memiliki langganan <strong>Google One AI Premium (Gemini Advanced/Pro)</strong>, fitur-fitur berikut dapat dimanfaatkan secara maksimal:
</p>
<ul>
  <li>
    <strong>Gemini di Google Docs (Help Me Write):</strong> Salin teks panduan ini ke Google Docs. Gunakan fitur <em>"Help me write"</em> untuk memformat modul, membuat ringkasan, dan memanfaatkan <em>"Insert &rarr; Image &rarr; Help me create an image"</em> (Imagen 3) untuk menghasilkan ilustrasi kustom. Unduh langsung dalam format <code>.docx</code> atau <code>.pdf</code>.
  </li>
  <li>
    <strong>Google NotebookLM (100% Gratis berbasis Gemini 1.5 Pro):</strong> Unggah file Markdown modul ini ke NotebookLM. AI akan otomatis membuatkan lembar tanya jawab (FAQ), panduan belajar (*Study Guide*), bahkan ringkasan podcast audio untuk peserta workshop.
  </li>
  <li>
    <strong>Gamma.app (AI Pembuat Dokumen & Presentasi):</strong> Cukup tempelkan teks Markdown modul ini ke Gamma.app. AI akan menyusunnya menjadi dokumen PDF atau slide presentasi interaktif lengkap dengan kartu visual otomatis.
  </li>
</ul>

<hr style="border: none; border-top: 1px solid #cbd5e1; margin: 30px 0;">
<p style="font-size: 8.5pt; color: #64748b; text-align: center;">
  Modul ini diproduksi untuk Pelatihan & Workshop Intensif WebGIS Spasial Berbasis AI. Hak Cipta Terbuka untuk Tujuan Pembelajaran Akademik (2026).
</p>

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML Template generated successfully: {HTML_PATH}")

# ==============================================================================
# 2. CONVERT HTML TO PROFESSIONAL PDF VIA HEADLESS MICROSOFT EDGE
# ==============================================================================
print("Rendering PDF via headless Microsoft Edge...")
cmd_pdf = [
    EDGE_EXE,
    "--headless",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={PDF_PATH}",
    HTML_PATH
]

res = subprocess.run(cmd_pdf, capture_output=True, text=True)
if os.path.exists(PDF_PATH) and os.path.getsize(PDF_PATH) > 0:
    print(f"PDF successfully created: {PDF_PATH} ({os.path.getsize(PDF_PATH):,} bytes)")
else:
    print(f"Failed to generate PDF. Output: {res.stderr}")

# ==============================================================================
# 3. GENERATE FORMATTED MICROSOFT WORD (.DOCX) USING PYTHON-DOCX
# ==============================================================================
print("Generating Microsoft Word (.docx) document...")
doc = docx.Document()

# Page Margins
sections = doc.sections
for section in sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

# Styles
COLOR_PRIMARY = RGBColor(15, 76, 58)    # #0f4c3a Emerald
COLOR_SECONDARY = RGBColor(217, 119, 6) # #d97706 Gold
COLOR_TEXT = RGBColor(30, 41, 59)       # #1e293b Slate Dark

# Title
p_title = doc.add_paragraph()
run_badge = p_title.add_run("MODUL PRAKTIKUM & PANDUAN WORKSHOP INTENSIF (2 JAM)\n")
run_badge.font.name = "Arial"
run_badge.font.size = Pt(10)
run_badge.font.bold = True
run_badge.font.color.rgb = COLOR_SECONDARY

run_title = p_title.add_run("Pemanfaatan Ekosistem Multi-AI dalam Pembuatan WebGIS Sebaran Tematik")
run_title.font.name = "Arial"
run_title.font.size = Pt(22)
run_title.font.bold = True
run_title.font.color.rgb = COLOR_PRIMARY

p_sub = doc.add_paragraph()
run_sub = p_sub.add_run("Alur Kerja Komprehensif: Scraping Data Spasial, Validasi Anti-Halusinasi, Prototyping UI, Agentic Coding Antigravity, hingga Hosting Gratis di GitHub Pages")
run_sub.font.name = "Arial"
run_sub.font.size = Pt(12)
run_sub.font.italic = True
run_sub.font.color.rgb = RGBColor(71, 85, 105)

# Meta Box Table
tbl_meta = doc.add_table(rows=2, cols=2)
tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_meta.rows[0].cells[0].text = "Sasaran: Mahasiswa, Peneliti, & Pengembang GIS"
tbl_meta.rows[0].cells[1].text = "Durasi: 2 Jam (120 Menit Hands-On)"
tbl_meta.rows[1].cells[0].text = "Studi Kasus: WebGIS Sejarah Islam Nusantara"
tbl_meta.rows[1].cells[1].text = "Teknologi: Leaflet.js, CRS WGS84, GitHub Pages"

doc.add_paragraph() # Spacer

# Heading 1
def add_h1(text):
    h = doc.add_heading(text, level=1)
    for r in h.runs:
        r.font.name = "Arial"
        r.font.size = Pt(15)
        r.font.bold = True
        r.font.color.rgb = COLOR_PRIMARY
    return h

def add_h2(text):
    h = doc.add_heading(text, level=2)
    for r in h.runs:
        r.font.name = "Arial"
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(26, 93, 72)
    return h

def add_p(text, bold_prefix=""):
    p = doc.add_paragraph()
    if bold_prefix:
        r_b = p.add_run(bold_prefix + " ")
        r_b.bold = True
        r_b.font.color.rgb = COLOR_PRIMARY
    p.add_run(text)
    p.paragraph_format.line_spacing = 1.25
    return p

# Section 1
add_h1("1. Latar Belakang & Paradigma Baru Pengembangan GIS")
add_p("Pembuatan WebGIS tematik konvensional membutuhkan keterampilan multidisiplin: kartografi, format data spasial GeoJSON, HTML/CSS, Leaflet JS, dan server web. Kehadiran Generative AI dan Agentic AI Coding mengubah paradigma ini: pengembang kini bertindak sebagai Arsitek Sistem dan Kurator Kualitas Data, sementara AI mengotomasi penulisan kode dan perbaikan bug.")

# Section 2
add_h1("2. Rundown Workshop Intensif 2 Jam (120 Menit)")
add_p("Jadwal disusun presisi untuk memastikan seluruh peserta dapat menyelesaikan proyek WebGIS dan mempublikasikannya:")

tbl_sched = doc.add_table(rows=6, cols=3)
tbl_sched.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Waktu & Durasi", "Materi & Aktivitas", "Output Peserta"]
for i, h in enumerate(headers):
    cell = tbl_sched.rows[0].cells[i]
    cell.text = h
    cell.paragraphs[0].runs[0].font.bold = True
    cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    # Shading header cell
    shd = parse_xml(r'<w:shd {} w:fill="0F4C3A"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shd)

sched_data = [
    ("00:00 - 00:15 (15 mnt)", "Pengantar & Paradigma 3 Pilar AI (ChatGPT, AI Studio, Antigravity)", "Pemahaman alur kerja modern"),
    ("00:15 - 00:40 (25 mnt)", "Sesi 1: AI Web Scraping & Ekstraksi Data Spasial dari Web", "Dataset mentah terstruktur"),
    ("00:40 - 01:00 (20 mnt)", "Sesi 2: Validasi Koordinat, Anti-Halusinasi & Dataset Mandiri", "Dataset bersih & terverifikasi"),
    ("01:00 - 01:35 (35 mnt)", "Sesi 3: Hands-on Coding di Antigravity (Leaflet WebGIS & Mobile)", "WebGIS aktif di server lokal"),
    ("01:35 - 01:50 (15 mnt)", "Sesi 4: Otomasi Publikasi & Hosting Gratis di GitHub Pages", "WebGIS online dapat diakses via HP"),
]

for row_idx, data in enumerate(sched_data):
    for col_idx, text in enumerate(data):
        tbl_sched.rows[row_idx + 1].cells[col_idx].text = text

doc.add_paragraph()

# Section 3
add_h1("3. Fase 1: AI Web Scraping & Ekstraksi Data Spasial")
add_p("Peserta diajarkan teknik mengekstrak data dari artikel web/Wikipedia menggunakan metode prompt parsing ke JSON/GeoJSON WGS84, atau skrip Python ringan menggunakan BeautifulSoup.")

# Section 4
add_h1("4. Fase 2: Koreksi & Pemeriksaan Keakuratan Data (Anti-Hallucination)")
add_p("Pemeriksaan wajib meliputi pencegahan Lat/Lng Inversion (tertukar lintang dan bujur), verifikasi toponimi fisik cagar budaya melalui citra satelit/OpenStreetMap, serta penentuan Confidence Level (Tinggi vs Interpretatif).")

# Section 5
add_h1("5. Fase 3: Panduan Melampirkan Dataset Mandiri Peserta (Ujian Praktikum)")
add_p("Peserta menyusun spreadsheet CSV mandiri dengan kolom: id, nama_objek, kategori, latitude, longitude, tahun_awal, tahun_akhir, foto_url, sumber_data. File disimpan di data/dataset_mandiri.csv dan dikonversi otomatis oleh Antigravity ke layer Leaflet.")

# Section 6
add_h1("6. Fase 4 & 5: Prototyping UI & Agentic Coding Antigravity")
add_p("Eksplorasi palet warna dan komponen responsif dilakukan di Google AI Studio. Hasilnya diintegrasikan ke Google Antigravity yang secara otonom merakit kode JavaScript, penanda custom, popup lazy-loaded image, dan bottom sheet.")

# Section 7
add_h1("7. Fase 6: Otomasi Publikasi ke GitHub Pages")
add_p("Peserta menginstruksikan Antigravity untuk menjalankan perintah git push secara otonom. GitHub Pages diaktifkan pada branch main untuk menerbitkan WebGIS secara live dan gratis.")

# Section 8
add_h1("8. Integrasi Ekosistem Google (Google One AI Premium / Gemini Pro)")
add_p("Bagi pengguna langganan Google Pro: dokumen ini dapat disalin ke Google Docs untuk diformat dengan Gemini ('Help me write'), ditambahkan ilustrasi otomatis dengan Imagen 3, dan dianalisis menggunakan Google NotebookLM untuk menghasilkan ringkasan panduan studi dan audio FAQ otomatis.")

doc.save(DOCX_PATH)
print(f"Word Document successfully created: {DOCX_PATH} ({os.path.getsize(DOCX_PATH):,} bytes)")
print("ALL DOCUMENTS GENERATED SUCCESSFULLY!")
