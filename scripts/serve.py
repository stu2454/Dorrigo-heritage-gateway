"""Preview the static site at its GitHub Pages project path."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1] / 'site'
PREFIX = '/Dorrigo-heritage-gateway'

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path in ('/', PREFIX):
            self.send_response(302)
            self.send_header('Location', PREFIX + '/')
            self.end_headers()
        elif path.startswith(PREFIX + '/'):
            self.path = self.path[len(PREFIX):]
            super().do_GET()
        else:
            self.send_error(404)

if __name__ == '__main__':
    print('Preview: http://127.0.0.1:8000' + PREFIX + '/', flush=True)
    ThreadingHTTPServer(('127.0.0.1', 8000), Handler).serve_forever()
