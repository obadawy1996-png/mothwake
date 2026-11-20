"""Serves publish/youtube on 127.0.0.1 only, so the YouTube Studio page in the in-app browser can fetch the masters."""
import http.server, functools, os
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "https://studio.youtube.com")
        self.send_header("Access-Control-Allow-Private-Network", "true")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        super().end_headers()
    def do_OPTIONS(self):
        self.send_response(204); self.end_headers()
d = os.path.dirname(os.path.abspath(__file__))
http.server.ThreadingHTTPServer(("127.0.0.1", 8765), functools.partial(H, directory=d)).serve_forever()
