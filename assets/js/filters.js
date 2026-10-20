/**
 * WebGIS Islamic Kingdoms Nusantara - Search & Geographic Filter Management
 */

window.FilterManager = (function() {
  let state = {
    region: 'Semua',
    search: '',
    onlyGoldenAge: false,
    showAllHistorical: false,
    siteCategory: 'all'
  };

  let onChangeCallback = null;

  function initFilters(onChange) {
    onChangeCallback = onChange;

    // Region Badges Listeners
    document.querySelectorAll('.filter-badge[data-region]').forEach(badge => {
      badge.addEventListener('click', () => {
        const region = badge.getAttribute('data-region');
        setRegion(region);
      });
    });

    // Site Category Chips
    document.querySelectorAll('.site-cat-chip[data-site-cat]').forEach(chip => {
      chip.addEventListener('click', () => {
        document.querySelectorAll('.site-cat-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        state.siteCategory = chip.getAttribute('data-site-cat');
        if (window.HistoryMap) {
          window.HistoryMap.setSiteCategoryFilter(state.siteCategory);
        }
        triggerChange();
      });
    });

    // Golden Age Toggle Button
    const goldenAgeBtn = document.getElementById('btn-filter-golden-age');
    if (goldenAgeBtn) {
      goldenAgeBtn.addEventListener('click', () => {
        toggleGoldenAge();
      });
    }

    // Show All Historical Points Toggle
    const showAllBtn = document.getElementById('btn-toggle-show-all');
    if (showAllBtn) {
      showAllBtn.addEventListener('click', () => {
        toggleHistoricalMode();
      });
    }
  }

  function setRegion(region, shouldZoom = true) {
    document.querySelectorAll('.filter-badge[data-region]').forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-region') === region);
    });
    state.region = region;
    triggerChange();

    // Smoothly fly & zoom the map to the selected geographic region
    if (shouldZoom && window.HistoryMap && typeof window.HistoryMap.zoomToRegion === 'function') {
      window.HistoryMap.zoomToRegion(region);
    }
  }

  function toggleGoldenAge() {
    state.onlyGoldenAge = !state.onlyGoldenAge;
    const goldenAgeBtn = document.getElementById('btn-filter-golden-age');
    if (goldenAgeBtn) {
      goldenAgeBtn.classList.toggle('active', state.onlyGoldenAge);
      if (state.onlyGoldenAge) {
        goldenAgeBtn.style.background = '#fef3c7';
        goldenAgeBtn.style.color = '#92400e';
        goldenAgeBtn.style.borderColor = '#f59e0b';
      } else {
        goldenAgeBtn.style.background = '';
        goldenAgeBtn.style.color = '';
        goldenAgeBtn.style.borderColor = '';
      }
    }
    triggerChange();
  }

  function toggleHistoricalMode() {
    state.showAllHistorical = !state.showAllHistorical;
    const showAllBtn = document.getElementById('btn-toggle-show-all');
    if (showAllBtn) {
      showAllBtn.classList.toggle('active', state.showAllHistorical);
      const label = document.getElementById('show-all-label');
      if (label) {
        label.innerText = state.showAllHistorical ? "Mode: Semua Titik Terpetakan" : "Mode: Kronologis Aktif";
      }
    }
    triggerChange();
  }

  function triggerChange() {
    if (onChangeCallback) {
      onChangeCallback(state);
    }
  }

  function getFilterState() {
    return { ...state };
  }

  return {
    initFilters,
    getFilterState,
    setRegion,
    toggleGoldenAge,
    toggleHistoricalMode
  };
})();
