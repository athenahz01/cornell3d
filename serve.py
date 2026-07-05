"""Static server + /shot endpoint so the page can save canvas captures to disk."""
import base64
import http.server
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def do_POST(self):
        if self.path.startswith('/shot'):
            n = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(n).decode()
            b64 = data.split(',', 1)[1]
            name = self.path.split('=')[-1] if '=' in self.path else 'shot'
            name = ''.join(ch for ch in name if ch.isalnum() or ch in '-_') or 'shot'
            os.makedirs(os.path.join(ROOT, '_shots'), exist_ok=True)
            with open(os.path.join(ROOT, '_shots', name + '.jpg'), 'wb') as f:
                f.write(base64.b64decode(b64))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'ok')
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, *a):
        pass


http.server.ThreadingHTTPServer(('127.0.0.1', 8741), Handler).serve_forever()
