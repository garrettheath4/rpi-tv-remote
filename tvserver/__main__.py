#!/usr/bin/env python3

"""Starts a web server that provides a TV remote control web app."""

__author__ = "Garrett Heath Koller"
__copyright__ = "Copyright 2017, Garrett Heath Koller"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Garrett Heath Koller"
__email__ = "garrettheath4@gmail.com"
__status__ = "Prototype"

from os import curdir, sep
from http.server import BaseHTTPRequestHandler, HTTPServer


# Source: https://gist.github.com/bradmontgomery/2219997
class Routes(BaseHTTPRequestHandler):
    def _set_headers(self, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        static_folder = 'webapp' + sep + 'build'
        if '..' in self.path:
            error_name = "Illegal Path"
            error_message = ("Path requested contains illegal '..' substring"
                             "- %s") % self.path
            self.send_error(403, error_name, error_message)
        elif '/.' in self.path:
            error_name = "Illegal Path"
            error_message = ("Path requested contains illegal '/.' substring"
                             "- %s") % self.path
            self.send_error(403, error_name, error_message)
        elif '~' in self.path:
            error_name = "Illegal Path"
            error_message = ("Path requested contains illegal '~' character"
                             "- %s") % self.path
            self.send_error(403, error_name, error_message)
        elif self.path.split("?")[0].endswith(".html") \
                or self.path.endswith(".ico") \
                or self.path.endswith(".svg") \
                or self.path.endswith(".css") \
                or self.path.endswith(".js") \
                or self.path.endswith(".map"):
            if self.path.endswith(".html") or self.path.endswith(".htm"):
                self._set_headers("text/html")
            elif self.path.endswith(".ico"):
                self._set_headers("image/x-icon")
            elif self.path.endswith(".svg"):
                self._set_headers("image/svg+xml")
            elif self.path.endswith(".css"):
                self._set_headers("text/css")
            elif self.path.endswith(".js"):
                self._set_headers("application/javascript")
            elif self.path.endswith(".map"):
                self._set_headers("application/x-navimap")
            else:
                self._set_headers()
            try:
                f = open(curdir + sep + static_folder + sep + self.path, 'rb')
                self.wfile.write(f.read())
                f.close()
            except IOError:
                self.send_error(404, "File Not Found",
                                "%s does not exist" % self.path)
        elif '.' in self.path:
            # Request is probably for a file that is not an approved extension
            self.send_error(404, "File Not Found",
                            "%s does not exist" % self.path)
        else:
            self._set_headers()
            self.wfile.write(bytes(
                ("<html><body>"
                 "<h1>Hellow, orld!</h1>"
                 "<p>You accessed path: %s</p>"
                 "</body></html>") % self.path,
                "utf-8"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(bytes(
            "<html><body><h1>POST!</h1></body></html>",
            "utf-8"))


def run(server_class=HTTPServer, handler_class=Routes, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port %s ...' % port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("^C received, shutting down server")
        httpd.socket.close()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
