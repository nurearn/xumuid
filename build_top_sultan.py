import base64
import os
import json
import urllib.request
import re

print("Building Upgraded Top Sultan Leaderboard with CDN Medals, Light Animation, Neo Motifs & No-Rocket CTA...")

# 1. Fetch current live leaderboard data from sociabuzz to embed as initial state
initial_donors = [
    {"rank": 1, "name": "Ncann", "amount": "IDR300,000"},
    {"rank": 2, "name": "Kairi", "amount": "IDR177,000"},
    {"rank": 3, "name": "Rrn", "amount": "IDR137,000"},
    {"rank": 4, "name": "Ilham", "amount": "IDR100,000"},
    {"rank": 5, "name": "Rrn", "amount": "IDR5000"},
    {"rank": 6, "name": "FKIH", "amount": "IDR2000"},
    {"rank": 7, "name": "Void", "amount": "IDR1000"},
    {"rank": 8, "name": "Void", "amount": "IDR1000"},
    {"rank": 9, "name": "Aosmareal", "amount": "IDR1000"},
]

try:
    url = "https://sociabuzz.com/pro/tribe/tribe_profile/get_detail_leaderboard_int_v4/3811394092"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=5) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        html_raw = data.get('datas', '')
        rows = re.findall(r'<strong class="text-limit\s*">\s*([^<]+)\s*</strong>.*?<strong class="text-limit-r">\s*([^<]+)\s*</strong>', html_raw, re.DOTALL)
        if rows:
            initial_donors = [{"rank": i + 1, "name": r[0].strip(), "amount": r[1].strip()} for i, r in enumerate(rows)]
            print(f"Fetched {len(initial_donors)} live donors from Sociabuzz API!")
except Exception as e:
    print(f"Using cached initial donors: {e}")

# 2. Load Medals (both Base64 and CDN URLs)
medal_1st_b64 = ''
medal_2nd_b64 = ''
medal_3rd_b64 = ''

if os.path.exists('medal_1st.png'):
    with open('medal_1st.png', 'rb') as f:
        medal_1st_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')
if os.path.exists('medal_2nd.png'):
    with open('medal_2nd.png', 'rb') as f:
        medal_2nd_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')
if os.path.exists('medal_3rd.png'):
    with open('medal_3rd.png', 'rb') as f:
        medal_3rd_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

# Fallback CDN URLs if local file is unavailable
cdn_medal_1 = "https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@main/assets/1st%20place%20medal/3D/1st_place_medal_3d.png"
cdn_medal_2 = "https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@main/assets/2nd%20place%20medal/3D/2nd_place_medal_3d.png"
cdn_medal_3 = "https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@main/assets/3rd%20place%20medal/3D/3rd_place_medal_3d.png"

medal_src_1 = medal_1st_b64 if medal_1st_b64 else cdn_medal_1
medal_src_2 = medal_2nd_b64 if medal_2nd_b64 else cdn_medal_2
medal_src_3 = medal_3rd_b64 if medal_3rd_b64 else cdn_medal_3

# Load avatar if exists
avatar_path = r'c:\Users\Rian\Desktop\Portfolio\xumuid_avatar.jpg'
avatar_b64 = ''
if os.path.exists(avatar_path):
    with open(avatar_path, 'rb') as f:
        avatar_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

initial_donors_json = json.dumps(initial_donors)

html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Top Sultan | xumu id Leaderboard</title>
  <meta name="description" content="Leaderboard Top Sultan Donatur & Supporter xumu id (@xumuid) - Push sekarang dan dukung via Sociabuzz Tribe!">
  <link rel="icon" href="{avatar_b64}">

  <!-- Google Fonts: Space Grotesk & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&family=Space+Grotesk:wght@600;700;800;900&display=swap" rel="stylesheet">

  <!-- Font Awesome 6 CDN for Crisp Vector Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer">

  <style>
    /* --- NEO-BRUTALISM LIGHT TOKENS --- */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    :root {{
      --bg-cream: #fbf7ee;
      --card-white: #ffffff;
      --border-black: #121212;
      --text-black: #121212;
      --text-muted: #525252;
      
      --gold-rank: #fde047;
      --gold-glow: #eab308;
      --silver-rank: #e2e8f0;
      --silver-glow: #94a3b8;
      --bronze-rank: #fdba74;
      --bronze-glow: #ea580c;
      
      --cyan-neo: #7dd3fc;
      --green-neo: #86efac;
      --purple-neo: #c4b5fd;
      --pink-neo: #f472b6;
      --orange-neo: #fb923c;
      
      --font-display: 'Space Grotesk', sans-serif;
      --font-sans: 'Plus Jakarta Sans', sans-serif;
      
      --shadow-card: 6px 6px 0px #121212;
      --shadow-btn: 4px 4px 0px #121212;
      --shadow-btn-hover: 6px 6px 0px #121212;
      --shadow-btn-active: 1px 1px 0px #121212;
    }}

    html, body {{
      min-height: 100vh;
      width: 100%;
      font-family: var(--font-sans);
      background-color: var(--bg-cream);
      color: var(--text-black);
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      position: relative;
    }}

    /* ======================================================================
       RETRO NEO-BRUTALIST BACKGROUND MOTIFS
       ====================================================================== */
    /* 1. Base Dot Grid */
    .bg-dots {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      background-image: radial-gradient(#121212 1.3px, transparent 1.3px);
      background-size: 24px 24px;
      opacity: 0.14;
    }}

    /* 2. Floating Neo-Brutalist Geometric Stickers / Decals in Background */
    .neo-decorations {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }}

    .neo-sticker {{
      position: absolute;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 2.5px solid var(--border-black);
      box-shadow: 3px 3px 0px #121212;
      font-family: var(--font-display);
      font-weight: 800;
      user-select: none;
    }}

    /* Sparkle Star 1 - Top Left */
    .sticker-star-1 {{
      top: 36px;
      left: 5%;
      width: 44px;
      height: 44px;
      background: var(--gold-rank);
      border-radius: 12px;
      transform: rotate(-12deg);
      font-size: 22px;
      animation: floatSlow 4s ease-in-out infinite alternate;
    }}

    /* Neo Badge - Top Right */
    .sticker-pill-1 {{
      top: 48px;
      right: 4%;
      background: var(--pink-neo);
      color: #121212;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 11px;
      letter-spacing: 0.05em;
      transform: rotate(8deg);
      animation: floatSlow 5s ease-in-out infinite alternate-reverse;
    }}

    /* Floating Plus Cross - Middle Left */
    .sticker-plus-1 {{
      top: 36%;
      left: 3%;
      width: 36px;
      height: 36px;
      background: var(--cyan-neo);
      border-radius: 10px;
      transform: rotate(15deg);
      font-size: 22px;
      animation: floatSlow 4.5s ease-in-out infinite alternate;
    }}

    /* Floating Diamond / Cube - Middle Right */
    .sticker-cube-1 {{
      top: 42%;
      right: 3%;
      width: 40px;
      height: 40px;
      background: var(--purple-neo);
      border-radius: 8px;
      transform: rotate(25deg);
      font-size: 20px;
      animation: floatSlow 3.8s ease-in-out infinite alternate-reverse;
    }}

    /* Diagonal Caution Stripes Strip - Bottom Left */
    .sticker-stripes {{
      bottom: 60px;
      left: 4%;
      padding: 4px 12px;
      background: repeating-linear-gradient(
        -45deg,
        #fde047,
        #fde047 10px,
        #121212 10px,
        #121212 20px
      );
      color: #ffffff;
      font-size: 10px;
      border-radius: 6px;
      transform: rotate(-8deg);
      border: 2px solid var(--border-black);
      box-shadow: 2.5px 2.5px 0px #121212;
    }}

    /* Starburst Sticker - Bottom Right */
    .sticker-star-2 {{
      bottom: 75px;
      right: 5%;
      width: 46px;
      height: 46px;
      background: var(--green-neo);
      border-radius: 50%;
      transform: rotate(12deg);
      font-size: 20px;
      animation: floatSlow 4.2s ease-in-out infinite alternate;
    }}

    @keyframes floatSlow {{
      0% {{ transform: translateY(0px) rotate(0deg); }}
      100% {{ transform: translateY(-8px) rotate(6deg); }}
    }}

    /* ======================================================================
       MAIN RESPONSIVE CONTAINER
       ====================================================================== */
    .page-wrapper {{
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 480px;
      padding: 20px 14px 48px 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 0 auto;
      box-sizing: border-box;
    }}

    /* Top Navigation Bar */
    .top-nav-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      margin-bottom: 16px;
    }}

    .nav-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--card-white);
      border: 2.5px solid var(--border-black);
      box-shadow: 2px 2px 0px #121212;
      border-radius: 999px;
      padding: 7px 15px;
      font-family: var(--font-display);
      font-size: 12px;
      font-weight: 800;
      color: var(--text-black);
      text-decoration: none;
      transition: all 0.15s ease;
      cursor: pointer;
    }}

    .nav-btn:hover {{
      transform: translate(-1px, -1px);
      box-shadow: 3.5px 3.5px 0px #121212;
      background: var(--gold-rank);
    }}

    .nav-btn:active {{
      transform: translate(1px, 1px);
      box-shadow: 1px 1px 0px #121212;
    }}

    .live-status-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #121212;
      color: #ffffff;
      border: 2.5px solid var(--border-black);
      box-shadow: 2px 2px 0px rgba(0,0,0,0.25);
      border-radius: 999px;
      padding: 6px 14px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.04em;
    }}

    .live-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: #22c55e;
      display: inline-block;
      animation: pulseLive 1.5s infinite;
    }}

    @keyframes pulseLive {{
      0%, 100% {{ transform: scale(1); opacity: 1; }}
      50% {{ transform: scale(1.3); opacity: 0.8; box-shadow: 0 0 8px #22c55e; }}
    }}

    /* ======================================================================
       MAIN NEO-BRUTALIST CARD
       ====================================================================== */
    .neo-card {{
      width: 100%;
      background: var(--card-white);
      border: 3.5px solid var(--border-black);
      border-radius: 28px;
      box-shadow: var(--shadow-card);
      padding: 24px 16px;
      box-sizing: border-box;
      position: relative;
      overflow: hidden;
      animation: cardEntrance 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) backwards;
    }}

    /* Subtle decorative corner badge inside card */
    .neo-card::before {{
      content: '★ TOP SULTAN ★';
      position: absolute;
      top: -12px;
      right: -24px;
      background: var(--gold-rank);
      color: #121212;
      border: 2px solid var(--border-black);
      padding: 3px 28px;
      font-family: var(--font-display);
      font-size: 9px;
      font-weight: 900;
      transform: rotate(45deg);
      box-shadow: 0 2px 0 #121212;
      pointer-events: none;
      z-index: 10;
    }}

    @keyframes cardEntrance {{
      0% {{ opacity: 0; transform: translateY(20px) scale(0.98); }}
      100% {{ opacity: 1; transform: translateY(0) scale(1); }}
    }}

    /* Card Header */
    .leaderboard-header {{
      text-align: center;
      margin-bottom: 22px;
    }}

    .header-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #fef08a;
      border: 2px solid var(--border-black);
      box-shadow: 2px 2px 0px #121212;
      border-radius: 999px;
      padding: 4px 14px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 10px;
    }}

    .leaderboard-title {{
      font-family: var(--font-display);
      font-size: 32px;
      font-weight: 900;
      color: var(--text-black);
      letter-spacing: -0.02em;
      line-height: 1.1;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
    }}

    .leaderboard-title i {{
      color: #eab308;
      filter: drop-shadow(2px 2px 0px #121212);
      -webkit-text-stroke: 1.5px #121212;
    }}

    .leaderboard-subtitle {{
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      margin-top: 5px;
    }}

    /* ======================================================================
       OLYMPIC PODIUM (Juara 1 - 3: Kiri=2, Tengah=1, Kanan=3)
       DENGAN ANIMASI TERANG & CDN MEDALS
       ====================================================================== */
    .podium-container {{
      display: flex;
      align-items: flex-end;
      justify-content: center;
      gap: 10px;
      width: 100%;
      margin: 18px 0 28px 0;
      padding: 10px 4px 0 4px;
      position: relative;
    }}

    .podium-col {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
    }}

    /* Podium 1 (Center) - Tallest */
    .col-rank-1 {{
      order: 2;
      z-index: 3;
    }}
    /* Podium 2 (Left) */
    .col-rank-2 {{
      order: 1;
      z-index: 2;
    }}
    /* Podium 3 (Right) */
    .col-rank-3 {{
      order: 3;
      z-index: 1;
    }}

    /* Floating Crown on Top of Rank 1 */
    .crown-sticker {{
      font-size: 28px;
      filter: drop-shadow(2px 2px 0px #121212);
      animation: crownBounce 2s ease-in-out infinite alternate;
      margin-bottom: -6px;
      z-index: 6;
      color: #fde047;
    }}

    @keyframes crownBounce {{
      0% {{ transform: translateY(0) rotate(-4deg) scale(1); }}
      100% {{ transform: translateY(-7px) rotate(4deg) scale(1.08); }}
    }}

    /* ======================================================================
       ANIMASI TERANG (LIGHT ANIMATIONS: SUNBURST AURA, RADIANT BEAMS & SHINE)
       ====================================================================== */
    .radiant-halo {{
      position: absolute;
      top: 50%;
      left: 50%;
      width: 130px;
      height: 130px;
      transform: translate(-50%, -50%);
      border-radius: 50%;
      pointer-events: none;
      z-index: 0;
      opacity: 0.85;
    }}

    /* Juara 1: Intense Golden Sunburst & Pulsing Glow */
    .col-rank-1 .radiant-halo {{
      width: 150px;
      height: 150px;
      background: radial-gradient(circle, rgba(254, 240, 138, 0.9) 0%, rgba(250, 204, 21, 0.5) 45%, transparent 70%);
      animation: goldBeacon 2s ease-in-out infinite alternate;
    }}

    .col-rank-1 .radiant-rays {{
      position: absolute;
      top: 50%;
      left: 50%;
      width: 140px;
      height: 140px;
      transform: translate(-50%, -50%);
      border-radius: 50%;
      background: repeating-conic-gradient(
        from 0deg,
        rgba(254, 240, 138, 0.5) 0deg 15deg,
        transparent 15deg 30deg
      );
      animation: spinRays 10s linear infinite;
      pointer-events: none;
      z-index: 0;
    }}

    /* Juara 2: Silver Radiant Aura */
    .col-rank-2 .radiant-halo {{
      background: radial-gradient(circle, rgba(241, 245, 249, 0.95) 0%, rgba(186, 230, 253, 0.5) 50%, transparent 75%);
      animation: silverBeacon 2.4s ease-in-out infinite alternate;
    }}

    /* Juara 3: Bronze Radiant Aura */
    .col-rank-3 .radiant-halo {{
      background: radial-gradient(circle, rgba(254, 215, 170, 0.9) 0%, rgba(251, 146, 60, 0.45) 50%, transparent 75%);
      animation: bronzeBeacon 2.6s ease-in-out infinite alternate;
    }}

    @keyframes spinRays {{
      0% {{ transform: translate(-50%, -50%) rotate(0deg); }}
      100% {{ transform: translate(-50%, -50%) rotate(360deg); }}
    }}

    @keyframes goldBeacon {{
      0% {{
        transform: translate(-50%, -50%) scale(0.92);
        filter: drop-shadow(0 0 10px rgba(250, 204, 21, 0.6));
      }}
      100% {{
        transform: translate(-50%, -50%) scale(1.15);
        filter: drop-shadow(0 0 25px rgba(234, 179, 8, 0.95)) drop-shadow(0 0 40px rgba(254, 240, 138, 0.8));
      }}
    }}

    @keyframes silverBeacon {{
      0% {{
        transform: translate(-50%, -50%) scale(0.95);
        filter: drop-shadow(0 0 8px rgba(186, 230, 253, 0.5));
      }}
      100% {{
        transform: translate(-50%, -50%) scale(1.12);
        filter: drop-shadow(0 0 20px rgba(148, 163, 184, 0.85)) drop-shadow(0 0 35px rgba(226, 232, 240, 0.7));
      }}
    }}

    @keyframes bronzeBeacon {{
      0% {{
        transform: translate(-50%, -50%) scale(0.95);
        filter: drop-shadow(0 0 8px rgba(251, 146, 60, 0.5));
      }}
      100% {{
        transform: translate(-50%, -50%) scale(1.1);
        filter: drop-shadow(0 0 20px rgba(234, 88, 12, 0.8)) drop-shadow(0 0 32px rgba(253, 186, 116, 0.7));
      }}
    }}

    /* Podium Avatar & Medal Frame */
    .podium-avatar-wrapper {{
      position: relative;
      width: 68px;
      height: 68px;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .col-rank-1 .podium-avatar-wrapper {{
      width: 82px;
      height: 82px;
      margin-bottom: 14px;
    }}

    .podium-avatar-frame {{
      width: 100%;
      height: 100%;
      border-radius: 50%;
      border: 3px solid var(--border-black);
      box-shadow: 3px 3px 0px #121212;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      position: relative;
      z-index: 1;
    }}

    .col-rank-1 .podium-avatar-frame {{
      border: 3.5px solid var(--border-black);
      box-shadow: 4px 4px 0px #121212;
      background: #fffbeb;
    }}

    /* CDN 3D Medal Image inside Avatar Frame */
    .medal-cdn-img {{
      width: 82%;
      height: 82%;
      object-fit: contain;
      filter: drop-shadow(1.5px 1.5px 0px rgba(0,0,0,0.25));
      transition: transform 0.2s ease;
      z-index: 2;
    }}

    .podium-col:hover .medal-cdn-img {{
      transform: scale(1.15) rotate(5deg);
    }}

    /* Gleam / Light Sweep Effect across Medal Circle */
    .podium-avatar-frame::after {{
      content: '';
      position: absolute;
      top: -50%;
      left: -60%;
      width: 220%;
      height: 200%;
      background: linear-gradient(
        60deg,
        transparent 35%,
        rgba(255, 255, 255, 0.8) 50%,
        transparent 65%
      );
      transform: rotate(25deg);
      animation: gleamSweep 3s ease-in-out infinite;
      pointer-events: none;
      z-index: 3;
    }}

    @keyframes gleamSweep {{
      0% {{ transform: translateX(-100%) rotate(25deg); }}
      25%, 100% {{ transform: translateX(100%) rotate(25deg); }}
    }}

    /* Small badge at bottom corner of medal */
    .podium-medal-badge {{
      position: absolute;
      bottom: -4px;
      right: -4px;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      border: 2px solid var(--border-black);
      box-shadow: 1.5px 1.5px 0px #121212;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-display);
      font-size: 11.5px;
      font-weight: 900;
      z-index: 5;
    }}

    .badge-gold {{
      background: var(--gold-rank);
      color: #121212;
    }}
    .badge-silver {{
      background: var(--silver-rank);
      color: #121212;
    }}
    .badge-bronze {{
      background: var(--bronze-rank);
      color: #121212;
    }}

    /* Donor Info Above Pedestal */
    .podium-donor-name {{
      font-family: var(--font-display);
      font-size: 13.5px;
      font-weight: 800;
      color: var(--text-black);
      max-width: 100%;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-bottom: 4px;
    }}

    .col-rank-1 .podium-donor-name {{
      font-size: 15px;
      color: #121212;
      font-weight: 900;
    }}

    .podium-donor-amount {{
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 800;
      padding: 2.5px 8px;
      border-radius: 999px;
      border: 1.5px solid var(--border-black);
      box-shadow: 1.5px 1.5px 0px #121212;
      white-space: nowrap;
      margin-bottom: 8px;
    }}

    .col-rank-1 .podium-donor-amount {{
      background: var(--gold-rank);
      font-size: 12px;
      padding: 3px 10px;
      box-shadow: 2px 2px 0px #121212;
    }}
    .col-rank-2 .podium-donor-amount {{
      background: var(--silver-rank);
    }}
    .col-rank-3 .podium-donor-amount {{
      background: var(--bronze-rank);
    }}

    /* The Solid Pedestal Block */
    .pedestal-block {{
      width: 100%;
      border: 3px solid var(--border-black);
      box-shadow: 4px 4px 0px #121212;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      padding-top: 12px;
      border-radius: 16px 16px 6px 6px;
      position: relative;
      overflow: hidden;
    }}

    /* Subtle light reflection on pedestal */
    .pedestal-block::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: rgba(255, 255, 255, 0.6);
      pointer-events: none;
    }}

    .col-rank-1 .pedestal-block {{
      height: 140px;
      background: var(--gold-rank);
      box-shadow: 5px 5px 0px #121212;
    }}
    .col-rank-2 .pedestal-block {{
      height: 105px;
      background: var(--silver-rank);
    }}
    .col-rank-3 .pedestal-block {{
      height: 80px;
      background: var(--bronze-rank);
    }}

    .pedestal-number {{
      font-family: var(--font-display);
      font-size: 32px;
      font-weight: 900;
      color: var(--text-black);
      line-height: 1;
    }}

    .col-rank-1 .pedestal-number {{
      font-size: 44px;
    }}

    .pedestal-label {{
      font-family: var(--font-display);
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-top: 4px;
      opacity: 0.85;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    /* ======================================================================
       RANKS 4 - 10 LIST SECTION
       ====================================================================== */
    .list-section-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      margin: 20px 0 12px 0;
      padding-bottom: 8px;
      border-bottom: 2.5px dashed #cbd5e1;
    }}

    .list-section-title {{
      font-family: var(--font-display);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .list-count-badge {{
      background: var(--border-black);
      color: #ffffff;
      font-family: var(--font-display);
      font-size: 10.5px;
      font-weight: 800;
      padding: 2.5px 9px;
      border-radius: 999px;
    }}

    .ranks-stack {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 100%;
      margin-bottom: 24px;
    }}

    .rank-row-card {{
      display: flex;
      align-items: center;
      width: 100%;
      min-height: 52px;
      padding: 8px 12px;
      background: #f8fafc;
      border: 2px solid var(--border-black);
      box-shadow: 3px 3px 0px #121212;
      border-radius: 14px;
      transition: all 0.15s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .rank-row-card:hover {{
      transform: translate(-2px, -2px);
      box-shadow: 5px 5px 0px #121212;
      background: #ffffff;
    }}

    .rank-number-box {{
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: #ffffff;
      border: 2px solid var(--border-black);
      box-shadow: 1.5px 1.5px 0px #121212;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-display);
      font-size: 13px;
      font-weight: 800;
      color: #121212;
      margin-right: 10px;
      flex-shrink: 0;
    }}

    .rank-donor-info {{
      flex: 1 1 0%;
      min-width: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      overflow: hidden;
    }}

    .rank-donor-name {{
      font-family: var(--font-display);
      font-size: 13.5px;
      font-weight: 800;
      color: #121212;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .rank-donor-amount-badge {{
      font-family: var(--font-display);
      font-size: 11.5px;
      font-weight: 800;
      color: #121212;
      background: #fef08a;
      border: 1.5px solid var(--border-black);
      box-shadow: 1.5px 1.5px 0px #121212;
      padding: 3px 9px;
      border-radius: 999px;
      white-space: nowrap;
      margin-left: 8px;
      flex-shrink: 0;
    }}

    /* ======================================================================
       CTA BUTTON: PUSH SEKARANG (NO ROCKET! USING CROWN & LIGHTNING)
       ====================================================================== */
    .cta-push-wrapper {{
      width: 100%;
      margin: 12px 0 16px 0;
    }}

    .cta-push-btn {{
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%;
      padding: 16px 14px;
      background: #22c55e;
      border: 3.5px solid var(--border-black);
      box-shadow: var(--shadow-btn);
      border-radius: 20px;
      text-decoration: none;
      color: #121212;
      cursor: pointer;
      user-select: none;
      transition: all 0.15s cubic-bezier(0.34, 1.56, 0.64, 1);
      overflow: hidden;
    }}

    .cta-push-btn::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: rgba(255, 255, 255, 0.4);
      pointer-events: none;
    }}

    .cta-push-btn:hover {{
      transform: translate(-2px, -2px);
      box-shadow: var(--shadow-btn-hover);
      background: #4ade80;
    }}

    .cta-push-btn:active {{
      transform: translate(3px, 3px);
      box-shadow: var(--shadow-btn-active);
    }}

    .cta-top-tag {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: #121212;
      color: #fde047;
      font-family: var(--font-display);
      font-size: 10.5px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 999px;
      margin-bottom: 6px;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}

    .cta-main-title {{
      font-family: var(--font-display);
      font-size: 18px;
      font-weight: 900;
      letter-spacing: -0.01em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .cta-main-title i.fa-crown {{
      color: #fde047;
      filter: drop-shadow(1.5px 1.5px 0px #121212);
      -webkit-text-stroke: 1.5px #121212;
      font-size: 20px;
    }}

    .cta-main-title i.fa-bolt {{
      color: #fde047;
      filter: drop-shadow(1.5px 1.5px 0px #121212);
      -webkit-text-stroke: 1.2px #121212;
      font-size: 17px;
    }}

    .cta-subtitle {{
      font-size: 11.5px;
      font-weight: 700;
      opacity: 0.95;
      margin-top: 3px;
      text-align: center;
    }}

    /* Footer & Overlay Status */
    .card-footer {{
      margin-top: 16px;
      text-align: center;
      font-size: 11.5px;
      font-weight: 600;
      color: var(--text-muted);
    }}


    /* Toast */
    .neo-toast {{
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(80px);
      background: #ffffff;
      border: 2.5px solid var(--border-black);
      box-shadow: 4px 4px 0px #121212;
      color: #121212;
      padding: 10px 22px;
      border-radius: 999px;
      font-family: var(--font-display);
      font-size: 13px;
      font-weight: 800;
      z-index: 2000;
      opacity: 0;
      pointer-events: none;
      transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .neo-toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}

    /* Responsiveness */
    @media (max-width: 480px) {{
      .page-wrapper {{
        padding: 16px 10px 36px 10px;
      }}
      .neo-card {{
        padding: 20px 12px;
        border-radius: 24px;
      }}
      .leaderboard-title {{
        font-size: 28px;
      }}
      .col-rank-1 .pedestal-block {{
        height: 125px;
      }}
      .col-rank-2 .pedestal-block {{
        height: 95px;
      }}
      .col-rank-3 .pedestal-block {{
        height: 75px;
      }}
      .podium-donor-name {{
        font-size: 12px;
      }}
      .col-rank-1 .podium-donor-name {{
        font-size: 13.5px;
      }}
      .podium-donor-amount {{
        font-size: 10px;
      }}
      .col-rank-1 .podium-donor-amount {{
        font-size: 11px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Retro Neo-Brutalist Dot Grid Layer -->
  <div class="bg-dots" aria-hidden="true"></div>

  <!-- Retro Neo-Brutalist Background Motifs (Decals & Stickers) -->
  <div class="neo-decorations" aria-hidden="true">
    <div class="neo-sticker sticker-star-1">✦</div>
    <div class="neo-sticker sticker-pill-1"><i class="fa-solid fa-crown" style="margin-right: 4px;"></i> TOP 10</div>
    <div class="neo-sticker sticker-plus-1">+</div>
    <div class="neo-sticker sticker-cube-1">★</div>
    <div class="neo-sticker sticker-stripes">/// PUSH SULTAN ///</div>
    <div class="neo-sticker sticker-star-2">👑</div>
  </div>

  <main class="page-wrapper">

    <!-- Top Navigation -->
    <header class="top-nav-bar">
      <a href="index.html" class="nav-btn" title="Kembali ke Dashboard Portfolio">
        <i class="fa-solid fa-arrow-left"></i>
        <span>Portfolio</span>
      </a>
      <div class="live-status-pill" id="live-indicator">
        <span class="live-dot"></span>
        <span>LIVE SULTAN</span>
      </div>
    </header>

    <!-- Main Leaderboard Card -->
    <article class="neo-card">

      <div class="leaderboard-header">
        <div class="header-badge">
          <i class="fa-solid fa-crown" style="color: #ca8a04;"></i>
          <span>SOCIABUZZ TRIBE LEADERBOARD</span>
        </div>
        <h1 class="leaderboard-title">
          <span>TOP SULTAN</span>
          <i class="fa-solid fa-trophy"></i>
        </h1>
        <p class="leaderboard-subtitle">Peringkat Donatur &amp; Supporter Terbesar xumu id</p>
      </div>

      <!-- ======================================================================
           PODIUM TOP 1-3 (Juara 2 di Kiri, Juara 1 di Tengah, Juara 3 di Kanan)
           DENGAN CDN 3D MEDALS & ANIMASI TERANG RADIANT
           ====================================================================== -->
      <section class="podium-container" aria-label="Podium Top 3 Sultan">

        <!-- JUARA 2 (SILVER - KIRI) -->
        <div class="podium-col col-rank-2">
          <div class="podium-avatar-wrapper">
            <!-- Radiant Silver Glow Halo -->
            <div class="radiant-halo"></div>

            <div class="podium-avatar-frame">
              <img src="{medal_src_2}" alt="Silver Medal 2nd Place" class="medal-cdn-img" loading="eager">
            </div>
            <div class="podium-medal-badge badge-silver">2</div>
          </div>
          <span class="podium-donor-name" id="podium-name-2">Kairi</span>
          <span class="podium-donor-amount" id="podium-amount-2">IDR 177,000</span>
          <div class="pedestal-block">
            <span class="pedestal-number">2</span>
            <span class="pedestal-label">
              <i class="fa-solid fa-medal"></i> SILVER
            </span>
          </div>
        </div>

        <!-- JUARA 1 (GOLD - TENGAH) -->
        <div class="podium-col col-rank-1">
          <div class="crown-sticker">👑</div>
          <div class="podium-avatar-wrapper">
            <!-- Radiant Sunburst Light Rays & Pulsing Aura -->
            <div class="radiant-rays"></div>
            <div class="radiant-halo"></div>

            <div class="podium-avatar-frame">
              <img src="{medal_src_1}" alt="Gold Medal 1st Place" class="medal-cdn-img" loading="eager">
            </div>
            <div class="podium-medal-badge badge-gold">1</div>
          </div>
          <span class="podium-donor-name" id="podium-name-1">Ncann</span>
          <span class="podium-donor-amount" id="podium-amount-1">IDR 300,000</span>
          <div class="pedestal-block">
            <span class="pedestal-number">1</span>
            <span class="pedestal-label">
              <i class="fa-solid fa-crown"></i> SULTAN #1
            </span>
          </div>
        </div>

        <!-- JUARA 3 (BRONZE - KANAN) -->
        <div class="podium-col col-rank-3">
          <div class="podium-avatar-wrapper">
            <!-- Radiant Bronze Glow Halo -->
            <div class="radiant-halo"></div>

            <div class="podium-avatar-frame">
              <img src="{medal_src_3}" alt="Bronze Medal 3rd Place" class="medal-cdn-img" loading="eager">
            </div>
            <div class="podium-medal-badge badge-bronze">3</div>
          </div>
          <span class="podium-donor-name" id="podium-name-3">Rrn</span>
          <span class="podium-donor-amount" id="podium-amount-3">IDR 137,000</span>
          <div class="pedestal-block">
            <span class="pedestal-number">3</span>
            <span class="pedestal-label">
              <i class="fa-solid fa-medal"></i> BRONZE
            </span>
          </div>
        </div>

      </section>

      <!-- ======================================================================
           RANKS 4 - 10 LIST
           ====================================================================== -->
      <div class="list-section-header">
        <span class="list-section-title">
          <i class="fa-solid fa-list-ol"></i>
          PERINGKAT 4 - 10
        </span>
        <span class="list-count-badge" id="list-counter">TOP LIST</span>
      </div>

      <div class="ranks-stack" id="ranks-list-container" role="list">
        <!-- Rendered dynamically -->
      </div>

      <!-- ======================================================================
           CTA BUTTON: PUSH SEKARANG (NO ROCKET! USING CROWN & LIGHTNING)
           ====================================================================== -->
      <div class="cta-push-wrapper">
        <a href="https://sociabuzz.com/xumu_id/tribe" class="cta-push-btn" target="_blank" rel="noopener noreferrer">
          <span class="cta-top-tag">
            <i class="fa-solid fa-bolt"></i> DUKUNG SEKARANG
          </span>
          <span class="cta-main-title">
            <i class="fa-solid fa-crown"></i>
            <span>PUSH SEKARANG!</span>
            <i class="fa-solid fa-bolt"></i>
          </span>
          <span class="cta-subtitle">Dukung xumuid &amp; rebut tahta Top Sultan di leaderboard ini! 👑</span>
        </a>
      </div>

      <!-- Footer -->
      <footer class="card-footer">
        <span>© 2026 xumu id · Top Sultan Leaderboard</span>
      </footer>

    </article>
  </main>

  <!-- Interactive Sound & Realtime Overlay Sync Script -->
  <script>
    // 1. Initial Donors Embedded from Server
    let currentDonors = {initial_donors_json};

    function renderLeaderboard(donors) {{
      if (!donors || donors.length === 0) return;

      // Update Top 1-3 Podium
      // Rank 1
      const d1 = donors.find(d => d.rank === 1) || donors[0];
      if (d1) {{
        document.getElementById('podium-name-1').textContent = d1.name || 'Anonymous';
        document.getElementById('podium-amount-1').textContent = formatCurrency(d1.amount);
      }}

      // Rank 2
      const d2 = donors.find(d => d.rank === 2) || donors[1];
      if (d2) {{
        document.getElementById('podium-name-2').textContent = d2.name || 'Anonymous';
        document.getElementById('podium-amount-2').textContent = formatCurrency(d2.amount);
      }}

      // Rank 3
      const d3 = donors.find(d => d.rank === 3) || donors[2];
      if (d3) {{
        document.getElementById('podium-name-3').textContent = d3.name || 'Anonymous';
        document.getElementById('podium-amount-3').textContent = formatCurrency(d3.amount);
      }}

      // Update Ranks 4-10 List
      const listContainer = document.getElementById('ranks-list-container');
      const remainingDonors = donors.filter(d => d.rank >= 4 && d.rank <= 10);
      
      let html = '';
      if (remainingDonors.length === 0) {{
        // Fallback default list if fewer than 4 donors
        for (let i = 4; i <= 10; i++) {{
          html += `
            <div class="rank-row-card" role="listitem">
              <div class="rank-number-box">#${{i}}</div>
              <div class="rank-donor-info">
                <span class="rank-donor-name" style="opacity: 0.5;">Slot Kosong</span>
              </div>
              <span class="rank-donor-amount-badge" style="opacity: 0.5;">-</span>
            </div>
          `;
        }}
      }} else {{
        remainingDonors.forEach(d => {{
          html += `
            <div class="rank-row-card" role="listitem">
              <div class="rank-number-box">#${{d.rank}}</div>
              <div class="rank-donor-info">
                <span class="rank-donor-name">${{escapeHtml(d.name)}}</span>
              </div>
              <span class="rank-donor-amount-badge">${{escapeHtml(formatCurrency(d.amount))}}</span>
            </div>
          `;
        }});
      }}
      listContainer.innerHTML = html;
    }}

    function formatCurrency(val) {{
      if (!val) return 'IDR 0';
      val = val.toString().trim();
      if (val.toUpperCase().startsWith('IDR')) {{
        const numPart = val.substring(3).trim();
        return 'IDR ' + numPart;
      }}
      return val;
    }}

    function escapeHtml(text) {{
      const div = document.createElement('div');
      div.textContent = text;
      return div.innerHTML;
    }}

    // Initial Render
    renderLeaderboard(currentDonors);

    // ========================================================================
    // REALTIME LIVE OVERLAY AUTO-SYNC (WebSocket + API Polling)
    // ========================================================================
    const RECIPIENT_ID = 3811394092;
    const API_ENDPOINT = 'https://sociabuzz.com/pro/tribe/tribe_profile/get_detail_leaderboard_int_v4/' + RECIPIENT_ID;

    async function fetchLiveLeaderboard() {{
      try {{
        const resp = await fetch(API_ENDPOINT);
        if (!resp.ok) return;
        const json = await resp.json();
        if (json && json.datas) {{
          parseAndApplyDatas(json.datas);
        }}
      }} catch (err) {{
        // Silent catch for local testing / CORS fallback
      }}
    }}

    function parseAndApplyDatas(htmlString) {{
      try {{
        const parser = new DOMParser();
        const doc = parser.parseFromString(htmlString, 'text/html');
        const rows = doc.querySelectorAll('table.show_donate tbody tr');
        const freshDonors = [];

        rows.forEach((tr, idx) => {{
          const nameEl = tr.querySelector('.text-limit');
          const amountEl = tr.querySelector('.text-limit-r');
          if (nameEl && amountEl) {{
            freshDonors.push({{
              rank: idx + 1,
              name: nameEl.textContent.trim(),
              amount: amountEl.textContent.trim()
            }});
          }}
        }});

        if (freshDonors.length > 0) {{
          currentDonors = freshDonors;
          renderLeaderboard(currentDonors);
        }}
      }} catch (e) {{
        console.error('Error parsing live datas:', e);
      }}
    }}

    // WebSocket Realtime Connection
    let ws = null;
    function connectLiveSocket() {{
      try {{
        ws = new WebSocket('wss://wss.sociabuzz.com:8901');

        ws.onopen = function () {{
          ws.send(JSON.stringify({{
            user_id: RECIPIENT_ID,
            recipient_id: RECIPIENT_ID,
            message: 'leaderboard'
          }}));
        }};

        ws.onmessage = function (event) {{
          try {{
            const data = JSON.parse(event.data);
            if (data.message === 'notif' || data.message === 'replay' || data.message === 'notif_ms') {{
              fetchLiveLeaderboard();
            }}
          }} catch (e) {{}}
        }};

        ws.onerror = function () {{}};

        ws.onclose = function () {{
          setTimeout(connectLiveSocket, 5000);
        }};
      }} catch (err) {{}}
    }}

    // Start Live Sync
    connectLiveSocket();
    // Periodic Auto-refresh fallback every 15 seconds
    setInterval(fetchLiveLeaderboard, 15000);

    // Subtle Web Audio Click Sound on CTA
    let audioCtx = null;
    function playTapSound() {{
      try {{
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(520, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(1040, audioCtx.currentTime + 0.05);
        gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.06);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.06);
      }} catch (e) {{}}
    }}

    document.querySelectorAll('.cta-push-btn, .nav-btn').forEach(el => {{
      el.addEventListener('pointerdown', playTapSound);
    }});
  </script>
</body>
</html>
'''

# Write to both 'top tank.html' (per exact user prompt) and 'Top Rank.html' (for casing & typos)
targets = [
    r'c:\Users\Rian\Desktop\Portfolio\top tank.html',
    r'c:\Users\Rian\Desktop\Portfolio\Top Rank.html',
    r'c:\Users\Rian\Desktop\Portfolio\top-rank.html'
]

for t in targets:
    with open(t, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Successfully generated {os.path.basename(t)}! Size: {len(html_content)} bytes")

