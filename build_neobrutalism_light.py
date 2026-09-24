import base64
import os

print("Building Neo-Brutalism Light xumuid Portfolio with White-Orange Gamepad Cover...")

avatar_path = r'c:\Users\Rian\Desktop\Portfolio\xumuid_avatar.jpg'
with open(avatar_path, 'rb') as f:
    avatar_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

cover_path = r'c:\Users\Rian\Desktop\Portfolio\xumuid_cover.jpg'
with open(cover_path, 'rb') as f:
    cover_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>xumu id (@xumuid) | Neo-Brutalist Light Hub</title>
  <meta name="description" content="Official link hub for xumu id (@xumuid) - Official Website, Support Me, Topup Coin TikTok, Tutorial Pasang Mod, Download Mod, Discord, YouTube, TikTok.">
  <link rel="icon" href="{avatar_b64}">

  <!-- Google Fonts: Space Grotesk & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Space+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">

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
      
      /* Neo-Brutalist Light Palette */
      --color-yellow: #fde047;
      --color-green: #86efac;
      --color-cyan: #7dd3fc;
      --color-orange: #fdba74;
      --color-coral: #fca5a5;
      --color-purple: #c4b5fd;
      --color-pink: #f9a8d4;
      --color-gold: #fbbf24;
      --color-official: #a5f3fc;
      
      --font-display: 'Space Grotesk', sans-serif;
      --font-sans: 'Plus Jakarta Sans', sans-serif;
      
      --shadow-card: 6px 6px 0px #121212;
      --shadow-btn: 3.5px 3.5px 0px #121212;
      --shadow-btn-hover: 5px 5px 0px #121212;
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

    /* 3D WebGL Background Canvas */
    #bg-canvas {{
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
    }}

    /* Retro Neo-Brutalist Dot Grid */
    .bg-dots {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      background-image: radial-gradient(#121212 1.2px, transparent 1.2px);
      background-size: 24px 24px;
      opacity: 0.12;
    }}

    /* Decorative Floating 3D Geometric Badges (Desktop/Tablet) */
    .deco-shape {{
      position: fixed;
      pointer-events: none;
      z-index: 0;
      border: 2px solid var(--border-black);
      box-shadow: 3px 3px 0px #121212;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 13px;
    }}
    .deco-shape-1 {{
      top: 30px;
      left: 20px;
      background: var(--color-yellow);
      border-radius: 8px;
      padding: 6px 12px;
      transform: rotate(-8deg);
      animation: floatA 6s ease-in-out infinite alternate;
    }}
    .deco-shape-2 {{
      top: 60px;
      right: 20px;
      background: var(--color-pink);
      border-radius: 999px;
      width: 44px;
      height: 44px;
      font-size: 18px;
      transform: rotate(12deg);
      animation: floatB 7s ease-in-out infinite alternate;
    }}
    .deco-shape-3 {{
      bottom: 40px;
      left: 15px;
      background: var(--color-cyan);
      border-radius: 50%;
      width: 40px;
      height: 40px;
      transform: rotate(6deg);
      animation: floatA 8s ease-in-out infinite alternate;
    }}

    @keyframes floatA {{
      0% {{ transform: translateY(0px) rotate(-8deg); }}
      100% {{ transform: translateY(-12px) rotate(-3deg); }}
    }}
    @keyframes floatB {{
      0% {{ transform: translateY(0px) rotate(12deg); }}
      100% {{ transform: translateY(14px) rotate(18deg); }}
    }}

    /* Mobile-first Main Wrapper */
    .page-wrapper {{
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 460px;
      padding: 24px 14px 48px 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 0 auto;
      box-sizing: border-box;
    }}

    /* ======================================================================
       MAIN NEO-BRUTALIST CARD (Light Theme with Header Cover)
       ====================================================================== */

    .neo-card {{
      width: 100%;
      max-width: 100%;
      background: var(--card-white);
      border: 3px solid var(--border-black);
      border-radius: 28px;
      box-shadow: var(--shadow-card);
      position: relative;
      box-sizing: border-box;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
      animation: cardEntrance 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) backwards;
      overflow: hidden;
    }}

    @keyframes cardEntrance {{
      0% {{
        opacity: 0;
        transform: translateY(24px) scale(0.97);
      }}
      100% {{
        opacity: 1;
        transform: translateY(0) scale(1);
      }}
    }}

    /* White & Orange Gamepad Neo-Brutalist Cover Banner */
    .card-cover-wrapper {{
      position: relative;
      width: 100%;
      height: 148px;
      background: #fff7ed;
      border-bottom: 3px solid var(--border-black);
      overflow: hidden;
    }}

    .card-cover-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
      display: block;
      transition: transform 0.4s ease;
    }}

    .neo-card:hover .card-cover-img {{
      transform: scale(1.04);
    }}

    /* Card Inner Body */
    .card-body {{
      padding: 0 18px 24px 18px;
      position: relative;
      width: 100%;
      box-sizing: border-box;
    }}

    /* Neo-Brutalist Sticker Pin on top-right of cover */
    .card-badge-pin {{
      position: absolute;
      top: 12px;
      right: 14px;
      background: var(--color-yellow);
      border: 2px solid var(--border-black);
      box-shadow: 2px 2px 0px #121212;
      border-radius: 999px;
      padding: 4px 12px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #121212;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      z-index: 10;
      user-select: none;
      animation: badgePop 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) 0.15s backwards;
    }}

    @keyframes badgePop {{
      0% {{
        opacity: 0;
        transform: scale(0.7);
      }}
      100% {{
        opacity: 1;
        transform: scale(1);
      }}
    }}

    .live-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: #16a34a;
      display: inline-block;
      animation: pulseLive 1.5s infinite;
    }}

    @keyframes pulseLive {{
      0%, 100% {{
        transform: scale(1);
        opacity: 1;
        box-shadow: 0 0 0 0 rgba(22, 163, 74, 0.7);
      }}
      50% {{
        transform: scale(1.25);
        opacity: 0.85;
        box-shadow: 0 0 0 4px rgba(22, 163, 74, 0);
      }}
    }}

    /* Profile Header - Overlapping Cover */
    .profile-header {{
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      margin-bottom: 20px;
      width: 100%;
    }}

    /* Avatar Wrapper with Animated Neo-Brutalist Running Border */
    .avatar-wrapper {{
      position: relative;
      width: 106px;
      height: 106px;
      margin: -53px auto 12px auto;
      z-index: 5;
      border-radius: 50%;
      box-shadow: 4px 4px 0px #121212;
    }}

    /* Running Animated Neo-Brutalism Border Ring */
    .avatar-running-border {{
      position: absolute;
      inset: -5px;
      border-radius: 50%;
      background: conic-gradient(
        #ff6b00 0deg 45deg,
        #121212 45deg 90deg,
        #fde047 90deg 135deg,
        #121212 135deg 180deg,
        #ff6b00 180deg 225deg,
        #121212 225deg 270deg,
        #38bdf8 270deg 315deg,
        #121212 315deg 360deg
      );
      animation: neoSpin 3.5s linear infinite;
      z-index: 1;
    }}

    @keyframes neoSpin {{
      from {{
        transform: rotate(0deg);
      }}
      to {{
        transform: rotate(360deg);
      }}
    }}

    .avatar-frame {{
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      border: 3.5px solid var(--border-black);
      overflow: hidden;
      background: #000000;
      transition: transform 0.25s ease;
      z-index: 2;
    }}

    .avatar-frame:hover {{
      transform: scale(1.04);
    }}

    .avatar-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}

    .avatar-online-dot {{
      position: absolute;
      bottom: 2px;
      right: 2px;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: #22c55e;
      border: 3px solid var(--border-black);
      box-shadow: 2px 2px 0px #121212;
      z-index: 6;
      animation: pulseAvatar 2s infinite;
    }}

    @keyframes pulseAvatar {{
      0%, 100% {{
        transform: scale(1);
      }}
      50% {{
        transform: scale(1.12);
      }}
    }}

    .profile-title {{
      font-family: var(--font-display);
      font-size: 30px;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: var(--text-black);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
    }}

    .verified-badge {{
      width: 24px;
      height: 24px;
      color: #0284c7;
      fill: currentColor;
    }}

    .profile-tag-pill {{
      display: inline-block;
      font-family: var(--font-display);
      font-size: 13px;
      font-weight: 700;
      color: #121212;
      background: #f1f5f9;
      border: 2px solid var(--border-black);
      box-shadow: 2px 2px 0px #121212;
      padding: 4px 14px;
      border-radius: 999px;
      margin-bottom: 10px;
      max-width: 100%;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .tag-row {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      justify-content: center;
      margin-top: 2px;
      width: 100%;
    }}

    .mini-sticker {{
      font-size: 11px;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: 6px;
      border: 1.5px solid var(--border-black);
      box-shadow: 1.5px 1.5px 0px #121212;
      background: #f8fafc;
      color: #1e293b;
      user-select: none;
      transition: transform 0.15s ease;
    }}

    .mini-sticker:hover {{
      transform: translateY(-2px);
    }}

    /* Section Label Header */
    .section-banner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      margin: 18px 0 12px 0;
      padding-bottom: 6px;
      border-bottom: 2px dashed #cbd5e1;
    }}

    .section-banner-title {{
      font-family: var(--font-display);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-black);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* 8 LINKS BADGE: Vivid Royal Blue, White text, Black border & shadow */
    .section-badge-counter {{
      background: #1d4ed8 !important;
      color: #ffffff !important;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.05em;
      padding: 3px 10px;
      border-radius: 999px;
      border: 2px solid #121212;
      box-shadow: 2px 2px 0px #121212;
      display: inline-flex !important;
      align-items: center;
      justify-content: center;
      white-space: nowrap;
      user-select: none;
      transition: transform 0.15s ease;
    }}

    .section-badge-counter:hover {{
      transform: scale(1.05);
    }}

    /* ======================================================================
       NEO-BRUTALIST LINK BUTTONS (Mobile Touch & 3D Tactile Physics)
       ====================================================================== */

    .links-stack {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      width: 100%;
      margin-bottom: 22px;
    }}

    .neo-link-btn {{
      position: relative;
      display: flex;
      align-items: center;
      width: 100%;
      box-sizing: border-box;
      min-height: 62px;
      padding: 9px 12px;
      border-radius: 16px;
      border: 2.5px solid var(--border-black);
      box-shadow: var(--shadow-btn);
      text-decoration: none;
      color: var(--text-black);
      transition: all 0.15s cubic-bezier(0.34, 1.56, 0.64, 1);
      cursor: pointer;
      user-select: none;
      overflow: hidden;
      transform-style: preserve-3d;
      animation: linkItemEntrance 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) backwards;
    }}

    .neo-link-btn:nth-child(1) {{ animation-delay: 0.04s; }}
    .neo-link-btn:nth-child(2) {{ animation-delay: 0.08s; }}
    .neo-link-btn:nth-child(3) {{ animation-delay: 0.12s; }}
    .neo-link-btn:nth-child(4) {{ animation-delay: 0.16s; }}
    .neo-link-btn:nth-child(5) {{ animation-delay: 0.20s; }}
    .neo-link-btn:nth-child(6) {{ animation-delay: 0.24s; }}
    .neo-link-btn:nth-child(7) {{ animation-delay: 0.28s; }}
    .neo-link-btn:nth-child(8) {{ animation-delay: 0.32s; }}

    @keyframes linkItemEntrance {{
      0% {{
        opacity: 0;
        transform: translateY(16px) scale(0.97);
      }}
      100% {{
        opacity: 1;
        transform: translateY(0) scale(1);
      }}
    }}

    /* 3D Tactile Push Down Physics */
    .neo-link-btn:hover {{
      transform: translate(-2px, -2px);
      box-shadow: var(--shadow-btn-hover);
    }}

    .neo-link-btn:active {{
      transform: translate(3px, 3px);
      box-shadow: var(--shadow-btn-active);
    }}

    /* Button Colors according to specified order */
    .btn-official {{
      background-color: var(--color-official); /* Cyan */
    }}
    .btn-support {{
      background-color: var(--color-green);    /* Mint Green */
    }}
    .btn-tiktok-coin {{
      background-color: var(--color-yellow);   /* Yellow */
    }}
    .btn-tutorial {{
      background-color: var(--color-orange);   /* Orange */
    }}
    .btn-mod {{
      background-color: var(--color-coral);    /* Coral / Red */
    }}
    .btn-discord {{
      background-color: var(--color-purple);   /* Lavender */
    }}
    .btn-tiktok {{
      background-color: var(--color-cyan);     /* Sky Blue */
    }}
    .btn-email {{
      background-color: #fed7aa;                /* Peach / Cream */
    }}

    /* Icon Box with solid borders */
    .btn-icon-square {{
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: #ffffff;
      border: 2px solid var(--border-black);
      box-shadow: 2px 2px 0px #121212;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-right: 10px;
      flex-shrink: 0;
      transition: transform 0.2s ease;
    }}

    .neo-link-btn:hover .btn-icon-square {{
      transform: scale(1.08) rotate(-3deg);
    }}

    .btn-icon-square svg {{
      width: 20px;
      height: 20px;
      fill: currentColor;
    }}

    /* Text block - MIN-WIDTH: 0 IS ESSENTIAL FOR FLEX TEXT TRUNCATION */
    .btn-text-block {{
      flex: 1 1 0%;
      min-width: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      overflow: hidden;
    }}

    .btn-main-title {{
      font-family: var(--font-display);
      font-size: 14px;
      font-weight: 800;
      color: #121212;
      letter-spacing: -0.01em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .btn-sub-title {{
      font-size: 11px;
      font-weight: 600;
      color: #262626;
      opacity: 0.85;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-top: 1px;
    }}

    /* Right Action Pill / Arrow */
    .btn-action-arrow {{
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: #ffffff;
      border: 2px solid var(--border-black);
      box-shadow: 1.5px 1.5px 0px #121212;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-left: 8px;
      flex-shrink: 0;
      transition: all 0.15s ease;
    }}

    .neo-link-btn:hover .btn-action-arrow {{
      transform: translateX(2px);
      background: #121212;
      color: #ffffff;
    }}

    /* ======================================================================
       BOTTOM SOCIAL ICONS ROW (Neo-Brutalist Light Style)
       ====================================================================== */

    .social-row {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin-top: 6px;
      width: 100%;
    }}

    .social-btn {{
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: #ffffff;
      border: 2.5px solid var(--border-black);
      box-shadow: 3px 3px 0px #121212;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #121212;
      text-decoration: none;
      transition: all 0.15s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .social-btn:hover {{
      transform: translate(-2px, -2px);
      box-shadow: 5px 5px 0px #121212;
      background: var(--color-yellow);
    }}

    .social-btn:active {{
      transform: translate(2px, 2px);
      box-shadow: 1px 1px 0px #121212;
    }}

    .social-btn svg {{
      width: 20px;
      height: 20px;
      fill: currentColor;
    }}

    /* Footer - Cleaned per user request (no carrd.co) */
    .card-footer {{
      margin-top: 20px;
      text-align: center;
      font-size: 11.5px;
      font-weight: 600;
      color: #525252;
      user-select: none;
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

    /* ======================================================================
       RESPONSIVE DESIGN ACROSS ALL DEVICES
       ====================================================================== */
    @media (max-width: 480px) {{
      .page-wrapper {{
        padding: 16px 12px 36px 12px;
      }}
      .neo-card {{
        border-radius: 24px;
        box-shadow: 4px 4px 0px #121212;
      }}
      .card-cover-wrapper {{
        height: 124px;
      }}
      .card-body {{
        padding: 0 12px 18px 12px;
      }}
      .avatar-wrapper {{
        width: 96px;
        height: 96px;
        margin: -48px auto 10px auto;
      }}
      .card-badge-pin {{
        top: 10px;
        right: 10px;
        padding: 3px 10px;
        font-size: 10px;
      }}
      .profile-title {{
        font-size: 26px;
      }}
      .neo-link-btn {{
        min-height: 58px;
        padding: 8px 10px;
      }}
      .btn-icon-square {{
        width: 36px;
        height: 36px;
        margin-right: 8px;
      }}
      .btn-icon-square svg {{
        width: 18px;
        height: 18px;
      }}
      .btn-main-title {{
        font-size: 13px;
      }}
      .btn-sub-title {{
        font-size: 10.5px;
      }}
      .btn-action-arrow {{
        width: 28px;
        height: 28px;
        margin-left: 6px;
      }}
      .deco-shape {{
        display: none;
      }}
    }}

    @media (max-width: 360px) {{
      .page-wrapper {{
        padding: 12px 8px 28px 8px;
      }}
      .neo-card {{
        border-radius: 20px;
      }}
      .card-cover-wrapper {{
        height: 110px;
      }}
      .card-body {{
        padding: 0 10px 16px 10px;
      }}
      .avatar-wrapper {{
        width: 88px;
        height: 88px;
        margin: -44px auto 8px auto;
      }}
      .btn-sub-title {{
        display: none;
      }}
      .mini-sticker {{
        font-size: 10px;
        padding: 2px 6px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Interactive 3D Background Canvas -->
  <canvas id="bg-canvas"></canvas>

  <!-- Neo-Brutalist Dot Grid Layer -->
  <div class="bg-dots" aria-hidden="true"></div>

  <!-- Decorative 3D Floating Stickers -->
  <div class="deco-shape deco-shape-1" aria-hidden="true">★ POPULAR</div>
  <div class="deco-shape deco-shape-2" aria-hidden="true">⚡</div>
  <div class="deco-shape deco-shape-3" aria-hidden="true"></div>

  <!-- Mobile-first Page Wrapper -->
  <main class="page-wrapper">

    <!-- ======================================================================
         NEO-BRUTALISM LIGHT CARD WITH COVER BANNER
         ====================================================================== -->
    <article class="neo-card" id="interactive-card">

      <!-- White & Orange 3D Gamepad Neo-Brutalist Cover Banner -->
      <div class="card-cover-wrapper">
        <img class="card-cover-img" src="{cover_b64}" alt="Sampul 3D Gamepad xumu id" width="960" height="540">

        <!-- Neo-brutalist sticker badge on cover corner -->
        <div class="card-badge-pin">
          <span class="live-dot"></span>
          <span>LIVE NOW</span>
        </div>
      </div>

      <!-- Card Inner Body -->
      <div class="card-body">

        <!-- Profile Header (Overlaps Cover Banner) -->
        <header class="profile-header">
          <div class="avatar-wrapper">
            <!-- Animated Running Neo-Brutalist Border Ring -->
            <div class="avatar-running-border" aria-hidden="true"></div>
            <div class="avatar-frame">
              <img class="avatar-img" src="{avatar_b64}" alt="Foto Profil xumu id" width="104" height="104">
            </div>
            <!-- Online Status Indicator -->
            <div class="avatar-online-dot" title="Online Sekarang" aria-label="Status Online"></div>
          </div>

          <h1 class="profile-title">
            xumu id
            <!-- Verified Checkmark Badge -->
            <svg class="verified-badge" viewBox="0 0 24 24">
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
            </svg>
          </h1>

          <span class="profile-tag-pill">@xumuid · Creator & Modder</span>

          <div class="tag-row">
            <span class="mini-sticker">🎮 GAMING</span>
            <span class="mini-sticker">⚡ CUSTOM MODS</span>
            <span class="mini-sticker">⭐ OFFICIAL</span>
          </div>
        </header>

        <!-- Section Banner -->
        <div class="section-banner">
          <span class="section-banner-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
            TAUTAN RESMI
          </span>
          <span class="section-badge-counter">8 LINKS</span>
        </div>

        <!-- ======================================================================
             NEO-BRUTALIST LINK BUTTONS (In User-Specified Order)
             ====================================================================== -->
        <div class="links-stack" role="list">

          <!-- 1. Official Website (nurearn.site) -->
          <a href="https://nurearn.site/" class="neo-link-btn btn-official" target="_blank" rel="noopener noreferrer" role="listitem">
            <div class="btn-icon-square" style="color: #0284c7;">
              <!-- Web Globe Icon -->
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="2" y1="12" x2="22" y2="12"></line>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
              </svg>
            </div>
            <div class="btn-text-block">
              <span class="btn-main-title">Official Website</span>
              <span class="btn-sub-title">nurearn.site · Portal Resmi & Update</span>
            </div>
            <div class="btn-action-arrow">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </div>
          </a>

          <!-- 2. Support Me (Link to Top Sultan Leaderboard) -->
          <a href="top tank.html" class="neo-link-btn btn-support" role="listitem">
            <div class="btn-icon-square" style="color: #16a34a;">
              <svg viewBox="0 0 24 24">
                <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
              </svg>
            </div>
            <div class="btn-text-block">
              <span class="btn-main-title">Support Me</span>
              <span class="btn-sub-title">Sociabuzz Tribe · Dukung karya xumuid</span>
            </div>
            <div class="btn-action-arrow">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </div>
          </a>

          <!-- 3. Topup Coin TikTok Murah -->
          <a href="https://www.tiktok.com/coin?lang=id-ID" class="neo-link-btn btn-tiktok-coin" target="_blank" rel="noopener noreferrer" role="listitem">
            <div class="btn-icon-square" style="color: #d97706;">
              <!-- Golden Coin Icon -->
              <svg viewBox="0 0 24 24">
                <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2" fill="#fef08a"/>
                <path d="M12 7v10M9.5 9.5h5a1.5 1.5 0 0 1 0 3h-5a1.5 1.5 0 0 0 0 3h5" stroke="#b45309" stroke-width="2" stroke-linecap="round"/>
              </svg>
            </div>
            <div class="btn-text-block">
              <span class="btn-main-title">Topup Coin TikTok Murah</span>
              <span class="btn-sub-title">Beli koin resmi TikTok harga hemat & kilat</span>
            </div>
            <div class="btn-action-arrow">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </div>
          </a>

          <!-- 4. Tutorial Pasang Mod (YouTube Video Guides) -->
          <a href="https://youtube.com/@xumuid?si=JSR4qqEwBjeJhBUU" class="neo-link-btn btn-tutorial" target="_blank" rel="noopener noreferrer" role="listitem">
            <div class="btn-icon-square" style="color: #ea580c;">
              <svg viewBox="0 0 24 24">
                <path d="M21.58 7.19a2.7 2.7 0 0 0-1.9-1.9C18 4.75 12 4.75 12 4.75s-6 0-7.68.54a2.7 2.7 0 0 0-1.9 1.9A28.3 28.3 0 0 0 2 12a28.3 28.3 0 0 0 .42 4.81 2.7 2.7 0 0 0 1.9 1.9c1.68.54 7.68.54 7.68.54s6 0 7.68-.54a2.7 2.7 0 0 0 1.9-1.9A28.3 28.3 0 0 0 22 12a28.3 28.3 0 0 0-.42-4.81zM10 15V9l5.2 3z"/>
              </svg>
            </div>
            <div class="btn-text-block">
              <span class="btn-main-title">Tutorial Pasang Mod</span>
              <span class="btn-sub-title">Panduan video lengkap langkah demi langkah</span>
            </div>
            <div class="btn-action-arrow">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </div>
          </a>

          <!-- 5. Download Mod (Trakteer Shop) -->
          <a href="https://trakteer.id/xumuid/shop" class="neo-link-btn btn-mod" target="_blank" rel="noopener noreferrer" role="listitem">
            <div class="btn-icon-square" style="color: #dc2626;">
              <svg viewBox="0 0 24 24">
                <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/>
              </svg>
            </div>
            <div class="btn-text-block">
              <span class="btn-main-title">Download Mod</span>
              <span class="btn-sub-title">Trakteer Shop · File mod eksklusif xumuid</span>
            </div>
            <div class="btn-action-arrow">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </div>
          </a>

          <!-- 6. Join Discord Community -->
          <a href="https://discord.gg/cx5xjEmRzh" class="neo-link-btn btn-discord" target="_blank" rel="noopener noreferrer" role="listitem">
            <div class="btn-icon-square" style="color: #5865f2;">
              <svg viewBox="0 0 24 24">
                <path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.893.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/>
              </svg>
            </div>
            <div class="btn-text-block">
              <span class="btn-main-title">Join Discord Community</span>
              <span class="btn-sub-title">Mabar, diskusi mod & nongkrong santai</span>
            </div>
            <div class="btn-action-arrow">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </div>
          </a>

          <!-- 7. Follow TikTok @xumuid -->
          <a href="https://www.tiktok.com/@xumuid?is_from_webapp=1&sender_device=pc" class="neo-link-btn btn-tiktok" target="_blank" rel="noopener noreferrer" role="listitem">
            <div class="btn-icon-square" style="color: #0284c7;">
              <svg viewBox="0 0 24 24">
                <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.88 2.89 2.89 0 0 1-2.89-2.88 2.89 2.89 0 0 1 2.89-2.89c.28 0 .55.04.81.1v-3.5a6.37 6.37 0 0 0-.81-.05A6.34 6.34 0 0 0 3 15.67 6.34 6.34 0 0 0 9.34 22a6.34 6.34 0 0 0 6.34-6.33V9.05a8.28 8.28 0 0 0 4.91 1.57v-3.5a4.86 4.86 0 0 1-1-.43z"/>
              </svg>
            </div>
            <div class="btn-text-block">
              <span class="btn-main-title">Follow TikTok @xumuid</span>
              <span class="btn-sub-title">Video gameplay, showcase & live streaming</span>
            </div>
            <div class="btn-action-arrow">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </div>
          </a>

          <!-- 8. Email Inquiries (xumu.id@gmail.com) -->
          <a href="mailto:xumu.id@gmail.com" class="neo-link-btn btn-email" role="listitem">
            <div class="btn-icon-square" style="color: #c2410c;">
              <svg viewBox="0 0 24 24">
                <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
              </svg>
            </div>
            <div class="btn-text-block">
              <span class="btn-main-title">Email Inquiries</span>
              <span class="btn-sub-title">xumu.id@gmail.com · Kolaborasi & Bisnis</span>
            </div>
            <div class="btn-action-arrow">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </div>
          </a>

        </div>

        <!-- Neo-Brutalist Social Dock -->
        <nav class="social-row" aria-label="Social media channels">
          <a href="https://discord.gg/cx5xjEmRzh" class="social-btn" target="_blank" rel="noopener noreferrer" title="Discord" aria-label="Discord">
            <svg viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.893.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
          </a>
          <a href="https://youtube.com/@xumuid?si=JSR4qqEwBjeJhBUU" class="social-btn" target="_blank" rel="noopener noreferrer" title="YouTube" aria-label="YouTube">
            <svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          </a>
          <a href="https://www.tiktok.com/@xumuid?is_from_webapp=1&sender_device=pc" class="social-btn" target="_blank" rel="noopener noreferrer" title="TikTok" aria-label="TikTok">
            <svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.88 2.89 2.89 0 0 1-2.89-2.88 2.89 2.89 0 0 1 2.89-2.89c.28 0 .55.04.81.1v-3.5a6.37 6.37 0 0 0-.81-.05A6.34 6.34 0 0 0 3 15.67 6.34 6.34 0 0 0 9.34 22a6.34 6.34 0 0 0 6.34-6.33V9.05a8.28 8.28 0 0 0 4.91 1.57v-3.5a4.86 4.86 0 0 1-1-.43z"/></svg>
          </a>
          <a href="mailto:xumu.id@gmail.com" class="social-btn" title="Email" aria-label="Email">
            <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          </a>
        </nav>

        <!-- Footer - Cleaned per user request (no carrd.co) -->
        <footer class="card-footer">
          <span>© 2026 xumu id</span>
        </footer>

      </div>
    </article>
  </main>

  <!-- Neo-Brutalist Toast -->
  <div class="neo-toast" id="toast">Tautan berhasil dibuka! 🚀</div>

  <!-- INTERACTIVE 3D PARTICLES & TACTILE PHYSICS -->
  <script>
    // 1. Light Neo-Brutalist 3D Floating Geometrics Canvas
    const canvas = document.getElementById('bg-canvas');
    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {{
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }});

    // Floating 3D Cubes & Polygons
    const shapes = [];
    const colors = ['#fde047', '#86efac', '#7dd3fc', '#fca5a5', '#c4b5fd', '#fdba74'];

    for (let i = 0; i < 16; i++) {{
      shapes.push({{
        x: Math.random() * width,
        y: Math.random() * height,
        size: Math.random() * 24 + 12,
        rot: Math.random() * Math.PI * 2,
        rotSpeed: (Math.random() - 0.5) * 0.02,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        color: colors[Math.floor(Math.random() * colors.length)],
        type: Math.floor(Math.random() * 3) // 0: square, 1: circle, 2: triangle
      }});
    }}

    const mouse = {{ x: width / 2, y: height / 2, tx: width / 2, ty: height / 2 }};
    window.addEventListener('mousemove', (e) => {{
      mouse.tx = e.clientX;
      mouse.ty = e.clientY;
    }});

    function render3DShapes() {{
      ctx.clearRect(0, 0, width, height);

      mouse.x += (mouse.tx - mouse.x) * 0.05;
      mouse.y += (mouse.ty - mouse.y) * 0.05;

      shapes.forEach(s => {{
        s.x += s.vx;
        s.y += s.vy;
        s.rot += s.rotSpeed;

        if (s.x < -40) s.x = width + 40;
        if (s.x > width + 40) s.x = -40;
        if (s.y < -40) s.y = height + 40;
        if (s.y > height + 40) s.y = -40;

        ctx.save();
        ctx.translate(s.x, s.y);
        ctx.rotate(s.rot);

        // Draw 3D shadow
        ctx.fillStyle = '#121212';
        if (s.type === 0) {{
          ctx.fillRect(-s.size/2 + 3, -s.size/2 + 3, s.size, s.size);
          ctx.fillStyle = s.color;
          ctx.fillRect(-s.size/2, -s.size/2, s.size, s.size);
          ctx.lineWidth = 2;
          ctx.strokeStyle = '#121212';
          ctx.strokeRect(-s.size/2, -s.size/2, s.size, s.size);
        }} else if (s.type === 1) {{
          ctx.beginPath();
          ctx.arc(3, 3, s.size/2, 0, Math.PI * 2);
          ctx.fill();
          ctx.fillStyle = s.color;
          ctx.beginPath();
          ctx.arc(0, 0, s.size/2, 0, Math.PI * 2);
          ctx.fill();
          ctx.lineWidth = 2;
          ctx.strokeStyle = '#121212';
          ctx.stroke();
        }} else {{
          // Triangle
          ctx.beginPath();
          ctx.moveTo(3, -s.size/2 + 3);
          ctx.lineTo(s.size/2 + 3, s.size/2 + 3);
          ctx.lineTo(-s.size/2 + 3, s.size/2 + 3);
          ctx.closePath();
          ctx.fill();
          ctx.fillStyle = s.color;
          ctx.beginPath();
          ctx.moveTo(0, -s.size/2);
          ctx.lineTo(s.size/2, s.size/2);
          ctx.lineTo(-s.size/2, s.size/2);
          ctx.closePath();
          ctx.fill();
          ctx.lineWidth = 2;
          ctx.strokeStyle = '#121212';
          ctx.stroke();
        }}

        ctx.restore();
      }});

      requestAnimationFrame(render3DShapes);
    }}
    render3DShapes();

    // 2. 3D Card Parallax on Desktop
    const mainCard = document.getElementById('interactive-card');
    if (mainCard && window.matchMedia('(hover: hover) and (min-width: 600px)').matches) {{
      window.addEventListener('mousemove', (e) => {{
        const cx = window.innerWidth / 2;
        const cy = window.innerHeight / 2;
        const dx = (e.clientX - cx) / cx;
        const dy = (e.clientY - cy) / cy;
        mainCard.style.transform = `perspective(1000px) rotateY(${{dx * 2}}deg) rotateX(${{-dy * 2}}deg)`;
      }});
      window.addEventListener('mouseleave', () => {{
        mainCard.style.transform = '';
      }});
    }}

    // 3. Button Click Tactile Audio Feedback (Optional Subtle Web Audio Synthesizer)
    let audioCtx = null;
    function playTapSound() {{
      try {{
        if (!audioCtx) {{
          audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }}
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(440, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.04);
        gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.05);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.05);
      }} catch (e) {{}}
    }}

    document.querySelectorAll('.neo-link-btn, .social-btn').forEach(btn => {{
      btn.addEventListener('pointerdown', playTapSound);
    }});
  </script>
</body>
</html>
'''

with open(r'c:\Users\Rian\Desktop\Portfolio\Dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(r'c:\Users\Rian\Desktop\Portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated Neo-Brutalism Light Dashboard.html & index.html with White-Orange Gamepad Cover! Size: {len(html_content)} bytes")
