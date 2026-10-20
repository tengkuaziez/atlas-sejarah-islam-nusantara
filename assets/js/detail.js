/**
 * WebGIS Islamic Kingdoms Nusantara - Kingdom Detail Drawer & Sultan Viewer
 * Upgraded with Historical Territory Metadata & Mobile Bottom Sheet UX
 */

window.DetailDrawer = (function() {
  let drawerEl = null;
  let currentKingdom = null;
  let currentSite = null;
  let kingdomsMap = {};
  let sultansMap = {}; // kingdom_id -> [sultans]
  let sourcesMap = {}; // source_id -> source
  let territoriesList = []; // Array of territory features
  let sitesList = []; // Array of historical sites
  let sitesMap = {}; // site_id -> site
  let eventsList = []; // Array of historical events

  function initDetailDrawer(kingdoms, sultans, sources, territoriesGeoJSON, sites, events) {
    drawerEl = document.getElementById('kingdom-detail-drawer');
    
    kingdoms.forEach(k => { kingdomsMap[k.id] = k; });
    sources.forEach(s => { sourcesMap[s.id] = s; });

    sultans.forEach(s => {
      if (!sultansMap[s.kingdom_id]) {
        sultansMap[s.kingdom_id] = [];
      }
      sultansMap[s.kingdom_id].push(s);
    });

    if (territoriesGeoJSON && territoriesGeoJSON.features) {
      territoriesList = territoriesGeoJSON.features;
    }

    if (sites && Array.isArray(sites)) {
      sitesList = sites;
      sites.forEach(st => { sitesMap[st.site_id] = st; });
    }

    if (events && Array.isArray(events)) {
      eventsList = events;
    }

    // Close button listener
    const closeBtn = document.getElementById('btn-close-drawer');
    if (closeBtn) {
      closeBtn.addEventListener('click', closeDrawer);
    }

    // Drag handle listener for mobile bottom sheet
    const dragHandle = document.getElementById('drawer-drag-handle');
    if (dragHandle) {
      dragHandle.addEventListener('click', closeDrawer);
    }
  }

  function openKingdom(kingdomId) {
    const kingdom = kingdomsMap[kingdomId];
    if (!kingdom || !drawerEl) return;

    currentKingdom = kingdom;
    currentSite = null;
    renderDrawerContent(kingdom);
    drawerEl.classList.add('open');

    // Also focus map to kingdom
    if (window.HistoryMap) {
      window.HistoryMap.focusKingdom(kingdomId, Object.values(kingdomsMap));
    }
  }

  function openSite(siteId) {
    const site = sitesMap[siteId];
    if (!site || !drawerEl) return;

    currentSite = site;
    currentKingdom = null;
    renderSiteDrawerContent(site);
    drawerEl.classList.add('open');

    // Focus map to site
    if (window.HistoryMap) {
      window.HistoryMap.focusSite(siteId);
    }
  }

  function closeDrawer() {
    if (drawerEl) {
      drawerEl.classList.remove('open');
    }
  }

  function renderDrawerContent(kingdom) {
    const container = document.getElementById('drawer-dynamic-content');
    if (!container) return;

    const sultans = sultansMap[kingdom.id] || [];
    const currentYear = window.TimelineController ? window.TimelineController.getCurrentYear() : 1625;

    // Check historical territory polygons available for this kingdom
    const relatedTerritories = territoriesList.filter(t => t.properties.kingdom_id === kingdom.id);

    // Territory Information Section
    let territoryCardHtml = '';
    if (relatedTerritories.length > 0) {
      const territoryPills = relatedTerritories.map(t => {
        const p = t.properties;
        let badgeColor = '#059669';
        if (p.territory_type === 'controlled') badgeColor = '#d97706';
        if (p.territory_type === 'influence') badgeColor = '#6366f1';
        return `
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:3px solid ${badgeColor}; padding:8px 12px; border-radius:6px; margin-bottom:8px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <strong style="font-size:0.8rem; color:#1e293b;">${p.historical_period}</strong>
              <span style="font-size:0.7rem; font-weight:700; color:${badgeColor}; text-transform:uppercase;">${p.territory_type}</span>
            </div>
            <div style="font-size:0.75rem; color:#475569; margin-bottom:4px;">
              <strong>Sumber:</strong> ${p.source_title} (${p.map_publication_year}) &bull; ${p.source_publisher}
            </div>
            <div style="font-size:0.73rem; color:#64748b; line-height:1.35;">
              ${p.uncertainty_notes}
            </div>
          </div>
        `;
      }).join('');

      territoryCardHtml = `
        <div class="detail-card">
          <div class="detail-card-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 3l-.16.03L15 5.1 9 3 3.36 4.9c-.21.07-.36.25-.36.48V20.5c0 .28.22.5.5.5l.16-.03L9 18.9l6 2.1 5.64-1.9c.21-.07.36-.25.36-.48V3.5c0-.28-.22-.5-.5-.5zM15 19l-6-2.11V5l6 2.11V19z"/></svg>
            REKONSTRUKSI POLIGON WILAYAH HISTORIS (${relatedTerritories.length} Lapisan Peta)
          </div>
          <p style="font-size:0.78rem; color:#334155; margin-bottom:10px; line-height:1.4;">
            Wilayah kerajaan ini telah berhasil digeoreferensi dan didigitasi dari atlas sejarah otoritatif (Robert Cribb 2000, Anthony Reid, Claude Guillot). Poligon otomatis berubah mengikuti linimasa.
          </p>
          ${territoryPills}
        </div>
      `;
    } else {
      territoryCardHtml = `
        <div class="detail-card" style="background:#fafaf9; border-style:dashed;">
          <div class="detail-card-title" style="color:#64748b;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>
            STATUS PEMETAAN WILAYAH HISTORIS
          </div>
          <p style="font-size:0.76rem; color:#57534e; line-height:1.45; margin:0;">
            Poligon spasial wilayah belum tersedia berdasarkan peta historis terverifikasi. Sesuai kaidah historiografi kemaritiman Nusantara (teori <em>Mandala</em>) dan prinsip integritas kartografi, batas wilayah administratif tidak dispekulasikan secara artifisial. Pusat kekuasaan dipetakan secara presisi melalui titik koordinat istana/keraton.
          </p>
        </div>
      `;
    }

    // Golden Age Section
    let goldenAgeHtml = '';
    if (kingdom.golden_age) {
      goldenAgeHtml = `
        <div class="golden-age-banner">
          <div class="golden-age-badge">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.4 7.2h7.6l-6.1 4.5 2.3 7.3-6.2-4.6-6.2 4.6 2.3-7.3-6.1-4.5h7.6z"/></svg>
            ERA KEEMASAN: ${kingdom.golden_age.start_year} &ndash; ${kingdom.golden_age.end_year} M
          </div>
          <div class="golden-age-leader">Penguasa Puncak: ${kingdom.golden_age.leader}</div>
          <div class="golden-age-desc">${kingdom.golden_age.description}</div>
        </div>
      `;
    }

    // Sultans Dropdown & Display Box
    let sultanSectionHtml = '';
    if (sultans.length > 0) {
      let sultanOptions = sultans.map((s, idx) => {
        let isReigningNow = (s.reign_start && s.reign_end && currentYear >= s.reign_start && currentYear <= s.reign_end)
          ? ' [Sedang Memerintah pada Tahun Ini]'
          : '';
        return `<option value="${s.id}">${s.order ? s.order + '. ' : ''}${s.name} (${s.reign_display})${isReigningNow}</option>`;
      }).join('');

      sultanSectionHtml = `
        <div class="detail-card">
          <div class="detail-card-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M5 16L3 5l5.5 5L12 4l3.5 6L21 5l-2 11H5zm14 3c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-1h14v1z"/></svg>
            DAFTAR SULTAN & PENGUASA HISTORIS (${sultans.length} Tercatat)
          </div>
          <div class="sultan-selector-wrapper">
            <select id="sultan-select-dropdown" class="sultan-select" onchange="window.DetailDrawer.onSultanSelected(this.value)">
              ${sultanOptions}
            </select>
          </div>
          <div id="sultan-detail-display-box" class="sultan-display-box">
            <!-- Rendered via onSultanSelected -->
          </div>
        </div>
      `;
    } else {
      sultanSectionHtml = `
        <div class="detail-card">
          <div class="detail-card-title">DAFTAR SULTAN & PENGUASA</div>
          <p style="font-size:0.8rem; color:#64748b;">Silsilah lengkap penguasa sedang dalam proses verifikasi filologis naskah lokal.</p>
        </div>
      `;
    }

    // Key Events Timeline
    let eventsHtml = '';
    if (kingdom.key_events && kingdom.key_events.length > 0) {
      const eventItems = kingdom.key_events.map(ev => `
        <div class="timeline-event-item">
          <div class="timeline-event-year">${ev.year} M</div>
          <div class="timeline-event-text">${ev.event}</div>
        </div>
      `).join('');

      eventsHtml = `
        <div class="detail-card">
          <div class="detail-card-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11z"/></svg>
            PERISTIWA PENTING & KRONOLOGI HISTORIS
          </div>
          <div class="events-timeline">
            ${eventItems}
          </div>
        </div>
      `;
    }

    // Relics & Heritage
    let relicsHtml = '';
    if (kingdom.relics_and_heritage && kingdom.relics_and_heritage.length > 0) {
      const relicTags = kingdom.relics_and_heritage.map(r => `
        <div class="relic-tag">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="var(--color-gold)"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          ${r}
        </div>
      `).join('');

      relicsHtml = `
        <div class="detail-card">
          <div class="detail-card-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3L2 12h3v8h14v-8h3L12 3zm0 4.5c1.38 0 2.5 1.12 2.5 2.5S13.38 12.5 12 12.5 9.5 11.38 9.5 10 10.62 7.5 12 7.5z"/></svg>
            PENINGGALAN ARKEOLOGIS & CAGAR BUDAYA
          </div>
          <div class="relics-tag-grid">
            ${relicTags}
          </div>
        </div>
      `;
    }

    // Historiographical Certainty Box
    const certaintyBadge = kingdom.data_certainty_level === 'Tinggi'
      ? `<span style="background:#bbf7d0; color:#166534; padding:2px 8px; border-radius:99px;">Tingkat Kepastian: Tinggi</span>`
      : `<span style="background:#fef08a; color:#854d0e; padding:2px 8px; border-radius:99px;">Tingkat Kepastian: Sedang / Interpretatif</span>`;

    const certaintyHtml = `
      <div class="detail-card">
        <div class="detail-card-title">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
          HISTORIOGRAFI & STATUS VERIFIKASI
        </div>
        <div class="certainty-box ${kingdom.data_certainty_level === 'Sedang' ? 'medium' : ''}">
          <div class="certainty-header">
            <span>Status: ${kingdom.verification_status}</span>
            ${certaintyBadge}
          </div>
          <div class="certainty-desc">${kingdom.certainty_notes}</div>
        </div>
      </div>
    `;

    // NKRI Integration Section
    let nkriIntegrationHtml = '';
    if (kingdom.nkri_integration) {
      const nkri = kingdom.nkri_integration;
      nkriIntegrationHtml = `
        <div class="nkri-integration-card">
          <div class="nkri-card-header">
            <span class="nkri-flag-icon">🇮🇩</span>
            <span class="nkri-badge">${nkri.integrated_into_nkri ? 'INTEGRASI NKRI' : 'HISTORIOGRAFI KEDAULATAN'}</span>
            <span style="font-size:0.72rem; color:#b91c1c; font-weight:700; margin-left:auto;">${nkri.integration_date_display || ''}</span>
          </div>
          <div style="font-size:0.84rem; font-weight:700; color:#1e293b; margin-bottom:4px;">
            ${nkri.title_document || 'Kedudukan Teritorial & Cagar Budaya'}
          </div>
          <div style="font-size:0.78rem; color:#475569; margin-bottom:6px; line-height:1.45;">
            ${nkri.summary}
          </div>
          ${nkri.historical_figure ? `
            <div style="font-size:0.75rem; color:#0f4c3a; font-weight:600; margin-bottom:4px;">
              <strong>Tokoh Kunci:</strong> ${nkri.historical_figure}
            </div>
          ` : ''}
          <div style="font-size:0.73rem; background:#ffffff; border:1px solid #fecaca; padding:4px 8px; border-radius:4px; color:#991b1b; font-weight:600;">
            Status Kontemporer: ${nkri.current_status}
          </div>
        </div>
      `;
    }

    // Associated Historical Sites Section
    let associatedSitesHtml = '';
    const relatedSites = sitesList.filter(s => s.associated_kingdom_ids && s.associated_kingdom_ids.includes(kingdom.id));
    if (relatedSites.length > 0) {
      const siteRows = relatedSites.map(s => {
        let icon = '🏛️';
        if (s.site_type === 'mosque') icon = '🕌';
        if (s.site_type === 'palace') icon = '👑';
        if (s.site_type === 'fortress') icon = '🛡️';
        if (s.site_type === 'port') icon = '⚓';
        return `
          <div style="display:flex; justify-content:space-between; align-items:center; background:#f8fafc; border:1px solid #e2e8f0; padding:8px 12px; border-radius:6px; margin-bottom:6px;">
            <div>
              <span style="font-size:1rem; margin-right:6px;">${icon}</span>
              <strong style="font-size:0.8rem; color:#0f4c3a;">${s.site_name}</strong>
              <div style="font-size:0.72rem; color:#64748b;">${s.construction_period_display}</div>
            </div>
            <button class="btn-ctrl" style="width:28px; height:28px; font-size:11px;" onclick="window.DetailDrawer.openSite('${s.site_id}')" title="Buka Detail Situs">
              &rarr;
            </button>
          </div>
        `;
      }).join('');

      associatedSitesHtml = `
        <div class="detail-card">
          <div class="detail-card-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3L2 12h3v8h6v-6h2v6h6v-8h3L12 3z"/></svg>
            SITUS & TINGGALAN CAGAR BUDAYA TERKAIT (${relatedSites.length})
          </div>
          ${siteRows}
        </div>
      `;
    }

    // Reference Sources
    let sourcesListHtml = '';
    if (kingdom.sources_ids && kingdom.sources_ids.length > 0) {
      const srcItems = kingdom.sources_ids.map(sid => {
        const src = sourcesMap[sid];
        if (!src) return '';
        return `
          <li style="margin-bottom:6px; font-size:0.77rem; color:#475569;">
            <strong>${src.authors} (${src.year})</strong>. <em>${src.title}</em>. ${src.publisher}.
          </li>
        `;
      }).join('');

      sourcesListHtml = `
        <div class="detail-card">
          <div class="detail-card-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"/></svg>
            REFERENSI SUMBER AKADEMIK
          </div>
          <ul style="padding-left:18px;">
            ${sourcesListHtml}
          </ul>
        </div>
      `;
    }

    // Assemble Drawer DOM
    document.getElementById('drawer-kingdom-name').innerText = kingdom.name;
    document.getElementById('drawer-kingdom-alts').innerText = kingdom.alternate_names 
      ? `Variasi Nama: ${kingdom.alternate_names.join(', ')}` 
      : '';

    container.innerHTML = `
      <div class="detail-card" style="border-left: 4px solid var(--color-primary);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
          <span style="font-size:0.75rem; text-transform:uppercase; color:var(--color-primary); font-weight:700;">${kingdom.region}</span>
          <span style="font-size:0.75rem; color:#64748b; font-weight:600;">GPS: ${kingdom.coordinates.lat.toFixed(4)}, ${kingdom.coordinates.lng.toFixed(4)}</span>
        </div>
        <div style="font-size:0.83rem; line-height:1.45; color:#334155; margin-bottom:10px;">
          <strong>Pusat Pemerintahan:</strong> ${kingdom.capital_city}<br>
          <strong>Periode Eksistensi:</strong> ${kingdom.year_founded_display} &ndash; ${kingdom.year_ended_display}<br>
          <strong>Pendiri Utama:</strong> ${kingdom.founder}
        </div>
        <p style="font-size:0.82rem; line-height:1.55; color:#1e293b;">
          ${kingdom.historical_summary}
        </p>
      </div>

      ${goldenAgeHtml}
      ${nkriIntegrationHtml}
      ${territoryCardHtml}
      ${sultanSectionHtml}
      ${associatedSitesHtml}
      ${eventsHtml}
      ${relicsHtml}
      ${certaintyHtml}
      ${sourcesListHtml}
    `;

    // Initialize first sultan view
    if (sultans.length > 0) {
      let activeSultan = sultans.find(s => s.reign_start && s.reign_end && currentYear >= s.reign_start && currentYear <= s.reign_end);
      if (!activeSultan) {
        activeSultan = sultans.find(s => s.is_golden_age_ruler) || sultans[0];
      }
      const select = document.getElementById('sultan-select-dropdown');
      if (select) select.value = activeSultan.id;
      renderSultanBox(activeSultan);
    }
  }

  function onSultanSelected(sultanId) {
    if (!currentKingdom) return;
    const sultans = sultansMap[currentKingdom.id] || [];
    const sultan = sultans.find(s => s.id === sultanId);
    if (sultan) {
      renderSultanBox(sultan);
    }
  }

  function renderSultanBox(sultan) {
    const box = document.getElementById('sultan-detail-display-box');
    if (!box) return;

    const goldenBadge = sultan.is_golden_age_ruler 
      ? `<span style="background:#fef3c7; color:#92400e; font-size:10px; font-weight:700; padding:2px 8px; border-radius:99px; margin-left:6px;">⭐ Penguasa Era Keemasan</span>`
      : '';

    const achievements = sultan.key_achievements 
      ? sultan.key_achievements.map(a => `<li>${a}</li>`).join('')
      : '';

    box.innerHTML = `
      <div class="sultan-display-header">
        <div>
          <span class="sultan-display-name">${sultan.name}</span>
          ${goldenBadge}
        </div>
        <span class="sultan-reign-badge">${sultan.reign_display}</span>
      </div>
      <div class="sultan-bio">${sultan.biography}</div>
      ${achievements ? `
        <div style="font-size:0.75rem; font-weight:700; color:var(--color-primary); margin:8px 0 4px;">Pencapaian & Kebijakan Utama:</div>
        <ul class="sultan-achievements-list">
          ${achievements}
        </ul>
      ` : ''}
      ${sultan.reference_notes ? `
        <div style="font-size:0.72rem; color:#64748b; font-style:italic; margin-top:8px; border-top:1px dashed #e2e8f0; padding-top:4px;">
          Catatan Verifikasi: ${sultan.reference_notes}
        </div>
      ` : ''}
    `;
  }

  function renderSiteDrawerContent(site) {
    const container = document.getElementById('drawer-dynamic-content');
    if (!container) return;

    let typeLabel = "Masjid Bersejarah";
    let iconChar = "🕌";
    if (site.site_type === 'palace') { typeLabel = "Keraton / Istana Kesultanan"; iconChar = "👑"; }
    if (site.site_type === 'tomb') { typeLabel = "Makam Sultan & Kompleks Diraja"; iconChar = "🏛️"; }
    if (site.site_type === 'fortress') { typeLabel = "Benteng & Pertahanan Maritim"; iconChar = "🛡️"; }
    if (site.site_type === 'port') { typeLabel = "Bandar Niaga & Pelabuhan Kuno"; iconChar = "⚓"; }

    document.getElementById('drawer-kingdom-name').innerText = site.site_name;
    document.getElementById('drawer-kingdom-alts').innerText = `${iconChar} ${typeLabel} • ${site.construction_period_display}`;

    // Associated Kingdoms Badges
    let relatedKingdomsHtml = '';
    if (site.associated_kingdom_ids && site.associated_kingdom_ids.length > 0) {
      const pills = site.associated_kingdom_ids.map(kid => {
        const k = kingdomsMap[kid];
        if (!k) return '';
        return `
          <button class="filter-badge" style="background:#0f4c3a; color:#fff; border-color:#0b382b; margin:2px;" onclick="window.DetailDrawer.openKingdom('${kid}')">
            👑 ${k.name} &rarr;
          </button>
        `;
      }).join('');
      relatedKingdomsHtml = `
        <div class="detail-card">
          <div class="detail-card-title">KERAJAAN & KESULTANAN TERKAIT</div>
          <div style="display:flex; flex-wrap:wrap; gap:4px; margin-top:6px;">
            ${pills}
          </div>
        </div>
      `;
    }

    // Sources
    let siteSourcesHtml = '';
    if (site.source_references && site.source_references.length > 0) {
      const srcItems = site.source_references.map(sid => {
        const src = sourcesMap[sid];
        if (!src) return '';
        return `
          <li style="margin-bottom:6px; font-size:0.77rem; color:#475569;">
            <strong>${src.authors} (${src.year})</strong>. <em>${src.title}</em>. ${src.publisher}.
          </li>
        `;
      }).join('');
      if (srcItems) {
        siteSourcesHtml = `
          <div class="detail-card">
            <div class="detail-card-title">REFERENSI AKADEMIK & REGISTRASI CAGAR BUDAYA</div>
            <ul style="padding-left:18px;">
              ${srcItems}
            </ul>
          </div>
        `;
      }
    }

    container.innerHTML = `
      <div class="detail-card" style="border-left: 4px solid #0ea5e9;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
          <span style="font-size:0.75rem; text-transform:uppercase; color:#0369a1; font-weight:700;">${typeLabel}</span>
          <span style="font-size:0.75rem; color:#64748b; font-weight:600;">GPS: ${site.latitude.toFixed(4)}, ${site.longitude.toFixed(4)}</span>
        </div>
        <div style="font-size:0.83rem; line-height:1.45; color:#334155; margin-bottom:10px;">
          <strong>Kurun Pembangunan:</strong> ${site.construction_period_display}<br>
          <strong>Status Cagar Budaya:</strong> <span style="color:#0f4c3a; font-weight:600;">${site.heritage_status || 'Cagar Budaya Nasional'}</span>
        </div>
        <p style="font-size:0.82rem; line-height:1.55; color:#1e293b;">
          ${site.historical_significance}
        </p>
      </div>

      <div class="detail-card">
        <div class="detail-card-title">KONDISI KONTEMPORER & ARSITEKTUR FISIK</div>
        <p style="font-size:0.8rem; color:#334155; line-height:1.5; margin:0;">
          ${site.current_condition}
        </p>
      </div>

      ${relatedKingdomsHtml}

      <div class="detail-card" style="background:#fafaf9;">
        <div class="detail-card-title" style="color:#44403c;">HISTORIOGRAFI & TINGKAT KEPASTIAN DATA</div>
        <div style="font-size:0.75rem; color:#78716c; margin-bottom:4px;">
          <strong>Tingkat Kepastian Koordinat & Kronologi:</strong> ${site.confidence_level}
        </div>
        <div style="font-size:0.75rem; color:#78716c; line-height:1.4;">
          ${site.uncertainty_notes}
        </div>
      </div>

      ${siteSourcesHtml}
    `;
  }

  return {
    initDetailDrawer,
    openKingdom,
    openSite,
    closeDrawer,
    onSultanSelected
  };
})();
