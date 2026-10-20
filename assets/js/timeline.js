/**
 * WebGIS Islamic Kingdoms Nusantara - Timeline & Animation Controller
 */

window.TimelineController = (function() {
  let currentYear = 1625;
  const MIN_YEAR = 1082;
  const MAX_YEAR = 1956;
  
  let isPlaying = false;
  let playTimer = null;
  let playbackSpeed = 1; // 1x, 2x, 5x
  let onYearChangeCallback = null;

  const EPOCH_DESCRIPTIONS = [
    { upTo: 1199, text: "Bukti Epigrafi Tertua Islam di Jawa (Leran 1082 M)" },
    { upTo: 1290, text: "Era Awal Masuknya Islam & Kesultanan Samudera Pasai" },
    { upTo: 1390, text: "Kemakmuran Pasai, Nisan Troloyo, & Lawatan Ibnu Battuta" },
    { upTo: 1470, text: "Jaringan Niaga Maritim Melaka & Rempah Maluku Kie Raha" },
    { upTo: 1525, text: "Kebangkitan Kesultanan Demak & Syiar Walisongo di Jawa" },
    { upTo: 1575, text: "Ekspansi Aceh Darussalam & Kejayaan Sultan Baabullah di Ternate" },
    { upTo: 1640, text: "Zaman Keemasan Sultan Iskandar Muda, Sultan Agung, & Banten" },
    { upTo: 1675, text: "Perang Makassar (Sultan Hasanuddin) & Sultan Ageng Tirtayasa" },
    { upTo: 1755, text: "Dinamika Monarki Maritim & Perjanjian Giyanti di Jawa" },
    { upTo: 1805, text: "Perjuangan Sultan Nuku Maluku & Perlawanan Bahari Siak" },
    { upTo: 1840, text: "Perang Padri, Perang Diponegoro, & Perang Palembang" },
    { upTo: 1944, text: "Perang Aceh, Perang Banjar, & Kebangkitan Nasional Menuju Republik" },
    { upTo: 1956, text: "🇮🇩 Kemerdekaan RI 1945 & Integrasi Kerajaan Nusantara ke NKRI" }
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
    const yearDisplay = document.getElementById(yearDisplayId);
    const epochDisplay = document.getElementById(epochDisplayId);

    if (slider) {
      slider.min = MIN_YEAR;
      slider.max = MAX_YEAR;
      slider.value = currentYear;

      slider.addEventListener('input', (e) => {
        setYear(parseInt(e.target.value, 10));
      });
    }

    updateDisplays(currentYear);
  }

  function updateDisplays(year) {
    const slider = document.getElementById('timeline-slider');
    const yearDisplay = document.getElementById('display-year-number');
    const epochDisplay = document.getElementById('display-epoch-badge');

    if (slider && parseInt(slider.value, 10) !== year) {
      slider.value = year;
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

    // Highlight active century button
    document.querySelectorAll('.century-btn').forEach(btn => {
      const targetYear = parseInt(btn.getAttribute('data-year'), 10);
      if (Math.abs(targetYear - year) <= 25) {
        btn.classList.add('active-century');
      } else {
        btn.classList.remove('active-century');
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

    const intervalMs = Math.round(140 / playbackSpeed);

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
    playbackSpeed = speedMultiplier;
    if (isPlaying) {
      pause();
      play();
    }
  }

  function stepYear(step) {
    setYear(currentYear + step);
  }

  function resetTimeline() {
    pause();
    setYear(1625); // Default golden epoch
  }

  function getCurrentYear() {
    return currentYear;
  }

  return {
    initTimeline,
    setYear,
    togglePlay,
    play,
    pause,
    setSpeed,
    stepYear,
    resetTimeline,
    getCurrentYear
  };
})();
