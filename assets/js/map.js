/**
 * WebGIS Islamic Kingdoms Nusantara - Leaflet Map Module
 */

window.HistoryMap = (function() {
  let map = null;
  let markersLayer = null;
  let tileLayers = {};
  let currentBaseLayer = 'positron';
  let kingdomMarkers = {}; // kingdomId -> Leaflet marker

  const INDONESIA_CENTER = [-0.7893, 118.9213];
  const DEFAULT_ZOOM = 5;

  function initMap(containerId) {
    // Define Base Tile Layers
    tileLayers = {
      positron: L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 19
      }),
      dark: L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 19
      }),
      osm: L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 19
      }),
      satellite: L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
        maxZoom: 18
      })
    };

    map = L.map(containerId, {
      center: INDONESIA_CENTER,
      zoom: DEFAULT_ZOOM,
      minZoom: 4,
      maxZoom: 15,
      zoomControl: false,
      layers: [tileLayers.positron]
    });

    // Custom Zoom Control at Top-Right
    L.control.zoom({ position: 'topright' }).addTo(map);

    markersLayer = L.layerGroup().addTo(map);

    return map;
  }

  function setBaseLayer(layerKey) {
    if (!tileLayers[layerKey] || layerKey === currentBaseLayer) return;
    map.removeLayer(tileLayers[currentBaseLayer]);
    map.addLayer(tileLayers[layerKey]);
    currentBaseLayer = layerKey;
  }

  function getKingdomStatus(kingdom, year) {
    if (year < kingdom.year_founded) {
      return 'not_yet_founded';
    }

    // Check if ended
    if (kingdom.year_ended && year > kingdom.year_ended) {
      if (kingdom.status_timeline_type === 'integrated') {
        return 'integrated';
      } else if (kingdom.status_timeline_type === 'cultural_continuation') {
        return 'cultural_continuation';
      }
      return 'ended';
    }

    // Is active: check if in golden age
    if (kingdom.golden_age) {
      if (year >= kingdom.golden_age.start_year && year <= kingdom.golden_age.end_year) {
        return 'golden_age';
      }
    }

    // Check if near end (within 25 years of fall)
    if (kingdom.year_ended && (kingdom.year_ended - year <= 25) && kingdom.year_ended > year) {
      return 'declining';
    }

    return 'active';
  }

  function createMarkerIcon(kingdom, status) {
    let iconSvg = '';
    let statusClass = `status-${status}`;

    if (status === 'golden_age') {
      // Radiant Crown / Star SVG
      iconSvg = `<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 2l2.4 7.2h7.6l-6.1 4.5 2.3 7.3-6.2-4.6-6.2 4.6 2.3-7.3-6.1-4.5h7.6z"/>
      </svg>`;
    } else if (status === 'active') {
      // Islamic Crescent / Mosque Dome SVG
      iconSvg = `<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79.9 2.59 3.23 4.5 6.09 4.71.39 2.75.7 4.51.7 5.01zm4.71-4.71c-1.89-1.89-4.57-2.73-7.21-2.22.42-2.5 2.36-4.52 4.9-5 3.86-.73 7.42 1.83 7.95 5.61-.92.83-2.25 1.5-5.64 1.61z"/>
      </svg>`;
    } else if (status === 'cultural_continuation' || status === 'integrated') {
      // Heritage Landmark Column SVG
      iconSvg = `<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 3L2 12h3v8h14v-8h3L12 3zm0 4.5c1.38 0 2.5 1.12 2.5 2.5S13.38 12.5 12 12.5 9.5 11.38 9.5 10 10.62 7.5 12 7.5z"/>
      </svg>`;
    } else {
      // Muted Dot / Flag
      iconSvg = `<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
        <circle cx="12" cy="12" r="6"/>
      </svg>`;
    }

    const shortName = kingdom.name.replace('Kesultanan ', '').replace('Kerajaan ', '');

    const html = `
      <div class="custom-kingdom-marker ${statusClass}" title="${kingdom.name}">
        <div class="marker-inner">
          ${iconSvg}
        </div>
        <div class="marker-label">${shortName}</div>
      </div>
    `;

    return L.divIcon({
      html: html,
      className: 'kingdom-leaflet-div-icon',
      iconSize: [32, 32],
      iconAnchor: [16, 16],
      popupAnchor: [0, -18]
    });
  }

  function getStatusBadgeHtml(status, year, kingdom) {
    if (status === 'golden_age') {
      return `<span style="background:#fde68a; color:#92400e; font-size:10px; font-weight:700; padding:2px 8px; border-radius:99px;">⭐ Era Keemasan</span>`;
    } else if (status === 'active') {
      return `<span style="background:#d1fae5; color:#065f46; font-size:10px; font-weight:700; padding:2px 8px; border-radius:99px;">● Berdaulat & Aktif</span>`;
    } else if (status === 'declining') {
      return `<span style="background:#fed7aa; color:#9a3412; font-size:10px; font-weight:700; padding:2px 8px; border-radius:99px;">▼ Fase Kemunduran</span>`;
    } else if (status === 'integrated') {
      return `<span style="background:#dbeafe; color:#1e40af; font-size:10px; font-weight:700; padding:2px 8px; border-radius:99px;">🇮🇩 Integrasi NKRI</span>`;
    } else if (status === 'cultural_continuation') {
      return `<span style="background:#e0e7ff; color:#3730a3; font-size:10px; font-weight:700; padding:2px 8px; border-radius:99px;">🏛️ Lembaga Adat Kultural</span>`;
    } else if (status === 'ended') {
      return `<span style="background:#f1f5f9; color:#475569; font-size:10px; font-weight:700; padding:2px 8px; border-radius:99px;">✕ Telah Runtuh (${kingdom.year_ended} M)</span>`;
    } else {
      return `<span style="background:#f1f5f9; color:#94a3b8; font-size:10px; font-weight:700; padding:2px 8px; border-radius:99px;">○ Belum Berdiri (Berdiri ${kingdom.year_founded} M)</span>`;
    }
  }

  function buildPopupContent(kingdom, status, year) {
    const statusBadge = getStatusBadgeHtml(status, year, kingdom);
    const goldenAgeInfo = kingdom.golden_age 
      ? `<div style="margin-top:6px; font-size:11px; background:#fffbeb; border:1px solid #fef3c7; padding:4px 8px; border-radius:4px; color:#92400e;">
           <strong>Zaman Keemasan:</strong> ${kingdom.golden_age.start_year}–${kingdom.golden_age.end_year} M (${kingdom.golden_age.leader})
         </div>`
      : '';

    return `
      <div class="popup-header">
        <div class="popup-region">${kingdom.region} &bull; ${statusBadge}</div>
        <div class="popup-title">${kingdom.name}</div>
      </div>
      <div class="popup-body">
        <div class="popup-meta-item">
          <span class="popup-meta-label">Masa Eksis</span>
          <span class="popup-meta-value">${kingdom.year_founded_display} &ndash; ${kingdom.year_ended_display}</span>
        </div>
        <div class="popup-meta-item">
          <span class="popup-meta-label">Pusat/Ibu Kota</span>
          <span class="popup-meta-value">${kingdom.capital_city}</span>
        </div>
        <div class="popup-meta-item">
          <span class="popup-meta-label">Pendiri</span>
          <span class="popup-meta-value">${kingdom.founder}</span>
        </div>
        ${goldenAgeInfo}
        <div class="popup-summary">${kingdom.historical_summary}</div>
      </div>
      <div class="popup-footer">
        <button class="btn-popup-detail" onclick="window.DetailDrawer.openKingdom('${kingdom.id}')">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
          Buka Detail Lengkap Kerajaan
        </button>
      </div>
    `;
  }

  function renderMarkers(kingdoms, currentYear, filters) {
    markersLayer.clearLayers();
    kingdomMarkers = {};

    let activeCount = 0;
    let goldenAgeCount = 0;

    kingdoms.forEach(kingdom => {
      const status = getKingdomStatus(kingdom, currentYear);

      // Filter: Region
      if (filters.region && filters.region !== 'Semua' && kingdom.region !== filters.region) {
        return;
      }

      // Filter: Search Text
      if (filters.search) {
        const query = filters.search.toLowerCase();
        const matchName = kingdom.name.toLowerCase().includes(query);
        const matchAlt = kingdom.alternate_names && kingdom.alternate_names.some(a => a.toLowerCase().includes(query));
        const matchCapital = kingdom.capital_city.toLowerCase().includes(query);
        if (!matchName && !matchAlt && !matchCapital) {
          return;
        }
      }

      // Filter: Only Golden Age
      if (filters.onlyGoldenAge && status !== 'golden_age') {
        return;
      }

      // Filter: Show Active Only in Year vs All Historical
      if (!filters.showAllHistorical) {
        // Active-only mode: hide kingdoms not yet founded or already ended without cultural continuation
        if (status === 'not_yet_founded' || status === 'ended') {
          return;
        }
      }

      if (status === 'active' || status === 'golden_age' || status === 'declining') {
        activeCount++;
      }
      if (status === 'golden_age') {
        goldenAgeCount++;
      }

      const icon = createMarkerIcon(kingdom, status);
      const marker = L.marker([kingdom.coordinates.lat, kingdom.coordinates.lng], {
        icon: icon,
        title: kingdom.name
      });

      marker.bindPopup(() => buildPopupContent(kingdom, status, currentYear), {
        maxWidth: 320,
        className: 'kingdom-popup-custom'
      });

      marker.on('click', () => {
        // Center smoothly without losing zoom
        map.panTo([kingdom.coordinates.lat, kingdom.coordinates.lng]);
      });

      markersLayer.addLayer(marker);
      kingdomMarkers[kingdom.id] = marker;
    });

    return {
      activeCount: activeCount,
      goldenAgeCount: goldenAgeCount,
      totalRendered: Object.keys(kingdomMarkers).length
    };
  }

  function focusKingdom(kingdomId, kingdoms) {
    const kingdom = kingdoms.find(k => k.id === kingdomId);
    if (!kingdom) return;

    map.flyTo([kingdom.coordinates.lat, kingdom.coordinates.lng], 8, {
      duration: 1.2
    });

    const marker = kingdomMarkers[kingdomId];
    if (marker) {
      setTimeout(() => {
        marker.openPopup();
      }, 1200);
    }
  }

  function resetView() {
    map.flyTo(INDONESIA_CENTER, DEFAULT_ZOOM, { duration: 1 });
  }

  return {
    initMap,
    setBaseLayer,
    renderMarkers,
    focusKingdom,
    resetView,
    getKingdomStatus
  };
})();
