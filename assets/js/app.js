/**
 * WebGIS Islamic Kingdoms Nusantara - Master Application Orchestrator
 * Upgraded with Historical Territories GeoJSON & Responsive Mobile Interaction
 */

window.App = (function() {
  let kingdoms = [];
  let sultans = [];
  let sources = [];
  let sites = [];
  let events = [];
  let territoriesGeoJSON = null;

  async function init() {
    try {
      showLoading(true);

      // Fetch all database files in parallel
      const [kRes, sRes, srcRes, tRes, sitesRes, eventsRes] = await Promise.all([
        fetch('data/kingdoms.json'),
        fetch('data/sultans.json'),
        fetch('data/sources.json'),
        fetch('data/historical-territories.geojson'),
        fetch('data/sites.json'),
        fetch('data/events.json')
      ]);

      if (!kRes.ok || !sRes.ok || !srcRes.ok) {
        throw new Error("Gagal memuat berkas database JSON kerajaan.");
      }

      kingdoms = await kRes.json();
      sultans = await sRes.json();
      sources = await srcRes.json();
      
      if (tRes.ok) {
        territoriesGeoJSON = await tRes.json();
      }

      if (sitesRes.ok) {
        sites = await sitesRes.json();
      }

      if (eventsRes.ok) {
        events = await eventsRes.json();
      }

      console.log(`[App] Berhasil memuat ${kingdoms.length} kerajaan, ${sultans.length} sultan, ${sources.length} sumber akademik, ${territoriesGeoJSON ? territoriesGeoJSON.features.length : 0} poligon historis, ${sites.length} situs cagar budaya, dan ${events.length} peristiwa sejarah.`);

      // 1. Initialize Map
      HistoryMap.initMap('map-container');
      if (territoriesGeoJSON) {
        HistoryMap.setTerritoriesData(territoriesGeoJSON);
      }
      if (sites.length > 0) {
        HistoryMap.setSitesData(sites);
      }
      if (sultans.length > 0) {
        HistoryMap.setSultansData(sultans);
      }

      // 2. Initialize Detail Drawer
      DetailDrawer.initDetailDrawer(kingdoms, sultans, sources, territoriesGeoJSON, sites, events);

      // 3. Initialize Filters
      FilterManager.initFilters(onFilterOrYearChanged);

      // 4. Initialize Timeline
      TimelineController.initTimeline(
        'timeline-slider',
        'display-year-number',
        'display-epoch-badge',
        onFilterOrYearChanged
      );

      // 5. Setup Modals, Mobile Nav, & Basemap UI
      setupUIInteractions();

      // 6. Initial Render of Markers, Polygons & Statistics
      onFilterOrYearChanged();

      showLoading(false);
    } catch (err) {
      console.error("[App Error]", err);
      showErrorState(err.message);
    }
  }

  function onFilterOrYearChanged() {
    const currentYear = TimelineController.getCurrentYear();
    const filters = FilterManager.getFilterState();

    const stats = HistoryMap.renderMarkers(kingdoms, currentYear, filters);

    // Update bottom status pills
    const activeStatEl = document.getElementById('stat-active-count');
    const goldenStatEl = document.getElementById('stat-golden-count');
    const totalStatEl = document.getElementById('stat-total-rendered');
    const territoryStatEl = document.getElementById('stat-territories-count');
    const sitesStatEl = document.getElementById('stat-sites-count');

    if (activeStatEl) activeStatEl.innerText = stats.activeCount;
    if (goldenStatEl) goldenStatEl.innerText = stats.goldenAgeCount;
    if (totalStatEl) totalStatEl.innerText = stats.totalRendered;
    if (territoryStatEl) territoryStatEl.innerText = stats.territoriesRendered;
    if (sitesStatEl) sitesStatEl.innerText = stats.sitesRendered || 0;
  }

  function setupUIInteractions() {
    // 1. Historical Territories Toggle Button (Desktop)
    const territoriesBtn = document.getElementById('btn-toggle-territories');
    if (territoriesBtn) {
      territoriesBtn.addEventListener('click', () => {
        const isVisible = HistoryMap.toggleTerritories();
        territoriesBtn.classList.toggle('active', isVisible);
        const label = document.getElementById('territories-btn-label');
        if (label) {
          label.innerText = isVisible ? "Wilayah: Aktif" : "Wilayah: Mati";
        }
        const chk = document.getElementById('chk-layer-territories');
        if (chk) chk.checked = isVisible;
        onFilterOrYearChanged();
      });
    }

    // 1b. Historical Sites Toggle Button (Desktop)
    const sitesBtn = document.getElementById('btn-toggle-sites');
    if (sitesBtn) {
      sitesBtn.addEventListener('click', () => {
        const isVisible = HistoryMap.toggleSites();
        sitesBtn.classList.toggle('active', isVisible);
        const label = document.getElementById('sites-btn-label');
        if (label) {
          label.innerText = isVisible ? "Situs: Aktif" : "Situs: Mati";
        }
        const chk = document.getElementById('chk-layer-sites');
        if (chk) chk.checked = isVisible;
        onFilterOrYearChanged();
      });
    }

    // 1c. Mobile Layers & Filters Modal Sheet
    const mobileLayersBtn = document.getElementById('btn-mobile-layers-toggle');
    const mobileLayersModal = document.getElementById('modal-mobile-layers');
    const closeMobileLayersBtn = document.getElementById('btn-close-mobile-layers');

    if (mobileLayersBtn && mobileLayersModal) {
      mobileLayersBtn.addEventListener('click', () => {
        mobileLayersModal.classList.add('open');
      });
    }
    if (closeMobileLayersBtn && mobileLayersModal) {
      closeMobileLayersBtn.addEventListener('click', () => {
        mobileLayersModal.classList.remove('open');
      });
    }

    // Layer Checkboxes inside Mobile Sheet
    const chkKingdoms = document.getElementById('chk-layer-kingdoms');
    if (chkKingdoms) {
      chkKingdoms.addEventListener('change', (e) => {
        HistoryMap.toggleKingdoms(e.target.checked);
        onFilterOrYearChanged();
      });
    }

    const chkTerritories = document.getElementById('chk-layer-territories');
    if (chkTerritories) {
      chkTerritories.addEventListener('change', (e) => {
        const isVisible = HistoryMap.toggleTerritories(e.target.checked);
        if (territoriesBtn) {
          territoriesBtn.classList.toggle('active', isVisible);
          const label = document.getElementById('territories-btn-label');
          if (label) label.innerText = isVisible ? "Wilayah: Aktif" : "Wilayah: Mati";
        }
        onFilterOrYearChanged();
      });
    }

    const chkSites = document.getElementById('chk-layer-sites');
    if (chkSites) {
      chkSites.addEventListener('change', (e) => {
        const isVisible = HistoryMap.toggleSites(e.target.checked);
        if (sitesBtn) {
          sitesBtn.classList.toggle('active', isVisible);
          const label = document.getElementById('sites-btn-label');
          if (label) label.innerText = isVisible ? "Situs: Aktif" : "Situs: Mati";
        }
        onFilterOrYearChanged();
      });
    }

    // Basemap Choice in Mobile Sheet
    document.querySelectorAll('.basemap-choice-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const layerKey = btn.getAttribute('data-basemap');
        HistoryMap.setBaseLayer(layerKey);
        document.querySelectorAll('.basemap-choice-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        document.querySelectorAll('.basemap-item').forEach(i => {
          i.classList.toggle('active', i.getAttribute('data-layer') === layerKey);
        });
      });
    });

    // Mobile Sheet Action Buttons
    const modalToggleModeBtn = document.getElementById('btn-modal-toggle-mode');
    if (modalToggleModeBtn) {
      modalToggleModeBtn.addEventListener('click', () => {
        FilterManager.toggleHistoricalMode();
        mobileLayersModal.classList.remove('open');
      });
    }

    const modalToggleGoldenBtn = document.getElementById('btn-modal-toggle-golden');
    if (modalToggleGoldenBtn) {
      modalToggleGoldenBtn.addEventListener('click', () => {
        FilterManager.toggleGoldenAge();
        mobileLayersModal.classList.remove('open');
      });
    }

    // Auto-close mobile layers sheet when a region badge is clicked so user sees the map zoom action
    if (mobileLayersModal) {
      mobileLayersModal.querySelectorAll('.filter-badge[data-region]').forEach(badge => {
        badge.addEventListener('click', () => {
          mobileLayersModal.classList.remove('open');
        });
      });
    }

    // 1d. Events Chronology Modal
    const eventsBtn = document.getElementById('btn-open-events-modal');
    const mobileEventsBtn = document.getElementById('btn-mobile-events-toggle');
    const eventsModal = document.getElementById('modal-events');
    const closeEventsBtn = document.getElementById('btn-close-events-modal');

    const openEvents = () => {
      renderEventsModal();
      if (eventsModal) eventsModal.classList.add('open');
    };

    if (eventsBtn) eventsBtn.addEventListener('click', openEvents);
    if (mobileEventsBtn) mobileEventsBtn.addEventListener('click', openEvents);
    if (closeEventsBtn && eventsModal) {
      closeEventsBtn.addEventListener('click', () => {
        eventsModal.classList.remove('open');
      });
    }

    // 2. Basemap toggle menu
    const basemapBtn = document.getElementById('btn-toggle-basemap');
    const basemapMenu = document.getElementById('basemap-menu');
    if (basemapBtn && basemapMenu) {
      basemapBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        basemapMenu.classList.toggle('show');
      });

      document.addEventListener('click', () => {
        basemapMenu.classList.remove('show');
      });

      document.querySelectorAll('.basemap-item').forEach(item => {
        item.addEventListener('click', (e) => {
          e.stopPropagation();
          const layerKey = item.getAttribute('data-layer');
          HistoryMap.setBaseLayer(layerKey);
          document.querySelectorAll('.basemap-item').forEach(i => i.classList.remove('active'));
          item.classList.add('active');
          basemapMenu.classList.remove('show');
        });
      });
    }

    // 3. Zoom In & Zoom Out Buttons (Dedicated Top-Right Controls)
    const zoomInBtn = document.getElementById('btn-zoom-in');
    if (zoomInBtn) {
      zoomInBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        HistoryMap.zoomIn();
      });
    }

    const zoomOutBtn = document.getElementById('btn-zoom-out');
    if (zoomOutBtn) {
      zoomOutBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        HistoryMap.zoomOut();
      });
    }

    // 4. Reset View Button
    const resetViewBtn = document.getElementById('btn-reset-map-view');
    if (resetViewBtn) {
      resetViewBtn.addEventListener('click', () => {
        HistoryMap.resetView();
        FilterManager.setRegion('Semua', false);
      });
    }

    // 4. Modal: Sources
    const sourcesBtn = document.getElementById('btn-open-sources-modal');
    const sourcesModal = document.getElementById('modal-sources');
    const closeSourcesBtn = document.getElementById('btn-close-sources-modal');

    if (sourcesBtn && sourcesModal) {
      sourcesBtn.addEventListener('click', () => {
        renderSourcesModal();
        sourcesModal.classList.add('open');
      });
    }
    if (closeSourcesBtn && sourcesModal) {
      closeSourcesBtn.addEventListener('click', () => {
        sourcesModal.classList.remove('open');
      });
    }

    // 5. Modal: Legend & Methodology
    const legendBtn = document.getElementById('btn-open-legend-modal');
    const legendModal = document.getElementById('modal-legend');
    const closeLegendBtn = document.getElementById('btn-close-legend-modal');

    if (legendBtn && legendModal) {
      legendBtn.addEventListener('click', () => {
        legendModal.classList.add('open');
      });
    }
    if (closeLegendBtn && legendModal) {
      closeLegendBtn.addEventListener('click', () => {
        legendModal.classList.remove('open');
      });
    }

    // 6. Mobile Search Toggle
    const mobileSearchBtn = document.getElementById('btn-mobile-search-toggle');
    const searchCenterControls = document.querySelector('.header-center-controls');
    if (mobileSearchBtn && searchCenterControls) {
      mobileSearchBtn.addEventListener('click', () => {
        searchCenterControls.classList.toggle('mobile-open');
        const input = document.getElementById('search-kingdom-input');
        if (searchCenterControls.classList.contains('mobile-open') && input) {
          setTimeout(() => input.focus(), 150);
        }
      });
    }

    // 6b. Unified Omnisearch Live Dropdown (All Time & All Types)
    const searchInput = document.getElementById('search-kingdom-input');
    const searchDropdown = document.getElementById('search-results-dropdown');

    if (searchInput && searchDropdown) {
      const performLiveSearch = (query) => {
        const q = query.trim().toLowerCase();
        if (q.length < 2) {
          searchDropdown.style.display = 'none';
          searchDropdown.innerHTML = '';
          return;
        }

        const matchKingdoms = kingdoms.filter(k => 
          k.name.toLowerCase().includes(q) ||
          (k.alternate_names && k.alternate_names.some(a => a.toLowerCase().includes(q))) ||
          (k.capital_city && k.capital_city.toLowerCase().includes(q)) ||
          (k.founder && k.founder.toLowerCase().includes(q))
        ).slice(0, 5);

        const matchSultans = sultans.filter(s =>
          s.name.toLowerCase().includes(q) ||
          (s.biography && s.biography.toLowerCase().includes(q))
        ).slice(0, 5);

        const matchSites = sites.filter(st =>
          st.site_name.toLowerCase().includes(q) ||
          (st.site_type && st.site_type.toLowerCase().includes(q)) ||
          (st.historical_significance && st.historical_significance.toLowerCase().includes(q))
        ).slice(0, 5);

        const matchEvents = events.filter(e =>
          e.event_name.toLowerCase().includes(q) ||
          (e.description && e.description.toLowerCase().includes(q))
        ).slice(0, 4);

        const totalMatches = matchKingdoms.length + matchSultans.length + matchSites.length + matchEvents.length;

        if (totalMatches === 0) {
          searchDropdown.innerHTML = `
            <div style="padding:12px; font-size:0.78rem; color:#64748b; text-align:center;">
              Tidak ada hasil yang cocok dengan "<strong>${query}</strong>" di semua kurun waktu.
            </div>
          `;
          searchDropdown.style.display = 'block';
          return;
        }

        let html = '';

        // Kingdoms section
        if (matchKingdoms.length > 0) {
          html += `<div class="search-group-header">👑 Kerajaan & Kesultanan (${matchKingdoms.length})</div>`;
          matchKingdoms.forEach(k => {
            const kYear = (k.golden_age && k.golden_age.start_year) ? k.golden_age.start_year : (k.year_founded || 1600);
            html += `
              <div class="search-result-item" data-action="kingdom" data-id="${k.id}" data-year="${kYear}">
                <div style="font-weight:700; color:#0f4c3a; font-size:0.83rem;">${k.name}</div>
                <div style="font-size:0.72rem; color:#64748b;">${k.region} &bull; ${k.year_founded_display || ''} &ndash; ${k.year_ended_display || ''}</div>
              </div>
            `;
          });
        }

        // Sultans section
        if (matchSultans.length > 0) {
          html += `<div class="search-group-header">👑 Penguasa & Tokoh Sultan (${matchSultans.length})</div>`;
          matchSultans.forEach(s => {
            const k = kingdoms.find(item => item.id === s.kingdom_id);
            const kName = k ? k.name : '';
            const sYear = s.reign_start || (k ? (k.golden_age ? k.golden_age.start_year : k.year_founded) : 1600);
            html += `
              <div class="search-result-item" data-action="sultan" data-id="${s.id}" data-kingdom="${s.kingdom_id}" data-year="${sYear}">
                <div style="font-weight:700; color:#b45309; font-size:0.83rem;">${s.name}</div>
                <div style="font-size:0.72rem; color:#64748b;">${kName} &bull; Masa Bertahta: ${s.reign_display || ''}</div>
              </div>
            `;
          });
        }

        // Sites section
        if (matchSites.length > 0) {
          html += `<div class="search-group-header">🏛️ Situs Cagar Budaya (${matchSites.length})</div>`;
          matchSites.forEach(st => {
            let catIcon = '🏛️';
            if (st.site_type === 'mosque') catIcon = '🕌';
            if (st.site_type === 'palace') catIcon = '👑';
            if (st.site_type === 'fortress') catIcon = '🛡️';
            if (st.site_type === 'port') catIcon = '⚓';
            html += `
              <div class="search-result-item" data-action="site" data-id="${st.site_id}" data-year="${st.construction_year || 1600}">
                <div style="font-weight:700; color:#0369a1; font-size:0.83rem;">${catIcon} ${st.site_name}</div>
                <div style="font-size:0.72rem; color:#64748b;">${st.construction_period_display} &bull; ${st.heritage_status || 'Cagar Budaya'}</div>
              </div>
            `;
          });
        }

        // Events section
        if (matchEvents.length > 0) {
          html += `<div class="search-group-header">📜 Peristiwa Sejarah (${matchEvents.length})</div>`;
          matchEvents.forEach(e => {
            html += `
              <div class="search-result-item" data-action="event" data-id="${e.event_id}" data-year="${e.event_year}">
                <div style="font-weight:700; color:#475569; font-size:0.83rem;">${e.event_name}</div>
                <div style="font-size:0.72rem; color:#64748b;">${e.event_date_display || e.event_year + ' M'} &bull; ${e.description.slice(0, 60)}...</div>
              </div>
            `;
          });
        }

        searchDropdown.innerHTML = html;
        searchDropdown.style.display = 'block';

        // Add item click handlers
        searchDropdown.querySelectorAll('.search-result-item').forEach(item => {
          item.addEventListener('click', () => {
            const action = item.getAttribute('data-action');
            const targetId = item.getAttribute('data-id');
            const targetYear = parseInt(item.getAttribute('data-year'), 10);

            // Auto-pause timeline so playback does not disrupt inspection
            if (window.TimelineController && window.TimelineController.pause) {
              window.TimelineController.pause();
            }

            // Always adjust timeline to destination's year!
            if (!isNaN(targetYear) && window.TimelineController) {
              window.TimelineController.setYear(targetYear);
            }

            // Reset region filter to 'Semua' so destination from any archipelago is visible
            if (window.FilterManager) {
              window.FilterManager.setRegion('Semua', false);
            }

            // Close search dropdown and clear input
            searchDropdown.style.display = 'none';
            searchInput.value = '';
            searchInput.blur();
            if (searchCenterControls) {
              searchCenterControls.classList.remove('mobile-open');
            }

            if (action === 'kingdom') {
              DetailDrawer.openKingdom(targetId);
            } else if (action === 'sultan') {
              const kingdomId = item.getAttribute('data-kingdom');
              DetailDrawer.openKingdom(kingdomId);
              setTimeout(() => {
                const select = document.getElementById('sultan-select-dropdown');
                if (select) {
                  select.value = targetId;
                  DetailDrawer.onSultanSelected(targetId);
                }
              }, 200);
            } else if (action === 'site') {
              DetailDrawer.openSite(targetId);
            } else if (action === 'event') {
              renderEventsModal();
              const eventsModal = document.getElementById('modal-events');
              if (eventsModal) eventsModal.classList.add('open');
            }
          });
        });
      };

      searchInput.addEventListener('input', (e) => {
        performLiveSearch(e.target.value);
      });

      searchInput.addEventListener('focus', (e) => {
        if (e.target.value.trim().length >= 2) {
          performLiveSearch(e.target.value);
        }
      });

      document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
          searchDropdown.style.display = 'none';
        }
      });
    }

    // 7. Mobile Timeline Collapse/Expand Toggle
    const timelineCollapseBtn = document.getElementById('btn-toggle-timeline-collapse');
    const timelineContainer = document.querySelector('.timeline-bar-container');
    if (timelineCollapseBtn && timelineContainer) {
      timelineCollapseBtn.addEventListener('click', () => {
        timelineContainer.classList.toggle('collapsed');
        timelineCollapseBtn.classList.toggle('is-collapsed', timelineContainer.classList.contains('collapsed'));
      });
    }

    // 8. Backdrop click close for modals
    document.querySelectorAll('.modal-overlay').forEach(overlay => {
      overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
          overlay.classList.remove('open');
        }
      });
    });

    // 9. Century jump clicks & proportional ruler tick clicks
    document.querySelectorAll('.century-btn, .ruler-tick').forEach(btn => {
      btn.addEventListener('click', () => {
        const yr = parseInt(btn.getAttribute('data-year'), 10);
        if (!isNaN(yr)) {
          TimelineController.setYear(yr);
        }
      });
    });
  }

  function renderEventsModal() {
    const container = document.getElementById('events-timeline-container');
    if (!container || !events) return;

    // Sort events chronologically
    const sortedEvents = [...events].sort((a, b) => a.event_year - b.event_year);

    container.innerHTML = sortedEvents.map(evt => {
      const isNkri = evt.event_type === 'nkri_integration';
      let typeLabel = "Perkembangan Sejarah";
      if (evt.event_type === 'early_evidence') typeLabel = "Bukti Awal Masuknya Islam";
      if (evt.event_type === 'kingdom_emergence') typeLabel = "Kemunculan Kesultanan";
      if (evt.event_type === 'golden_age') typeLabel = "Era Puncak Kejayaan";
      if (evt.event_type === 'conflict_colonialism') typeLabel = "Perang & Penetrasi Kolonial";
      if (evt.event_type === 'treaty_partition') typeLabel = "Perjanjian & Partisi Wilayah";
      if (evt.event_type === 'nkri_integration') typeLabel = "🇮🇩 Kemerdekaan RI & Integrasi NKRI";

      // Kingdom buttons
      let kingdomButtons = '';
      if (evt.related_kingdom_ids && evt.related_kingdom_ids.length > 0) {
        const kPills = evt.related_kingdom_ids.map(kid => {
          const k = kingdoms.find(item => item.id === kid);
          if (!k) return '';
          return `
            <button class="filter-badge" style="font-size:10px; padding:2px 7px; background:#0f4c3a; color:#fff;" onclick="window.DetailDrawer.openKingdom('${kid}'); document.getElementById('modal-events').classList.remove('open');">
              👑 ${k.name}
            </button>
          `;
        }).join('');
        kingdomButtons = `<div style="display:flex; flex-wrap:wrap; gap:4px; margin-top:6px;">${kPills}</div>`;
      }

      return `
        <div class="event-item-card ${isNkri ? 'event-nkri' : ''}">
          <div class="event-header-row">
            <span class="event-year-badge">${evt.event_date_display || evt.event_year + ' M'}</span>
            <span class="event-type-label">${typeLabel}</span>
          </div>
          <div class="event-title">${evt.event_name}</div>
          <div class="event-desc">${evt.description}</div>
          ${kingdomButtons}
          ${evt.uncertainty_notes ? `
            <div style="font-size:0.72rem; color:#64748b; margin-top:4px; font-style:italic;">
              ${evt.uncertainty_notes}
            </div>
          ` : ''}
        </div>
      `;
    }).join('');
  }

  function renderSourcesModal() {
    const listContainer = document.getElementById('sources-list-container');
    if (!listContainer) return;

    listContainer.innerHTML = sources.map((src, index) => {
      const typeBadge = `<span style="background:#e2e8f0; color:#334155; font-size:10px; font-weight:700; padding:2px 8px; border-radius:99px; margin-left:8px;">${src.type}</span>`;
      const urlLink = src.url 
        ? `<div style="margin-top:4px;"><a href="${src.url}" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary); font-size:11px; text-decoration:underline;">Tautan Referensi / Katalog Perpusnas &rarr;</a></div>`
        : '';

      return `
        <div class="source-item-card">
          <div class="source-item-title">${index + 1}. ${src.title} ${typeBadge}</div>
          <div class="source-item-author">Penulis/Penyusun: <strong>${src.authors}</strong> &bull; Penerbit: ${src.publisher} (${src.year})</div>
          <div class="source-item-claims">
            <strong>Klaim Historis yang Didukung:</strong> ${src.claims_supported}
          </div>
          ${urlLink}
        </div>
      `;
    }).join('');
  }

  function showLoading(show) {
    const loader = document.getElementById('app-loading-screen');
    if (loader) {
      loader.style.display = show ? 'flex' : 'none';
    }
  }

  function showErrorState(message) {
    const loader = document.getElementById('app-loading-screen');
    if (loader) {
      loader.innerHTML = `
        <div style="background:#fff; padding:24px 32px; border-radius:12px; border:2px solid #ef4444; text-align:center; max-width:420px;">
          <h3 style="color:#b91c1c; margin-bottom:8px;">Kesalahan Pemuatan Data</h3>
          <p style="font-size:13px; color:#475569; margin-bottom:16px;">${message}</p>
          <button onclick="location.reload()" style="background:#0f4c3a; color:#fff; border:none; padding:8px 16px; border-radius:6px; cursor:pointer;">Muat Ulang Halaman</button>
        </div>
      `;
    }
  }

  return {
    init,
    getKingdoms: () => kingdoms,
    getSultans: () => sultans,
    getSources: () => sources,
    getTerritories: () => territoriesGeoJSON,
    getSites: () => sites,
    getEvents: () => events
  };
})();

// Start App when DOM ready
document.addEventListener('DOMContentLoaded', () => {
  App.init();
});
