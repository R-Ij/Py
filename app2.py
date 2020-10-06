from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloServerHandler(BaseHTTPRequestHandler):

    def do_get(self):
        self.send_response(200)
        self.end_headers()
        # byte文字列でないとエラー
        self.wfile.write(b'Sample web server')
        return


# if __name__ == '__main__':
server = HTTPServer(('', 5000), HelloServerHandler)
server.serve_forever()
