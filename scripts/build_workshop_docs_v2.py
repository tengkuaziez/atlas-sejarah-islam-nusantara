import os
import subprocess
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))
HTML_PATH = os.path.join(DOCS_DIR, "MODUL_PANDUAN_WORKSHOP_WEBGIS.html")
PDF_PATH = os.path.join(DOCS_DIR, "MODUL_PANDUAN_WORKSHOP_WEBGIS.pdf")
DOCX_PATH = os.path.join(DOCS_DIR, "MODUL_PANDUAN_WORKSHOP_WEBGIS.docx")
MD_PATH = os.path.join(DOCS_DIR, "PANDUAN_WORKSHOP_AI_WEBGIS.md")
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

print(f"Generating Comprehensive Module in: {DOCS_DIR}")

# ==============================================================================
# HTML CONTENT BUILDER WITH PROFESSIONAL SVGs & EXPANDED DETAIL
# ==============================================================================
html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Modul Pelatihan: Pengembangan WebGIS Tematik Menggunakan Ekosistem AI</title>
<style>
  @page {
    size: A4 portrait;
    margin: 18mm 16mm 20mm 16mm;
    @bottom-center {
      content: "Modul Praktikum WebGIS Spasial Berbasis AI — Halaman " counter(page);
      font-size: 8pt;
      color: #64748b;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    }
  }

  * { box-sizing: border-box; }
  
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 9.5pt;
    line-height: 1.6;
    color: #1e293b;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }

  /* COVER PAGE */
  .cover-page {
    page-break-after: always;
    min-height: 94vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 36px 28px;
    border: 3px solid #0f4c3a;
    border-radius: 8px;
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
    position: relative;
  }

  .cover-header {
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .inst-name {
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 1px;
    color: #475569;
    text-transform: uppercase;
  }

  .cover-badge {
    align-self: flex-start;
    background: #0f4c3a;
    color: #fde68a;
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 4px;
    border-left: 4px solid #d97706;
    margin-top: 15px;
  }

  .cover-title-group {
    margin-top: 25px;
  }

  .cover-title {
    font-size: 24pt;
    font-weight: 800;
    color: #0f4c3a;
    line-height: 1.25;
    margin: 0 0 16px 0;
  }

  .cover-subtitle {
    font-size: 11.5pt;
    color: #475569;
    line-height: 1.5;
    margin-bottom: 20px;
    border-left: 4px solid #d97706;
    padding-left: 14px;
    text-align: justify;
  }

  .cover-meta {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 16px 20px;
    font-size: 9pt;
    color: #334155;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }

  .cover-meta strong {
    color: #0f4c3a;
  }

  /* HEADINGS */
  h1, h2, h3, h4 {
    color: #0f4c3a;
    font-weight: 700;
    page-break-after: avoid;
  }

  h1 {
    font-size: 15pt;
    border-bottom: 2px solid #0f4c3a;
    padding-bottom: 6px;
    margin-top: 28px;
    margin-bottom: 12px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  h2 {
    font-size: 12pt;
    color: #1a5d48;
    margin-top: 20px;
    margin-bottom: 8px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
  }

  h3 {
    font-size: 10.5pt;
    color: #334155;
    margin-top: 14px;
    margin-bottom: 6px;
  }

  p {
    margin: 0 0 10px 0;
    text-align: justify;
  }

  ul, ol {
    margin: 0 0 12px 0;
    padding-left: 20px;
  }

  li {
    margin-bottom: 5px;
    text-align: justify;
  }

  /* TABLES */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 7px 9px;
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
    font-size: 9pt;
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
    font-size: 8pt;
    line-height: 1.45;
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
    font-size: 8.5pt;
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
    font-size: 8pt;
    color: #64748b;
    font-style: italic;
    margin-top: 8px;
    text-align: center;
  }

  .page-break {
    page-break-before: always;
  }

  .rubric-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin: 12px 0;
  }
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover-page">
  <div class="cover-header">
    <span class="inst-name">Modul Pembelajaran Praktikum Laboratorium Sistem Informasi Geospasial</span>
    <span style="font-size:8pt; color:#64748b; font-weight:600;">Edisi Standar 2026</span>
  </div>

  <div class="cover-badge">Modul Pelatihan & Pedoman Praktikum Mandiri (120 Menit)</div>
  
  <div class="cover-title-group">
    <h1 class="cover-title">Pengembangan Sistem Informasi Geografis Berbasis Web (WebGIS) Tematik Menggunakan Ekosistem Artificial Intelligence</h1>
    <div class="cover-subtitle">
      Panduan Lengkap Alur Kerja: Ekstraksi Data Spasial Otomatis (AI Web Scraping), Protokol Validasi Geodesi Anti-Halusinasi, Perancangan Antarmuka Responsif Seluler, Pemrograman Otonom (Agentic Pair-Programming), hingga Publikasi Terbuka di GitHub Pages.
    </div>
  </div>

  <div style="text-align: center; margin: 15px 0;">
    <!-- SVG ILLUSTRATION 1: ARSITEKTUR EKOSISTEM 3 PILAR AI -->
    <svg width="600" height="135" viewBox="0 0 600 135" xmlns="http://www.w3.org/2000/svg">
      <!-- Step 1: ChatGPT -->
      <rect x="10" y="18" width="125" height="95" rx="8" fill="#10a37f" />
      <text x="72" y="45" fill="#ffffff" font-weight="bold" font-size="11" text-anchor="middle">1. THE BRAIN</text>
      <text x="72" y="65" fill="#ffffff" font-size="8.5" text-anchor="middle">ChatGPT / Perplexity</text>
      <text x="72" y="80" fill="#e6fffa" font-size="8" text-anchor="middle">Scraping & Skema Data</text>
      <text x="72" y="95" fill="#e6fffa" font-size="7.5" text-anchor="middle">Prompt Engineering</text>

      <!-- Arrow 1 -->
      <path d="M 140 65 L 165 65" stroke="#d97706" stroke-width="2.5" fill="none" marker-end="url(#arrow)" />
      
      <!-- Step 2: Google AI Studio -->
      <rect x="170" y="18" width="125" height="95" rx="8" fill="#1a73e8" />
      <text x="232" y="45" fill="#ffffff" font-weight="bold" font-size="11" text-anchor="middle">2. THE DESIGNER</text>
      <text x="232" y="65" fill="#ffffff" font-size="8.5" text-anchor="middle">Google AI Studio</text>
      <text x="232" y="80" fill="#e8f0fe" font-size="8" text-anchor="middle">Prototyping UI/UX</text>
      <text x="232" y="95" fill="#e8f0fe" font-size="7.5" text-anchor="middle">Mobile Layout & Cards</text>

      <!-- Arrow 2 -->
      <path d="M 300 65 L 325 65" stroke="#d97706" stroke-width="2.5" fill="none" />

      <!-- Step 3: Google Antigravity -->
      <rect x="330" y="18" width="125" height="95" rx="8" fill="#0f4c3a" />
      <text x="392" y="45" fill="#fde68a" font-weight="bold" font-size="11" text-anchor="middle">3. THE ENGINEER</text>
      <text x="392" y="65" fill="#ffffff" font-size="8.5" text-anchor="middle">Agentic Coding</text>
      <text x="392" y="80" fill="#fef08a" font-size="8" text-anchor="middle">Leaflet Engine & Test</text>
      <text x="392" y="95" fill="#fef08a" font-size="7.5" text-anchor="middle">Git Push Otomatis</text>

      <!-- Arrow 3 -->
      <path d="M 460 65 L 485 65" stroke="#d97706" stroke-width="2.5" fill="none" />

      <!-- Step 4: GitHub Pages -->
      <rect x="490" y="18" width="100" height="95" rx="8" fill="#1e293b" />
      <text x="540" y="45" fill="#ffffff" font-weight="bold" font-size="11" text-anchor="middle">4. DEPLOY</text>
      <text x="540" y="65" fill="#4ade80" font-size="8.5" text-anchor="middle">GitHub Pages</text>
      <text x="540" y="80" fill="#ffffff" font-size="8" text-anchor="middle">Hosting Publik</text>
      <text x="540" y="95" fill="#94a3b8" font-size="7.5" text-anchor="middle">Live Website</text>
    </svg>
  </div>

  <div class="cover-meta">
    <div>
      <strong>Sasaran Pembaca:</strong> Mahasiswa, Peneliti, Asisten GIS, & Praktisi Data<br>
      <strong>Durasi Pelatihan:</strong> 2 Jam (120 Menit Intensif Hands-On)<br>
      <strong>Sifat Pembelajaran:</strong> Teori Praktis & Laboratorium Mandiri
    </div>
    <div>
      <strong>Prasyarat Teknis:</strong> Koneksi Internet, Akun GitHub, Web Browser Modern<br>
      <strong>Perangkat Lunak:</strong> Leaflet.js, CRS WGS84, Agentic AI Environment<br>
      <strong>Studi Kasus Rujukan:</strong> Atlas Spasial Sejarah Nusantara
    </div>
  </div>
</div>

<!-- BAGIAN I: PENDAHULUAN & LANDASAN TEORI -->
<h1>Bagian I: Pendahuluan & Landasan Teori</h1>

<h2>1.1 Transformasi Paradigma Geospasial di Era Artificial Intelligence</h2>
<p>
  Sistem Informasi Geografis Berbasis Web (WebGIS) telah menjadi media paling efektif dalam mendemokratisasikan data geospasial kepada publik. Melalui peramban web tanpa memerlukan instalasi perangkat lunak GIS desktop yang berat, pengguna awam dapat mengeksplorasi data sebaran, pola keruangan, hingga analisis temporal.
</p>
<p>
  Namun, kurva pembelajaran pengembangan WebGIS konvensional sangat terjal. Pengembang dituntut menguasai kartografi geodesi (sistem proyeksi, datum WGS84, koordinat desimal), penataan format data (GeoJSON, TopoJSON), pemrograman frontend modern (HTML5, CSS Flexbox/Grid, JavaScript asynchronous), pustaka pemetaan (Leaflet.js, OpenLayers), serta manajemen server dan deployment (Git, GitHub, web server).
</p>
<p>
  Hadirnya <strong>Generative AI</strong> dan <strong>Agentic AI Coding Assistant</strong> tidak menghilangkan kaidah keilmuan geospasial, melainkan mentransformasi alur kerja: pengembang tidak lagi disibukkan oleh penulisan kode sintaksis baris-demi-baris yang rawan galat (syntax error), melainkan fokus sebagai <strong>Arsitek Sistem (System Architect)</strong> dan <strong>Kurator Kualitas Data (Quality Assurer)</strong>.
</p>

<h2>1.2 Capaian Pembelajaran Workshop (Learning Outcomes)</h2>
<p>Setelah menyelesaikan modul pelatihan ini selama 120 menit, peserta diharapkan mampu:</p>
<ul>
  <li><strong>Capaian Kognitif:</strong> Memahami arsitektur alur kerja multi-AI dalam rekayasa geospasial serta prinsip dasar mitigasi halusinasi toponimi.</li>
  <li><strong>Capaian Psikomotorik:</strong> Mampu mengekstrak data tabel web menjadi JSON spasial terstruktur, mengoreksi anomali pembalikan koordinat (lat/lng inversion), merancang antarmuka Leaflet interaktif, dan mempublikasikan kode ke GitHub Pages secara otonom.</li>
  <li><strong>Capaian Afektif:</strong> Memiliki etika integritas data ilmiah dengan melampirkan atribusi sumber, lisensi berkas terbuka, dan indikator kepastian historis (confidence level).</li>
</ul>

<!-- BAGIAN II: ALOKASI WAKTU 120 MENIT -->
<div class="page-break"></div>
<h1>Bagian II: Alokasi Waktu & Silabus Pelatihan (120 Menit)</h1>
<p>
  Pelatihan disusun menggunakan pendekatan <em>Action Learning</em> dengan rasio 25% pemahaman konsep dan 75% praktik laboratorium terbimbing:
</p>

<table>
  <thead>
    <tr>
      <th style="width: 14%;">Waktu</th>
      <th style="width: 11%;">Durasi</th>
      <th style="width: 45%;">Materi Pelatihan & Langkah Kerja</th>
      <th style="width: 30%;">Keluaran (Output) Peserta</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>00:00 - 00:15</strong></td>
      <td>15 menit</td>
      <td><strong>Pengantar Paradigma & Ekosistem 3 Pilar AI:</strong> Peran ChatGPT (Konsep), Google AI Studio (Desain UI), dan Antigravity (Eksekusi Coding & Git).</td>
      <td>Pemahaman arsitektur sistem & persiapan workspace</td>
    </tr>
    <tr>
      <td><strong>00:15 - 00:40</strong></td>
      <td>25 menit</td>
      <td><strong>Fase 1: AI Web Scraping & Ekstraksi Data:</strong> Teknik mengambil tabel dari web/Wikipedia dan konversi ke skema data JSON/GeoJSON terstandar WGS84.</td>
      <td>Berkas dataset mentah terstruktur (<code>data/raw.json</code>)</td>
    </tr>
    <tr>
      <td><strong>00:40 - 01:00</strong></td>
      <td>20 menit</td>
      <td><strong>Fase 2: Validasi Geospasial & Anti-Halusinasi:</strong> Verifikasi koordinat (deteksi Lat/Lng flip), validasi toponimi citra satelit, dan penetapan <em>Confidence Level</em>.</td>
      <td>Dataset bersih terverifikasi (<code>data/sites.json</code>)</td>
    </tr>
    <tr>
      <td><strong>01:00 - 01:35</strong></td>
      <td>35 menit</td>
      <td><strong>Fase 3: Agentic Coding (Leaflet Engine):</strong> Merakit peta Leaflet, popup foto lazy-loading, drawer informasi responsif seluler, dan filter pencarian.</td>
      <td>Aplikasi WebGIS fungsional di server lokal</td>
    </tr>
    <tr>
      <td><strong>01:35 - 01:50</strong></td>
      <td>15 menit</td>
      <td><strong>Fase 4: Otomasi Publikasi ke GitHub Pages:</strong> Perintah Git otomatis via AI, konfigurasi branch deployment, dan peluncuran website publik.</td>
      <td>URL aktif WebGIS (dapat dibuka di smartphone)</td>
    </tr>
    <tr>
      <td><strong>01:50 - 02:00</strong></td>
      <td>10 menit</td>
      <td><strong>Fase 5: Evaluasi Mandiri & Pengumpulan Ujian:</strong> Presentasi hasil proyek, pengujian fitur responsif, dan evaluasi capaian tugas.</td>
      <td>Penilaian proyek mandiri peserta</td>
    </tr>
  </tbody>
</table>

<!-- BAGIAN III: AI WEB SCRAPING & EKSTRAKSI DATA -->
<h1>Bagian III: Ekstraksi Data Spasial (AI Web Scraping)</h1>
<p>
  Tantangan utama pemetaan tematik adalah ketiadaan data spasial siap pakai (seperti format SHP atau GeoJSON) dari institusi resmi. Sebagian besar data cagar budaya, fasilitas kesehatan, atau pariwisata tersimpan dalam format teks artikel, siaran pers, atau tabel Wikipedia.
</p>

<div class="diagram-box">
  <!-- SVG ILLUSTRATION 2: DATA EXTRACTION WORKFLOW -->
  <svg width="560" height="95" viewBox="0 0 560 95" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="15" width="120" height="65" rx="6" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5" />
    <text x="70" y="38" fill="#1e293b" font-size="9" font-weight="bold" text-anchor="middle">Sumber Web</text>
    <text x="70" y="52" fill="#64748b" font-size="7.5" text-anchor="middle">Wikipedia, Berita,</text>
    <text x="70" y="65" fill="#64748b" font-size="7.5" text-anchor="middle">Tabel HTML, PDF</text>

    <path d="M 130 47 L 155 47" stroke="#0f4c3a" stroke-width="2" />

    <rect x="155" y="15" width="130" height="65" rx="6" fill="#ecfdf5" stroke="#059669" stroke-width="1.5" />
    <text x="220" y="38" fill="#065f46" font-size="9" font-weight="bold" text-anchor="middle">AI Parsing Prompt</text>
    <text x="220" y="52" fill="#047857" font-size="7.5" text-anchor="middle">Ekstraksi Entitas &</text>
    <text x="220" y="65" fill="#047857" font-size="7.5" text-anchor="middle">Estimasi Koordinat</text>

    <path d="M 285 47 L 310 47" stroke="#0f4c3a" stroke-width="2" />

    <rect x="310" y="15" width="115" height="65" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" />
    <text x="367" y="38" fill="#92400e" font-size="9" font-weight="bold" text-anchor="middle">Skema Terstruktur</text>
    <text x="367" y="52" fill="#b45309" font-size="7.5" text-anchor="middle">JSON Array Object</text>
    <text x="367" y="65" fill="#b45309" font-size="7.5" text-anchor="middle">Atribut Tematik</text>

    <path d="M 425 47 L 450 47" stroke="#0f4c3a" stroke-width="2" />

    <rect x="450" y="15" width="100" height="65" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5" />
    <text x="500" y="38" fill="#0369a1" font-size="9" font-weight="bold" text-anchor="middle">GeoJSON WGS84</text>
    <text x="500" y="52" fill="#0284c7" font-size="7.5" text-anchor="middle">FeatureCollection</text>
    <text x="500" y="65" fill="#0284c7" font-size="7.5" text-anchor="middle">Siap Leaflet.js</text>
  </svg>
  <div class="diagram-caption">Gambar 2: Alur Konversi Data Semi-Terstruktur Web Menjadi Standar Geospasial</div>
</div>

<h3>3.1 Metode AI Table & Text Parsing (Tanpa Koding)</h3>
<p>
  Peserta dapat menyalin tabel atau teks panjang dari halaman web, kemudian menggunakan prompt terstruktur pada model AI (ChatGPT atau Gemini):
</p>

<pre><code>"Anda adalah Data Extraction Specialist. Berikut teks daftar cagar budaya yang saya salin:
[TEMPELKAN TEKS / TABEL DARI WEBSITE]

Tugas:
1. Ekstrak menjadi format JSON array murni tanpa narasi pembuka/penutup.
2. Setiap objek wajib memuat atribut: id, nama_objek, kategori, tahun_pembangunan, latitude, longitude, deskripsi, sumber_referensi.
3. Estimasi koordinat geografis dalam sistem proyeksi CRS WGS84 (EPSG:4326).
4. Verifikasi bahwa nilai Latitude bernilai negatif untuk belahan bumi selatan Indonesia (0 s/d -11) dan Longitude berkisar antara 95 s/d 141 BT."</code></pre>

<div class="page-break"></div>

<!-- BAGIAN IV: PROTOKOL VALIDASI & ANTI-HALUSINASI -->
<h1>Bagian IV: Protokol Validasi Geospasial (Anti-Hallucination)</h1>

<div class="callout callout-caution">
  <div class="callout-title">⚠️ PERINGATAN KRITIS: KARAKTERISTIK HALUSINASI AI PADA DATA SPASIAL</div>
  Model bahasa besar (LLM) bekerja memprediksi probabilitas kata berikutnya, bukan menghitung posisi geodesi di permukaan bumi. Oleh sebab itu, AI sangat rentan mengarang desimal koordinat geografis. Seluruh data spasial yang dihasilkan oleh AI <strong>WAJIB</strong> melalui protokol pengujian berikut sebelum dimasukkan ke peta.
</div>

<div class="diagram-box">
  <!-- SVG ILLUSTRATION 3: QUALITY CONTROL WORKFLOW -->
  <svg width="560" height="90" viewBox="0 0 560 90" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="15" width="120" height="60" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5" />
    <text x="70" y="42" fill="#0369a1" font-size="8.5" font-weight="bold" text-anchor="middle">1. Cek Lat/Lng Flip</text>
    <text x="70" y="58" fill="#0284c7" font-size="7.5" text-anchor="middle">Rentang Bounding Box</text>

    <path d="M 130 45 L 150 45" stroke="#64748b" stroke-width="2" />

    <rect x="150" y="15" width="120" height="60" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" />
    <text x="210" y="42" fill="#92400e" font-size="8.5" font-weight="bold" text-anchor="middle">2. Verifikasi Satelit</text>
    <text x="210" y="58" fill="#b45309" font-size="7.5" text-anchor="middle">Tapak Cagar Budaya</text>

    <path d="M 270 45 L 290 45" stroke="#64748b" stroke-width="2" />

    <rect x="290" y="15" width="125" height="60" rx="6" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.5" />
    <text x="352" y="42" fill="#6b21a8" font-size="8.5" font-weight="bold" text-anchor="middle">3. Kronologi & Epigrafi</text>
    <text x="352" y="58" fill="#7c3aed" font-size="7.5" text-anchor="middle">Bukti Penulisan Sejarah</text>

    <path d="M 415 45 L 435 45" stroke="#64748b" stroke-width="2" />

    <rect x="435" y="15" width="115" height="60" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" />
    <text x="492" y="42" fill="#15803d" font-size="8.5" font-weight="bold" text-anchor="middle">4. Confidence Level</text>
    <text x="492" y="58" fill="#16a34a" font-size="7.5" text-anchor="middle">Tinggi / Interpretatif</text>
  </svg>
  <div class="diagram-caption">Gambar 3: Empat Pilar Protokol Verifikasi Integritas Data Geospasial</div>
</div>

<h3>4.1 Uji Inversi Koordinat (Latitude / Longitude Flip Test)</h3>
<p>
  Kesalahan paling lazim yang dilakukan pemula maupun sistem AI adalah tertukarnya kolom lintang (Latitude) dan bujur (Longitude). Wilayah Negara Kesatuan Republik Indonesia berada pada batas koordinat (<em>Bounding Box</em>):
</p>
<ul>
  <li><strong>Latitude ($\phi$):</strong> $+6^\circ\text{ LU}$ (Pulau Weh/Sabang) hingga $-11^\circ\text{ LS}$ (Pulau Rote).</li>
  <li><strong>Longitude ($\lambda$):</strong> $+95^\circ\text{ BT}$ (Ujung barat Sumatera) hingga $+141^\circ\text{ BT}$ (Merauke).</li>
</ul>
<p>
  <em>Aturan Baku: Jika nilai latitude bernilai positif di atas $6$ atau bernilai lebih dari $90$ (misal $110.36$), berarti koordinat tertukar dengan longitude! Jika tidak dikoreksi, titik akan terlempar ke Samudera Hindia atau kutub bumi.</em>
</p>

<h3>4.2 Verifikasi Toponimi Fisik vs Administrasi Modern</h3>
<p>
  Pencarian lokasi sejarah di peta modern seringkali keliru mengarah ke pusat kecamatan atau kantor bupati masa kini. Contoh: <em>Sunda Kelapa</em> harus diposisikan di muara pelabuhan tua Jakarta Utara (bukan Monas), dan <em>Bandar Kuno Barus</em> harus diletakkan pada situs arkeologi Makam Papan Tinggi / Lobu Tua di Tapanuli Tengah (bukan terminal bus kota).
</p>

<h3>4.3 Penentuan Indikator Kepastian Data (Confidence Level)</h3>
<table>
  <thead>
    <tr>
      <th style="width: 25%;">Tingkat Kepastian</th>
      <th style="width: 45%;">Kriteria Arkeologis & Geodesi</th>
      <th style="width: 30%;">Penetapan Tampilan Peta</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Tinggi (High)</strong></td>
      <td>Struktur fisik bangunan cagar budaya masih berdiri utuh; koordinat diverifikasi melalui GPS geodetik / citra satelit resolusi tinggi; didukung SK Cagar Budaya Nasional.</td>
      <td>Titik solid; poligon batas definitif terverifikasi peta arsip resmi.</td>
    </tr>
    <tr>
      <td><strong>Sedang (Medium)</strong></td>
      <td>Sisa fondasi berupa reruntuhan arkeologis ditemukan; toponimi didukung prasasti/laporan kolonial (Oudheidkundige Dienst), namun batas lingkungan luar bersifat estimasi.</td>
      <td>Titik solid; poligon batas diberi garis putus-putus (*dashed line*).</td>
    </tr>
    <tr>
      <td><strong>Interpretatif</strong></td>
      <td>Hanya disebutkan dalam naskah babad/hikayat tanpa sisa arsitektur fisik yang dapat diidentifikasi secara pasti di lapangan.</td>
      <td>Dilarang membuat batas administratif rekaan; wajib diberi label perkiraan wilayah mandala.</td>
    </tr>
  </tbody>
</table>

<!-- BAGIAN V: PANDUAN DATASET MANDIRI UJIAN -->
<div class="page-break"></div>
<h1>Bagian V: Panduan Melampirkan Dataset Mandiri Peserta (Ujian Praktikum)</h1>
<p>
  Sebagai syarat kelulusan pelatihan, peserta diwajibkan menyusun dan memetakan satu dataset tematik mandiri yang relevan dengan bidang studinya (misal: <em>sebaran puskesmas dan apotek</em>, <em>sebaran peninggalan era kolonial di kota asal</em>, atau <em>sebaran destinasi ekowisata</em>).
</p>

<h3>5.1 Standar Format Berkas Spreadsheet (CSV / Excel)</h3>
<p>
  Peserta wajib menyusun data dalam format berkas <code>data/dataset_mandiri.csv</code> dengan struktur kolom baku sebagai berikut:
</p>

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
      <td>https://commons.../Demak.jpg</td>
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
      <td>https://commons.../Somba.jpg</td>
      <td>Balai Arkeologi Sulsel</td>
    </tr>
    <tr>
      <td><code>obj-03</code></td>
      <td>Keraton Kasepuhan</td>
      <td>istana</td>
      <td>-6.7265</td>
      <td>108.5711</td>
      <td>1529</td>
      <td>9999</td>
      <td>https://commons.../Cirebon.jpg</td>
      <td>Disbudpar Cirebon</td>
    </tr>
  </tbody>
</table>

<h3>5.2 Instruksi Eksekusi Konversi Data pada Antigravity</h3>
<p>
  Setelah menyalin file CSV ke dalam direktori <code>data/</code>, peserta cukup memberikan instruksi bahasa alami berikut pada konsol asisten AI:
</p>

<pre><code>"Saya telah menyiapkan dataset mandiri untuk ujian praktikum di berkas 'data/dataset_mandiri.csv'.
Tolong lakukan audit terhadap berkas tersebut:
1. Validasi nilai latitude dan longitude pada setiap baris data agar berada dalam Bounding Box Indonesia.
2. Konversikan berkas CSV tersebut menjadi format 'data/sites.json' berstandar GeoJSON/WGS84.
3. Sambungkan layer ini ke modul pemetaan Leaflet pada 'assets/js/map.js' lengkap dengan ikon penanda sesuai kategori dan popup kartu foto yang responsif."</code></pre>

<!-- BAGIAN VI: PERANCANGAN UI/UX & AGENTIC CODING -->
<h1>Bagian VI: Perancangan UI & Pemrograman Otonom (Agentic Coding)</h1>

<div class="diagram-box">
  <!-- SVG ILLUSTRATION 4: WIREFRAME UI MOBILE -->
  <svg width="550" height="150" viewBox="0 0 550 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Smartphone Frame -->
    <rect x="25" y="10" width="105" height="130" rx="8" fill="#ffffff" stroke="#334155" stroke-width="2" />
    <rect x="30" y="15" width="95" height="15" fill="#0f4c3a" />
    <text x="77" y="25" fill="#fde68a" font-size="6" text-anchor="middle">WebGIS Sebaran</text>
    <!-- Map Canvas -->
    <rect x="30" y="32" width="95" height="60" fill="#e2e8f0" />
    <circle cx="55" cy="55" r="4" fill="#059669" />
    <circle cx="85" cy="65" r="4" fill="#d97706" />
    <!-- Floating Slider -->
    <rect x="35" y="78" width="85" height="10" rx="3" fill="#ffffff" opacity="0.9" stroke="#cbd5e1" />
    <line x1="45" y1="83" x2="110" y2="83" stroke="#0f4c3a" stroke-width="1.5" />
    <circle cx="75" cy="83" r="2.5" fill="#d97706" />
    <!-- Bottom Sheet / Drawer -->
    <rect x="30" y="95" width="95" height="40" rx="4" fill="#ffffff" stroke="#cbd5e1" />
    <line x1="68" y1="98" x2="87" y2="98" stroke="#94a3b8" stroke-width="1.5" stroke-linecap="round" />
    <rect x="35" y="103" width="20" height="20" fill="#0f172a" rx="2" />
    <text x="60" y="110" fill="#0f4c3a" font-size="5" font-weight="bold">Masjid Demak</text>
    <text x="60" y="118" fill="#64748b" font-size="4">Tahun: 1479 M</text>

    <!-- Legend Arrows -->
    <path d="M 140 25 L 200 25" stroke="#0f4c3a" stroke-width="1.5" marker-end="url(#arrow)" />
    <text x="210" y="28" fill="#1e293b" font-size="8.5" font-weight="bold">1. Header Responsif & Bilah Pencarian Cepat</text>

    <path d="M 140 60 L 200 60" stroke="#0f4c3a" stroke-width="1.5" />
    <text x="210" y="63" fill="#1e293b" font-size="8.5" font-weight="bold">2. Kanvas Peta Interaktif Leaflet (Tile OpenStreetMap / CartoDB)</text>

    <path d="M 140 85 L 200 85" stroke="#0f4c3a" stroke-width="1.5" />
    <text x="210" y="88" fill="#1e293b" font-size="8.5" font-weight="bold">3. Floating Timeline Bar (Pengatur Filter Periode Waktu Temporal)</text>

    <path d="M 140 115 L 200 115" stroke="#0f4c3a" stroke-width="1.5" />
    <text x="210" y="118" fill="#1e293b" font-size="8.5" font-weight="bold">4. Interactive Bottom Sheet (Drawer Detail Cagar Budaya & Foto)</text>
  </svg>
  <div class="diagram-caption">Gambar 4: Rancangan Tata Letak Wireframe Antarmuka Mobile-First WebGIS</div>
</div>

<h3>6.1 Arsitektur Modular Kode JavaScript</h3>
<p>
  Aplikasi dibangun tidak dalam satu berkas raksasa, melainkan modular agar mudah dipelihara dan diperbaiki:
</p>
<ul>
  <li><code>assets/js/map.js</code>: Mengatur inisialisasi peta Leaflet, pergeseran pusat pandang (zoom to bounding box), penanganan marker cluster, dan pergantian basemap.</li>
  <li><code>assets/js/timeline.js</code>: Mengatur kontrol linimasa dinamis, pemutaran animasi otomatis (play/pause), dan penyaringan layer berdasarkan tahun historis.</li>
  <li><code>assets/js/detail.js</code>: Mengelola panel informasi detail (*drawer*), penayangan foto resolusi tinggi, data silsilah penguasa, dan daftar referensi akademik.</li>
  <li><code>assets/js/filters.js</code>: Mengatur penyaringan spasial berdasarkan kepulauan dan kategori situs.</li>
</ul>

<div class="page-break"></div>

<!-- BAGIAN VII: PUBLIKASI KE GITHUB PAGES -->
<h1>Bagian VII: Publikasi Terbuka di GitHub Pages</h1>

<div class="diagram-box">
  <!-- SVG ILLUSTRATION 5: GITHUB DEPLOYMENT PIPELINE -->
  <svg width="560" height="85" viewBox="0 0 560 85" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="15" width="115" height="55" rx="6" fill="#f8fafc" stroke="#334155" stroke-width="1.5" />
    <text x="67" y="38" fill="#1e293b" font-size="8.5" font-weight="bold" text-anchor="middle">Komputer Lokal</text>
    <text x="67" y="52" fill="#64748b" font-size="7.5" text-anchor="middle">Workspace Proyek</text>

    <path d="M 125 42 L 155 42" stroke="#0f4c3a" stroke-width="2" />

    <rect x="155" y="15" width="115" height="55" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5" />
    <text x="212" y="38" fill="#166534" font-size="8.5" font-weight="bold" text-anchor="middle">Git Command</text>
    <text x="212" y="52" fill="#15803d" font-size="7.5" text-anchor="middle">Commit & Push</text>

    <path d="M 270 42 L 300 42" stroke="#0f4c3a" stroke-width="2" />

    <rect x="300" y="15" width="115" height="55" rx="6" fill="#1e293b" />
    <text x="357" y="38" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">GitHub Cloud</text>
    <text x="357" y="52" fill="#4ade80" font-size="7.5" text-anchor="middle">Branch 'main'</text>

    <path d="M 415 42 L 445 42" stroke="#0f4c3a" stroke-width="2" />

    <rect x="445" y="15" width="105" height="55" rx="6" fill="#0f4c3a" />
    <text x="497" y="38" fill="#fde68a" font-size="8.5" font-weight="bold" text-anchor="middle">GitHub Pages</text>
    <text x="497" y="52" fill="#ffffff" font-size="7.5" text-anchor="middle">Live Website HTTPS</text>
  </svg>
  <div class="diagram-caption">Gambar 5: Siklus Otomasi Continuous Deployment Menggunakan GitHub Pages</div>
</div>

<h3>7.1 Langkah Aktivasi Publikasi</h3>
<ol>
  <li>Pastikan seluruh berkas telah di-push ke repositori GitHub pada branch <code>main</code>.</li>
  <li>Buka repositori Anda di browser web &rarr; Masuk ke menu <strong>Settings</strong> &rarr; Pilih bilah <strong>Pages</strong> di sebelah kiri.</li>
  <li>Pada menu <em>Build and deployment</em> &rarr; <em>Branch</em>: pilih <code>main</code> dan direktori <code>/ (root)</code> &rarr; Klik <strong>Save</strong>.</li>
  <li>Tunggu 60–120 detik, muat ulang halaman. Alamat situs publik Anda akan aktif pada tautan:
    <br><code>https://[nama-pengguna].github.io/[nama-repositori]/</code>
  </li>
</ol>

<!-- BAGIAN VIII: EVALUASI & RUBRIK PENILAIAN -->
<h1>Bagian VIII: Lembar Evaluasi & Rubrik Penilaian Ujian Praktikum</h1>

<p>
  Penilaian proyek WebGIS mandiri peserta didasarkan pada skala 100 dengan pembobotan komprehensif:
</p>

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Komponen Penilaian</th>
      <th style="width: 15%;">Bobot</th>
      <th style="width: 60%;">Indikator Keberhasilan (Kriteria Objektif)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Integritas Data & Validasi Spasial</strong></td>
      <td><strong>30%</strong></td>
      <td>Tidak terjadi galat lat/lng inversion; seluruh koordinat objek berada tepat pada tapak fisik di Indonesia; format data memenuhi standar JSON/GeoJSON WGS84; memiliki indikator <em>confidence level</em>.</td>
    </tr>
    <tr>
      <td><strong>2. Fungsionalitas Peta & Interaktivitas</strong></td>
      <td><strong>25%</strong></td>
      <td>Peta Leaflet memuat basemap dengan baik; marker dapat diklik untuk membuka popup; fitur filter kategori dan pencarian nama berfungsi mulus.</td>
    </tr>
    <tr>
      <td><strong>3. Kualitas UI/UX & Responsif Mobile</strong></td>
      <td><strong>25%</strong></td>
      <td>Tampilan tidak tumpang tindih (*overlapping*) di layar smartphone (lebar layar 360–400px); drawer informasi dapat digeser; gambar dokumentasi menerapkan <em>lazy loading</em> (anti-lag).</td>
    </tr>
    <tr>
      <td><strong>4. Publikasi & Continuous Deployment</strong></td>
      <td><strong>20%</strong></td>
      <td>Proyek berhasil dipublikasikan di GitHub Pages; website dapat dibuka secara publik melalui URL HTTPS tanpa galat 404; riwayat commit Git terdokumentasi dengan baik.</td>
    </tr>
  </tbody>
</table>

<!-- BAGIAN IX: GLOSARIUM & REFERENSI AKADEMIK -->
<div class="page-break"></div>
<h1>Bagian IX: Glosarium Istilah & Rujukan Akademik</h1>

<h3>Glosarium Geospasial & Web Development:</h3>
<ul>
  <li><strong>CRS (Coordinate Reference System):</strong> Sistem koordinat untuk memproyeksikan permukaan lengkung bumi ke dalam representasi matematis.</li>
  <li><strong>WGS84 (EPSG:4326):</strong> Datum geodesi standar global yang digunakan oleh GPS dan Leaflet.js dengan unit derajat desimal.</li>
  <li><strong>GeoJSON:</strong> Format standar berbasis JSON untuk menyandikan aneka struktur data geografis (Point, LineString, Polygon, FeatureCollection).</li>
  <li><strong>Lat/Lng Inversion:</strong> Galat fatal akibat tertukarnya urutan lintang (Latitude) dan bujur (Longitude), menyebabkan fitur spasial berpindah posisi ke belahan bumi lain.</li>
  <li><strong>Native Lazy Loading:</strong> Atribut peramban (<code>loading="lazy"</code>) yang menunda pengunduhan gambar hingga pengguna menggulir layar mendekati posisi gambar tersebut, sangat krusial untuk menghemat memori perangkat seluler.</li>
  <li><strong>Agentic AI:</strong> Model kecerdasan buatan tingkat lanjut yang memiliki kapabilitas menggunakan alat (*tool use*), mengeksekusi perintah terminal, membaca basis kode, dan memperbaiki galat pemrograman secara mandiri.</li>
</ul>

<h3>Rujukan Kartografi & Historiografi:</h3>
<ol>
  <li>Cribb, R. (2000). <em>Historical Atlas of Indonesia</em>. Richmond, Surrey: Curzon Press.</li>
  <li>Reid, A. (1993). <em>Southeast Asia in the Age of Commerce 1450–1680: Volume Two: Expansion and Crisis</em>. New Haven: Yale University Press.</li>
  <li>De Graaf, H. J., & Pigeaud, T. G. T. (1985). <em>Kerajaan-Kerajaan Islam Pertama di Jawa: Kajian Sejarah Politik Abad ke-15 dan ke-16</em>. Jakarta: Grafiti Pers.</li>
  <li>Direktorat Pelindungan Kebudayaan. (2020). <em>Sistem Registrasi Nasional Cagar Budaya</em>. Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi Republik Indonesia.</li>
</ol>

<hr style="border: none; border-top: 1px solid #cbd5e1; margin: 30px 0;">
<p style="font-size: 8pt; color: #64748b; text-align: center;">
  Modul Pelatihan & Ujian Praktikum: Pengembangan WebGIS Tematik Menggunakan Ekosistem Multi-AI.<br>
  Diproduksi untuk Penggunaan Akademik, Laboratorium Sistem Informasi Geospasial, dan Workshop Pelatihan (2026).
</p>

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML Template generated: {HTML_PATH}")

# ==============================================================================
# CONVERT TO PDF VIA HEADLESS MICROSOFT EDGE
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
# GENERATE DETAILED WORD DOCUMENT (.DOCX)
# ==============================================================================
print("Generating comprehensive Microsoft Word (.docx)...")
doc = docx.Document()

# Margins
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

COLOR_PRIMARY = RGBColor(15, 76, 58)    # #0f4c3a Emerald
COLOR_SECONDARY = RGBColor(217, 119, 6) # #d97706 Gold
COLOR_TEXT = RGBColor(30, 41, 59)       # #1e293b Slate Dark

p_head = doc.add_paragraph()
r_head = p_head.add_run("MODUL PEMBELAJARAN & PEDOMAN PRAKTIKUM LABORATORIUM GIS\n")
r_head.font.name = "Arial"
r_head.font.size = Pt(9)
r_head.font.bold = True
r_head.font.color.rgb = RGBColor(100, 116, 139)

r_badge = p_head.add_run("EDISI LENGKAP WORKSHOP INTENSIF (120 MENIT)\n")
r_badge.font.name = "Arial"
r_badge.font.size = Pt(10)
r_badge.font.bold = True
r_badge.font.color.rgb = COLOR_SECONDARY

r_title = p_head.add_run("Pengembangan Sistem Informasi Geografis Berbasis Web (WebGIS) Tematik Menggunakan Ekosistem Artificial Intelligence")
r_title.font.name = "Arial"
r_title.font.size = Pt(20)
r_title.font.bold = True
r_title.font.color.rgb = COLOR_PRIMARY

p_sub = doc.add_paragraph()
r_sub = p_sub.add_run("Panduan Komprehensif: Ekstraksi Data Spasial Otomatis, Protokol Validasi Geodesi Anti-Halusinasi, Perancangan Antarmuka Responsif, Pemrograman Otonom, hingga Publikasi Terbuka di GitHub Pages.")
r_sub.font.name = "Arial"
r_sub.font.size = Pt(11)
r_sub.font.italic = True
r_sub.font.color.rgb = RGBColor(71, 85, 105)

# Metadata Table
tbl_meta = doc.add_table(rows=2, cols=2)
tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_meta.rows[0].cells[0].text = "Sasaran: Mahasiswa, Peneliti, & Pengembang GIS"
tbl_meta.rows[0].cells[1].text = "Durasi: 2 Jam (120 Menit Hands-On)"
tbl_meta.rows[1].cells[0].text = "Studi Kasus: Atlas Sejarah Islam Nusantara"
tbl_meta.rows[1].cells[1].text = "Teknologi: Leaflet.js, CRS WGS84, GitHub Pages"

doc.add_paragraph()

def add_h1(text):
    h = doc.add_heading(text, level=1)
    for r in h.runs:
        r.font.name = "Arial"
        r.font.size = Pt(14)
        r.font.bold = True
        r.font.color.rgb = COLOR_PRIMARY
    return h

def add_h2(text):
    h = doc.add_heading(text, level=2)
    for r in h.runs:
        r.font.name = "Arial"
        r.font.size = Pt(11.5)
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
    p.paragraph_format.line_spacing = 1.2
    return p

# Sections
add_h1("Bagian I: Pendahuluan & Landasan Teori")
add_h2("1.1 Transformasi Paradigma Geospasial di Era AI")
add_p("WebGIS adalah sarana utama dalam mendemokratisasikan akses data geospasial bagi masyarakat luas. Pengembangan WebGIS konvensional memerlukan kemahiran multidisiplin: kartografi geodesi, struktur data GeoJSON/WGS84, antarmuka web, pustaka pemetaan Leaflet, serta manajemen server. Hadirnya Generative AI dan Agentic AI Coding Assistant mentransformasi pengembang menjadi Arsitek Sistem dan Kurator Kualitas Data, sementara AI mengotomasi penulisan kode sintaksis dan debugging.")

add_h2("1.2 Capaian Pembelajaran Workshop (Learning Outcomes)")
add_p("Peserta diharapkan menguasai: 1) Pemahaman arsitektur multi-AI, 2) Keterampilan teknis ekstraksi data web dan validasi koordinat WGS84, 3) Perancangan antarmuka mobile-first Leaflet, 4) Publikasi otonom via GitHub Pages, serta 5) Integritas data ilmiah.")

add_h1("Bagian II: Alokasi Waktu & Silabus Pelatihan (120 Menit)")
add_p("Pelatihan dirancang intensif dalam 5 fase kerja terstruktur:")
add_p("1. 00:00 - 00:15 (15 mnt): Pengantar Paradigma 3 Pilar AI (ChatGPT, Google AI Studio, Antigravity)")
add_p("2. 00:15 - 00:40 (25 mnt): Fase 1 - AI Web Scraping & Ekstraksi Data Tabular Web ke format JSON")
add_p("3. 00:40 - 01:00 (20 mnt): Fase 2 - Validasi Geospasial Anti-Halusinasi & Penyusunan Dataset Mandiri")
add_p("4. 01:00 - 01:35 (35 mnt): Fase 3 - Hands-on Coding di Antigravity (Peta Leaflet, Drawer, & Mobile)")
add_p("5. 01:35 - 01:50 (15 mnt): Fase 4 - Otomasi Publikasi Git & Peluncuran GitHub Pages")
add_p("6. 01:50 - 02:00 (10 mnt): Fase 5 - Evaluasi Ujian & Presentasi Karya Peserta")

add_h1("Bagian III: Ekstraksi Data Spasial (AI Web Scraping)")
add_p("Data cagar budaya dan potensi wilayah umumnya tersimpan dalam bentuk teks berita atau tabel Wikipedia. Peserta menggunakan prompt rekayasa ekstraksi data untuk mengubah tabel tidak terstruktur menjadi JSON array dengan atribut: id, nama_objek, kategori, tahun, latitude, longitude, deskripsi, dan referensi sumber.")

add_h1("Bagian IV: Protokol Validasi Geospasial (Anti-Hallucination)")
add_p("Pemeriksaan kualitas wajib mencakup:")
add_p("1. Uji Inversi Koordinat (Lat/Lng Flip): Memastikan nilai Latitude bernilai negatif (0 s/d -11) dan Longitude berkisar 95 s/d 141 BT di wilayah Indonesia.")
add_p("2. Verifikasi Toponimi Fisik vs Administrasi: Memastikan titik tepat berada di atas tapak cagar budaya, bukan sekadar kantor kecamatan modern.")
add_p("3. Penetapan Confidence Level: Mengklasifikasikan data menjadi Tinggi (arkeologis terdaftar), Sedang (reruntuhan bersejarah), dan Interpretatif (teks naskah kuno).")

add_h1("Bagian V: Panduan Dataset Mandiri Peserta (Ujian Praktikum)")
add_p("Peserta menyusun berkas data/dataset_mandiri.csv dengan kolom baku: id, nama_objek, kategori, latitude, longitude, tahun_awal, tahun_akhir, foto_url, sumber_data. Peserta menginstruksikan Antigravity untuk mengonversi dan memetakan layernya secara instan.")

add_h1("Bagian VI: Perancangan UI & Pemrograman Otonom (Agentic Coding)")
add_p("Arsitektur kode dipecah secara modular: map.js (manajemen Leaflet), timeline.js (slider temporal), detail.js (drawer informasi & foto lazy-loading), dan filters.js (filter kategori). Antarmuka menerapkan prinsip Mobile-First dengan floating slider dan interactive bottom sheet.")

add_h1("Bagian VII: Publikasi Terbuka di GitHub Pages")
add_p("Peserta menginstruksikan Antigravity untuk menjalankan perintah git push secara otonom. GitHub Pages diaktifkan pada branch main untuk menerbitkan WebGIS secara live dan gratis tanpa perlu konfigurasi server rumit.")

add_h1("Bagian VIII: Lembar Evaluasi & Rubrik Penilaian")
add_p("Penilaian ujian praktikum didasarkan pada 4 kriteria: 1) Integritas Data & Validasi Spasial (30%), 2) Fungsionalitas Peta & Interaktivitas (25%), 3) Kualitas UI/UX & Responsif Mobile (25%), dan 4) Keberhasilan Publikasi GitHub Pages (20%).")

add_h1("Bagian IX: Glosarium & Referensi")
add_p("Memuat definisi istilah: CRS, WGS84, GeoJSON, Lat/Lng Inversion, Native Lazy Loading, dan Agentic AI, serta referensi akademik otoritatif (Cribb 2000, Reid 1993, De Graaf 1985, Kemendikbudristek 2020).")

doc.save(DOCX_PATH)
print(f"Word Document updated: {DOCX_PATH} ({os.path.getsize(DOCX_PATH):,} bytes)")

# ==============================================================================
# ALSO UPDATE MARKDOWN VERSION
# ==============================================================================
# Strip HTML tags simply or generate a clean markdown mirror
md_content = """# MODUL PELATIHAN PRAKTIKUM: PENGEMBANGAN SISTEM INFORMASI GEOGRAFIS BERBASIS WEB (WEBGIS) TEMATIK MENGGUNAKAN EKOSISTEM ARTIFICIAL INTELLIGENCE
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
- **Latitude ($\phi$):** $+6^\circ\text{ LU}$ (Sabang) hingga $-11^\circ\text{ LS}$ (Rote).
- **Longitude ($\lambda$):** $+95^\circ\text{ BT}$ hingga $+141^\circ\text{ BT}$.

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
"""

with open(MD_PATH, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Markdown file updated: {MD_PATH}")
print("ALL FORMATS REBUILT SUCCESSFULLY!")
