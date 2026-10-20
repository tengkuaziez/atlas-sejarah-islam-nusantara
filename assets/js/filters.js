/**
 * WebGIS Islamic Kingdoms Nusantara - Search & Geographic Filter Management
 */

window.FilterManager = (function() {
  let state = {
    region: 'Semua',
    search: '',
    onlyGoldenAge: false,
    showAllHistorical: false
  };

  let onChangeCallback = null;

  function initFilters(onChange) {
    onChangeCallback = onChange;

    // Search Input Listener
    const searchInput = document.getElementById('search-kingdom-input');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        state.search = e.target.value.trim();
        triggerChange();
      });
    }

    // Region Badges Listeners
    document.querySelectorAll('.filter-badge[data-region]').forEach(badge => {
      badge.addEventListener('click', () => {
        document.querySelectorAll('.filter-badge[data-region]').forEach(b => b.classList.remove('active'));
        badge.classList.add('active');
        state.region = badge.getAttribute('data-region');
        triggerChange();
      });
    });

    // Golden Age Toggle Button
    const goldenAgeBtn = document.getElementById('btn-filter-golden-age');
    if (goldenAgeBtn) {
      goldenAgeBtn.addEventListener('click', () => {
        state.onlyGoldenAge = !state.onlyGoldenAge;
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
        triggerChange();
      });
    }

    // Show All Historical Points Toggle
    const showAllBtn = document.getElementById('btn-toggle-show-all');
    if (showAllBtn) {
      showAllBtn.addEventListener('click', () => {
        state.showAllHistorical = !state.showAllHistorical;
        showAllBtn.classList.toggle('active', state.showAllHistorical);
        const label = document.getElementById('show-all-label');
        if (label) {
          label.innerText = state.showAllHistorical ? "Mode: Semua Titik Terpetakan" : "Mode: Kronologis Aktif";
        }
        triggerChange();
      });
    }
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
    getFilterState
  };
})();
