#!/usr/bin/env python3

"""Starts a web server that provides a web app interface to the remote control."""

__author__ = "Garrett Heath Koller"
__copyright__ = "Copyright 2017, Garrett Heath Koller"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Garrett Heath Koller"
__email__ = "garrettheath4@gmail.com"
__status__ = "Prototype"

from http.server import BaseHTTPRequestHandler, HTTPServer

# Source: https://gist.github.com/bradmontgomery/2219997
class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(bytes("<html><body><h1>Hellow, orld!</h1></body></html>", "utf-8"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(bytes("<html><body><h1>POST!</h1></body></html>", "utf-8"))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port %s ...' % port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=init(argv[1]))
    else:
        run()

