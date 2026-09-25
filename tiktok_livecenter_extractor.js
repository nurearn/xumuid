/**
 * TIKTOK LIVE CENTER 1-CLICK EXTRACTOR & SYNC SCRIPT
 * ==================================================
 * Cara Pakai:
 * 1. Buka browser di halaman: https://livecenter.tiktok.com/rank_list?lang=en
 * 2. Tekan F12 (atau klik kanan -> Inspect -> tab Console)
 * 3. Copy & paste kode di bawah ini lalu tekan Enter!
 * 4. Data langsung otomatis ter-sync ke http://localhost:5000 dan halaman TopGifter.html / Penonton Setia.html!
 */

(async function syncTikTokLiveCenter() {
  console.log("%c[TikTok Live Sync] Memulai ekstraksi data rank list...", "color: #25f4ee; font-weight: bold; font-size: 14px;");

  // Deteksi tab yang sedang aktif ("Most Gifts" atau "Most watch time")
  const activeTabEl = document.querySelector('.semi-tabs-item-active, [aria-selected="true"], .active') || document.body;
  const isWatchTime = document.body.innerText.includes('Most watch time') && (activeTabEl.innerText.includes('watch') || window.location.href.includes('watch'));
  
  // Ambil baris user ranking
  // Selector otomatis mencari container item list di Live Center
  const rows = Array.from(document.querySelectorAll('div, li, tr')).filter(el => {
    const text = el.innerText || '';
    return text.includes('Coins') || (text.includes('h ') && text.includes('m'));
  });

  // Cari elemen yang paling spesifik (yang punya nama & koin/jam)
  const userItems = [];
  const processedNames = new Set();

  // Parse dari elemen DOM umum di TikTok Live Center
  const candidateRows = document.querySelectorAll('[class*="item"], [class*="row"], [class*="card"], li');
  let currentRank = 1;

  for (const row of candidateRows) {
    const text = row.innerText || '';
    const hasCoins = /(\d+[\d,.]*)\s*Coins/i.exec(text);
    const hasWatchTime = /(\d+h\s*\d+m|\d+h|\d+m)/i.exec(text);

    if ((hasCoins || hasWatchTime) && (text.includes('Message') || text.includes('Follow') || row.querySelector('img'))) {
      const lines = text.split('\n').map(l => l.trim()).filter(Boolean);
      // Abaikan jika ini parent container yang menampung banyak baris
      if (lines.length > 15) continue;

      const img = row.querySelector('img');
      const avatarSrc = img ? img.src : null;

      // Cari baris username (biasanya baris sebelum badge atau sebelum coin/jam)
      let username = 'Viewer';
      for (const line of lines) {
        if (!line.includes('Coins') && 
            !line.includes('Message') && 
            !line.includes('Follow') && 
            !/^\d+$/.test(line) && 
            !line.includes('Total') && 
            !line.includes('Increase') &&
            !line.includes('xumu') &&
            !/^\d+h/i.test(line)) {
          username = line;
          break;
        }
      }

      if (username && !processedNames.has(username) && username !== 'Viewer ranking' && username !== 'Most Gifts') {
        processedNames.add(username);
        
        let badge = null;
        if (text.includes('xumu')) {
          badge = '🧡 xumu';
        }

        if (hasCoins) {
          const coinNum = parseInt(hasCoins[1].replace(/[,.]/g, ''), 10);
          userItems.push({
            rank: currentRank++,
            username: username,
            display_name: username,
            coins: coinNum,
            badge: badge,
            badge_type: badge ? 'fan_club' : null,
            avatar: avatarSrc
          });
        } else if (hasWatchTime) {
          userItems.push({
            rank: currentRank++,
            username: username,
            display_name: username,
            watch_time_str: hasWatchTime[1],
            badge: badge,
            badge_type: badge ? 'fan_club' : null,
            avatar: avatarSrc
          });
        }
      }
    }
  }

  console.log(`%c[TikTok Live Sync] Berhasil mengekstrak ${userItems.length} pengguna!`, "color: #22c55e; font-weight: bold;");
  console.table(userItems);

  if (userItems.length === 0) {
    alert("Belum terdeteksi data di layar. Pastikan kamu membuka tab 'Most Gifts' atau 'Most watch time' di TikTok Live Center!");
    return;
  }

  // Tentukan endpoint tujuan
  const isGifterData = userItems[0].coins !== undefined;
  const targetEndpoint = isGifterData ? 'http://localhost:5000/api/sync-gifters' : 'http://localhost:5000/api/sync-watchtime';
  const payloadKey = isGifterData ? 'gifters' : 'viewers';

  const payload = {
    updated_at: new Date().toISOString(),
    channel: "@xumuid",
    source: window.location.href,
    filter: "livecenter_extracted",
    [payloadKey]: userItems
  };

  try {
    const res = await fetch(targetEndpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const result = await res.json();
    console.log("%c[TikTok Live Sync] Berhasil sinkronisasi ke server lokal!", "color: #22c55e; font-weight: bold; font-size: 16px;");
    alert(`Sukses! ${userItems.length} data ${isGifterData ? 'Top Gifter' : 'Penonton Setia'} berhasil dikirim ke server & leaderboard.`);
  } catch (err) {
    console.warn("[TikTok Live Sync] Server lokal http://localhost:5000 belum aktif, mendownload file JSON sebagai gantinya...", err);
    
    // Download file JSON langsung jika server lokal belum dinyalakan
    const fileName = isGifterData ? 'top_gifters.json' : 'penonton_setia.json';
    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = fileName;
    a.click();
    alert(`File ${fileName} berhasil diunduh! Pindahkan ke folder Portfolio untuk update leaderboard.`);
  }
})();
