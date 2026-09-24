import json
import base64
import os
import hashlib

print("Building xumuid Card & 3D Portfolio...")

# 1. Read ThreeDPaper source from content.md
with open(r'C:\Users\Rian\.gemini\antigravity-ide\brain\2909d196-7237-4df3-bddd-b311198f509f\.system_generated\steps\4\content.md', 'r', encoding='utf-8') as f:
    c4 = f.read()
data4 = json.loads(c4[c4.find('{'):])
code_paper = next(f['code'] for f in data4['files'] if 'site-of-the-year' in f['path'])

# 2. Read GlassAiButton source from content.md
with open(r'C:\Users\Rian\.gemini\antigravity-ide\brain\2909d196-7237-4df3-bddd-b311198f509f\.system_generated\steps\7\content.md', 'r', encoding='utf-8') as f:
    c7 = f.read()
data7 = json.loads(c7[c7.find('{'):])
code_button = next(f['code'] for f in data7['files'] if 'glass-ai-button.html' in f['path'])

# 3. Read xumuid avatar
avatar_path = r'c:\Users\Rian\Desktop\Portfolio\xumuid_yt_avatar.jpg'
with open(avatar_path, 'rb') as f:
    avatar_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

# Verify hashes
paper_sha = hashlib.sha256(code_paper.encode('utf-8')).hexdigest()
button_sha = hashlib.sha256(code_button.encode('utf-8')).hexdigest()
print(f"Paper SHA256: {paper_sha} (Matches: {paper_sha == 'fdef93fa96a3927430ef35411af70568c56b9488921aead8f36be36800689b7d'})")
print(f"Button SHA256: {button_sha} (Matches: {button_sha == 'a484571de316c05ab7fbd2da82da5e028ee1ffe0bd169449fb8a3c7801abd81e'})")

b64_paper = base64.b64encode(code_paper.encode('utf-8')).decode('ascii')
b64_button = base64.b64encode(code_button.encode('utf-8')).decode('ascii')

html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>xumu id (@xumuid) | Official 3D Hub & Portfolio</title>
  <meta name="description" content="Official Hub of xumu id (@xumuid) - Support Me, Tutorial Pasang Mod, Download Mod, Discord, YouTube, TikTok and 3D Interactive WebGL Experience.">
  <link rel="icon" href="{avatar_b64}">

  <!-- Google Fonts: JetBrains Mono (from carrd.co) & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">

  <style>
    /* --- CSS RESET & THEME VARIABLES --- */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    :root {{
      --bg-dark: #070b12;
      --card-bg: rgba(15, 32, 39, 0.78);
      --card-border: #000000;
      --card-shadow: 0.35rem 0.35rem 0rem 0rem #000000;
      --text-white: #ffffff;
      --text-dim: #94a3b8;
      --color-green: #22c55e;
      --color-yellow: #ffe500;
      --color-red: #e83333;
      --color-cyan: #48c3f7;
      --color-blurple: #5865f2;
      --color-pink: #e851a7;
      --font-mono: 'JetBrains Mono', monospace;
      --font-sans: 'Plus Jakarta Sans', sans-serif;
    }}

    html, body {{
      min-height: 100vh;
      font-family: var(--font-mono);
      background-color: var(--bg-dark);
      color: var(--text-white);
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      position: relative;
    }}

    /* Cyber Ambient Background */
    .bg-canvas-layer {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      background: 
        radial-gradient(ellipse 90% 60% at 50% -10%, rgba(34, 197, 94, 0.15) 0%, transparent 60%),
        radial-gradient(circle at 15% 85%, rgba(72, 195, 247, 0.12) 0%, transparent 50%),
        radial-gradient(circle at 85% 75%, rgba(232, 81, 167, 0.14) 0%, transparent 50%),
        linear-gradient(180deg, rgba(7, 11, 18, 0.6) 0%, rgba(10, 15, 26, 0.95) 100%);
    }}

    /* Subtle Animated Matrix/Grid Lines */
    .bg-grid {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      opacity: 0.14;
      background-size: 40px 40px;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.1) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.1) 1px, transparent 1px);
    }}

    /* Main Container */
    .page-wrapper {{
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 680px;
      padding: 32px 18px 64px 18px;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 0 auto;
    }}

    /* Top Floating Controls Bar */
    .top-controls-bar {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding: 0 4px;
    }}

    .top-pill-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: 999px;
      background: rgba(15, 23, 42, 0.8);
      border: 1.5px solid #000000;
      box-shadow: 0.15rem 0.15rem 0 #000000;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: var(--color-green);
      backdrop-filter: blur(10px);
    }}

    .top-pill-badge .dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--color-green);
      box-shadow: 0 0 8px var(--color-green);
      animation: pulseDot 2s infinite;
    }}

    @keyframes pulseDot {{
      0%, 100% {{ transform: scale(1); opacity: 1; }}
      50% {{ transform: scale(1.3); opacity: 0.7; }}
    }}

    .top-action-btn {{
      width: 42px;
      height: 42px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 2px solid #000000;
      box-shadow: 0.18rem 0.18rem 0 #000000;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: #ffffff;
      transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .top-action-btn:hover {{
      transform: translateY(-2px) scale(1.08);
      background: var(--color-cyan);
      color: #000000;
    }}

    /* ======================================================================
       THE CENTRAL CARD CONTAINER (Inspired by xumuid.carrd.co)
       ====================================================================== */

    .xumu-card {{
      width: 100%;
      background-color: var(--card-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 2px solid var(--card-border);
      box-shadow: var(--card-shadow), 0 20px 50px rgba(0, 0, 0, 0.5);
      border-radius: 24px;
      padding: 36px 30px;
      position: relative;
      overflow: hidden;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
    }}

    /* Card Glowing Header Accent */
    .xumu-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, var(--color-green), var(--color-cyan), var(--color-pink), var(--color-yellow));
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

    .avatar-wrap {{
      position: relative;
      width: 120px;
      height: 120px;
      margin-bottom: 18px;
    }}

    .avatar-glow-ring {{
      position: absolute;
      inset: -6px;
      border-radius: 50%;
      background: conic-gradient(from 0deg, var(--color-cyan), var(--color-pink), var(--color-yellow), var(--color-green), var(--color-cyan));
      filter: blur(6px);
      animation: spinGlow 8s linear infinite;
      opacity: 0.85;
    }}

    @keyframes spinGlow {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}

    .avatar-img-circle {{
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid #000000;
      background: #000;
      z-index: 2;
      display: block;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
    }}

    .avatar-badge-online {{
      position: absolute;
      bottom: 4px;
      right: 4px;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: var(--color-green);
      border: 3px solid #000000;
      box-shadow: 0 0 10px var(--color-green);
      z-index: 3;
    }}

    .profile-title {{
      font-family: var(--font-mono);
      font-size: 38px;
      font-weight: 800;
      letter-spacing: -0.04em;
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
      text-shadow: 0 2px 10px rgba(72, 195, 247, 0.3);
    }}

    .profile-handle-tag {{
      display: inline-block;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.05em;
      color: var(--color-cyan);
      margin-bottom: 16px;
      background: rgba(72, 195, 247, 0.12);
      padding: 4px 14px;
      border-radius: 999px;
      border: 1px solid rgba(72, 195, 247, 0.3);
    }}

    /* Quotes from xumuid.carrd.co */
    .bio-quote-box {{
      width: 100%;
      text-align: center;
      background: rgba(0, 0, 0, 0.4);
      border: 1.5px solid rgba(255, 255, 255, 0.12);
      border-radius: 16px;
      padding: 18px 20px;
      margin-bottom: 24px;
      box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.3);
    }}

    .bio-quote-main {{
      font-size: 15px;
      font-weight: 600;
      line-height: 1.6;
      color: #f1f5f9;
      margin-bottom: 12px;
      font-style: italic;
    }}

    .bio-quote-desc {{
      font-size: 12.5px;
      font-weight: 400;
      line-height: 1.7;
      color: #94a3b8;
      margin-bottom: 10px;
    }}

    .bio-quote-cta {{
      font-size: 12.5px;
      font-weight: 600;
      color: var(--color-yellow);
      margin-top: 6px;
      display: block;
    }}

    /* Section Headers inside Card */
    .card-section-label {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      margin: 22px 0 14px 0;
      padding-bottom: 6px;
      border-bottom: 1.5px dashed rgba(255, 255, 255, 0.15);
    }}

    .card-section-label span {{
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #cbd5e1;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .card-section-label .tag {{
      background: #000000;
      color: var(--color-cyan);
      font-size: 10px;
      padding: 2px 10px;
      border-radius: 6px;
      border: 1px solid var(--color-cyan);
    }}

    /* ======================================================================
       3D GLASS AI BUTTON (ThreeUI exact source r170)
       ====================================================================== */
    
    .shader-frame {{
      position: relative;
      width: 100%;
      border-radius: 20px;
      overflow: hidden;
      margin-bottom: 20px;
      transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.25s ease;
    }}

    .glass-ai-frame {{
      height: 154px;
      background: #a8b0bd;
      border: 2px solid #000000;
      box-shadow: 0.25rem 0.25rem 0 #000000;
      border-radius: 9999px; /* Pill button */
    }}

    .glass-ai-frame:hover {{
      transform: scale(1.02);
      box-shadow: 0.35rem 0.35rem 0 #000000;
    }}

    .threeui-background {{
      position: relative;
      width: 100%;
      height: 100%;
      min-width: 0;
      min-height: 0;
      overflow: hidden;
    }}

    .glass-ai-button iframe,
    .three-d-paper iframe {{
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

    .glass-ai-button iframe.loaded,
    .three-d-paper iframe.loaded {{
      opacity: 1;
    }}

    /* ======================================================================
       LINK BUTTONS (Styled like xumuid.carrd.co Neo-Brutalist Cyber aesthetic)
       ====================================================================== */
    
    .buttons-container {{
      display: flex;
      flex-direction: column;
      gap: 14px;
      width: 100%;
      margin-bottom: 26px;
    }}

    .carrd-btn {{
      position: relative;
      display: flex;
      align-items: center;
      width: 100%;
      height: 60px;
      padding: 0 16px;
      border-radius: 12px;
      border: 2px solid #000000;
      box-shadow: 0.22rem 0.22rem 0rem 0rem #000000;
      text-decoration: none;
      color: #000000;
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 15px;
      letter-spacing: -0.01em;
      transition: transform 0.15s ease, box-shadow 0.15s ease, background-color 0.15s ease;
      cursor: pointer;
      user-select: none;
    }}

    .carrd-btn:hover {{
      transform: translate(-2px, -2px);
      box-shadow: 0.35rem 0.35rem 0rem 0rem #000000;
    }}

    .carrd-btn:active {{
      transform: translate(2px, 2px);
      box-shadow: 0.08rem 0.08rem 0rem 0rem #000000;
    }}

    /* Button Colors from Carrd */
    .carrd-btn.btn-green {{
      background-color: var(--color-green);
    }}
    .carrd-btn.btn-green:hover {{
      background-color: #4ade80;
    }}

    .carrd-btn.btn-yellow {{
      background-color: var(--color-yellow);
    }}
    .carrd-btn.btn-yellow:hover {{
      background-color: #fef08a;
    }}

    .carrd-btn.btn-red {{
      background-color: var(--color-red);
      color: #ffffff;
    }}
    .carrd-btn.btn-red:hover {{
      background-color: #f87171;
    }}

    .carrd-btn.btn-cyan {{
      background-color: var(--color-cyan);
    }}
    .carrd-btn.btn-cyan:hover {{
      background-color: #bae6fd;
    }}

    .carrd-btn.btn-blurple {{
      background-color: var(--color-blurple);
      color: #ffffff;
    }}
    .carrd-btn.btn-blurple:hover {{
      background-color: #818cf8;
    }}

    .carrd-btn.btn-dark {{
      background-color: #111827;
      color: #ffffff;
      border-color: #000000;
    }}
    .carrd-btn.btn-dark:hover {{
      background-color: #1f2937;
    }}

    .btn-icon-wrap {{
      width: 36px;
      height: 36px;
      border-radius: 8px;
      background: rgba(0, 0, 0, 0.12);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-right: 14px;
      flex-shrink: 0;
    }}

    .carrd-btn.btn-red .btn-icon-wrap,
    .carrd-btn.btn-blurple .btn-icon-wrap,
    .carrd-btn.btn-dark .btn-icon-wrap {{
      background: rgba(255, 255, 255, 0.2);
    }}

    .btn-icon-wrap svg {{
      width: 22px;
      height: 22px;
      fill: currentColor;
    }}

    .btn-label-box {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      overflow: hidden;
    }}

    .btn-title-text {{
      font-size: 14.5px;
      font-weight: 800;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .btn-subtitle-text {{
      font-size: 11px;
      font-weight: 500;
      opacity: 0.8;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-top: 1px;
    }}

    .btn-arrow {{
      width: 20px;
      height: 20px;
      margin-left: 8px;
      flex-shrink: 0;
      transition: transform 0.15s ease;
    }}

    .carrd-btn:hover .btn-arrow {{
      transform: translateX(4px);
    }}

    /* ======================================================================
       3D PAPER — SITE OF THE YEAR SHOWCASE (ThreeUI exact source r149)
       ====================================================================== */

    .three-d-paper-frame {{
      height: 460px;
      background: #08080a;
      border: 2px solid #000000;
      box-shadow: 0.35rem 0.35rem 0 #000000;
      border-radius: 20px;
      position: relative;
    }}

    .paper-top-dock {{
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

    .paper-award-pill {{
      background: rgba(11, 12, 16, 0.9);
      border: 1px solid rgba(206, 242, 168, 0.4);
      color: #cef2a8;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      backdrop-filter: blur(8px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }}

    .paper-expand-btn {{
      pointer-events: auto;
      background: rgba(11, 12, 16, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #ffffff;
      border-radius: 999px;
      padding: 6px 14px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}

    .paper-expand-btn:hover {{
      background: #000;
      border-color: #cef2a8;
      color: #cef2a8;
    }}

    .paper-bottom-hint {{
      position: absolute;
      bottom: 14px;
      left: 0;
      right: 0;
      text-align: center;
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: rgba(242, 242, 240, 0.6);
      pointer-events: none;
      z-index: 10;
    }}

    .paper-bottom-hint b {{
      color: #cef2a8;
    }}

    /* ======================================================================
       SOCIAL ICONS BAR INSIDE CARD
       ====================================================================== */

    .card-social-row {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      margin: 18px 0 10px 0;
      width: 100%;
    }}

    .card-social-item {{
      width: 46px;
      height: 46px;
      border-radius: 12px;
      background: #000000;
      border: 2px solid #000000;
      box-shadow: 0.18rem 0.18rem 0 rgba(255, 255, 255, 0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      text-decoration: none;
      transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .card-social-item.discord-btn {{
      color: #6b7ee3;
    }}
    .card-social-item.youtube-btn {{
      color: #ff0000;
    }}
    .card-social-item.tiktok-btn {{
      color: #ffffff;
    }}

    .card-social-item:hover {{
      transform: translateY(-4px) scale(1.1);
      box-shadow: 0.28rem 0.28rem 0 rgba(255, 255, 255, 0.5);
    }}

    .card-social-item svg {{
      width: 24px;
      height: 24px;
      fill: currentColor;
    }}

    /* Footer Credits (Made with Carrd & 3D WebGL) */
    .card-footer {{
      margin-top: 24px;
      text-align: center;
      font-size: 11px;
      color: #64748b;
      letter-spacing: 0.05em;
    }}

    .card-footer a {{
      color: var(--color-pink);
      text-decoration: none;
      font-weight: 600;
    }}

    .card-footer a:hover {{
      text-decoration: underline;
    }}

    /* ======================================================================
       SHARE MODAL & TOAST
       ====================================================================== */

    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(7, 11, 18, 0.75);
      backdrop-filter: blur(8px);
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
      background: #0f172a;
      border: 2px solid var(--color-cyan);
      box-shadow: 0.35rem 0.35rem 0 #000000, 0 20px 40px rgba(0, 0, 0, 0.5);
      border-radius: 20px;
      width: 100%;
      max-width: 440px;
      padding: 26px 22px;
      position: relative;
      color: #ffffff;
    }}

    .modal-close-btn {{
      position: absolute;
      top: 16px;
      right: 16px;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: 1px solid #334155;
      background: #1e293b;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #94a3b8;
    }}

    .modal-close-btn:hover {{
      background: #334155;
      color: #ffffff;
    }}

    .share-input-row {{
      display: flex;
      gap: 8px;
      margin: 16px 0;
    }}

    .share-input {{
      flex: 1;
      padding: 10px 14px;
      border-radius: 10px;
      border: 1.5px solid #334155;
      background: #1e293b;
      color: #f8fafc;
      font-family: inherit;
      font-size: 13px;
      outline: none;
    }}

    .copy-btn {{
      padding: 10px 16px;
      border-radius: 10px;
      background: var(--color-cyan);
      color: #000000;
      border: none;
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      font-family: inherit;
    }}

    .toast-msg {{
      position: fixed;
      bottom: 28px;
      left: 50%;
      transform: translateX(-50%) translateY(80px);
      background: #1e293b;
      border: 1px solid var(--color-cyan);
      color: #ffffff;
      padding: 12px 24px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
      z-index: 2000;
      opacity: 0;
      pointer-events: none;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .toast-msg.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}

    /* Responsive */
    @media (max-width: 540px) {{
      .xumu-card {{
        padding: 26px 18px;
        border-radius: 18px;
      }}
      .profile-title {{
        font-size: 30px;
      }}
      .three-d-paper-frame {{
        height: 400px;
      }}
      .glass-ai-frame {{
        height: 140px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Cyber background layer -->
  <div class="bg-canvas-layer" aria-hidden="true"></div>
  <div class="bg-grid" aria-hidden="true"></div>

  <!-- Page Wrapper -->
  <main class="page-wrapper">

    <!-- Top floating controls -->
    <div class="top-controls-bar">
      <div class="top-pill-badge">
        <span class="dot"></span>
        xumuid.carrd.co · 3D Edition
      </div>
      <button class="top-action-btn" id="btn-share" aria-label="Bagikan" title="Bagikan Profil">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"></path>
          <polyline points="16 6 12 2 8 6"></polyline>
          <line x1="12" y1="2" x2="12" y2="15"></line>
        </svg>
      </button>
    </div>

    <!-- ======================================================================
         MAIN XUMU ID CARD CONTAINER
         ====================================================================== -->
    <article class="xumu-card" id="main-card">

      <!-- Profile Header -->
      <header class="profile-header">
        <div class="avatar-wrap">
          <div class="avatar-glow-ring"></div>
          <img class="avatar-img-circle" src="{avatar_b64}" alt="Foto Profil xumu id" width="120" height="120">
          <div class="avatar-badge-online" title="Online / Live"></div>
        </div>

        <h1 class="profile-title">
          xumu id
          <!-- Cyan Verified Badge -->
          <svg width="26" height="26" viewBox="0 0 24 24" fill="#48c3f7">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
          </svg>
        </h1>

        <span class="profile-handle-tag">@xumuid · Content Creator & Modder</span>

        <!-- Quotes from xumuid.carrd.co -->
        <div class="bio-quote-box">
          <p class="bio-quote-main">&quot;Kadang, dunia nyata terlalu bising untuk hati yang cuma butuh tenang.&quot; 🖤🎮</p>
          <p class="bio-quote-desc">Di saat orang lain melihat gameplay ini cuma sebatas permainan angka dan skill, bagi gua ini adalah tempat bertahan hidup. Di balik frame rate tinggi dan lampu RGB, ada cerita tentang melarikan diri dari penatnya kehidupan, mengubah luka jadi karya, dan menjadikan layar sebagai tempat pulang.</p>
          <p class="bio-quote-desc">🥀 Dunia mungkin jahat, tapi di sini kita menang bareng.</p>
          <span class="bio-quote-cta">⚡ Klik link di bawah, mari berjuang di pertempuran berikutnya.</span>
        </div>
      </header>

      <!-- SECTION: 3D GLASS AI BUTTON (ThreeUI exact source r170) -->
      <div class="card-section-label">
        <span>✨ 3D GLASS AI ACTIVATION</span>
        <span class="tag">THREEUI r170</span>
      </div>

      <!-- Exact configured usage of GlassAiButton from ThreeUI -->
      <div class="shader-frame glass-ai-frame" id="glass-ai-button-host">
        <div class="threeui-background glass-ai-button" role="group" aria-label="Interactive glass AI button">
          <iframe id="iframe-glass-ai" title="Glass AI Button" sandbox="allow-scripts" loading="eager"></iframe>
        </div>
      </div>

      <!-- SECTION: ALL BUTTONS FROM xumuid.carrd.co -->
      <div class="card-section-label">
        <span>🔗 TAUTAN RESMI XUMUID</span>
        <span class="tag">VERIFIED LINKS</span>
      </div>

      <div class="buttons-container" role="list">

        <!-- 1. Support Me (Sociabuzz Tribe) -->
        <a href="https://sociabuzz.com/xumu_id/tribe" class="carrd-btn btn-green" target="_blank" rel="noopener noreferrer" role="listitem">
          <div class="btn-icon-wrap">
            <svg viewBox="0 0 24 24">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
          </div>
          <div class="btn-label-box">
            <span class="btn-title-text">Support Me</span>
            <span class="btn-subtitle-text">Sociabuzz Tribe · Dukung karya konten xumuid</span>
          </div>
          <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>

        <!-- 2. Tutorial Pasang Mod (YouTube) -->
        <a href="https://youtu.be/mNXXSzqsdHA?si=_iUUA-QWP28aLbWr" class="carrd-btn btn-yellow" target="_blank" rel="noopener noreferrer" role="listitem">
          <div class="btn-icon-wrap">
            <svg viewBox="0 0 24 24">
              <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
            </svg>
          </div>
          <div class="btn-label-box">
            <span class="btn-title-text">Tutorial Pasang Mod</span>
            <span class="btn-subtitle-text">Tonton panduan langkah demi langkah di YouTube</span>
          </div>
          <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>

        <!-- 3. Download Mod (Trakteer) -->
        <a href="https://trakteer.id/xumu_id/shop" class="carrd-btn btn-red" target="_blank" rel="noopener noreferrer" role="listitem">
          <div class="btn-icon-wrap">
            <svg viewBox="0 0 24 24">
              <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/>
            </svg>
          </div>
          <div class="btn-label-box">
            <span class="btn-title-text">Download Mod</span>
            <span class="btn-subtitle-text">Trakteer Shop · Dapatkan file mod eksklusif</span>
          </div>
          <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>

        <!-- 4. Email Inquiries -->
        <a href="mailto:contact@xumuid.com" class="carrd-btn btn-cyan" role="listitem">
          <div class="btn-icon-wrap">
            <svg viewBox="0 0 24 24">
              <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
            </svg>
          </div>
          <div class="btn-label-box">
            <span class="btn-title-text">Email Business</span>
            <span class="btn-subtitle-text">contact@xumuid.com · Kolaborasi & Bisnis</span>
          </div>
          <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>

        <!-- 5. Discord Server -->
        <a href="https://discord.gg/cx5xjEmRzh" class="carrd-btn btn-blurple" target="_blank" rel="noopener noreferrer" role="listitem">
          <div class="btn-icon-wrap">
            <svg viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.893.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
          </div>
          <div class="btn-label-box">
            <span class="btn-title-text">Join Discord Community</span>
            <span class="btn-subtitle-text">Mabar, diskusi mod & nongkrong santai</span>
          </div>
          <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>

        <!-- 6. TikTok Official -->
        <a href="https://www.tiktok.com/@xumuid?is_from_webapp=1&sender_device=pc" class="carrd-btn btn-dark" target="_blank" rel="noopener noreferrer" role="listitem">
          <div class="btn-icon-wrap" style="background: rgba(255,255,255,0.15);">
            <svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.88 2.89 2.89 0 0 1-2.89-2.88 2.89 2.89 0 0 1 2.89-2.89c.28 0 .55.04.81.1v-3.5a6.37 6.37 0 0 0-.81-.05A6.34 6.34 0 0 0 3 15.67 6.34 6.34 0 0 0 9.34 22a6.34 6.34 0 0 0 6.34-6.33V9.05a8.28 8.28 0 0 0 4.91 1.57v-3.5a4.86 4.86 0 0 1-1-.43z"/></svg>
          </div>
          <div class="btn-label-box">
            <span class="btn-title-text">Follow TikTok @xumuid</span>
            <span class="btn-subtitle-text">Video gameplay, mod & live streaming</span>
          </div>
          <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>

      </div>

      <!-- SECTION: 3D PAPER — SITE OF THE YEAR (ThreeUI exact source r149) -->
      <div class="card-section-label">
        <span>🏆 3D AWARD SHOWCASE — SITE OF THE YEAR</span>
        <span class="tag">THREEUI r149</span>
      </div>

      <!-- Exact configured usage of ThreeDPaper from ThreeUI -->
      <div class="shader-frame three-d-paper-frame" id="three-d-paper-host">
        <div class="paper-top-dock">
          <span class="paper-award-pill">SITE OF THE YEAR 2026</span>
          <button class="paper-expand-btn" id="btn-expand-paper" title="Buka mode penuh">
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

        <div class="paper-bottom-hint">
          <b>Drag</b> to turn it &nbsp;·&nbsp; <b>Hover</b> to light it
        </div>
      </div>

      <!-- Social Icons Row (Inside Card) -->
      <div class="card-social-row" aria-label="Social media channels">
        <a href="https://discord.gg/cx5xjEmRzh" class="card-social-item discord-btn" target="_blank" rel="noopener noreferrer" title="Discord" aria-label="Discord">
          <svg viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.893.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
        </a>
        <a href="https://youtube.com/@xumuid?si=JSR4qqEwBjeJhBUU" class="card-social-item youtube-btn" target="_blank" rel="noopener noreferrer" title="YouTube" aria-label="YouTube">
          <svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
        </a>
        <a href="https://www.tiktok.com/@xumuid?is_from_webapp=1&sender_device=pc" class="card-social-item tiktok-btn" target="_blank" rel="noopener noreferrer" title="TikTok" aria-label="TikTok">
          <svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.88 2.89 2.89 0 0 1-2.89-2.88 2.89 2.89 0 0 1 2.89-2.89c.28 0 .55.04.81.1v-3.5a6.37 6.37 0 0 0-.81-.05A6.34 6.34 0 0 0 3 15.67 6.34 6.34 0 0 0 9.34 22a6.34 6.34 0 0 0 6.34-6.33V9.05a8.28 8.28 0 0 0 4.91 1.57v-3.5a4.86 4.86 0 0 1-1-.43z"/></svg>
        </a>
        <a href="mailto:contact@xumuid.com" class="card-social-item" title="Email" aria-label="Email">
          <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        </a>
      </div>

      <!-- Card Footer -->
      <footer class="card-footer">
        <span>© 2026 xumu id · Inspired by <a href="https://xumuid.carrd.co/" target="_blank">xumuid.carrd.co</a> & ThreeUI 3D</span>
      </footer>

    </article>
  </main>

  <!-- SHARE MODAL -->
  <div class="modal-backdrop" id="share-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <div class="modal-card">
      <button class="modal-close-btn" id="btn-close-modal" aria-label="Tutup">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>

      <h2 style="font-size: 20px; font-weight: 800; margin-bottom: 6px;" id="modal-title">Bagikan Profil xumu id</h2>
      <p style="font-size: 13px; color: #94a3b8; margin-bottom: 16px;">Salin link profil resmi @xumuid untuk dibagikan ke teman:</p>

      <div class="share-input-row">
        <input type="text" class="share-input" id="share-input" value="https://xumuid.carrd.co/" readonly>
        <button class="copy-btn" id="btn-copy-link">Salin</button>
      </div>
    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div class="toast-msg" id="toast">Tautan berhasil disalin! 📋</div>

  <!-- JAVASCRIPT & THREEUI LOADERS -->
  <script>
    function decodeB64(str) {{
      const bin = atob(str);
      const bytes = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) {{
        bytes[i] = bin.charCodeAt(i);
      }}
      return new TextDecoder('utf-8').decode(bytes);
    }}

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

      // 3. Fullscreen / Expand 3D Paper
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
            paperHost.style.height = '460px';
            paperHost.style.zIndex = 'auto';
            paperHost.style.borderRadius = '20px';
            paperHost.style.margin = '0 0 20px 0';
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

      // 4. Modal & Toast
      const shareModal = document.getElementById('share-modal');
      const btnShare = document.getElementById('btn-share');
      const btnCloseModal = document.getElementById('btn-close-modal');
      const btnCopyLink = document.getElementById('btn-copy-link');
      const shareInput = document.getElementById('share-input');

      if (btnShare) btnShare.addEventListener('click', () => shareModal.classList.add('active'));
      if (btnCloseModal) btnCloseModal.addEventListener('click', () => shareModal.classList.remove('active'));
      shareModal.addEventListener('click', (e) => {{
        if (e.target === shareModal) shareModal.classList.remove('active');
      }});

      window.showToast = (msg) => {{
        const toast = document.getElementById('toast');
        toast.textContent = msg;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2800);
      }};

      if (btnCopyLink) {{
        btnCopyLink.addEventListener('click', () => {{
          shareInput.select();
          navigator.clipboard.writeText(shareInput.value).then(() => {{
            showToast('Tautan xumu id disalin ke clipboard! 📋');
            shareModal.classList.remove('active');
          }}).catch(() => {{
            document.execCommand('copy');
            showToast('Tautan disalin! 📋');
            shareModal.classList.remove('active');
          }});
        }});
      }}

      // 5. 3D Card Parallax Tilt on Pointer Move (Desktop)
      const mainCard = document.getElementById('main-card');
      if (mainCard && window.matchMedia('(hover: hover)').matches) {{
        window.addEventListener('mousemove', (e) => {{
          const cx = window.innerWidth / 2;
          const cy = window.innerHeight / 2;
          const dx = (e.clientX - cx) / cx;
          const dy = (e.clientY - cy) / cy;
          mainCard.style.transform = `perspective(1000px) rotateY(${{dx * 2.5}}deg) rotateX(${{-dy * 2.5}}deg)`;
        }});
        window.addEventListener('mouseleave', () => {{
          mainCard.style.transform = '';
        }});
      }}
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

print(f"Successfully generated xumuid Dashboard.html & index.html! Size: {len(html_content)} bytes")
