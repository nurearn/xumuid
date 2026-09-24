import base64
import os

print("Building modern xumuid portfolio without top bar...")

# Read xumuid avatar
avatar_path = r'c:\Users\Rian\Desktop\Portfolio\xumuid_yt_avatar.jpg'
with open(avatar_path, 'rb') as f:
    avatar_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>xumu id (@xumuid) | Official Links</title>
  <meta name="description" content="Official link hub for xumu id (@xumuid) - Support Me, Tutorial Pasang Mod, Download Mod, Discord, YouTube, TikTok.">
  <link rel="icon" href="{avatar_b64}">

  <!-- Modern Google Fonts: Plus Jakarta Sans & Space Grotesk -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">

  <style>
    /* --- CSS RESET & MODERN DESIGN TOKENS --- */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    :root {{
      --bg-dark: #07090e;
      --card-bg: rgba(14, 19, 29, 0.72);
      --card-border: rgba(255, 255, 255, 0.08);
      --card-border-hover: rgba(56, 189, 248, 0.35);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-sub: #64748b;
      --accent-cyan: #38bdf8;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-blurple: #6366f1;
      --font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-display: 'Space Grotesk', sans-serif;
    }}

    html, body {{
      min-height: 100vh;
      font-family: var(--font-main);
      background-color: var(--bg-dark);
      color: var(--text-main);
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
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

    /* Ambient Gradient Orbs */
    .ambient-glow {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }}

    .glow-orb {{
      position: absolute;
      border-radius: 50%;
      filter: blur(100px);
      opacity: 0.28;
      animation: floatOrb 12s ease-in-out infinite alternate;
    }}

    .glow-orb-1 {{
      top: -10%;
      left: 20%;
      width: 480px;
      height: 480px;
      background: radial-gradient(circle, #38bdf8, #6366f1);
    }}

    .glow-orb-2 {{
      bottom: 5%;
      right: 15%;
      width: 420px;
      height: 420px;
      background: radial-gradient(circle, #10b981, #06b6d4);
      animation-delay: -5s;
    }}

    @keyframes floatOrb {{
      0% {{ transform: translate(0, 0) scale(1); }}
      50% {{ transform: translate(30px, 40px) scale(1.08); }}
      100% {{ transform: translate(-20px, 20px) scale(0.95); }}
    }}

    /* Main Content Wrapper */
    .page-wrapper {{
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 580px;
      padding: 40px 18px 60px 18px;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 0 auto;
    }}

    /* ======================================================================
       MODERN CENTRAL GLASS CARD
       ====================================================================== */

    .modern-card {{
      width: 100%;
      background: var(--card-bg);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid var(--card-border);
      border-radius: 28px;
      box-shadow: 
        0 24px 60px -12px rgba(0, 0, 0, 0.65),
        0 0 0 1px rgba(255, 255, 255, 0.04),
        0 0 40px rgba(56, 189, 248, 0.06);
      padding: 38px 26px 30px 26px;
      position: relative;
      overflow: hidden;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }}

    /* Card Top Glow Accent */
    .modern-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 15%;
      right: 15%;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.6), rgba(99, 102, 241, 0.6), transparent);
    }}

    /* Profile Header */
    .profile-header {{
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      margin-bottom: 26px;
      width: 100%;
    }}

    .avatar-wrapper {{
      position: relative;
      width: 108px;
      height: 108px;
      margin-bottom: 16px;
    }}

    .avatar-glow {{
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent-cyan), #818cf8, var(--accent-emerald));
      filter: blur(8px);
      opacity: 0.75;
      animation: rotateGlow 8s linear infinite;
    }}

    @keyframes rotateGlow {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}

    .avatar-img {{
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
      border: 2.5px solid rgba(255, 255, 255, 0.25);
      background: #000;
      z-index: 1;
      display: block;
    }}

    .avatar-badge {{
      position: absolute;
      bottom: 2px;
      right: 2px;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--accent-emerald);
      border: 2.5px solid #0b0f19;
      box-shadow: 0 0 8px rgba(16, 185, 129, 0.8);
      z-index: 2;
    }}

    .profile-name {{
      font-family: var(--font-display);
      font-size: 30px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
    }}

    .verified-icon {{
      width: 22px;
      height: 22px;
      color: var(--accent-cyan);
      fill: currentColor;
    }}

    .profile-tag {{
      font-size: 13.5px;
      font-weight: 500;
      color: var(--text-muted);
      margin-bottom: 12px;
    }}

    .badges-row {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      justify-content: center;
      margin-top: 4px;
    }}

    .badge-pill {{
      font-size: 11px;
      font-weight: 600;
      padding: 4px 12px;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #cbd5e1;
      letter-spacing: 0.02em;
    }}

    /* Section Divider */
    .section-divider {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      margin: 18px 0 14px 0;
      padding-bottom: 6px;
    }}

    .section-title {{
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--text-sub);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .section-count {{
      font-size: 10.5px;
      font-weight: 600;
      color: var(--accent-cyan);
      background: rgba(56, 189, 248, 0.1);
      padding: 2px 8px;
      border-radius: 999px;
      border: 1px solid rgba(56, 189, 248, 0.2);
    }}

    /* ======================================================================
       MODERN TAUTAN RESMI (BENTO CARDS)
       ====================================================================== */

    .links-grid {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      width: 100%;
      margin-bottom: 24px;
    }}

    .modern-link-card {{
      position: relative;
      display: flex;
      align-items: center;
      width: 100%;
      height: 68px;
      padding: 0 16px 0 12px;
      border-radius: 18px;
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.08);
      text-decoration: none;
      color: var(--text-main);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
      transition: all 0.24s cubic-bezier(0.34, 1.56, 0.64, 1);
      cursor: pointer;
      user-select: none;
      overflow: hidden;
      transform-style: preserve-3d;
    }}

    /* Card Sheen Light Reflection */
    .modern-link-card::after {{
      content: '';
      position: absolute;
      top: -50%;
      left: -60%;
      width: 40%;
      height: 200%;
      background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.08),
        transparent
      );
      transform: rotate(25deg);
      transition: transform 0.6s ease;
      pointer-events: none;
    }}

    .modern-link-card:hover::after {{
      transform: rotate(25deg) translate(500%, 0);
    }}

    .modern-link-card:hover {{
      transform: translateY(-3px) scale(1.015);
      background: rgba(255, 255, 255, 0.065);
      box-shadow: 0 12px 28px -6px rgba(0, 0, 0, 0.45);
    }}

    .modern-link-card:active {{
      transform: translateY(1px) scale(0.99);
    }}

    /* Card-specific accent glows on hover */
    .card-support:hover {{
      border-color: rgba(16, 185, 129, 0.4);
      box-shadow: 0 12px 28px -6px rgba(16, 185, 129, 0.25);
    }}
    .card-tutorial:hover {{
      border-color: rgba(245, 158, 11, 0.4);
      box-shadow: 0 12px 28px -6px rgba(245, 158, 11, 0.25);
    }}
    .card-mod:hover {{
      border-color: rgba(244, 63, 94, 0.4);
      box-shadow: 0 12px 28px -6px rgba(244, 63, 94, 0.25);
    }}
    .card-discord:hover {{
      border-color: rgba(99, 102, 241, 0.4);
      box-shadow: 0 12px 28px -6px rgba(99, 102, 241, 0.25);
    }}
    .card-tiktok:hover {{
      border-color: rgba(56, 189, 248, 0.4);
      box-shadow: 0 12px 28px -6px rgba(56, 189, 248, 0.25);
    }}
    .card-youtube:hover {{
      border-color: rgba(239, 68, 68, 0.4);
      box-shadow: 0 12px 28px -6px rgba(239, 68, 68, 0.25);
    }}
    .card-email:hover {{
      border-color: rgba(56, 189, 248, 0.4);
      box-shadow: 0 12px 28px -6px rgba(56, 189, 248, 0.25);
    }}

    /* Squircle Icon Wrap */
    .link-icon-box {{
      width: 44px;
      height: 44px;
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-right: 14px;
      flex-shrink: 0;
      position: relative;
      transition: transform 0.25s ease;
    }}

    .modern-link-card:hover .link-icon-box {{
      transform: scale(1.1);
    }}

    .link-icon-box svg {{
      width: 22px;
      height: 22px;
      fill: currentColor;
    }}

    /* Distinct Icon Color Accents */
    .icon-support {{
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}
    .icon-tutorial {{
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}
    .icon-mod {{
      background: rgba(244, 63, 94, 0.15);
      color: #fb7185;
      border: 1px solid rgba(244, 63, 94, 0.3);
    }}
    .icon-discord {{
      background: rgba(99, 102, 241, 0.15);
      color: #818cf8;
      border: 1px solid rgba(99, 102, 241, 0.3);
    }}
    .icon-tiktok {{
      background: rgba(6, 182, 212, 0.15);
      color: #38bdf8;
      border: 1px solid rgba(6, 182, 212, 0.3);
    }}
    .icon-youtube {{
      background: rgba(239, 68, 68, 0.15);
      color: #f87171;
      border: 1px solid rgba(239, 68, 68, 0.3);
    }}
    .icon-email {{
      background: rgba(56, 189, 248, 0.15);
      color: #7dd3fc;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}

    /* Card Text Content */
    .link-info {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      overflow: hidden;
    }}

    .link-title {{
      font-size: 15px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: -0.01em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .link-desc {{
      font-size: 12px;
      font-weight: 500;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-top: 2px;
    }}

    /* Right Action Arrow */
    .link-arrow-box {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.05);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #64748b;
      margin-left: 8px;
      flex-shrink: 0;
      transition: all 0.2s ease;
    }}

    .modern-link-card:hover .link-arrow-box {{
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
      transform: translateX(3px);
    }}

    /* ======================================================================
       BOTTOM SOCIAL ICONS ROW
       ====================================================================== */

    .social-dock {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin-top: 10px;
      width: 100%;
    }}

    .social-dock-btn {{
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-muted);
      text-decoration: none;
      transition: all 0.22s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .social-dock-btn:hover {{
      transform: translateY(-3px) scale(1.1);
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.25);
      color: #ffffff;
    }}

    .social-dock-btn.btn-discord:hover {{ color: #818cf8; border-color: rgba(99, 102, 241, 0.4); }}
    .social-dock-btn.btn-youtube:hover {{ color: #f87171; border-color: rgba(239, 68, 68, 0.4); }}
    .social-dock-btn.btn-tiktok:hover {{ color: #38bdf8; border-color: rgba(56, 189, 248, 0.4); }}
    .social-dock-btn.btn-email:hover {{ color: #34d399; border-color: rgba(16, 185, 129, 0.4); }}

    .social-dock-btn svg {{
      width: 20px;
      height: 20px;
      fill: currentColor;
    }}

    /* Footer */
    .card-footer {{
      margin-top: 24px;
      text-align: center;
      font-size: 11px;
      color: var(--text-sub);
      letter-spacing: 0.02em;
    }}

    .card-footer a {{
      color: var(--accent-cyan);
      text-decoration: none;
      font-weight: 600;
    }}

    .card-footer a:hover {{
      text-decoration: underline;
    }}

    /* Responsive */
    @media (max-width: 480px) {{
      .modern-card {{
        padding: 26px 18px;
        border-radius: 22px;
      }}
      .profile-name {{
        font-size: 26px;
      }}
      .modern-link-card {{
        height: 64px;
      }}
    }}
  </style>
</head>
<body>

  <!-- 3D Interactive WebGL Starfield/Wave Background -->
  <canvas id="bg-canvas"></canvas>

  <!-- Ambient glow orbs -->
  <div class="ambient-glow" aria-hidden="true">
    <div class="glow-orb glow-orb-1"></div>
    <div class="glow-orb glow-orb-2"></div>
  </div>

  <!-- Page Wrapper -->
  <main class="page-wrapper">

    <!-- ======================================================================
         MODERN CENTRAL GLASS CARD
         ====================================================================== -->
    <article class="modern-card" id="interactive-card">

      <!-- Profile Header -->
      <header class="profile-header">
        <div class="avatar-wrapper">
          <div class="avatar-glow"></div>
          <img class="avatar-img" src="{avatar_b64}" alt="Foto Profil xumu id" width="108" height="108">
          <div class="avatar-badge" title="Online"></div>
        </div>

        <h1 class="profile-name">
          xumu id
          <!-- Cyan Verified Badge -->
          <svg class="verified-icon" viewBox="0 0 24 24">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
          </svg>
        </h1>

        <span class="profile-tag">@xumuid · Content Creator & Modder</span>

        <div class="badges-row">
          <span class="badge-pill">🎮 Gaming Creator</span>
          <span class="badge-pill">⚡ Mod Specialist</span>
          <span class="badge-pill">⭐ Verified</span>
        </div>
      </header>

      <!-- Section Divider -->
      <div class="section-divider">
        <span class="section-title">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
          TAUTAN RESMI
        </span>
        <span class="section-count">7 LINKS</span>
      </div>

      <!-- ======================================================================
           MODERN TAUTAN RESMI (BENTO CARDS)
           ====================================================================== -->
      <div class="links-grid" role="list">

        <!-- 1. Support Me (Sociabuzz Tribe) -->
        <a href="https://sociabuzz.com/xumu_id/tribe" class="modern-link-card card-support" target="_blank" rel="noopener noreferrer" role="listitem">
          <div class="link-icon-box icon-support">
            <svg viewBox="0 0 24 24">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
          </div>
          <div class="link-info">
            <span class="link-title">Support Me</span>
            <span class="link-desc">Sociabuzz Tribe · Dukung karya konten xumuid</span>
          </div>
          <div class="link-arrow-box">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </a>

        <!-- 2. Tutorial Pasang Mod (YouTube) -->
        <a href="https://youtu.be/mNXXSzqsdHA?si=_iUUA-QWP28aLbWr" class="modern-link-card card-tutorial" target="_blank" rel="noopener noreferrer" role="listitem">
          <div class="link-icon-box icon-tutorial">
            <svg viewBox="0 0 24 24">
              <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
            </svg>
          </div>
          <div class="link-info">
            <span class="link-title">Tutorial Pasang Mod</span>
            <span class="link-desc">Tonton panduan langkah demi langkah di YouTube</span>
          </div>
          <div class="link-arrow-box">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </a>

        <!-- 3. Download Mod (Trakteer) -->
        <a href="https://trakteer.id/xumu_id/shop" class="modern-link-card card-mod" target="_blank" rel="noopener noreferrer" role="listitem">
          <div class="link-icon-box icon-mod">
            <svg viewBox="0 0 24 24">
              <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/>
            </svg>
          </div>
          <div class="link-info">
            <span class="link-title">Download Mod</span>
            <span class="link-desc">Trakteer Shop · Akses file mod eksklusif xumuid</span>
          </div>
          <div class="link-arrow-box">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </a>

        <!-- 4. Join Discord Community -->
        <a href="https://discord.gg/cx5xjEmRzh" class="modern-link-card card-discord" target="_blank" rel="noopener noreferrer" role="listitem">
          <div class="link-icon-box icon-discord">
            <svg viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.893.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
          </div>
          <div class="link-info">
            <span class="link-title">Join Discord Community</span>
            <span class="link-desc">Mabar, diskusi mod & nongkrong santai bareng</span>
          </div>
          <div class="link-arrow-box">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </a>

        <!-- 5. Follow TikTok @xumuid -->
        <a href="https://www.tiktok.com/@xumuid?is_from_webapp=1&sender_device=pc" class="modern-link-card card-tiktok" target="_blank" rel="noopener noreferrer" role="listitem">
          <div class="link-icon-box icon-tiktok">
            <svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.88 2.89 2.89 0 0 1-2.89-2.88 2.89 2.89 0 0 1 2.89-2.89c.28 0 .55.04.81.1v-3.5a6.37 6.37 0 0 0-.81-.05A6.34 6.34 0 0 0 3 15.67 6.34 6.34 0 0 0 9.34 22a6.34 6.34 0 0 0 6.34-6.33V9.05a8.28 8.28 0 0 0 4.91 1.57v-3.5a4.86 4.86 0 0 1-1-.43z"/></svg>
          </div>
          <div class="link-info">
            <span class="link-title">Follow TikTok @xumuid</span>
            <span class="link-desc">Video gameplay, showcase mod & live streaming</span>
          </div>
          <div class="link-arrow-box">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </a>

        <!-- 6. Subscribe YouTube Channel -->
        <a href="https://youtube.com/@xumuid?si=JSR4qqEwBjeJhBUU" class="modern-link-card card-youtube" target="_blank" rel="noopener noreferrer" role="listitem">
          <div class="link-icon-box icon-youtube">
            <svg viewBox="0 0 24 24">
              <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
            </svg>
          </div>
          <div class="link-info">
            <span class="link-title">Subscribe YouTube @xumuid</span>
            <span class="link-desc">Official video, tutorial & gaming highlights</span>
          </div>
          <div class="link-arrow-box">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </a>

        <!-- 7. Email Inquiries -->
        <a href="mailto:contact@xumuid.com" class="modern-link-card card-email" role="listitem">
          <div class="link-icon-box icon-email">
            <svg viewBox="0 0 24 24">
              <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
            </svg>
          </div>
          <div class="link-info">
            <span class="link-title">Email Inquiries</span>
            <span class="link-desc">contact@xumuid.com · Kolaborasi & Bisnis</span>
          </div>
          <div class="link-arrow-box">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </a>

      </div>

      <!-- Social Icons Dock (Clean Modern Frosted Dock) -->
      <nav class="social-dock" aria-label="Social media channels">
        <a href="https://discord.gg/cx5xjEmRzh" class="social-dock-btn btn-discord" target="_blank" rel="noopener noreferrer" title="Discord" aria-label="Discord">
          <svg viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.893.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
        </a>
        <a href="https://youtube.com/@xumuid?si=JSR4qqEwBjeJhBUU" class="social-dock-btn btn-youtube" target="_blank" rel="noopener noreferrer" title="YouTube" aria-label="YouTube">
          <svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
        </a>
        <a href="https://www.tiktok.com/@xumuid?is_from_webapp=1&sender_device=pc" class="social-dock-btn btn-tiktok" target="_blank" rel="noopener noreferrer" title="TikTok" aria-label="TikTok">
          <svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.88 2.89 2.89 0 0 1-2.89-2.88 2.89 2.89 0 0 1 2.89-2.89c.28 0 .55.04.81.1v-3.5a6.37 6.37 0 0 0-.81-.05A6.34 6.34 0 0 0 3 15.67 6.34 6.34 0 0 0 9.34 22a6.34 6.34 0 0 0 6.34-6.33V9.05a8.28 8.28 0 0 0 4.91 1.57v-3.5a4.86 4.86 0 0 1-1-.43z"/></svg>
        </a>
        <a href="mailto:contact@xumuid.com" class="social-dock-btn btn-email" title="Email" aria-label="Email">
          <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        </a>
      </nav>

      <!-- Footer -->
      <footer class="card-footer">
        <span>© 2026 xumu id · All rights reserved · <a href="https://xumuid.carrd.co/" target="_blank">xumuid.carrd.co</a></span>
      </footer>

    </article>
  </main>

  <!-- INTERACTIVE LOGIC & 3D BACKGROUND PARTICLES -->
  <script>
    // 1. Interactive 3D Background Canvas (Starfield / Constellation particles)
    const canvas = document.getElementById('bg-canvas');
    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {{
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }});

    const particles = [];
    const particleCount = Math.min(65, Math.floor(window.innerWidth / 16));
    const mouse = {{ x: width / 2, y: height / 2, tx: width / 2, ty: height / 2 }};

    window.addEventListener('mousemove', (e) => {{
      mouse.tx = e.clientX;
      mouse.ty = e.clientY;
    }});

    for (let i = 0; i < particleCount; i++) {{
      particles.push({{
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.45,
        vy: (Math.random() - 0.5) * 0.45,
        radius: Math.random() * 1.8 + 0.8,
        alpha: Math.random() * 0.5 + 0.2
      }});
    }}

    function animateParticles() {{
      ctx.clearRect(0, 0, width, height);

      mouse.x += (mouse.tx - mouse.x) * 0.05;
      mouse.y += (mouse.ty - mouse.y) * 0.05;

      for (let i = 0; i < particles.length; i++) {{
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        if (p.y > height) p.y = 0;

        // Draw particle
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(56, 189, 248, ${{p.alpha}})`;
        ctx.fill();

        // Connect nearby particles
        for (let j = i + 1; j < particles.length; j++) {{
          const p2 = particles[j];
          const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist < 110) {{
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.strokeStyle = `rgba(56, 189, 248, ${{(1 - dist / 110) * 0.14}})`;
            ctx.lineWidth = 0.75;
            ctx.stroke();
          }}
        }}

        // React subtly to mouse
        const mDist = Math.hypot(p.x - mouse.x, p.y - mouse.y);
        if (mDist < 140) {{
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(mouse.x, mouse.y);
          ctx.strokeStyle = `rgba(16, 185, 129, ${{(1 - mDist / 140) * 0.18}})`;
          ctx.lineWidth = 0.85;
          ctx.stroke();
        }}
      }}

      requestAnimationFrame(animateParticles);
    }}
    animateParticles();

    // 2. 3D Card Parallax & Hover Tilt
    const cards = document.querySelectorAll('.modern-link-card');
    cards.forEach(card => {{
      card.addEventListener('mousemove', (e) => {{
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        card.style.transform = `perspective(800px) rotateX(${{-y * 0.08}}deg) rotateY(${{x * 0.05}}deg) translateY(-3px) scale(1.015)`;
      }});

      card.addEventListener('mouseleave', () => {{
        card.style.transform = '';
      }});
    }});

    // 3. Main Card Subtle Parallax
    const mainCard = document.getElementById('interactive-card');
    if (mainCard && window.matchMedia('(hover: hover)').matches) {{
      window.addEventListener('mousemove', (e) => {{
        const cx = window.innerWidth / 2;
        const cy = window.innerHeight / 2;
        const dx = (e.clientX - cx) / cx;
        const dy = (e.clientY - cy) / cy;
        mainCard.style.transform = `perspective(1200px) rotateY(${{dx * 1.5}}deg) rotateX(${{-dy * 1.5}}deg)`;
      }});
      window.addEventListener('mouseleave', () => {{
        mainCard.style.transform = '';
      }});
    }}
  </script>
</body>
</html>
'''

# Write to Dashboard.html and index.html
with open(r'c:\Users\Rian\Desktop\Portfolio\Dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(r'c:\Users\Rian\Desktop\Portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated clean modern xumuid Dashboard.html & index.html! Size: {len(html_content)} bytes")
