import http.server
import socketserver
import json
import os
import urllib.parse
from datetime import datetime

PORT = 5000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class TikTokSyncHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS for browser integration & TikTok LiveCenter script
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "OK")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        
        if parsed.path == '/api/top-gifters':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            file_path = os.path.join(DIRECTORY, 'top_gifters.json')
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b'{"gifters":[]}')
            return

        elif parsed.path == '/api/penonton-setia':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            file_path = os.path.join(DIRECTORY, 'penonton_setia.json')
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b'{"viewers":[]}')
            return

        elif parsed.path == '/':
            self.path = '/TopGifter.html'
            return super().do_GET()

        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len)

        try:
            payload = json.loads(post_body.decode('utf-8'))
        except Exception as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(f'{{"error": "Invalid JSON: {str(e)}"}}'.encode('utf-8'))
            return

        if parsed.path == '/api/sync-gifters':
            payload['updated_at'] = datetime.now().isoformat()
            target = os.path.join(DIRECTORY, 'top_gifters.json')
            with open(target, 'w', encoding='utf-8') as f:
                json.dump(payload, f, indent=2, ensure_ascii=False)
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Updated top_gifters.json with {len(payload.get('gifters', []))} donors!")
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok","message":"Top Gifters synced successfully"}')
            return

        elif parsed.path == '/api/sync-watchtime':
            payload['updated_at'] = datetime.now().isoformat()
            target = os.path.join(DIRECTORY, 'penonton_setia.json')
            with open(target, 'w', encoding='utf-8') as f:
                json.dump(payload, f, indent=2, ensure_ascii=False)
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Updated penonton_setia.json with {len(payload.get('viewers', []))} loyal viewers!")
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok","message":"Penonton Setia synced successfully"}')
            return

        self.send_response(404)
        self.end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), TikTokSyncHandler) as httpd:
        print("="*65)
        print(f"  TIKTOK LIVE REALTIME SYNC SERVER READY ON PORT {PORT}")
        print("="*65)
        print(f"  * Top Gifter Page   : http://localhost:{PORT}/TopGifter.html")
        print(f"  * Penonton Setia    : http://localhost:{PORT}/Penonton%20Setia.html")
        print(f"  * API Top Gifters   : http://localhost:{PORT}/api/top-gifters")
        print(f"  * API Penonton Setia: http://localhost:{PORT}/api/penonton-setia")
        print("="*65)
        print("  Press Ctrl+C to stop server.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
