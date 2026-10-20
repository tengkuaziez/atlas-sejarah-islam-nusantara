/**
 * WebGIS Islamic Kingdoms Nusantara - Timeline & Animation Controller
 */

window.TimelineController = (function() {
  let currentYear = 1625;
  const MIN_YEAR = 1082;
  const MAX_YEAR = 1956;
  
  let isPlaying = false;
  let playTimer = null;
  let playbackSpeed = 1; // 1x, 2x, 3x, 4x
  let onYearChangeCallback = null;

  const EPOCH_DESCRIPTIONS = [
    { upTo: 1199, text: "Bukti Epigrafi Islam Tertua: Fatimah binti Maimun Leran (1082 M)" },
    { upTo: 1266, text: "Awal Perkembangan Komunitas Muslim & Pelabuhan Niaga Pesisir" },
    { upTo: 1296, text: "Pendirian Kesultanan Samudera Pasai oleh Sultan Malik as-Saleh (1267 M)" },
    { upTo: 1344, text: "Pencetakan Koin Emas Dirham & Kemakmuran Samudera Pasai" },
    { upTo: 1367, text: "Lawatan Musafir Dunia Ibnu Battuta ke Samudera Pasai (1345 M)" },
    { upTo: 1399, text: "Jejak Komunitas Muslim Troloyo di Majapahit (1368 M)" },
    { upTo: 1474, text: "Jaringan Niaga Bahari Selat Melaka & Rempah Maluku Kie Raha" },
    { upTo: 1499, text: "Pendirian Kesultanan Demak Bintoro & Majelis Walisongo (1475 M)" },
    { upTo: 1525, text: "Perjuangan Bahari Pati Unus Melawan Portugis di Melaka" },
    { upTo: 1550, text: "Berdirinya Kesultanan Banten, Cirebon, & Banjar (1526 M)" },
    { upTo: 1574, text: "Perlawanan Maluku Terhadap Portugis & Sultan Khairun Ternate" },
    { upTo: 1604, text: "Zaman Kejayaan Sultan Baabullah Ternate & Pendirian Mataram Islam" },
    { upTo: 1624, text: "Islamisasi Makassar Gowa-Tallo (1605 M) & Awal Sultan Iskandar Muda" },
    { upTo: 1645, text: "⭐ Puncak Kejayaan Sultan Agung Mataram & Sultan Iskandar Muda Aceh" },
    { upTo: 1666, text: "Bandar Niaga Bebas Somba Opu Makassar & Sultan Ageng Banten" },
    { upTo: 1699, text: "Perjanjian Bongaya (1667 M) & Dinamika Perebutan Takhta Banten" },
    { upTo: 1754, text: "Kebangkitan Dinasti Maritim Siak, Palembang, & Sambas" },
    { upTo: 1779, text: "Perjanjian Giyanti (1755 M) & Berdirinya Yogyakarta & Surakarta" },
    { upTo: 1824, text: "Perjuangan Sultan Nuku Maluku & Traktat London (1824 M)" },
    { upTo: 1837, text: "Perang Jawa Pangeran Diponegoro (1825–1830 M) & Perang Padri" },
    { upTo: 1872, text: "Perang Banjar Pangeran Antasari & Penetrasi Kolonial Belanda" },
    { upTo: 1907, text: "Perang Semesta Aceh Darussalam Melawan Invasi Kolonial Belanda" },
    { upTo: 1944, text: "Pergerakan Kebangkitan Nasional Menuju Kemerdekaan Indonesia" },
    { upTo: 1949, text: "🇮🇩 Proklamasi Kemerdekaan RI 1945 & Amanat 5 September Yogyakarta" },
    { upTo: 1956, text: "🇮🇩 Integrasi Kerajaan Nusantara ke NKRI & Pembebasan Irian Barat" }
  ];

  function getEpochText(year) {
    for (const epoch of EPOCH_DESCRIPTIONS) {
      if (year <= epoch.upTo) {
        return epoch.text;
      }
    }
    return "Era Indonesia Berdaulat (NKRI)";
  }

  function initTimeline(sliderId, yearDisplayId, epochDisplayId, onYearChange) {
    onYearChangeCallback = onYearChange;
    const slider = document.getElementById(sliderId);

    if (slider) {
      slider.min = MIN_YEAR;
      slider.max = MAX_YEAR;
      slider.value = currentYear;

      slider.addEventListener('input', (e) => {
        setYear(parseInt(e.target.value, 10));
      });
      slider.addEventListener('change', (e) => {
        setYear(parseInt(e.target.value, 10));
      });
    }

    updateDisplays(currentYear);
  }

  function updateDisplays(year) {
    const slider = document.getElementById('timeline-slider');
    const yearDisplay = document.getElementById('display-year-number');
    const epochDisplay = document.getElementById('display-epoch-badge');
    const thumbBubble = document.getElementById('slider-thumb-bubble');

    const pct = Math.min(100, Math.max(0, ((year - MIN_YEAR) / (MAX_YEAR - MIN_YEAR)) * 100));

    if (slider) {
      if (parseInt(slider.value, 10) !== year) {
        slider.value = year;
      }
      // Fill slider track up to current thumb position
      slider.style.background = `linear-gradient(to right, #059669 0%, #d4af37 ${pct}%, #e2d9c2 ${pct}%, #dcd4c0 100%)`;
    }

    // Update floating year bubble above the thumb (24px thumb diameter offset)
    if (thumbBubble) {
      thumbBubble.innerText = `${year} M`;
      thumbBubble.style.left = `calc(${pct}% + ${(0.5 - pct / 100) * 24}px)`;
    }

    if (yearDisplay) {
      yearDisplay.innerText = `${year} M`;
    }

    if (epochDisplay) {
      epochDisplay.innerText = getEpochText(year);
      if (year >= 1945) {
        epochDisplay.style.background = '#fee2e2';
        epochDisplay.style.color = '#991b1b';
        epochDisplay.style.borderColor = '#ef4444';
      } else {
        epochDisplay.style.background = '';
        epochDisplay.style.color = '';
        epochDisplay.style.borderColor = '';
      }
    }

    // Highlight closest milestone chip
    let closestBtn = null;
    let closestDist = Infinity;
    document.querySelectorAll('.century-btn').forEach(btn => {
      const targetYear = parseInt(btn.getAttribute('data-year'), 10);
      const dist = Math.abs(targetYear - year);
      if (dist < closestDist) {
        closestDist = dist;
        closestBtn = btn;
      }
      btn.classList.remove('active-century');
    });
    if (closestBtn && closestDist <= 35) {
      closestBtn.classList.add('active-century');
    }

    // Highlight closest proportional ruler tick
    document.querySelectorAll('.ruler-tick').forEach(tick => {
      const tickYear = parseInt(tick.getAttribute('data-year'), 10);
      if (!isNaN(tickYear) && Math.abs(tickYear - year) <= 15) {
        tick.classList.add('active-tick');
      } else {
        tick.classList.remove('active-tick');
      }
    });
  }

  function setYear(year) {
    if (year < MIN_YEAR) year = MIN_YEAR;
    if (year > MAX_YEAR) year = MAX_YEAR;

    currentYear = year;
    updateDisplays(currentYear);

    if (onYearChangeCallback) {
      onYearChangeCallback(currentYear);
    }
  }

  function togglePlay() {
    if (isPlaying) {
      pause();
    } else {
      play();
    }
  }

  function play() {
    if (isPlaying) return;
    isPlaying = true;

    const playBtn = document.getElementById('btn-play-toggle');
    if (playBtn) {
      playBtn.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
          <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
        </svg>
      `;
      playBtn.title = "Pause Linimasa";
    }

    // If reached end, restart
    if (currentYear >= MAX_YEAR) {
      setYear(MIN_YEAR);
    }

    const intervalMs = Math.max(35, Math.round(180 / playbackSpeed));

    playTimer = setInterval(() => {
      if (currentYear >= MAX_YEAR) {
        pause();
      } else {
        setYear(currentYear + 1);
      }
    }, intervalMs);
  }

  function pause() {
    isPlaying = false;
    if (playTimer) {
      clearInterval(playTimer);
      playTimer = null;
    }

    const playBtn = document.getElementById('btn-play-toggle');
    if (playBtn) {
      playBtn.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
          <path d="M8 5v14l11-7z"/>
        </svg>
      `;
      playBtn.title = "Putar Linimasa Otomatis";
    }
  }

  function setSpeed(speedMultiplier) {
    const validSpeed = Math.min(4, Math.max(1, parseInt(speedMultiplier, 10) || 1));
    playbackSpeed = validSpeed;
    
    // Update speed button UI
    const speedBtn = document.getElementById('btn-timeline-speed');
    if (speedBtn) {
      speedBtn.innerText = `${playbackSpeed}x`;
      speedBtn.title = `Kecepatan Putar: ${playbackSpeed}x (Klik untuk ganti 1x–4x)`;
    }

    if (isPlaying) {
      clearInterval(playTimer);
      const intervalMs = Math.max(35, Math.round(180 / playbackSpeed));
      playTimer = setInterval(() => {
        if (currentYear >= MAX_YEAR) {
          pause();
        } else {
          setYear(currentYear + 1);
        }
      }, intervalMs);
    }
  }

  function cycleSpeed() {
    const speeds = [1, 2, 3, 4];
    const currentIndex = speeds.indexOf(playbackSpeed);
    const nextSpeed = speeds[(currentIndex + 1) % speeds.length];
    setSpeed(nextSpeed);
    return nextSpeed;
  }

  function stepYear(step) {
    pause(); // Auto-pause when stepping manually
    setYear(currentYear + step);
  }

  function resetTimeline() {
    pause();
    setYear(1625); // Default golden epoch
  }

  function getCurrentYear() {
    return currentYear;
  }

  function getSpeed() {
    return playbackSpeed;
  }

  return {
    initTimeline,
    setYear,
    togglePlay,
    play,
    pause,
    setSpeed,
    cycleSpeed,
    getSpeed,
    stepYear,
    resetTimeline,
    getCurrentYear
  };
})();
