# -*- coding: utf-8 -*-
"""
Historical Data Generator for WebGIS Atlas Sejarah Kerajaan Islam Nusantara
Synthesizes verified academic data based on Ricklefs, Poesponegoro & Notosusanto,
Vlekke, De Graaf & Pigeaud, Reid, Andaya, Guillot, Kemendikbud Cagar Budaya.
"""
import json
import os

kingdoms_data = [
    # ==========================================
    # SUMATERA
    # ==========================================
    {
        "id": "samudera-pasai",
        "name": "Kesultanan Samudera Pasai",
        "alternate_names": ["Samudera Shalihat", "Pasai", "Samudra"],
        "region": "Sumatera",
        "year_founded": 1267,
        "year_founded_display": "c. 1267 M",
        "year_ended": 1521,
        "year_ended_display": "1521 M (Ditaklukkan Portugis & diserap ke Aceh Darussalam 1524 M)",
        "status_timeline_type": "ended",
        "founder": "Meurah Silu (Sultan Malik as-Saleh)",
        "capital_city": "Geudong / Samudera, Aceh Utara",
        "coordinates": {"lat": 5.1278, "lng": 97.2098},
        "golden_age": {
            "start_year": 1350,
            "end_year": 1400,
            "leader": "Sultan Ahmad Malik az-Zahir & Sultan Zainal Abidin I",
            "description": "Menjadi episentrum perdagangan internasional dan transmisi intelektual Islam di Selat Malaka. Mengedarkan mata uang emas murni (Deureuham) dan dikunjungi pengembara Maroko Ibnu Battuta yang mencatat kefasihan sultan dalam fikih Syafi'i."
        },
        "historical_summary": "Kesultanan Samudera Pasai merupakan kerajaan Islam pertama di Nusantara yang terbukti secara arkeologis melalui inskripsi nisan makam Sultan Malik as-Saleh berangka 1297 M (696 H). Berawal dari penggabungan dua kota pelabuhan Samudera dan Pasai di pesisir timur Aceh, kesultanan ini bertumbuh menjadi emporium maritim kosmopolitan penyedia lada dan pusat transmisi fikih bermazhab Syafi'i ke seantero Asia Tenggara sebelum akhirnya mengalami agresi Portugis pada 1521 dan diintegrasikan oleh Kesultanan Aceh Darussalam.",
        "key_events": [
            {"year": 1267, "event": "Meurah Silu memeluk Islam dan mendirikan Kesultanan Samudera Pasai bergelar Sultan Malik as-Saleh."},
            {"year": 1292, "event": "Marco Polo singgah di Pasai (disebut Ferlec/Basma) dalam pelayaran pulang menuju Venesia."},
            {"year": 1297, "event": "Wafatnya Sultan Malik as-Saleh, digantikan Sultan Muhammad Malik az-Zahir yang mencetak koin emas Dirham."},
            {"year": 1345, "event": "Ibnu Battuta singgah dan tinggal selama 15 hari di istana Sultan Ahmad Malik az-Zahir."},
            {"year": 1360, "event": "Ekspedisi angkatan laut Majapahit menyerang bandar Pasai sebagaimana dikonfirmasi naskah Hikayat Raja-Raja Pasai."},
            {"year": 1521, "event": "Armada Portugis di bawah Jorge de Albuquerque menduduki bandar Pasai setelah konflik perniagaan."},
            {"year": 1524, "event": "Sultan Ali Mughayat Syah dari Kesultanan Aceh Darussalam merebut kembali wilayah Pasai dan mengintegrasikannya."}
        ],
        "relics_and_heritage": [
            "Kompleks Makam Sultan Malik as-Saleh di Beuringen, Geudong",
            "Mata Uang Emas Kuno 'Deureuham' berlafaz Arab",
            "Lonceng Cakra Donya (hadiah kekaisaran Ming yang kini disimpan di Museum Aceh)",
            "Naskah Hikayat Raja-Raja Pasai (sastra historiografi Melayu tertua)",
            "Nisan Ratu Nahrasiyah bercorak kaligrafi relief tinggi khas Cambay"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Tahun berdirinya kesultanan sekitar 1267 M didukung kuat oleh kronologi epigrafi nisan wafatnya Sultan Malik as-Saleh pada 1297 M (Ramadhan 696 H) serta catatan sinkron Ibnu Battuta (1345 M) dan Marco Polo (1292 M).",
        "sources_ids": ["ricklefs-2008", "poesponegoro-notosusanto-2008", "alfian-1999", "ibn-battuta-1958", "kemendikbud-cagarbudaya"],
        "sultans_count": 6
    },
    {
        "id": "perlak",
        "name": "Kesultanan Perlak",
        "alternate_names": ["Peureulak", "Ferlec", "Mamlakat Peureulak"],
        "region": "Sumatera",
        "year_founded": 840,
        "year_founded_display": "Tradisional: 840 M / Akademik: c. Abad ke-12 M",
        "year_ended": 1292,
        "year_ended_display": "c. 1292 M (Menyatu dengan Samudera Pasai)",
        "status_timeline_type": "ended",
        "founder": "Sultan Sayyid Maulana Abdul Aziz Syah (Tradisional)",
        "capital_city": "Peureulak, Aceh Timur",
        "coordinates": {"lat": 4.7905, "lng": 97.8764},
        "golden_age": {
            "start_year": 1200,
            "end_year": 1285,
            "leader": "Sultan Makhdum Alaiddin Malik Muhammad Amin Syah II",
            "description": "Bandar perdagangan kayu perlak (kayu pembuat kapal) terkemuka yang menjadi tempat persinggahan pedagang Muslim Arab, Persia, dan Gujarat sebelum Selat Malaka dikuasai Malaka."
        },
        "historical_summary": "Kesultanan Perlak memiliki status istimewa dalam historiografi lokal Aceh. Tradisi naskah Idharul Haq mencatat berdirinya kesultanan pada tahun 840 M oleh Sayyid Maulana Abdul Aziz Syah. Namun, sejarawan akademik modern membedakan tradisi lokal abad ke-9 dengan fakta sejarah abad ke-13 yang tercatat dalam catatan Marco Polo (1292 M), di mana kota Ferlec telah dihuni kaum Muslimin pedagang namun pedalamannya masih menganut animisme. Kesultanan ini akhirnya berfusi dengan Samudera Pasai melalui pernikahan putri Ganggang Sari dengan Meurah Silu.",
        "key_events": [
            {"year": 840, "event": "Tahun pendirian menurut naskah tradisional lokal Tazkirah Thabaqat Jumuk Sultan As-Salathin."},
            {"year": 1225, "event": "Perekonomian pelabuhan Perlak berkembang pesat dengan ekspor komoditas kayu perlak bermutu tinggi."},
            {"year": 1285, "event": "Pernikahan putri Perlak, Putri Ganggang Sari, dengan Meurah Silu (Sultan Malik as-Saleh)."},
            {"year": 1292, "event": "Kunjungan Marco Polo mencatat komunitas Muslim di kota pelabuhan Ferlec; wilayah berangsur melebur ke dalam Samudera Pasai."}
        ],
        "relics_and_heritage": [
            "Kompleks Makam Raja-Raja Peureulak di Bandar Khalifah, Aceh Timur",
            "Makam Sultan Makhdum Alaiddin Malik Muhammad Amin Syah II Johan Berdaulat",
            "Naskah Idharul Haq fi Mamlakatil Peureulak (manuskrip salinan tradisi lokal)"
        ],
        "verification_status": "Ketidakpastian Historiografi",
        "data_certainty_level": "Sedang",
        "certainty_notes": "Terdapat diskrepansi signifikan antara tradisi naskah lokal (yang menetapkan 840 M / 225 H sebagai tahun berdirinya dinasti) dan analisis sejarawan seperti G.W.J. Drewes & Ricklefs yang menilai keberadaan institusi monarki Islam baru terkonfirmasi secara kuat pada abad ke-12/13 M berdasarkan laporan Marco Polo (1292 M).",
        "sources_ids": ["drewes-1968", "poesponegoro-notosusanto-2008", "ricklefs-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 3
    },
    {
        "id": "aceh-darussalam",
        "name": "Kesultanan Aceh Darussalam",
        "alternate_names": ["Aceh Raya", "Serambi Mekkah", "Kingdom of Achin"],
        "region": "Sumatera",
        "year_founded": 1496,
        "year_founded_display": "1496 M (Penyatuan 1514–1520 M)",
        "year_ended": 1903,
        "year_ended_display": "1903 M (Sultan Muhammad Daud Syah ditawan Belanda)",
        "status_timeline_type": "ended",
        "founder": "Sultan Ali Mughayat Syah",
        "capital_city": "Kutaraja (Banda Aceh)",
        "coordinates": {"lat": 5.5539, "lng": 95.3195},
        "golden_age": {
            "start_year": 1607,
            "end_year": 1636,
            "leader": "Sultan Iskandar Muda (1607–1636 M)",
            "description": "Aceh menjelma menjadi kekuatan adidaya militer dan maritim di Asia Tenggara dengan armada laut tangguh, menguasai pesisir barat-timur Sumatera dan Semenanjung Malaya (Johor, Perak, Pahang, Kedah). Pusat intelektualisme Islam dipimpin Syaikh Nuruddin ar-Raniri dan Hamzah Fansuri, serta menerapkan hukum tata negara Adat Meukuta Alam."
        },
        "historical_summary": "Didirikan oleh Sultan Ali Mughayat Syah pada akhir abad ke-15, Kesultanan Aceh Darussalam bangkit menjadi benteng utama Islam Nusantara menentang hegemoni kolonial Portugis di Selat Malaka. Bersekutu secara diplomatik dan militer dengan Kesultanan Utsmaniyah (Ottoman) di Istanbul sejak era Sultan Alauddin Riayat Syah al-Kahar, Aceh mencapai puncak kejayaan di bawah Sultan Iskandar Muda. Perang Aceh yang berkecamuk sejak 1873 membuktikan daya tahan kesultanan ini hingga ditawannya Sultan terakhir pada 1903.",
        "key_events": [
            {"year": 1496, "event": "Sultan Ali Mughayat Syah dinobatkan sebagai penguasa Banda Aceh Darussalam."},
            {"year": 1520, "event": "Penaklukan Daya, Pidie, dan Pasai, menyatukan seluruh kawasan utara Sumatera ke dalam satu daulah monarki."},
            {"year": 1568, "event": "Kedatangan bantuan militer, artileri meriam, dan teknisi mesiu dari Sultan Selim II Kekhalifahan Utsmaniyah."},
            {"year": 1607, "event": "Sultan Iskandar Muda naik takhta, memulai ekspansi teritorial dan modernisasi undang-undang kanun Adat Meukuta Alam."},
            {"year": 1641, "event": "Era kepemimpinan Sultanah (Sultanah Tajul Alam Safiatuddin Syah) yang menonjolkan stabilitas perniagaan dan sastra sufi."},
            {"year": 1873, "event": "Belanda menyatakan perang kepada Aceh, memulai Perang Aceh yang menewaskan Jenderal Kohler di pelataran Masjid Baiturrahman."},
            {"year": 1903, "event": "Sultan Muhammad Daud Syah ditawan Belanda di Kutaraja; perlawanan berlanjut secara gerilya di pedalaman hingga 1913."}
        ],
        "relics_and_heritage": [
            "Masjid Raya Baiturrahman (dibangun pertama kali pada 1614 oleh Sultan Iskandar Muda)",
            "Kompleks Taman Ghairah dan Gunongan (tempat peraduan Putri Phang asal Pahang)",
            "Meriam Lada Sicupak peninggalan hubungan diplomatik dengan Utsmaniyah",
            "Kompleks Makam Sultan Iskandar Muda di Baperis Banda Aceh",
            "Koleksi Naskah Bustanussalatin karya Syaikh Nuruddin ar-Raniri"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah para sultan dan dokumen diplomatik sangat lengkap, terverifikasi melalui arsip Ottoman di Istanbul, arsip VOC, naskah Bustanussalatin, serta batu-batu nisan berinskripsi di pemakaman bangsawan Kandang Meuh.",
        "sources_ids": ["ricklefs-2008", "poesponegoro-notosusanto-2008", "reid-1993", "kemendikbud-cagarbudaya"],
        "sultans_count": 8
    },
    {
        "id": "siak-sri-indrapura",
        "name": "Kesultanan Siak Sri Indrapura",
        "alternate_names": ["Siak", "Kerajaan Siak"],
        "region": "Sumatera",
        "year_founded": 1723,
        "year_founded_display": "1723 M",
        "year_ended": 1945,
        "year_ended_display": "1945 M (Bergabung sukarela ke Republik Indonesia)",
        "status_timeline_type": "integrated",
        "founder": "Raja Kecik (Sultan Abdul Jalil Rahmad Syah I)",
        "capital_city": "Siak Sri Indrapura, Riau",
        "coordinates": {"lat": 0.7963, "lng": 102.0494},
        "golden_age": {
            "start_year": 1760,
            "end_year": 1800,
            "leader": "Sultan Assyaidis Syarif Ali Abdul Jalil Saifuddin",
            "description": "Menguasai jaringan perdagangan pesisir timur Sumatera dari Tamiang hingga Sambas, berhasil mempertahankan kedaulatan laut dari tekanan VOC melalui Perang Guntung, serta menyusun kitab hukum Bab al-Qawa'id."
        },
        "historical_summary": "Didirikan oleh Raja Kecik pada tahun 1723 setelah kemelut suksesi di Kesultanan Johor, Kesultanan Siak berkembang pesat di sepanjang Sungai Siak yang strategis. Di bawah Dinasti Syarif, kesultanan memperkokoh kedudukan maritim dan melahirkan hukum kenegaraan tertulis Bab al-Qawa'id. Pada masa proklamasi 1945, Sultan Syarif Kasim II menyerahkan kedaulatan dan menyumbangkan 13 juta gulden serta mahkota kerajaan demi mendukung kemerdekaan Republik Indonesia.",
        "key_events": [
            {"year": 1723, "event": "Raja Kecik mendirikan Kesultanan Siak dan berpusat di Buantan."},
            {"year": 1759, "event": "Perang Siak melawan kongsi dagang VOC di Selat Guntung yang dimenangkan oleh Siak."},
            {"year": 1784, "event": "Dinasti Ba'alawi Hadhramaut mulai memerintah di bawah Sultan Syarif Ali."},
            {"year": 1889, "event": "Pembangunan Istana Asserayah Hasyimiah yang megah bergaya perpaduan Melayu, Arab, dan Eropa oleh Sultan Syarif Hasyim."},
            {"year": 1945, "event": "Sultan Syarif Kasim II menyatakan integrasi Siak ke NKRI dan menyerahkan mahkota emas serta kas negara kepada Presiden Sukarno."}
        ],
        "relics_and_heritage": [
            "Istana Asserayah Hasyimiah (Istana Siak Sri Indrapura)",
            "Mahkota Emas Kesultanan Siak bertahtakan rubi dan berlian (kini di Museum Nasional Jakarta)",
            "Alat Musik Komet (gramofon langka hanya ada 2 unit di dunia)",
            "Jembatan Tangsi dan Kapal Uap Kato milik kesultanan",
            "Masjid Raya Syahabuddin di tepi Sungai Siak"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Seluruh silsilah dan administrasi hukum kerajaan tercatat rapi dalam naskah Bab al-Qawa'id dan arsip kolonial Hindia Belanda (Besluit 1915).",
        "sources_ids": ["ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 6
    },
    {
        "id": "palembang-darussalam",
        "name": "Kesultanan Palembang Darussalam",
        "alternate_names": ["Kesultanan Palembang", "Palembang Darussalam"],
        "region": "Sumatera",
        "year_founded": 1659,
        "year_founded_display": "1659 M (Melepaskan diri dari Banten)",
        "year_ended": 1823,
        "year_ended_display": "1823 M (Dihapuskan oleh Kolonial Belanda)",
        "status_timeline_type": "ended",
        "founder": "Sri Susuhunan Abdurrahman Khalifatul Mukminin Sayidul Iman",
        "capital_city": "Palembang (Benteng Kuto Besak), Sumatera Selatan",
        "coordinates": {"lat": -2.9904, "lng": 104.7592},
        "golden_age": {
            "start_year": 1776,
            "end_year": 1821,
            "leader": "Sultan Muhammad Bahauddin & Sultan Mahmud Badaruddin II",
            "description": "Menikmati surplus kemakmuran luar biasa dari komoditas timah di Pulau Bangka dan lada pedalaman Musi. Membangun kompleks pertahanan benteng batu bata Kuto Besak dan memproduksi karya sastra keagamaan oleh ulama terkemuka Syekh Abdus Shamad al-Palimbani."
        },
        "historical_summary": "Setelah hancurnya keraton lama Kuto Gawang akibat gempuran VOC pada 1659, Pangeran Ario Kesumo mendeklarasikan kemerdekaan Palembang dengan gelar Sri Susuhunan Abdurrahman, melepaskan keterikatan dengan Banten. Kesultanan Palembang menjadi kekuatan ekonomi utama di selatan Selat Bangka berkat monopoli timah dan lada. Perang Palembang (1819–1821) di bawah Sultan Mahmud Badaruddin II menghasilkan perlawanan gigih sebelum akhirnya sang sultan diasingkan ke Ternate.",
        "key_events": [
            {"year": 1659, "event": "Deklarasi Kesultanan Palembang Darussalam dan melepaskan diri dari protektorat Banten."},
            {"year": 1710, "event": "Penemuan deposit timah melimpah di Bangka yang melipatgandakan kas kesultanan."},
            {"year": 1780, "event": "Selesainya pembangunan Benteng Kuto Besak sebagai keraton berbenteng pertahanan modern."},
            {"year": 1812, "event": "Pasukan Inggris di bawah Mayor Gillespie menyerang Palembang dan menjarah keraton Kuto Besak."},
            {"year": 1819, "event": "Sultan Mahmud Badaruddin II memukul mundur ekspedisi militer Belanda di Sungai Musi (Perang Palembang I)."},
            {"year": 1821, "event": "Ekspedisi De Kock berhasil merebut Benteng Kuto Besak; SMB II diasingkan ke Ternate."},
            {"year": 1823, "event": "Pemerintah kolonial Hindia Belanda secara sepihak membubarkan lembaga Kesultanan Palembang."}
        ],
        "relics_and_heritage": [
            "Benteng Kuto Besak di tepi Sungai Musi",
            "Masjid Agung Sultan Mahmud Badaruddin I Jayo Wikramo",
            "Makam Kawah Tengkurep (pemakaman sultan dan pembesar)",
            "Kain Songket Palembang benang emas bersulam motif naga besaung",
            "Naskah Sair Perang Palembang karangan sastrawan keraton"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Data genealogi, catatan arsip VOC dan Inggris (Raffles), serta peninggalan fisik benteng dan masjid terverifikasi secara mendalam.",
        "sources_ids": ["peeters-1997", "ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 5
    },
    {
        "id": "jambi",
        "name": "Kesultanan Jambi",
        "alternate_names": ["Tanah Pilih Pusako Batuah", "Kerajaan Melayu Jambi"],
        "region": "Sumatera",
        "year_founded": 1615,
        "year_founded_display": "1615 M (Gelar Sultan pertama kali)",
        "year_ended": 1904,
        "year_ended_display": "1904 M (Wafatnya Sultan Thaha Syaifuddin dalam pertempuran)",
        "status_timeline_type": "ended",
        "founder": "Sultan Abdul Kahar (Pangeran Kedah)",
        "capital_city": "Kota Jambi / Muaro Jambi, Jambi",
        "coordinates": {"lat": -1.5907, "lng": 103.6139},
        "golden_age": {
            "start_year": 1630,
            "end_year": 1680,
            "leader": "Sultan Abdul Kahar & Sultan Sri Ingalogo",
            "description": "Menjadi pelabuhan pengekspor lada terbesar kedua di Sumatera setelah Banten dan Aceh, memelihara otonomi politik dari ancaman Johor dan Mataram melalui diplomasi perniagaan bebas."
        },
        "historical_summary": "Berakar dari Kerajaan Melayu kuno di Batanghari yang mengalami islamisasi sejak kepemimpinan Orang Kayo Hitam, status kesultanan resmi disematkan pada 1615 ketika Pangeran Kedah dinobatkan sebagai Sultan Abdul Kahar. Jambi mempertahankan kedaulatan di pedalaman hulu Batanghari. Pada abad ke-19, Sultan Thaha Syaifuddin memimpin perang gerilya selama puluhan tahun menolak traktat monopoli Belanda hingga ia gugur di medan tempur Betung Bedarah pada 1904.",
        "key_events": [
            {"year": 1615, "event": "Pangeran Kedah ditabalkan sebagai Sultan Abdul Kahar, sultan pertama Jambi."},
            {"year": 1643, "event": "Perjanjian perdagangan komoditas lada pertama dengan kantor dagang VOC."},
            {"year": 1673, "event": "Perang Jambi-Johor berkobar mengakibatkan kehancuran armada laut Johor di Sungai Batanghari."},
            {"year": 1858, "event": "Sultan Thaha Syaifuddin menolak mendatatangani traktat kedaulatan Belanda dan menyingkir ke Muara Tebo memimpin perlawanan bersenjata."},
            {"year": 1904, "event": "Sultan Thaha Syaifuddin gugur dalam pertempuran fajar melawan pasukan marsose di Betung Bedarah."}
        ],
        "relics_and_heritage": [
            "Masjid Agung Pondok Tinggi dan Masjid Al-Falah Jambi",
            "Keris Siginjai (pusaka lambang legitimasi mahkota Kesultanan Jambi)",
            "Kompleks Makam Orang Kayo Hitam di Simpang Malapari",
            "Kompleks Makam Pahlawan Nasional Sultan Thaha Syaifuddin di Muara Tebo"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah terverifikasi naskah Undang-Undang Piagam Pencacahan Jambi dan arsip perang kolonial Jambi 1858–1904.",
        "sources_ids": ["ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 4
    },
    {
        "id": "deli",
        "name": "Kesultanan Deli",
        "alternate_names": ["Deli Darul Maimun", "Deli"],
        "region": "Sumatera",
        "year_founded": 1632,
        "year_founded_display": "1632 M (Pecah dari Aceh)",
        "year_ended": 1946,
        "year_ended_display": "1946 M (Peristiwa Revolusi Sosial Sumatera Timur / Lembaga Adat)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Tuanku Panglima Gocah Pahlawan",
        "capital_city": "Medan (Istana Maimun), Sumatera Utara",
        "coordinates": {"lat": 3.5753, "lng": 98.6839},
        "golden_age": {
            "start_year": 1873,
            "end_year": 1924,
            "leader": "Sultan Ma'mun Al Rasyid Perkasa Alamsyah",
            "description": "Era kemakmuran perkebunan tembakau Deli kelas dunia yang mendanai pembangunan Istana Maimun yang megah dan Masjid Raya Al-Mashun dengan paduan arsitektur Melayu, Islam Spanyol (Moorish), dan Italia."
        },
        "historical_summary": "Didirikan oleh Tuanku Panglima Gocah Pahlawan pada tahun 1632 yang awalnya merupakan wakil Sultan Aceh Iskandar Muda di Tanah Deli. Kesultanan ini menjadi entitas berdaulat dan meraih kemakmuran ekonomi modern luar biasa pada paruh kedua abad ke-19 berkat konsesi perkebunan tembakau Deli Maatschappij. Saat ini Kesultanan Deli tetap lestari sebagai penjaga adat dan warisan budaya Melayu Sumatera Timur.",
        "key_events": [
            {"year": 1632, "event": "Tuanku Panglima Gocah Pahlawan ditunjuk menjadi wakil Kesultanan Aceh di wilayah Deli."},
            {"year": 1669, "event": "Tuanku Panglima Parunggit memproklamasikan pemisahan kemerdekaan Deli dari Aceh."},
            {"year": 1863, "event": "Pengusaha tembakau Jacobus Nienhuys tiba dan merintis industri perkebunan tembakau Deli beromset raksasa."},
            {"year": 1888, "event": "Peletakan batu pertama pembangunan Istana Maimun oleh arsitek Kapten Th. van Erp."},
            {"year": 1906, "event": "Pembangunan Masjid Raya Al-Mashun Medan."},
            {"year": 1946, "event": "Gelombang Revolusi Sosial di Sumatera Timur mengakhiri kekuasaan politik administratif kesultanan."}
        ],
        "relics_and_heritage": [
            "Istana Maimun di Kota Medan",
            "Masjid Raya Al-Mashun Medan",
            "Taman Sri Deli",
            "Kompleks Pemakaman Kesultanan Deli di Masjid Raya",
            "Koleksi meriam Puntung bertuah"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah dinasti Gocah Pahlawan tercatat akurat dalam buku silsilah Kesultanan Deli dan dokumen akta konsesi tembakau Hindia Belanda.",
        "sources_ids": ["ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 5
    },
    {
        "id": "riau-lingga",
        "name": "Kesultanan Riau-Lingga",
        "alternate_names": ["Kesultanan Lingga-Riau", "Negeri Daik Lingga"],
        "region": "Sumatera",
        "year_founded": 1824,
        "year_founded_display": "1824 M (Traktat London)",
        "year_ended": 1911,
        "year_ended_display": "1911 M (Dimakzulkan sepihak oleh Belanda)",
        "status_timeline_type": "ended",
        "founder": "Sultan Abdul Rahman Muazzam Syah",
        "capital_city": "Daik (Pulau Lingga) & Pulau Penyengat, Kepulauan Riau",
        "coordinates": {"lat": -0.2104, "lng": 104.6186},
        "golden_age": {
            "start_year": 1845,
            "end_year": 1895,
            "leader": "Yang Dipertuan Muda Raja Ali Haji & Sultan Mahmud IV Muzaffar Syah",
            "description": "Pusat renaisans kesusastraan dan standardisasi bahasa Melayu tinggi (akar Bahasa Indonesia). Raja Ali Haji menggubah maha karya sastra Gurindam Dua Belas serta menyusun kamus ekabahasa Melayu pertama Kitab Pengetahuan Bahasa."
        },
        "historical_summary": "Terbentuk akibat Traktat London 1824 yang membelah wilayah Kesultanan Johor-Riau menjadi wilayah protektorat Inggris (Semenanjung Malaya/Singapura) dan Belanda (Kepulauan Riau-Lingga). Beribu kota di Daik Lingga dan memiliki pusat kebudayaan di Pulau Penyengat, kesultanan ini mengukir sejarah sebagai kiblat pembakuan bahasa dan adab Melayu modern. Kesultanan dibubarkan paksa oleh Belanda pada 1911 setelah Sultan Abdul Rahman II menolak menandatangani Korte Verklaring.",
        "key_events": [
            {"year": 1824, "event": "Traktat London memisahkan Kepulauan Lingga-Riau dari Kesultanan Johor."},
            {"year": 1847, "event": "Raja Ali Haji menyelesaikan gubahan mahakarya Gurindam Dua Belas di Pulau Penyengat."},
            {"year": 1857, "event": "Sultan Mahmud IV dipecat sepihak oleh Gubernur Jenderal Belanda karena menolak tunduk pada hegemoni Batavia."},
            {"year": 1911, "event": "Sultan Abdul Rahman II menolak menandatangani perjanjian penyerahan kedaulatan, melarikan diri ke Singapura; Belanda membubarkan kesultanan."}
        ],
        "relics_and_heritage": [
            "Masjid Raya Sultan Riau di Pulau Penyengat (dinding berperekat putih telur)",
            "Kompleks Makam Raja Ali Haji (Pahlawan Nasional Bahasa)",
            "Situs Istana Damnah di Daik Lingga",
            "Gedung Percetakan Mathba'ah al-Ahmadiyah dan naskah-naskah Bustan al-Katibin"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Dokumentasi arsip Belanda, naskah Tuhfat al-Nafis karya Raja Ali Haji, serta monumen fisik di Pulau Penyengat sangat lengkap.",
        "sources_ids": ["dijk-2007", "ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 4
    },
    {
        "id": "indragiri",
        "name": "Kesultanan Indragiri",
        "alternate_names": ["Kerajaan Indragiri", "Inderagiri"],
        "region": "Sumatera",
        "year_founded": 1508,
        "year_founded_display": "1508 M (Transformasi Islam)",
        "year_ended": 1945,
        "year_ended_display": "1945 M (Integrasi ke NKRI)",
        "status_timeline_type": "integrated",
        "founder": "Raja Merlang II / Sultan Jamaluddin Narasinga II",
        "capital_city": "Kuantan / Rengat, Riau",
        "coordinates": {"lat": -0.3756, "lng": 102.5458},
        "golden_age": {
            "start_year": 1530,
            "end_year": 1580,
            "leader": "Sultan Nara Singa II (Paduka Sri Sultan Alaudin Jallaludin)",
            "description": "Mempertahankan kedaulatan di pesisir tengah Sumatera dari serbuan Portugis dan mengamankan jalur pelayaran komoditas emas dan lada dari hulu Batang Kuantan ke Selat Malaka."
        },
        "historical_summary": "Berasal dari kerajaan kuno yang berakar di hulu Sungai Batang Kuantan, Indragiri bertransformasi menjadi kesultanan Islam setelah perkawinan keluarga kerajaan dengan putri Kesultanan Malaka di era Sultan Mansur Syah. Pusat kesultanan beberapa kali bergeser dari Japura hingga ke Kota Lama dan Rengat. Sultan Nara Singa II memimpin perlawanan terhadap agresi armada Portugis di muara Sungai Indragiri.",
        "key_events": [
            {"year": 1508, "event": "Raja Narasinga II naik takhta dan memperkuat institusi syariat Islam."},
            {"year": 1515, "event": "Pertahanan gigih armada Indragiri memukul mundur ekspedisi kapal perang Portugis di muara sungai."},
            {"year": 1815, "event": "Ibu kota kesultanan dipindahkan ke Rengat oleh Sultan Ibrahim."},
            {"year": 1945, "event": "Sultan Mahmud Syah menyatakan kepatuhan dan peleburan wilayah kekuasaan Indragiri ke dalam Republik Indonesia."}
        ],
        "relics_and_heritage": [
            "Kompleks Pemakaman Raja-Raja Indragiri di Kota Lama, Rengat",
            "Makam Sultan Nara Singa II dan Panglima Ali Besar",
            "Rumah Adat Melayu Tradisional Rengat",
            "Masjid Raya Rengat"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Terkonfirmasi melalui naskah Sejarah Melayu, naskah Hikayat Merong Mahawangsa, serta batu-batu nisan di situs cagar budaya Kota Lama.",
        "sources_ids": ["poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 3
    },
    {
        "id": "pagaruyung-islam",
        "name": "Kerajaan Pagaruyung (Fase Kesultanan)",
        "alternate_names": ["Kerajaan Minangkabau Islam", "Darul Qorror"],
        "region": "Sumatera",
        "year_founded": 1560,
        "year_founded_display": "c. 1560 M (Era Sultan Alif)",
        "year_ended": 1825,
        "year_ended_display": "1825 M (Perjanjian Padang & Perang Padri)",
        "status_timeline_type": "ended",
        "founder": "Sultan Alif Khalifatullah",
        "capital_city": "Batusangkar, Tanah Datar, Sumatera Barat",
        "coordinates": {"lat": -0.4712, "lng": 100.6212},
        "golden_age": {
            "start_year": 1600,
            "end_year": 1680,
            "leader": "Raja Alam Minangkabau & Tri Tunggal Tigo Jangko",
            "description": "Penyatuan filsafat 'Adat Basandi Syarak, Syarak Basandi Kitabullah' (ABS-SBK) melalui Piagam Bukit Marapalam, menaungi wilayah rantau dari pesisir barat hingga timur Sumatera serta penghasil emas pedalaman."
        },
        "historical_summary": "Pagaruyung yang sebelumnya berakar pada masa Adityawarman mengalami islamisasi bertahap pada abad ke-16 di bawah kepemimpinan Sultan Alif Khalifatullah. Struktur kepemimpinan unik 'Rajo Tigo Jangko' (Raja Alam, Raja Adat, dan Raja Ibadat) memadukan syariat Islam dengan hukum adat matrilineal Minangkabau. Pada awal abad ke-19, Perang Padri meletus akibat perselisihan purifikasi kaum Padri dengan kaum adat yang kemudian dimanfaatkan Belanda untuk menguasai pedalaman Minangkabau.",
        "key_events": [
            {"year": 1560, "event": "Sultan Alif Khalifatullah dinobatkan sebagai Raja Islam pertama Pagaruyung."},
            {"year": 1674, "event": "Pemberontakan perniagaan lada dan emas pesisir barat melawan kongsi monopoli VOC."},
            {"year": 1803, "event": "Kembalinya tiga haji dari Mekkah memulai gerakan pembaruan Padri di Luhak Agam."},
            {"year": 1815, "event": "Pasukan Padri menyerang ibu kota Pagaruyung; keluarga kerajaan terpaksa mengungsi."},
            {"year": 1821, "event": "Kaum Adat menandatangani perjanjian penyerahan kedaulatan kepada Belanda di Padang guna menghadapi Padri."}
        ],
        "relics_and_heritage": [
            "Istano Basa Pagaruyung di Batusangkar (replika agung istana bertanduk gonjong)",
            "Prasasti Pagaruyung dan Batu Kasur",
            "Naskah Tambo Minangkabau di istana Silinduang Bulan",
            "Masjid Bingkudu di Ampek Angkek (arsitektur atap tumpang bertingkat)"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Transisi dari kerajaan era Adityawarman ke fase kesultanan terkonfirmasi lewat kronik VOC (laporan Jacob Pits 1668) dan teks Tambo Minangkabau.",
        "sources_ids": ["ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 3
    },

    # ==========================================
    # JAWA
    # ==========================================
    {
        "id": "demak",
        "name": "Kesultanan Demak",
        "alternate_names": ["Demak Bintoro", "Glagah Wangi", "Kingdom of Demak"],
        "region": "Jawa",
        "year_founded": 1475,
        "year_founded_display": "c. 1475 M (Otonom) / 1500 M (Kedaulatan Penuh)",
        "year_ended": 1554,
        "year_ended_display": "1554 M (Peralihan kekuasaan ke Pajang)",
        "status_timeline_type": "ended",
        "founder": "Raden Patah (Sultan Syah Alam Akbar I)",
        "capital_city": "Demak, Jawa Tengah",
        "coordinates": {"lat": -6.8944, "lng": 110.6385},
        "golden_age": {
            "start_year": 1518,
            "end_year": 1546,
            "leader": "Sultan Trenggana (1521–1546 M) & Pati Unus",
            "description": "Menjadi kesultanan maritim terkuat di Laut Jawa. Pati Unus melancarkan ekspedisi gabungan menyerang armada Portugis di Malaka (1513 & 1521). Fatahillah merebut Sunda Kelapa (1527), dan kekuasaan militer Demak membentang dari Banten, Cirebon, hingga Pasuruan dan Blambangan."
        },
        "historical_summary": "Kesultanan Demak merupakan kerajaan Islam pelopor di Pulau Jawa yang didirikan oleh Raden Patah atas restu dan bimbingan majelis Walisongo. Berawal dari kadipaten Glagah Wangi di pesisir utara Jawa, Demak menggantikan supremasi politik Majapahit yang melemah. Di bawah Sultan Trenggana, Demak menyatukan kota-kota pelabuhan pesisir Jawa. Konflik suksesi pasca gugurnya Sultan Trenggana di Panarukan mengakhiri riwayat Demak dan pusat politik Jawa bergeser ke pedalaman Pajang.",
        "key_events": [
            {"year": 1475, "event": "Raden Patah membuka hutan Glagah Wangi menjadi pusat dakwah Islam dan pemukiman santri."},
            {"year": 1479, "event": "Pembangunan Masjid Agung Demak dengan saka guru tatal oleh para Walisongo."},
            {"year": 1513, "event": "Pati Unus (Pangeran Sabrang Lor) memimpin 100 kapal perang menyerbu benteng Portugis di Malaka."},
            {"year": 1521, "event": "Sultan Trenggana naik takhta, menandai fase perluasan wilayah besar-besaran di pedalaman dan pesisir Jawa."},
            {"year": 1527, "event": "Pasukan gabungan Demak-Cirebon dipimpin Fatahillah merebut Sunda Kelapa dari Portugis dan mengubah namanya menjadi Jayakarta."},
            {"year": 1546, "event": "Sultan Trenggana gugur dalam pengepungan benteng Panarukan, memicu perang saudara antar trah Sekar Seda Lepen dan Sunan Prawoto."},
            {"year": 1554, "event": "Joko Tingkir (Hadiwijaya) menumpas Arya Penangsang dan memindahkan takhta ke Kesultanan Pajang."}
        ],
        "relics_and_heritage": [
            "Masjid Agung Demak (Masjid Wali dengan saka tatal Sunan Kalijaga)",
            "Pintu Bledeg buatan Ki Ageng Selo berinskripsi candrasengkala",
            "Kompleks Pemakaman Sultan-Sultan Demak di sisi barat masjid",
            "Makam Sunan Kalijaga di Kadilangu Demak",
            "Bedug dan Kentongan bersejarah peninggalan Walisongo"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Catatan Tome Pires dalam Suma Oriental (1512–1515 M) mengonfirmasi peranan 'Pate Rodim' (Raden Patah) dan 'Pate Unus' sebagai penguasa maritim terkuat pesisir utara Jawa.",
        "sources_ids": ["graaf-pigeaud-2001", "tome-pires-1944", "ricklefs-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 5
    },
    {
        "id": "pajang",
        "name": "Kesultanan Pajang",
        "alternate_names": ["Kerajaan Pajang"],
        "region": "Jawa",
        "year_founded": 1568,
        "year_founded_display": "1568 M",
        "year_ended": 1586,
        "year_ended_display": "1586 M (Diserap oleh Kesultanan Mataram)",
        "status_timeline_type": "ended",
        "founder": "Jaka Tingkir (Sultan Hadiwijaya)",
        "capital_city": "Pajang, Surakarta / Sukoharjo, Jawa Tengah",
        "coordinates": {"lat": -7.5683, "lng": 110.7852},
        "golden_age": {
            "start_year": 1568,
            "end_year": 1582,
            "leader": "Sultan Hadiwijaya (Jaka Tingkir)",
            "description": "Pergeseran paradigma politik dari maritim pesisir ke kerajaan agraris pedalaman lembah Bengawan Solo, melimpahnya surplus beras dan pengakuan ketundukan adipati-adipati pesisir Jawa Timur (Surabaya, Tuban, Madura)."
        },
        "historical_summary": "Didirikan oleh Sultan Hadiwijaya (Jaka Tingkir, menantu Sultan Trenggana), Pajang menandai babak peralihan hegemoni kekuasaan Islam Jawa dari jalur bahari pesisir pantai utara menuju pusat-pusat agraris pedalaman lembah subur Bengawan Solo. Pajang membawahi kadipaten-kadipaten penting Jawa Timur. Pemberian tanah perdikan Hutan Mentaok kepada Ki Ageng Pamanahan kemudian melahirkan cikal bakal dinasti Mataram yang akhirnya menggeser dan menyerap takhta Pajang.",
        "key_events": [
            {"year": 1568, "event": "Penobatan Sultan Hadiwijaya di hadapan Sunan Giri dan adipati-adipati seluruh Jawa."},
            {"year": 1575, "event": "Sultan Hadiwijaya menganugerahkan alas Mentaok kepada Ki Ageng Pamanahan sebagai hadiah atas sayembara membunuh Arya Penangsang."},
            {"year": 1582, "event": "Pertempuran antara pasukan Pajang melawan Senapati di Prambanan; Sultan Hadiwijaya jatuh sakit dan wafat di Butuh."},
            {"year": 1586, "event": "Sutawijaya (Panembahan Senapati) secara resmi mengambil alih pusaka kerajaan dan memindahkan pusat kekuasaan ke Mataram."}
        ],
        "relics_and_heritage": [
            "Situs Petilasan Keraton Pajang di Makamhaji, Kartasura",
            "Kompleks Makam Sultan Hadiwijaya di Butuh, Sragen",
            "Sendang Pengantin dan bekas umpak-umpak batu keraton"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Historiografi Pajang tercatat dalam Babad Tanah Jawi, Serat Pranitiradya, dan dianalisis secara kritis oleh De Graaf & Pigeaud.",
        "sources_ids": ["graaf-pigeaud-2001", "ricklefs-2008", "poesponegoro-notosusanto-2008"],
        "sultans_count": 2
    },
    {
        "id": "mataram-islam",
        "name": "Kesultanan Mataram Islam",
        "alternate_names": ["Mataram Baru", "Karajan Mataram"],
        "region": "Jawa",
        "year_founded": 1586,
        "year_founded_display": "1586 M",
        "year_ended": 1755,
        "year_ended_display": "1755 M (Terbagi melalui Perjanjian Giyanti menjadi Surakarta & Yogyakarta)",
        "status_timeline_type": "ended",
        "founder": "Danang Sutawijaya (Panembahan Senapati)",
        "capital_city": "Kotagede / Karta / Plered / Kartasura, D.I. Yogyakarta & Jawa Tengah",
        "coordinates": {"lat": -7.8286, "lng": 110.3997},
        "golden_age": {
            "start_year": 1613,
            "end_year": 1645,
            "leader": "Sultan Agung Hanyakrakusuma (1613–1645 M)",
            "description": "Menyatukan hampir seluruh Pulau Jawa, Madura, dan Sukadana (Kalimantan). Mengorganisasi dua kali penyerbuan akbar mengepung benteng VOC di Batavia (1628 & 1629), menyusun Kalender Jawa (anarki penanggalan Saka & Hijriah), serta menggubah Kitab Sastra Gendhing."
        },
        "historical_summary": "Didirikan oleh Panembahan Senapati di Kotagede, Mataram Islam tumbuh menjadi kemaharajaan agraris-militer terbesar di Jawa pada abad ke-17. Di bawah pimpinan cucunya, Sultan Agung Hanyakrakusuma, Mataram mengintegrasikan kebudayaan Jawa-Islam tingkat tinggi, mengasimilasi penanggalan Saka dengan Hijriah, dan melancarkan penyerbuan terhadap benteng VOC Batavia. Pemberontakan Trunajaya dan intrik suksesi internal pada abad ke-18 melemahkan kedaulatan Mataram hingga akhirnya pecah melalui Perjanjian Giyanti (1755) menjadi Kasunanan Surakarta dan Kasultanan Yogyakarta.",
        "key_events": [
            {"year": 1586, "event": "Panembahan Senapati mendeklarasikan berdirinya Kesultanan Mataram di Kotagede."},
            {"year": 1613, "event": "Raden Mas Rangsang naik takhta dan kemudian bergelar Sultan Agung Senapati ing Alaga Abdurrahman."},
            {"year": 1628, "event": "Penyerbuan pertama armada bala tentara Mataram mengepung benteng VOC di Batavia di bawah pimpinan Tumenggung Bahureksa."},
            {"year": 1629, "event": "Penyerbuan kedua Mataram ke Batavia dengan membendung Sungai Ciliwung; Gubernur Jenderal Jan Pieterszoon Coen tewas di dalam benteng."},
            {"year": 1633, "event": "Sultan Agung secara resmi memberlakukan Kalender Jawa (Sultan Agungan)."},
            {"year": 1677, "event": "Pemberontakan Pangeran Trunajaya dari Madura berhasil menjebol Keraton Plered; Amangkurat I mangkat di Tegalarum."},
            {"year": 1755, "event": "Perjanjian Giyanti membagi wilayah Mataram menjadi Kasunanan Surakarta dan Kasultanan Yogyakarta."}
        ],
        "relics_and_heritage": [
            "Kompleks Makam Raja-Raja Mataram Imogiri di Bantul",
            "Makam Kotagede dan Watu Gilang",
            "Situs Keraton Karta dan Reruntuhan Benteng Keraton Plered",
            "Kalender Jawa Islam (Tahun Jawa Anno Javanico)",
            "Kitab Sastra Gendhing karangan Sultan Agung"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah terverifikasi naskah Babad Tanah Jawi, Daghregister VOC Batavia, serta arsip perjanjian diplomatik Giyanti 1755 dan Salatiga 1757.",
        "sources_ids": ["ricklefs-2008", "graaf-pigeaud-2001", "vlekke-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 6
    },
    {
        "id": "kasunanan-surakarta",
        "name": "Kasunanan Surakarta Hadiningrat",
        "alternate_names": ["Keraton Solo", "Surakarta"],
        "region": "Jawa",
        "year_founded": 1755,
        "year_founded_display": "1755 M (Perjanjian Giyanti)",
        "year_ended": 1945,
        "year_ended_display": "1945 M (Daerah Istimewa Surakarta/Status Kultural Adat)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Sri Susuhunan Pakubuwana III",
        "capital_city": "Surakarta (Solo), Jawa Tengah",
        "coordinates": {"lat": -7.5778, "lng": 110.8281},
        "golden_age": {
            "start_year": 1788,
            "end_year": 1820,
            "leader": "Sri Susuhunan Pakubuwana IV (1788–1820 M)",
            "description": "Zaman keemasan kesusastraan keraton Jawa (Renaisans Jawa Baru). Menggubah Serat Wulangreh, melahirkan pujangga agung Raden Ngabehi Yasadipura I dan Yasadipura II, serta penataan arsitektur Sasana Sewaka."
        },
        "historical_summary": "Didirikan sebagai kelanjutan resmi dinasti Mataram pasca Perjanjian Giyanti 1755, Kasunanan Surakarta di bawah pimpinan Pakubuwana III memusatkan pusat keraton di Desa Sala. Kasunanan menjadi episentrum kebudayaan adi luhung Jawa, tata krama karaton, seni tari bedhaya, dan sastra piwulang. Pada masa kemerdekaan 1945, Pakubuwana XII menyatakan integrasi dengan NKRI, dan kini keraton berfungsi sebagai penjaga warisan pusaka kebudayaan bangsa.",
        "key_events": [
            {"year": 1745, "event": "Pakubuwana II memindahkan istana dari Kartasura ke Sala (cikal bakal Surakarta)."},
            {"year": 1755, "event": "Penandatanganan Perjanjian Giyanti yang mengukuhkan Pakubuwana III sebagai Susuhunan Surakarta."},
            {"year": 1788, "event": "Pakubuwana IV naik takhta dan menyusun kitab etika kepemimpinan Serat Wulangreh."},
            {"year": 1893, "event": "Pakubuwana X naik takhta, merintis modernisasi fasilitas kota Surakarta, stadion, rumah sakit, dan mendanai pergerakan Sarekat Islam."},
            {"year": 1945, "event": "Susuhunan Pakubuwana XII mengeluarkan maklumat 1 September 1945 menyatakan Surakarta berdiri di belakang NKRI."}
        ],
        "relics_and_heritage": [
            "Keraton Kasunanan Surakarta Hadiningrat dan Alun-Alun Kidul",
            "Menara Panggung Sangga Buwana (tempat meditasi raja)",
            "Museum Keraton Kasunanan dan Sasana Sewaka",
            "Naskah Serat Wulangreh dan Serat Centhini",
            "Masjid Agung Surakarta Kauman"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah para Sunan terdokumentasi lengkap dan eksis secara berkesinambungan hingga masa kini.",
        "sources_ids": ["ricklefs-2008", "poesponegoro-notosusanto-2008", "lombard-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 5
    },
    {
        "id": "kasultanan-yogyakarta",
        "name": "Kasultanan Ngayogyakarta Hadiningrat",
        "alternate_names": ["Keraton Jogja", "Yogyakarta Hadiningrat"],
        "region": "Jawa",
        "year_founded": 1755,
        "year_founded_display": "1755 M (Perjanjian Giyanti)",
        "year_ended": None,
        "year_ended_display": "Masih Bertahan (Daerah Istimewa Yogyakarta / UU No. 13 Tahun 2012)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Pangeran Mangkubumi (Sri Sultan Hamengkubuwana I)",
        "capital_city": "Kota Yogyakarta, D.I. Yogyakarta",
        "coordinates": {"lat": -7.8053, "lng": 110.3644},
        "golden_age": {
            "start_year": 1756,
            "end_year": 1792,
            "leader": "Sri Sultan Hamengkubuwana I (Pangeran Mangkubumi)",
            "description": "Perancang tata ruang filosofis poros imajiner Merapi-Tugu-Keraton-Panggung Krapyak-Laut Selatan. Membangun benteng Baluwerti, Taman Sari, dan menegakkan supremasi militer prajurit keraton serta tradisi Grebeg Maulud."
        },
        "historical_summary": "Lahir dari buah perjuangan Pangeran Mangkubumi melawan VOC dalam Perjanjian Giyanti 1755, Kasultanan Yogyakarta dibangun dengan konsep filosofis tata ruang adiluhung 'Hamemayu Hayuning Bawana'. Tokoh besar Pangeran Diponegoro memimpin Perang Jawa (1825–1830) yang nyaris membangkrutkan kas Hindia Belanda. Pada 1945, Sri Sultan Hamengkubuwana IX mengeluarkan Amanat 5 September 1945 yang mengintegrasikan Yogyakarta ke Republik Indonesia dan menjadikannya Ibu Kota Revolusi RI (1946–1949). Keistimewaan DIY diakui abadi dalam UU No. 13 Tahun 2012.",
        "key_events": [
            {"year": 1755, "event": "Perjanjian Giyanti membagi Mataram; Pangeran Mangkubumi menjadi Sultan Hamengkubuwana I."},
            {"year": 1756, "event": "Sultan HB I resmi memasuki Keraton Yogyakarta (penanggalan candrasengkala Dwi Naga Rasa Tunggal)."},
            {"year": 1758, "event": "Pembangunan pesanggrahan air dan benteng pertahanan bawah tanah Taman Sari."},
            {"year": 1825, "event": "Pangeran Diponegoro mengobarkan Perang Jawa melawan penindasan kolonial Belanda (1825–1830)."},
            {"year": 1945, "event": "Amanat 5 September 1945 oleh Sri Sultan HB IX & Paku Alam VIII menyatakan Yogyakarta bergabung dengan NKRI."},
            {"year": 1946, "event": "Yogyakarta menjadi Ibu Kota Perjuangan Republik Indonesia saat Jakarta diduduki Sekutu-NICA."}
        ],
        "relics_and_heritage": [
            "Keraton Ngayogyakarta Hadiningrat (Bangsal Kencono, Pagelaran, Siti Hinggil)",
            "Pesanggrahan Taman Sari (Water Castle)",
            "Masjid Gedhe Kauman Yogyakarta",
            "Sumbu Filosofis Yogyakarta (Warisan Dunia UNESCO 2023)",
            "Kereta-kereta Kencana Pusaka (Kanjeng Nyai Jimat, Garuda Yeksa)"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah para Sultan dan kepustakaan naskah keraton (Widyabudaya & Krandhapradangga) terdata sangat akurat dan terverifikasi di kancah internasional (UNESCO).",
        "sources_ids": ["ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 6
    },
    {
        "id": "banten",
        "name": "Kesultanan Banten",
        "alternate_names": ["Banten Girang", "Bantam", "Daulah Islamiyah Banten"],
        "region": "Jawa",
        "year_founded": 1526,
        "year_founded_display": "c. 1526 M",
        "year_ended": 1813,
        "year_ended_display": "1813 M (Dihapuskan Raffles saat pendudukan Inggris)",
        "status_timeline_type": "ended",
        "founder": "Syarif Hidayatullah (Sunan Gunung Jati) & Sultan Maulana Hasanuddin",
        "capital_city": "Banten Lama, Serang, Banten",
        "coordinates": {"lat": -6.0359, "lng": 106.1544},
        "golden_age": {
            "start_year": 1651,
            "end_year": 1683,
            "leader": "Sultan Ageng Tirtayasa (Pangeran Surya)",
            "description": "Menjadikan Pelabuhan Karangantu bandar niaga internasional bebas yang menghubungkan Inggris, Prancis, Denmark, Turki, dan Persia. Membangun sistem kanal irigasi pertanian modern di Pontang dan Tanara, serta memiliki armada kapal dagang modern berbendera Banten."
        },
        "historical_summary": "Didirikan oleh Maulana Hasanuddin putra Sunan Gunung Jati pada 1526 setelah merebut Banten Girang dan Pelabuhan Sunda Kalapa dari Kerajaan Sunda. Banten menguasai jalur perdagangan Selat Sunda dan memonopoli komoditas lada Lampung. Puncak kemakmuran diraih pada era Sultan Ageng Tirtayasa yang gigih menentang monopoli dagang VOC. Konflik perpecahan antara Sultan Ageng dan putranya, Sultan Haji yang berkomplot dengan Belanda, menandai kemunduran kesultanan hingga akhirnya dibubarkan oleh Letnan Gubernur Raffles pada 1813.",
        "key_events": [
            {"year": 1526, "event": "Maulana Hasanuddin menaklukkan Banten Girang dan mendeklarasikan Kesultanan Banten."},
            {"year": 1552, "event": "Sunan Gunung Jati secara resmi menyerahkan kepemimpinan mandiri Banten kepada Maulana Hasanuddin."},
            {"year": 1579, "event": "Maulana Yusuf menaklukkan Pakuan Pajajaran, mengakhiri sisa pengaruh dinasti Hindu Sunda di Jawa Barat."},
            {"year": 1651, "event": "Sultan Ageng Tirtayasa dinobatkan, membangun kanal irigasi dan armada dagang berteknologi Eropa."},
            {"year": 1682, "event": "Perang saudara Banten; VOC membantu Sultan Haji menyingkirkan Sultan Ageng Tirtayasa di Keraton Tirtayasa."},
            {"year": 1808, "event": "Gubernur Jenderal Daendels menghancurkan Keraton Surosowan setelah Sultan Banten menolak perintah kerja paksa Anyer-Panarukan."},
            {"year": 1813, "event": "Thomas Stamford Raffles resmi membubarkan institusi Kesultanan Banten."}
        ],
        "relics_and_heritage": [
            "Masjid Agung Banten dan Menara Mercusuar khas rancangan Cek Ban Cut",
            "Reruntuhan Keraton Surosowan dan sistem hidrolika kolam Pengindelan",
            "Reruntuhan Keraton Kaibon (istana ibunda ratu)",
            "Meriam Raksasa Ki Amuk",
            "Benteng Speelwijk peninggalan era VOC di Banten Lama"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Terdokumentasi secara detail lewat catatan harian kongsi dagang Inggris (EIC), Belanda (VOC), laporan arsitektur Guillot, dan naskah Sajarah Banten.",
        "sources_ids": ["guillot-1990", "ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 6
    },
    {
        "id": "cirebon",
        "name": "Kesultanan Cirebon",
        "alternate_names": ["Caruban Larang", "Nagari Cerbon"],
        "region": "Jawa",
        "year_founded": 1479,
        "year_founded_display": "1479 M",
        "year_ended": 1677,
        "year_ended_display": "1677 M (Terbagi menjadi Kasepuhan & Kanoman / Dilanjutkan kultural)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Syarif Hidayatullah (Sunan Gunung Jati)",
        "capital_city": "Kota Cirebon, Jawa Barat",
        "coordinates": {"lat": -6.7262, "lng": 108.5711},
        "golden_age": {
            "start_year": 1479,
            "end_year": 1568,
            "leader": "Sultan Syarif Hidayatullah (Sunan Gunung Jati)",
            "description": "Menjadi poros syiar Islam, diplomasi internasional, dan akulturasi budaya Jawa, Sunda, Tiongkok, dan Arab. Menjalin pernikahan diplomatik dengan putri Tiongkok Ong Tien Nio dan menaungi jaringan pelayaran pesisir Laut Jawa."
        },
        "historical_summary": "Didirikan oleh Pangeran Walangsungsang (Cakrabuana) dan dikembangkan menjadi kesultanan besar oleh keponakannya, Syarif Hidayatullah (Sunan Gunung Jati). Cirebon menjadi pusat dakwah Walisongo di Jawa Barat dengan memadukan elemen seni budaya Tiongkok, Arab, dan Sunda. Pasca wafatnya Panembahan Girilaya pada 1677, kesultanan terbagi menjadi tiga keraton: Kasepuhan, Kanoman, dan kemudian Kacirebonan, yang hingga kini merawat tradisi Panjang Jimat.",
        "key_events": [
            {"year": 1479, "event": "Sunan Gunung Jati mengambil alih kepemimpinan Cirebon dan menghentikan pengiriman upeti terasi ke Galuh Pajajaran."},
            {"year": 1481, "event": "Pembangunan Masjid Agung Sang Cipta Rasa yang dirancang oleh Sunan Kalijaga."},
            {"year": 1528, "event": "Armada Cirebon bersama Demak berhasil mengamankan pesisir utara dari ancaman perjanjian Sunda-Portugis."},
            {"year": 1568, "event": "Wafatnya Sunan Gunung Jati; kepemimpinan diteruskan oleh cucunya, Fatahillah dan Pangeran Emas."},
            {"year": 1677, "event": "Pembagian takhta Cirebon menjadi Kasultanan Kasepuhan dan Kasultanan Kanoman melalui mediasi Sultan Ageng Tirtayasa."}
        ],
        "relics_and_heritage": [
            "Keraton Kasepuhan dan Keraton Kanoman Cirebon",
            "Masjid Agung Sang Cipta Rasa",
            "Kereta Singa Barong (perpaduan motif gajah berbelalai garuda bersayap buroq)",
            "Taman Gua Sunyaragi (kompleks pertapaan berbatu karang)",
            "Kompleks Pemakaman Sunan Gunung Jati di Astana Gunung Sembung"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Historiografi Cirebon tercatat dalam naskah Carita Purwaka Caruban Nagari, Babad Cirebon, dan arsip perjanjian VOC abad ke-17.",
        "sources_ids": ["graaf-pigeaud-2001", "ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 5
    },
    {
        "id": "giri-kedaton",
        "name": "Giri Kedaton",
        "alternate_names": ["Kedatuan Giri", "Giri Gajah", "Kerajaan Ulama Gresik"],
        "region": "Jawa",
        "year_founded": 1487,
        "year_founded_display": "1487 M",
        "year_ended": 1680,
        "year_ended_display": "1680 M (Ditundukkan Amangkurat II bersama VOC)",
        "status_timeline_type": "ended",
        "founder": "Raden Paku (Sunan Giri / Prabu Satmata)",
        "capital_city": "Giri, Kebomas, Gresik, Jawa Timur",
        "coordinates": {"lat": -7.1691, "lng": 112.6322},
        "golden_age": {
            "start_year": 1487,
            "end_year": 1605,
            "leader": "Sunan Giri I (Prabu Satmata) & Sunan Prapen",
            "description": "Menjadi 'Vatikan-nya Jawa' dan poros legitimasi spiritual seluruh raja Islam di Nusantara. Penguasa Giri bertindak sebagai penabal sah penobatan raja-raja Demak, Pajang, Mataram, hingga mubalighnya mengislamkan Ternate, Tidore, Kutai, dan Hitu."
        },
        "historical_summary": "Didirikan oleh Sunan Giri di atas bukit Giri Gajah Gresik pada 1487, Giri Kedaton merupakan kedatuan teokratis unik di mana ulama memegang kepemimpinan politik dan spiritual tertinggi. Sunan Prapen tercatat melantik Sultan Hadiwijaya di Pajang dan mengislamkan raja-raja di Maluku dan Kalimantan Timur. Posisi Giri yang independen dipandang ancaman oleh Mataram, hingga akhirnya ditundukkan oleh pasukan Mataram pimpinan Amangkurat II yang dibantu serdadu VOC pada 1680.",
        "key_events": [
            {"year": 1487, "event": "Sunan Giri mendirikan pesantren dan pusat pemerintahan Giri Kedaton di Bukit Giri."},
            {"year": 1548, "event": "Sunan Prapen dinobatkan sebagai penguasa Giri ke-4, memperluas dakwah ke Indonesia Timur."},
            {"year": 1581, "event": "Sunan Prapen memediasi pertemuan para adipati Jawa Timur dan menobatkan Sultan Hadiwijaya Pajang."},
            {"year": 1636, "event": "Sultan Agung Mataram menaklukkan sebagian wilayah Giri setelah perlawanan sengit para santri."},
            {"year": 1680, "event": "Panembahan Ageng Giri dieksekusi setelah benteng Giri dihancurkan pasukan gabungan Mataram-VOC pimpinan Kapten Tack."}
        ],
        "relics_and_heritage": [
            "Situs Giri Kedaton di Sidomukti, Kebomas, Gresik",
            "Kompleks Makam Sunan Giri dan Makam Sunan Prapen",
            "Masjid Sunan Giri dan Cungkup Makam berukir kayu jati kuno",
            "Kolam Wudhu Kuno Giri"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Peranan politik Giri dicatat secara konvergen dalam Babad Tanah Jawi, Babad Gresik, Hikayat Hitu, serta laporan Daghregister VOC 1680.",
        "sources_ids": ["graaf-pigeaud-2001", "ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 4
    },

    # ==========================================
    # KALIMANTAN
    # ==========================================
    {
        "id": "banjar",
        "name": "Kesultanan Banjar",
        "alternate_names": ["Kesultanan Banjarmasin", "Bandjarmasin"],
        "region": "Kalimantan",
        "year_founded": 1526,
        "year_founded_display": "1526 M (24 September 1526 M)",
        "year_ended": 1860,
        "year_ended_display": "1860 M (Dihapuskan sepihak oleh Belanda / Perang Banjar berlanjut hingga 1905)",
        "status_timeline_type": "ended",
        "founder": "Raden Samudera (Sultan Suriansyah)",
        "capital_city": "Banjarmasin (Kuin) & Martapura, Kalimantan Selatan",
        "coordinates": {"lat": -3.4217, "lng": 114.8519},
        "golden_age": {
            "start_year": 1595,
            "end_year": 1642,
            "leader": "Sultan Musta'inbillah (Marhum Panembahan)",
            "description": "Mengekspor puluhan ribu pikul lada hitam berkualitas ke pasar internasional, memperluas pengaruh politik meliputi Sambas, Sukadana, Kotawaringin, hingga Berau dan Kutai, serta menjadi pusat pengkajian Islam di bawah bimbingan para khatib agung."
        },
        "historical_summary": "Berawal dari Kerajaan Negara Daha di pedalaman sungai, Pangeran Samudera yang terdesak memohon bantuan militer kepada Kesultanan Demak. Setelah mengalahkan Pangeran Tumenggung, sang pangeran memeluk Islam dengan gelar Sultan Suriansyah pada 24 September 1526 (kini diperingati sebagai Hari Jadi Kota Banjarmasin). Perekonomian kesultanan berkembang pesat dari komoditas lada dan intan Martapura. Ketika Belanda secara sepihak menghapuskan kesultanan pada 1860, meletuslah Perang Banjar yang dipimpin Pangeran Antasari dan Sultan Muhammad Seman hingga 1905.",
        "key_events": [
            {"year": 1526, "event": "Pangeran Samudera memeluk Islam bergelar Sultan Suriansyah atas bimbingan Khatib Dayan utusan Demak."},
            {"year": 1612, "event": "Serangan armada VOC membumihanguskan keraton Kuin, ibu kota kesultanan dipindahkan ke Martapura."},
            {"year": 1779, "event": "Syekh Muhammad Arsyad al-Banjari kembali dari Mekkah dan menyusun kitab fikih agung Sabilal Muhtadin."},
            {"year": 1859, "event": "Pangeran Antasari mengobarkan Perang Banjar menyerang tambang batu bara Oranje Nassau milik Belanda di Pengaron."},
            {"year": 1860, "event": "Pemerintah kolonial Belanda mengumumkan penghapusan takhta Kesultanan Banjar secara sepihak."},
            {"year": 1862, "event": "Pangeran Antasari diangkat sebagai pimpinan tertinggi dan Panembahan Amiruddin Khalifatul Mukminin."}
        ],
        "relics_and_heritage": [
            "Masjid Bersejarah Sultan Suriansyah di Kuin Utara Banjarmasin",
            "Kompleks Makam Sultan Suriansyah dan Khatib Dayan",
            "Makam Pahlawan Nasional Pangeran Antasari di Banjarmasin",
            "Kompleks Pemakaman Syekh Muhammad Arsyad al-Banjari (Datu Kelampayan) di Martapura",
            "Kitab Sabilal Muhtadin (karya rujukan fikih mazhab Syafi'i di Asia Tenggara)"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah terverifikasi naskah Hikayat Banjar, catatan VOC Daghregister, dan dokumen arsip militer Hindia Belanda dalam De Banjermasinsche Krijg.",
        "sources_ids": ["saleh-1982", "ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 6
    },
    {
        "id": "kutai-kartanegara",
        "name": "Kesultanan Kutai Kartanegara ing Martadipura",
        "alternate_names": ["Kutai Kartanegara", "Kesultanan Kutai"],
        "region": "Kalimantan",
        "year_founded": 1605,
        "year_founded_display": "c. 1605 M (Fase Islam) / Abad ke-14 (Pra-Islam)",
        "year_ended": 1960,
        "year_ended_display": "1960 M (Integrasi Pemerintahan Daerah / Kultural)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Aji Pangeran Sinum Panji Mendapa",
        "capital_city": "Tenggarong, Sungai Mahakam, Kalimantan Timur",
        "coordinates": {"lat": -0.4137, "lng": 116.9897},
        "golden_age": {
            "start_year": 1850,
            "end_year": 1915,
            "leader": "Sultan Aji Muhammad Sulaiman (1845–1899 M)",
            "description": "Mengelola kekayaan konsesi minyak bumi di Sanga-Sanga dan batu bara di lembah Mahakam. Menjadikan Tenggarong kota modern bercahaya listrik pertama di pedalaman Kalimantan dan pusat seni pertunjukan tari keraton Ganjur."
        },
        "historical_summary": "Didirikan di Jembayan pada abad ke-14, kerajaan ini bertransformasi menjadi kesultanan Islam pada awal abad ke-17 setelah Raja Aji Pangeran Sinum Panji Mendapa menaklukkan Kutai Martapura di Muara Kaman dan menerima dakwah Tuan Tunggang Parangan dari Minangkabau. Pusat kesultanan kemudian dipindahkan ke Tenggarong oleh Sultan Aji Muhammad Muslihuddin pada 1782. Di era modern, Sultan Aji Muhammad Parikesit menyerahkan kekuasaan administratif kepada NKRI pada 1960, dan keraton kini dilestarikan sebagai Museum Mulawarman.",
        "key_events": [
            {"year": 1605, "event": "Raja Aji Mahkota dan putranya Aji Dilanggar memeluk Islam atas dakwah Tuan Tunggang Parangan."},
            {"year": 1635, "event": "Aji Pangeran Sinum Panji Mendapa menyatukan wilayah Kutai Martadipura dan menyusun Kitab Brajaniti."},
            {"year": 1782, "event": "Sultan Aji Muhammad Muslihuddin memindahkan ibu kota kesultanan ke Tepian Pandan (kini Tenggarong)."},
            {"year": 1844, "event": "Pertempuran sengit di muara Mahakam melawan ekspedisi kapal perang Inggris pimpinan James Erskine Murray."},
            {"year": 1897, "event": "Pengeboran sumur minyak pertama 'Louise' di Sanga-Sanga yang membawa kemakmuran finansial melimpah."},
            {"year": 1960, "event": "Pemerintah Daerah Istimewa Kutai resmi dilebur ke dalam Provinsi Kalimantan Timur."}
        ],
        "relics_and_heritage": [
            "Kedaton Kutai Kartanegara (kini Museum Negeri Mulawarman di Tenggarong)",
            "Singgasana Kerajaan Kutai berlapis emas",
            "Ketopong Emas Mahkota Sultan Kutai Kartanegara",
            "Kalung Uncal lambang kebesaran dinasti",
            "Kompleks Pemakaman Sultan Kutai di samping Museum Mulawarman"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah terverifikasi manuskrip Surat Salasilah Raja dalam Negeri Kutai Kertanegara dan piagam konsesi migas kolonial.",
        "sources_ids": ["poesponegoro-notosusanto-2008", "ricklefs-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 5
    },
    {
        "id": "sambas",
        "name": "Kesultanan Sambas",
        "alternate_names": ["Kesultanan Sambas Darul Islam", "Sambas"],
        "region": "Kalimantan",
        "year_founded": 1671,
        "year_founded_display": "1671 M",
        "year_ended": 1950,
        "year_ended_display": "1950 M (Bergabung dalam NKRI / Berlanjut Kultural)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Raden Sulaiman (Sultan Muhammad Shafiuddin I)",
        "capital_city": "Sambas, Kalimantan Barat",
        "coordinates": {"lat": 1.3606, "lng": 109.3025},
        "golden_age": {
            "start_year": 1708,
            "end_year": 1762,
            "leader": "Sultan Umar Aqamaddin I & Sultan Abubakar Kamaluddin",
            "description": "Menjadi kesultanan terkemuka di pantai barat Kalimantan dengan armada bahari kuat yang disegani perompak Lanun dan kekuatan kolonial, pusat perdagangan intan, emas Montrado, dan perniagaan kain tenun Sambas."
        },
        "historical_summary": "Didirikan oleh Raden Sulaiman, putra bangsawan Kesultanan Brunei yang menikah dengan putri Kerajaan Panembahan Sambas Hindu. Kesultanan Sambas tumbuh pesat di pertemuan Sungai Sambas dan Sungai Teberau. Kesultanan ini melahirkan ulama legendaris Syekh Ahmad Khatib as-Sambasi (pendiri tarekat Qadiriyah wa Naqsabandiyah). Keraton Alwatzikhoebillah hingga kini tetap tegak terawat sebagai simbol jati diri peradaban Melayu Sambas.",
        "key_events": [
            {"year": 1671, "event": "Raden Sulaiman dinobatkan menjadi Sultan Sambas pertama bergelar Sultan Muhammad Shafiuddin I."},
            {"year": 1760, "event": "Perekonomian tambang emas Montrado berkembang dan mendatangkan migrasi pekerja Tionghoa Kongsi."},
            {"year": 1812, "event": "Ekspedisi angkatan laut Inggris menyerang benteng pertahanan Sambas akibat ketegangan sengketa maritim."},
            {"year": 1850, "event": "Pembangunan Istana Alwatzikhoebillah oleh Sultan Abubakar Tajuddin II."},
            {"year": 1950, "event": "Sultan Muhammad Ibrahim Syafi'uddin menyerahkan kekuasaan eksekutif swapraja kepada Republik Indonesia Serikat."}
        ],
        "relics_and_heritage": [
            "Istana Alwatzikhoebillah Sambas dan Gerbang Ramin Tradisional",
            "Masjid Jami' Sultan Muhammad Syafi'uddin Sambas",
            "Kain Tenun Songket Sambas (Tenun Lunggi motif puncuk rebung)",
            "Koleksi meriam kuno keraton dan pedang pusaka kebesaran"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah terverifikasi manuskrip Silsilah Raja-Raja Sambas dan dokumen diplomatik Kesultanan Brunei serta VOC.",
        "sources_ids": ["poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 4
    },
    {
        "id": "pontianak",
        "name": "Kesultanan Pontianak",
        "alternate_names": ["Kesultanan Kadriah Pontianak", "Kadriah"],
        "region": "Kalimantan",
        "year_founded": 1771,
        "year_founded_display": "1771 M (23 Oktober 1771 M)",
        "year_ended": 1950,
        "year_ended_display": "1950 M (Integrasi ke NKRI / Kultural)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Sultan Syarif Abdurrahman Alkadrie",
        "capital_city": "Pontianak (Muara Sungai Kapuas), Kalimantan Barat",
        "coordinates": {"lat": -0.0261, "lng": 109.3458},
        "golden_age": {
            "start_year": 1779,
            "end_year": 1855,
            "leader": "Sultan Syarif Abdurrahman & Sultan Syarif Usman Alkadrie",
            "description": "Menjadikan simpang Sungai Kapuas dan Landak bandar transit bebas pajak yang makmur, menyatukan jalur niaga pedalaman Kalimantan Barat dan pesisir Selat Karimata, serta mendirikan Istana Kadriah dan Masjid Jami'."
        },
        "historical_summary": "Didirikan pada 23 Oktober 1771 oleh Syarif Abdurrahman Alkadrie, keturunan ulama Hadhramaut dari Mempawah, di persimpangan strategis Sungai Kapuas Kecil dan Sungai Landak. Kesultanan Pontianak tumbuh pesat sebagai emporium perniagaan bebas komoditas karet, kopra, dan sarang burung walet. Pada masa revolusi kemerdekaan, Sultan Hamid II (Syarif Abdul Hamid Alkadrie) menjadi perancang lambang negara Indonesia 'Garuda Pancasila'. Keraton Kadriah kini menjadi cagar budaya nasional.",
        "key_events": [
            {"year": 1771, "event": "Syarif Abdurrahman Alkadrie membuka pemukiman dan mendirikan kesultanan di muara Kapuas."},
            {"year": 1778, "event": "Syarif Abdurrahman resmi ditabalkan menjadi Sultan pertama Pontianak dengan gelar Sultan Syarif Abdurrahman Alkadrie."},
            {"year": 1779, "event": "Pemberian status pelabuhan bebas dan penandatanganan perjanjian persahabatan dengan VOC."},
            {"year": 1855, "event": "Renovasi dan perluasan Istana Kadriah dari kayu belian pilihan."},
            {"year": 1950, "event": "Sultan Hamid II merancang lambang negara Republik Indonesia, Burung Garuda Pancasila."}
        ],
        "relics_and_heritage": [
            "Istana Kadriah Pontianak (berstruktur kayu besi/belian)",
            "Masjid Jami' Sultan Syarif Abdurrahman",
            "Rancangan asli lambang negara Garuda Pancasila karya Sultan Hamid II",
            "Cermin antik pemberian Kaisar Prancis Napoleon Bonaparte",
            "Kompleks Pemakaman Kesultanan di Batu Layang"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah klan Alkadrie tercatat akurat dalam buku nasab As-Saadah Al-Ba'alawi dan arsip Hindia Belanda.",
        "sources_ids": ["ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 5
    },
    {
        "id": "paser",
        "name": "Kesultanan Paser",
        "alternate_names": ["Kesultanan Sadurengas", "Paser"],
        "region": "Kalimantan",
        "year_founded": 1516,
        "year_founded_display": "1516 M (Islam c. 1600 M)",
        "year_ended": 1906,
        "year_ended_display": "1906 M (Dihapuskan pemerintah Hindia Belanda)",
        "status_timeline_type": "ended",
        "founder": "Putri Di Dalam Petung & Aji Mas Pati Indra",
        "capital_city": "Tanah Grogot / Paser Belengkong, Kalimantan Timur",
        "coordinates": {"lat": -1.9056, "lng": 116.2083},
        "golden_age": {
            "start_year": 1700,
            "end_year": 1770,
            "leader": "Sultan Sepuh I (Sultan Alamsyah)",
            "description": "Menguasai pesisir tenggara Kalimantan dari Teluk Balikpapan hingga perbatasan Teluk Pamukan, mengontrol perniagaan sarang burung walet, lilin lebah, dan rotan pedalaman Dayak Paser."
        },
        "historical_summary": "Didirikan oleh Putri Di Dalam Petung pada 1516, kerajaan tradisional ini bertransformasi menjadi kesultanan Islam setelah perkawinannya dengan bangsawan Muslim asal Giri (Abu Mansyur Indra Jaya). Kesultanan Sadurengas memiliki pengaruh penting di pesisir Selat Makassar. Tekanan kolonial Belanda memuncak pada penghujung abad ke-19 hingga kesultanan dihapuskan pada 1906 setelah perlawanan sengit rakyat Paser.",
        "key_events": [
            {"year": 1516, "event": "Awal pendirian Kerajaan Sadurengas di bawah Ratu Putri Di Dalam Petung."},
            {"year": 1600, "event": "Aji Mas Pati Indra dinobatkan dan melembagakan hukum-hukum syariat Islam."},
            {"year": 1730, "event": "Aji Geger dinobatkan sebagai Sultan Paser pertama dengan gelar Sultan Aji Muhammad Alamsyah."},
            {"year": 1906, "event": "Sultan Ibrahim Khaliluddin dipaksa turun takhta; wilayah Paser ditempatkan di bawah Onderafdeeling Pasir Belanda."}
        ],
        "relics_and_heritage": [
            "Museum Sadurengas (bekas keraton Kesultanan Paser di Pasir Belengkong)",
            "Masjid Jami' Nurul Ibadah Pasir Belengkong (dibangun 1851)",
            "Kompleks Makam Raja-Raja Paser Belengkong",
            "Meriam Raden Tumenggung dan pusaka tombak Datu Mustika"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah terverifikasi dalam manuskrip lokal Silsilah Kesultanan Paser dan laporan kolonial Schwaner.",
        "sources_ids": ["poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 3
    },
    {
        "id": "bulungan",
        "name": "Kesultanan Bulungan",
        "alternate_names": ["Bulungan"],
        "region": "Kalimantan",
        "year_founded": 1731,
        "year_founded_display": "1731 M",
        "year_ended": 1958,
        "year_ended_display": "1958 M (Peleburan swapraja / Peristiwa Bultiken 1964)",
        "status_timeline_type": "ended",
        "founder": "Wira Amir (Sultan Muhammad Amiril Mukminin)",
        "capital_city": "Tanjung Palas, Bulungan, Kalimantan Utara",
        "coordinates": {"lat": 2.8988, "lng": 117.3323},
        "golden_age": {
            "start_year": 1870,
            "end_year": 1925,
            "leader": "Sultan Datu Alam & Sultan Muhammad Kasimuddin",
            "description": "Menguasai jalur niaga Sungai Kayan dan pesisir Kalimantan Utara hingga perbatasan Sabah dan Sulu, mengelola hasil hutan damar, gaharu, sarang burung walet, serta deposit minyak di Pulau Tarakan."
        },
        "historical_summary": "Didirikan oleh Wira Amir keturunan bangsawan Kayan dan Melayu Brunei pada 1731. Kesultanan Bulungan berpusat di Tanjung Palas di tepian Sungai Kayan. Kesultanan ini memiliki peranan geopolitik krusial di utara pulau Kalimantan sebagai benteng kedaulatan Nusantara berhadapan dengan pengaruh Kesultanan Sulu dan kongsi Inggris di Borneo Utara. Di era kemerdekaan, wilayah swapraja Bulungan dilebur ke dalam administrasi Republik Indonesia.",
        "key_events": [
            {"year": 1731, "event": "Wira Amir mendirikan kesultanan dan bergelar Sultan Amiril Mukminin."},
            {"year": 1850, "event": "Perjanjian perbatasan kedaulatan sungai dengan pemerintah Hindia Belanda."},
            {"year": 1905, "event": "Eksplorasi deposit minyak bumi modern dimulai di Pulau Tarakan di bawah konsesi kesultanan."},
            {"year": 1958, "event": "Status Daerah Istimewa Bulungan diubah menjadi Kabupaten Bulungan, mengakhiri hak swapraja politik kesultanan."}
        ],
        "relics_and_heritage": [
            "Museum Kesultanan Bulungan di Tanjung Palas",
            "Masjid Kasimuddin (Masjid Kuno Bulungan dibangun 1902)",
            "Kompleks Pemakaman Para Sultan Bulungan",
            "Singgasana keraton dan koleksi senjata adat Kayan-Melayu"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah terverifikasi dokumen kontrak politik Hindia Belanda dan naskah silsilah Kesultanan Bulungan.",
        "sources_ids": ["poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 4
    },

    # ==========================================
    # SULAWESI
    # ==========================================
    {
        "id": "gowa",
        "name": "Kesultanan Gowa",
        "alternate_names": ["Makassar", "Kembar Gowa-Tallo", "Kerajaan Gowa"],
        "region": "Sulawesi",
        "year_founded": 1605,
        "year_founded_display": "1605 M (Deklarasi Resmi Islam) / Abad ke-14 (Pra-Islam)",
        "year_ended": 1946,
        "year_ended_display": "1946 M (Integrasi Republik Indonesia / Lembaga Adat)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Karaeng Matoaya (Tallo) & I Manga'rangi Daeng Manrabbia (Sultan Alauddin)",
        "capital_city": "Somba Opu / Sungguminasa, Gowa / Makassar, Sulawesi Selatan",
        "coordinates": {"lat": -5.1974, "lng": 119.4503},
        "golden_age": {
            "start_year": 1636,
            "end_year": 1669,
            "leader": "Sultan Malikussaid & Sultan Hasanuddin (Ayam Jantan dari Timur)",
            "description": "Menjadi adidaya bahari terbesar di kawasan timur Nusantara yang memegang prinsip mare liberum (laut terbuka bebas untuk semua bangsa). Memiliki Benteng Somba Opu yang perkasa, armada kapal phinisi pelintas samudra, dan menaungi perdagangan internasional dari Maluku hingga Malaka."
        },
        "historical_summary": "Didirikan pada awal abad ke-14, Gowa bersekutu erat dengan kembarannya Tallo. Pada 22 September 1605, penguasa Gowa-Tallo resmi mengikrarkan dua kalimat syahadat di bawah bimbingan ulama Minangkabau Dato ri Bandang. Gowa menjelma menjadi benteng pertahanan maritim paling tangguh di Nusantara melawan monopoli VOC. Puncak Perang Makassar dipimpin oleh Sultan Hasanuddin (1653–1669) yang bertempur gigih hingga penandatanganan Perjanjian Bungaya 1667. Istana Balla Lompoa kini menjadi simbol kebanggaan kebudayaan Bugis-Makassar.",
        "key_events": [
            {"year": 1605, "event": "Raja Gowa ke-14 I Manga'rangi Daeng Manrabbia resmi memeluk Islam bergelar Sultan Alauddin."},
            {"year": 1607, "event": "Shalat Jumat pertama digelar di Masjid Tallo dan Islam dideklarasikan sebagai agama resmi negara."},
            {"year": 1653, "event": "Sultan Hasanuddin naik takhta dan memperkuat benteng-benteng pertahanan pesisir Somba Opu."},
            {"year": 1666, "event": "Perang Makassar meletus; armada VOC dipimpin Cornelis Speelman bersekutu dengan Arung Palakka dari Bone."},
            {"year": 1667, "event": "Penandatanganan Perjanjian Bungaya yang mengakhiri monopoli maritim bebas Gowa."},
            {"year": 1669, "event": "Jatuhnya Benteng Somba Opu setelah pertempuran artileri sengit berdarah selama berbulan-bulan."}
        ],
        "relics_and_heritage": [
            "Benteng Somba Opu (benteng induk berstruktur bata lempung raksasa)",
            "Istana Balla Lompoa di Sungguminasa",
            "Benteng Rotterdam (Benteng Ujung Pandang sebelum direbut VOC)",
            "Kompleks Makam Sultan Hasanuddin di Katangka",
            "Masjid Tua Katangka (Al-Hilal) dibangun 1603"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Kronologi sangat presisi berdasarkan naskah Lontara Bilang (buku catatan harian raja-raja Gowa dan Tallo), naskah Lontara Patturioloanga ri Gowa, dan arsip harian Cornelis Speelman.",
        "sources_ids": ["andaya-1981", "ricklefs-2008", "poesponegoro-notosusanto-2008", "reid-1993", "kemendikbud-cagarbudaya"],
        "sultans_count": 6
    },
    {
        "id": "bone",
        "name": "Kesultanan Bone",
        "alternate_names": ["Kerajaan Bone", "Tanete Bone"],
        "region": "Sulawesi",
        "year_founded": 1611,
        "year_founded_display": "1611 M (Masuk Islam) / 1330 M (Tradisional)",
        "year_ended": 1905,
        "year_ended_display": "1905 M (Perang Rumpia / Ekspedisi Bone Belanda)",
        "status_timeline_type": "ended",
        "founder": "La Tenriruwa (Sultan Adam) & La Ummasa",
        "capital_city": "Watampone, Bone, Sulawesi Selatan",
        "coordinates": {"lat": -4.5447, "lng": 120.3275},
        "golden_age": {
            "start_year": 1667,
            "end_year": 1696,
            "leader": "Arung Palakka (La Tenritatta To Unru Petta Malampe'e Gemme'na)",
            "description": "Menjadi kekuatan dominan terkuat di jazirah Sulawesi Selatan, membebaskan Bone dari dominasi Gowa, menegakkan sistem hukum adat Ade' Pitu, dan memperluas hegemoni politik melintasi Selat Flores dan Sumbawa."
        },
        "historical_summary": "Bone didirikan sekitar tahun 1330 oleh Manurungnge ri Matajang. Agama Islam diterima secara resmi pada 1611 pasca Perang Pengislaman (Musu Asellengeng) yang dilancarkan Gowa. Di bawah pimpinan Arung Palakka pada akhir abad ke-17, Bone bangkit menjadi kekuatan hegemoni utama di Sulawesi Selatan bersekutu dengan kompeni Belanda untuk meruntuhkan kekuasaan Gowa. Pada tahun 1905, Belanda melancarkan Ekspedisi Militer Bone yang mengakhiri kedaulatan kesultanan setelah Raja La Pawawoi Karaeng Segeri gugur/ditawan.",
        "key_events": [
            {"year": 1611, "event": "Raja Bone La Tenriruwa memeluk Islam dan digantikan oleh La Maddaremmeng yang menegakkan syariat Islam secara ketat."},
            {"year": 1667, "event": "Arung Palakka memimpin pasukan Bone bersama VOC mengalahkan Gowa dalam Perang Makassar."},
            {"year": 1672, "event": "Arung Palakka dinobatkan menjadi Mangkau' (Raja) Bone ke-15."},
            {"year": 1824, "event": "Perang Bone melawan ekspedisi Belanda yang dipimpin Jenderal Van Geen."},
            {"year": 1905, "event": "Pasukan Belanda menaklukkan benteng-benteng Bone; La Pawawoi Karaeng Segeri diasingkan ke Bandung."}
        ],
        "relics_and_heritage": [
            "Museum Bola Soba (Rumah Adat Besar Saoraja Bone)",
            "Kompleks Pemakaman Raja-Raja Bone di Bukaka",
            "Makam Pahlawan Nasional Arung Palakka di Bonto Biraeng",
            "Koleksi Salokoa (Mahkota Emas Bone) dan Keris Pusaka Teddung Pulaweng"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah terverifikasi naskah Lontara Akkarungeng ri Bone dan riset komprehensif Leonard Y. Andaya dalam The Heritage of Arung Palakka.",
        "sources_ids": ["andaya-1981", "ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 5
    },
    {
        "id": "buton",
        "name": "Kesultanan Buton",
        "alternate_names": ["Kesultanan Wolio", "Butung"],
        "region": "Sulawesi",
        "year_founded": 1538,
        "year_founded_display": "1538 M (Transformasi Islam) / 1332 M (Pra-Islam)",
        "year_ended": 1960,
        "year_ended_display": "1960 M (Wafatnya Sultan Falihi / Bergabung NKRI)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Lakilaponto (Sultan Murhum Kaimuddin Khalifatul Khamis)",
        "capital_city": "Baubau (Benteng Keraton Wolio), Pulau Buton, Sulawesi Tenggara",
        "coordinates": {"lat": -5.4658, "lng": 122.6178},
        "golden_age": {
            "start_year": 1580,
            "end_year": 1650,
            "leader": "Sultan Dayanu Ikhsanuddin (La Elangi)",
            "description": "Menyusun konstitusi ketatanegaraan Islam yang maju 'Undang-Undang Martabat Tujuh', membangun Benteng Keraton Wolio seluas 23,3 hektar (benteng keraton terluas di dunia versi Guinness World Records), dan mempertahankan kedaulatan mandiri di tengah kepungan hegemoni Ternate, Gowa, dan VOC."
        },
        "historical_summary": "Didirikan pada 1332 oleh empat orang pendiri suku Melayu, Buton bertransformasi menjadi kesultanan Islam pada 1538 ketika Raja ke-6 Lakilaponto masuk Islam dengan gelar Sultan Murhum. Kesultanan Buton memiliki sistem tata negara demokratis unik di mana sultan tidak diwariskan turun-temurun melainkan dipilih oleh dewan menteri Siolimbona berdasarkan kualifikasi moral dan kepemimpinan. Benteng Keraton Wolio yang megah berdiri kokoh di puncak bukit Baubau dengan tembok karang tanpa semen.",
        "key_events": [
            {"year": 1538, "event": "Lakilaponto masuk Islam atas bimbingan Syekh Abdul Wahid dan dinobatkan sebagai Sultan Murhum."},
            {"year": 1610, "event": "Sultan Dayanu Ikhsanuddin mengesahkan kitab konstitusi kerajaan Martabat Tujuh."},
            {"year": 1613, "event": "Perjanjian pertahanan bilateral dengan kongsi dagang VOC tanpa penyerahan hak monopoli kedaulatan tanah Buton."},
            {"year": 1750, "event": "Penyelesaian penyempurnaan dinding keliling Benteng Wolio dengan 16 kubu pertahanan (bastion) dan 12 pintu gerbang (lawa)."},
            {"year": 1960, "event": "Sultan Buton ke-38 Muhammad Falihi mangkat; Buton menyatu penuh ke dalam NKRI sebagai daerah otonom."}
        ],
        "relics_and_heritage": [
            "Benteng Keraton Wolio Baubau (Benteng terluas di dunia versi MURI & Guinness)",
            "Masjid Agung Keraton Buton (dibangun 1712 dengan tiang gantung)",
            "Kasulana Tombi (tiang bendera kayu jati setinggi 21 meter peninggalan 1712)",
            "Batu Popaua (tempat upacara pelantikan sumpah para sultan Buton)",
            "Naskah-naskah Kuno Martabat Tujuh dan aksara Buri Wolio"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Sistem perundang-undangan, silsilah 38 sultan, dan dokumen undang-undang terdata sangat sistematis dalam arsip naskah Wolio dan registrasi cagar budaya nasional.",
        "sources_ids": ["zahari-1977", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 5
    },
    {
        "id": "luwu-islam",
        "name": "Kedatuan Luwu (Fase Islam)",
        "alternate_names": ["Kerajaan Luwu", "Luwuq"],
        "region": "Sulawesi",
        "year_founded": 1605,
        "year_founded_display": "1605 M (Fase Islam) / Abad ke-13 (Sureq Galigo)",
        "year_ended": 1945,
        "year_ended_display": "1945 M (Integrasi Sukarela NKRI / Kultural)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Datu La Patiwareq Daeng Parabbung (Sultan Muhammad Wali Mu'zhiruddin)",
        "capital_city": "Palopo (Istana Datu Luwu), Sulawesi Selatan",
        "coordinates": {"lat": -2.9944, "lng": 120.1983},
        "golden_age": {
            "start_year": 1605,
            "end_year": 1660,
            "leader": "Datu La Patiwareq & Sultan Abdullah Matinroe ri Malangke",
            "description": "Menjadi kerajaan pertama di semenanjung barat Sulawesi Selatan yang menerima dakwah Islam secara damai dari Dato ri Bandang dan Dato Sulaiman, menjabat sebagai 'Payung Luwu' yang dituakan dan dihormati oleh seluruh konfederasi Bugis-Makassar."
        },
        "historical_summary": "Luwu dipandang sebagai kerajaan Bugis tertua yang menjadi latar epos agung sastra terpanjang dunia 'I La Galigo'. Pada Februari 1605, Datu Luwu La Patiwareq memeluk Islam atas dakwah ulama asal Minangkabau Dato Sulaiman (Khatib Sulaiman), mendahului konversi Gowa dan Bone. Pusat kedatuan kemudian berkedudukan di Palopo. Pada 1945, Datu Luwu Andi Djemma menyatakan sumpah setia kepada NKRI dan memimpin perjuangan rakyat Luwu mempertahankan kemerdekaan.",
        "key_events": [
            {"year": 1605, "event": "Datu La Patiwareq mengikrarkan Islam pada 4 Februari 1605 di Pattimang, Malangke."},
            {"year": 1604, "event": "Pembangunan Masjid Jami' Palopo beratap tumpang tiga dan bertiang kayu cinna gori."},
            {"year": 1945, "event": "Datu Luwu Andi Djemma memimpin Petisi Rakyat Luwu menyatakan bergabung dengan NKRI tanpa syarat."},
            {"year": 1946, "event": "Perlawanan bersenjata Semesta Rakyat Luwu meletus pada 23 Januari 1946 menentang tentara NICA Belanda."}
        ],
        "relics_and_heritage": [
            "Istana Datu Luwu di Kota Palopo",
            "Masjid Tua Palopo (dibangun 1604 dari susunan batu kali dan perekat putih telur)",
            "Kompleks Makam Kuno Pattimang di Malangke (Makam Datu La Patiwareq)",
            "Pusaka Salokoa dan Keris Kebesaran Luwu"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah terverifikasi dalam Lontara Sukku'na Tana Luwu, naskah I La Galigo, serta arsip kolonial Gouvernement van Celebes.",
        "sources_ids": ["andaya-1981", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 4
    },

    # ==========================================
    # MALUKU & PAPUA
    # ==========================================
    {
        "id": "ternate",
        "name": "Kesultanan Ternate",
        "alternate_names": ["Kerajaan Gapi", "Ternate"],
        "region": "Maluku & Papua",
        "year_founded": 1257,
        "year_founded_display": "1257 M (Gapi) / c. 1486 M (Fase Kesultanan)",
        "year_ended": None,
        "year_ended_display": "Masih Bertahan (Lembaga Adat & Budaya)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Baab Mashur Malamo (1257 M) / Sultan Marhum & Sultan Zainal Abidin (Islam)",
        "capital_city": "Pulau Ternate, Maluku Utara",
        "coordinates": {"lat": 0.7997, "lng": 127.3875},
        "golden_age": {
            "start_year": 1570,
            "end_year": 1583,
            "leader": "Sultan Baabullah (Penguasa 72 Pulau Berpenghuni)",
            "description": "Mengusir penjajah Portugis dari benteng Gamlamo (1575), memperluas federasi kemaharajaan maritim meliputi 72 pulau dari Maluku, Sulawesi Utara dan Tengah, Buton, Kepulauan Banggai, hingga perbatasan Filipina Selatan (Mindanao), dan memonopoli rempah cengkeh dunia."
        },
        "historical_summary": "Didirikan pada 1257 di lereng Gunung Gamalama, Ternate merupakan pemimpin persekutuan 'Uli Lima' di Maluku. Sultan Marhum dan putranya Sultan Zainal Abidin mentransformasikan monarki menjadi kesultanan Islam pada akhir abad ke-15 setelah menimba ilmu di Pesantren Giri Jawa. Pasca pembunuhan keji Sultan Khairun oleh kapten Portugis di dalam benteng, putranya Sultan Baabullah memimpin perang semesta selama 5 tahun hingga Portugis menyerah total pada 1575. Kedaton Sultan Ternate hingga kini berdiri megah memelihara pusaka kesultanan.",
        "key_events": [
            {"year": 1257, "event": "Musyawarah empat klan (Momole) mengangkat Baab Mashur Malamo sebagai Kolano Ternate pertama."},
            {"year": 1486, "event": "Sultan Zainal Abidin memperdalam syariat Islam ke Jawa dan mengganti gelar Kolano menjadi Sultan."},
            {"year": 1522, "event": "Portugis di bawah Antonio de Brito mulai membangun benteng pertahanan Sao Joao Baptista (Kastela)."},
            {"year": 1570, "event": "Sultan Khairun dibunuh secara licik oleh Portugis, memicu sumpah pembalasan Sultan Baabullah."},
            {"year": 1575, "event": "Pasukan Ternate berhasil merebut benteng Kastela dan mengusir penjajah Portugis selamanya dari Ternate."},
            {"year": 1579, "event": "Kunjungan navigator penjelajah Inggris Sir Francis Drake yang disambut ramah oleh Sultan Baabullah."}
        ],
        "relics_and_heritage": [
            "Kedaton Kesultanan Ternate di Bukit Limau",
            "Masjid Sultan Ternate (Masjid Sigi Lamo)",
            "Mahkota Berambut Emas Sultan Ternate (Pusaka keramat yang rambutnya terus memanjang)",
            "Benteng Kastela (Gamlamo) dan Benteng Tolukko",
            "Naskah surat diplomatik Sultan Ternate kepada Ratu Elizabeth I Inggris"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Terdokumentasi sangat luas dalam arsip nasional Portugis (Torre do Tombo), laporan Francis Drake, kronik Valentijn, dan naskah Hikayat Ternate.",
        "sources_ids": ["andaya-1993", "ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 6
    },
    {
        "id": "tidore",
        "name": "Kesultanan Tidore",
        "alternate_names": ["Kerajaan Limau Duko", "Tidore"],
        "region": "Maluku & Papua",
        "year_founded": 1081,
        "year_founded_display": "1081 M (Kolano) / c. 1495 M (Fase Kesultanan)",
        "year_ended": None,
        "year_ended_display": "Masih Bertahan (Lembaga Adat & Budaya)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Kolano Syahjati / Sultan Ciriliyati (Sultan Jamaluddin)",
        "capital_city": "Soasio, Pulau Tidore, Maluku Utara",
        "coordinates": {"lat": 0.6728, "lng": 127.4428},
        "golden_age": {
            "start_year": 1780,
            "end_year": 1805,
            "leader": "Sultan Nuku (Sri Paduka Maha Tuan Sultan Saidul Jehad el-Mabus Amiruddin Syah Kaicil Paparangan)",
            "description": "Pahlawan bahari agung yang tak pernah terkalahkan. Memimpin perang gerilya laut membebaskan Maluku dari penjajahan VOC, menyatukan kekuatan suku-suku Papua, Raja Ampat, Seram Timur, dan armada Inggris untuk memulihkan kedaulatan kedaulatan wilayah Tidore."
        },
        "historical_summary": "Tidore merupakan kekuatan utama persekutuan 'Uli Siwa' (Sembilan Persekutuan) di Kepulauan Maluku yang memiliki ikatan wilayah kekuasaan dan pertuanan luas meliputi pesisir Halmahera Timur, Seram, hingga pesisir daratan Papua dan Kepulauan Raja Ampat. Islam diterima secara resmi pada akhir abad ke-15 di bawah Sultan Ciriliyati. Tokoh paling legendaris adalah Sultan Nuku yang berjuang selama 25 tahun di lautan menentang kolonialisme VOC tanpa pernah terkalahkan hingga dinobatkan sebagai penguasa sah Tidore dan Seram.",
        "key_events": [
            {"year": 1081, "event": "Penobatan Kolano Syahjati di atas Pulau Tidore."},
            {"year": 1495, "event": "Sultan Ciriliyati masuk Islam dan memantapkan hubungan keagamaan dengan Kesultanan Malaka."},
            {"year": 1521, "event": "Armada kapal Spanyol ekspedisi Ferdinand Magellan-Juan Sebastian Elcano berlabuh di Tidore dan disambut Sultan Al-Mansur."},
            {"year": 1780, "event": "Pangeran Nuku dinobatkan oleh para raja Papua dan Seram Timur sebagai Sultan Amiruddin untuk memimpin perang melawan VOC."},
            {"year": 1797, "event": "Sultan Nuku berhasil merebut kembali takhta Tidore dari tangan boneka Belanda dan mengusir garnisun VOC."},
            {"year": 1801, "event": "Pasukan gabungan Nuku dan sekutu merebut Ternate dari Belanda, menyatukan seluruh Maluku."}
        ],
        "relics_and_heritage": [
            "Kedaton Kie Kesultanan Tidore di Soasio",
            "Benteng Torre dan Benteng Tahula peninggalan Spanyol",
            "Makam Pahlawan Nasional Sultan Nuku di Soasio",
            "Masjid Sultan Tidore (Sigi Kolano)",
            "Peti pusaka dan panji bendera perang Sultan Nuku"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Perjuangan Sultan Nuku dan silsilah Tidore terdokumentasi akurat dalam buku The World of Maluku oleh Leonard Y. Andaya dan arsip kolonial VOC.",
        "sources_ids": ["andaya-1993", "ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 5
    },
    {
        "id": "bacan",
        "name": "Kesultanan Bacan",
        "alternate_names": ["Bacan", "Kerajaan Kasiruta"],
        "region": "Maluku & Papua",
        "year_founded": 1322,
        "year_founded_display": "1322 M / 1557 M (Resmi Kesultanan Islam)",
        "year_ended": None,
        "year_ended_display": "Masih Bertahan (Lembaga Adat & Budaya)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Said Muhammad al-Bakir (Kolano Bacan) & Sultan Zainal Abidin",
        "capital_city": "Labuha, Pulau Bacan, Maluku Utara",
        "coordinates": {"lat": -0.6278, "lng": 127.4811},
        "golden_age": {
            "start_year": 1557,
            "end_year": 1600,
            "leader": "Sultan Zainal Abidin (1557–1577 M)",
            "description": "Menjadi pilar keempat persekutuan 'Maluku Kie Raha' (Empat Gunung Maluku), pusat penghasil rempah cengkeh dan pala di selatan Halmahera, serta pionir penyebaran ajaran Islam ke semenanjung Onin dan Papua Barat."
        },
        "historical_summary": "Merupakan salah satu dari empat pilar kemaharajaan 'Maluku Kie Raha' bersama Ternate, Tidore, dan Jailolo. Berawal di Pulau Kasiruta sebelum berpusat di Labuha, Bacan menerima Islam secara resmi pada 1557 melalui Sultan Zainal Abidin. Kesultanan Bacan memiliki pengaruh jaringan maritim penting ke kepulauan Maluku Selatan dan pesisir barat Papua. Keraton Bacan dan tradisi adatnya masih terus dirawat oleh masyarakat Pulau Bacan hingga saat ini.",
        "key_events": [
            {"year": 1322, "event": "Awal mula institusi monarki Bacan di Pulau Kasiruta."},
            {"year": 1557, "event": "Raja Bacan memeluk Islam dan berganti nama menjadi Sultan Zainal Abidin."},
            {"year": 1609, "event": "Perjanjian persahabatan awal antara Sultan Bacan dengan laksamana Belanda Paulus van Caerden."},
            {"year": 1780, "event": "Kesultanan Bacan mendukung persekutuan Sultan Nuku dalam menentang hegemoni VOC."}
        ],
        "relics_and_heritage": [
            "Kedaton Kesultanan Bacan di Labuha",
            "Masjid Tua Sultan Bacan",
            "Benteng Bernaveld peninggalan Portugis dan Belanda",
            "Koleksi mahkota dan keris kebesaran Kesultanan Bacan"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah terverifikasi dalam tradisi lisan Maluku Kie Raha dan naskah catatan VOC Valentijn.",
        "sources_ids": ["andaya-1993", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 3
    },
    {
        "id": "rumbati-papua",
        "name": "Petuanan Islam Rumbati",
        "alternate_names": ["Kerajaan Rumbati", "Petuanan Onin"],
        "region": "Maluku & Papua",
        "year_founded": 1600,
        "year_founded_display": "c. 1600 M",
        "year_ended": 1950,
        "year_ended_display": "1950 M (Integrasi Pemerintahan RI / Status Adat)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Raja Patipi & Marga Bauw",
        "capital_city": "Rumbati, Semenanjung Onin, Fakfak, Papua Barat",
        "coordinates": {"lat": -2.8719, "lng": 132.3381},
        "golden_age": {
            "start_year": 1750,
            "end_year": 1880,
            "leader": "Raja Paduai & Raja Ismail Bauw",
            "description": "Menjadi episentrum syiar Islam dan pusat perniagaan pala kuskus (Myristica argentea) di pesisir barat tanah Papua, mengoordinasi petuanan-petuanan pesisir Onin dalam jaringan bahari Nusantara."
        },
        "historical_summary": "Semenanjung Onin di Kabupaten Fakfak, Papua Barat, memiliki sejarah panjang kerajaan-kerajaan Islam tradisional (petuanan) yang dipimpin oleh para 'Raja' Muslim. Kerajaan Rumbati merupakan yang terdepan di antara sembilan petuanan di Fakfak (seperti Fatagar, Ati-Ati, Patipi). Terjalin melalui ikatan kultural dan perdagangan rempah pala dengan Kesultanan Tidore dan pedagang Bugis-Seram, masyarakat Onin memelihara tradisi toleransi tinggi 'Satu Tungku Tiga Batu'. Masjid Tua Patimburak yang berdiri sejak 1870 membuktikan jejak peradaban Islam di bumi Papua.",
        "key_events": [
            {"year": 1600, "event": "Masuknya pengaruh Islam melalui jalur dakwah maritim mubaligh Banda dan utusan Kesultanan Tidore."},
            {"year": 1785, "event": "Penguatan struktur pemerintahan petuanan adat bergelar Raja di bawah naungan diplomasi Tidore."},
            {"year": 1870, "event": "Pembangunan Masjid Tua Patimburak oleh Raja Pertuanan Wertuar di pesisir Fakfak."},
            {"year": 1898, "event": "Pemerintah Hindia Belanda mendirikan pos administratif Fakfak dan mengakui kedaulatan adat petuanan Rumbati."}
        ],
        "relics_and_heritage": [
            "Masjid Tua Patimburak di Distrik Kokas, Fakfak (arsitektur khas Eropa dan kubah masjid)",
            "Rumah Raja Rumbati di Distrik Teluk Patipi",
            "Naskah Al-Qur'an Kuno tulisan tangan di atas kulit kayu di Semenanjung Onin",
            "Makam Kuno para mubaligh dan Raja Rumbati di pesisir Fakfak"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Dikonfirmasi melalui kajian arkeologi Balai Arkeologi Maluku-Papua (Syahruddin Mansyur 2016), arsip kolonial Memorie van Overgave Fakfak, dan silsilah klan dinasti Bauw.",
        "sources_ids": ["mansyur-2016", "andaya-1993", "kemendikbud-cagarbudaya"],
        "sultans_count": 3
    },
    {
        "id": "misool-papua",
        "name": "Kerajaan Islam Misool",
        "alternate_names": ["Petuanan Misool", "Lilinta Misool"],
        "region": "Maluku & Papua",
        "year_founded": 1650,
        "year_founded_display": "c. 1650 M",
        "year_ended": 1950,
        "year_ended_display": "1950 M (Integrasi Pemerintahan RI / Status Adat)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Fun Bis (Marga Umkabu)",
        "capital_city": "Lilinta, Pulau Misool, Kepulauan Raja Ampat, Papua Barat Daya",
        "coordinates": {"lat": -1.8833, "lng": 130.2833},
        "golden_age": {
            "start_year": 1750,
            "end_year": 1830,
            "leader": "Fun Abdul Majid & Fun Malan",
            "description": "Menjadi salah satu dari empat kerajaan kepulauan agung (Raja Ampat: Misool, Salawati, Batanta, Waigeo) yang menjamin keamanan pelayaran maritim, mengelola perniagaan mutiara, teripang, dan burung cenderawasih."
        },
        "historical_summary": "Kerajaan Misool merupakan salah satu dari 'Empat Raja' (Raja Ampat) di barat daya kepala burung Papua. Dipimpin oleh penguasa adat bergelar 'Fun' atau 'Kalana' dari marga Umkabu yang berkedudukan di Lilinta. Pengaruh Islam berakar kuat melalui persahabatan dan ikatan vasal diplomatik dengan Kesultanan Bacan dan Tidore. Kerajaan Misool bersama para petuanan kepulauan lainnya memainkan peranan vital dalam membantu armada Sultan Nuku menghadapi kolonialisasi di perairan Maluku-Papua.",
        "key_events": [
            {"year": 1650, "event": "Fun Bis diangkat sebagai penguasa Lilinta dan mengadopsi ajaran syariat Islam."},
            {"year": 1710, "event": "Hubungan perniagaan rempah dan hasil laut berkembang dengan Kesultanan Tidore."},
            {"year": 1790, "event": "Raja Misool mengerahkan armada perahu kora-kora untuk memperkuat armada perlawanan bahari Sultan Nuku."},
            {"year": 1911, "event": "Pemerintah kolonial Hindia Belanda mengukuhkan surat keputusan pengakuan wilayah adat Petuanan Misool."}
        ],
        "relics_and_heritage": [
            "Situs Istana Kampung Lilinta di Pulau Misool",
            "Makam-makam kuno bertuliskan huruf Arab-Melayu di Misool Selatan",
            "Meriam-meriam kuno peninggalan armada kesultanan",
            "Cap stempel perak Kerajaan Misool"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Silsilah terverifikasi dalam penelitian Balai Arkeologi Papua, catatan perjalanan ekspedisi D.F. van Braam Morris (1884), dan arsip Kesultanan Tidore.",
        "sources_ids": ["mansyur-2016", "andaya-1993", "poesponegoro-notosusanto-2008"],
        "sultans_count": 3
    },

    # ==========================================
    # NUSA TENGGARA
    # ==========================================
    {
        "id": "bima",
        "name": "Kesultanan Bima",
        "alternate_names": ["Kerajaan Mbojo", "Bima"],
        "region": "Nusa Tenggara",
        "year_founded": 1621,
        "year_founded_display": "1621 M (7 Februari 1621 M)",
        "year_ended": 1958,
        "year_ended_display": "1958 M (Integrasi Swapraja ke Provinsi NTB / Museum Asi Mbojo)",
        "status_timeline_type": "cultural_continuation",
        "founder": "La Ka'i (Sultan Abdul Kahir I)",
        "capital_city": "Kota Bima (Istana Asi Mbojo), Sumbawa Timur, NTB",
        "coordinates": {"lat": -8.4594, "lng": 118.7275},
        "golden_age": {
            "start_year": 1640,
            "end_year": 1696,
            "leader": "Sultan Abdul Khair Sirajuddin & Sultan Nuruddin",
            "description": "Menjadi poros peradaban dan syiar Islam terkuat di Kepulauan Nusa Tenggara. Wilayah pengaruhnya meluas meliputi Manggarai (Flores Barat), Sumba, Solor, dan Alor. Memiliki sistem arsip naskah istana tertulis 'Bo' Sangaji Kai' yang sangat rapi."
        },
        "historical_summary": "Didirikan sebagai kerajaan tradisional Mbojo, Bima resmi bertransformasi menjadi kesultanan Islam pada 7 Februari 1621 ketika Raja ke-37 La Ka'i memeluk Islam bergelar Sultan Abdul Kahir I setelah dibimbing mubaligh asal Luwu dan Makassar. Bima memiliki hubungan aliansi persaudaraan darah yang sangat erat dengan Kesultanan Gowa. Arsip harian istana 'Bo' Sangaji Kai' merupakan dokumen historiografi terlengkap di Nusa Tenggara. Istana megah Asi Mbojo kini diabadikan sebagai Museum Kebudayaan Bima.",
        "key_events": [
            {"year": 1621, "event": "La Ka'i resmi mengikrarkan dua kalimat syahadat dan ditabalkan sebagai Sultan Abdul Kahir I."},
            {"year": 1640, "event": "Sultan Abdul Khair Sirajuddin menikahi saudara perempuan Sultan Hasanuddin Gowa, memperkokoh aliansi militer."},
            {"year": 1669, "event": "Bima menjadi tempat suaka para pejuang Makassar pasca jatuhnya Somba Opu."},
            {"year": 1927, "event": "Pembangunan Istana megah Asi Mbojo oleh Sultan Muhammad Salahuddin memadukan gaya Melayu, Bima, dan Belanda."},
            {"year": 1958, "event": "Sultan Muhammad Salahuddin wafat; Bima melebur secara sukarela menjadi daerah otonom Kabupaten dan Kota Bima."}
        ],
        "relics_and_heritage": [
            "Museum Istana Asi Mbojo di Kota Bima",
            "Naskah Manuskrip Bo' Sangaji Kai (catatan harian kesultanan terlengkap)",
            "Masjid Sultan Muhammad Salahuddin di Bima",
            "Kompleks Pemakaman Raja-Raja Bima di Tolobali",
            "Mahkota Emas dan Senjata Pusaka Kesultanan Bima"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Historiografi Bima memiliki kepastian sangat tinggi berkat naskah catatan resmi istana Bo' Sangaji Kai yang diteliti oleh Henri Chambert-Loir dan Siti Maryam Salahuddin.",
        "sources_ids": ["chambert-loir-salahuddin-1999", "ricklefs-2008", "poesponegoro-notosusanto-2008", "kemendikbud-cagarbudaya"],
        "sultans_count": 6
    },
    {
        "id": "sumbawa",
        "name": "Kesultanan Sumbawa",
        "alternate_names": ["Tana Samawa", "Sumbawa"],
        "region": "Nusa Tenggara",
        "year_founded": 1674,
        "year_founded_display": "1674 M (Fase Kesultanan Islam)",
        "year_ended": 1958,
        "year_ended_display": "1958 M (Integrasi Swapraja NTB / Kultural)",
        "status_timeline_type": "cultural_continuation",
        "founder": "Dewa Maja Paruwa (Sultan Harunnurrasyid I)",
        "capital_city": "Sumbawa Besar (Istana Dalam Loka), Sumbawa Barat, NTB",
        "coordinates": {"lat": -8.4975, "lng": 117.4208},
        "golden_age": {
            "start_year": 1700,
            "end_year": 1760,
            "leader": "Sultan Muhammad Jalaluddin Syah I",
            "description": "Menata perekonomian berbasis pertanian, kuda sumbawa, madu hutan, dan kayu sepang. Membangun tata kelola hukum adat syarak yang harmonis serta menjalin hubungan persaudaraan erat dengan Banjar dan Makassar."
        },
        "historical_summary": "Sebelum memeluk Islam, wilayah Sumbawa bagian barat terbagi atas kepangeranan-kepangeranan seperti Seran, Taliwang, dan Jelimung. Islam masuk secara intensif melalui hubungan erat dengan Kesultanan Gowa pada abad ke-17. Kesultanan Sumbawa berdiri mandiri setelah Perjanjian Bungaya dan dipimpin oleh dinasti yang terhubung dengan Makassar dan Banjar. Istana Dalam Loka yang dibangun pada 1885 dengan konstruksi 99 tiang kayu jati tanpa paku besi kini menjadi kebanggaan cagar budaya nasional.",
        "key_events": [
            {"year": 1674, "event": "Dewa Maja Paruwa ditabalkan sebagai Sultan Harunnurrasyid I Kesultanan Sumbawa."},
            {"year": 1815, "event": "Letusan dahsyat Gunung Tambora meluluhlantakkan sebagian besar populasi dan lahan pertanian di Sumbawa."},
            {"year": 1885, "event": "Pembangunan Istana megah Dalam Loka oleh Sultan Muhammad Jalaluddin Syah III."},
            {"year": 1958, "event": "Sultan Muhammad Kaharuddin III mengikrarkan integrasi swapraja Sumbawa ke dalam Negara Kesatuan RI."}
        ],
        "relics_and_heritage": [
            "Istana Dalam Loka di Sumbawa Besar (istana kayu panggung megah dengan 99 tiang)",
            "Masjid Jami' Nurul Huda Sumbawa Besar",
            "Bala Kuning (tempat penyimpanan pusaka keraton)",
            "Kompleks Makam Sultan-Sultan Sumbawa di Sampar"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Tinggi",
        "certainty_notes": "Terdokumentasi dalam naskah hukum adat Lontar Sumbawa dan arsip kolonial Hindia Belanda.",
        "sources_ids": ["poesponegoro-notosusanto-2008", "chambert-loir-salahuddin-1999", "kemendikbud-cagarbudaya"],
        "sultans_count": 4
    },
    {
        "id": "selaparang",
        "name": "Kerajaan Selaparang (Islam)",
        "alternate_names": ["Selaparang", "Lombok Islam"],
        "region": "Nusa Tenggara",
        "year_founded": 1520,
        "year_founded_display": "c. 1520 M (Islam c. pertengahan abad ke-16)",
        "year_ended": 1740,
        "year_ended_display": "c. 1740 M (Ditundukkan oleh aliansi Karangasem Bali)",
        "status_timeline_type": "ended",
        "founder": "Raden Mas Panji Tilar Negara / Sunan Prapen (Dakwah Islam)",
        "capital_city": "Selaparang, Pringgabaya, Lombok Timur, NTB",
        "coordinates": {"lat": -8.5306, "lng": 116.5444},
        "golden_age": {
            "start_year": 1580,
            "end_year": 1650,
            "leader": "Prabu Rangkesari",
            "description": "Menjadi episentrum peradaban dan pusat dakwah Islam di Pulau Lombok, menjalin persekutuan pertahanan laut dengan Kesultanan Gowa untuk membendung ekspansi militer dari arah barat."
        },
        "historical_summary": "Kerajaan Selaparang di Pulau Lombok mengalami gelombang islamisasi pada pertengahan abad ke-16 melalui dakwah Sunan Prapen dari Giri Kedaton Jawa Timur. Selaparang berkembang menjadi kerajaan Islam yang memegang peranan kunci di Selat Alas. Menghadapi ancaman ekspansi kerajaan Karangasem Bali, Selaparang menjalin aliansi militer dengan Kesultanan Gowa. Pada abad ke-18, setelah pertempuran panjang dan pengkhianatan internal, Selaparang runtuh di bawah tekanan dinasti Karangasem.",
        "key_events": [
            {"year": 1545, "event": "Sunan Prapen dari Giri Kedaton memimpin ekspedisi dakwah ke Pulau Lombok, mengislamkan para bangsawan Selaparang."},
            {"year": 1648, "event": "Selaparang memperkuat hubungan pertahanan militer dengan Kesultanan Gowa menghadapi serbuan dari arah Bali."},
            {"year": 1678, "event": "Pusat pemerintahan sempat dipindahkan ke Sumbawa Barat saat tekanan militer meningkat."},
            {"year": 1740, "event": "Kerajaan Karangasem merebut benteng Selaparang, mengakhiri kekuasaan dinasti Islam Selaparang di Lombok."}
        ],
        "relics_and_heritage": [
            "Kompleks Makam Keramat Selaparang di Desa Selaparang, Lombok Timur",
            "Masjid Kuno Bayan Beleq di Lombok Utara (simbol awal masuknya Islam di Lombok)",
            "Batu Nisan bertuliskan huruf Arab-Jawa (Pegon) kuno",
            "Naskah Lontar Babad Selaparang"
        ],
        "verification_status": "Terverifikasi Akademik",
        "data_certainty_level": "Sedang",
        "certainty_notes": "Historiografi bertumpu pada naskah Lontar Babad Selaparang, Babad Lombok, dan laporan ekspedisi VOC di Kepulauan Sunda Kecil.",
        "sources_ids": ["poesponegoro-notosusanto-2008", "graaf-pigeaud-2001", "kemendikbud-cagarbudaya"],
        "sultans_count": 3
    }
]

# Write kingdoms_data to data/kingdoms.json
with open(r"c:\Users\TengQ\antigravity\webgis-islamic-history\data\kingdoms.json", "w", encoding="utf-8") as f:
    json.dump(kingdoms_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated data/kingdoms.json with {len(kingdoms_data)} kingdoms.")
