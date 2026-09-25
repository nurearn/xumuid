import os
import json
import base64

def get_base64_img(filepath, mime='image/png'):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            return f"data:{mime};base64," + base64.b64encode(f.read()).decode('utf-8')
    return ''

medal_1 = get_base64_img('medal_1st.png') or "https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@main/assets/1st%20place%20medal/3D/1st_place_medal_3d.png"
medal_2 = get_base64_img('medal_2nd.png') or "https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@main/assets/2nd%20place%20medal/3D/2nd_place_medal_3d.png"
medal_3 = get_base64_img('medal_3rd.png') or "https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@main/assets/3rd%20place%20medal/3D/3rd_place_medal_3d.png"
avatar_xumu = get_base64_img('xumuid_avatar.jpg', 'image/jpeg') or 'https://images.unsplash.com/photo-1566492031773-4f4e44671857?auto=format&fit=crop&w=150&q=80'

# Load JSON initial data
with open('top_gifters.json', 'r', encoding='utf-8') as f:
    top_gifters_data = json.load(f)

with open('penonton_setia.json', 'r', encoding='utf-8') as f:
    penonton_setia_data = json.load(f)

top_gifters_json_str = json.dumps(top_gifters_data)
penonton_setia_json_str = json.dumps(penonton_setia_data)

def generate_page(default_tab):
    is_gifter_default = (default_tab == 'gifts')
    page_title = "Top Gifter TikTok" if is_gifter_default else "Penonton Setia TikTok"
    target_filename = "TopGifter.html" if is_gifter_default else "Penonton Setia.html"

    html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <meta name="referrer" content="no-referrer">
  <title>{page_title} | xumu id Leaderboard</title>
  <meta name="description" content="Leaderboard Top Gifter & Penonton Setia TikTok @xumuid - Tampilan Neo-Brutalism dengan sinkronisasi realtime TikTok Live Center">
  <link rel="icon" href="{avatar_xumu}">

  <!-- Google Fonts: Space Grotesk & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&family=Space+Grotesk:wght@600;700;800;900&display=swap" rel="stylesheet">

  <!-- Font Awesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">

  <style>
    /* ======================================================================
       NEO-BRUTALISM LIGHT TOKENS (MATCHING TOP SULTAN / SOCIALBUZZ)
       ====================================================================== */
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
      --text-dim: #737373;
      
      --gold-rank: #fde047;
      --gold-glow: #eab308;
      --silver-rank: #e2e8f0;
      --silver-glow: #94a3b8;
      --bronze-rank: #fdba74;
      --bronze-glow: #ea580c;
      
      --tiktok-red: #fe2c55;
      --tiktok-cyan: #25f4ee;
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

    /* 1. Base Dot Grid Background */
    .bg-dots {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      background-image: radial-gradient(#121212 1.3px, transparent 1.3px);
      background-size: 24px 24px;
      opacity: 0.14;
    }}

    /* 2. Floating Neo-Brutalist Geometric Stickers / Decals */
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

    .sticker-pill-1 {{
      top: 48px;
      right: 4%;
      background: var(--tiktok-cyan);
      color: #121212;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 11px;
      letter-spacing: 0.05em;
      transform: rotate(8deg);
      animation: floatSlow 5s ease-in-out infinite alternate-reverse;
    }}

    .sticker-plus-1 {{
      top: 36%;
      left: 3%;
      width: 36px;
      height: 36px;
      background: var(--cyan-neo);
      border-radius: 10px;
      transform: rotate(15deg);
      font-size: 20px;
      animation: floatSlow 4.5s ease-in-out infinite alternate;
    }}

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

    .sticker-star-2 {{
      bottom: 75px;
      right: 5%;
      width: 46px;
      height: 46px;
      background: var(--pink-neo);
      border-radius: 50%;
      font-size: 22px;
      transform: rotate(18deg);
      animation: floatSlow 4.2s ease-in-out infinite alternate;
    }}

    @keyframes floatSlow {{
      0% {{ transform: translateY(0px) rotate(-5deg); }}
      100% {{ transform: translateY(-10px) rotate(5deg); }}
    }}

    /* Main Container */
    .app-container {{
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 680px;
      padding: 16px 14px 60px 14px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    /* Top Navigation */
    .top-nav-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      background: var(--card-white);
      border: 2.5px solid var(--border-black);
      box-shadow: var(--shadow-btn);
      border-radius: 14px;
      padding: 10px 14px;
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: var(--text-black);
    }}

    .brand-avatar {{
      width: 38px;
      height: 38px;
      border-radius: 50%;
      border: 2px solid var(--border-black);
      object-fit: cover;
      box-shadow: 2px 2px 0px #121212;
    }}

    .brand-text {{
      display: flex;
      flex-direction: column;
    }}

    .brand-name {{
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 15px;
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .brand-badge {{
      background: var(--tiktok-red);
      color: #fff;
      font-size: 9px;
      font-weight: 900;
      padding: 2px 6px;
      border-radius: 6px;
      border: 1px solid var(--border-black);
      box-shadow: 1px 1px 0px #121212;
    }}

    .brand-sub {{
      font-size: 11px;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .nav-buttons-group {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .nav-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--card-white);
      border: 2px solid var(--border-black);
      color: var(--text-black);
      padding: 6px 12px;
      border-radius: 10px;
      font-size: 12px;
      font-weight: 800;
      text-decoration: none;
      box-shadow: 3px 3px 0px #121212;
      transition: all 0.15s ease;
      cursor: pointer;
    }}

    .nav-btn:hover {{
      transform: translate(-1px, -1px);
      box-shadow: 5px 5px 0px #121212;
    }}

    .nav-btn:active {{
      transform: translate(2px, 2px);
      box-shadow: 1px 1px 0px #121212;
    }}

    .nav-btn.btn-sultan {{
      background: var(--gold-rank);
    }}

    /* Main Leaderboard Card */
    .neo-main-card {{
      background: var(--card-white);
      border: 3px solid var(--border-black);
      box-shadow: var(--shadow-card);
      border-radius: 20px;
      padding: 22px 18px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      position: relative;
    }}

    .leaderboard-header {{
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 6px;
    }}

    .header-badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--gold-rank);
      border: 2px solid var(--border-black);
      box-shadow: 2px 2px 0px #121212;
      padding: 4px 12px;
      border-radius: 999px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.04em;
    }}

    .leaderboard-main-title {{
      font-family: var(--font-display);
      font-size: 28px;
      font-weight: 900;
      letter-spacing: -0.03em;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .leaderboard-subtitle {{
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 600;
    }}

    /* ======================================================================
       TIKTOK LIVE CENTER INTERACTIVE TABS (Most Gifts vs Most watch time)
       ====================================================================== */
    .tiktok-tabs-container {{
      display: flex;
      border-bottom: 2.5px solid var(--border-black);
      margin-top: 4px;
      position: relative;
    }}

    .tiktok-tab-btn {{
      flex: 1;
      padding: 12px 16px;
      background: transparent;
      border: none;
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 800;
      color: var(--text-dim);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      position: relative;
      transition: all 0.2s ease;
    }}

    .tiktok-tab-btn:hover {{
      color: var(--text-black);
    }}

    .tiktok-tab-btn.active {{
      color: var(--text-black);
    }}

    .tiktok-tab-btn.active::after {{
      content: '';
      position: absolute;
      bottom: -2.5px;
      left: 15%;
      right: 15%;
      height: 4px;
      background: var(--tiktok-red);
      border-radius: 4px 4px 0 0;
    }}

    /* Filter Controls Row: Total/Increase + Dropdown (60 days) */
    .filter-controls-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 4px;
    }}

    .pill-filter-group {{
      display: flex;
      background: #f1f5f9;
      border: 2px solid var(--border-black);
      border-radius: 999px;
      padding: 3px;
      box-shadow: 2px 2px 0px #121212;
    }}

    .pill-btn {{
      background: transparent;
      border: none;
      border-radius: 999px;
      padding: 5px 14px;
      font-family: var(--font-sans);
      font-size: 12px;
      font-weight: 800;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .pill-btn.active {{
      background: #121212;
      color: #ffffff;
    }}

    /* Dropdown 60 days */
    .dropdown-wrapper {{
      position: relative;
    }}

    .dropdown-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--card-white);
      border: 2px solid var(--border-black);
      box-shadow: 3px 3px 0px #121212;
      padding: 6px 14px;
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 12px;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .dropdown-btn:hover {{
      transform: translate(-1px, -1px);
      box-shadow: 4px 4px 0px #121212;
    }}

    .dropdown-menu {{
      display: none;
      position: absolute;
      top: calc(100% + 6px);
      right: 0;
      background: #1e212d;
      color: #ffffff;
      border: 2px solid var(--border-black);
      box-shadow: 4px 4px 0px #121212;
      border-radius: 12px;
      padding: 6px;
      min-width: 140px;
      z-index: 50;
      flex-direction: column;
      gap: 2px;
    }}

    .dropdown-menu.open {{
      display: flex;
    }}

    .dropdown-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      color: #cbd5e1;
      cursor: pointer;
      transition: background 0.15s;
    }}

    .dropdown-item:hover {{
      background: #2d3246;
      color: #ffffff;
    }}

    .dropdown-item.selected {{
      color: #ffffff;
      font-weight: 800;
    }}

    /* ======================================================================
       PODIUM SECTION (TOP 1, 2, 3) - NEO-BRUTALIST RADIANT
       ====================================================================== */
    .podium-section {{
      display: grid;
      grid-template-columns: 1fr 1.15fr 1fr;
      gap: 12px;
      align-items: end;
      margin-top: 8px;
      margin-bottom: 6px;
    }}

    .podium-col {{
      background: var(--card-white);
      border: 2.5px solid var(--border-black);
      box-shadow: var(--shadow-btn);
      border-radius: 16px;
      padding: 16px 8px 14px 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
      overflow: hidden;
      transition: transform 0.2s ease;
    }}

    .podium-col:hover {{
      transform: translateY(-3px);
    }}

    .podium-col.rank-1 {{
      order: 2;
      background: #fffef2;
      border-color: var(--border-black);
      box-shadow: 6px 6px 0px #121212;
      padding-top: 24px;
      padding-bottom: 18px;
    }}

    .podium-col.rank-2 {{
      order: 1;
      background: #fafafa;
    }}

    .podium-col.rank-3 {{
      order: 3;
      background: #fff8f5;
    }}

    /* Radiant Halo & Spinning Rays on Rank 1 */
    .podium-col.rank-1 .radiant-rays {{
      position: absolute;
      top: 56px;
      left: 50%;
      width: 140px;
      height: 140px;
      transform: translate(-50%, -50%);
      border-radius: 50%;
      background: repeating-conic-gradient(
        from 0deg,
        rgba(254, 240, 138, 0.45) 0deg 15deg,
        transparent 15deg 30deg
      );
      animation: spinRays 12s linear infinite;
      pointer-events: none;
      z-index: 0;
    }}

    .podium-col.rank-1 .radiant-halo {{
      position: absolute;
      top: 56px;
      left: 50%;
      width: 110px;
      height: 110px;
      transform: translate(-50%, -50%);
      border-radius: 50%;
      background: radial-gradient(circle, rgba(250, 204, 21, 0.5) 0%, transparent 70%);
      pointer-events: none;
      z-index: 0;
    }}

    @keyframes spinRays {{
      0% {{ transform: translate(-50%, -50%) rotate(0deg); }}
      100% {{ transform: translate(-50%, -50%) rotate(360deg); }}
    }}

    .avatar-wrapper {{
      position: relative;
      width: 66px;
      height: 66px;
      margin-bottom: 12px;
      z-index: 1;
    }}

    .podium-col.rank-1 .avatar-wrapper {{
      width: 80px;
      height: 80px;
      margin-bottom: 14px;
    }}

    .podium-avatar {{
      width: 100%;
      height: 100%;
      border-radius: 50%;
      border: 2.5px solid var(--border-black);
      object-fit: cover;
      box-shadow: 2px 2px 0px #121212;
      background: #fde047;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-display);
      font-size: 24px;
      font-weight: 900;
      color: #121212;
    }}

    .crown-icon {{
      position: absolute;
      top: -16px;
      left: 50%;
      transform: translateX(-50%);
      color: #ca8a04;
      font-size: 20px;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.4));
      animation: crownBounce 2s ease-in-out infinite alternate;
    }}

    @keyframes crownBounce {{
      0% {{ transform: translateX(-50%) translateY(0); }}
      100% {{ transform: translateX(-50%) translateY(-4px); }}
    }}

    .medal-img {{
      position: absolute;
      bottom: -6px;
      right: -6px;
      width: 28px;
      height: 28px;
      object-fit: contain;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
    }}

    .podium-col.rank-1 .medal-img {{
      width: 34px;
      height: 34px;
      bottom: -8px;
      right: -8px;
    }}

    .rank-pill {{
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 900;
      padding: 2px 8px;
      border-radius: 999px;
      border: 1.5px solid var(--border-black);
      box-shadow: 1.5px 1.5px 0px #121212;
      margin-bottom: 6px;
      z-index: 1;
    }}

    .podium-col.rank-1 .rank-pill {{
      background: var(--gold-rank);
      color: #121212;
    }}

    .podium-col.rank-2 .rank-pill {{
      background: var(--silver-rank);
      color: #121212;
    }}

    .podium-col.rank-3 .rank-pill {{
      background: var(--bronze-rank);
      color: #121212;
    }}

    .podium-user-name {{
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 13.5px;
      color: var(--text-black);
      width: 100%;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      z-index: 1;
    }}

    .fan-club-badge {{
      display: inline-flex;
      align-items: center;
      gap: 3px;
      background: #ffe4e6;
      border: 1px solid #f43f5e;
      color: #e11d48;
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 9.5px;
      font-weight: 800;
      margin-top: 3px;
      margin-bottom: 8px;
      z-index: 1;
    }}

    .fan-club-badge.silver {{
      background: #f1f5f9;
      border-color: #94a3b8;
      color: #475569;
    }}

    .podium-score-box {{
      background: #f8fafc;
      border: 2px solid var(--border-black);
      box-shadow: 2px 2px 0px #121212;
      padding: 5px 8px;
      border-radius: 8px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 1;
    }}

    .podium-score-val {{
      font-family: var(--font-display);
      font-weight: 900;
      font-size: 14.5px;
      color: #0284c7;
    }}

    .podium-col.rank-1 .podium-score-val {{
      color: #b45309;
      font-size: 16px;
    }}

    .podium-score-sub {{
      font-size: 9px;
      font-weight: 800;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    /* ======================================================================
       RANKS 4 - 10 LIST (NEO-BRUTALIST CARDS)
       ====================================================================== */
    .ranks-list-container {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-top: 4px;
    }}

    .rank-card-row {{
      background: var(--card-white);
      border: 2.5px solid var(--border-black);
      box-shadow: 3px 3px 0px #121212;
      border-radius: 12px;
      padding: 10px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      transition: all 0.15s ease;
    }}

    .rank-card-row:hover {{
      transform: translate(-1px, -1px);
      box-shadow: 5px 5px 0px #121212;
    }}

    .rank-card-left {{
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 0;
    }}

    .rank-number-box {{
      font-family: var(--font-display);
      font-weight: 900;
      font-size: 15px;
      color: var(--text-muted);
      width: 24px;
      text-align: center;
    }}

    .rank-avatar-img {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      border: 2px solid var(--border-black);
      object-fit: cover;
      box-shadow: 2px 2px 0px #121212;
      background: #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 16px;
      color: #121212;
      flex-shrink: 0;
    }}

    .rank-user-info {{
      display: flex;
      flex-direction: column;
      min-width: 0;
    }}

    .rank-username-text {{
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 14px;
      color: var(--text-black);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .rank-card-right {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }}

    .rank-metric-badge {{
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      background: #f8fafc;
      border: 2px solid var(--border-black);
      box-shadow: 2px 2px 0px #121212;
      padding: 4px 10px;
      border-radius: 8px;
    }}

    .rank-metric-val {{
      font-family: var(--font-display);
      font-weight: 900;
      font-size: 14px;
      color: #0284c7;
    }}

    .rank-metric-sub {{
      font-size: 9px;
      font-weight: 800;
      color: var(--text-dim);
    }}

    /* Sync Indicator Status */
    .sync-status-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
      padding-top: 10px;
      border-top: 2px dashed #cbd5e1;
      font-size: 11.5px;
      font-weight: 700;
      color: var(--text-muted);
    }}

    .live-pulse-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #dcfce7;
      border: 1.5px solid #16a34a;
      color: #15803d;
      padding: 3px 8px;
      border-radius: 999px;
    }}

    .pulse-dot {{
      width: 7px;
      height: 7px;
      background: #16a34a;
      border-radius: 50%;
      animation: pulseAnim 1.5s infinite;
    }}

    @keyframes pulseAnim {{
      0%, 100% {{ transform: scale(0.9); opacity: 0.7; }}
      50% {{ transform: scale(1.3); opacity: 1; }}
    }}

    @media (max-width: 480px) {{
      .podium-section {{
        gap: 6px;
      }}
      .avatar-wrapper {{
        width: 52px;
        height: 52px;
      }}
      .podium-col.rank-1 .avatar-wrapper {{
        width: 66px;
        height: 66px;
      }}
      .podium-user-name {{
        font-size: 12px;
      }}
      .podium-score-val {{
        font-size: 12.5px;
      }}
    }}
  </style>
</head>
<body>
  <div class="bg-dots"></div>

  <!-- Geometric Neo Stickers -->
  <div class="neo-decorations">
    <div class="neo-sticker sticker-star-1">⭐</div>
    <div class="neo-sticker sticker-pill-1">🔴 TIKTOK LIVE</div>
    <div class="neo-sticker sticker-plus-1">✦</div>
    <div class="neo-sticker sticker-stripes">/// TOP RANK ///</div>
    <div class="neo-sticker sticker-star-2">👑</div>
  </div>

  <div class="app-container">
    <!-- Top Navbar -->
    <header class="top-nav-bar">
      <a href="index.html" class="nav-brand">
        <img src="{avatar_xumu}" alt="xumu id" class="brand-avatar" referrerpolicy="no-referrer">
        <div class="brand-text">
          <span class="brand-name">xumu id <span class="brand-badge">LIVE</span></span>
          <span class="brand-sub">TikTok Leaderboard</span>
        </div>
      </a>
      <div class="nav-buttons-group">
        <a href="Top Rank.html" class="nav-btn btn-sultan" title="Leaderboard Sociabuzz">
          <i class="fa-solid fa-crown" style="color: #b45309;"></i> Top Sultan
        </a>
      </div>
    </header>

    <!-- Main Leaderboard Card -->
    <article class="neo-main-card">
      <div class="leaderboard-header">
        <div class="header-badge-pill">
          <i class="fa-brands fa-tiktok"></i>
          <span>VIEWER RANKING SYSTEM</span>
        </div>
        <h1 class="leaderboard-main-title" id="pageTitleDisplay">
          <span>Viewer Ranking</span>
          <i class="fa-solid fa-trophy" style="color: #eab308;"></i>
        </h1>
        <p class="leaderboard-subtitle">Daftar Peringkat Resmi Penonton & Donatur Live @xumuid</p>
      </div>

      <!-- TikTok Live Center Tabs: Most Gifts vs Most watch time -->
      <div class="tiktok-tabs-container">
        <button class="tiktok-tab-btn {'active' if is_gifter_default else ''}" id="tabGiftsBtn" onclick="switchMainTab('gifts')">
          <i class="fa-solid fa-gift" style="color: var(--tiktok-red)"></i> Most Gifts
        </button>
        <button class="tiktok-tab-btn {'active' if not is_gifter_default else ''}" id="tabWatchBtn" onclick="switchMainTab('watch')">
          <i class="fa-solid fa-stopwatch" style="color: var(--tiktok-cyan)"></i> Most watch time
        </button>
      </div>

      <!-- Filter Controls: Total / Increase + 60 days Dropdown -->
      <div class="filter-controls-row">
        <div class="pill-filter-group">
          <button class="pill-btn active" onclick="switchSubFilter(this, 'total')">Total</button>
          <button class="pill-btn" onclick="switchSubFilter(this, 'increase')">Increase</button>
        </div>

        <div class="dropdown-wrapper">
          <button class="dropdown-btn" onclick="toggleDropdown(event)">
            <span id="selectedPeriodText">60 days</span>
            <i class="fa-solid fa-chevron-down" style="font-size: 10px;"></i>
          </button>
          <div class="dropdown-menu" id="periodDropdownMenu">
            <div class="dropdown-item" onclick="selectPeriod('Latest LIVE')">
              <span>Latest LIVE</span>
            </div>
            <div class="dropdown-item" onclick="selectPeriod('7 days')">
              <span>7 days</span>
            </div>
            <div class="dropdown-item" onclick="selectPeriod('28 days')">
              <span>28 days</span>
            </div>
            <div class="dropdown-item selected" onclick="selectPeriod('60 days')">
              <span>60 days</span>
              <i class="fa-solid fa-check" style="font-size: 11px; color: var(--tiktok-cyan)"></i>
            </div>
          </div>
        </div>
      </div>

      <!-- Podium Top 1, 2, 3 -->
      <div class="podium-section" id="podiumSection">
        <!-- Rendered dynamically -->
      </div>

      <!-- List Peringkat 4 - 10 -->
      <div class="ranks-list-container" id="ranksListContainer">
        <!-- Rendered dynamically -->
      </div>

      <!-- Sync Status & Timestamp -->
      <div class="sync-status-footer">
        <div class="live-pulse-badge">
          <span class="pulse-dot"></span>
          <span id="syncStatusText">REALTIME SYNC AKTIF</span>
        </div>
        <div>
          <span>Terakhir diperbarui: </span>
          <strong id="lastUpdatedClock">Baru saja</strong>
        </div>
      </div>
    </article>
  </div>

  <script>
    // Initial Verified Data (10 Boss Ranks each)
    const giftersData = {top_gifters_json_str};
    const viewersData = {penonton_setia_json_str};

    let activeTab = "{default_tab}"; // 'gifts' or 'watch'
    let activeSubFilter = 'total';
    let activePeriod = '60 days';

    const MEDAL_1 = "{medal_1}";
    const MEDAL_2 = "{medal_2}";
    const MEDAL_3 = "{medal_3}";

    function formatNumber(num) {{
      return new Intl.NumberFormat('id-ID').format(num);
    }}

    function handleAvatarError(img, name) {{
      img.onerror = null;
      const initial = name ? name.charAt(0).toUpperCase() : 'U';
      const colors = ['#f472b6', '#38bdf8', '#fb923c', '#a78bfa', '#4ade80'];
      const bg = colors[name.charCodeAt(0) % colors.length];
      img.outerHTML = `<div class="${{img.className}}" style="background: ${{bg}}; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #121212;">${{initial}}</div>`;
    }}

    function renderView() {{
      const isGifts = (activeTab === 'gifts');
      const items = isGifts ? (giftersData.gifters || []) : (viewersData.viewers || []);
      const metricLabel = isGifts ? 'Coins' : 'Jam Nonton';
      const metricSub = isGifts ? 'TOTAL COINS' : 'WATCH TIME';

      const podiumEl = document.getElementById('podiumSection');
      const listEl = document.getElementById('ranksListContainer');

      const top1 = items.find(x => x.rank === 1);
      const top2 = items.find(x => x.rank === 2);
      const top3 = items.find(x => x.rank === 3);
      const rest = items.filter(x => x.rank > 3);

      function renderPodiumCard(user, rank, medalSrc) {{
        if (!user) return '';
        const isFirst = (rank === 1);
        const score = isGifts ? `${{formatNumber(user.coins)}}` : (user.watch_time_str || `${{user.watch_time_minutes}}m`);
        const badgeHtml = user.badge ? `<span class="fan-club-badge ${{user.badge_type === 'fan_club_silver' ? 'silver' : ''}}">${{user.badge}}</span>` : '';
        const avatarSrc = user.avatar || `https://api.dicebear.com/7.x/bottts/svg?seed=${{encodeURIComponent(user.username)}}`;

        return `
          <div class="podium-col rank-${{rank}}">
            ${{isFirst ? '<div class="radiant-rays"></div><div class="radiant-halo"></div>' : ''}}
            <div class="avatar-wrapper">
              ${{isFirst ? '<i class="fa-solid fa-crown crown-icon"></i>' : ''}}
              <img src="${{avatarSrc}}" class="podium-avatar" alt="${{user.username}}" referrerpolicy="no-referrer" onerror="handleAvatarError(this, '${{user.username}}')">
              <img src="${{medalSrc}}" class="medal-img" alt="Medal Rank ${{rank}}">
            </div>
            <span class="rank-pill">#${{rank}}</span>
            <span class="podium-user-name" title="${{user.display_name || user.username}}">${{user.display_name || user.username}}</span>
            ${{badgeHtml}}
            <div class="podium-score-box">
              <span class="podium-score-val">${{score}}</span>
              <span class="podium-score-sub">${{metricSub}}</span>
            </div>
          </div>
        `;
      }}

      podiumEl.innerHTML = `
        ${{renderPodiumCard(top2, 2, MEDAL_2)}}
        ${{renderPodiumCard(top1, 1, MEDAL_1)}}
        ${{renderPodiumCard(top3, 3, MEDAL_3)}}
      `;

      listEl.innerHTML = rest.map(u => {{
        const score = isGifts ? `${{formatNumber(u.coins)}} Coins` : (u.watch_time_str || `${{u.watch_time_minutes}}m`);
        const badgeHtml = u.badge ? `<span class="fan-club-badge" style="margin: 0; margin-top: 2px;">${{u.badge}}</span>` : '';
        const avatarSrc = u.avatar || `https://api.dicebear.com/7.x/bottts/svg?seed=${{encodeURIComponent(u.username)}}`;

        return `
          <div class="rank-card-row">
            <div class="rank-card-left">
              <span class="rank-number-box">${{u.rank}}</span>
              <img src="${{avatarSrc}}" class="rank-avatar-img" alt="${{u.username}}" referrerpolicy="no-referrer" onerror="handleAvatarError(this, '${{u.username}}')">
              <div class="rank-user-info">
                <span class="rank-username-text">${{u.display_name || u.username}}</span>
                ${{badgeHtml}}
              </div>
            </div>
            <div class="rank-card-right">
              <div class="rank-metric-badge">
                <span class="rank-metric-val">${{score}}</span>
                <span class="rank-metric-sub">${{metricSub}}</span>
              </div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    function switchMainTab(tab) {{
      activeTab = tab;
      document.getElementById('tabGiftsBtn').classList.toggle('active', tab === 'gifts');
      document.getElementById('tabWatchBtn').classList.toggle('active', tab === 'watch');
      renderView();
    }}

    function switchSubFilter(btn, filter) {{
      activeSubFilter = filter;
      document.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderView();
    }}

    function toggleDropdown(e) {{
      e.stopPropagation();
      document.getElementById('periodDropdownMenu').classList.toggle('open');
    }}

    function selectPeriod(period) {{
      activePeriod = period;
      document.getElementById('selectedPeriodText').innerText = period;
      document.querySelectorAll('.dropdown-item').forEach(el => {{
        const isMatch = el.innerText.includes(period);
        el.classList.toggle('selected', isMatch);
        el.innerHTML = isMatch ? `<span>${{period}}</span><i class="fa-solid fa-check" style="font-size: 11px; color: var(--tiktok-cyan)"></i>` : `<span>${{el.innerText.trim()}}</span>`;
      }});
      document.getElementById('periodDropdownMenu').classList.remove('open');
    }}

    document.addEventListener('click', () => {{
      document.getElementById('periodDropdownMenu').classList.remove('open');
    }});

    // Polling sync from server if running
    async function pollSyncServer() {{
      try {{
        const giftersRes = await fetch('http://localhost:5000/api/top-gifters', {{ cache: 'no-store' }});
        if (giftersRes.ok) {{
          const fresh = await giftersRes.json();
          if (fresh.gifters && fresh.gifters.length > 0) {{
            giftersData.gifters = fresh.gifters;
          }}
        }}
        const viewersRes = await fetch('http://localhost:5000/api/penonton-setia', {{ cache: 'no-store' }});
        if (viewersRes.ok) {{
          const freshV = await viewersRes.json();
          if (freshV.viewers && freshV.viewers.length > 0) {{
            viewersData.viewers = freshV.viewers;
          }}
        }}
        renderView();
        document.getElementById('lastUpdatedClock').innerText = new Date().toLocaleTimeString('id-ID');
      }} catch (e) {{
        // Fallback silently
      }}
    }}

    renderView();
    setInterval(pollSyncServer, 5000);
  </script>
</body>
</html>'''

    with open(target_filename, 'w', encoding='utf-8') as out:
        out.write(html)
    print(f"Generated {target_filename} successfully ({len(html)} bytes)")

generate_page('gifts')
generate_page('watch')
