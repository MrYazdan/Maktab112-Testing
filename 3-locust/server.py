from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", 'application/json')
        self.end_headers()
        self.wfile.write(b'{"maktab": 112}')


if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 8091), Handler)
    print("Starting server on http://127.0.0.1:8091")
    server.serve_forever()


