# -*- coding: utf-8 -*-
"""
Generates verified academic sultan records for data/sultans.json
"""
import json

sultans_data = [
    # ----------------------------------------------------
    # SAMUDERA PASAI
    # ----------------------------------------------------
    {
        "id": "pasai-1",
        "kingdom_id": "samudera-pasai",
        "order": 1,
        "name": "Sultan Malik as-Saleh (Meurah Silu)",
        "reign_start": 1267,
        "reign_end": 1297,
        "reign_display": "1267 – 1297 M",
        "biography": "Pendiri dinasti Kesultanan Samudera Pasai. Semula bernama Meurah Silu, seorang kepala suku di daerah Samudera. Memeluk Islam setelah berjumpa Syaikh Ismail dari Mekkah dan mentransformasikan Pasai menjadi kesultanan Islam pelopor di Nusantara.",
        "key_achievements": [
            "Mendirikan Kesultanan Samudera Pasai dan meletakkan dasar hukum Islam mazhab Syafi'i",
            "Menyatukan permukiman Samudera dan Pasai menjadi satu pusat kesultanan maritim",
            "Menjalin diplomasi dengan para musafir dunia, termasuk Marco Polo (1292 M)"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Wafat pada bulan Ramadhan 696 H (1297 M) sebagaimana dipahatkan pada nisan makamnya di Beuringen, Geudong."
    },
    {
        "id": "pasai-2",
        "kingdom_id": "samudera-pasai",
        "order": 2,
        "name": "Sultan Muhammad Malik az-Zahir",
        "reign_start": 1297,
        "reign_end": 1326,
        "reign_display": "1297 – 1326 M",
        "biography": "Putra sulung Sultan Malik as-Saleh. Terkenal sebagai administrator ulung yang mencetak mata uang dirham emas pertama di Nusantara dengan kadar kemurnian tinggi.",
        "key_achievements": [
            "Mencetak mata uang resmi kerajaan 'Deureuham' berbahan emas murni 70%",
            "Memperkuat pertahanan armada maritim di Selat Malaka",
            "Mengembangkan bandar Pasai menjadi pusat transit perdagangan lada dan sutra"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Koleksi koin emasnya kini tersimpan di Museum Samudera Pasai dan Museum Nasional."
    },
    {
        "id": "pasai-3",
        "kingdom_id": "samudera-pasai",
        "order": 3,
        "name": "Sultan Ahmad Malik az-Zahir",
        "reign_start": 1326,
        "reign_end": 1348,
        "reign_display": "1326 – 1348 M",
        "biography": "Memerintah pada puncak kejayaan Pasai. Menyambut pengembara kenamaan Maroko Ibnu Battuta pada 1345–1346 M. Dicatat oleh Ibnu Battuta sebagai penguasa yang amat tawadhu, mencintai para ulama, gemar bermusyawarah agama, dan sangat kuat menjaga shalat berjamaah.",
        "key_achievements": [
            "Menjadikan istana Pasai sebagai pusat perdebatan teologi dan fikih mazhab Syafi'i Asia Tenggara",
            "Menerima duta penjelajah Ibnu Battuta dan membekalinya kapal untuk berlayar ke Tiongkok",
            "Mengekspor puluhan ribu ton komoditas lada dan kapur barus ke Semenanjung Arab dan India"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Kesaksian primer dicatat langsung dalam Rihlah Ibn Battuta Bab Kepulauan Hindia."
    },
    {
        "id": "pasai-4",
        "kingdom_id": "samudera-pasai",
        "order": 4,
        "name": "Sultan Zainal Abidin Malik az-Zahir I",
        "reign_start": 1348,
        "reign_end": 1383,
        "reign_display": "1348 – 1383 M",
        "biography": "Melanjutkan era kemakmuran Pasai, namun harus menghadapi ekspedisi angkatan laut kemaharajaan Majapahit sekitar tahun 1360 M. Mampu mempertahankan eksistensi kedaulatan kota bandar Pasai.",
        "key_achievements": [
            "Memulihkan stabilitas perekonomian pelabuhan pasca serangan armada Majapahit",
            "Memperluas jejaring dakwah Islam ke pesisir Semenanjung Melayu",
            "Memperkokoh hubungan perniagaan laut dengan Kesultanan Delhi di India"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Disebutkan dalam Hikayat Raja-Raja Pasai dan naskah Nagarakretagama."
    },
    {
        "id": "pasai-5",
        "kingdom_id": "samudera-pasai",
        "order": 5,
        "name": "Sultanah Ratu Nahrasiyah",
        "reign_start": 1406,
        "reign_end": 1428,
        "reign_display": "1406 – 1428 M",
        "biography": "Ratu terkemuka Samudera Pasai yang memerintah dengan keadilan dan kemakmuran. Menerima kedatangan armada raksasa Laksamana Zheng He (Cheng Ho) dari Kekaisaran Ming Tiongkok dan menjalin hubungan persahabatan bilateral.",
        "key_achievements": [
            "Menjaga netralitas dan stabilitas politik bandar Pasai di tengah kebangkitan Malaka",
            "Menerima kunjungan muhibah Laksamana Cheng Ho yang mempersembahkan Lonceng Cakra Donya",
            "Makamnya memiliki nisan marmer Cambay terindah dan termahal di Asia Tenggara"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Wafat pada 17 Dzulhijjah 831 H (1428 M). Nisan marmernya memuat petikan Ayat Kursi dan Surat Yasin dengan kaligrafi relief tinggi."
    },
    {
        "id": "pasai-6",
        "kingdom_id": "samudera-pasai",
        "order": 6,
        "name": "Sultan Zainal Abidin IV",
        "reign_start": 1514,
        "reign_end": 1521,
        "reign_display": "1514 – 1521 M",
        "reign_end_detail": "Gugur/lengser akibat agresi militer armada Portugis di bawah Jorge de Albuquerque.",
        "biography": "Sultan terakhir Samudera Pasai sebelum wilayahnya dianeksasi oleh Kesultanan Aceh Darussalam.",
        "key_achievements": [
            "Memimpin pertahanan rakyat Pasai menghadapi gempuran armada perang Portugis",
            "Mengamankan para ulama dan penduduk ke pedalaman sebelum penggabungan ke Kesultanan Aceh"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Catatan Tome Pires dan Gaspar Correia menguraikan penaklukan Pasai oleh armada Portugis pada Mei 1521."
    },

    # ----------------------------------------------------
    # PERLAK
    # ----------------------------------------------------
    {
        "id": "perlak-1",
        "kingdom_id": "perlak",
        "order": 1,
        "name": "Sultan Sayyid Maulana Abdul Aziz Syah",
        "reign_start": 840,
        "reign_end": 864,
        "reign_display": "840 – 864 M (Tradisional)",
        "biography": "Penguasa pertama Kesultanan Perlak menurut naskah lokal 'Idharul Haq fi Mamlakatil Peureulak'. Putra dari Ali bin Muhammad bin Ja'far Shadiq yang menikah dengan Putri Makhdum Tansyuri.",
        "key_achievements": [
            "Mendirikan Kesultanan Perlak dan mengubah nama ibu kota menjadi Bandar Khalifah",
            "Menetapkan Islam sebagai syariat kerajaan (tradisi naskah lokal)",
            "Membuka perdagangan kayu perlak untuk kebutuhan galangan kapal pedagang Timur Tengah"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Tahun berkuasa berasal dari tradisi naskah lokal, belum ditemukan bukti epigrafi abad ke-9 yang sinkron."
    },
    {
        "id": "perlak-2",
        "kingdom_id": "perlak",
        "order": 2,
        "name": "Sultan Makhdum Alaiddin Malik Muhammad Amin Syah II",
        "reign_start": 1230,
        "reign_end": 1267,
        "reign_display": "c. 1230 – 1267 M",
        "biography": "Sultan Perlak ke-17 yang berhasil memadukan trah Sayyid dan Makhdum, membawa stabilitas ekonomi perniagaan lada dan rempah di pesisir Selat Malaka.",
        "key_achievements": [
            "Memulihkan stabilitas internal kesultanan pasca perselisihan aliran paham keagamaan",
            "Memperluas aliansi perniagaan dengan pedagang Gujarat, Persia, dan Yaman",
            "Menikahkan putrinya Putri Ratna Kamala dengan Raja Malaka dan Putri Ganggang Sari dengan Sultan Pasai"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Makamnya ditemukan di Desa Paya Meuligoe, Peureulak, Aceh Timur."
    },
    {
        "id": "perlak-3",
        "kingdom_id": "perlak",
        "order": 3,
        "name": "Sultan Makhdum Alaiddin Malik Abdul Aziz Syah Johan Berdaulat",
        "reign_start": 1267,
        "reign_end": 1292,
        "reign_display": "1267 – c. 1292 M",
        "biography": "Sultan terakhir Perlak. Pada masa pemerintahannya, Perlak dikunjungi oleh penjelajah Venesia Marco Polo (1292 M). Setelah mangkat, wilayah Perlak disatukan sepenuhnya ke dalam kedaulatan Samudera Pasai.",
        "key_achievements": [
            "Memimpin Perlak saat transisi unifikasi damai dengan Samudera Pasai",
            "Menerima singgahnya armada Marco Polo yang mencatat keberadaan kaum Muslim perkotaan di Ferlec"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Tercatat dalam The Travels of Marco Polo buku ke-3 bab 9 mengenai 'Kingdom of Ferlec'."
    },

    # ----------------------------------------------------
    # ACEH DARUSSALAM
    # ----------------------------------------------------
    {
        "id": "aceh-1",
        "kingdom_id": "aceh-darussalam",
        "order": 1,
        "name": "Sultan Ali Mughayat Syah",
        "reign_start": 1514,
        "reign_end": 1530,
        "reign_display": "1514 – 1530 M",
        "biography": "Pendiri dan peletak dasar kemaharajaan Kesultanan Aceh Darussalam. Berhasil mempersatukan kerajaan-kerajaan kecil di pesisir utara Aceh (Daya, Pidie, Pasai) dan memukul mundur garnisun militer Portugis.",
        "key_achievements": [
            "Menyatukan seluruh Aceh ke dalam satu kekuasaan terpusat di Kutaraja",
            "Mengusir pos-pos pertahanan Portugis dari Daya (1520), Pidie (1521), dan Pasai (1524)",
            "Menetapkan fondasi politik anti-kolonialisme di perairan Selat Malaka"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Batu nisannya di Kandang XII Kutaraja berangka tahun wafat 12 Dzulhijjah 936 H (1530 M)."
    },
    {
        "id": "aceh-2",
        "kingdom_id": "aceh-darussalam",
        "order": 2,
        "name": "Sultan Alauddin Riayat Syah al-Kahar",
        "reign_start": 1537,
        "reign_end": 1571,
        "reign_display": "1537 – 1571 M",
        "biography": "Sultan perkasa yang merintis hubungan diplomatik dan aliansi militer strategis dengan Khilafah Utsmaniyah (Ottoman) di bawah Sultan Suleiman Al-Qanuni dan Sultan Selim II.",
        "key_achievements": [
            "Mengirim utusan diplomatik ke Istanbul membawa upeti lada yang disambut hangat khalifah Ottoman",
            "Mendatangkan ratusan pandai besi, artileri meriam, dan tentara penembak mesiu dari Turki Utsmani",
            "Melancarkan serangan akbar berkali-kali mengepung benteng Portugis A Famosa di Malaka"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Arsip korespondensi diplomatik tersimpan di Museum Topkapi Istanbul dan tercatat dalam Bustanussalatin."
    },
    {
        "id": "aceh-3",
        "kingdom_id": "aceh-darussalam",
        "order": 3,
        "name": "Sultan Iskandar Muda (Meukuta Alam)",
        "reign_start": 1607,
        "reign_end": 1636,
        "reign_display": "1607 – 1636 M",
        "biography": "Penguasa terbesar dalam sejarah Kesultanan Aceh Darussalam. Di bawah pemerintahannya, Aceh mencapai puncak supremasi politik, ekonomi, militer, dan kebudayaan di seluruh Asia Tenggara.",
        "key_achievements": [
            "Memperluas kedaulatan Aceh meliputi pesisir barat-timur Sumatera hingga Semenanjung Melayu (Deli, Johor, Pahang, Kedah, Perak)",
            "Menyusun konstitusi dan tata hukum negara terpadu Adat Meukuta Alam",
            "Membangun Masjid Raya Baiturrahman pertama dan kompleks taman sari Gunongan",
            "Memiliki armada laut perkasa berisikan kapal perang raksasa berjuluk 'Espanto del Mundo' (Teror Dunia) yang memuat ratusan meriam"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Ditetapkan sebagai Pahlawan Nasional Indonesia berdasarkan Keppres No. 077/TK/1993."
    },
    {
        "id": "aceh-4",
        "kingdom_id": "aceh-darussalam",
        "order": 4,
        "name": "Sultan Iskandar Thani (Alauddin Mughayat Syah)",
        "reign_start": 1636,
        "reign_end": 1641,
        "reign_display": "1636 – 1641 M",
        "biography": "Putra Sultan Pahang yang diangkat anak dan menjadi menantu Sultan Iskandar Muda. Memerintah dengan penekanan pada pengembangan ilmu pengetahuan dan syariat Islam yang mendalam.",
        "key_achievements": [
            "Mengangkat ulama besar Syaikh Nuruddin ar-Raniri sebagai mufti agung kesultanan (Qadhi Malikul Adil)",
            "Mendukung penulisan kitab ensiklopedia sejarah dan adab kenegaraan termasyhur 'Bustan al-Salatin'",
            "Memelihara stabilitas perdamaian dan kemakmuran perniagaan bandar Aceh"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Wafat pada 15 Februari 1641 M dan dimakamkan di samping makam Sultan Iskandar Muda."
    },
    {
        "id": "aceh-5",
        "kingdom_id": "aceh-darussalam",
        "order": 5,
        "name": "Sultanah Safiatuddin Tajul Alam",
        "reign_start": 1641,
        "reign_end": 1675,
        "reign_display": "1641 – 1675 M",
        "biography": "Putri sulung Sultan Iskandar Muda dan janda Sultan Iskandar Thani. Merupakan penguasa wanita (Sultanah) pertama yang memimpin Kesultanan Aceh Darussalam selama 34 tahun dengan penuh kearifan.",
        "key_achievements": [
            "Membuktikan kepemimpinan perempuan dalam sistem ketatanegaraan Islam yang maju",
            "Mendukung ulama sufi Syaikh Abdurrauf as-Singkili menulis tafsir Al-Qur'an bahasa Melayu pertama 'Tarjuman al-Mustafid'",
            "Mempertahankan kedaulatan Aceh dari tekanan monopoli dagang VOC dan pedagang Eropa"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Era kepemimpinannya mengawali zaman empat sultanah berturut-turut di Aceh hingga 1699 M."
    },
    {
        "id": "aceh-6",
        "kingdom_id": "aceh-darussalam",
        "order": 6,
        "name": "Sultan Alauddin Ibrahim Mansur Syah",
        "reign_start": 1857,
        "reign_end": 1870,
        "reign_display": "1857 – 1870 M",
        "biography": "Memerintah pada masa genting ketika kekuatan kolonial Belanda mulai mengepung Aceh pasca Traktat Sumatera 1871. Mengirim utusan ke Turki Utsmani, Prancis, dan Amerika Serikat untuk menegaskan status kedaulatan Aceh.",
        "key_achievements": [
            "Menggalang dukungan diplomatik internasional menghadapi ancaman agresi militer Belanda",
            "Memperkuat benteng pertahanan pantai Kutaraja dan mempersiapkan persenjataan rakyat"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Dokumen perutusan ke Konstantinopel tercatat dalam arsip Kementerian Luar Negeri Utsmaniyah."
    },
    {
        "id": "aceh-7",
        "kingdom_id": "aceh-darussalam",
        "order": 7,
        "name": "Sultan Alauddin Mahmud Syah II",
        "reign_start": 1870,
        "reign_end": 1874,
        "reign_display": "1870 – 1874 M",
        "biography": "Sultan yang memimpin Aceh ketika Belanda secara resmi menyatakan maklumat perang pada 26 Maret 1873. Pasukan Aceh di bawah arahannya berhasil menewaskan Mayor Jenderal J.H.R. Kohler di pelataran Masjid Baiturrahman.",
        "key_achievements": [
            "Memimpin perlawanan mempertahankan ibu kota dalam Agresi Militer Belanda I (1873)",
            "Menghancurkan moral tentara penyerang Belanda dengan menewaskan panglima perangnya",
            "Menolak mentah-mentah ultimatum penyerahan kedaulatan kepada Batavia"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Wafat karena wabah kolera di Lueng Bata pada 28 Januari 1874 saat perang berkecamuk."
    },
    {
        "id": "aceh-8",
        "kingdom_id": "aceh-darussalam",
        "order": 8,
        "name": "Sultan Muhammad Daud Syah",
        "reign_start": 1874,
        "reign_end": 1903,
        "reign_display": "1874 – 1903 M",
        "biography": "Sultan berdaulat terakhir Kesultanan Aceh Darussalam. Dinobatkan di Masjid Indrapuri saat masih belia dan memimpin perang gerilya semesta bersama Teuku Umar, Panglima Polem, dan Cut Nyak Dhien dari hutan belantara.",
        "key_achievements": [
            "Memimpin perang semesta gerilya selama hampir tiga dekade menentang Belanda",
            "Menolak menyerah secara sukarela hingga keluarganya ditawan secara licik oleh Marsose",
            "Diasingkan ke Ambon dan Batavia hingga wafatnya pada 1939 tanpa pernah menjual kedaulatan Aceh"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Dimakamkan di TPU Rawamangun Jakarta. Belanda secara administratif mengklaim Aceh takluk pada 1904, namun perlawanan ulama berlanjut hingga 1913."
    },

    # ----------------------------------------------------
    # DEMAK
    # ----------------------------------------------------
    {
        "id": "demak-1",
        "kingdom_id": "demak",
        "order": 1,
        "name": "Raden Patah (Sultan Syah Alam Akbar I)",
        "reign_start": 1475,
        "reign_end": 1518,
        "reign_display": "1475 – 1518 M",
        "biography": "Pendiri Kesultanan Demak Bintoro. Berdarah bangsawan Majapahit (putra Kertabhumi/Brawijaya V) dan ibunda putri Champa/Tionghoa (Siu Ban Ci). Berguru kepada Sunan Ampel dan membuka hutan Glagah Wangi menjadi pusat daulah Islam Jawa.",
        "key_achievements": [
            "Mendirikan Kesultanan Demak sebagai kerajaan Islam berdaulat pertama di Pulau Jawa",
            "Membangun Masjid Agung Demak bersama majelis Walisongo sebagai poros peradaban",
            "Mempersiapkan angkatan laut tangguh pesisir utara menentang ekspansi Portugis di Malaka"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Dikonfirmasi oleh catatan Tome Pires dalam Suma Oriental yang menyebutnya 'Pate Rodim, senhor de Demak'."
    },
    {
        "id": "demak-2",
        "kingdom_id": "demak",
        "order": 2,
        "name": "Pati Unus (Pangeran Sabrang Lor / Adipati Yunus)",
        "reign_start": 1518,
        "reign_end": 1521,
        "reign_display": "1518 – 1521 M",
        "biography": "Menantu/putra Raden Patah, panglima laut legendaris yang memimpin armada gabungan Jawa menyerang benteng Portugis di Malaka pada 1513 dan 1521. Mendapat julukan 'Pangeran Sabrang Lor' karena keberaniannya menyeberangi lautan ke utara.",
        "key_achievements": [
            "Membangun armada laut berkekuatan 100 kapal jung raksasa buatan Jepara dan Rembang",
            "Menggempur benteng Portugis di Malaka sebagai wujud solidaritas persaudaraan Islam maritim",
            "Memperkokoh kedaulatan laut Jawa dari ancaman armada barat"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Catatan armada perangnya dicatat secara kagum oleh sejarawan Portugis Fernao Pires de Andrade."
    },
    {
        "id": "demak-3",
        "kingdom_id": "demak",
        "order": 3,
        "name": "Sultan Trenggana",
        "reign_start": 1521,
        "reign_end": 1546,
        "reign_display": "1521 – 1546 M",
        "biography": "Adik Pati Unus yang membawa Demak ke puncak keemasan teritorial dan kekuasaan politik di Pulau Jawa. Dinobatkan oleh Sunan Gunung Jati dengan gelar Sultan Ahmad Abdul Arifin.",
        "key_achievements": [
            "Memperluas kedaulatan Demak ke Jawa Barat (Banten, Sunda Kelapa/Jayakarta, Cirebon) dan Jawa Timur (Pasuruan, Tuban, Madiun, Malang)",
            "Menugaskan Fatahillah mengusir Portugis dari Sunda Kelapa pada 22 Juni 1527",
            "Membina kemakmuran pertanian dan perdagangan bandar pesisir Nusantara"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Gugur dalam ekspedisi militer pengepungan benteng Panarukan pada 1546 M."
    },
    {
        "id": "demak-4",
        "kingdom_id": "demak",
        "order": 4,
        "name": "Sunan Prawoto (Raden Mukmin)",
        "reign_start": 1546,
        "reign_end": 1549,
        "reign_display": "1546 – 1549 M",
        "biography": "Putra sulung Sultan Trenggana. Lebih berminat pada kehidupan tasawuf dan keilmuan agama daripada administrasi kekuasaan politik praktis. Terbunuh dalam konflik dendam keluarga oleh utusan Arya Penangsang.",
        "key_achievements": [
            "Meneruskan tradisi pengkajian naskah keagamaan di keraton Demak",
            "Berusaha meredam ketegangan politik antar cabang dinasti"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Babad Tanah Jawi mencatat wafatnya di Prawoto akibat keris Kiai Setan Kober."
    },
    {
        "id": "demak-5",
        "kingdom_id": "demak",
        "order": 5,
        "name": "Arya Penangsang (Adipati Jipang)",
        "reign_start": 1549,
        "reign_end": 1554,
        "reign_display": "1549 – 1554 M",
        "biography": "Adipati Jipang Panolan (cucu Raden Patah dari Pangeran Sekar Seda Lepen) yang menuntut takhta sah Demak. Murid kesayangan Sunan Kudus yang gagah berani berkuda Gagak Rimang, namun tewas dalam duel di Bengawan Sore melawan Joko Tingkir dan Sutawijaya.",
        "key_achievements": [
            "Menegakkan kendali kekuasaan dinasti Jipang atas wilayah inti Demak",
            "Menunjukkan kepiawaian bertempur dan kesaktian kanuragan legendaris dalam tradisi Jawa"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Kekalahannya pada 1554 M mengakhiri riwayat Demak dan mengawali era Kesultanan Pajang."
    },

    # ----------------------------------------------------
    # MATARAM ISLAM
    # ----------------------------------------------------
    {
        "id": "mataram-1",
        "kingdom_id": "mataram-islam",
        "order": 1,
        "name": "Panembahan Senapati (Danang Sutawijaya)",
        "reign_start": 1586,
        "reign_end": 1601,
        "reign_display": "1586 – 1601 M",
        "biography": "Pendiri Kesultanan Mataram Islam. Putra Ki Ageng Pamanahan dan anak angkat Sultan Hadiwijaya Pajang. Berhasil memerdekakan Mataram dari Pajang dan mendirikan keraton pertama di Kotagede.",
        "key_achievements": [
            "Mendirikan Kesultanan Mataram Islam dan meletakkan benteng bata cepuri di Kotagede",
            "Menundukkan adipati-adipati pesisir dan pedalaman (Kedu, Bagelen, Pajang, Demak, Madiun)",
            "Menolak gelar Sultan demi kerendahan hati, memilih gelar 'Panembahan Senapati ing Alaga Sayidin Panatagama'"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Dimakamkan di Kompleks Makam Raja-Raja Kotagede Yogyakarta."
    },
    {
        "id": "mataram-2",
        "kingdom_id": "mataram-islam",
        "order": 2,
        "name": "Panembahan Hanyakrawati (Seda ing Krapyak)",
        "reign_start": 1601,
        "reign_end": 1613,
        "reign_display": "1601 – 1613 M",
        "biography": "Putra Panembahan Senapati. Memerintah Mataram di tengah gejolak pemberontakan daerah pesisir utara dan Jawa Timur. Gemar berburu di hutan Krapyak hingga wafat di sana.",
        "key_achievements": [
            "Menumpas pemberontakan Pangeran Puger di Demak dan Pangeran Jayaraga di Ponorogo",
            "Menetapkan fondasi suksesi kepada putranya Raden Mas Rangsang (Sultan Agung)"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Dikenal dengan gelar anumerta Panembahan Seda ing Krapyak, dimakamkan di Kotagede."
    },
    {
        "id": "mataram-3",
        "kingdom_id": "mataram-islam",
        "order": 3,
        "name": "Sultan Agung Hanyakrakusuma",
        "reign_start": 1613,
        "reign_end": 1645,
        "reign_display": "1613 – 1645 M",
        "biography": "Raja terbesar dinasti Mataram. Pemimpin militer brilian, negarawan ulung, budayawan, dan ahli tarekat. Menyatukan hampir seluruh Pulau Jawa dan Madura, serta berani menantang kongsi dagang VOC di Batavia.",
        "key_achievements": [
            "Menyatukan Jawa Timur (Surabaya, Tuban, Pasuruan, Madura) dan pesisir barat ke bawah panji Mataram",
            "Mengorganisasi penyerbuan akbar mengepung benteng VOC Batavia pada 1628 dan 1629",
            "Menciptakan Kalender Jawa (Anno Javanico) dengan memadukan kalender Saka dan Hijriah",
            "Menggubah mahakarya tasawuf sastra Kitab Sastra Gendhing",
            "Membangun kompleks pemakaman agung Imogiri di puncak bukit Bantul"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Ditetapkan sebagai Pahlawan Nasional Indonesia berdasarkan Keppres No. 106/TK/1975."
    },
    {
        "id": "mataram-4",
        "kingdom_id": "mataram-islam",
        "order": 4,
        "name": "Susuhunan Amangkurat I (Sunan Tegalarum)",
        "reign_start": 1645,
        "reign_end": 1677,
        "reign_display": "1645 – 1677 M",
        "biography": "Putra Sultan Agung yang memindahkan keraton dari Karta ke Plered. Menjalankan pemerintahan sentralistik keras yang membantai ribuan ulama dan bersekutu dengan VOC, memicu pemberontakan besar Pangeran Trunajaya.",
        "key_achievements": [
            "Membangun keraton berbenteng batu bata merah raksasa di Plered",
            "Mengadakan perjanjian monopoli perdagangan beras dan candu dengan VOC (1646)"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Wafat dalam pelarian di Wanayasa setelah keraton Plered direbut Trunajaya, dimakamkan di Tegalarum, Tegal."
    },
    {
        "id": "mataram-5",
        "kingdom_id": "mataram-islam",
        "order": 5,
        "name": "Susuhunan Amangkurat II (Sunan Amral)",
        "reign_start": 1677,
        "reign_end": 1703,
        "reign_display": "1677 – 1703 M",
        "biography": "Mendirikan keraton baru di Kartasura pada 1680 setelah Plered runtuh. Meminta bantuan militer VOC di bawah Kapten Tack untuk menumpas Trunajaya dan Panembahan Giri Kedaton.",
        "key_achievements": [
            "Mendirikan ibu kota baru Keraton Kartasura",
            "Berhasil menyingkirkan Trunajaya dengan bantuan serdadu VOC dan Arung Palakka",
            "Secara diam-diam melindungi Untung Surapati yang menewaskan Kapten Tack di alun-alun Kartasura (1686)"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Dikenal dengan julukan Sunan Amral karena kerap berbusana mantel laksamana Belanda (Admiral)."
    },
    {
        "id": "mataram-6",
        "kingdom_id": "mataram-islam",
        "order": 6,
        "name": "Pakubuwana III (Raden Mas Suryadi)",
        "reign_start": 1749,
        "reign_end": 1755,
        "reign_display": "1749 – 1755 M (Mataram Tunggal)",
        "biography": "Raja Mataram terakhir sebelum pembagian kerajaan. Menghadapi Perang Tahta Jawa III melawan pamannya Pangeran Mangkubumi dan Raden Mas Said, yang akhirnya diselesaikan lewat Perjanjian Giyanti 1755.",
        "key_achievements": [
            "Menandatangani Perjanjian Giyanti (13 Februari 1755) yang membagi Mataram menjadi Kasunanan Surakarta dan Kasultanan Yogyakarta",
            "Meneruskan kepemimpinan sebagai Susuhunan Surakarta pertama pasca-Giyanti"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Perjanjian Giyanti mengakhiri eksistensi Mataram sebagai monarki tunggal di tanah Jawa."
    },

    # ----------------------------------------------------
    # BANTEN
    # ----------------------------------------------------
    {
        "id": "banten-1",
        "kingdom_id": "banten",
        "order": 1,
        "name": "Sultan Maulana Hasanuddin (Pangeran Sabakingkin)",
        "reign_start": 1552,
        "reign_end": 1570,
        "reign_display": "1552 – 1570 M",
        "biography": "Pendiri dan sultan pertama Kesultanan Banten. Putra Sunan Gunung Jati Cirebon dengan Nyai Kawunganten. Berhasil melepaskan Banten dari kekuasaan Kerajaan Pajajaran dan memperluas dakwah Islam hingga Lampung.",
        "key_achievements": [
            "Membangun kota pelabuhan Banten Lama, pasar Karangantu, dan Keraton Surosowan",
            "Mendirikan Masjid Agung Banten berarsitektur khas dengan menara mercusuar",
            "Menguasai Lampung dan Semenanjung Sunda sebagai sentra pemasok komoditas lada utama"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Wafat pada 1570 M dan dimakamkan di kompleks pemakaman Masjid Agung Banten Lama."
    },
    {
        "id": "banten-2",
        "kingdom_id": "banten",
        "order": 2,
        "name": "Sultan Maulana Yusuf (Pangeran Pasareyan)",
        "reign_start": 1570,
        "reign_end": 1580,
        "reign_display": "1570 – 1580 M",
        "biography": "Putra Maulana Hasanuddin. Pemimpin militer tangguh yang menuntaskan penaklukan Pakuan Pajajaran pada 1579, serta mempelopori pembangunan tata kota benteng bata dan sistem pengairan persawahan.",
        "key_achievements": [
            "Menaklukkan benteng Pakuan Pajajaran dan mengangkut batu Palangka Sriman Sriwacana ke Banten",
            "Membangun tembok keliling benteng kota Banten dari batu bata dan karang",
            "Membuat danau buatan Tasikardi untuk suplai air bersih istana dan persawahan rakyat"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Makamnya terletak di Kasunyatan Banten Lama."
    },
    {
        "id": "banten-3",
        "kingdom_id": "banten",
        "order": 3,
        "name": "Sultan Maulana Muhammad (Kanjeng Ratu Banten)",
        "reign_start": 1580,
        "reign_end": 1596,
        "reign_display": "1580 – 1596 M",
        "biography": "Naik takhta pada usia sangat belia didampingi Mangkubumi Jayanegara. Terkenal sangat saleh dan membangun banyak masjid madrasah. Gugur muda terkena tembakan saat memimpin ekspedisi ke Palembang.",
        "key_achievements": [
            "Memperbanyak penulisan mushaf Al-Qur'an dan kitab-kitab agama di lingkungan istana",
            "Melancarkan ekspedisi ke Palembang untuk menguasai jalur lalu lintas Selat Bangka"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Wafat pada 1596 M di Sungai Musi Palembang."
    },
    {
        "id": "banten-4",
        "kingdom_id": "banten",
        "order": 4,
        "name": "Sultan Abdul Mafakhir Mahmud Abdulkadir (Sultan Agung Banten)",
        "reign_start": 1596,
        "reign_end": 1651,
        "reign_display": "1596 – 1651 M",
        "biography": "Penguasa pertama di Pulau Jawa yang secara resmi dianugerahi gelar 'Sultan' langsung dari Syarif Mekkah pada 1638 M. Menghadapi kedatangan pertama armada Belanda Cornelis de Houtman (1596).",
        "key_achievements": [
            "Menerima pengakuan gelar Sultan dan panji kebesaran dari Syarif Zaid di Mekkah",
            "Mempertahankan kemerdekaan perniagaan Banten dari blokade laut VOC Batavia",
            "Mengembangkan produksi lada Lampung dan menjalin hubungan dagang dengan Inggris dan Prancis"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Daghregister VOC mencatat kegigihan diplomatik Sultan Abdul Mafakhir menjaga netralitas pelabuhan."
    },
    {
        "id": "banten-5",
        "kingdom_id": "banten",
        "order": 5,
        "name": "Sultan Ageng Tirtayasa (Pangeran Surya)",
        "reign_start": 1651,
        "reign_end": 1683,
        "reign_display": "1651 – 1683 M",
        "biography": "Sultan terbesar dalam historiografi Banten. Negarawan berwawasan global, pakar rekayasa hidrolika dan pertanian, serta musuh paling gigih kongsi dagang VOC. Menjadikan Banten bandar kosmopolitan termaju di Jawa.",
        "key_achievements": [
            "Membangun kanal irigasi sungai modern di Pontang dan Tanara untuk ketahanan pangan agraris",
            "Memiliki armada kapal perang dan kapal niaga modern yang berlayar hingga Filipina dan Timur Tengah",
            "Menerapkan kebijakan pasar bebas internasional di Pelabuhan Karangantu",
            "Mengangkat Syekh Yusuf al-Makassari sebagai mufti agung dan penasihat spiritual kesultanan",
            "Melancarkan perang gerilya laut dan darat menghancurkan pos-pos perdagangan VOC"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Ditetapkan sebagai Pahlawan Nasional Indonesia berdasarkan Keppres No. 045/TK/1970."
    },
    {
        "id": "banten-6",
        "kingdom_id": "banten",
        "order": 6,
        "name": "Sultan Haji (Sultan Abu Nashar Abdul Qahar)",
        "reign_start": 1682,
        "reign_end": 1687,
        "reign_display": "1682 – 1687 M",
        "biography": "Putra Sultan Ageng Tirtayasa yang pernah menunaikan haji ke Mekkah. Terbujuk intrik politik VOC sehingga berkomplot merebut takhta dari ayahnya sendiri, menandai awal mula runtuhnya kemandirian Banten.",
        "key_achievements": [
            "Membangun hubungan diplomatik dengan Utsmaniyah dan Inggris selama safar hajinya",
            "Menandatangani traktat 1684 dengan VOC yang menyerahkan hak monopoli lada dan pendirian Benteng Speelwijk"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Konflik ayah-anak ini dianalisis secara komprehensif oleh Claude Guillot dalam The Sultanate of Banten."
    },

    # ----------------------------------------------------
    # GOWA
    # ----------------------------------------------------
    {
        "id": "gowa-1",
        "kingdom_id": "gowa",
        "order": 1,
        "name": "Sultan Alauddin (I Manga'rangi Daeng Manrabbia)",
        "reign_start": 1593,
        "reign_end": 1639,
        "reign_display": "1593 – 1639 M (Islam sejak 1605 M)",
        "biography": "Raja Gowa ke-14 dan penguasa pertama yang resmi memeluk Islam pada malam Jumat, 22 September 1605 (9 Jumadil Awwal 1014 H). Bersama Mangkubumi Karaeng Matoaya dari Tallo, ia menjadikan Islam sebagai agama resmi kerajaan kembar Gowa-Tallo.",
        "key_achievements": [
            "Menetapkan Islam sebagai agama resmi Kerajaan Gowa-Tallo",
            "Mengirim juru dakwah ke kerajaan-kerajaan sekutu di Sulawesi Selatan (Soppeng, Wajo, Bone)",
            "Menolak klaim monopoli VOC dengan doktrin kebebasan laut: 'Tuhan telah menciptakan bumi dan laut untuk semua manusia'"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Wafat pada 15 Juni 1639, bergelar anumerta Tumenanga ri Gaukanna."
    },
    {
        "id": "gowa-2",
        "kingdom_id": "gowa",
        "order": 2,
        "name": "Sultan Malikussaid (I Manuntungi Daeng Mattola)",
        "reign_start": 1639,
        "reign_end": 1653,
        "reign_display": "1639 – 1653 M",
        "biography": "Putra Sultan Alauddin. Didampingi perdana menteri jenius Karaeng Pattingalloang yang menguasai berbagai bahasa Eropa, memiliki perpustakaan atlas bola dunia terbesar di Asia Tenggara, dan memproduksi meriam mesiu canggih.",
        "key_achievements": [
            "Memperluas pengaruh kemaritiman Makassar meliputi Flores, Sumbawa, Buton, dan Maluku",
            "Memperkuat industri pembuatan senjata api, bubuk mesiu, dan kapal perang di Somba Opu",
            "Menjadikan Makassar bandar perniagaan paling bebas dan multietnis di belahan timur benua Asia"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Tercatat dalam laporan para pastor Yesuit dan saudagar Inggris Alexander Hamilton."
    },
    {
        "id": "gowa-3",
        "kingdom_id": "gowa",
        "order": 3,
        "name": "Sultan Hasanuddin (I Mallombasi Daeng Mattawang)",
        "reign_start": 1653,
        "reign_end": 1669,
        "reign_display": "1653 – 1669 M",
        "biography": "Raja Gowa ke-16, bergelar 'Ayam Jantan dari Timur' (De Haantjes van het Oosten) karena keberaniannya luar biasa memimpin perlawanan semesta menghadapi koalisi armada gabungan VOC dan sekutunya dalam Perang Makassar.",
        "key_achievements": [
            "Memimpin benteng-benteng pertahanan pantai Somba Opu, Panakkukang, dan Ujung Pandang",
            "Menggerakkan ratusan perahu kora-kora dan prajurit berani mati Bugis-Makassar",
            "Bertahan dengan gigih hingga menandatangani Perjanjian Bungaya pada 18 November 1667",
            "Meneruskan pertempuran kembali pada 1669 hingga benteng Somba Opu luluh lantak oleh 20.000 pon mesiu VOC"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Ditetapkan sebagai Pahlawan Nasional Indonesia berdasarkan Keppres No. 087/TK/1973."
    },
    {
        "id": "gowa-4",
        "kingdom_id": "gowa",
        "order": 4,
        "name": "Sultan Amir Hamzah",
        "reign_start": 1669,
        "reign_end": 1674,
        "reign_display": "1669 – 1674 M",
        "biography": "Putra Sultan Hasanuddin yang naik takhta setelah ayahnya melepaskan mahkota pasca hancurnya Benteng Somba Opu. Berusaha merekonstruksi kembali kehidupan rakyat di tengah pengawasan ketat garnisun benteng Rotterdam.",
        "key_achievements": [
            "Memindahkan pusat aktivitas istana ke Balla Lompoa di Katangka",
            "Menjaga kerukunan masyarakat dan kelangsungan tradisi adat Bugis-Makassar"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Dimakamkan di kompleks pemakaman raja-raja Gowa di Katangka."
    },
    {
        "id": "gowa-5",
        "kingdom_id": "gowa",
        "order": 5,
        "name": "Sultan Muhammad Abdul Kadir Aididdin",
        "reign_start": 1826,
        "reign_end": 1893,
        "reign_display": "1826 – 1893 M",
        "biography": "Raja Gowa ke-32 yang memerintah paling lama (67 tahun). Membangun Istana megah Balla Lompoa di Sungguminasa pada 1936 oleh penerusnya dan mempertahankan marwah adat di bawah tekanan birokrasi Hindia Belanda.",
        "key_achievements": [
            "Mempertahankan tatanan adat hukum syarak dan lembaga dewan Hadat Bate Salapang",
            "Memelihara benda-benda pusaka keramat kebesaran Gowa (Kalompoang)"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Dicatat dalam silsilah resmi Keraton Gowa dan arsip Memorie van Overgave Gouverneur van Celebes."
    },
    {
        "id": "gowa-6",
        "kingdom_id": "gowa",
        "order": 6,
        "name": "Sultan Muhammad Tahir Muhibuddin (Karaeng Katangka)",
        "reign_start": 1936,
        "reign_end": 1946,
        "reign_display": "1936 – 1946 M",
        "biography": "Raja Gowa ke-36 dan penguasa administratif terakhir. Mendukung penuh kemerdekaan Republik Indonesia pada 1945 bersama tokoh pejuang Dr. Sam Ratulangi dan Andi Pangerang Pettarani.",
        "key_achievements": [
            "Menyatakan kesetiaan Kerajaan Gowa ke dalam wadah Negara Kesatuan Republik Indonesia",
            "Menjadikan Istana Balla Lompoa sebagai museum cagar budaya kebanggaan Sulawesi Selatan"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Keraton Gowa berlanjut sebagai lembaga pemangku adat dan kebudayaan."
    },

    # ----------------------------------------------------
    # TERNATE
    # ----------------------------------------------------
    {
        "id": "ternate-1",
        "kingdom_id": "ternate",
        "order": 1,
        "name": "Sultan Zainal Abidin",
        "reign_start": 1486,
        "reign_end": 1500,
        "reign_display": "1486 – 1500 M",
        "biography": "Raja Ternate ke-18 yang pertama kali secara resmi memakai gelar 'Sultan' dan meninggalkan gelar Kolano. Belajar langsung ilmu agama Islam ke Pesantren Giri di Jawa Timur (berguru kepada Sunan Giri) dan mendirikan madrasah pertama di Maluku.",
        "key_achievements": [
            "Mengganti sistem hukum tradisional dengan Syariat Islam sebagai hukum negara",
            "Mendirikan lembaga peradilan agama kesultanan dan menunjuk mufti (Qadhi)",
            "Menjalin aliansi keagamaan dan perniagaan erat dengan Kesultanan Demak dan Giri Kedaton"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Dikenal sebagai Kolano Marhum Jawa dalam historiografi Maluku."
    },
    {
        "id": "ternate-2",
        "kingdom_id": "ternate",
        "order": 2,
        "name": "Sultan Bayanullah (Abu Lais)",
        "reign_start": 1500,
        "reign_end": 1522,
        "reign_display": "1500 – 1522 M",
        "biography": "Putra Sultan Zainal Abidin. Menerima kedatangan ekspedisi armada kapal penjelajah bangsa Portugis di bawah pimpinan Francisco Serrao pada 1512 dan mengizinkan pendirian kantor dagang di Ternate.",
        "key_achievements": [
            "Membuka perdagangan rempah cengkeh langsung dengan bangsa-bangsa Eropa",
            "Memperkuat pertahanan kota Ternate menghadapi persaingan dengan Tidore"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Kematiannya pada 1522 mengawali fase campur tangan militer Portugis dalam suksesi kesultanan."
    },
    {
        "id": "ternate-3",
        "kingdom_id": "ternate",
        "order": 3,
        "name": "Sultan Khairun Jamil",
        "reign_start": 1535,
        "reign_end": 1570,
        "reign_display": "1535 – 1570 M",
        "biography": "Sultan yang gigih menentang monopoli perdagangan dan kristenisasi paksa yang dilakukan bangsa Portugis di Maluku. Dibunuh secara licik oleh tentara Portugis di dalam Benteng Sao Joao Baptista sesaat setelah bersumpah damai di atas Al-Qur'an dan Injil.",
        "key_achievements": [
            "Menyatukan rakyat Maluku dalam menolak tindakan sewenang-wenang kapten benteng Portugis",
            "Menjadi syahid pemicu gelombang perlawanan akbar semesta rakyat Maluku Kie Raha"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Tragedi pembunuhan Khairun pada 28 Februari 1570 memicu perang pembalasan lima tahun pimpinan putranya, Baabullah."
    },
    {
        "id": "ternate-4",
        "kingdom_id": "ternate",
        "order": 4,
        "name": "Sultan Baabullah (Datu Syah)",
        "reign_start": 1570,
        "reign_end": 1583,
        "reign_display": "1570 – 1583 M",
        "biography": "Penguasa teragung Kesultanan Ternate. Dikenal dengan julukan 'Penguasa 72 Pulau Berpenghuni'. Bersumpah menuntut balas kematian ayahnya, ia mengepung benteng Portugis selama 5 tahun tanpa kompromi hingga Portugis terusir selamanya dari Ternate pada 1575.",
        "key_achievements": [
            "Mengusir penjajah Portugis dari Ternate dan merebut benteng Gamlamo (1575)",
            "Memperluas kemaharajaan maritim Ternate meliputi 72 pulau berpenghuni dari Maluku, Sulawesi, Kepulauan Banggai, hingga Mindanao Selatan",
            "Menjalin diplomasi dengan Ratu Elizabeth I dari Inggris (kunjungan Francis Drake 1579)",
            "Menegakkan kemakmuran rempah cengkeh tertinggi di dunia tanpa dominasi kolonial"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Ditetapkan sebagai Pahlawan Nasional Indonesia berdasarkan Keppres No. 117/TK/2020."
    },
    {
        "id": "ternate-5",
        "kingdom_id": "ternate",
        "order": 5,
        "name": "Sultan Said Barakati (Sultan Saiduddin)",
        "reign_start": 1583,
        "reign_end": 1606,
        "reign_display": "1583 – 1606 M",
        "biography": "Putra Sultan Baabullah yang mempertahankan wilayah kemaharajaan Ternate dari invasi balasan armada Spanyol dari Manila. Ditawan secara licik oleh pasukan Gubernur Jenderal Spanyol Pedro Bravo de Acuna dan diasingkan ke Manila.",
        "key_achievements": [
            "Menjalin aliansi perdagangan awal dengan kongsi dagang Belanda (VOC) pada 1599",
            "Memimpin pertempuran maritim membendung ekspansi armada Spanyol di perairan Maluku Utara"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Wafat dalam pengasingan di Manila pada 1628."
    },
    {
        "id": "ternate-6",
        "kingdom_id": "ternate",
        "order": 6,
        "name": "Sultan Mudaffar Sjah",
        "reign_start": 1975,
        "reign_end": 2015,
        "reign_display": "1975 – 2015 M",
        "biography": "Sultan Ternate ke-48 di era modern. Tokoh pemersatu adat dan anggota Dewan Perwakilan Daerah (DPD) RI yang sangat berjasa merawat eksistensi adat Kie Sehe Ternate serta mendamaikan konflik horizontal Maluku Utara.",
        "key_achievements": [
            "Merevitalisasi upacara adat agung Legu Gam dan merawat Kedaton Ternate",
            "Berperan besar dalam pemulihan perdamaian rekonsiliasi Maluku pasca konflik 1999–2000",
            "Menjaga kelestarian pusaka Mahkota Berambut Emas Ternate"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Wafat pada 19 Februari 2015 dan dimakamkan dengan upacara kebesaran adat di Ternate."
    },

    # ----------------------------------------------------
    # TIDORE
    # ----------------------------------------------------
    {
        "id": "tidore-1",
        "kingdom_id": "tidore",
        "order": 1,
        "name": "Sultan Ciriliyati (Sultan Jamaluddin)",
        "reign_start": 1495,
        "reign_end": 1512,
        "reign_display": "c. 1495 – 1512 M",
        "biography": "Raja Tidore pertama yang memeluk Islam dan berganti gelar dari Kolano menjadi Sultan Jamaluddin setelah menerima dakwah Syekh Mansur dari Arab. Meletakkan dasar daulah Islam di Pulau Tidore.",
        "key_achievements": [
            "Menjadikan Islam sebagai syariat dan agama resmi Kesultanan Tidore",
            "Menjalin hubungan persahabatan maritim dengan Kesultanan Malaka",
            "Memperkokoh kepemimpinan konfederasi Uli Siwa di Maluku"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Dicatat dalam buku Sejarah Kepulauan Maluku dan naskah tradisi Kie Sehe."
    },
    {
        "id": "tidore-2",
        "kingdom_id": "tidore",
        "order": 2,
        "name": "Sultan Al-Mansur",
        "reign_start": 1512,
        "reign_end": 1526,
        "reign_display": "1512 – 1526 M",
        "biography": "Sultan yang menyambut kedatangan dua kapal sisa ekspedisi keliling dunia Ferdinand Magellan (Trinidad dan Victoria) di bawah Juan Sebastian Elcano pada November 1521. Membuka aliansi dagang cengkeh dengan Kerajaan Spanyol.",
        "key_achievements": [
            "Menjalin hubungan diplomatik dan perniagaan cengkeh resmi dengan Spanyol",
            "Memanfaatkan persaingan Spanyol-Portugis untuk mempertahankan kemerdekaan Tidore",
            "Mengisi kapal Victoria dengan muatan cengkeh kering yang berhasil dibawa selamat kembali ke Spanyol"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Catatan saksi mata ditulis oleh Antonio Pigafetta dalam Relazione del primo viaggio intorno al mondo."
    },
    {
        "id": "tidore-3",
        "kingdom_id": "tidore",
        "order": 3,
        "name": "Sultan Saifuddin (Kaicil Golofino)",
        "reign_start": 1657,
        "reign_end": 1687,
        "reign_display": "1657 – 1687 M",
        "biography": "Sultan yang piawai dalam diplomasi. Berhasil meredakan ketegangan dengan VOC tanpa mengorbankan martabat kedaulatan takhta Tidore dan mempertahankan wilayah pertuanan atas pesisir pulau Papua.",
        "key_achievements": [
            "Mempertegas klaim kedaulatan Tidore atas Kepulauan Raja Ampat dan daratan pesisir barat Papua",
            "Mengembangkan kota pelabuhan Soasio menjadi pusat kebudayaan Maluku Kie Raha"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Arsip korespondensinya dengan Gubernur VOC di Ambon tercatat dalam Corpus Diplomaticum Neerlando-Indicum."
    },
    {
        "id": "tidore-4",
        "kingdom_id": "tidore",
        "order": 4,
        "name": "Sultan Nuku (Jou Barakati / Sri Paduka Maha Tuan)",
        "reign_start": 1797,
        "reign_end": 1805,
        "reign_display": "1797 – 1805 M (Gerilya sejak 1780 M)",
        "biography": "Pahlawan bahari terbesar Maluku yang tak pernah terkalahkan di medan perang. Memimpin perjuangan gerilya laut selama 25 tahun menentang penjajahan VOC, menyatukan kekuatan suku-suku Papua, Raja Ampat, Seram Timur, dan armada Inggris, hingga berhasil merebut kembali takhta Tidore dan Ternate.",
        "key_achievements": [
            "Memimpin perang gerilya maritim akbar selama seperempat abad menentang hegemoni Belanda",
            "Menyatukan konfederasi para penguasa Papua, Raja Ampat, Halmahera, dan Seram Timur di bawah satu komando",
            "Merebut kembali benteng dan takhta Soasio Tidore dari penguasa boneka Belanda pada 1797",
            "Menaklukkan benteng Belanda di Ternate pada 1801 dan menyatukan seluruh Maluku",
            "Memulihkan kedaulatan penuh rakyat Maluku bebas dari kerja paksa hongitochten"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Ditetapkan sebagai Pahlawan Nasional Indonesia berdasarkan Keppres No. 071/TK/1995."
    },
    {
        "id": "tidore-5",
        "kingdom_id": "tidore",
        "order": 5,
        "name": "Sultan Zainal Abidin Sjah",
        "reign_start": 1947,
        "reign_end": 1967,
        "reign_display": "1947 – 1967 M",
        "biography": "Sultan Tidore ke-36 yang memegang peranan krusial dalam integrasi Irian Barat (Papua) ke pangkuan NKRI. Ditunjuk oleh Presiden Soekarno sebagai Gubernur pertama Provinsi Irian Barat pada 1956 yang berkedudukan di Soasio Tidore.",
        "key_achievements": [
            "Menyerahkan legitimasi historis pertuanan Tidore atas Papua kepada Republik Indonesia untuk membatalkan klaim Belanda",
            "Menjabat sebagai Gubernur Irian Barat pertama (1956–1961)",
            "Memperkokoh persatuan nasional dari Sabang sampai Merauke"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Ditetapkan sebagai Pahlawan Nasional Indonesia berdasarkan Keppres No. 117/TK/2020."
    },

    # ----------------------------------------------------
    # BIMA
    # ----------------------------------------------------
    {
        "id": "bima-1",
        "kingdom_id": "bima",
        "order": 1,
        "name": "Sultan Abdul Kahir I (La Ka'i)",
        "reign_start": 1621,
        "reign_end": 1640,
        "reign_display": "1621 – 1640 M",
        "biography": "Raja Bima ke-37 yang menjadi Sultan pertama setelah masuk Islam pada 7 Februari 1621 (15 Jumadil Awwal 1030 H). Mentransformasikan Kerajaan Mbojo menjadi kesultanan Islam berdaulat dan menyusun undang-undang syariat.",
        "key_achievements": [
            "Mendirikan Kesultanan Islam Bima dan meletakkan dasar hukum syariat Islam",
            "Menjalin persekutuan persaudaraan erat dengan Kesultanan Gowa dan Tallo",
            "Mendirikan masjid pertama di Bima dan membuka pusat pengajian Al-Qur'an"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Tercatat dalam naskah harian istana Bo' Sangaji Kai bab konversi Islam."
    },
    {
        "id": "bima-2",
        "kingdom_id": "bima",
        "order": 2,
        "name": "Sultan Abdul Khair Sirajuddin (Ma Ntau Dana Nyari)",
        "reign_start": 1640,
        "reign_end": 1682,
        "reign_display": "1640 – 1682 M",
        "biography": "Putra Sultan Abdul Kahir. Menikahi Daeng Sikontu, saudara perempuan Sultan Hasanuddin Gowa. Memimpin Bima dalam fase perluasan wilayah kedaulatan hingga ke Manggarai, Sumba, dan Solor.",
        "key_achievements": [
            "Memperluas pengaruh kesultanan meliputi Flores Barat (Manggarai) dan kepulauan sekitarnya",
            "Membantu armada Makassar dalam perang laut menentang kongsi monopoli VOC",
            "Menata sistem administrasi birokrasi istana Hadat Bima yang tertib dan berwibawa"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Wafat pada 1682 dan dimakamkan di Kompleks Tolobali."
    },
    {
        "id": "bima-3",
        "kingdom_id": "bima",
        "order": 3,
        "name": "Sultan Nuruddin Abubakar Ali Syah",
        "reign_start": 1682,
        "reign_end": 1687,
        "reign_display": "1682 – 1687 M",
        "biography": "Meneruskan kepemimpinan Bima dengan fokus pada penyusunan kitab-kitab peradilan agama Islam dan penguatan armada pelayaran niaga kuda dan kayu sepang.",
        "key_achievements": [
            "Menyusun regulasi perniagaan laut komoditas kayu sapan (sepang) dan kuda bima",
            "Menghidupkan majelis penulisan sejarah naskah Bo' Sangaji Kai"
        ],
        "is_golden_age_ruler": True,
        "reference_notes": "Naskah Bo' Sangaji Kai memuat catatan harian terperinci masa pemerintahannya."
    },
    {
        "id": "bima-4",
        "kingdom_id": "bima",
        "order": 4,
        "name": "Sultan Abdul Hamid Muhammad Syah",
        "reign_start": 1773,
        "reign_end": 1817,
        "reign_display": "1773 – 1817 M",
        "biography": "Memerintah saat meletusnya bencana letusan katastrofik Gunung Tambora pada April 1815 yang membumihanguskan tiga kerajaan tetangga (Tambora, Pekat, Sanggar) dan menutupi langit dunia dengan abu vulkanik.",
        "key_achievements": [
            "Memimpin penanganan bencana dan penyelamatan rakyat korban erupsi maha dahsyat Tambora 1815",
            "Memulihkan tata sosial dan persawahan Bima pasca hujan abu tebal bertahun-tahun"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Laporan bencana ini dicatat secara akurat oleh Sir Stamford Raffles dalam The History of Java."
    },
    {
        "id": "bima-5",
        "kingdom_id": "bima",
        "order": 5,
        "name": "Sultan Ibrahim",
        "reign_start": 1868,
        "reign_end": 1923,
        "reign_display": "1868 – 1923 M",
        "biography": "Memerintah selama 55 tahun. Melakukan modernisasi sistem pendidikan Islam dan mendirikan sekolah-sekolah rakyat pertama di Dana Mbojo.",
        "key_achievements": [
            "Mengirim pelajar-pelajar Bima menuntut ilmu ke Mekkah dan Batavia",
            "Menata sistem pencatatan tanah ulayat dan kesejahteraan petani garam dan padi"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Silsilah terdata dalam dokumen Registrasi Kesultanan Bima."
    },
    {
        "id": "bima-6",
        "kingdom_id": "bima",
        "order": 6,
        "name": "Sultan Muhammad Salahuddin (Ma Kakidi Agama)",
        "reign_start": 1923,
        "reign_end": 1958,
        "reign_display": "1923 – 1958 M",
        "biography": "Sultan terakhir Kesultanan Bima. Tokoh intelektual, arsitek, dan ulama yang membangun Istana megah Asi Mbojo (1927–1930). Mendukung penuh kemerdekaan RI dan menyerahkan wilayah swapraja menjadi Kabupaten Bima.",
        "key_achievements": [
            "Membangun Istana megah Asi Mbojo rancangan arsitek Rehatta",
            "Mendirikan Percetakan Al-Ittihad dan menerbitkan buku-buku agama beraksara Melayu",
            "Menyatakan integrasi swapraja Bima ke dalam Negara Kesatuan RI pada 1950",
            "Namanya diabadikan sebagai nama Bandara dan Universitas terkemuka di Bima"
        ],
        "is_golden_age_ruler": False,
        "reference_notes": "Wafat pada 1958 di Jakarta dan dimakamkan di pemakaman raja-raja Tolobali."
    }
]

# We will also add prominent sultans for the remaining kingdoms to ensure every kingdom has verified rulers
additional_sultans = [
    # Siak
    {
        "id": "siak-1", "kingdom_id": "siak-sri-indrapura", "order": 1,
        "name": "Raja Kecik (Sultan Abdul Jalil Rahmad Syah I)", "reign_start": 1723, "reign_end": 1746, "reign_display": "1723 – 1746 M",
        "biography": "Pendiri Kesultanan Siak Sri Indrapura di Buantan setelah konflik takhta Kesultanan Johor.",
        "key_achievements": ["Mendirikan kesultanan dan armada perang laut Siak", "Menguasai perairan timur Sumatera"], "is_golden_age_ruler": False, "reference_notes": "Tercatat dalam Syair Perang Siak."
    },
    {
        "id": "siak-2", "kingdom_id": "siak-sri-indrapura", "order": 2,
        "name": "Sultan Assyaidis Syarif Ali Abdul Jalil Saifuddin", "reign_start": 1784, "reign_end": 1810, "reign_display": "1784 – 1810 M",
        "biography": "Sultan berdarah Arab Ba'alawi pertama yang membawa Siak ke puncak keemasan politik dan maritim.",
        "key_achievements": ["Memperluas kedaulatan Siak dari Tamiang hingga Sambas", "Menyusun konstitusi Bab al-Qawa'id"], "is_golden_age_ruler": True, "reference_notes": "Makam Koto Tinggi Siak."
    },
    {
        "id": "siak-3", "kingdom_id": "siak-sri-indrapura", "order": 3,
        "name": "Sultan Syarif Hasyim Abdul Jalil Syarifuddin", "reign_start": 1889, "reign_end": 1908, "reign_display": "1889 – 1908 M",
        "biography": "Membangun Istana megah Asserayah Hasyimiah pada 1889 dan melawat ke berbagai negara Eropa.",
        "key_achievements": ["Membangun Istana Siak bercorak Moorish-Melayu", "Memperkenalkan pemutar piringan hitam langka 'Komet'"], "is_golden_age_ruler": False, "reference_notes": "Istana Siak kini cagar budaya nasional."
    },
    {
        "id": "siak-4", "kingdom_id": "siak-sri-indrapura", "order": 4,
        "name": "Sultan Syarif Kasim II", "reign_start": 1915, "reign_end": 1945, "reign_display": "1915 – 1945 M",
        "biography": "Sultan terakhir Siak dan Pahlawan Nasional Indonesia. Menyerahkan mahkota emas dan uang 13 juta gulden demi mendukung kemerdekaan RI.",
        "key_achievements": ["Menyerahkan kedaulatan dan kekayaan kerajaan kepada Presiden Sukarno", "Mendirikan sekolah modern Madrasah Taufiqiyah"], "is_golden_age_ruler": False, "reference_notes": "Pahlawan Nasional RI Keppres No. 109/TK/1998."
    },

    # Palembang
    {
        "id": "palembang-1", "kingdom_id": "palembang-darussalam", "order": 1,
        "name": "Sri Susuhunan Abdurrahman Khalifatul Mukminin Sayidul Iman", "reign_start": 1659, "reign_end": 1706, "reign_display": "1659 – 1706 M",
        "biography": "Pendiri Kesultanan Palembang Darussalam yang memerdekakan diri dari hegemoni Banten pasca hancurnya keraton Kuto Gawang.",
        "key_achievements": ["Mendeklarasikan kemerdekaan Palembang", "Menata tata kota keraton baru di tepi Musi"], "is_golden_age_ruler": False, "reference_notes": "Makam Candi Walang Palembang."
    },
    {
        "id": "palembang-2", "kingdom_id": "palembang-darussalam", "order": 2,
        "name": "Sultan Mahmud Badaruddin I Jayo Wikramo", "reign_start": 1724, "reign_end": 1757, "reign_display": "1724 – 1757 M",
        "biography": "Membangun Masjid Agung Palembang dan kompleks pemakaman Kawah Tengkurep. Mengamankan tambang timah Bangka.",
        "key_achievements": ["Membangun Masjid Agung Palembang (1738)", "Mengembangkan kemakmuran perniagaan timah"], "is_golden_age_ruler": False, "reference_notes": "Dimakamkan di Kawah Tengkurep."
    },
    {
        "id": "palembang-3", "kingdom_id": "palembang-darussalam", "order": 3,
        "name": "Sultan Muhammad Bahauddin", "reign_start": 1776, "reign_end": 1803, "reign_display": "1776 – 1803 M",
        "biography": "Membawa Palembang ke puncak kejayaan ekonomi dan pertahanan. Menyelesaikan pembangunan Benteng Kuto Besak.",
        "key_achievements": ["Membangun kompleks pertahanan batu bata Benteng Kuto Besak", "Mendukung penulisan karya sastra keagamaan"], "is_golden_age_ruler": True, "reference_notes": "Benteng Kuto Besak kini cagar budaya nasional."
    },
    {
        "id": "palembang-4", "kingdom_id": "palembang-darussalam", "order": 4,
        "name": "Sultan Mahmud Badaruddin II (Raden Hasan)", "reign_start": 1803, "reign_end": 1821, "reign_display": "1803 – 1821 M",
        "biography": "Pahlawan Nasional Indonesia. Memimpin rakyat Palembang dalam Perang Palembang (1819–1821) memukul mundur armada Belanda sebelum akhirnya diasingkan ke Ternate.",
        "key_achievements": ["Menghancurkan ekspedisi armada Belanda di Sungai Musi pada 1819", "Menolak traktat penyerahan kedaulatan kepada Inggris dan Belanda"], "is_golden_age_ruler": True, "reference_notes": "Pahlawan Nasional RI Keppres No. 063/TK/1984."
    },

    # Banjar
    {
        "id": "banjar-1", "kingdom_id": "banjar", "order": 1,
        "name": "Sultan Suriansyah (Raden Samudera)", "reign_start": 1526, "reign_end": 1550, "reign_display": "1526 – 1550 M",
        "biography": "Pendiri dan raja Islam pertama Kesultanan Banjar setelah dibimbing Khatib Dayan utusan Kesultanan Demak.",
        "key_achievements": ["Mendirikan Kesultanan Banjar di muara Kuin", "Membangun Masjid Sultan Suriansyah pada 1526"], "is_golden_age_ruler": False, "reference_notes": "Hikayat Banjar."
    },
    {
        "id": "banjar-2", "kingdom_id": "banjar", "order": 2,
        "name": "Sultan Musta'inbillah (Marhum Panembahan)", "reign_start": 1595, "reign_end": 1642, "reign_display": "1595 – 1642 M",
        "biography": "Membawa Banjar ke puncak kemakmuran ekspor lada dan memindahkan ibu kota ke Martapura setelah Kuin diserang VOC.",
        "key_achievements": ["Mengekspor puluhan ribu pikul lada hitam berkualitas", "Memperluas pengaruh kesultanan ke Kotawaringin dan Sambas"], "is_golden_age_ruler": True, "reference_notes": "Makam di Martapura."
    },
    {
        "id": "banjar-3", "kingdom_id": "banjar", "order": 3,
        "name": "Sultan Tahmidullah II (Sunan Nata Alam)", "reign_start": 1761, "reign_end": 1801, "reign_display": "1761 – 1801 M",
        "biography": "Mendukung penuh kiprah dakwah Syekh Muhammad Arsyad al-Banjari menyusun kitab fikih akbar Sabilal Muhtadin.",
        "key_achievements": ["Membina pusat pendidikan keilmuan Islam tertua di Kalimantan", "Membangun institusi Mahkamah Syar'iyah Banjar"], "is_golden_age_ruler": False, "reference_notes": "Sejarah Banjar Idwar Saleh."
    },
    {
        "id": "banjar-4", "kingdom_id": "banjar", "order": 4,
        "name": "Pangeran Antasari (Panembahan Amiruddin Khalifatul Mukminin)", "reign_start": 1859, "reign_end": 1862, "reign_display": "1859 – 1862 M",
        "biography": "Pahlawan Nasional Indonesia. Pemimpin spiritual dan panglima tertinggi Perang Banjar menentang penjajahan Belanda dengan semboyan: 'Haram Manyarah Waja Sampai Kaputing'.",
        "key_achievements": ["Mengobarkan Perang Banjar menyerang benteng dan tambang tambang batu bara Belanda", "Menyatukan suku Dayak dan Banjar dalam perang suci mempertahankan kedaulatan"], "is_golden_age_ruler": False, "reference_notes": "Pahlawan Nasional RI Keppres No. 06/TK/1968."
    },

    # Buton
    {
        "id": "buton-1", "kingdom_id": "buton", "order": 1,
        "name": "Sultan Murhum Kaimuddin Khalifatul Khamis (Lakilaponto)", "reign_start": 1538, "reign_end": 1584, "reign_display": "1538 – 1584 M",
        "biography": "Raja Buton ke-6 yang memeluk Islam dan menjadi Sultan Buton pertama setelah dibimbing Syekh Abdul Wahid.",
        "key_achievements": ["Mentransformasikan Buton menjadi kesultanan Islam", "Menata tata kelola kepulauan Buton dan Muna"], "is_golden_age_ruler": False, "reference_notes": "Makam di Keraton Wolio Baubau."
    },
    {
        "id": "buton-2", "kingdom_id": "buton", "order": 2,
        "name": "Sultan Dayanu Ikhsanuddin (La Elangi)", "reign_start": 1584, "reign_end": 1617, "reign_display": "1584 – 1617 M",
        "biography": "Sultan ke-4 yang menggubah konstitusi ketatanegaraan Islam termasyhur 'Undang-Undang Martabat Tujuh'.",
        "key_achievements": ["Mengundangkan konstitusi Martabat Tujuh", "Merancang perluasan kompleks benteng batu karang Wolio"], "is_golden_age_ruler": True, "reference_notes": "Naskah Kuno Martabat Tujuh."
    },
    {
        "id": "buton-3", "kingdom_id": "buton", "order": 3,
        "name": "Sultan La Buke (Sultan Syafiuddin)", "reign_start": 1632, "reign_end": 1645, "reign_display": "1632 – 1645 M",
        "biography": "Memperkokoh kedaulatan maritim dan menyelesaikan kubu-kubu pertahanan (bastion) Benteng Wolio.",
        "key_achievements": ["Memperkuat 16 bastion dan meriam pertahanan benteng", "Menjaga otonomi Buton di tengah rivalitas Ternate dan Makassar"], "is_golden_age_ruler": True, "reference_notes": "Benteng Wolio Baubau."
    },
    {
        "id": "buton-4", "kingdom_id": "buton", "order": 4,
        "name": "Sultan Muhammad Falihi", "reign_start": 1937, "reign_end": 1960, "reign_display": "1937 – 1960 M",
        "biography": "Sultan Buton ke-38 dan penguasa monarki terakhir sebelum wilayahnya diintegrasikan ke dalam Republik Indonesia.",
        "key_achievements": ["Menjaga stabilitas masyarakat Buton pada era transisi kemerdekaan", "Menyerahkan mandat kedaulatan administratif kepada NKRI"], "is_golden_age_ruler": False, "reference_notes": "Wafat pada 1960."
    },

    # Kutai Kartanegara
    {
        "id": "kutai-1", "kingdom_id": "kutai-kartanegara", "order": 1,
        "name": "Aji Pangeran Sinum Panji Mendapa", "reign_start": 1605, "reign_end": 1635, "reign_display": "1605 – 1635 M",
        "biography": "Raja yang menyatukan Kutai Kartanegara dan Kutai Martapura serta menerima syiar Islam dari Tuan Tunggang Parangan.",
        "key_achievements": ["Menyatukan dua entitas Kutai di lembah Mahakam", "Menerapkan hukum Islam dalam Kitab Brajaniti"], "is_golden_age_ruler": False, "reference_notes": "Salasilah Kutai."
    },
    {
        "id": "kutai-2", "kingdom_id": "kutai-kartanegara", "order": 2,
        "name": "Sultan Aji Muhammad Muslihuddin (Aji Imbut)", "reign_start": 1780, "reign_end": 1816, "reign_display": "1780 – 1816 M",
        "biography": "Memindahkan ibu kota kesultanan dari Pemarangan ke Tepian Pandan (kini Tenggarong) pada 28 September 1782.",
        "key_achievements": ["Mendirikan ibu kota bersejarah Tenggarong", "Mempertahankan kedaulatan dari serbuan bajak laut"], "is_golden_age_ruler": False, "reference_notes": "Hari Jadi Kota Tenggarong."
    },
    {
        "id": "kutai-3", "kingdom_id": "kutai-kartanegara", "order": 3,
        "name": "Sultan Aji Muhammad Sulaiman", "reign_start": 1845, "reign_end": 1899, "reign_display": "1845 – 1899 M",
        "biography": "Membawa Kutai ke puncak kemakmuran ekonomi modern berkat konsesi tambang minyak Sanga-Sanga dan batu bara.",
        "key_achievements": ["Mengelola kekayaan royalti minyak dan batu bara pertama di Kaltim", "Membangun Tenggarong dengan fasilitas listrik dan seni keraton"], "is_golden_age_ruler": True, "reference_notes": "Museum Mulawarman Tenggarong."
    },
    {
        "id": "kutai-4", "kingdom_id": "kutai-kartanegara", "order": 4,
        "name": "Sultan Aji Muhammad Parikesit", "reign_start": 1920, "reign_end": 1960, "reign_display": "1920 – 1960 M",
        "biography": "Sultan terakhir Kutai yang membangun kedaton megah beton bertulang pada 1936 dan menyerahkan administrasi ke NKRI pada 1960.",
        "key_achievements": ["Membangun Kedaton Kutai modern bergaya art-deco", "Menyerahkan kekuasaan Daerah Istimewa Kutai kepada Pemprov Kaltim"], "is_golden_age_ruler": False, "reference_notes": "Kedaton kini Museum Mulawarman."
    },

    # Pontianak
    {
        "id": "pontianak-1", "kingdom_id": "pontianak", "order": 1,
        "name": "Sultan Syarif Abdurrahman Alkadrie", "reign_start": 1771, "reign_end": 1808, "reign_display": "1771 – 1808 M",
        "biography": "Pendiri Kesultanan Pontianak di simpang tiga Sungai Kapuas dan Landak pada 23 Oktober 1771.",
        "key_achievements": ["Membuka kota Pontianak dan membangun Istana Kadriah serta Masjid Jami'", "Menjadikan Pontianak emporium perdagangan bebas terkemuka"], "is_golden_age_ruler": True, "reference_notes": "Hari Jadi Kota Pontianak 23 Oktober."
    },
    {
        "id": "pontianak-2", "kingdom_id": "pontianak", "order": 2,
        "name": "Sultan Syarif Kasim Alkadrie", "reign_start": 1808, "reign_end": 1819, "reign_display": "1808 – 1819 M",
        "biography": "Putra Sultan Syarif Abdurrahman yang memperkuat hubungan persaudaraan dengan kesultanan-kesultanan pesisir Malaya dan Riau.",
        "key_achievements": ["Memperluas perdagangan komoditas hasil hutan dan kopra"], "is_golden_age_ruler": False, "reference_notes": "Makam Kesultanan Batulayang."
    },
    {
        "id": "pontianak-3", "kingdom_id": "pontianak", "order": 3,
        "name": "Sultan Hamid II (Syarif Abdul Hamid Alkadrie)", "reign_start": 1945, "reign_end": 1950, "reign_display": "1945 – 1950 M",
        "biography": "Sultan Pontianak ke-8, lulusan Akademi Militer Breda Belanda. Tokoh perancang Lambang Negara Indonesia 'Garuda Pancasila'.",
        "key_achievements": ["Merancang lambang negara Republik Indonesia Garuda Pancasila", "Menjabat Presiden Negara Kalimantan Barat dan Ketua BFO"], "is_golden_age_ruler": False, "reference_notes": "Rancangan asli tersimpan di Istana Kadriah."
    },

    # Sambas
    {
        "id": "sambas-1", "kingdom_id": "sambas", "order": 1,
        "name": "Raden Sulaiman (Sultan Muhammad Shafiuddin I)", "reign_start": 1671, "reign_end": 1682, "reign_display": "1671 – 1682 M",
        "biography": "Bangsawan Kesultanan Brunei yang mendirikan Kesultanan Sambas di pertemuan Sungai Subah dan Sambas.",
        "key_achievements": ["Mendirikan Kesultanan Islam Sambas", "Menyatukan suku Melayu dan Dayak pesisir"], "is_golden_age_ruler": False, "reference_notes": "Silsilah Raja Sambas."
    },
    {
        "id": "sambas-2", "kingdom_id": "sambas", "order": 2,
        "name": "Sultan Umar Aqamaddin I", "reign_start": 1708, "reign_end": 1732, "reign_display": "1708 – 1732 M",
        "biography": "Membawa Sambas ke zaman keemasan kekuatan armada maritim yang disegani di Laut Natuna dan Selat Karimata.",
        "key_achievements": ["Mengamankan jalur pelayaran pantai barat Kalimantan", "Mengembangkan perniagaan intan dan tenun"], "is_golden_age_ruler": True, "reference_notes": "Makam Kesultanan Sambas."
    },
    {
        "id": "sambas-3", "kingdom_id": "sambas", "order": 3,
        "name": "Sultan Muhammad Radjiuddin", "reign_start": 1854, "reign_end": 1866, "reign_display": "1854 – 1866 M",
        "biography": "Membangun kembali kemegahan Istana Alwatzikhoebillah Sambas.",
        "key_achievements": ["Menyelesaikan arsitektur istana keraton kayu belian Alwatzikhoebillah", "Mendukung penulisan naskah keagamaan Melayu"], "is_golden_age_ruler": False, "reference_notes": "Istana Alwatzikhoebillah."
    },

    # Bone
    {
        "id": "bone-1", "kingdom_id": "bone", "order": 1,
        "name": "La Tenriruwa (Sultan Adam)", "reign_start": 1611, "reign_end": 1611, "reign_display": "1611 M",
        "biography": "Raja Bone ke-11 yang pertama kali memeluk Islam pasca perang persaudaraan dengan Gowa.",
        "key_achievements": ["Membuka jalan penerimaan Islam di Kerajaan Bone"], "is_golden_age_ruler": False, "reference_notes": "Lontara Bone."
    },
    {
        "id": "bone-2", "kingdom_id": "bone", "order": 2,
        "name": "Arung Palakka (La Tenritatta Petta Malampe'e Gemme'na)", "reign_start": 1672, "reign_end": 1696, "reign_display": "1672 – 1696 M",
        "biography": "Raja Bone ke-15 yang membebaskan rakyat Bone dari dominasi Gowa dan memimpin konfederasi Bugis ke puncak supremasi politik.",
        "key_achievements": ["Menjadikan Bone kekuatan dominan terbesar di Sulawesi Selatan", "Menegakkan pranata hukum adat Ade' Pitu"], "is_golden_age_ruler": True, "reference_notes": "Leonard Y. Andaya (1981)."
    },
    {
        "id": "bone-3", "kingdom_id": "bone", "order": 3,
        "name": "La Pawawoi Karaeng Segeri", "reign_start": 1895, "reign_end": 1905, "reign_display": "1895 – 1905 M",
        "biography": "Pahlawan Nasional Indonesia. Raja Bone ke-31 yang memimpin perlawanan gigih menghadapi Ekspedisi Militer Belanda 1905.",
        "key_achievements": ["Memimpin perang mempertahankan benteng Bone hingga gugur putranya Petta Ponggawae", "Menolak menyerahkan pusaka kerajaan kepada Belanda"], "is_golden_age_ruler": False, "reference_notes": "Pahlawan Nasional RI Keppres No. 082/TK/2005."
    },

    # Cirebon
    {
        "id": "cirebon-1", "kingdom_id": "cirebon", "order": 1,
        "name": "Sunan Gunung Jati (Syarif Hidayatullah)", "reign_start": 1479, "reign_end": 1568, "reign_display": "1479 – 1568 M",
        "biography": "Anggota Walisongo termasyhur dan pendiri dinasti kesultanan Cirebon dan Banten. Mengembangkan Cirebon menjadi pusat dakwah Islam, diplomasi, dan seni budaya di Tatar Sunda.",
        "key_achievements": ["Memerdekakan Cirebon dari upeti Kerajaan Galuh Pajajaran", "Membangun Masjid Agung Sang Cipta Rasa bersama Sunan Kalijaga", "Menjalin pernikahan diplomatik dengan putri Ong Tien Nio dari Tiongkok"], "is_golden_age_ruler": True, "reference_notes": "Makam di Astana Gunung Sembung Cirebon."
    },
    {
        "id": "cirebon-2", "kingdom_id": "cirebon", "order": 2,
        "name": "Panembahan Ratu I (Pangeran Emas)", "reign_start": 1568, "reign_end": 1649, "reign_display": "1568 – 1649 M",
        "biography": "Cicit Sunan Gunung Jati yang memelihara kestabilan dan kedamaian Cirebon di tengah pergeseran kekuatan Demak, Pajang, dan Mataram.",
        "key_achievements": ["Membangun Keraton Pakungwati (kini Kasepuhan)", "Merancang Kereta Kencana Singa Barong"], "is_golden_age_ruler": True, "reference_notes": "Keraton Kasepuhan Cirebon."
    },
    {
        "id": "cirebon-3", "kingdom_id": "cirebon", "order": 3,
        "name": "Sultan Sepuh I (Pangeran Raja Syamsuddin)", "reign_start": 1677, "reign_end": 1697, "reign_display": "1677 – 1697 M",
        "biography": "Sultan pertama Kasultanan Kasepuhan setelah takhta Cirebon terbagi menjadi Kasepuhan dan Kanoman.",
        "key_achievements": ["Meletakkan tradisi pelestarian pusaka Panjang Jimat", "Merawat arsitektur keraton Kasepuhan"], "is_golden_age_ruler": False, "reference_notes": "Babad Cirebon."
    },

    # Giri Kedaton
    {
        "id": "giri-1", "kingdom_id": "giri-kedaton", "order": 1,
        "name": "Sunan Giri I (Raden Paku / Prabu Satmata)", "reign_start": 1487, "reign_end": 1506, "reign_display": "1487 – 1506 M",
        "biography": "Anggota Walisongo pendiri Giri Kedaton. Menciptakan lagu anak-anak dolanan bermakna tauhid (Jitungan, Jamuran) dan merintis kedatuan santri di atas bukit Giri.",
        "key_achievements": ["Mendirikan Giri Kedaton sebagai pusat keagamaan independen", "Mengirim ekspedisi dakwah ke kepulauan Maluku dan Nusa Tenggara"], "is_golden_age_ruler": True, "reference_notes": "Makam Sunan Giri di Kebomas Gresik."
    },
    {
        "id": "giri-2", "kingdom_id": "giri-kedaton", "order": 2,
        "name": "Sunan Prapen (R.M. Pratikal)", "reign_start": 1548, "reign_end": 1605, "reign_display": "1548 – 1605 M",
        "biography": "Penguasa Giri ke-4 yang memiliki pengaruh spiritual tertinggi di Jawa. Melantik Sultan Hadiwijaya Pajang dan mengislamkan raja-raja di Lombok dan Maluku.",
        "key_achievements": ["Melantik raja-raja Islam di Jawa sebagai pengesah takhta spiritual", "Memperluas pengaruh dakwah Giri hingga Selaparang Lombok dan Hitu Ambon"], "is_golden_age_ruler": True, "reference_notes": "De Graaf & Pigeaud (2001)."
    },

    # Yogyakarta
    {
        "id": "yogyakarta-1", "kingdom_id": "kasultanan-yogyakarta", "order": 1,
        "name": "Sri Sultan Hamengkubuwana I (Pangeran Mangkubumi)", "reign_start": 1755, "reign_end": 1792, "reign_display": "1755 – 1792 M",
        "biography": "Pendiri Kasultanan Ngayogyakarta Hadiningrat, ahli strategi perang dan arsitek ulung perancang Keraton Yogyakarta dan Taman Sari.",
        "key_achievements": ["Merancang tata ruang poros filosofis Yogyakarta", "Membangun Keraton Yogyakarta dan pesanggrahan Taman Sari", "Menang dalam Perang Takhta Jawa III melawan VOC"], "is_golden_age_ruler": True, "reference_notes": "Pahlawan Nasional RI Keppres No. 107/TK/2006."
    },
    {
        "id": "yogyakarta-2", "kingdom_id": "kasultanan-yogyakarta", "order": 2,
        "name": "Sri Sultan Hamengkubuwana IX", "reign_start": 1940, "reign_end": 1988, "reign_display": "1940 – 1988 M",
        "biography": "Bapak Pramuka Indonesia dan Pahlawan Nasional. Mengeluarkan Amanat 5 September 1945 menggabungkan Yogyakarta ke NKRI dan menyediakan keraton sebagai pusat pemerintahan RI.",
        "key_achievements": ["Menjadikan Yogyakarta Ibu Kota Republik Indonesia (1946–1949)", "Mendanai operasional pemerintahan darurat Republik Indonesia", "Menjabat Wakil Presiden Republik Indonesia ke-2"], "is_golden_age_ruler": False, "reference_notes": "Pahlawan Nasional RI Keppres No. 053/TK/1990."
    },
    {
        "id": "yogyakarta-3", "kingdom_id": "kasultanan-yogyakarta", "order": 3,
        "name": "Sri Sultan Hamengkubuwana X", "reign_start": 1989, "reign_end": None, "reign_display": "1989 – Sekarang",
        "biography": "Sultan Yogyakarta ke-10 sekaligus Gubernur Daerah Istimewa Yogyakarta. Memperjuangkan pengesahan UU Keistimewaan DIY dan penetapan Warisan Dunia UNESCO.",
        "key_achievements": ["Mengawal pengesahan UU No. 13 Tahun 2012 tentang Keistimewaan DIY", "Berhasil mendaftarkan Sumbu Filosofis Yogyakarta sebagai Warisan Dunia UNESCO (2023)"], "is_golden_age_ruler": False, "reference_notes": "Bertahta aktif saat ini."
    },

    # Surakarta
    {
        "id": "surakarta-1", "kingdom_id": "kasunanan-surakarta", "order": 1,
        "name": "Sri Susuhunan Pakubuwana IV (Sinuhun Bagus)", "reign_start": 1788, "reign_end": 1820, "reign_display": "1788 – 1820 M",
        "biography": "Pujangga agung raja Surakarta penggubah Serat Wulangreh, karya sastra piwulang moral dan kepemimpinan adiluhung.",
        "key_achievements": ["Menggubah Serat Wulangreh", "Menjadikan Surakarta kiblat sastra dan budaya Jawa Baru"], "is_golden_age_ruler": True, "reference_notes": "Serat Wulangreh."
    },
    {
        "id": "surakarta-2", "kingdom_id": "kasunanan-surakarta", "order": 2,
        "name": "Sri Susuhunan Pakubuwana X", "reign_start": 1893, "reign_end": 1939, "reign_display": "1893 – 1939 M",
        "biography": "Raja Surakarta terkaya dan dermawan yang memodernisasi kota Sala serta mendukung pergerakan kebangsaan Budi Utomo dan Sarekat Islam.",
        "key_achievements": ["Membangun Stadion Sriwedari, RS Panti Kosala, dan Pasar Gede", "Mendukung finansial pergerakan nasional kemerdekaan Indonesia"], "is_golden_age_ruler": False, "reference_notes": "Pahlawan Nasional RI Keppres No. 113/TK/2011."
    },

    # Rumbati & Misool (Papua)
    {
        "id": "rumbati-1", "kingdom_id": "rumbati-papua", "order": 1,
        "name": "Raja Ismail Bauw", "reign_start": 1850, "reign_end": 1895, "reign_display": "c. 1850 – 1895 M",
        "biography": "Raja Petuanan Rumbati di Semenanjung Onin Fakfak yang merawat kerukunan antarumat beragama dan memajukan perdagangan pala negeri Onin.",
        "key_achievements": ["Memimpin perniagaan pala kuskus dengan pedagang Maluku dan Bugis", "Merawat tradisi toleransi filosofis 'Satu Tungku Tiga Batu'"], "is_golden_age_ruler": True, "reference_notes": "Syahruddin Mansyur (2016)."
    },
    {
        "id": "misool-1", "kingdom_id": "misool-papua", "order": 1,
        "name": "Fun Abdul Majid (Raja Misool)", "reign_start": 1870, "reign_end": 1904, "reign_display": "c. 1870 – 1904 M",
        "biography": "Penguasa bergelar Fun dari klan Umkabu yang berkedudukan di Lilinta Pulau Misool Raja Ampat.",
        "key_achievements": ["Menjaga keamanan teritorial bahari perairan Misool dan Raja Ampat", "Mempererat hubungan diplomatik dengan Kesultanan Tidore"], "is_golden_age_ruler": True, "reference_notes": "Balai Arkeologi Papua."
    },

    # Sumbawa
    {
        "id": "sumbawa-1", "kingdom_id": "sumbawa", "order": 1,
        "name": "Sultan Harunnurrasyid I (Dewa Maja Paruwa)", "reign_start": 1674, "reign_end": 1702, "reign_display": "1674 – 1702 M",
        "biography": "Sultan pertama Kesultanan Sumbawa yang melembagakan syariat Islam pasca kemerdekaan dari persekutuan Makassar.",
        "key_achievements": ["Mendirikan Kesultanan Sumbawa mandiri", "Menata hukum adat bersendi syarak"], "is_golden_age_ruler": False, "reference_notes": "Lontar Sumbawa."
    },
    {
        "id": "sumbawa-2", "kingdom_id": "sumbawa", "order": 2,
        "name": "Sultan Muhammad Jalaluddin Syah III", "reign_start": 1883, "reign_end": 1931, "reign_display": "1883 – 1931 M",
        "biography": "Membangun Istana megah Dalam Loka di Sumbawa Besar pada 1885 dengan struktur kayu panggung 99 tiang tanpa paku besi.",
        "key_achievements": ["Membangun Istana bersejarah Dalam Loka", "Memajukan kemakmuran pertanian dan peternakan rakyat"], "is_golden_age_ruler": True, "reference_notes": "Istana Dalam Loka cagar budaya nasional."
    },

    # Selaparang Lombok
    {
        "id": "selaparang-1", "kingdom_id": "selaparang", "order": 1,
        "name": "Prabu Rangkesari", "reign_start": 1580, "reign_end": 1620, "reign_display": "c. 1580 – 1620 M",
        "biography": "Raja Islam Selaparang yang membawa Pulau Lombok menjadi pusat keilmuan Islam dan lumbung padi Selat Alas.",
        "key_achievements": ["Memperkokoh daulah Islam di Pulau Lombok", "Menjalin kerja sama pertahanan bahari dengan Kesultanan Gowa"], "is_golden_age_ruler": True, "reference_notes": "Babad Lombok."
    }
]

all_sultans = sultans_data + additional_sultans

# Save to data/sultans.json
with open(r"c:\Users\TengQ\antigravity\webgis-islamic-history\data\sultans.json", "w", encoding="utf-8") as f:
    json.dump(all_sultans, f, ensure_ascii=False, indent=2)

print(f"Successfully generated data/sultans.json with {len(all_sultans)} sultans.")
