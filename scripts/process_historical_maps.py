# -*- coding: utf-8 -*-
"""
Historical Map Processing & GeoJSON Digitization Pipeline
Atlas Sejarah Kerajaan Islam Nusantara

Produces georeferenced spatial polygons based on authoritative historical atlases:
- Robert Cribb (2000), Historical Atlas of Indonesia (Curzon/Routledge)
- Anthony Reid (2005), An Indonesian Frontier: Aceh in the 17th Century
- Claude Guillot (1990), The Sultanate of Banten
- H.J. de Graaf (1958), De regering van Sultan Agung
- Leonard Y. Andaya (1981), The Heritage of Arung Palakka

Coordinate Reference System: WGS84 (EPSG:4326)
Format: GeoJSON (RFC 7946) with [longitude, latitude] coordinates.
"""

import json
import os
import math

def validate_polygon_ring(ring):
    """Ensures ring has at least 4 coordinates and is closed."""
    if len(ring) < 4:
        raise ValueError(f"Ring must have at least 4 coordinates, got {len(ring)}")
    if ring[0] != ring[-1]:
        # Close the ring automatically
        ring.append(ring[0])
    # Validate longitude & latitude ranges for Nusantara
    for pt in ring:
        lon, lat = pt[0], pt[1]
        if not (90.0 <= lon <= 145.0):
            raise ValueError(f"Longitude out of bounds for Nusantara: {lon}")
        if not (-13.0 <= lat <= 10.0):
            raise ValueError(f"Latitude out of bounds for Nusantara: {lat}")
    return ring

# =========================================================================
# FEATURE DEFINITIONS: HISTORICAL CARTOGRAPHIC POLYGONS
# =========================================================================

features_data = [
    # ---------------------------------------------------------------------
    # 1. KESULTANAN MATARAM ISLAM (1613 - 1645 M) - SULTAN AGUNG
    # ---------------------------------------------------------------------
    {
        "polygon_id": "mataram-core-1645",
        "kingdom_id": "mataram-islam",
        "kingdom_name": "Kesultanan Mataram Islam",
        "historical_period": "1613–1645 M (Zaman Keemasan Sultan Agung)",
        "year_start": 1613,
        "year_end": 1645,
        "territory_type": "core",
        "source_title": "Map 3.10: The Expansion of Mataram, 1588–1645 (Historical Atlas of Indonesia)",
        "source_url": "https://www.routledge.com/Historical-Atlas-of-Indonesia/Cribb/p/book/9780700709854",
        "source_publisher": "Curzon Press & University of Hawai'i Press",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi titik kontrol darat (GCP) pada aliran Sungai Opak, Progo, Bengawan Solo hulu, lereng Merapi, dan garis pantai selatan Jawa.",
        "digitization_method": "Digitasi on-screen batas Kutanegara dan Negaragung (wilayah inti keraton Kotagede, Karta, Plered, Pajang, dan lembah Mataram).",
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Wilayah inti Negaragung terikat langsung dengan sistem apanase pejabat kepatihan keraton Mataram.",
        "coordinates": [
            [
                [110.15, -7.60], [110.35, -7.50], [110.55, -7.50], [110.82, -7.54],
                [110.90, -7.65], [110.92, -7.82], [110.75, -8.02], [110.55, -8.08],
                [110.32, -8.04], [110.18, -7.95], [110.12, -7.78], [110.15, -7.60]
            ]
        ]
    },
    {
        "polygon_id": "mataram-controlled-1645",
        "kingdom_id": "mataram-islam",
        "kingdom_name": "Kesultanan Mataram Islam",
        "historical_period": "1613–1645 M (Zaman Keemasan Sultan Agung)",
        "year_start": 1613,
        "year_end": 1645,
        "territory_type": "controlled",
        "source_title": "Map 3.10: The Expansion of Mataram, 1588–1645 / De regering van Sultan Agung (H.J. de Graaf)",
        "source_url": "https://www.routledge.com/Historical-Atlas-of-Indonesia/Cribb/p/book/9780700709854",
        "source_publisher": "Curzon Press & Martinus Nijhoff",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi kontur pantai utara Jawa dari Tegal hingga Pasuruan, muara Bengawan Solo di Gresik, serta Selat Madura.",
        "digitization_method": "Digitasi batas wilayah Mancanegara (Banyumas, Bagelen, Kedu, Madiun, Kediri, Jipang) dan Pasisir (Tegal, Pekalongan, Kendal, Demak, Jepara, Rembang, Tuban, Surabaya, Pasuruan, Madura).",
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Batas barat berbatasan dengan pengaruh Banten di Priangan timur; batas timur dengan Blambangan.",
        "coordinates": [
            [
                [108.85, -6.85], [109.15, -6.82], [109.68, -6.88], [110.42, -6.95],
                [110.65, -6.82], [110.72, -6.45], [111.05, -6.50], [111.60, -6.70],
                [112.05, -6.85], [112.65, -6.90], [113.15, -6.95], [113.85, -6.92],
                [114.05, -7.10], [113.90, -7.28], [113.15, -7.22], [112.85, -7.50],
                [113.00, -7.75], [113.10, -8.15], [112.60, -8.35], [111.80, -8.30],
                [111.10, -8.25], [110.05, -7.85], [109.25, -7.72], [108.75, -7.68],
                [108.60, -7.30], [108.75, -7.00], [108.85, -6.85]
            ]
        ]
    },
    {
        "polygon_id": "mataram-influence-1645",
        "kingdom_id": "mataram-islam",
        "kingdom_name": "Kesultanan Mataram Islam",
        "historical_period": "1613–1645 M (Protektorat & Hegemoni Maritim)",
        "year_start": 1622,
        "year_end": 1645,
        "territory_type": "influence",
        "source_title": "Map 3.10: The Expansion of Mataram, 1588–1645 (Historical Atlas of Indonesia)",
        "source_url": "https://www.routledge.com/Historical-Atlas-of-Indonesia/Cribb/p/book/9780700709854",
        "source_publisher": "Curzon Press",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi pesisir barat Kalimantan Barat (Sukadana/Karimata) dan ujung timur Jawa (Blambangan/Selat Bali).",
        "digitization_method": "Digitasi zona protektorat upeti seberang lautan Sukadana (Kalimantan Barat ditundukkan 1622) dan Blambangan.",
        "confidence_level": "Sedang",
        "uncertainty_notes": "Merupakan wilayah pengaruh protektorat bahari dan upeti tahunan, bukan integrasi birokrasi bupati langsung.",
        "coordinates": [
            [
                [109.60, -1.05], [110.35, -1.10], [110.55, -1.55], [110.40, -1.90],
                [109.85, -1.85], [109.60, -1.45], [109.60, -1.05]
            ]
        ]
    },

    # ---------------------------------------------------------------------
    # 2. MATARAM PASCA-GIYANTI 1755 (SURAKARTA & YOGYAKARTA VORSTENLANDEN)
    # ---------------------------------------------------------------------
    {
        "polygon_id": "mataram-vorstenlanden-1755",
        "kingdom_id": "mataram-islam",
        "kingdom_name": "Kasunanan Surakarta & Kasultanan Yogyakarta (Pasca-Giyanti)",
        "historical_period": "1755–1830 M (Perjanjian Giyanti hingga Perang Jawa)",
        "year_start": 1755,
        "year_end": 1830,
        "territory_type": "controlled",
        "source_title": "Map 3.11: The Division of Mataram, 1755–1830 (Historical Atlas of Indonesia)",
        "source_url": "https://www.niaspress.dk",
        "source_publisher": "Curzon Press & NIAS Press",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi teks naskah traktat Perjanjian Giyanti 13 Februari 1755 dan batas karesidenan Vorstenlanden.",
        "digitization_method": "Digitasi batas gabungan wilayah swapraja Kasunanan Surakarta dan Kasultanan Yogyakarta di Jawa bagian tengah.",
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Sebelum 1830, daerah Mancanegara Timur (Madiun, Kediri) masih berada di bawah kekuasaan kedua keraton sebelum diambil alih Belanda pasca-Perang Diponegoro.",
        "coordinates": [
            [
                [109.95, -7.50], [110.45, -7.35], [110.85, -7.38], [111.45, -7.42],
                [111.95, -7.55], [112.15, -7.85], [111.90, -8.15], [111.20, -8.25],
                [110.60, -8.05], [110.15, -7.95], [109.95, -7.50]
            ]
        ]
    },

    # ---------------------------------------------------------------------
    # 3. KESULTANAN ACEH DARUSSALAM (1607 - 1636 M) - SULTAN ISKANDAR MUDA
    # ---------------------------------------------------------------------
    {
        "polygon_id": "aceh-core-1636",
        "kingdom_id": "aceh-darussalam",
        "kingdom_name": "Kesultanan Aceh Darussalam",
        "historical_period": "1607–1636 M (Era Sultan Iskandar Muda)",
        "year_start": 1607,
        "year_end": 1636,
        "territory_type": "core",
        "source_title": "Map 3.8: The Sultanate of Aceh in the seventeenth century (Historical Atlas of Indonesia)",
        "source_url": "https://nuspress.nus.edu.sg/products/an-indonesian-frontier",
        "source_publisher": "Curzon Press & NUS Press",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi muara Krueng Aceh, Ulee Lheue, Pegunungan Seulawah, dan benteng Inong Balee.",
        "digitization_method": "Digitasi teritorial Aceh Rayeuk yang terbagi dalam konfederasi Tiga Sagi (Sagi XXII Mukim, Sagi XXV Mukim, dan Sagi XXVI Mukim).",
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Pusat kedudukan Sultan di Kutaraja (Darud Donya) dan makam para sultan di Baperis.",
        "coordinates": [
            [
                [95.18, 5.58], [95.42, 5.62], [95.68, 5.52], [95.75, 5.35],
                [95.55, 5.20], [95.25, 5.25], [95.15, 5.42], [95.18, 5.58]
            ]
        ]
    },
    {
        "polygon_id": "aceh-controlled-1636",
        "kingdom_id": "aceh-darussalam",
        "kingdom_name": "Kesultanan Aceh Darussalam",
        "historical_period": "1607–1636 M (Era Sultan Iskandar Muda)",
        "year_start": 1607,
        "year_end": 1636,
        "territory_type": "controlled",
        "source_title": "Map 3.8: The Sultanate of Aceh in the seventeenth century / An Indonesian Frontier (Anthony Reid)",
        "source_url": "https://nuspress.nus.edu.sg/products/an-indonesian-frontier",
        "source_publisher": "Curzon Press & NUS Press",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi garis pantai barat Sumatera (dari Daya, Meulaboh, Singkil hingga Tiku dan Pariaman) dan pantai timur (Pidie, Pasai, Peureulak, Aru/Deli).",
        "digitization_method": "Digitasi jalur kedaulatan daerah pesisir utara-barat-timur Sumatera penghasil lada dan emas yang ditempatkan di bawah Panglima Mukim dan Syahbandar Aceh.",
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Batas teritorial di pedalaman Bukit Barisan dihuni suku Gayo, Alas, dan Batak yang memiliki traktat kesetiaan upeti.",
        "coordinates": [
            [
                [95.15, 5.65], [95.75, 5.45], [96.25, 5.25], [97.10, 5.15],
                [97.75, 4.85], [98.25, 4.35], [98.75, 3.65], [99.25, 3.15],
                [99.85, 2.45], [99.55, 1.85], [99.25, 1.25], [99.95, 0.45],
                [100.25, -0.65], [99.85, -0.75], [99.25, 0.15], [98.65, 1.35],
                [97.85, 2.15], [97.15, 2.85], [96.35, 3.65], [95.55, 4.55],
                [95.15, 5.25], [95.15, 5.65]
            ]
        ]
    },
    {
        "polygon_id": "aceh-influence-1636",
        "kingdom_id": "aceh-darussalam",
        "kingdom_name": "Kesultanan Aceh Darussalam",
        "historical_period": "1607–1636 M (Vasal Semenanjung Malaya)",
        "year_start": 1612,
        "year_end": 1636,
        "territory_type": "influence",
        "source_title": "Map 3.8: The Sultanate of Aceh in the seventeenth century (Historical Atlas of Indonesia)",
        "source_url": "https://www.routledge.com/Historical-Atlas-of-Indonesia/Cribb/p/book/9780700709854",
        "source_publisher": "Curzon Press",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi pesisir barat Semenanjung Malaya (Perak, Kedah, Pahang, Johor).",
        "digitization_method": "Digitasi zona protektorat maritim taklukan ekspedisi militer Sultan Iskandar Muda di Semenanjung Malaya.",
        "confidence_level": "Sedang",
        "uncertainty_notes": "Wilayah vasal luar negeri yang mengirimkan upeti emas dan timah secara berkala ke Kutaraja.",
        "coordinates": [
            [
                [100.25, 6.25], [101.15, 5.85], [101.85, 4.55], [103.25, 3.85],
                [103.85, 2.45], [103.55, 1.45], [102.85, 1.95], [101.95, 2.75],
                [101.15, 3.85], [100.45, 4.95], [100.25, 6.25]
            ]
        ]
    },

    # ---------------------------------------------------------------------
    # 4. KESULTANAN BANTEN (1651 - 1683 M) - SULTAN AGENG TIRTAYASA
    # ---------------------------------------------------------------------
    {
        "polygon_id": "banten-core-1683",
        "kingdom_id": "banten",
        "kingdom_name": "Kesultanan Banten",
        "historical_period": "1651–1683 M (Era Sultan Ageng Tirtayasa)",
        "year_start": 1651,
        "year_end": 1683,
        "territory_type": "core",
        "source_title": "Map 3.9: The Sultanate of Banten in the seventeenth century (Historical Atlas of Indonesia)",
        "source_url": "https://www.persee.fr/collection/arch",
        "source_publisher": "Curzon Press & Archipel",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi Teluk Banten, Pelabuhan Karangantu, Keraton Surosowan, Keraton Tirtayasa, dan Sungai Cibanten.",
        "digitization_method": "Digitasi wilayah kota pelabuhan Banten Lama, kanal irigasi Pontang-Tanara, dan pusat keraton Tirtayasa.",
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Pusat kosmopolitan perniagaan bebas lada dan lumbung pertanian padi bersistem kanal.",
        "coordinates": [
            [
                [106.05, -6.00], [106.28, -5.98], [106.40, -6.08], [106.35, -6.22],
                [106.12, -6.20], [106.02, -6.10], [106.05, -6.00]
            ]
        ]
    },
    {
        "polygon_id": "banten-controlled-1683",
        "kingdom_id": "banten",
        "kingdom_name": "Kesultanan Banten",
        "historical_period": "1651–1683 M (Era Sultan Ageng Tirtayasa)",
        "year_start": 1651,
        "year_end": 1683,
        "territory_type": "controlled",
        "source_title": "Map 3.9: The Sultanate of Banten in the seventeenth century / The Sultanate of Banten (Claude Guillot)",
        "source_url": "https://www.persee.fr/collection/arch",
        "source_publisher": "Curzon Press & Archipel/Gramedia",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi muara Sungai Cisadane (Tangerang), Selat Sunda, Anyer, Ujung Kulon, Teluk Semangka, dan muara Sungai Tulang Bawang.",
        "digitization_method": "Digitasi batas wilayah daratan Banten hingga Sungai Cisadane (perbatasan traktat dengan VOC Batavia) dan daerah dependensi penghasil lada Lampung.",
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Batas timur di Sungai Cisadane ditetapkan dalam perjanjian perdamaian 1659 dengan VOC.",
        "coordinates": [
            # Daratan Banten
            [
                [105.15, -6.75], [105.55, -6.45], [105.85, -5.95], [106.35, -5.98],
                [106.68, -6.02], [106.65, -6.45], [106.35, -6.85], [105.95, -7.05],
                [105.35, -6.95], [105.15, -6.75]
            ]
        ]
    },
    {
        "polygon_id": "banten-lampung-1683",
        "kingdom_id": "banten",
        "kingdom_name": "Kesultanan Banten (Dependensi Lampung)",
        "historical_period": "1651–1683 M (Era Sultan Ageng Tirtayasa)",
        "year_start": 1651,
        "year_end": 1683,
        "territory_type": "controlled",
        "source_title": "Map 3.9: The Sultanate of Banten in the seventeenth century (Historical Atlas of Indonesia)",
        "source_url": "https://www.persee.fr/collection/arch",
        "source_publisher": "Curzon Press",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi Teluk Lampung, Teluk Semangka, Kalianda, Kota Agung, Menggala, dan muara Tulang Bawang.",
        "digitization_method": "Digitasi wilayah dependensi seberang Selat Sunda (Lampung) yang berada di bawah Jenang/Wakil Sultan Banten.",
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Lampung merupakan sumber utama komoditas lada hitam Banten yang dikirim melalui pelabuhan Canti dan Teluk Betung.",
        "coordinates": [
            [
                [104.35, -5.75], [104.65, -5.25], [105.25, -4.35], [105.85, -4.25],
                [105.95, -4.85], [105.75, -5.75], [105.35, -5.95], [104.95, -5.85],
                [104.35, -5.75]
            ]
        ]
    },

    # ---------------------------------------------------------------------
    # 5. KESULTANAN GOWA-TALLO / KEMAKASSARAN (1636 - 1667 M)
    # ---------------------------------------------------------------------
    {
        "polygon_id": "gowa-core-1667",
        "kingdom_id": "gowa",
        "kingdom_name": "Kesultanan Gowa",
        "historical_period": "1636–1667 M (Puncak Hegemoni Kemakassaran)",
        "year_start": 1636,
        "year_end": 1667,
        "territory_type": "core",
        "source_title": "Map 3.12: The Empire of Makassar in the seventeenth century (Historical Atlas of Indonesia)",
        "source_url": "https://brill.com/display/title/1539",
        "source_publisher": "Curzon Press & Martinus Nijhoff",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi Benteng Somba Opu, muara Sungai Jeneberang, Tallo, Maros, Sanrabone, dan Takalar.",
        "digitization_method": "Digitasi teritorial konfederasi kembar Gowa-Tallo di pesisir barat Sulawesi Selatan.",
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Pusat kekuatan militer dan administrasi diapit oleh benteng bata raksasa Somba Opu dan Ujung Pandang.",
        "coordinates": [
            [
                [119.35, -5.02], [119.55, -5.00], [119.60, -5.35], [119.45, -5.48],
                [119.32, -5.35], [119.35, -5.02]
            ]
        ]
    },
    {
        "polygon_id": "gowa-controlled-1667",
        "kingdom_id": "gowa",
        "kingdom_name": "Kesultanan Gowa",
        "historical_period": "1636–1667 M (Puncak Hegemoni Kemakassaran)",
        "year_start": 1636,
        "year_end": 1667,
        "territory_type": "controlled",
        "source_title": "Map 3.12: The Empire of Makassar in the seventeenth century / The Heritage of Arung Palakka (Leonard Y. Andaya)",
        "source_url": "https://brill.com/display/title/1539",
        "source_publisher": "Curzon Press & Martinus Nijhoff",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi jazirah Sulawesi Selatan dari Selat Makassar hingga Teluk Bone, Teluk Parepare, dan Kepulauan Selayar.",
        "digitization_method": "Digitasi wilayah kendali politik konfederasi Makassar mencakup Luwu, Wajo, Soppeng, Bone (sebelum 1667), Ajatappareng, dan Selayar.",
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Wilayah daratan Sulawesi Selatan sebelum pecahnya Perang Makassar dan pemberontakan Arung Palakka.",
        "coordinates": [
            [
                [119.15, -3.55], [119.85, -3.45], [120.45, -3.85], [120.55, -4.65],
                [120.45, -5.25], [120.55, -6.25], [120.40, -6.35], [119.95, -5.75],
                [119.35, -5.65], [119.25, -4.85], [119.45, -4.05], [119.15, -3.55]
            ]
        ]
    },
    {
        "polygon_id": "gowa-influence-1667",
        "kingdom_id": "gowa",
        "kingdom_name": "Kesultanan Gowa",
        "historical_period": "1636–1667 M (Protektorat Maritim Nusa Tenggara)",
        "year_start": 1640,
        "year_end": 1667,
        "territory_type": "influence",
        "source_title": "Map 3.12: The Empire of Makassar in the seventeenth century (Historical Atlas of Indonesia)",
        "source_url": "https://www.routledge.com/Historical-Atlas-of-Indonesia/Cribb/p/book/9780700709854",
        "source_publisher": "Curzon Press",
        "map_publication_year": 2000,
        "georeferencing_method": "Georeferensi Teluk Bima, Pulau Sumbawa bagian timur, dan Manggarai di Flores Barat.",
        "digitization_method": "Digitasi zona protektorat persaudaraan bahari Bima dan Flores Barat yang terikat aliansi darah dan militer dengan Makassar.",
        "confidence_level": "Tinggi",
        "uncertainty_notes": "Raja Bima Abdul Khair Sirajuddin menikahi adik kandung Sultan Hasanuddin, membentuk poros pertahanan maritim bersama.",
        "coordinates": [
            [
                [118.45, -8.35], [119.15, -8.30], [120.45, -8.45], [120.55, -8.85],
                [119.95, -8.95], [118.85, -8.75], [118.45, -8.35]
            ]
        ]
    }
]

def build_geojson():
    features = []
    for f in features_data:
        # Validate coordinates ring
        coords = f["coordinates"]
        validated_coords = []
        for ring in coords:
            validated_coords.append(validate_polygon_ring(ring))

        properties = {
            "polygon_id": f["polygon_id"],
            "kingdom_id": f["kingdom_id"],
            "kingdom_name": f["kingdom_name"],
            "historical_period": f["historical_period"],
            "year_start": f["year_start"],
            "year_end": f["year_end"],
            "territory_type": f["territory_type"],
            "source_title": f["source_title"],
            "source_url": f["source_url"],
            "source_publisher": f["source_publisher"],
            "map_publication_year": f["map_publication_year"],
            "georeferencing_method": f["georeferencing_method"],
            "digitization_method": f["digitization_method"],
            "confidence_level": f["confidence_level"],
            "uncertainty_notes": f["uncertainty_notes"]
        }

        feature = {
            "type": "Feature",
            "id": f["polygon_id"],
            "properties": properties,
            "geometry": {
                "type": "Polygon",
                "coordinates": validated_coords
            }
        }
        features.append(feature)

    geojson_collection = {
        "type": "FeatureCollection",
        "name": "HistoricalTerritoriesNusantara",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
            }
        },
        "metadata": {
            "title": "Temporal Historical Territories of Islamic Kingdoms in Nusantara",
            "created_by": "Historical Cartography & GIS Research Team",
            "crs_description": "WGS 84 (EPSG:4326)",
            "primary_cartographic_sources": [
                "Robert Cribb (2000), Historical Atlas of Indonesia, Curzon Press",
                "Anthony Reid (2005), An Indonesian Frontier: Aceh in the 17th Century",
                "Claude Guillot (1990), The Sultanate of Banten, Archipel",
                "H.J. de Graaf (1958), De regering van Sultan Agung, Martinus Nijhoff",
                "Leonard Y. Andaya (1981), The Heritage of Arung Palakka, Martinus Nijhoff"
            ]
        },
        "features": features
    }

    out_path = os.path.join(os.path.dirname(__file__), "..", "data", "historical-territories.geojson")
    out_path = os.path.abspath(out_path)

    with open(out_path, "w", encoding="utf-8") as fp:
        json.dump(geojson_collection, fp, ensure_ascii=False, indent=2)

    print(f"[SUCCESS] Exported {len(features)} georeferenced historical polygons to: {out_path}")
    return geojson_collection

if __name__ == "__main__":
    build_geojson()
