/**
 * WebGIS Islamic Kingdoms Nusantara - Leaflet Map Module
 * Upgraded with Historical Territory Mapping & Temporal Polygons
 */

window.HistoryMap = (function() {
  let map = null;
  let markersLayer = null;
  let territoriesLayer = null;
  let sitesLayer = null;
  let territoriesData = null;
  let sitesData = [];
  let sultansData = [];
  let tileLayers = {};
  let currentBaseLayer = 'osm';
  let kingdomMarkers = {}; // kingdomId -> Leaflet marker
  let siteMarkers = {}; // siteId -> Leaflet marker
  let activePolygons = []; // currently rendered polygon layers
  let showTerritories = true; // layer toggle state
  let showKingdoms = true;
  let showSites = true;
  let selectedSiteCategory = 'all';

  const INDONESIA_CENTER = [-0.7893, 118.9213];
  const DEFAULT_ZOOM = 5;

  function initMap(containerId) {
    // 100% Free Public Basemaps - Zero API Key Required
    tileLayers = {
      osm: L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> contributors',
        maxZoom: 19
      }),
      natgeo: L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; National Geographic, Esri &mdash; National Geographic Style',
        maxZoom: 16
      }),
      topo: L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, SRTM | Style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a>',
        maxZoom: 17
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
      layers: [tileLayers.osm]
    });

    // Custom Zoom Control at Top-Right
    L.control.zoom({ position: 'topright' }).addTo(map);

    // CRITICAL: Dedicated Pane for Historical Territories (Z-Index 350)
    // Ensures polygons are placed below markers (Z-Index 600) so markers always stay clickable
    map.createPane('territoriesPane');
    const tPane = map.getPane('territoriesPane');
    if (tPane) {
      tPane.style.zIndex = 350;
    }

    territoriesLayer = L.layerGroup().addTo(map);
    sitesLayer = L.layerGroup().addTo(map);
    markersLayer = L.layerGroup().addTo(map);

    return map;
  }

  function setBaseLayer(layerKey) {
    if (!tileLayers[layerKey] || layerKey === currentBaseLayer) return;
    map.removeLayer(tileLayers[currentBaseLayer]);
    map.addLayer(tileLayers[layerKey]);
    currentBaseLayer = layerKey;
  }

  function setTerritoriesData(geojsonData) {
    territoriesData = geojsonData;
  }

  function setSitesData(sitesArray) {
    sitesData = sitesArray || [];
  }

  function setSultansData(sultansArray) {
    sultansData = sultansArray || [];
  }

  function toggleTerritories(enable) {
    if (typeof enable === 'boolean') {
      showTerritories = enable;
    } else {
      showTerritories = !showTerritories;
    }
    return showTerritories;
  }

  function isTerritoriesVisible() {
    return showTerritories;
  }

  function toggleKingdoms(enable) {
    if (typeof enable === 'boolean') {
      showKingdoms = enable;
    } else {
      showKingdoms = !showKingdoms;
    }
    return showKingdoms;
  }

  function toggleSites(enable) {
    if (typeof enable === 'boolean') {
      showSites = enable;
    } else {
      showSites = !showSites;
    }
    return showSites;
  }

  function setSiteCategoryFilter(cat) {
    selectedSiteCategory = cat || 'all';
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

    // Check if kingdom has verified polygon in database
    const hasPolygon = territoriesData && territoriesData.features.some(f => f.properties.kingdom_id === kingdom.id);
    const territoryBadge = hasPolygon 
      ? `<div style="font-size:10.5px; color:#047857; margin-top:5px; display:flex; align-items:center; gap:4px;">
           <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
           <strong>Peta Wilayah Historis Tersedia</strong>
         </div>`
      : `<div style="font-size:10.5px; color:#64748b; margin-top:5px; font-style:italic;">
           ℹ️ Poligon wilayah belum tersedia dari sumber historis terverifikasi.
         </div>`;

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
        ${territoryBadge}
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

  // =========================================================================
  // HISTORICAL TERRITORY POLYGON STYLING & POPUP
  // =========================================================================

  function getTerritoryStyle(type) {
    if (type === 'core') {
      return {
        pane: 'territoriesPane',
        fillColor: '#059669', // Deep Emerald
        color: '#047857',
        weight: 2.2,
        fillOpacity: 0.42,
        dashArray: null
      };
    } else if (type === 'controlled') {
      return {
        pane: 'territoriesPane',
        fillColor: '#d97706', // Warm Amber
        color: '#b45309',
        weight: 1.8,
        fillOpacity: 0.32,
        dashArray: null
      };
    } else if (type === 'influence') {
      return {
        pane: 'territoriesPane',
        fillColor: '#6366f1', // Indigo / Slate
        color: '#4f46e5',
        weight: 1.6,
        fillOpacity: 0.20,
        dashArray: '6, 6'
      };
    } else {
      return {
        pane: 'territoriesPane',
        fillColor: '#64748b',
        color: '#475569',
        weight: 1.5,
        fillOpacity: 0.18,
        dashArray: '4, 4'
      };
    }
  }

  function getTerritoryTypeLabel(type) {
    if (type === 'core') return 'Wilayah Inti (Kutanegara / Negaragung)';
    if (type === 'controlled') return 'Wilayah Taklukan & Dependensi Langsung (Mancanegara / Pasisir)';
    if (type === 'influence') return 'Zona Pengaruh Maritim / Vasal Luar Negeri';
    return 'Estimasi / Interpretasi Kartografis';
  }

  function buildTerritoryPopupContent(props) {
    const typeLabel = getTerritoryTypeLabel(props.territory_type);
    const confidenceBadge = props.confidence_level === 'Tinggi'
      ? `<span style="background:#bbf7d0; color:#166534; font-size:10px; font-weight:700; padding:2px 8px; border-radius:99px;">Kepastian: Tinggi</span>`
      : `<span style="background:#fef08a; color:#854d0e; font-size:10px; font-weight:700; padding:2px 8px; border-radius:99px;">Kepastian: Sedang</span>`;

    return `
      <div class="popup-header" style="background:linear-gradient(135deg, #18222d 0%, #2a3b4c 100%);">
        <div class="popup-region" style="color:#fcd34d;">PETA WILAYAH HISTORIS &bull; ${confidenceBadge}</div>
        <div class="popup-title">${props.kingdom_name}</div>
      </div>
      <div class="popup-body">
        <div class="popup-meta-item">
          <span class="popup-meta-label">Klasifikasi</span>
          <span class="popup-meta-value">${typeLabel}</span>
        </div>
        <div class="popup-meta-item">
          <span class="popup-meta-label">Periode Waktu</span>
          <span class="popup-meta-value">${props.historical_period} (${props.year_start}&ndash;${props.year_end} M)</span>
        </div>
        <div class="popup-meta-item">
          <span class="popup-meta-label">Sumber Peta</span>
          <span class="popup-meta-value">${props.source_title} (${props.map_publication_year})</span>
        </div>
        <div class="popup-meta-item">
          <span class="popup-meta-label">Metode Digitasi</span>
          <span class="popup-meta-value">${props.digitization_method}</span>
        </div>
        <div style="font-size:11px; background:#f8fafc; border-left:3px solid #3b82f6; padding:6px 10px; border-radius:0 6px 6px 0; margin-top:8px; color:#475569;">
          <strong>Keterbatasan & Ketidakpastian:</strong> ${props.uncertainty_notes}
        </div>
      </div>
      <div class="popup-footer">
        <button class="btn-popup-detail" onclick="window.DetailDrawer.openKingdom('${props.kingdom_id}')">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
          Lihat Profil Lengkap Kerajaan & Silsilah Sultan
        </button>
      </div>
    `;
  }

  function renderTerritories(currentYear, filters, kingdoms) {
    territoriesLayer.clearLayers();
    activePolygons = [];

    if (!showTerritories || !territoriesData || !territoriesData.features) {
      return 0;
    }

    let renderedCount = 0;

    territoriesData.features.forEach(feature => {
      const p = feature.properties;

      // Temporal Filter: Check if selected year is within territory active timeframe
      if (currentYear < p.year_start || currentYear > p.year_end) {
        return;
      }

      // Region Filter
      if (filters.region && filters.region !== 'Semua') {
        const k = kingdoms.find(k => k.id === p.kingdom_id);
        if (k && k.region !== filters.region) {
          return;
        }
      }

      // Search Filter
      if (filters.search) {
        const query = filters.search.toLowerCase();
        const matchName = p.kingdom_name.toLowerCase().includes(query);
        const matchTitle = p.source_title.toLowerCase().includes(query);
        if (!matchName && !matchTitle) {
          return;
        }
      }

      const defaultStyle = getTerritoryStyle(p.territory_type);

      const polyLayer = L.geoJSON(feature, {
        pane: 'territoriesPane',
        style: defaultStyle,
        onEachFeature: function(feat, layer) {
          // Hover highlighting
          layer.on({
            mouseover: function(e) {
              const l = e.target;
              l.setStyle({
                weight: defaultStyle.weight + 1.5,
                fillOpacity: Math.min(defaultStyle.fillOpacity + 0.25, 0.75)
              });
            },
            mouseout: function(e) {
              polyLayer.resetStyle(e.target);
            },
            click: function(e) {
              L.DomEvent.stopPropagation(e);
            }
          });

          // Bind Tooltip & Popup
          layer.bindTooltip(`<strong>${p.kingdom_name}</strong><br><small>${getTerritoryTypeLabel(p.territory_type)}</small>`, {
            sticky: true,
            className: 'historical-territory-tooltip'
          });

          layer.bindPopup(() => buildTerritoryPopupContent(p), {
            maxWidth: 340,
            className: 'kingdom-popup-custom'
          });
        }
      });

      territoriesLayer.addLayer(polyLayer);
      activePolygons.push(polyLayer);
      renderedCount++;
    });

    return renderedCount;
  }

  function createSiteIcon(site) {
    let pinClass = 'site-pin-mosque';
    let iconChar = '🕌';

    if (site.site_type === 'palace') {
      pinClass = 'site-pin-palace';
      iconChar = '👑';
    } else if (site.site_type === 'tomb') {
      pinClass = 'site-pin-tomb';
      iconChar = '🏛️';
    } else if (site.site_type === 'fortress') {
      pinClass = 'site-pin-fortress';
      iconChar = '🛡️';
    } else if (site.site_type === 'port') {
      pinClass = 'site-pin-port';
      iconChar = '⚓';
    }

    return L.divIcon({
      className: 'custom-site-marker',
      html: `
        <div class="site-marker-pin ${pinClass}" style="width:26px; height:26px; font-size:12px;" title="${site.site_name} (${site.construction_period_display})">
          <span>${iconChar}</span>
        </div>
      `,
      iconSize: [26, 26],
      iconAnchor: [13, 13],
      popupAnchor: [0, -14]
    });
  }

  function buildSitePopupContent(site) {
    let typeLabel = "Masjid Bersejarah";
    if (site.site_type === 'palace') typeLabel = "Keraton / Istana";
    if (site.site_type === 'tomb') typeLabel = "Makam Sultan & Tokoh";
    if (site.site_type === 'fortress') typeLabel = "Benteng Pertahanan";
    if (site.site_type === 'port') typeLabel = "Bandar Niaga / Pelabuhan Kuno";

    return `
      <div class="leaflet-popup-content">
        <div class="popup-header" style="background: linear-gradient(135deg, #0f4c3a 0%, #1a5d48 100%);">
          <div class="popup-region" style="color:#fde68a;">${typeLabel}</div>
          <div class="popup-title">${site.site_name}</div>
        </div>
        <div class="popup-body">
          <div class="popup-meta-item">
            <span class="popup-meta-label">Pembangunan:</span>
            <span class="popup-meta-value">${site.construction_period_display}</span>
          </div>
          <div class="popup-meta-item">
            <span class="popup-meta-label">Status Cagar:</span>
            <span class="popup-meta-value" style="font-size:0.75rem; color:#0f4c3a;">${site.heritage_status || 'Cagar Budaya Nasional'}</span>
          </div>
          <div class="popup-summary">
            ${site.historical_significance}
          </div>
        </div>
        <div class="popup-footer">
          <button class="btn-popup-detail" onclick="window.DetailDrawer.openSite('${site.site_id}')">
            <span>Buka Detail Situs & Historiografi</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
        </div>
      </div>
    `;
  }

  function renderSites(currentYear, filters) {
    // Preserve open popup if any
    let openPopupSiteId = null;
    for (const sid in siteMarkers) {
      if (siteMarkers[sid].isPopupOpen && siteMarkers[sid].isPopupOpen()) {
        openPopupSiteId = sid;
        break;
      }
    }

    sitesLayer.clearLayers();
    siteMarkers = {};

    if (!showSites || !sitesData || sitesData.length === 0) {
      return 0;
    }

    let renderedSites = 0;
    const isSearching = Boolean(filters.search && filters.search.trim().length > 0);
    const query = isSearching ? filters.search.toLowerCase().trim() : '';

    sitesData.forEach(site => {
      // Category filter (if selected)
      if (selectedSiteCategory !== 'all' && site.site_type !== selectedSiteCategory) {
        return;
      }

      // Search filter across ALL TIME and ALL TYPES
      if (isSearching) {
        const matchName = site.site_name.toLowerCase().includes(query);
        const matchSignificance = site.historical_significance && site.historical_significance.toLowerCase().includes(query);
        const matchType = site.site_type && site.site_type.toLowerCase().includes(query);
        const matchCondition = site.current_condition && site.current_condition.toLowerCase().includes(query);
        const matchPeriod = site.construction_period_display && site.construction_period_display.toLowerCase().includes(query);
        if (!matchName && !matchSignificance && !matchType && !matchCondition && !matchPeriod) {
          return;
        }
        // When searching, bypass construction_year filter so sites appear across all time!
      } else {
        // Temporal filter: Site must be constructed by this year, unless showAllHistorical is true
        if (!filters.showAllHistorical && site.construction_year > currentYear) {
          return;
        }
      }

      const icon = createSiteIcon(site);
      const marker = L.marker([site.latitude, site.longitude], {
        icon: icon,
        title: site.site_name,
        riseOnHover: true
      });

      marker.bindPopup(() => buildSitePopupContent(site), {
        maxWidth: 300,
        className: 'kingdom-popup-custom'
      });

      // Auto-pause timeline when inspecting site so timeseries does not destroy the popup
      marker.on('click', () => {
        if (window.TimelineController && window.TimelineController.pause) {
          window.TimelineController.pause();
        }
      });
      marker.on('popupopen', () => {
        if (window.TimelineController && window.TimelineController.pause) {
          window.TimelineController.pause();
        }
      });

      sitesLayer.addLayer(marker);
      siteMarkers[site.site_id] = marker;
      renderedSites++;
    });

    // Restore open popup if still present
    if (openPopupSiteId && siteMarkers[openPopupSiteId]) {
      siteMarkers[openPopupSiteId].openPopup();
    }

    return renderedSites;
  }

  function renderMarkers(kingdoms, currentYear, filters) {
    // Preserve open popup if any
    let openPopupKingdomId = null;
    for (const kid in kingdomMarkers) {
      if (kingdomMarkers[kid].isPopupOpen && kingdomMarkers[kid].isPopupOpen()) {
        openPopupKingdomId = kid;
        break;
      }
    }

    markersLayer.clearLayers();
    kingdomMarkers = {};

    let activeCount = 0;
    let goldenAgeCount = 0;

    // 1. Render Polygons First in dedicated pane (Z-Index 350)
    const territoryCount = renderTerritories(currentYear, filters, kingdoms);

    // 2. Render Historical Sites
    const sitesCount = renderSites(currentYear, filters);

    // 3. Render Kingdom Markers on Top in markerPane (Z-Index 600)
    const isSearching = Boolean(filters.search && filters.search.trim().length > 0);
    const query = isSearching ? filters.search.toLowerCase().trim() : '';

    if (showKingdoms) {
      kingdoms.forEach(kingdom => {
        const status = getKingdomStatus(kingdom, currentYear);

        // Filter: Region
        if (filters.region && filters.region !== 'Semua' && kingdom.region !== filters.region) {
          return;
        }

        // Filter: Search across ALL TIME and ALL TYPES (Kingdoms, Sultans, Capitals, Founders, Summaries)
        if (isSearching) {
          const matchName = kingdom.name.toLowerCase().includes(query);
          const matchAlt = kingdom.alternate_names && kingdom.alternate_names.some(a => a.toLowerCase().includes(query));
          const matchCapital = kingdom.capital_city && kingdom.capital_city.toLowerCase().includes(query);
          const matchFounder = kingdom.founder && kingdom.founder.toLowerCase().includes(query);
          const matchSummary = kingdom.historical_summary && kingdom.historical_summary.toLowerCase().includes(query);

          // Check if any sultan in this kingdom matches
          const matchSultan = sultansData.some(s => s.kingdom_id === kingdom.id && (
            s.name.toLowerCase().includes(query) || (s.biography && s.biography.toLowerCase().includes(query))
          ));

          if (!matchName && !matchAlt && !matchCapital && !matchFounder && !matchSummary && !matchSultan) {
            return;
          }
          // Note: When isSearching is true, DO NOT filter out status === 'not_yet_founded' or 'ended'!
          // The matched kingdom will be shown across all time!
        } else {
          // Normal mode (not searching):
          // Filter: Only Golden Age
          if (filters.onlyGoldenAge && status !== 'golden_age') {
            return;
          }

          // Filter: Show Active Only in Year vs All Historical
          if (!filters.showAllHistorical) {
            if (status === 'not_yet_founded' || status === 'ended') {
              return;
            }
          }
        }

        if (status === 'active' || status === 'golden_age' || status === 'declining') {
          activeCount++;
        }
        if (status === 'golden_age') {
          goldenAgeCount++;
        }

        // When searching, if the kingdom is outside current year range, render it with active visibility so user can see it
        const effectiveStatus = (isSearching && (status === 'not_yet_founded' || status === 'ended')) ? 'active' : status;

        const icon = createMarkerIcon(kingdom, effectiveStatus);
        const marker = L.marker([kingdom.coordinates.lat, kingdom.coordinates.lng], {
          icon: icon,
          title: kingdom.name,
          riseOnHover: true
        });

        marker.bindPopup(() => buildPopupContent(kingdom, effectiveStatus, currentYear), {
          maxWidth: 320,
          className: 'kingdom-popup-custom'
        });

        // Auto-pause timeline when clicking marker or opening popup
        marker.on('click', () => {
          if (window.TimelineController && window.TimelineController.pause) {
            window.TimelineController.pause();
          }
          map.panTo([kingdom.coordinates.lat, kingdom.coordinates.lng]);
        });
        marker.on('popupopen', () => {
          if (window.TimelineController && window.TimelineController.pause) {
            window.TimelineController.pause();
          }
        });

        markersLayer.addLayer(marker);
        kingdomMarkers[kingdom.id] = marker;
      });
    }

    // Restore open popup if still present
    if (openPopupKingdomId && kingdomMarkers[openPopupKingdomId]) {
      kingdomMarkers[openPopupKingdomId].openPopup();
    }

    return {
      activeCount: activeCount,
      goldenAgeCount: goldenAgeCount,
      totalRendered: Object.keys(kingdomMarkers).length,
      territoriesRendered: territoryCount,
      sitesRendered: sitesCount
    };
  }

  function focusSite(siteId) {
    const site = sitesData.find(s => s.site_id === siteId);
    if (!site) return;

    const isMobile = window.innerWidth < 768;
    const targetLat = isMobile ? site.latitude - 0.3 : site.latitude;

    map.flyTo([targetLat, site.longitude], isMobile ? 8 : 10, {
      duration: 1.1
    });

    const marker = siteMarkers[siteId];
    if (marker) {
      setTimeout(() => {
        marker.openPopup();
      }, 1150);
    }
  }

  function focusKingdom(kingdomId, kingdoms) {
    const kingdom = kingdoms.find(k => k.id === kingdomId);
    if (!kingdom) return;

    // Check if on mobile (screen width < 768px): offset center slightly upward so bottom sheet doesn't cover point
    const isMobile = window.innerWidth < 768;
    const targetLat = isMobile ? kingdom.coordinates.lat - 0.4 : kingdom.coordinates.lat;

    map.flyTo([targetLat, kingdom.coordinates.lng], isMobile ? 7 : 8, {
      duration: 1.1
    });

    const marker = kingdomMarkers[kingdomId];
    if (marker) {
      setTimeout(() => {
        marker.openPopup();
      }, 1150);
    }
  }

  function resetView() {
    map.flyTo(INDONESIA_CENTER, DEFAULT_ZOOM, { duration: 1 });
  }

  const REGION_BOUNDS = {
    'Semua': [
      [-11.0, 95.0],
      [6.0, 141.0]
    ],
    'Sumatera': [
      [-6.0, 95.0],
      [6.0, 106.0]
    ],
    'Jawa': [
      [-8.8, 105.5],
      [-5.8, 114.6]
    ],
    'Kalimantan': [
      [-4.3, 108.5],
      [4.5, 119.2]
    ],
    'Sulawesi': [
      [-6.2, 118.5],
      [2.0, 125.3]
    ],
    'Maluku & Papua': [
      [-5.5, 125.5],
      [2.5, 135.0]
    ],
    'Nusa Tenggara': [
      [-10.2, 115.5],
      [-7.8, 125.2]
    ]
  };

  function zoomToRegion(region) {
    if (!map) return;

    if (!region || region === 'Semua') {
      resetView();
      return;
    }

    const bounds = REGION_BOUNDS[region];
    if (bounds) {
      map.closePopup();
      const isMobile = window.innerWidth < 768;
      map.flyToBounds(bounds, {
        paddingTopLeft: isMobile ? [15, 15] : [40, 40],
        paddingBottomRight: isMobile ? [15, 85] : [40, 40],
        duration: 1.25,
        maxZoom: region === 'Jawa' ? 7 : (isMobile ? 6 : 7)
      });
    }
  }

  return {
    initMap,
    setBaseLayer,
    setTerritoriesData,
    setSitesData,
    setSultansData,
    toggleTerritories,
    isTerritoriesVisible,
    toggleKingdoms,
    toggleSites,
    setSiteCategoryFilter,
    renderMarkers,
    focusKingdom,
    focusSite,
    resetView,
    zoomToRegion,
    getKingdomStatus
  };
})();
