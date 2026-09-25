"""
Sync local top_gifters.json and penonton_setia.json to Firebase Realtime Database
Path: /xumuid-dashboard/tiktok_leaderboard
"""
import json
import urllib.request
import datetime

FIREBASE_URL = "https://xumuid-dashboard-default-rtdb.asia-southeast1.firebasedatabase.app/xumuid-dashboard/tiktok_leaderboard.json"

def sync():
    with open("top_gifters.json", "r", encoding="utf-8") as f:
        gifters = json.load(f)
    with open("penonton_setia.json", "r", encoding="utf-8") as f:
        viewers = json.load(f)

    payload = {
        "top_gifters": gifters,
        "penonton_setia": viewers,
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        FIREBASE_URL,
        data=data_bytes,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="PUT"
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                print("[BERHASIL] Data lokal berhasil disinkronkan ke Firebase xumuid-dashboard!")
            else:
                print(f"[PERINGATAN] Respon Firebase: {response.status}")
    except Exception as e:
        print(f"[GAGAL] Terjadi kesalahan saat sinkronisasi: {e}")

if __name__ == "__main__":
    sync()
