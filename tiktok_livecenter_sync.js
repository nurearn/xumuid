/**
 * TikTok Live Center -> Firebase Realtime Sync Tool
 * Buka https://livecenter.tiktok.com/rank_list?lang=en
 * Buka Console (Tekan F12 -> tab Console)
 * Paste kode ini lalu tekan Enter!
 */
(async function syncTikTokToFirebase() {
  const FIREBASE_ENDPOINT = "https://xumuid-dashboard-default-rtdb.asia-southeast1.firebasedatabase.app/xumuid-dashboard/tiktok_leaderboard.json";
  
  console.log("%c[xumuid]%c Memulai sinkronisasi TikTok Live Center...", "color:#fe2c55;font-weight:bold;", "color:#121212;");

  // 1. Deteksi Tab aktif (Most gifts / Most watch time)
  const isWatchTime = window.location.href.includes("watch") || 
                      document.body.innerText.includes("Most watch time") && 
                      document.querySelector('.semi-tabs-item-active')?.innerText?.toLowerCase().includes("watch");

  // 2. Ambil baris tabel
  const rows = document.querySelectorAll('tr.semi-table-row, div[role="row"]');
  const items = [];

  rows.forEach((row, idx) => {
    try {
      const text = row.innerText.trim().split('\n').filter(Boolean);
      if (text.length < 2) return;

      const rank = parseInt(text[0]) || (idx + 1);
      const name = text[1] || `User_${rank}`;
      
      // Deteksi koin atau watch time
      let amountVal = text[text.length - 1];
      let coins = 0;
      let watchStr = "";

      if (isWatchTime) {
        watchStr = amountVal;
      } else {
        coins = parseInt(amountVal.replace(/[^0-9]/g, '')) || 0;
      }

      // Deteksi avatar
      const img = row.querySelector('img');
      const avatar = img ? img.src : '';

      // Deteksi badge
      let badge = null;
      if (text.some(t => t.includes('xumu') || t.includes('team') || t.includes('fan'))) {
        badge = "🧡 xumu";
      }

      if (isWatchTime) {
        items.push({
          rank: rank,
          username: name,
          display_name: name,
          watch_time_str: watchStr,
          badge: badge,
          avatar: avatar
        });
      } else {
        items.push({
          rank: rank,
          username: name,
          display_name: name,
          coins: coins,
          badge: badge,
          avatar: avatar
        });
      }
    } catch(e) {}
  });

  if (items.length === 0) {
    console.warn("%c[xumuid]%c Tabel tidak ditemukan atau data belum termuat. Pastikan halaman sudah terbuka sempurna.", "color:#eab308;font-weight:bold;", "color:#121212;");
    alert("Tabel TikTok Live Center belum siap atau belum terbuka. Silakan coba beberapa detik lagi.");
    return;
  }

  // Siapkan payload
  const payload = {};
  if (isWatchTime) {
    payload.penonton_setia = {
      channel: "@xumuid",
      filter: "60_days",
      updated_at: new Date().toISOString(),
      viewers: items.slice(0, 10)
    };
  } else {
    payload.top_gifters = {
      channel: "@xumuid",
      filter: "60_days",
      updated_at: new Date().toISOString(),
      gifters: items.slice(0, 10)
    };
  }
  payload.last_updated = new Date().toISOString();

  // Kirim ke Firebase Realtime Database
  try {
    const res = await fetch(FIREBASE_ENDPOINT, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (res.ok) {
      console.log("%c[xumuid SUKSES]%c Data berhasil disinkronkan langsung ke Firebase!", "color:#22c55e;font-weight:bold;font-size:14px;", "color:#121212;");
      alert("✅ BERHASIL!\nData TikTok Live Center Anda langsung terkirim ke Firebase & website penonton otomatis ter-update realtime!");
    } else {
      console.error("Gagal mengirim ke Firebase:", res.status);
    }
  } catch(err) {
    console.error("Koneksi gagal:", err);
  }
})();
