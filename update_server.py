import http.server
import socketserver

PORT = 8000
DIRECTORY = "updates"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving updates at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
