/**
 * WebGIS Islamic Kingdoms Nusantara - Master Application Orchestrator
 * Upgraded with Historical Territories GeoJSON & Responsive Mobile Interaction
 */

window.App = (function() {
  let kingdoms = [];
  let sultans = [];
  let sources = [];
  let territoriesGeoJSON = null;

  async function init() {
    try {
      showLoading(true);

      // Fetch all four database files in parallel
      const [kRes, sRes, srcRes, tRes] = await Promise.all([
        fetch('data/kingdoms.json'),
        fetch('data/sultans.json'),
        fetch('data/sources.json'),
        fetch('data/historical-territories.geojson')
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

      console.log(`[App] Berhasil memuat ${kingdoms.length} kerajaan, ${sultans.length} sultan, ${sources.length} sumber akademik, dan ${territoriesGeoJSON ? territoriesGeoJSON.features.length : 0} poligon historis.`);

      // 1. Initialize Map
      HistoryMap.initMap('map-container');
      if (territoriesGeoJSON) {
        HistoryMap.setTerritoriesData(territoriesGeoJSON);
      }

      // 2. Initialize Detail Drawer
      DetailDrawer.initDetailDrawer(kingdoms, sultans, sources, territoriesGeoJSON);

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

    if (activeStatEl) activeStatEl.innerText = stats.activeCount;
    if (goldenStatEl) goldenStatEl.innerText = stats.goldenAgeCount;
    if (totalStatEl) totalStatEl.innerText = stats.totalRendered;
    if (territoryStatEl) territoryStatEl.innerText = stats.territoriesRendered;
  }

  function setupUIInteractions() {
    // 1. Historical Territories Toggle Button
    const territoriesBtn = document.getElementById('btn-toggle-territories');
    if (territoriesBtn) {
      territoriesBtn.addEventListener('click', () => {
        const isVisible = HistoryMap.toggleTerritories();
        territoriesBtn.classList.toggle('active', isVisible);
        const label = document.getElementById('territories-btn-label');
        if (label) {
          label.innerText = isVisible ? "Wilayah: Aktif" : "Wilayah: Mati";
        }
        onFilterOrYearChanged();
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

    // 3. Reset View Button
    const resetViewBtn = document.getElementById('btn-reset-map-view');
    if (resetViewBtn) {
      resetViewBtn.addEventListener('click', () => {
        HistoryMap.resetView();
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

    // 9. Century jump clicks
    document.querySelectorAll('.century-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const yr = parseInt(btn.getAttribute('data-year'), 10);
        TimelineController.setYear(yr);
      });
    });
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
    getTerritories: () => territoriesGeoJSON
  };
})();

// Start App when DOM ready
document.addEventListener('DOMContentLoaded', () => {
  App.init();
});
