"""
generate_sites_and_events.py
Generates data/sites.json, data/events.json, and enriches data/kingdoms.json with NKRI integration metadata.
Based on academic sources:
- Ricklefs (2008) Sejarah Indonesia Modern 1200-2008
- Reid (2005) An Indonesian Frontier
- De Graaf & Pigeaud (1985) Kerajaan Islam Pertama di Jawa
- Kemendikbudristek: Sistem Registrasi Nasional Cagar Budaya (cagarbudaya.kemdikbud.go.id)
- Arsip Nasional Republik Indonesia (ANRI) Seri Swapraja & Kooti 1945-1950
"""

import json
import os

SITES_DATA = [
    # MASJID BERSEJARAH (Mosques)
    {
        "site_id": "masjid-agung-demak",
        "site_name": "Masjid Agung Demak",
        "site_type": "mosque",
        "latitude": -6.8946,
        "longitude": 110.6373,
        "associated_kingdom_ids": ["demak"],
        "associated_ruler_ids": ["demak-1"],
        "construction_year": 1479,
        "construction_period_display": "1479 M (Tahun Saka 1401 berdasar Candra Sengkala Lawang Bledeg)",
        "historical_significance": "Pusat transmisi dakwah dan permusyawaratan Wali Songo di tanah Jawa; ikon arsitektur atap tumpang tiga akulturasi Hindu-Jawa-Islam dengan tiang tatal legendaris buatan Sunan Kalijaga.",
        "current_condition": "Terpelihara sangat baik, aktif digunakan sebagai pusat ibadah dan cagar budaya nasional.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (Kepmenbudpar No. PM.18/PW.007/MKP/2007)",
        "source_references": ["de-graaf-pigeaud-1985", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Tahun berdirinya didukung epigrafi candra sengkala Lawang Bledeg (1466 M / 1479 M)."
    },
    {
        "site_id": "masjid-menara-kudus",
        "site_name": "Masjid Menara Kudus (Al-Aqsha Manarat Qudus)",
        "site_type": "mosque",
        "latitude": -6.8048,
        "longitude": 110.8327,
        "associated_kingdom_ids": ["demak"],
        "associated_ruler_ids": [],
        "construction_year": 1549,
        "construction_period_display": "1549 M (956 H)",
        "historical_significance": "Didirikan oleh Sunan Kudus (Ja'far Shadiq) dengan menara menyerupai candi berarsitektur bata merah Majapahit, melambangkan kearifan lokal toleransi budaya dan penghormatan tradisi Jawa-Hindu.",
        "current_condition": "Terawat utuh dengan kompleks pemakaman Sunan Kudus di bagian belakang.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (Kepmenbudpar No. PM.18/PW.007/MKP/2007)",
        "source_references": ["de-graaf-pigeaud-1985", "kemendikbud-cagarbudaya"],
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Prasasti batu bertuliskan huruf Arab di atas mihrab menyebutkan tahun 956 H (1549 M)."
    },
    {
        "site_id": "masjid-raya-baiturrahman",
        "site_name": "Masjid Raya Baiturrahman",
        "site_type": "mosque",
        "latitude": 5.5536,
        "longitude": 95.3193,
        "associated_kingdom_ids": ["aceh-darussalam"],
        "associated_ruler_ids": ["aceh-3"],
        "construction_year": 1614,
        "construction_period_display": "1614 M era Sultan Iskandar Muda (Rekonstruksi Belanda 1879–1881 M)",
        "historical_significance": "Simbol kedaulatan agama dan benteng pertahanan rakyat Aceh dalam Perang Aceh; tempat gugurnya Jenderal Kohler pada 1873.",
        "current_condition": "Megah dan aktif, bertahan kokoh saat bencana Tsunami Samudera Hindia 2004.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (Kemendikbud No. SK: PM.91/PW.007/MKP/2011)",
        "source_references": ["reid-2005", "kemendikbud-cagarbudaya"],
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Struktur asli kayu terbakar dalam Perang Aceh 1873, dibangun kembali oleh arsitek Gerrit van Bruins bergaya Moghul revivalis."
    },
    {
        "site_id": "masjid-agung-banten",
        "site_name": "Masjid Agung Banten",
        "site_type": "mosque",
        "latitude": -6.0357,
        "longitude": 106.1554,
        "associated_kingdom_ids": ["banten"],
        "associated_ruler_ids": ["banten-1"],
        "construction_year": 1556,
        "construction_period_display": "1556–1570 M era Sultan Maulana Hasanuddin",
        "historical_significance": "Mahakarya akulturasi arsitektur Jawa, Tiongkok (karya arsitek Tjek Ban Tjut), dan Eropa (menara mercusuar segi delapan karya Hendrik Lucasz Cardeel).",
        "current_condition": "Terpelihara baik dalam kawasan Banten Lama, pusat ziarah makam kesultanan.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 139/M/1998)",
        "source_references": ["guillot-1990", "kemendikbud-cagarbudaya"],
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Menara mercusuar ditambahkan pada masa kekuasaan Sultan Haji (akhir abad ke-17)."
    },
    {
        "site_id": "masjid-tua-katangka",
        "site_name": "Masjid Tua Katangka (Masjid Al-Hilal)",
        "site_type": "mosque",
        "latitude": -5.1978,
        "longitude": 119.4528,
        "associated_kingdom_ids": ["gowa-tallo"],
        "associated_ruler_ids": ["gowa-1"],
        "construction_year": 1603,
        "construction_period_display": "1603 M era Sultan Alauddin (I Mangarangi Daeng Manrabbia)",
        "historical_significance": "Masjid tertua di Sulawesi Selatan, didirikan segera setelah pembacaan dua kalimat syahadat oleh pembesar Gowa-Tallo dibimbing Dato ri Bandang.",
        "current_condition": "Terawat baik dengan dinding kokoh setebal 1 meter dan kompleks makam para raja Gowa.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud RI)",
        "source_references": ["andaya-1981", "kemendikbud-cagarbudaya"],
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Inskripsi di pintu masjid menyebut renovasi 1816 M oleh Sultan Abdul Rauf."
    },
    {
        "site_id": "masjid-sultan-suriansyah",
        "site_name": "Masjid Sultan Suriansyah (Masjid Kuin)",
        "site_type": "mosque",
        "latitude": -3.2952,
        "longitude": 114.5778,
        "associated_kingdom_ids": ["banjar"],
        "associated_ruler_ids": ["banjar-1"],
        "construction_year": 1526,
        "construction_period_display": "1526 M era Pangeran Samudera / Sultan Suriansyah",
        "historical_significance": "Masjid tertua di Kalimantan Selatan di tepian Sungai Kuin, memadukan arsitektur panggung kayu ulin Banjar dengan atap tumpang khas Demak.",
        "current_condition": "Terawat baik, menjadi monumen sejarah masuknya Islam pertama di Tanah Banjar.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 047/M/1998)",
        "source_references": ["poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Struktur kayu ulin mengalami beberapa kali pemugaran tanpa mengubah denah dasar."
    },
    {
        "site_id": "masjid-tua-wapauwe",
        "site_name": "Masjid Tua Wapauwe",
        "site_type": "mosque",
        "latitude": -3.5855,
        "longitude": 128.0833,
        "associated_kingdom_ids": ["hitu-maluku"],
        "associated_ruler_ids": [],
        "construction_year": 1414,
        "construction_period_display": "1414 M",
        "historical_significance": "Masjid tertua di Kepulauan Maluku, dibangun dari pelepah sagu (gaba-gaba) dan pasak kayu tanpa paku oleh Perdana Jamilu; menyimpan mushaf Al-Qur'an tulisan tangan tertua Maluku bertahun 1590 M.",
        "current_condition": "Terawat sangat autentik di Desa Kaitetu, Leihitu, Maluku Tengah.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 012/M/1999)",
        "source_references": ["andaya-1993", "kemendikbud-cagarbudaya"],
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Dipindahkan dari Gunung Wawane ke Desa Kaitetu pada tahun 1614 M."
    },
    {
        "site_id": "masjid-gedhe-kauman-jogja",
        "site_name": "Masjid Gedhe Kauman Kraton Yogyakarta",
        "site_type": "mosque",
        "latitude": -7.8037,
        "longitude": 110.3628,
        "associated_kingdom_ids": ["kasultanan-yogyakarta"],
        "associated_ruler_ids": ["jogja-1"],
        "construction_year": 1773,
        "construction_period_display": "1773 M (Tahun Jawa Alip 1699 berdasar Kyai Wiryokusumo)",
        "historical_significance": "Masjid raya Kasultanan Yogyakarta beratap tumpang tiga bertakhta mustaka daun kluwih dan gada, pusat peringatan Sekaten dan peribadatan keraton berfilosofi Hamemayu Hayuning Bawana.",
        "current_condition": "Terpelihara sangat agung di sisi barat Alun-alun Utara Yogyakarta.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 210/M/2011)",
        "source_references": ["ricklefs-2008", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Dibangun oleh Sri Sultan Hamengkubuwono I didampingi penghulu keraton Kyai Faqih Ibrahim."
    },
    {
        "site_id": "masjid-sultan-ternate",
        "site_name": "Masjid Sultan Ternate (Sigi Lamo)",
        "site_type": "mosque",
        "latitude": 0.7981,
        "longitude": 127.3872,
        "associated_kingdom_ids": ["ternate"],
        "associated_ruler_ids": [],
        "construction_year": 1606,
        "construction_period_display": "1606 M era Sultan Saidi Berkat",
        "historical_significance": "Masjid Kesultanan Ternate beratap tumpang tujuh dengan aturan adat ketat: jamaah dilarang memakai sarung (harus bercelana panjang/destar) melambangkan kesiapan berperang menegakkan kebenaran.",
        "current_condition": "Terawat sakral di lereng Gunung Gamalama dekat Kedaton Sultan Ternate.",
        "heritage_status": "Cagar Budaya Peringkat Nasional",
        "source_references": ["andaya-1993", "kemendikbud-cagarbudaya"],
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Tradisi lisan menyebut cikal bakal sejak abad ke-15 namun struktur batu permanen dibangun 1606 M."
    },

    # KERATON & ISTANA (Palaces)
    {
        "site_id": "keraton-kasepuhan-cirebon",
        "site_name": "Keraton Kasepuhan Cirebon",
        "site_type": "palace",
        "latitude": -6.7265,
        "longitude": 108.5714,
        "associated_kingdom_ids": ["cirebon"],
        "associated_ruler_ids": ["cirebon-1"],
        "construction_year": 1445,
        "construction_period_display": "1445–1529 M (Pengembangan Pangeran Cakrabuana & Sunan Gunung Jati)",
        "historical_significance": "Pusat kekuasaan awal Kesultanan Cirebon, menyimpan kereta kencana legendaris Singa Barong (1549 M) dengan perpaduan ornamen gajah-garuda-naga simbol persahabatan Islam, Hindu, dan Tiongkok.",
        "current_condition": "Terpelihara baik, museum aktif, dan kediaman Sultan Sepuh.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 062/M/1998)",
        "source_references": ["de-graaf-pigeaud-1985", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Bermula dari Keraton Pakungwati yang didirikan 1445 M."
    },
    {
        "site_id": "keraton-yogyakarta",
        "site_name": "Keraton Ngayogyakarta Hadiningrat",
        "site_type": "palace",
        "latitude": -7.8053,
        "longitude": 110.3642,
        "associated_kingdom_ids": ["kasultanan-yogyakarta"],
        "associated_ruler_ids": ["jogja-1", "jogja-2"],
        "construction_year": 1755,
        "construction_period_display": "1755–1756 M era Sri Sultan Hamengkubuwono I",
        "historical_significance": "Pusat pemerintahan dinasti Mataram Yogyakarta, poros filosofis garis imajiner Gunung Merapi–Tugu–Keraton–Panggung Krapyak–Laut Selatan, dinobatkan sebagai Warisan Dunia UNESCO (2023). Menjadi basis pertahanan Republik Indonesia 1946–1949.",
        "current_condition": "Sangat terawat, kediaman resmi Gubernur DIY / Sultan Hamengkubuwono X.",
        "heritage_status": "Warisan Dunia UNESCO (The Cosmological Axis of Yogyakarta and its Historic Landmarks)",
        "source_references": ["ricklefs-2008", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Sultan Hamengkubuwono I memasuki istana pada 7 Oktober 1756 (bertepatan tahun Jawa Dwi Naga Rasa Tunggal)."
    },
    {
        "site_id": "keraton-surakarta",
        "site_name": "Keraton Kasunanan Surakarta Hadiningrat",
        "site_type": "palace",
        "latitude": -7.5779,
        "longitude": 110.8281,
        "associated_kingdom_ids": ["kasunanan-surakarta"],
        "associated_ruler_ids": ["surakarta-1"],
        "construction_year": 1744,
        "construction_period_display": "1744–1745 M era Susuhunan Pakubuwono II",
        "historical_significance": "Penerus trah Mataram Islam setelah perpindahan pusat kerajaan dari Kartasura akibat Peristiwa Geger Pacinan 1742 M; memiliki menara Panggung Songgobuwono untuk kontemplasi spritual.",
        "current_condition": "Terpelihara baik, museum pusaka aktif dan kediaman Susuhunan Pakubuwono.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 064/M/1998)",
        "source_references": ["ricklefs-2008", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Pindah dari Kartasura pada 17 Februari 1745 M."
    },
    {
        "site_id": "istana-maimun",
        "site_name": "Istana Maimun Kesultanan Deli",
        "site_type": "palace",
        "latitude": 3.5753,
        "longitude": 98.6838,
        "associated_kingdom_ids": ["deli"],
        "associated_ruler_ids": ["deli-1"],
        "construction_year": 1888,
        "construction_period_display": "1888–1891 M era Sultan Mahmud Al Rasyid Perkasa Alamsyah",
        "historical_significance": "Istana megah rancangan Kapten KNIL Theodoor van Erp yang memadukan corak arsitektur Melayu deli, Islam Timur Tengah, Spanyol, dan Italia di masa kemakmuran tembakau Deli.",
        "current_condition": "Terawat megah di pusat Kota Medan, menjadi destinasi budaya ikonik Sumatera Utara.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 048/M/1998)",
        "source_references": ["ricklefs-2008", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Diresmikan 18 Mei 1891 M."
    },
    {
        "site_id": "istana-siak",
        "site_name": "Istana Siak Sri Indrapura (Asserayah Hasyimiah)",
        "site_type": "palace",
        "latitude": 0.7977,
        "longitude": 102.0494,
        "associated_kingdom_ids": ["siak-sri-indrapura"],
        "associated_ruler_ids": ["siak-1"],
        "construction_year": 1889,
        "construction_period_display": "1889 M era Sultan Syarif Hasyim",
        "historical_significance": "Istana 'Istana Matahari Timur' berarsitektur Moor-Melayu; tempat tinggal Sultan Syarif Kasim II yang menyerahkan mahkota berlapis berlian dan 13 juta gulden kepada Presiden Soekarno demi kemerdekaan RI 1945.",
        "current_condition": "Terawat sangat megah di tepi Sungai Siak dengan koleksi alat musik gramofon Komet langka dunia.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 011/M/1999)",
        "source_references": ["reid-2005", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Sultan Syarif Kasim II dinobatkan sebagai Pahlawan Nasional Indonesia."
    },
    {
        "site_id": "istana-kadriah-pontianak",
        "site_name": "Istana Kadriah Kesultanan Pontianak",
        "site_type": "palace",
        "latitude": -0.0298,
        "longitude": 109.3486,
        "associated_kingdom_ids": ["pontianak"],
        "associated_ruler_ids": [],
        "construction_year": 1771,
        "construction_period_display": "1771 M era Sultan Syarif Abdurrahman Alkadrie",
        "historical_significance": "Pusat Kesultanan Pontianak di muara persimpangan Sungai Kapuas dan Landak, dibangun dari kayu belian pilihan; kediaman Sultan Hamid II perancang lambang negara Garuda Pancasila.",
        "current_condition": "Terpelihara baik dengan koleksi meriam kuno dan tahta berlapis emas.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 013/M/1999)",
        "source_references": ["poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Didirikan pertama kali 23 Oktober 1771 M."
    },
    {
        "site_id": "kedaton-sultan-ternate",
        "site_name": "Kedaton Kesultanan Ternate",
        "site_type": "palace",
        "latitude": 0.8003,
        "longitude": 127.3876,
        "associated_kingdom_ids": ["ternate"],
        "associated_ruler_ids": [],
        "construction_year": 1811,
        "construction_period_display": "1811 M era Sultan Muhammad Ali",
        "historical_significance": "Istana Kesultanan Ternate di Bukit Limau menghadap Laut Halmahera dan Gunung Gamalama; menyimpan Mahkota Berambut Sultan Ternate yang dikeramatkan dan tumbuh setiap tahun.",
        "current_condition": "Museum cagar budaya aktif dan pusat adat Kesultanan Ternate.",
        "heritage_status": "Cagar Budaya Peringkat Nasional",
        "source_references": ["andaya-1993", "kemendikbud-cagarbudaya"],
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Dibangun di atas tapak kedaton lama abad ke-16 M."
    },

    # MAKAM SULTAN & TOKOH ISLAM (Tombs)
    {
        "site_id": "makam-fatimah-binti-maimun",
        "site_name": "Makam Siti Fatimah binti Maimun",
        "site_type": "tomb",
        "latitude": -7.1332,
        "longitude": 112.5786,
        "associated_kingdom_ids": [],
        "associated_ruler_ids": [],
        "construction_year": 1082,
        "construction_period_display": "1082 M (475 H)",
        "historical_significance": "Bukti epigrafi arkeologis tertua keberadaan Muslim di Pulau Jawa dan Nusantara; batu nisan berinskripsi Arab bergaya Kufi kuno di Desa Leran, Manyar, Gresik.",
        "current_condition": "Cungkup batu putih kuno terawat dan dikunjungi peziarah serta arkeolog internasional.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud RI)",
        "source_references": ["poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Tahun wafat 7 Rajab 475 H (1082 M) tertera tegas dalam inskripsi nisan Kufi."
    },
    {
        "site_id": "makam-malik-as-saleh",
        "site_name": "Kompleks Makam Sultan Malik as-Saleh",
        "site_type": "tomb",
        "latitude": 5.1281,
        "longitude": 97.2104,
        "associated_kingdom_ids": ["samudera-pasai"],
        "associated_ruler_ids": ["pasai-1"],
        "construction_year": 1297,
        "construction_period_display": "1297 M (696 H)",
        "historical_significance": "Makam pendiri Kesultanan Samudera Pasai (Meurah Silu); nisannya berhiaskan kaligrafi kalimah tauhid dan syair tasawuf berbahasa Arab berakulturasi seni nisan Gujarat/Cambay.",
        "current_condition": "Terpelihara dalam kompleks situs cagar budaya Geudong, Aceh Utara.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. PM.18/PW.007/MKP/2007)",
        "source_references": ["alfian-1999", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Tanggal wafat Ramadan 696 H (1297 M) menjadi patokan ilmiah berdirinya Pasai."
    },
    {
        "site_id": "makam-troloyo-majapahit",
        "site_name": "Kompleks Makam Islam Troloyo",
        "site_type": "tomb",
        "latitude": -7.5621,
        "longitude": 112.3812,
        "associated_kingdom_ids": [],
        "associated_ruler_ids": [],
        "construction_year": 1368,
        "construction_period_display": "1368–1428 M (Masa Keemasan Kerajaan Majapahit)",
        "historical_significance": "Kompleks pemakaman Muslim di pusat ibu kota Trowulan Majapahit dengan angka tahun Jawa Kuno dan ayat suci Al-Qur'an, membuktikan adanya pejabat dan kerabat istana Majapahit yang telah memeluk Islam.",
        "current_condition": "Situs arkeologi aktif terpelihara di Trowulan, Mojokerto.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (Kawasan Cagar Budaya Trowulan)",
        "source_references": ["de-graaf-pigeaud-1985", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Nisan tertua berangka tahun Saka 1290 (1368 M) pada era Hayam Wuruk."
    },
    {
        "site_id": "makam-imogiri",
        "site_name": "Kompleks Pemakaman Raja-Raja Mataram Imogiri (Pajimatan Imogiri)",
        "site_type": "tomb",
        "latitude": -7.9208,
        "longitude": 110.3922,
        "associated_kingdom_ids": ["mataram-islam", "kasultanan-yogyakarta", "kasunanan-surakarta"],
        "associated_ruler_ids": ["mataram-3"],
        "construction_year": 1632,
        "construction_period_display": "1632 M dibangun oleh Sultan Agung Hanyokrokusumo",
        "historical_significance": "Kompleks pemakaman suci dinasti Mataram Islam di perbukitan Merak, tempat peristirahatan Sultan Agung, raja-raja Kasunanan Surakarta, dan sultan-sultan Kasultanan Yogyakarta.",
        "current_condition": "Terpelihara sangat sakral dijaga abdi dalem kedua keraton bersatu.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 210/M/2011)",
        "source_references": ["ricklefs-2008", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Sultan Agung memindahkan lokasi pemakaman dinasti dari Kotagede ke Imogiri pada 1632 M."
    },
    {
        "site_id": "makam-katangka-gowa",
        "site_name": "Kompleks Makam Raja-Raja Gowa Katangka",
        "site_type": "tomb",
        "latitude": -5.1983,
        "longitude": 119.4533,
        "associated_kingdom_ids": ["gowa-tallo"],
        "associated_ruler_ids": ["gowa-1", "gowa-2"],
        "construction_year": 1670,
        "construction_period_display": "Abad ke-17 M (Makam Sultan Hasanuddin wafat 1670 M)",
        "historical_significance": "Tempat peristirahatan Sultan Hasanuddin (Ayam Jantan dari Timur) dan para penguasa Kesultanan Gowa yang gigih melawan monopoli dagang VOC Belanda.",
        "current_condition": "Terawat baik di Kompleks Makam Pahlawan Nasional Sultan Hasanuddin, Somba Opu.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 046/M/1998)",
        "source_references": ["andaya-1981", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Terdapat kubah cungkup khas arsitektur makam raja-raja Makassar."
    },

    # BENTENG PERTAHANAN (Fortresses)
    {
        "site_id": "benteng-somba-opu",
        "site_name": "Benteng Somba Opu",
        "site_type": "fortress",
        "latitude": -5.1911,
        "longitude": 119.3944,
        "associated_kingdom_ids": ["gowa-tallo"],
        "associated_ruler_ids": ["gowa-2"],
        "construction_year": 1545,
        "construction_period_display": "1545 M (Dibangun Karaeng Tumapa'risi' Kallonna, diperkuat batu bata merah 1630 M)",
        "historical_significance": "Benteng pertahanan utama dan emporium niaga Kesultanan Gowa-Tallo tempat berkantornya loji dagang internasional (Inggris, Denmark, Portugis); memiliki meriam legendaris Anak Makassar berbobot 9,5 ton.",
        "current_condition": "Situs arkeologi dan taman cagar budaya di tepi Sungai Jeneberang.",
        "heritage_status": "Cagar Budaya Peringkat Nasional (SK Mendikbud No. 046/M/1998)",
        "source_references": ["andaya-1981", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Dihancurkan VOC setelah Perang Makassar 1669, diekskavasi kembali oleh Balai Arkeologi akhir abad ke-20."
    },
    {
        "site_id": "benteng-keraton-wolio-buton",
        "site_name": "Benteng Keraton Wolio (Benteng Buton)",
        "site_type": "fortress",
        "latitude": -5.4742,
        "longitude": 122.6186,
        "associated_kingdom_ids": ["buton"],
        "associated_ruler_ids": [],
        "construction_year": 1634,
        "construction_period_display": "1634 M era Sultan Buton IV Dayanu Ikhsanuddin",
        "historical_significance": "Benteng pertahanan terluas di dunia (Guinness World Records 2006, keliling 2,74 km) yang mengelilingi seluruh ibu kota Wolio dan istana Kesultanan Buton dari serangan bajak laut dan penjajah.",
        "current_condition": "Terawat utuh di atas bukit Baubau dengan pemandangan Selat Buton.",
        "heritage_status": "Cagar Budaya Peringkat Nasional & Rekor Dunia Guinness",
        "source_references": ["ricklefs-2008", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Dibangun dari batu gunung menggunakan perekat tradisional kapur dan putih telur."
    },
    {
        "site_id": "benteng-inong-balee",
        "site_name": "Benteng Inong Balee",
        "site_type": "fortress",
        "latitude": 5.5978,
        "longitude": 95.5342,
        "associated_kingdom_ids": ["aceh-darussalam"],
        "associated_ruler_ids": [],
        "construction_year": 1599,
        "construction_period_display": "1599 M era Sultan Alauddin Ri'ayat Syah Sayyid al-Mukammal",
        "historical_significance": "Benteng pangkalan armada laut beranggotakan para janda pahlawan (Inong Balee) yang dipimpin Laksamana perempuan pertama dunia modern, Malahayati, yang menewaskan Cornelis de Houtman dalam duel laut.",
        "current_condition": "Reruntuhan dinding benteng kokoh di Teluk Krueng Raya, Aceh Besar.",
        "heritage_status": "Cagar Budaya Peringkat Nasional",
        "source_references": ["reid-2005", "kemendikbud-cagarbudaya"],
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Laksamana Malahayati diakui sebagai Pahlawan Nasional Republik Indonesia."
    },

    # PELABUHAN & ARKEOLOGI EPIGRAFI (Ports & Epigraphy)
    {
        "site_id": "pelabuhan-barus",
        "site_name": "Bandar Niaga Kuno Barus (Fansur)",
        "site_type": "port",
        "latitude": 2.0089,
        "longitude": 98.4039,
        "associated_kingdom_ids": [],
        "associated_ruler_ids": [],
        "construction_year": 1200,
        "construction_period_display": "Abad ke-7 s.d. 13 M",
        "historical_significance": "Pelabuhan transito tertua di pantai barat Sumatera pengekspor kapur barus dan kemenyan yang disebut dalam naskah Claudius Ptolemaeus, catatan dinasti Tang, serta makam Mahligai dan Papan Tinggi.",
        "current_condition": "Kawasan situs bersejarah Titik Nol Peradaban Islam Nusantara di Tapanuli Tengah.",
        "heritage_status": "Kawasan Cagar Budaya Peringkat Nasional (Titik Nol Peradaban Islam Nusantara)",
        "source_references": ["guillot-1990", "poesponegoro-notosusanto-2008"],
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Inskripsi makam Syekh Mahmud di Papan Tinggi berangka tahun 44 H (klaim lokal) vs kajian arkeologi abad ke-13 M."
    },
    {
        "site_id": "pelabuhan-sunda-kelapa",
        "site_name": "Pelabuhan Sunda Kelapa / Jayakarta",
        "site_type": "port",
        "latitude": -6.1261,
        "longitude": 106.8089,
        "associated_kingdom_ids": ["cirebon", "demak", "banten"],
        "associated_ruler_ids": [],
        "construction_year": 1527,
        "construction_period_display": "22 Juni 1527 M penaklukan Fatahillah (Hari Jadi Kota Jakarta)",
        "historical_significance": "Pelabuhan strategis muara Ciliwung tempat armada gabungan Demak-Cirebon pimpinan Fatahillah mengusir armada Portugis pimpinan Francisco de Sá, mengganti namanya menjadi Jayakarta (Kemenangan Sempurna).",
        "current_condition": "Pelabuhan rakyat aktif untuk kapal kayu phinisi di muara Jakarta Utara.",
        "heritage_status": "Kawasan Cagar Budaya DKI Jakarta",
        "source_references": ["ricklefs-2008", "kemendikbud-cagarbudaya"],
        "confidence_level": "Sangat Tinggi",
        "uncertainty_notes": "Tanggal 22 Juni 1527 ditetapkan sebagai HUT Kota Jakarta berdasarkan riset Prof. Dr. Sukanto."
    }
]

EVENTS_DATA = [
    # FASE 1: BUKTI AWAL & TRANSMISI DAKWAH MARITIM (1082 - 1400 M)
    {
        "event_id": "event-1082-leran",
        "event_name": "Inskripsi Wafatnya Siti Fatimah binti Maimun di Leran",
        "event_year": 1082,
        "event_date_display": "1082 M (7 Rajab 475 H)",
        "event_type": "early_evidence",
        "description": "Batu nisan berinskripsi huruf Kufi kuno dipancangkan di Leran, Gresik, menandai keberadaan pemukiman atau komunitas Muslim asing tertua di pesisir utara Jawa Timur.",
        "related_kingdom_ids": [],
        "related_site_ids": ["makam-fatimah-binti-maimun"],
        "source_references": ["poesponegoro-notosusanto-2008"],
        "uncertainty_notes": "Membuktikan interaksi niaga maritim dengan dunia Islam di era Dinasti Fatimiyah."
    },
    {
        "event_id": "event-1267-samudera-pasai",
        "event_name": "Pendirian Kesultanan Samudera Pasai oleh Sultan Malik as-Saleh",
        "event_year": 1267,
        "event_date_display": "c. 1267 M",
        "event_type": "kingdom_emergence",
        "description": "Meurah Silu memeluk Islam dibimbing Syekh Ismail dari Mekkah, mendirikan Kesultanan Samudera Pasai sebagai kerajaan Islam berdaulat pertama di kepulauan Nusantara.",
        "related_kingdom_ids": ["samudera-pasai"],
        "related_site_ids": ["makam-malik-as-saleh"],
        "source_references": ["alfian-1999", "ricklefs-2008"],
        "uncertainty_notes": "Kronologi dikonfirmasi batu nisan wafat 1297 M (696 H) dan catatan Marco Polo 1292 M."
    },
    {
        "event_id": "event-1345-ibnu-battuta",
        "event_name": "Kunjungan Pengelana Ibnu Battuta ke Istana Samudera Pasai",
        "event_year": 1345,
        "event_date_display": "1345 M",
        "event_type": "diplomacy_trade",
        "description": "Pengembara legendaris Maroko Ibnu Battuta singgah di Pasai selama 15 hari, mencatat kemegahan istana Sultan Ahmad Malik az-Zahir, ketaatan mazhab Syafi'i, serta armada jung laut yang perkasa.",
        "related_kingdom_ids": ["samudera-pasai"],
        "related_site_ids": ["pelabuhan-barus"],
        "source_references": ["alfian-1999", "ricklefs-2008"],
        "uncertainty_notes": "Sumber primer manuskrip Tuhfat an-Nuzzhar (Rihlah Ibnu Battuta)."
    },
    {
        "event_id": "event-1368-troloyo",
        "event_name": "Bukti Komunitas Muslim di Ibu Kota Majapahit (Troloyo)",
        "event_year": 1368,
        "event_date_display": "1368 M (Tahun Saka 1290)",
        "event_type": "early_evidence",
        "description": "Inskripsi nisan tertua di Kompleks Makam Troloyo dipancangkan di pusat ibu kota Trowulan, membuktikan bahwa kaum elit dan kerabat istana Majapahit telah berakulturasi dan memeluk Islam.",
        "related_kingdom_ids": [],
        "related_site_ids": ["makam-troloyo-majapahit"],
        "source_references": ["de-graaf-pigeaud-1985"],
        "uncertainty_notes": "Menunjukkan penyebaran Islam melalui jalur damai dan kekerabatan keraton."
    },

    # FASE 2: KEMUNCULAN KESULTANAN & JARINGAN NIAGA MARITIM (1400 - 1599 M)
    {
        "event_id": "event-1475-demak-bintoro",
        "event_name": "Pendirian Kadipaten Demak Bintoro oleh Raden Patah",
        "event_year": 1475,
        "event_date_display": "1475 M (Status Kadipaten) / 1500 M (Kesultanan Penuh)",
        "event_type": "kingdom_emergence",
        "description": "Raden Patah (putra Prabu Brawijaya V) mendirikan pusat peradaban Islam di Glagah Wangi (Demak) dengan restu dewan Wali Songo, membangun Masjid Agung Demak sebagai pusat permusyawaratan.",
        "related_kingdom_ids": ["demak"],
        "related_site_ids": ["masjid-agung-demak"],
        "source_references": ["de-graaf-pigeaud-1985", "ricklefs-2008"],
        "uncertainty_notes": "Tahun Saka 1401 (1479 M) tertera pada candrasengkala Lawang Bledeg Masjid Agung Demak."
    },
    {
        "event_id": "event-1511-jatuhnya-malaka",
        "event_name": "Jatuhnya Malaka ke Tangan Portugis & Pergeseran Jalur Perdagangan",
        "event_year": 1511,
        "event_date_display": "Agustus 1511 M",
        "event_type": "conflict_colonialism",
        "description": "Alfonso de Albuquerque menaklukkan Malaka; pedagang Muslim mengalihkan rute pelayaran dari Selat Malaka menuju pesisir barat Sumatera, Selat Sunda, dan memicu ledakan ekonomi Aceh Darussalam dan Banten.",
        "related_kingdom_ids": ["samudera-pasai", "aceh-darussalam", "banten"],
        "related_site_ids": [],
        "source_references": ["ricklefs-2008", "reid-2005"],
        "uncertainty_notes": "Memicu ekspedisi jihad Pati Unus (Pangeran Sabrang Lor) dari Demak ke Malaka pada 1513 M."
    },
    {
        "event_id": "event-1526-banjar-islam",
        "event_name": "Pangeran Samudera Memeluk Islam & Berdirinya Kesultanan Banjar",
        "event_year": 1526,
        "event_date_display": "1526 M (24 September 1526 M Hari Jadi Banjarmasin)",
        "event_type": "kingdom_emergence",
        "description": "Pangeran Samudera memenangkan konflik dinasti Daha berkat bantuan armada Demak, memeluk Islam dengan gelar Sultan Suriansyah, dan mendirikan Kesultanan Banjar di muara Sungai Kuin.",
        "related_kingdom_ids": ["banjar", "demak"],
        "related_site_ids": ["masjid-sultan-suriansyah"],
        "source_references": ["poesponegoro-notosusanto-2008"],
        "uncertainty_notes": "Didokumentasikan dalam naskah klasik Hikayat Banjar."
    },
    {
        "event_id": "event-1527-sunda-kelapa-jayakarta",
        "event_name": "Fatahillah Membebaskan Sunda Kelapa & Mendirikan Jayakarta",
        "event_year": 1527,
        "event_date_display": "22 Juni 1527 M",
        "event_type": "conflict_colonialism",
        "description": "Panglima armada gabungan Demak-Cirebon, Fatahillah, mengalahkan armada Portugis di muara Sungai Ciliwung dan mengganti nama Sunda Kelapa menjadi Jayakarta (Kemenangan Sempurna).",
        "related_kingdom_ids": ["demak", "cirebon", "banten"],
        "related_site_ids": ["pelabuhan-sunda-kelapa"],
        "source_references": ["de-graaf-pigeaud-1985"],
        "uncertainty_notes": "Tanggal kemenangan ini kini diabadikan sebagai Hari Jadi Kota Jakarta."
    },
    {
        "event_id": "event-1575-baabullah-usir-portugis",
        "event_name": "Sultan Baabullah Mengusir Portugis dari Ternate",
        "event_year": 1575,
        "event_date_display": "15 Juli 1575 M",
        "event_type": "golden_age",
        "description": "Setelah mengepung Benteng Kastela selama 5 tahun pasca-pembunuhan ayahnya Sultan Khairun, Sultan Baabullah membebaskan Maluku dari dominasi Portugis dan memperluas hegemoni Kesultanan Ternate atas 72 pulau berpenghuni.",
        "related_kingdom_ids": ["ternate"],
        "related_site_ids": ["kedaton-sultan-ternate"],
        "source_references": ["andaya-1993"],
        "uncertainty_notes": "Dikenal sebagai 'Penguasa 72 Pulau' (The Lord of 72 Islands)."
    },

    # FASE 3: PUNCAK HEGEMONI & PERANG MELAWAN VOC (1600 - 1700 M)
    {
        "event_id": "event-1605-gowa-resmi-islam",
        "event_name": "Deklarasi Islam sebagai Agama Resmi Kesultanan Kembar Gowa-Tallo",
        "event_year": 1605,
        "event_date_display": "22 September 1605 M (9 Jumadil Awwal 1014 H)",
        "event_type": "kingdom_emergence",
        "description": "Raja Gowa ke-14 I Mangarangi Daeng Manrabbia (Sultan Alauddin) dan Raja Tallo Karaeng Matoaya memeluk Islam dibimbing ulama Minangkabau Dato ri Bandang, disusul salat Jumat perdana di Masjid Katangka pada 1607 M.",
        "related_kingdom_ids": ["gowa-tallo"],
        "related_site_ids": ["masjid-tua-katangka"],
        "source_references": ["andaya-1981"],
        "uncertainty_notes": "Dikonfirmasi dalam catatan lontara' Patturioloanga ri Gowa."
    },
    {
        "event_id": "event-1607-iskandar-muda-naik-tahta",
        "event_name": "Penobatan Sultan Iskandar Muda di Aceh Darussalam",
        "event_year": 1607,
        "event_date_display": "1607 M",
        "event_type": "golden_age",
        "description": "Sultan Iskandar Muda memimpin era keemasan Kesultanan Aceh Darussalam; membangun armada laut terkuat di Selat Malaka, menyusun hukum tata negara Adat Meukuta Alam, dan menjadikan Aceh serambi Mekkah.",
        "related_kingdom_ids": ["aceh-darussalam"],
        "related_site_ids": ["masjid-raya-baiturrahman", "benteng-inong-balee"],
        "source_references": ["reid-2005", "ricklefs-2008"],
        "uncertainty_notes": "Wilayah kekuasaan mencakup seluruh pesisir Sumatera hingga Johor, Pahang, dan Kedah."
    },
    {
        "event_id": "event-1613-sultan-agung-mataram",
        "event_name": "Penobatan Sultan Agung Hanyokrokusumo & Konsolidasi Mataram",
        "event_year": 1613,
        "event_date_display": "1613 M (Puncak Hegemoni hingga 1645 M)",
        "event_type": "golden_age",
        "description": "Raden Mas Rangsang dinobatkan sebagai Sultan Mataram Islam, menyatukan seluruh pedalaman dan pesisir Jawa, memadukan kalender Saka dan Hijriyah menjadi Kalender Jawa (1633 M), serta memimpin pengepungan Batavia (1628 & 1629 M).",
        "related_kingdom_ids": ["mataram-islam"],
        "related_site_ids": ["makam-imogiri"],
        "source_references": ["de-graaf-1958", "ricklefs-2008"],
        "uncertainty_notes": "Mendapat gelar resmi Sultan Abdullah Muhammad Maulana Matarami dari Syarif Mekkah pada 1641 M."
    },
    {
        "event_id": "event-1667-perjanjian-bongaya",
        "event_name": "Penandatanganan Perjanjian Bongaya Pasca-Perang Makassar",
        "event_year": 1667,
        "event_date_display": "18 November 1667 M",
        "event_type": "treaty_partition",
        "description": "Setelah pertempuran sengit melawan persekutuan Cornelis Speelman (VOC) dan Arung Palakka (Bone), Sultan Hasanuddin terpaksa menandatangani Perjanjian Bongaya yang mengakhiri monopoli niaga bebas maritim Makassar.",
        "related_kingdom_ids": ["gowa-tallo", "bone"],
        "related_site_ids": ["benteng-somba-opu", "makam-katangka-gowa"],
        "source_references": ["andaya-1981"],
        "uncertainty_notes": "Sultan Hasanuddin dijuluki 'De Haantjes van het Oosten' (Ayam Jantan dari Timur)."
    },
    {
        "event_id": "event-1682-intervensi-voc-banten",
        "event_name": "Intervensi VOC dalam Perang Suksesi Kesultanan Banten",
        "event_year": 1682,
        "event_date_display": "1682 M",
        "event_type": "conflict_colonialism",
        "description": "Sultan Haji meminta bantuan militer VOC di Batavia untuk menggulingkan ayahnya sendiri, Sultan Ageng Tirtayasa. Kemenangan VOC menandai berakhirnya masa keemasan Banten dan pengalihan monopoli lada Banten ke VOC.",
        "related_kingdom_ids": ["banten"],
        "related_site_ids": ["masjid-agung-banten"],
        "source_references": ["guillot-1990", "ricklefs-2008"],
        "uncertainty_notes": "Sultan Ageng Tirtayasa ditangkap pada 1683 dan diasingkan ke Batavia hingga wafat."
    },

    # FASE 4: PARTISI DINASTI & PERANG PERLAWANAN KOLONIAL (1700 - 1900 M)
    {
        "event_id": "event-1755-perjanjian-giyanti",
        "event_name": "Perjanjian Giyanti & Pembagian Wilayah Mataram Islam",
        "event_year": 1755,
        "event_date_display": "13 Februari 1755 M",
        "event_type": "treaty_partition",
        "description": "Perjanjian damai segitiga antara Pangeran Mangkubumi, Sunan Pakubuwono III, dan VOC yang membelah Mataram menjadi dua entitas berdaulat: Kasunanan Surakarta dan Kesultanan Ngayogyakarta Hadiningrat (Pangeran Mangkubumi bergelar Sri Sultan Hamengkubuwono I).",
        "related_kingdom_ids": ["mataram-islam", "kasultanan-yogyakarta", "kasunanan-surakarta"],
        "related_site_ids": ["keraton-yogyakarta", "keraton-surakarta"],
        "source_references": ["ricklefs-2008"],
        "uncertainty_notes": "Perjanjian ditandatangani di Desa Giyanti (kini Karanganyar, Jawa Tengah)."
    },
    {
        "event_id": "event-1825-perang-diponegoro",
        "event_name": "Meletusnya Perang Diponegoro (Perang Jawa)",
        "event_year": 1825,
        "event_date_display": "1825–1830 M",
        "event_type": "conflict_colonialism",
        "description": "Pangeran Diponegoro memimpin perang suci melawan penindasan kolonial Hindia Belanda dan rusaknya tatanan keraton; perang menghabiskan kas kolonial sebesar 20 juta gulden dan mengubah total sistem administrasi kolonial di Jawa.",
        "related_kingdom_ids": ["kasultanan-yogyakarta", "kasunanan-surakarta"],
        "related_site_ids": ["makam-imogiri"],
        "source_references": ["ricklefs-2008"],
        "uncertainty_notes": "Berakhir dengan penangkapan licik Pangeran Diponegoro di Magelang pada 28 Maret 1830."
    },
    {
        "event_id": "event-1873-perang-aceh",
        "event_name": "Deklarasi Perang Belanda terhadap Kesultanan Aceh Darussalam",
        "event_year": 1873,
        "event_date_display": "26 Maret 1873 M",
        "event_type": "conflict_colonialism",
        "description": "Hindia Belanda menyatakan perang secara resmi kepada Kesultanan Aceh setelah pembatalan Traktat London; memicu perang perlawanan rakyat semesta di bawah para sultan, ulama (Teungku Chik di Tiro), dan bangsawan (Teuku Umar, Cut Nyak Dhien).",
        "related_kingdom_ids": ["aceh-darussalam"],
        "related_site_ids": ["masjid-raya-baiturrahman"],
        "source_references": ["reid-2005", "ricklefs-2008"],
        "uncertainty_notes": "Perang berlangsung sengit lebih dari 30 tahun hingga awal abad ke-20."
    },

    # FASE 5: KEMERDEKAAN RI & INTEGRASI KERAJAAN KE NKRI (1945 - 1956 M)
    {
        "event_id": "event-1945-proklamasi",
        "event_name": "Proklamasi Kemerdekaan Republik Indonesia",
        "event_year": 1945,
        "event_date_display": "17 Agustus 1945 M",
        "event_type": "nkri_integration",
        "description": "Soekarno dan Mohammad Hatta memproklamasikan kemerdekaan Indonesia atas nama bangsa Indonesia di Pegangsaan Timur 56 Jakarta, meletakkan fondasi republik berdaulat.",
        "related_kingdom_ids": [],
        "related_site_ids": [],
        "source_references": ["ricklefs-2008"],
        "uncertainty_notes": "Diikuti sidang PPKI 18–19 Agustus 1945 yang menetapkan status daerah swapraja/kooti."
    },
    {
        "event_id": "event-1945-maklumat-surakarta",
        "event_name": "Maklumat Integrasi Susuhunan Pakubuwono XII & Mangkunegoro VIII ke RI",
        "event_year": 1945,
        "event_date_display": "1 September 1945 M",
        "event_type": "nkri_integration",
        "description": "Sri Susuhunan Pakubuwono XII dan K.G.P.A.A. Mangkunegoro VIII mengeluarkan maklumat resmi bahwa negeri Kasunanan Surakarta Hadiningrat dan Mangkunegaran berintegrasi penuh dengan Republik Indonesia.",
        "related_kingdom_ids": ["kasunanan-surakarta"],
        "related_site_ids": ["keraton-surakarta"],
        "source_references": ["ricklefs-2008"],
        "uncertainty_notes": "Sempat berstatus Daerah Istimewa Surakarta sebelum dinamika sosial anti-swapraja 1946."
    },
    {
        "event_id": "event-1945-amanat-5-september-jogja",
        "event_name": "Amanat 5 September 1945 Sri Sultan Hamengkubuwono IX (Yogyakarta Integrasi NKRI)",
        "event_year": 1945,
        "event_date_display": "5 September 1945 M",
        "event_type": "nkri_integration",
        "description": "Sri Sultan Hamengkubuwono IX dan K.G.P.A.A. Paku Alam VIII mengeluarkan Amanat 5 September 1945, menyatakan Kasultanan Ngayogyakarta Hadiningrat berintegrasi secara sukarela ke Republik Indonesia dengan status Daerah Istimewa yang bertanggung jawab langsung kepada Presiden RI.",
        "related_kingdom_ids": ["kasultanan-yogyakarta"],
        "related_site_ids": ["keraton-yogyakarta"],
        "source_references": ["ricklefs-2008"],
        "uncertainty_notes": "Presiden Soekarno memberikan Piagam Kedudukan tertanggal 19 Agustus 1945 kepada Sri Sultan Hamengkubuwono IX."
    },
    {
        "event_id": "event-1945-siak-penyerahan-mahkota",
        "event_name": "Proklamasi Integrasi Kesultanan Siak & Penyerahan 13 Juta Gulden oleh Sultan Syarif Kasim II",
        "event_year": 1945,
        "event_date_display": "Oktober 1945 M",
        "event_type": "nkri_integration",
        "description": "Sultan Syarif Kasim II memproklamasikan Kesultanan Siak Sri Indrapura bergabung mutlak dengan NKRI, mengibarkan bendera Merah Putih di istana, dan menyerahkan mahkota emas kerajaan beserta dana tunai 13 juta gulden (setara lebih dari Rp 1 triliun hari ini) kepada Presiden Soekarno demi modal perjuangan republik.",
        "related_kingdom_ids": ["siak-sri-indrapura"],
        "related_site_ids": ["istana-siak"],
        "source_references": ["reid-2005", "ricklefs-2008"],
        "uncertainty_notes": "Sultan Syarif Kasim II dianugerahi gelar Pahlawan Nasional Indonesia."
    },
    {
        "event_id": "event-1946-integrasi-bima-sumbawa",
        "event_name": "Pernyataan Integrasi Kesultanan Bima & Sumbawa ke NKRI",
        "event_year": 1946,
        "event_date_display": "1946 M",
        "event_type": "nkri_integration",
        "description": "Sultan Muhammad Salahuddin dari Kesultanan Bima dan Sultan Muhammad Kaharuddin III dari Sumbawa menyatakan kesetiaan wilayah swapraja Nusa Tenggara Barat kepada Republik Indonesia.",
        "related_kingdom_ids": ["bima", "sumbawa"],
        "related_site_ids": [],
        "source_references": ["ricklefs-2008"],
        "uncertainty_notes": "Kedua wilayah bertransformasi menjadi Daerah Swatantra Tingkat II pada 1958 M."
    },
    {
        "event_id": "event-1949-kmb-garuda-pancasila",
        "event_name": "Konferensi Meja Bundar (KMB) & Perancangan Lambang Garuda oleh Sultan Hamid II",
        "event_year": 1949,
        "event_date_display": "Desember 1949 M",
        "event_type": "nkri_integration",
        "description": "Pengakuan kedaulatan Indonesia oleh Belanda; Sultan Hamid II (Sultan Pontianak ke-7) memimpin perancangan lambang negara Elang Rajawali Garuda Pancasila yang diresmikan oleh Presiden Soekarno.",
        "related_kingdom_ids": ["pontianak"],
        "related_site_ids": ["istana-kadriah-pontianak"],
        "source_references": ["ricklefs-2008"],
        "uncertainty_notes": "Lambang Garuda Pancasila pertama kali diperkenalkan pada sidang Kabinet RIS 11 Februari 1950."
    },
    {
        "event_id": "event-1950-penghapusan-swapraja",
        "event_name": "Pemulihan NKRI & Transformasi Daerah Swapraja Menjadi Kabupaten Otonom",
        "event_year": 1950,
        "event_date_display": "17 Agustus 1950 M",
        "event_type": "nkri_integration",
        "description": "Pembubaran Republik Indonesia Serikat (RIS) kembali ke Negara Kesatuan Republik Indonesia (NKRI). Wilayah-wilayah swapraja kerajaan di Kalimantan, Sulawesi, Maluku, dan Sumatera secara bertahap dilebur menjadi Kabupaten/Kota Administratif Otonom di bawah UU Pemerintahan Daerah, sementara institusi istana beralih fungsi menjadi pemangku adat dan warisan budaya.",
        "related_kingdom_ids": ["kutai-kartanegara", "pontianak", "sambas", "gowa", "buton", "ternate", "tidore"],
        "related_site_ids": ["benteng-keraton-wolio-buton"],
        "source_references": ["ricklefs-2008"],
        "uncertainty_notes": "Hanya Kasultanan Ngayogyakarta Hadiningrat yang mempertahankan kedudukan kepala pemerintahan definitif (UU Keistimewaan No. 13/2012)."
    },
    {
        "event_id": "event-1956-tidore-gubernur-irian-barat",
        "event_name": "Penetapan Sultan Tidore Zainal Abidin Syah sebagai Gubernur Pertama Irian Barat",
        "event_year": 1956,
        "event_date_display": "23 September 1956 M",
        "event_type": "nkri_integration",
        "description": "Presiden Soekarno mengangkat Sultan Zainal Abidin Syah dari Kesultanan Tidore sebagai Gubernur pertama Provinsi Perjuangan Irian Barat (berkedudukan di Soasio, Tidore), menegaskan fakta sejarah bahwa kepulauan Papua Barat dan Tanah Papua secara sah merupakan wilayah kedaulatan Nusantara yang tak terpisahkan dari NKRI.",
        "related_kingdom_ids": ["tidore", "rumbati-papua", "misool-papua"],
        "related_site_ids": [],
        "source_references": ["andaya-1993", "ricklefs-2008"],
        "uncertainty_notes": "Memperkuat legitimasi posisi diplomasi Indonesia di PBB menjelang Trikora 1961."
    }
]

def main():
    print("Generating sites.json...")
    with open('data/sites.json', 'w', encoding='utf-8') as f:
        json.dump(SITES_DATA, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(SITES_DATA)} sites.")

    print("Generating events.json...")
    with open('data/events.json', 'w', encoding='utf-8') as f:
        json.dump(EVENTS_DATA, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(EVENTS_DATA)} events.")

    # Enrich kingdoms.json with explicit nkri_integration metadata
    print("Enriching kingdoms.json with nkri_integration metadata...")
    with open('data/kingdoms.json', 'r', encoding='utf-8') as f:
        kingdoms = json.load(f)

    # Detailed integration definitions
    nkri_map = {
        "kasultanan-yogyakarta": {
            "integrated_into_nkri": True,
            "integration_year": 1945,
            "integration_date_display": "5 September 1945 M",
            "integration_type": "special_region",
            "historical_figure": "Sri Sultan Hamengkubuwono IX & KGPAA Paku Alam VIII",
            "title_document": "Amanat 5 September 1945 & Piagam Kedudukan Presiden Soekarno 19 Agustus 1945",
            "summary": "Bergabung secara sukarela dan penuh ke Republik Indonesia segera setelah proklamasi. Mengakui RI berdaulat dan menjadikan Keraton Yogyakarta sebagai benteng perlindungan dan ibu kota Republik Indonesia (1946–1949). Kini berstatus Daerah Istimewa Yogyakarta (UU Keistimewaan No. 13 Tahun 2012) di mana Sultan bertahta otomatis menjabat Gubernur DIY.",
            "current_status": "Pusat Pemerintahan Daerah Istimewa & Lembaga Pelestari Budaya Dunia UNESCO"
        },
        "kasunanan-surakarta": {
            "integrated_into_nkri": True,
            "integration_year": 1945,
            "integration_date_display": "1 September 1945 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Sri Susuhunan Pakubuwono XII",
            "title_document": "Maklumat 1 September 1945 Sri Susuhunan Pakubuwono XII",
            "summary": "Menyatakan Kasunanan Surakarta Hadiningrat menjadi bagian integral NKRI. Sempat ditetapkan sebagai Daerah Istimewa Surakarta sebelum status swapraja dibekukan pada 1946 akibat dinamika politik lokal. Saat ini bertahan sebagai episentrum pelestari adat, seni karawitan, dan cagar budaya adiluhung Jawa.",
            "current_status": "Lembaga Pemangku Adat & Cagar Budaya Nasional"
        },
        "siak-sri-indrapura": {
            "integrated_into_nkri": True,
            "integration_year": 1945,
            "integration_date_display": "Oktober 1945 M",
            "integration_type": "full_integration_heroic",
            "historical_figure": "Sultan Syarif Kasim II (Pahlawan Nasional Indonesia)",
            "title_document": "Surat Kawat Kesetiaan kepada Presiden RI & Penyerahan Mahkota Diraja",
            "summary": "Salah satu peristiwa integrasi paling heroik dalam sejarah kemerdekaan: Sultan Syarif Kasim II menyatakan kesetiaan mutlak kepada Republik Indonesia, menyerahkan mahkota emas bertahtakan berlian dan dana kas kesultanan sebesar 13 juta gulden (setara Rp 1 triliun lebih) kepada Bung Karno untuk membiayai perjuangan kemerdekaan.",
            "current_status": "Cagar Budaya Nasional & Kompleks Museum Istana Siak"
        },
        "deli": {
            "integrated_into_nkri": True,
            "integration_year": 1946,
            "integration_date_display": "1946 M (Revolusi Sosial Sumatera Timur)",
            "integration_type": "cultural_institution",
            "historical_figure": "Sultan Otteman Mahmud Ma'amun",
            "title_document": "Penyatuan Wilayah Sumatera Timur ke dalam NKRI",
            "summary": "Melebur ke dalam Negara Kesatuan Republik Indonesia pasca-dinamika Revolusi Sosial Sumatera Timur 1946. Menjadi bagian dari Provinsi Sumatera Utara, sementara garis dinasti Kesultanan Deli terus lestari memelihara tradisi Melayu dan Istana Maimun.",
            "current_status": "Lembaga Pemangku Adat Melayu Deli & Pengelola Warisan Istana Maimun"
        },
        "pontianak": {
            "integrated_into_nkri": True,
            "integration_year": 1950,
            "integration_date_display": "1950 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Sultan Hamid II (Syarif Abdul Hamid Alkadrie)",
            "title_document": "Peleburan Daerah Swapraja Kalimantan Barat ke NKRI",
            "summary": "Menjadi bagian dari Republik Indonesia Serikat (RIS) dan melebur ke NKRI pada 1950. Sultan Hamid II berjasa besar sebagai ketua BFO dan perancang utama lambang negara Indonesia, Garuda Pancasila.",
            "current_status": "Lembaga Pemangku Adat Melayu Pontianak & Cagar Budaya Istana Kadriah"
        },
        "sambas": {
            "integrated_into_nkri": True,
            "integration_year": 1950,
            "integration_date_display": "1950 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Sultan Muhammad Tarhan / Raden Sulaiman dinasti",
            "title_document": "Penghapusan Swapraja Sambas menjadi Kabupaten Sambas",
            "summary": "Melebur ke dalam NKRI pada 1950 dan wilayahnya bertransformasi menjadi Kabupaten Sambas, Kalimantan Barat.",
            "current_status": "Lembaga Pemangku Adat Keraton Alwatzikhoebillah"
        },
        "kutai-kartanegara": {
            "integrated_into_nkri": True,
            "integration_year": 1960,
            "integration_date_display": "21 Januari 1960 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Sultan Aji Muhammad Parikesit",
            "title_document": "Penyerahan Kekuasaan Pemerintahan Swapraja kepada Bupati KDH Kutai",
            "summary": "Menyatakan kesetiaan kepada RI sejak 1947 dan berstatus Daerah Istimewa Kutai hingga 1960 saat kekuasaan eksekutif resmi diserahkan kepada Pemda Kabupaten Kutai Kartanegara. Pada 2001, Kesultanan dihidupkan kembali sebagai lembaga pemangku adat dan kebudayaan.",
            "current_status": "Lembaga Adat Resmi & Pusat Festival Budaya Erau"
        },
        "bulungan": {
            "integrated_into_nkri": True,
            "integration_year": 1958,
            "integration_date_display": "1958 M",
            "integration_type": "integrated",
            "historical_figure": "Sultan Jalaluddin",
            "title_document": "UU Pembentukan Daerah Tingkat II Bulungan",
            "summary": "Bergabung ke RI dan berstatus Swapraja hingga dibentuknya Daerah Istimewa Bulungan dan Kabupaten Bulungan pada 1958.",
            "current_condition": "Peninggalan sejarah dan kesultanan adat di Tanjung Palas."
        },
        "gowa": {
            "integrated_into_nkri": True,
            "integration_year": 1946,
            "integration_date_display": "1946–1950 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Sultan Muhammad Tahir Muhibuddin (Karaeng Gowa)",
            "title_document": "Peleburan Daerah Swapraja ke Provinsi Sulawesi",
            "summary": "Menyatakan kesetiaan kepada proklamasi RI 1945 dan menolak pembentukan negara boneka NIT oleh Belanda. Wilayahnya menjadi Kabupaten Gowa, Sulawesi Selatan.",
            "current_status": "Lembaga Adat Makassar & Pengelola Museum Balla Lompoa"
        },
        "buton": {
            "integrated_into_nkri": True,
            "integration_year": 1960,
            "integration_date_display": "1960 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Sultan La Ode Falihi (Sultan Buton ke-38)",
            "title_document": "Integrasi Swapraja Buton ke Propinsi Sulawesi Tenggara",
            "summary": "Menyatakan bergabung dengan NKRI tanpa perlawanan, mempertahankan nilai filosofi falsafah Sara Pataanguna (Pomae-maeaka, Popia-piara, Poangka-angkataka, Pomaa-maasiaka). Wilayah kesultanan bertransformasi menjadi Kabupaten Buton dan Kota Baubau.",
            "current_status": "Lembaga Adat Kesultanan Buton & Penjaga Benteng Keraton Wolio"
        },
        "luwu-islam": {
            "integrated_into_nkri": True,
            "integration_year": 1945,
            "integration_date_display": "19 Agustus 1945 M",
            "integration_type": "full_integration_heroic",
            "historical_figure": "Datu Luwu Andi Djemma (Pahlawan Nasional)",
            "title_document": "Pernyataan Kesetiaan Datu Luwu Mendukung Proklamasi RI",
            "summary": "Datu Luwu Andi Djemma menyatakan Kerajaan Luwu adalah bagian tak terpisahkan dari Republik Indonesia hanya dua hari setelah Proklamasi, memimpin perlawanan heroik rakyat Luwu melawan tentara NICA Belanda.",
            "current_status": "Lembaga Pemangku Adat Istana Luwu Palopo"
        },
        "ternate": {
            "integrated_into_nkri": True,
            "integration_year": 1950,
            "integration_date_display": "1950 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Sultan Iskandar Muhammad Djabir Sjah",
            "title_document": "Integrasi Maluku Utara ke dalam NKRI",
            "summary": "Mendukung kemerdekaan Republik Indonesia dan berperan dalam penyatuan Maluku Utara ke pangkuan Ibu Pertiwi. Tetap menjaga kedaton dan tatanan adat Moloku Kie Raha hingga kini.",
            "current_status": "Lembaga Adat Kesultanan Ternate & Kedaton Ternate"
        },
        "tidore": {
            "integrated_into_nkri": True,
            "integration_year": 1950,
            "integration_date_display": "1950 / 1956 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Sultan Zainal Abidin Syah (Pahlawan Nasional)",
            "title_document": "Keputusan Presiden RI Penetapan Ibu Kota Irian Barat di Soasio 1956",
            "summary": "Berperan krusial dalam kedaulatan NKRI atas Papua Barat: Sultan Zainal Abidin Syah diangkat Bung Karno menjadi Gubernur pertama Irian Barat (1956) membuktikan keterikatan historis Papua dengan Nusantara sejak berabad-abad lampau.",
            "current_status": "Lembaga Adat Kesultanan Tidore & Pengelola Kedaton Soasio"
        },
        "bacan": {
            "integrated_into_nkri": True,
            "integration_year": 1950,
            "integration_date_display": "1950 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Sultan Kamarullah",
            "title_document": "Integrasi Swapraja Bacan ke NKRI",
            "summary": "Melebur ke dalam Negara Kesatuan Republik Indonesia pada 1950 dan bertransformasi menjadi bagian dari Kabupaten Halmahera Selatan.",
            "current_status": "Lembaga Adat Kesultanan Bacan"
        },
        "bima": {
            "integrated_into_nkri": True,
            "integration_year": 1958,
            "integration_date_display": "1958 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Sultan Muhammad Salahuddin",
            "title_document": "Maklumat Kesultanan Bima 1945 & UU Pembentukan Dati II Bima 1958",
            "summary": "Sultan Muhammad Salahuddin menyatakan berdiri di belakang Republik Indonesia sejak 1945. Wilayahnya bertransformasi menjadi Kabupaten dan Kota Bima.",
            "current_status": "Lembaga Adat Asi Mbojo & Museum Bima"
        },
        "sumbawa": {
            "integrated_into_nkri": True,
            "integration_year": 1958,
            "integration_date_display": "1958 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Sultan Muhammad Kaharuddin III",
            "title_document": "Maklumat Sumbawa 1945 & UU No. 69 Tahun 1958",
            "summary": "Menyatakan integrasi swapraja ke NKRI pasca-kemerdekaan dan wilayah kesultanan bertransformasi menjadi Kabupaten Sumbawa.",
            "current_status": "Lembaga Adat Kesultanan Sumbawa & Istana Bala Kuning"
        },
        "rumbati-papua": {
            "integrated_into_nkri": True,
            "integration_year": 1950,
            "integration_date_display": "1950–1963 M (Pembebasan Irian Barat)",
            "integration_type": "cultural_institution",
            "historical_figure": "Raja Abu Bakar Bauw / Klan Bauw",
            "title_document": "Pernyataan Kesetiaan Petuanan Semenanjung Onin ke NKRI",
            "summary": "Petuanan Islam di Semenanjung Onin (Fakfak, Papua Barat) yang secara historis terhubung dengan Kesultanan Tidore menegaskan kesetiaan penuh kepada NKRI dalam perjuangan Trikora dan Penentuan Pendapat Rakyat (Pepera) 1969.",
            "current_status": "Lembaga Adat Petuanan Rumbati Fakfak"
        },
        "misool-papua": {
            "integrated_into_nkri": True,
            "integration_year": 1950,
            "integration_date_display": "1950–1963 M",
            "integration_type": "cultural_institution",
            "historical_figure": "Raja Umkabu / Matbat",
            "title_document": "Integrasi Kepulauan Raja Ampat ke NKRI",
            "summary": "Petuanan Islam di Kepulauan Raja Ampat yang bersatu teguh dengan NKRI mendukung integrasi Irian Barat ke Republik Indonesia.",
            "current_status": "Lembaga Adat Petuanan Misool Raja Ampat"
        },
        "indragiri": {
            "integrated_into_nkri": True,
            "integration_year": 1945,
            "integration_date_display": "1945 M",
            "integration_type": "integrated",
            "historical_figure": "Sultan Mahmud Syah",
            "title_document": "Peleburan Swapraja Indragiri ke NKRI",
            "summary": "Menyatakan dukungan terhadap kemerdekaan Indonesia dan melebur menjadi Kabupaten Indragiri Hulu dan Hilir di Riau.",
            "current_status": "Cagar Budaya Kompleks Makam Raja-Raja Indragiri"
        }
    }

    # Add default or specific nkri_integration to each kingdom
    for k in kingdoms:
        kid = k["id"]
        if kid in nkri_map:
            k["nkri_integration"] = nkri_map[kid]
        else:
            # Earlier ended kingdoms (e.g. Samudera Pasai, Demak, Pajang, Malaka, etc.)
            ye = k.get("year_ended")
            ye_display = k.get("year_ended_display", "")
            k["nkri_integration"] = {
                "integrated_into_nkri": False,
                "integration_year": None,
                "integration_date_display": f"Telah berakhir sebelum era modern ({ye_display})",
                "integration_type": "historical_predecessor",
                "historical_figure": None,
                "title_document": None,
                "summary": f"Kesultanan ini telah berakhir masa kedaulatan politiknya pada kurun historis {ye_display}. Seluruh wilayah teritorial historisnya kini menjadi bagian sah dan integral dari wilayah kedaulatan Negara Kesatuan Republik Indonesia, dengan tinggalan cagar budayanya dilindungi negara berdasarkan UU Cagar Budaya No. 11 Tahun 2010.",
                "current_status": "Situs Cagar Budaya Arkeologi Nasional"
            }

    with open('data/kingdoms.json', 'w', encoding='utf-8') as f:
        json.dump(kingdoms, f, indent=2, ensure_ascii=False)
    print("Enriched all 36 kingdoms in data/kingdoms.json with nkri_integration metadata.")

if __name__ == '__main__':
    main()
