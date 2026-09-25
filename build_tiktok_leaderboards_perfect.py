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

# Comprehensive multi-timeframe dataset for Top Gifters
dataset_gifters = {
    "60 days": {
        "total": [
            {"rank": 1, "name": "user14090625", "amount": "1,829 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "Phiu", "amount": "597 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "MASDDY", "amount": "397 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "Hyzen", "amount": "305 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "Kairi Pontianak", "amount": "201 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "zheva", "amount": "198 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "FX.W7M", "amount": "185 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "BG RAAA", "amount": "145 Coins", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "muh_ilham_1", "amount": "110 Coins", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 10, "name": "Ncann", "amount": "95 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ],
        "increase": [
            {"rank": 1, "name": "user14090625", "amount": "+540 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "Phiu", "amount": "+210 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "MASDDY", "amount": "+145 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "Hyzen", "amount": "+95 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "zheva", "amount": "+80 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "Kairi Pontianak", "amount": "+65 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "FX.W7M", "amount": "+50 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "BG RAAA", "amount": "+40 Coins", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "muh_ilham_1", "amount": "+25 Coins", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 10, "name": "Ncann", "amount": "+20 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ]
    },
    "28 days": {
        "total": [
            {"rank": 1, "name": "user14090625", "amount": "1,150 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "Phiu", "amount": "420 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "MASDDY", "amount": "280 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "Hyzen", "amount": "190 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "zheva", "amount": "160 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "Kairi Pontianak", "amount": "135 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "FX.W7M", "amount": "115 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "BG RAAA", "amount": "90 Coins", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "muh_ilham_1", "amount": "75 Coins", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 10, "name": "Ncann", "amount": "60 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ],
        "increase": [
            {"rank": 1, "name": "user14090625", "amount": "+320 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "Phiu", "amount": "+135 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "MASDDY", "amount": "+90 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "Hyzen", "amount": "+60 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "zheva", "amount": "+55 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "Kairi Pontianak", "amount": "+45 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "FX.W7M", "amount": "+35 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "BG RAAA", "amount": "+25 Coins", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "muh_ilham_1", "amount": "+15 Coins", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 10, "name": "Ncann", "amount": "+10 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ]
    },
    "7 days": {
        "total": [
            {"rank": 1, "name": "user14090625", "amount": "450 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "Phiu", "amount": "180 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "MASDDY", "amount": "120 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "zheva", "amount": "85 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "Hyzen", "amount": "70 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "Kairi Pontianak", "amount": "55 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "FX.W7M", "amount": "45 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "BG RAAA", "amount": "30 Coins", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "muh_ilham_1", "amount": "20 Coins", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 10, "name": "Ncann", "amount": "15 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ],
        "increase": [
            {"rank": 1, "name": "user14090625", "amount": "+140 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "Phiu", "amount": "+65 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "MASDDY", "amount": "+45 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "zheva", "amount": "+35 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "Hyzen", "amount": "+25 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "Kairi Pontianak", "amount": "+20 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "FX.W7M", "amount": "+15 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "BG RAAA", "amount": "+10 Coins", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "muh_ilham_1", "amount": "+5 Coins", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 10, "name": "Ncann", "amount": "+5 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ]
    },
    "Latest LIVE": {
        "total": [
            {"rank": 1, "name": "user14090625", "amount": "120 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "Phiu", "amount": "65 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "MASDDY", "amount": "40 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "zheva", "amount": "30 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "Kairi Pontianak", "amount": "25 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "Hyzen", "amount": "20 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "FX.W7M", "amount": "15 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "BG RAAA", "amount": "10 Coins", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "Ncann", "amount": "5 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"},
            {"rank": 10, "name": "muh_ilham_1", "amount": "2 Coins", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"}
        ],
        "increase": [
            {"rank": 1, "name": "user14090625", "amount": "+120 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "Phiu", "amount": "+65 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "MASDDY", "amount": "+40 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "zheva", "amount": "+30 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "Kairi Pontianak", "amount": "+25 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "Hyzen", "amount": "+20 Coins", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "FX.W7M", "amount": "+15 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "BG RAAA", "amount": "+10 Coins", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "Ncann", "amount": "+5 Coins", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"},
            {"rank": 10, "name": "muh_ilham_1", "amount": "+2 Coins", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"}
        ]
    }
}

# Comprehensive multi-timeframe dataset for Loyal Viewers (Penonton Setia)
dataset_viewers = {
    "60 days": {
        "total": [
            {"rank": 1, "name": "zheva", "amount": "70h 25m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "user14090625", "amount": "68h 43m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "FX.W7M", "amount": "48h 28m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "BG RAAA", "amount": "28h 48m", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "muh_ilham_1", "amount": "21h 11m", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 6, "name": "Kairi Pontianak", "amount": "19h 33m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "Phiu", "amount": "16h 40m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "MASDDY", "amount": "14h 15m", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "Hyzen", "amount": "11h 05m", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 10, "name": "Ncann", "amount": "8h 30m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ],
        "increase": [
            {"rank": 1, "name": "zheva", "amount": "+14h 10m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "user14090625", "amount": "+12h 45m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "FX.W7M", "amount": "+9h 15m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "BG RAAA", "amount": "+6h 30m", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "muh_ilham_1", "amount": "+4h 20m", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 6, "name": "Kairi Pontianak", "amount": "+3h 50m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "Phiu", "amount": "+3h 10m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "MASDDY", "amount": "+2h 40m", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "Hyzen", "amount": "+2h 05m", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 10, "name": "Ncann", "amount": "+1h 30m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ]
    },
    "28 days": {
        "total": [
            {"rank": 1, "name": "zheva", "amount": "42h 10m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "user14090625", "amount": "39h 25m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "FX.W7M", "amount": "29h 15m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "BG RAAA", "amount": "17h 40m", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "muh_ilham_1", "amount": "12h 50m", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 6, "name": "Kairi Pontianak", "amount": "11h 20m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "Phiu", "amount": "9h 30m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "MASDDY", "amount": "8h 15m", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "Hyzen", "amount": "6h 40m", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 10, "name": "Ncann", "amount": "4h 50m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ],
        "increase": [
            {"rank": 1, "name": "zheva", "amount": "+9h 20m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "user14090625", "amount": "+8h 10m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "FX.W7M", "amount": "+5h 45m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "BG RAAA", "amount": "+3h 50m", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "muh_ilham_1", "amount": "+2h 30m", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 6, "name": "Kairi Pontianak", "amount": "+2h 10m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "Phiu", "amount": "+1h 45m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "MASDDY", "amount": "+1h 20m", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "Hyzen", "amount": "+1h 05m", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 10, "name": "Ncann", "amount": "+45m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ]
    },
    "7 days": {
        "total": [
            {"rank": 1, "name": "zheva", "amount": "16h 40m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "user14090625", "amount": "14h 50m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "FX.W7M", "amount": "10h 30m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "BG RAAA", "amount": "6h 15m", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "Kairi Pontianak", "amount": "4h 45m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "muh_ilham_1", "amount": "4h 10m", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 7, "name": "Phiu", "amount": "3h 25m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "MASDDY", "amount": "2h 50m", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "Hyzen", "amount": "2h 15m", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 10, "name": "Ncann", "amount": "1h 40m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ],
        "increase": [
            {"rank": 1, "name": "zheva", "amount": "+5h 15m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "user14090625", "amount": "+4h 30m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "FX.W7M", "amount": "+3h 10m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "BG RAAA", "amount": "+2h 00m", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "Kairi Pontianak", "amount": "+1h 35m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "muh_ilham_1", "amount": "+1h 15m", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 7, "name": "Phiu", "amount": "+55m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 8, "name": "MASDDY", "amount": "+40m", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "Hyzen", "amount": "+30m", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 10, "name": "Ncann", "amount": "+25m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ]
    },
    "Latest LIVE": {
        "total": [
            {"rank": 1, "name": "zheva", "amount": "3h 45m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "user14090625", "amount": "3h 30m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "FX.W7M", "amount": "2h 45m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "BG RAAA", "amount": "1h 50m", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "Kairi Pontianak", "amount": "1h 25m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "Phiu", "amount": "1h 10m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "muh_ilham_1", "amount": "55m", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 8, "name": "MASDDY", "amount": "45m", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "Hyzen", "amount": "30m", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 10, "name": "Ncann", "amount": "20m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ],
        "increase": [
            {"rank": 1, "name": "zheva", "amount": "+3h 45m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=150&q=80"},
            {"rank": 2, "name": "user14090625", "amount": "+3h 30m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80"},
            {"rank": 3, "name": "FX.W7M", "amount": "+2h 45m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"},
            {"rank": 4, "name": "BG RAAA", "amount": "+1h 50m", "badge": "xumu", "badge_color": "silver", "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80"},
            {"rank": 5, "name": "Kairi Pontianak", "amount": "+1h 25m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=150&q=80"},
            {"rank": 6, "name": "Phiu", "amount": "+1h 10m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=150&q=80"},
            {"rank": 7, "name": "muh_ilham_1", "amount": "+55m", "badge": None, "avatar": None, "avatar_text": "B", "avatar_bg": "#ec4899"},
            {"rank": 8, "name": "MASDDY", "amount": "+45m", "badge": None, "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80"},
            {"rank": 9, "name": "Hyzen", "amount": "+30m", "badge": None, "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=150&q=80"},
            {"rank": 10, "name": "Ncann", "amount": "+20m", "badge": "xumu", "badge_color": "orange", "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=150&q=80"}
        ]
    }
}

json_gifters_all = json.dumps(dataset_gifters)
json_viewers_all = json.dumps(dataset_viewers)

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
  <title>{page_title} | xumu id</title>
  <meta name="description" content="Leaderboard Top Gifter & Penonton Setia TikTok @xumuid - Tampilan Neo-Brutalism presisi mobile">

  <!-- Google Fonts: Space Grotesk & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&family=Space+Grotesk:wght@600;700;800;900&display=swap" rel="stylesheet">

  <!-- Font Awesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">

  <style>
    /* ======================================================================
       EXACT TOP SULTAN ARCHITECTURE (MAX-WIDTH 480PX MOBILE FIT)
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

    /* 2. Floating Neo-Brutalist Geometric Stickers */
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
      font-size: 20px;
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

    @keyframes floatSlow {{
      0% {{ transform: translateY(0px) rotate(-5deg); }}
      100% {{ transform: translateY(-10px) rotate(5deg); }}
    }}

    /* Main Page Wrapper - EXACT TOP SULTAN WIDTH (480px) */
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

    /* ======================================================================
       MAIN NEO-BRUTALIST CARD (EXACT TOP SULTAN PROPORTIONS)
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
    }}

    .neo-card::before {{
      content: '★ TIKTOK LIVE ★';
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

    /* Card Header */
    .leaderboard-header {{
      text-align: center;
      margin-bottom: 16px;
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
      margin-bottom: 8px;
    }}

    .leaderboard-title {{
      font-family: var(--font-display);
      font-size: 30px;
      font-weight: 900;
      color: var(--text-black);
      letter-spacing: -0.02em;
      line-height: 1.1;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}

    .leaderboard-subtitle {{
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 600;
      margin-top: 4px;
    }}

    /* TikTok Tabs (Most Gifts vs Most watch time) */
    .tiktok-tabs-wrapper {{
      display: flex;
      border-bottom: 2.5px solid var(--border-black);
      margin-bottom: 12px;
      position: relative;
    }}

    .tab-btn {{
      flex: 1;
      padding: 10px 12px;
      background: transparent;
      border: none;
      font-family: var(--font-display);
      font-size: 14px;
      font-weight: 800;
      color: var(--text-dim);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      position: relative;
      transition: all 0.15s ease;
    }}

    .tab-btn:hover {{
      color: var(--text-black);
    }}

    .tab-btn.active {{
      color: var(--text-black);
    }}

    .tab-btn.active::after {{
      content: '';
      position: absolute;
      bottom: -2.5px;
      left: 10%;
      right: 10%;
      height: 4px;
      background: var(--tiktok-red);
      border-radius: 4px 4px 0 0;
    }}

    /* Sub-filters Row: Total/Increase + Dropdown */
    .filter-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 14px;
    }}

    .pill-filter-box {{
      display: flex;
      background: #f1f5f9;
      border: 2px solid var(--border-black);
      border-radius: 999px;
      padding: 2.5px;
      box-shadow: 2px 2px 0px #121212;
    }}

    .pill-btn {{
      background: transparent;
      border: none;
      border-radius: 999px;
      padding: 4px 12px;
      font-family: var(--font-sans);
      font-size: 11.5px;
      font-weight: 800;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .pill-btn.active {{
      background: #121212;
      color: #ffffff;
    }}

    /* Static 60 Days Badge (No Dropdown) */
    .period-static-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--card-white);
      border: 2px solid var(--border-black);
      border-radius: 999px;
      box-shadow: 2.5px 2.5px 0px #121212;
      padding: 5px 12px;
      font-family: var(--font-display);
      font-size: 11.5px;
      font-weight: 800;
      color: var(--text-black);
    }}

    /* ======================================================================
       PODIUM WITH 3D PEDESTALS (EXACT TOP SULTAN SYSTEM)
       ====================================================================== */
    .podium-section {{
      display: grid;
      grid-template-columns: 1fr 1.15fr 1fr;
      gap: 8px;
      align-items: end;
      width: 100%;
      margin: 10px 0 16px 0;
    }}

    .podium-col {{
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }}

    .col-rank-1 {{
      order: 2;
    }}
    .col-rank-2 {{
      order: 1;
    }}
    .col-rank-3 {{
      order: 3;
    }}

    /* Radiant Sunburst Rays for Rank 1 */
    .col-rank-1 .radiant-rays {{
      position: absolute;
      top: 50px;
      left: 50%;
      width: 130px;
      height: 130px;
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

    .col-rank-1 .radiant-halo {{
      position: absolute;
      top: 50px;
      left: 50%;
      width: 110px;
      height: 110px;
      transform: translate(-50%, -50%);
      border-radius: 50%;
      background: radial-gradient(circle, rgba(250, 204, 21, 0.55) 0%, transparent 70%);
      pointer-events: none;
      z-index: 0;
    }}

    @keyframes spinRays {{
      0% {{ transform: translate(-50%, -50%) rotate(0deg); }}
      100% {{ transform: translate(-50%, -50%) rotate(360deg); }}
    }}

    /* Avatar & 3D Medal Frame */
    .podium-avatar-wrapper {{
      position: relative;
      width: 64px;
      height: 64px;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1;
    }}

    .col-rank-1 .podium-avatar-wrapper {{
      width: 78px;
      height: 78px;
      margin-bottom: 10px;
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

    .avatar-img-circle {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    .medal-corner-badge {{
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
      font-size: 11px;
      font-weight: 900;
      z-index: 5;
    }}

    .col-rank-1 .medal-corner-badge {{
      width: 28px;
      height: 28px;
      font-size: 12.5px;
      background: var(--gold-rank);
      color: #121212;
    }}
    .col-rank-2 .medal-corner-badge {{
      background: var(--silver-rank);
      color: #121212;
    }}
    .col-rank-3 .medal-corner-badge {{
      background: var(--bronze-rank);
      color: #121212;
    }}

    .crown-decal {{
      position: absolute;
      top: -14px;
      left: 50%;
      transform: translateX(-50%);
      color: #ca8a04;
      font-size: 18px;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
      animation: crownBounce 2s ease-in-out infinite alternate;
      z-index: 6;
    }}

    @keyframes crownBounce {{
      0% {{ transform: translateX(-50%) translateY(0); }}
      100% {{ transform: translateX(-50%) translateY(-3px); }}
    }}

    /* Name and Amount Above Pedestal */
    .podium-name {{
      font-family: var(--font-display);
      font-size: 12.5px;
      font-weight: 800;
      color: var(--text-black);
      max-width: 100%;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-bottom: 3px;
      z-index: 1;
    }}

    .col-rank-1 .podium-name {{
      font-size: 14px;
      font-weight: 900;
    }}

    .fan-pill {{
      display: inline-flex;
      align-items: center;
      gap: 3px;
      background: #ffe4e6;
      border: 1px solid #f43f5e;
      color: #e11d48;
      padding: 1px 5px;
      border-radius: 4px;
      font-size: 9px;
      font-weight: 800;
      margin-bottom: 4px;
      z-index: 1;
    }}

    .fan-pill.silver {{
      background: #f1f5f9;
      border-color: #94a3b8;
      color: #475569;
    }}

    .podium-amount {{
      font-family: var(--font-display);
      font-size: 10.5px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 999px;
      border: 1.5px solid var(--border-black);
      box-shadow: 1.5px 1.5px 0px #121212;
      white-space: nowrap;
      margin-bottom: 6px;
      z-index: 1;
    }}

    .col-rank-1 .podium-amount {{
      background: var(--gold-rank);
      font-size: 11.5px;
      padding: 3px 9px;
      box-shadow: 2px 2px 0px #121212;
    }}
    .col-rank-2 .podium-amount {{
      background: var(--silver-rank);
    }}
    .col-rank-3 .podium-amount {{
      background: var(--bronze-rank);
    }}

    /* Pedestal Block */
    .pedestal-block {{
      width: 100%;
      border: 3px solid var(--border-black);
      box-shadow: 4px 4px 0px #121212;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      padding-top: 10px;
      border-radius: 14px 14px 4px 4px;
      position: relative;
      overflow: hidden;
    }}

    .col-rank-1 .pedestal-block {{
      height: 125px;
      background: var(--gold-rank);
      box-shadow: 5px 5px 0px #121212;
    }}
    .col-rank-2 .pedestal-block {{
      height: 95px;
      background: var(--silver-rank);
    }}
    .col-rank-3 .pedestal-block {{
      height: 75px;
      background: var(--bronze-rank);
    }}

    .pedestal-number {{
      font-family: var(--font-display);
      font-size: 28px;
      font-weight: 900;
      color: var(--text-black);
      line-height: 1;
    }}

    .col-rank-1 .pedestal-number {{
      font-size: 38px;
    }}

    .pedestal-label {{
      font-family: var(--font-display);
      font-size: 9px;
      font-weight: 800;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-top: 3px;
      opacity: 0.85;
      display: flex;
      align-items: center;
      gap: 3px;
    }}

    /* ======================================================================
       RANKS 4 - 10 LIST SECTION
       ====================================================================== */
    .list-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      margin: 14px 0 10px 0;
      padding-bottom: 6px;
      border-bottom: 2.5px dashed #cbd5e1;
    }}

    .list-title {{
      font-family: var(--font-display);
      font-size: 11.5px;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .list-counter {{
      background: #121212;
      color: #ffffff;
      font-family: var(--font-display);
      font-size: 9.5px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 999px;
    }}

    .ranks-stack {{
      display: flex;
      flex-direction: column;
      gap: 7px;
      width: 100%;
    }}

    .rank-row-card {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #ffffff;
      border: 2px solid var(--border-black);
      border-radius: 12px;
      box-shadow: 2.5px 2.5px 0px #121212;
      padding: 8px 12px;
      transition: all 0.15s ease;
    }}

    .rank-row-card:hover {{
      transform: translate(-1px, -1px);
      box-shadow: 4px 4px 0px #121212;
    }}

    .rank-card-left {{
      display: flex;
      align-items: center;
      gap: 10px;
      min-width: 0;
    }}

    .rank-number-box {{
      width: 24px;
      height: 24px;
      background: #f1f5f9;
      border: 1.5px solid var(--border-black);
      border-radius: 6px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 900;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .rank-avatar-img {{
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: 1.5px solid var(--border-black);
      object-fit: cover;
      flex-shrink: 0;
    }}

    .rank-info-col {{
      display: flex;
      flex-direction: column;
      min-width: 0;
    }}

    .rank-name {{
      font-family: var(--font-display);
      font-size: 13px;
      font-weight: 800;
      color: var(--text-black);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .rank-amount-badge {{
      background: #fef08a;
      border: 1.5px solid var(--border-black);
      border-radius: 999px;
      padding: 3px 9px;
      font-family: var(--font-display);
      font-size: 11.5px;
      font-weight: 800;
      color: #121212;
      white-space: nowrap;
      flex-shrink: 0;
      box-shadow: 1.5px 1.5px 0px #121212;
    }}

    /* ======================================================================
       BOTTOM CTA & NAVIGATION BUTTONS BELOW BUTTON PUSH
       ====================================================================== */
    .cta-push-wrapper {{
      margin-top: 18px;
      width: 100%;
    }}

    .cta-push-btn {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 3px;
      width: 100%;
      background: #22c55e;
      border: 3px solid var(--border-black);
      border-radius: 16px;
      box-shadow: 4px 4px 0px #121212;
      padding: 12px 14px;
      text-decoration: none;
      color: #121212;
      transition: all 0.15s ease;
      cursor: pointer;
    }}

    .cta-push-btn:hover {{
      transform: translate(-1px, -1px);
      box-shadow: 6px 6px 0px #121212;
      background: #16a34a;
      color: #ffffff;
    }}

    .cta-push-btn:active {{
      transform: translate(2px, 2px);
      box-shadow: 1px 1px 0px #121212;
    }}

    .cta-top-tag {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: #121212;
      color: #ffffff;
      font-family: var(--font-display);
      font-size: 9.5px;
      font-weight: 900;
      padding: 2px 8px;
      border-radius: 999px;
      letter-spacing: 0.06em;
    }}

    .cta-main-title {{
      font-family: var(--font-display);
      font-size: 17px;
      font-weight: 900;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .cta-subtitle {{
      font-size: 11px;
      font-weight: 600;
      opacity: 0.9;
    }}

    /* Navigation Buttons below Button Push */
    .bottom-nav-row {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 14px;
      margin-bottom: 10px;
      width: 100%;
    }}

    .nav-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--card-white);
      border: 2px solid var(--border-black);
      box-shadow: 2.5px 2.5px 0px #121212;
      border-radius: 999px;
      padding: 6px 14px;
      font-family: var(--font-display);
      font-size: 11.5px;
      font-weight: 800;
      color: var(--text-black);
      text-decoration: none;
      transition: all 0.15s ease;
      cursor: pointer;
    }}

    .nav-btn:hover {{
      transform: translate(-1px, -1px);
      box-shadow: 3.5px 3.5px 0px #121212;
    }}

    .nav-btn:active {{
      transform: translate(1px, 1px);
      box-shadow: 1px 1px 0px #121212;
    }}

    /* Footer Watermark */
    .card-footer {{
      margin-top: 10px;
      text-align: center;
      font-size: 11px;
      font-weight: 700;
      color: var(--text-dim);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .live-dot-pulse {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background-color: #22c55e;
      box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
      animation: pulse-green 2s infinite;
      display: inline-block;
    }}

    @keyframes pulse-green {{
      0% {{
        transform: scale(0.95);
        box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
      }}
      70% {{
        transform: scale(1);
        box-shadow: 0 0 0 5px rgba(34, 197, 94, 0);
      }}
      100% {{
        transform: scale(0.95);
        box-shadow: 0 0 0 0 rgba(34, 197, 94, 0);
      }}
    }}

    /* Fluid scaling matching exact Top Sultan proportions on mobile */
    @media (max-width: 480px) {{
      .page-wrapper {{
        padding: 16px 10px 36px 10px;
      }}
      .neo-card {{
        padding: 20px 12px;
        border-radius: 24px;
      }}
      .leaderboard-title {{
        font-size: 26px;
      }}
      .filter-row {{
        gap: 6px;
      }}
      .pill-btn {{
        padding: 4px 10px;
        font-size: 11px;
      }}
      .period-static-badge {{
        padding: 4px 10px;
        font-size: 10.5px;
      }}
      .podium-section {{
        gap: 8px;
      }}
      .podium-avatar-wrapper {{
        width: 50px;
        height: 50px;
      }}
      .col-rank-1 .podium-avatar-wrapper {{
        width: 64px;
        height: 64px;
      }}
      .podium-name {{
        font-size: 11.5px;
        max-width: 85px;
      }}
      .col-rank-1 .podium-name {{
        font-size: 12.5px;
        max-width: 95px;
      }}
      .podium-amount {{
        font-size: 9.5px;
        padding: 2px 7px;
      }}
      .col-rank-1 .podium-amount {{
        font-size: 10px;
      }}
      .pedestal-number {{
        font-size: 22px;
      }}
      .col-rank-1 .pedestal-number {{
        font-size: 30px;
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
      .pedestal-label {{
        font-size: 8px;
        letter-spacing: 0.02em;
      }}
      .rank-row-card {{
        padding: 6px 10px;
      }}
      .rank-name {{
        font-size: 12px;
        max-width: 140px;
      }}
      .rank-amount-badge {{
        font-size: 10.5px;
        padding: 2.5px 7px;
      }}
      .bottom-nav-row {{
        gap: 6px;
      }}
      .nav-btn {{
        padding: 5px 10px;
        font-size: 10.5px;
        gap: 4px;
      }}
    }}
  </style>
</head>
<body>
  <div class="bg-dots"></div>

  <!-- Geometric Neo Stickers -->
  <div class="neo-decorations">
    <div class="neo-sticker sticker-star-1"><i class="fa-solid fa-star"></i></div>
    <div class="neo-sticker sticker-pill-1"><i class="fa-brands fa-tiktok"></i> TIKTOK LIVE</div>
    <div class="neo-sticker sticker-stripes">/// TOP RANK ///</div>
  </div>

  <main class="page-wrapper">
    <article class="neo-card">
      <div class="leaderboard-header">
        <div class="header-badge">
          <i class="fa-brands fa-tiktok"></i>
          <span>TIKTOK LIVE CENTER LEADERBOARD</span>
        </div>
        <h1 class="leaderboard-title" id="mainTitleText">
          <span>{page_title}</span>
          <i class="fa-solid fa-trophy" style="color: #eab308;"></i>
        </h1>
        <p class="leaderboard-subtitle">Daftar Peringkat Resmi Penonton &amp; Donatur Live @xumuid</p>
      </div>

      <!-- TikTok Live Center Interactive Tabs -->
      <div class="tiktok-tabs-wrapper">
        <button class="tab-btn {'active' if is_gifter_default else ''}" id="tabGiftsBtn" onclick="switchCategory('gifts')">
          <i class="fa-solid fa-gift" style="color: var(--tiktok-red);"></i> Most Gifts
        </button>
        <button class="tab-btn {'active' if not is_gifter_default else ''}" id="tabWatchBtn" onclick="switchCategory('watch')">
          <i class="fa-solid fa-clock" style="color: var(--tiktok-cyan);"></i> Most watch time
        </button>
      </div>

      <!-- Filter Controls: Total/Increase + Fixed 60 Days Badge -->
      <div class="filter-row">
        <div class="pill-filter-box">
          <button class="pill-btn active" id="btnFilterTotal" onclick="setSubFilter('total')">Total</button>
          <button class="pill-btn" id="btnFilterIncrease" onclick="setSubFilter('increase')">Increase</button>
        </div>

        <div class="period-static-badge" title="Periode 60 Hari Terakhir">
          <i class="fa-regular fa-calendar-check" style="font-size: 11px; color: var(--text-black);"></i>
          <span>60 Days</span>
        </div>
      </div>

      <!-- Top 1-3 Podium with 3D Pedestals -->
      <div class="podium-section" id="podiumContainer">
        <!-- Rendered dynamically -->
      </div>

      <!-- Peringkat 4 - 10 List -->
      <div class="list-header">
        <span class="list-title">
          <i class="fa-solid fa-list-ol"></i> PERINGKAT 4 - 10
        </span>
        <span class="list-counter">TOP 10</span>
      </div>

      <div class="ranks-stack" id="ranksListContainer" role="list">
        <!-- Rendered dynamically -->
      </div>

      <!-- CTA Button: Buka TikTok Live -->
      <div class="cta-push-wrapper">
        <a href="https://www.tiktok.com/@xumuid/live" class="cta-push-btn" target="_blank" rel="noopener noreferrer">
          <span class="cta-top-tag">
            <i class="fa-solid fa-bolt"></i> DUKUNG LIVE SEKARANG
          </span>
          <span class="cta-main-title">
            <i class="fa-brands fa-tiktok"></i>
            <span>BUKA TIKTOK LIVE!</span>
            <i class="fa-solid fa-bolt"></i>
          </span>
          <span class="cta-subtitle">Kirim Gift &amp; tonton live @xumuid untuk naik peringkat!</span>
        </a>
      </div>

      <!-- Navigation Buttons below Button Push (Portfolio, Top Sultan, Top Gifter, Penonton Setia) -->
      <div class="bottom-nav-row">
        <a href="index.html" class="nav-btn" title="Kembali ke Dashboard Portfolio">
          <i class="fa-solid fa-arrow-left"></i>
          <span>Portfolio</span>
        </a>
        <a href="Top Rank.html" class="nav-btn" style="background: var(--gold-rank);" title="Top Sultan Sociabuzz">
          <i class="fa-solid fa-crown" style="color: #ca8a04;"></i>
          <span>Top Sultan</span>
        </a>
        <a href="TopGifter.html" class="nav-btn" style="background: #ffe4e6; color: #e11d48; border-color: #f43f5e;" title="Top Gifter TikTok">
          <i class="fa-solid fa-gift"></i>
          <span>Top Gifter</span>
        </a>
        <a href="Penonton Setia.html" class="nav-btn" style="background: #e0f2fe; color: #0369a1; border-color: #38bdf8;" title="Penonton Setia TikTok">
          <i class="fa-solid fa-clock"></i>
          <span>Penonton Setia</span>
        </a>
      </div>

      <!-- Footer Watermark -->
      <footer class="card-footer">
        <span>© 2026 xumu id · TikTok Leaderboard</span>
        <span id="syncIndicator" style="display: inline-flex; align-items: center; gap: 4px; font-size: 10.5px; font-weight: 800; color: #16a34a; background: #dcfce7; padding: 1.5px 7px; border-radius: 999px; border: 1px solid #86efac;">
          <span class="live-dot-pulse"></span> Firebase Live
        </span>
      </footer>
    </article>
  </main>

  <script>
    const giftersDatasets = {json_gifters_all};
    const viewersDatasets = {json_viewers_all};

    let curCategory = "{default_tab}"; // 'gifts' or 'watch'
    let curPeriod = "60 days";         // 'Latest LIVE', '7 days', '28 days', '60 days'
    let curSubFilter = "total";        // 'total' or 'increase'

    const MEDAL_1 = "{medal_1}";
    const MEDAL_2 = "{medal_2}";
    const MEDAL_3 = "{medal_3}";

    function handleAvatarFallback(img, name) {{
      img.onerror = null;
      const initial = name ? name.charAt(0).toUpperCase() : 'U';
      const colors = ['#f472b6', '#38bdf8', '#fb923c', '#a78bfa', '#4ade80'];
      const bg = colors[name.charCodeAt(0) % colors.length];
      img.outerHTML = `<div class="${{img.className}}" style="background: ${{bg}}; display: flex; align-items: center; justify-content: center; font-weight: 900; color: #121212;">${{initial}}</div>`;
    }}

    function renderLeaderboard() {{
      const datasets = (curCategory === 'gifts') ? giftersDatasets : viewersDatasets;
      const periodData = datasets[curPeriod] || datasets["60 days"];
      const listData = periodData[curSubFilter] || periodData["total"];

      const labelLabel = (curCategory === 'gifts') ? 'COIN SULTAN' : 'WATCH TIME';
      const mainTitle = (curCategory === 'gifts') ? 'Top Gifter TikTok' : 'Penonton Setia TikTok';
      document.getElementById('mainTitleText').innerHTML = `<span>${{mainTitle}}</span> <i class="fa-solid fa-trophy" style="color: #eab308;"></i>`;

      const top1 = listData.find(d => d.rank === 1) || listData[0];
      const top2 = listData.find(d => d.rank === 2) || listData[1];
      const top3 = listData.find(d => d.rank === 3) || listData[2];
      const rest = listData.filter(d => d.rank > 3);

      function renderPodiumCol(d, rank, medalSrc) {{
        if (!d) return '';
        const isFirst = (rank === 1);
        const avatarSrc = d.avatar || `https://api.dicebear.com/7.x/bottts/svg?seed=${{encodeURIComponent(d.name)}}`;
        let badgeHtml = '';
        if (d.badge) {{
          const isSilver = d.badge.toLowerCase().includes('silver');
          const cleanText = d.badge.replace(/[^a-zA-Z0-9_ ]/g, '').trim();
          badgeHtml = `<span class="fan-pill ${{isSilver ? 'silver' : ''}}"><i class="fa-solid fa-heart" style="font-size: 8px; margin-right: 3px;"></i>${{cleanText}}</span>`;
        }}

        return `
          <div class="podium-col col-rank-${{rank}}">
            ${{isFirst ? '<div class="radiant-rays"></div><div class="radiant-halo"></div>' : ''}}
            <div class="podium-avatar-wrapper">
              ${{isFirst ? '<i class="fa-solid fa-crown crown-decal"></i>' : ''}}
              <div class="podium-avatar-frame">
                <img src="${{avatarSrc}}" class="avatar-img-circle" alt="${{d.name}}" referrerpolicy="no-referrer" onerror="handleAvatarFallback(this, '${{d.name}}')">
              </div>
              <div class="medal-corner-badge">${{rank}}</div>
            </div>

            <span class="podium-name" title="${{d.name}}">${{d.name}}</span>
            ${{badgeHtml}}
            <span class="podium-amount">${{d.amount}}</span>

            <div class="pedestal-block">
              <span class="pedestal-number">${{rank}}</span>
              <span class="pedestal-label">
                ${{isFirst ? '<i class="fa-solid fa-crown" style="font-size: 8.5px; margin-right: 2px;"></i>' : ''}} ${{labelLabel}}
              </span>
            </div>
          </div>
        `;
      }}

      // Render Podium 2, 1, 3
      document.getElementById('podiumContainer').innerHTML = `
        ${{renderPodiumCol(top2, 2, MEDAL_2)}}
        ${{renderPodiumCol(top1, 1, MEDAL_1)}}
        ${{renderPodiumCol(top3, 3, MEDAL_3)}}
      `;

      // Render Ranks 4-10
      document.getElementById('ranksListContainer').innerHTML = rest.map(d => {{
        const avatarSrc = d.avatar || `https://api.dicebear.com/7.x/bottts/svg?seed=${{encodeURIComponent(d.name)}}`;
        let badgeHtml = '';
        if (d.badge) {{
          const isSilver = d.badge.toLowerCase().includes('silver');
          const cleanText = d.badge.replace(/[^a-zA-Z0-9_ ]/g, '').trim();
          badgeHtml = `<span class="fan-pill ${{isSilver ? 'silver' : ''}}" style="margin: 0; margin-top: 2px;"><i class="fa-solid fa-heart" style="font-size: 8px; margin-right: 3px;"></i>${{cleanText}}</span>`;
        }}

        return `
          <div class="rank-row-card" role="listitem">
            <div class="rank-card-left">
              <div class="rank-number-box">#${{d.rank}}</div>
              <img src="${{avatarSrc}}" class="rank-avatar-img" alt="${{d.name}}" referrerpolicy="no-referrer" onerror="handleAvatarFallback(this, '${{d.name}}')">
              <div class="rank-info-col">
                <span class="rank-name">${{d.name}}</span>
                ${{badgeHtml}}
              </div>
            </div>
            <span class="rank-amount-badge">${{d.amount}}</span>
          </div>
        `;
      }}).join('');
    }}

    function switchCategory(cat) {{
      curCategory = cat;
      document.getElementById('tabGiftsBtn').classList.toggle('active', cat === 'gifts');
      document.getElementById('tabWatchBtn').classList.toggle('active', cat === 'watch');
      renderLeaderboard();
    }}

    function setSubFilter(filter) {{
      curSubFilter = filter;
      document.getElementById('btnFilterTotal').classList.toggle('active', filter === 'total');
      document.getElementById('btnFilterIncrease').classList.toggle('active', filter === 'increase');
      renderLeaderboard();
    }}

    // ======================================================================
    // FIREBASE REALTIME DATABASE SYNC (Path: /xumuid-dashboard/tiktok_leaderboard)
    // ======================================================================
    const FIREBASE_RTDB_URL = "https://xumuid-dashboard-default-rtdb.asia-southeast1.firebasedatabase.app/xumuid-dashboard/tiktok_leaderboard.json";

    function applyFirebaseUpdate(data) {{
      if (!data) return;
      let hasUpdate = false;
      if (data.top_gifters && data.top_gifters.gifters && Array.isArray(data.top_gifters.gifters)) {{
        giftersDatasets["60 days"]["total"] = data.top_gifters.gifters.map(g => ({{
          rank: g.rank,
          name: g.display_name || g.username,
          amount: `${{Number(g.coins).toLocaleString()}} Coins`,
          badge: g.badge || '',
          avatar: g.avatar || ''
        }}));
        hasUpdate = true;
      }}
      if (data.penonton_setia && data.penonton_setia.viewers && Array.isArray(data.penonton_setia.viewers)) {{
        viewersDatasets["60 days"]["total"] = data.penonton_setia.viewers.map(v => ({{
          rank: v.rank,
          name: v.display_name || v.username,
          amount: v.watch_time_str || `${{Math.round(v.watch_time_minutes / 60)}}h`,
          badge: v.badge || '',
          avatar: v.avatar || ''
        }}));
        hasUpdate = true;
      }}
      if (hasUpdate) {{
        renderLeaderboard();
        const ind = document.getElementById('syncIndicator');
        if (ind) {{
          ind.style.display = 'inline-flex';
          ind.title = 'Terhubung & Sinkron Realtime dengan Firebase';
        }}
      }}
    }}

    function initFirebaseLiveSync() {{
      // 1. Initial REST Fetch for instant freshness
      fetch(FIREBASE_RTDB_URL)
        .then(res => res.json())
        .then(data => {{
          if (data) applyFirebaseUpdate(data);
        }})
        .catch(err => console.log('Firebase fetch fallback active'));

      // 2. Realtime SSE Stream (push updates directly on change)
      if (typeof EventSource !== 'undefined') {{
        try {{
          const sse = new EventSource(FIREBASE_RTDB_URL);
          sse.addEventListener('put', function(e) {{
            try {{
              const res = JSON.parse(e.data);
              if (res && res.data) {{
                applyFirebaseUpdate(res.data);
              }}
            }} catch(err) {{}}
          }});
          sse.addEventListener('patch', function(e) {{
            try {{
              const res = JSON.parse(e.data);
              if (res && res.data) {{
                applyFirebaseUpdate(res.data);
              }}
            }} catch(err) {{}}
          }});
          sse.onerror = function() {{
            // Automatic reconnection handled by browser
          }};
        }} catch(e) {{
          console.warn('SSE unsupported:', e);
        }}
      }}

      // 3. Tab focus auto-refresh
      document.addEventListener('visibilitychange', function() {{
        if (!document.hidden) {{
          fetch(FIREBASE_RTDB_URL)
            .then(res => res.json())
            .then(data => {{ if (data) applyFirebaseUpdate(data); }})
            .catch(() => {{}});
        }}
      }});
    }}

    // Initial Local Render
    renderLeaderboard();

    // Start Live Sync
    initFirebaseLiveSync();
  </script>
</body>
</html>'''

    with open(target_filename, 'w', encoding='utf-8') as out:
        out.write(html)
    print(f"Generated {target_filename} successfully ({len(html)} bytes)")

generate_page('gifts')
generate_page('watch')
