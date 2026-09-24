import json
import base64
import os
import hashlib

print("Starting build process...")

# 1. Read ThreeDPaper source from content.md
with open(r'C:\Users\Rian\.gemini\antigravity-ide\brain\2909d196-7237-4df3-bddd-b311198f509f\.system_generated\steps\4\content.md', 'r', encoding='utf-8') as f:
    c4 = f.read()
data4 = json.loads(c4[c4.find('{'):])
code_paper = next(f['code'] for f in data4['files'] if 'site-of-the-year' in f['path'])
css_shared = next(f['code'] for f in data4['files'] if 'threeui.css' in f['path'])

# 2. Read GlassAiButton source from content.md
with open(r'C:\Users\Rian\.gemini\antigravity-ide\brain\2909d196-7237-4df3-bddd-b311198f509f\.system_generated\steps\7\content.md', 'r', encoding='utf-8') as f:
    c7 = f.read()
data7 = json.loads(c7[c7.find('{'):])
code_button = next(f['code'] for f in data7['files'] if 'glass-ai-button.html' in f['path'])

# 3. Read avatar image
avatar_path = r'c:\Users\Rian\Desktop\Portfolio\wiha_avatar.jpg'
with open(avatar_path, 'rb') as f:
    avatar_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

# Verify SHA256 hashes
paper_sha = hashlib.sha256(code_paper.encode('utf-8')).hexdigest()
button_sha = hashlib.sha256(code_button.encode('utf-8')).hexdigest()
print(f"Paper SHA256: {paper_sha} (Matches expected: {paper_sha == 'fdef93fa96a3927430ef35411af70568c56b9488921aead8f36be36800689b7d'})")
print(f"Button SHA256: {button_sha} (Matches expected: {button_sha == 'a484571de316c05ab7fbd2da82da5e028ee1ffe0bd169449fb8a3c7801abd81e'})")

# Base64 encode for embedding inside JS
b64_paper = base64.b64encode(code_paper.encode('utf-8')).decode('ascii')
b64_button = base64.b64encode(code_button.encode('utf-8')).decode('ascii')

html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>@WiHaofficial | Linktree 3D Edition</title>
  <meta name="description" content="Official Linktree of @WiHaofficial - Hai Guys Welcome To My World. Beli Coin TikTok, Media Share Saweria, Sociabuzz, Discord, and 3D Interactive Experience.">
  <link rel="icon" href="{avatar_b64}">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">

  <style>
    /* --- CSS RESET & ROOT TOKENS --- */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    :root {{
      --bg-gradient: radial-gradient(140% 120% at 50% 10%, #bcc5d3 0%, #9caab8 45%, #8896a7 100%);
      --surface-bg: #9caab8;
      --card-white: #ffffff;
      --card-border: #111111;
      --card-shadow: 0 5px 0 #111111;
      --card-shadow-hover: 0 7px 0 #111111;
      --text-main: #0b0c10;
      --text-muted: #4a5568;
      --accent-blue: #1d4ed8;
      --accent-cyan: #06b6d4;
      --accent-lime: #cef2a8;
      --font-main: 'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif;
    }}

    html, body {{
      min-height: 100vh;
      font-family: var(--font-main);
      background: var(--bg-gradient);
      background-attachment: fixed;
      color: var(--text-main);
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    /* Subtle Animated Ambient Mesh in Background */
    .ambient-bg {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      opacity: 0.35;
      background-image: 
        radial-gradient(circle at 20% 15%, rgba(255, 255, 255, 0.6) 0%, transparent 40%),
        radial-gradient(circle at 85% 65%, rgba(6, 182, 212, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 50% 90%, rgba(29, 78, 216, 0.12) 0%, transparent 50%);
    }}

    /* Main Container — replicates mobile Linktree width with responsive scaling */
    .linktree-wrapper {{
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 580px;
      padding: 24px 20px 48px 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 0 auto;
    }}

    /* Top Bar (Badge & Share Icon) */
    .top-nav {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      padding: 0 4px;
    }}

    .icon-circle-btn {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.9);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: #1e293b;
      transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .icon-circle-btn:hover {{
      transform: scale(1.08) translateY(-2px);
      background: #ffffff;
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
      color: #0f172a;
    }}

    .icon-circle-btn:active {{
      transform: scale(0.95);
    }}

    /* Profile Section */
    .profile-section {{
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      margin-bottom: 22px;
      width: 100%;
    }}

    .avatar-container {{
      position: relative;
      width: 104px;
      height: 104px;
      margin-bottom: 14px;
    }}

    .avatar-glow {{
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      background: linear-gradient(135deg, #0ea5e9, #3b82f6, #06b6d4, #a855f7);
      animation: rotateGlow 6s linear infinite;
      filter: blur(4px);
      opacity: 0.85;
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
      border: 3px solid #ffffff;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.18);
      z-index: 1;
      display: block;
    }}

    .status-badge {{
      position: absolute;
      bottom: 2px;
      right: 2px;
      z-index: 2;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: #22c55e;
      border: 3px solid #ffffff;
      box-shadow: 0 0 10px rgba(34, 197, 94, 0.7);
    }}

    .profile-title {{
      font-size: 24px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #1d4ed8;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 6px;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.4);
    }}

    .verified-icon {{
      width: 22px;
      height: 22px;
      color: #2563eb;
      fill: currentColor;
    }}

    .profile-subtitle {{
      font-size: 15px;
      font-weight: 600;
      color: #1e3a8a;
      letter-spacing: -0.01em;
      opacity: 0.9;
    }}

    .badges-row {{
      display: flex;
      gap: 8px;
      margin-top: 12px;
      flex-wrap: wrap;
      justify-content: center;
    }}

    .mini-badge {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 12px;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.8);
      color: #1e293b;
      backdrop-filter: blur(8px);
    }}

    /* Section Divider Header */
    .section-label {{
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin: 18px 0 12px 0;
      padding: 0 4px;
    }}

    .section-label span {{
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #334155;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .section-label .tag {{
      background: #1e293b;
      color: #f8fafc;
      font-size: 9px;
      padding: 2px 8px;
      border-radius: 999px;
    }}

    /* ======================================================================
       THREEUI INTEGRATION: GlassAiButton & ThreeDPaper
       ====================================================================== */
    
    .shader-frame {{
      position: relative;
      width: 100%;
      border-radius: 28px;
      overflow: hidden;
      margin-bottom: 18px;
      transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease;
    }}

    /* Glass AI Button Frame */
    .glass-ai-frame {{
      height: 156px;
      background: #a8b0bd;
      border: 2px solid #111111;
      box-shadow: var(--card-shadow), 0 12px 28px rgba(0, 0, 0, 0.12);
      border-radius: 9999px; /* Pill shape matching Linktree! */
    }}

    .glass-ai-frame:hover {{
      transform: translateY(-3px);
      box-shadow: var(--card-shadow-hover), 0 18px 36px rgba(0, 0, 0, 0.16);
    }}

    /* ThreeDPaper Frame */
    .three-d-paper-frame {{
      height: 480px;
      background: #08080a;
      border: 2px solid #111111;
      border-radius: 32px;
      box-shadow: var(--card-shadow), 0 16px 40px rgba(0, 0, 0, 0.25);
      position: relative;
    }}

    .three-d-paper-frame:hover {{
      box-shadow: var(--card-shadow-hover), 0 22px 48px rgba(0, 0, 0, 0.3);
    }}

    .threeui-background {{
      position: relative;
      width: 100%;
      height: 100%;
      min-width: 0;
      min-height: 0;
      overflow: hidden;
    }}

    .three-d-paper iframe,
    .glass-ai-button iframe {{
      position: absolute;
      inset: 0;
      display: block;
      width: 100%;
      height: 100%;
      border: 0;
      opacity: 0;
      pointer-events: auto;
      transition: opacity 300ms ease-out;
    }}

    .three-d-paper iframe.loaded,
    .glass-ai-button iframe.loaded {{
      opacity: 1;
    }}

    .paper-overlay-bar {{
      position: absolute;
      top: 14px;
      left: 14px;
      right: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      pointer-events: none;
      z-index: 10;
    }}

    .paper-pill-tag {{
      background: rgba(11, 12, 16, 0.85);
      border: 1px solid rgba(206, 242, 168, 0.4);
      color: #cef2a8;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      backdrop-filter: blur(8px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }}

    .paper-controls-btn {{
      pointer-events: auto;
      background: rgba(11, 12, 16, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      border-radius: 999px;
      padding: 6px 12px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .paper-controls-btn:hover {{
      background: #111;
      border-color: #cef2a8;
      color: #cef2a8;
    }}

    .paper-hint-text {{
      position: absolute;
      bottom: 14px;
      left: 0;
      right: 0;
      text-align: center;
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: rgba(242, 242, 240, 0.55);
      pointer-events: none;
      z-index: 10;
    }}

    .paper-hint-text b {{
      color: #cef2a8;
    }}

    /* ======================================================================
       LINKTREE PILL CARDS (9 items from the screenshot)
       ====================================================================== */
    
    .links-list {{
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 15px;
      margin-bottom: 28px;
    }}

    .link-pill {{
      position: relative;
      display: flex;
      align-items: center;
      width: 100%;
      height: 64px;
      background: var(--card-white);
      border: 2px solid var(--card-border);
      border-radius: 9999px;
      padding: 0 16px 0 10px;
      text-decoration: none;
      color: var(--text-main);
      box-shadow: var(--card-shadow);
      transition: all 0.22s cubic-bezier(0.34, 1.56, 0.64, 1);
      cursor: pointer;
      user-select: none;
    }}

    .link-pill:hover {{
      transform: translateY(-3px) scale(1.01);
      box-shadow: var(--card-shadow-hover);
      border-color: #000000;
    }}

    .link-pill:active {{
      transform: translateY(2px) scale(0.99);
      box-shadow: 0 2px 0 var(--card-border);
    }}

    /* Icon in left bubble */
    .link-icon-wrap {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      overflow: hidden;
      background: #f1f5f9;
      border: 1px solid #e2e8f0;
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }}

    .link-icon-wrap img,
    .link-icon-wrap svg {{
      width: 28px;
      height: 28px;
      object-fit: cover;
    }}

    .link-icon-avatar {{
      width: 100% !important;
      height: 100% !important;
      border-radius: 50%;
    }}

    /* Center text content */
    .link-content {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      text-align: center;
      padding: 0 12px;
      overflow: hidden;
    }}

    .link-title {{
      font-size: 14.5px;
      font-weight: 700;
      color: #111827;
      letter-spacing: -0.01em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .link-subtitle {{
      font-size: 11px;
      font-weight: 500;
      color: #64748b;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-top: 1px;
    }}

    /* Right 3-dots action button */
    .link-menu-btn {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #94a3b8;
      border: none;
      background: transparent;
      cursor: pointer;
      flex-shrink: 0;
      transition: all 0.15s;
    }}

    .link-pill:hover .link-menu-btn {{
      color: #334155;
    }}

    .link-menu-btn:hover {{
      background: #f1f5f9;
      color: #0f172a;
    }}

    /* ======================================================================
       BOTTOM SOCIAL ICONS DOCK
       ====================================================================== */
    
    .social-dock {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 36px;
      width: 100%;
    }}

    .social-icon-link {{
      color: #1e293b;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.9);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.06);
      text-decoration: none;
      transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .social-icon-link svg {{
      width: 20px;
      height: 20px;
      fill: currentColor;
    }}

    .social-icon-link:hover {{
      transform: translateY(-4px) scale(1.12);
      background: #ffffff;
      color: #1d4ed8;
      box-shadow: 0 8px 18px rgba(0, 0, 0, 0.12);
    }}

    /* ======================================================================
       LINKTREE BOTTOM PILL & FOOTER
       ====================================================================== */
    
    .join-linktree-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 12px 28px;
      background: #ffffff;
      border: 2px solid #111111;
      border-radius: 9999px;
      font-size: 14px;
      font-weight: 700;
      color: #111111;
      text-decoration: none;
      box-shadow: 0 4px 0 #111111;
      transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
      margin-bottom: 24px;
    }}

    .join-linktree-pill:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 0 #111111;
    }}

    .linktree-logo-icon {{
      width: 18px;
      height: 18px;
    }}

    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 8px 12px;
      font-size: 11px;
      color: #334155;
      opacity: 0.85;
      text-align: center;
      line-height: 1.6;
    }}

    .footer-links a {{
      color: inherit;
      text-decoration: none;
      transition: color 0.15s;
    }}

    .footer-links a:hover {{
      color: #0f172a;
      text-decoration: underline;
    }}

    /* ======================================================================
       MODAL & TOAST
       ====================================================================== */
    
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      z-index: 1000;
      display: none;
      place-items: center;
      padding: 20px;
      opacity: 0;
      transition: opacity 0.25s ease;
    }}

    .modal-backdrop.active {{
      display: grid;
      opacity: 1;
    }}

    .modal-card {{
      background: #ffffff;
      border: 2px solid #111111;
      box-shadow: 0 10px 0 #111111, 0 20px 40px rgba(0, 0, 0, 0.25);
      border-radius: 28px;
      width: 100%;
      max-width: 440px;
      padding: 28px 24px;
      position: relative;
      transform: translateY(20px) scale(0.95);
      transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .modal-backdrop.active .modal-card {{
      transform: translateY(0) scale(1);
    }}

    .modal-close-btn {{
      position: absolute;
      top: 18px;
      right: 18px;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: 1px solid #cbd5e1;
      background: #f8fafc;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #64748b;
      transition: all 0.2s;
    }}

    .modal-close-btn:hover {{
      background: #e2e8f0;
      color: #0f172a;
    }}

    .modal-title {{
      font-size: 20px;
      font-weight: 800;
      margin-bottom: 6px;
      color: #0f172a;
    }}

    .modal-desc {{
      font-size: 13px;
      color: #64748b;
      margin-bottom: 20px;
    }}

    .share-link-input-row {{
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
    }}

    .share-link-input {{
      flex: 1;
      padding: 10px 14px;
      border-radius: 12px;
      border: 1.5px solid #cbd5e1;
      font-family: inherit;
      font-size: 13px;
      color: #334155;
      background: #f8fafc;
      outline: none;
    }}

    .copy-btn {{
      padding: 10px 18px;
      border-radius: 12px;
      background: #1d4ed8;
      color: #ffffff;
      border: none;
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      transition: background 0.15s;
    }}

    .copy-btn:hover {{
      background: #1e40af;
    }}

    .qr-preview-box {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 16px;
      border-radius: 16px;
      background: #f1f5f9;
      border: 1px dashed #cbd5e1;
    }}

    .toast-msg {{
      position: fixed;
      bottom: 28px;
      left: 50%;
      transform: translateX(-50%) translateY(80px);
      background: #0f172a;
      color: #ffffff;
      padding: 12px 24px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
      z-index: 2000;
      opacity: 0;
      pointer-events: none;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .toast-msg.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}

    /* Responsive adjustments */
    @media (max-width: 480px) {{
      .linktree-wrapper {{
        padding: 16px 14px 36px 14px;
      }}
      .three-d-paper-frame {{
        height: 420px;
      }}
      .glass-ai-frame {{
        height: 140px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Ambient background lighting -->
  <div class="ambient-bg" aria-hidden="true"></div>

  <!-- Main Linktree Container -->
  <main class="linktree-wrapper">

    <!-- Top Navigation (Badge & Share) -->
    <header class="top-nav">
      <button class="icon-circle-btn" id="btn-star" aria-label="WiHa Verified Badge" title="WiHa Official Creator">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
        </svg>
      </button>

      <button class="icon-circle-btn" id="btn-share" aria-label="Bagikan Linktree WiHa" title="Bagikan">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"></path>
          <polyline points="16 6 12 2 8 6"></polyline>
          <line x1="12" y1="2" x2="12" y2="15"></line>
        </svg>
      </button>
    </header>

    <!-- Profile Info Header -->
    <section class="profile-section">
      <div class="avatar-container">
        <div class="avatar-glow"></div>
        <img class="avatar-img" src="{avatar_b64}" alt="Foto Profil Kang WiHa Official" width="104" height="104">
        <div class="status-badge" title="Online / Live Now"></div>
      </div>

      <h1 class="profile-title">
        @WiHaofficial
        <svg class="verified-icon" viewBox="0 0 24 24">
          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
        </svg>
      </h1>

      <p class="profile-subtitle">Hai Guys Welcome To My World</p>

      <div class="badges-row">
        <span class="mini-badge">🎮 Gaming Streamer</span>
        <span class="mini-badge">⚡ Official Creator</span>
        <span class="mini-badge">🌐 Indonesia</span>
      </div>
    </section>

    <!-- SECTION: 3D GLASS AI BUTTON (From ThreeUI exact source) -->
    <div class="section-label">
      <span>✨ 3D GLASS AI INTERACTION</span>
      <span class="tag">THREEUI r170</span>
    </div>

    <!-- Exact configured usage of GlassAiButton from ThreeUI -->
    <div class="shader-frame glass-ai-frame" id="glass-ai-button-host">
      <div class="threeui-background glass-ai-button" role="group" aria-label="Interactive glass AI button">
        <iframe id="iframe-glass-ai" title="Glass AI Button" sandbox="allow-scripts" loading="eager"></iframe>
      </div>
    </div>

    <!-- SECTION: ALL 9 LINKTREE LINKS -->
    <div class="section-label">
      <span>📌 TAUTAN RESMI WIHA</span>
      <span class="tag">9 LINKS</span>
    </div>

    <div class="links-list" role="list">

      <!-- 1. Beli Coin TikTok Murah -->
      <a href="https://linktr.ee/wihaofficial" class="link-pill" target="_blank" rel="noopener noreferrer" role="listitem">
        <div class="link-icon-wrap" style="background: #fffbeb;">
          <svg viewBox="0 0 24 24" width="26" height="26" fill="#f59e0b">
            <circle cx="12" cy="12" r="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
            <path d="M12 6v12m-3-9h6a2 2 0 0 1 0 4H9a2 2 0 0 0 0 4h6" stroke="#b45309" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </div>
        <div class="link-content">
          <span class="link-title">BELI COIN TIKTOK MURAH</span>
          <span class="link-subtitle">Top up koin kilat, aman & terpercaya</span>
        </div>
        <button class="link-menu-btn" aria-label="More options" onclick="event.preventDefault(); openShareMenu('Beli Coin TikTok Murah', 'https://linktr.ee/wihaofficial')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
        </button>
      </a>

      <!-- 2. Sociabuzz -->
      <a href="https://sociabuzz.com/wihaofficial" class="link-pill" target="_blank" rel="noopener noreferrer" role="listitem">
        <div class="link-icon-wrap" style="background: #ecfdf5;">
          <svg viewBox="0 0 48 48" width="28" height="28">
            <rect width="48" height="48" rx="24" fill="#10b981"/>
            <path d="M31 16C31 14.34 29.66 13 28 13H19C15.69 13 13 15.69 13 19C13 22.31 15.69 25 19 25H29C30.66 25 32 26.34 32 28C32 29.66 30.66 31 29 31H17C15.34 31 14 29.66 14 28" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round" fill="none"/>
          </svg>
        </div>
        <div class="link-content">
          <span class="link-title">Media Share | Challenge | Support by SOCIABUZZ</span>
          <span class="link-subtitle">Kirim video & tantangan langsung di live stream</span>
        </div>
        <button class="link-menu-btn" aria-label="More options" onclick="event.preventDefault(); openShareMenu('Sociabuzz WiHa', 'https://sociabuzz.com/wihaofficial')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
        </button>
      </a>

      <!-- 3. Saweria -->
      <a href="https://saweria.co/wihaofficial" class="link-pill" target="_blank" rel="noopener noreferrer" role="listitem">
        <div class="link-icon-wrap" style="background: #fff7ed;">
          <svg viewBox="0 0 48 48" width="28" height="28">
            <rect width="48" height="48" rx="24" fill="#f97316"/>
            <!-- Cute Saweria Cup -->
            <path d="M12 18h24v12a12 12 0 0 1-24 0V18z" fill="#ffedd5"/>
            <path d="M36 21h3a4 4 0 0 1 0 8h-3" stroke="#ffedd5" stroke-width="3" stroke-linecap="round" fill="none"/>
            <circle cx="20" cy="24" r="2" fill="#ea580c"/>
            <circle cx="28" cy="24" r="2" fill="#ea580c"/>
            <path d="M21 28c1.5 1.5 4.5 1.5 6 0" stroke="#ea580c" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </div>
        <div class="link-content">
          <span class="link-title">Media Share | Challenge | Support by SAWERIA</span>
          <span class="link-subtitle">Dukungan via QRIS, GoPay, OVO, Dana & ShopeePay</span>
        </div>
        <button class="link-menu-btn" aria-label="More options" onclick="event.preventDefault(); openShareMenu('Saweria WiHa', 'https://saweria.co/wihaofficial')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
        </button>
      </a>

      <!-- 4. Facebook Kang WiHa -->
      <a href="https://facebook.com/wihaofficial" class="link-pill" target="_blank" rel="noopener noreferrer" role="listitem">
        <div class="link-icon-wrap" style="background: #eff6ff;">
          <svg viewBox="0 0 48 48" width="28" height="28">
            <circle cx="24" cy="24" r="24" fill="#1877f2"/>
            <path d="M26.7 38V24.5h4.5l.7-5.3h-5.2v-3.4c0-1.5.4-2.6 2.6-2.6h2.8V8.5c-.5-.1-2.2-.2-4.1-.2-4.1 0-6.9 2.5-6.9 7.1v3.8H16v5.3h4.6V38h6.1z" fill="#ffffff"/>
          </svg>
        </div>
        <div class="link-content">
          <span class="link-title">Facebook Kang WiHa</span>
          <span class="link-subtitle">Official Facebook Gaming Page</span>
        </div>
        <button class="link-menu-btn" aria-label="More options" onclick="event.preventDefault(); openShareMenu('Facebook Kang WiHa', 'https://facebook.com/wihaofficial')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
        </button>
      </a>

      <!-- 5. Tiktok Kang WiHa -->
      <a href="https://tiktok.com/@wihaofficial" class="link-pill" target="_blank" rel="noopener noreferrer" role="listitem">
        <div class="link-icon-wrap" style="background: #000000;">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="#ffffff">
            <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.88 2.89 2.89 0 0 1-2.89-2.88 2.89 2.89 0 0 1 2.89-2.89c.28 0 .55.04.81.1v-3.5a6.37 6.37 0 0 0-.81-.05A6.34 6.34 0 0 0 3 15.67 6.34 6.34 0 0 0 9.34 22a6.34 6.34 0 0 0 6.34-6.33V9.05a8.28 8.28 0 0 0 4.91 1.57v-3.5a4.86 4.86 0 0 1-1-.43z"/>
          </svg>
        </div>
        <div class="link-content">
          <span class="link-title">Tiktok Kang WiHa</span>
          <span class="link-subtitle">Video lucu & highlight live streaming</span>
        </div>
        <button class="link-menu-btn" aria-label="More options" onclick="event.preventDefault(); openShareMenu('TikTok Kang WiHa', 'https://tiktok.com/@wihaofficial')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
        </button>
      </a>

      <!-- 6. IG Kang WiHA -->
      <a href="https://instagram.com/wihaofficial" class="link-pill" target="_blank" rel="noopener noreferrer" role="listitem">
        <div class="link-icon-wrap" style="background: linear-gradient(45deg, #f09433 0%,#e6683c 25%,#dc2743 50%,#cc2366 75%,#bc1888 100%);">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="#ffffff">
            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
          </svg>
        </div>
        <div class="link-content">
          <span class="link-title">IG Kang WiHA</span>
          <span class="link-subtitle">Follow update kegiatan harian & story</span>
        </div>
        <button class="link-menu-btn" aria-label="More options" onclick="event.preventDefault(); openShareMenu('Instagram WiHa', 'https://instagram.com/wihaofficial')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
        </button>
      </a>

      <!-- 7. Kang WiHa Youtube Channel -->
      <a href="https://youtube.com/@wihaofficial" class="link-pill" target="_blank" rel="noopener noreferrer" role="listitem">
        <div class="link-icon-wrap" style="background: #fef2f2;">
          <svg viewBox="0 0 24 24" width="26" height="26" fill="#ef4444">
            <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
          </svg>
        </div>
        <div class="link-content">
          <span class="link-title">Kang WiHa Youtube Channel</span>
          <span class="link-subtitle">Official gameplay, live stream & video seru</span>
        </div>
        <button class="link-menu-btn" aria-label="More options" onclick="event.preventDefault(); openShareMenu('YouTube WiHa', 'https://youtube.com/@wihaofficial')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
        </button>
      </a>

      <!-- 8. Join Discord -->
      <a href="https://discord.gg/wihaofficial" class="link-pill" target="_blank" rel="noopener noreferrer" role="listitem">
        <div class="link-icon-wrap" style="background: #eef2ff;">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="#5865f2">
            <path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.893.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/>
          </svg>
        </div>
        <div class="link-content">
          <span class="link-title">Join Discord</span>
          <span class="link-subtitle">Discord Server • Free to join</span>
        </div>
        <button class="link-menu-btn" aria-label="More options" onclick="event.preventDefault(); openShareMenu('Discord WiHa Official', 'https://discord.gg/wihaofficial')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
        </button>
      </a>

      <!-- 9. Whatsapp Business -->
      <a href="https://wa.me/6281234567890" class="link-pill" target="_blank" rel="noopener noreferrer" role="listitem">
        <div class="link-icon-wrap" style="background: #ecfdf5; position: relative;">
          <img src="{avatar_b64}" class="link-icon-avatar" alt="Avatar">
          <div style="position: absolute; bottom: 0; right: 0; width: 16px; height: 16px; background: #25d366; border-radius: 50%; display: grid; place-items: center; border: 1.5px solid #fff;">
            <svg viewBox="0 0 24 24" width="10" height="10" fill="#fff"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
          </div>
        </div>
        <div class="link-content">
          <span class="link-title">Whatsapp Business</span>
          <span class="link-subtitle">Keperluan Bisnis, Endorsement & Kerjasama</span>
        </div>
        <button class="link-menu-btn" aria-label="More options" onclick="event.preventDefault(); openShareMenu('WhatsApp Business WiHa', 'https://wa.me/6281234567890')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
        </button>
      </a>

    </div>

    <!-- SECTION: 3D PAPER — SITE OF THE YEAR AWARD (From ThreeUI exact source) -->
    <div class="section-label">
      <span>🏆 3D AWARD SHOWCASE — SITE OF THE YEAR</span>
      <span class="tag">THREEUI r149</span>
    </div>

    <!-- Exact configured usage of ThreeDPaper from ThreeUI -->
    <div class="shader-frame three-d-paper-frame" id="three-d-paper-host">
      <div class="paper-overlay-bar">
        <span class="paper-pill-tag">SITE OF THE YEAR 2026</span>
        <button class="paper-controls-btn" id="btn-expand-paper" title="Buka mode penuh">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="15 3 21 3 21 9"></polyline>
            <polyline points="9 21 3 21 3 15"></polyline>
            <line x1="21" y1="3" x2="14" y2="10"></line>
            <line x1="3" y1="21" x2="10" y2="14"></line>
          </svg>
          Full 3D
        </button>
      </div>

      <div class="threeui-background three-d-paper" role="group" aria-label="Interactive translucent 3D paper certificate" data-variant="site-of-the-year">
        <iframe id="iframe-paper" title="3D Paper — Site of the Year" sandbox="allow-scripts" loading="eager"></iframe>
      </div>

      <div class="paper-hint-text">
        <b>Drag</b> to turn it &nbsp;·&nbsp; <b>Hover</b> to light it
      </div>
    </div>

    <!-- SOCIAL DOCK ROW -->
    <nav class="social-dock" aria-label="Social media channels">
      <!-- TikTok -->
      <a href="https://tiktok.com/@wihaofficial" class="social-icon-link" target="_blank" rel="noopener noreferrer" title="TikTok" aria-label="TikTok">
        <svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.88 2.89 2.89 0 0 1-2.89-2.88 2.89 2.89 0 0 1 2.89-2.89c.28 0 .55.04.81.1v-3.5a6.37 6.37 0 0 0-.81-.05A6.34 6.34 0 0 0 3 15.67 6.34 6.34 0 0 0 9.34 22a6.34 6.34 0 0 0 6.34-6.33V9.05a8.28 8.28 0 0 0 4.91 1.57v-3.5a4.86 4.86 0 0 1-1-.43z"/></svg>
      </a>
      <!-- Discord -->
      <a href="https://discord.gg/wihaofficial" class="social-icon-link" target="_blank" rel="noopener noreferrer" title="Discord" aria-label="Discord">
        <svg viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.893.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
      </a>
      <!-- WhatsApp -->
      <a href="https://wa.me/6281234567890" class="social-icon-link" target="_blank" rel="noopener noreferrer" title="WhatsApp" aria-label="WhatsApp">
        <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2zm.01 16.67c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24 2.2 0 4.27.86 5.82 2.42a8.18 8.18 0 0 1 2.41 5.83c.02 4.54-3.68 8.23-8.22 8.23zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.09-.39-.12-.56.12-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.12-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.84-.86 2.05 0 1.21.88 2.38 1.01 2.55.12.17 1.74 2.65 4.21 3.72.59.25 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.17-.47-.29z"/></svg>
      </a>
      <!-- Instagram -->
      <a href="https://instagram.com/wihaofficial" class="social-icon-link" target="_blank" rel="noopener noreferrer" title="Instagram" aria-label="Instagram">
        <svg viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
      </a>
      <!-- YouTube -->
      <a href="https://youtube.com/@wihaofficial" class="social-icon-link" target="_blank" rel="noopener noreferrer" title="YouTube" aria-label="YouTube">
        <svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
      </a>
      <!-- Facebook -->
      <a href="https://facebook.com/wihaofficial" class="social-icon-link" target="_blank" rel="noopener noreferrer" title="Facebook" aria-label="Facebook">
        <svg viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
      </a>
      <!-- Website -->
      <a href="https://linktr.ee/wihaofficial" class="social-icon-link" target="_blank" rel="noopener noreferrer" title="Website Resmi" aria-label="Website">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="2" y1="12" x2="22" y2="12"></line>
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
        </svg>
      </a>
    </nav>

    <!-- JOIN LINKTREE BUTTON (from screenshot) -->
    <a href="https://linktr.ee/wihaofficial" class="join-linktree-pill" target="_blank" rel="noopener noreferrer">
      <!-- Linktree Brand Logo Tree -->
      <svg class="linktree-logo-icon" viewBox="0 0 24 24" fill="currentColor">
        <path d="M13.51 5.952l3.603-3.603a.5.5 0 0 1 .707 0l1.414 1.414a.5.5 0 0 1 0 .707l-3.603 3.603h4.636a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.5.5h-4.636l3.603 3.603a.5.5 0 0 1 0 .707l-1.414 1.414a.5.5 0 0 1-.707 0l-3.603-3.603v4.636a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-4.636l-3.603 3.603a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 0-.707l3.603-3.603H3.636a.5.5 0 0 1-.5-.5v-2a.5.5 0 0 1 .5-.5h4.636l-3.603-3.603a.5.5 0 0 1 0-.707l1.414-1.414a.5.5 0 0 1 .707 0l3.603 3.603V1.316a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 .5.5v4.636z"/>
      </svg>
      Join WiHaofficial on Linktree
    </a>

    <!-- FOOTER NAV -->
    <footer class="footer-links">
      <a href="#cookie" onclick="showToast('Preferensi cookie tersimpan'); return false;">Cookie Preferences</a> • 
      <a href="#report" onclick="showToast('Laporan diteruskan ke tim moderasi'); return false;">Report</a> • 
      <a href="#privacy">Privacy</a> • 
      <a href="#explore">Explore</a> • 
      <a href="#about">About this account</a> • 
      <a href="https://linktr.ee" target="_blank" rel="noopener">More from Linktree</a>
    </footer>

  </main>

  <!-- SHARE MODAL DIALOG -->
  <div class="modal-backdrop" id="share-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <div class="modal-card">
      <button class="modal-close-btn" id="btn-close-modal" aria-label="Tutup">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>

      <h2 class="modal-title" id="modal-title">Bagikan Profil WiHa</h2>
      <p class="modal-desc" id="modal-desc">Bagikan link resmi @WiHaofficial ke teman atau media sosial.</p>

      <div class="share-link-input-row">
        <input type="text" class="share-link-input" id="share-input" value="https://linktr.ee/wihaofficial" readonly>
        <button class="copy-btn" id="btn-copy-link">Salin</button>
      </div>

      <div class="qr-preview-box">
        <svg width="120" height="120" viewBox="0 0 100 100" fill="#0f172a">
          <!-- Stylized high-res QR Pattern -->
          <rect width="100" height="100" fill="#ffffff" rx="8"/>
          <path d="M10 10h24v24H10zM14 14h16v16H14zM18 18h8v8H18zM66 10h24v24H66zM70 14h16v16H70zM74 18h8v8H74zM10 66h24v24H10zM14 70h16v16H14zM18 74h8v8H18zM42 12h6v6h-6zM52 12h6v6h-6zM42 22h16v6H42zM12 42h6v6h-6zM22 42h10v6H22zM42 42h6v6h-6zM58 42h10v6H58zM78 42h10v6H78zM12 52h16v6H12zM38 52h8v6h-8zM56 52h8v6h-8zM74 52h14v6H74zM42 64h6v6h-6zM58 64h16v6H58zM42 74h16v6H42zM68 74h6v6h-6zM84 74h6v6h-8zM42 84h8v6h-8zM60 84h12v6H60zM82 84h8v6h-8z"/>
        </svg>
        <span style="font-size: 11px; font-weight: 700; color: #475569; margin-top: 10px;">SCAN DENGAN KAMERA HP</span>
      </div>
    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div class="toast-msg" id="toast">Tautan berhasil disalin ke clipboard!</div>

  <!-- EMBEDDED THREEUI SOURCE CODES (EXACT AUTHOR REVISIONS VIA BASE64) -->
  <script>
    // Decodes UTF-8 base64 strings exactly into raw HTML source string
    function decodeB64(str) {{
      const bin = atob(str);
      const bytes = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) {{
        bytes[i] = bin.charCodeAt(i);
      }}
      return new TextDecoder('utf-8').decode(bytes);
    }}

    // Exact registered source bundles from ThreeUI
    const B64_PAPER_SOURCE = "{b64_paper}";
    const B64_BUTTON_SOURCE = "{b64_button}";

    window.addEventListener('DOMContentLoaded', () => {{
      // 1. Mount GlassAiButton
      try {{
        const btnHtml = decodeB64(B64_BUTTON_SOURCE);
        const btnIframe = document.getElementById('iframe-glass-ai');
        if (btnIframe) {{
          btnIframe.srcdoc = btnHtml;
          btnIframe.onload = () => {{
            btnIframe.classList.add('loaded');
          }};
        }}
      }} catch (err) {{
        console.error("Error mounting GlassAiButton:", err);
      }}

      // 2. Mount ThreeDPaper (variant: site-of-the-year)
      try {{
        const paperHtml = decodeB64(B64_PAPER_SOURCE);
        const paperIframe = document.getElementById('iframe-paper');
        if (paperIframe) {{
          paperIframe.srcdoc = paperHtml;
          paperIframe.onload = () => {{
            paperIframe.classList.add('loaded');
          }};
        }}
      }} catch (err) {{
        console.error("Error mounting ThreeDPaper:", err);
      }}

      // 3. Setup Interactive Fullscreen for 3D Paper
      const expandBtn = document.getElementById('btn-expand-paper');
      const paperHost = document.getElementById('three-d-paper-host');
      let isExpanded = false;
      if (expandBtn && paperHost) {{
        expandBtn.addEventListener('click', () => {{
          isExpanded = !isExpanded;
          if (isExpanded) {{
            paperHost.style.position = 'fixed';
            paperHost.style.inset = '0';
            paperHost.style.width = '100vw';
            paperHost.style.height = '100vh';
            paperHost.style.zIndex = '999';
            paperHost.style.borderRadius = '0';
            paperHost.style.margin = '0';
            expandBtn.innerHTML = `
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <polyline points="4 14 10 14 10 20"></polyline>
                <polyline points="20 10 14 10 14 4"></polyline>
                <line x1="14" y1="10" x2="21" y2="3"></line>
                <line x1="3" y1="21" x2="10" y2="14"></line>
              </svg> Close`;
          }} else {{
            paperHost.style.position = 'relative';
            paperHost.style.inset = 'auto';
            paperHost.style.width = '100%';
            paperHost.style.height = '480px';
            paperHost.style.zIndex = 'auto';
            paperHost.style.borderRadius = '32px';
            paperHost.style.margin = '0 0 18px 0';
            expandBtn.innerHTML = `
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <polyline points="15 3 21 3 21 9"></polyline>
                <polyline points="9 21 3 21 3 15"></polyline>
                <line x1="21" y1="3" x2="14" y2="10"></line>
                <line x1="3" y1="21" x2="10" y2="14"></line>
              </svg> Full 3D`;
          }}
        }});
      }}

      // 4. Modal & Toast functionality
      const shareModal = document.getElementById('share-modal');
      const btnShare = document.getElementById('btn-share');
      const btnCloseModal = document.getElementById('btn-close-modal');
      const btnCopyLink = document.getElementById('btn-copy-link');
      const shareInput = document.getElementById('share-input');

      function openModal(title, url) {{
        if (title) document.getElementById('modal-title').textContent = title;
        if (url) {{
          shareInput.value = url;
          document.getElementById('modal-desc').textContent = 'Bagikan tautan ini ke teman atau komunitas kamu:';
        }} else {{
          shareInput.value = 'https://linktr.ee/wihaofficial';
          document.getElementById('modal-desc').textContent = 'Bagikan link resmi @WiHaofficial ke teman atau media sosial:';
        }}
        shareModal.classList.add('active');
      }}

      function closeModal() {{
        shareModal.classList.remove('active');
      }}

      if (btnShare) btnShare.addEventListener('click', () => openModal());
      if (btnCloseModal) btnCloseModal.addEventListener('click', closeModal);
      shareModal.addEventListener('click', (e) => {{
        if (e.target === shareModal) closeModal();
      }});

      window.openShareMenu = (title, url) => {{
        openModal('Bagikan: ' + title, url);
      }};

      if (btnCopyLink) {{
        btnCopyLink.addEventListener('click', () => {{
          shareInput.select();
          navigator.clipboard.writeText(shareInput.value).then(() => {{
            showToast('Tautan berhasil disalin ke clipboard! 📋');
            closeModal();
          }}).catch(() => {{
            document.execCommand('copy');
            showToast('Tautan berhasil disalin! 📋');
            closeModal();
          }});
        }});
      }}

      window.showToast = (msg) => {{
        const toast = document.getElementById('toast');
        toast.textContent = msg;
        toast.classList.add('show');
        setTimeout(() => {{
          toast.classList.remove('show');
        }}, 2800);
      }};

      // 5. Star badge click
      const btnStar = document.getElementById('btn-star');
      if (btnStar) {{
        btnStar.addEventListener('click', () => {{
          showToast('⭐ Akun Terverifikasi Resmi: @WiHaofficial');
        }});
      }}

      // 6. Interactive 3D Card Parallax on Mouse Move (Desktop)
      document.querySelectorAll('.link-pill').forEach(pill => {{
        pill.addEventListener('mousemove', (e) => {{
          const rect = pill.getBoundingClientRect();
          const x = e.clientX - rect.left - rect.width / 2;
          const y = e.clientY - rect.top - rect.height / 2;
          pill.style.transform = `perspective(600px) rotateX(${{-y * 0.08}}deg) rotateY(${{x * 0.04}}deg) translateY(-3px) scale(1.01)`;
        }});
        pill.addEventListener('mouseleave', () => {{
          pill.style.transform = '';
        }});
      }});
    }});
  </script>
</body>
</html>
'''

# Write to Dashboard.html and index.html
with open(r'c:\Users\Rian\Desktop\Portfolio\Dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(r'c:\Users\Rian\Desktop\Portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully wrote Dashboard.html and index.html! File size: {len(html_content)} bytes")
