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
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess


# Source: https://gist.github.com/bradmontgomery/2219997
class Routes(BaseHTTPRequestHandler):

    def _set_headers(self, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _send_not_found(self):
        self.send_error(404, "File Not Found", "%s does not exist" % self.path)

    def do_GET(self):
        content_types = {
            '.html': 'text/html',
            '.htm':  'text/html',
            '.ico':  'image/x-icon',
            '.svg':  'image/svg+xml',
            '.css':  'text/css',
            '.js':   'application/javascript',
            '.json': 'application/json',
            '.map':  'application/x-navimap'
        }
        static_folder = 'webapp' + sep + 'build'
        file_extension_search = re.search('\\.[a-zA-Z]+$',
                                          self.path.split('?')[0])

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
        elif file_extension_search \
                and file_extension_search.group(0) in content_types:
            self._set_headers(content_types[file_extension_search.group(0)])
            try:
                f = open(curdir + sep + static_folder + sep + self.path, 'rb')
                self.wfile.write(f.read())
                f.close()
            except IOError:
                self._send_not_found()
        elif '.' in self.path:
            # Request is probably for a file that is not an approved extension
            self._send_not_found()
        else:
            self._send_not_found()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        routes = {
            '/api/test': "echo hello world",
            '/api/source/rpi': "echo as | cec-client RPI -s -d 1",
            '/api/source/chromebox': "echo 'tx 1F:82:10:00' | cec-client RPI --single-command --log-level 1",
            '/api/volume/up': "echo 'tx 10:44:41' | cec-client RPI --single-command --log-level 1; echo 'tx 10:45' | cec-client RPI --single-command --log-level 1",
            '/api/volume/down': "echo 'tx 10:44:42' | cec-client RPI --single-command --log-level 1; echo 'tx 10:45' | cec-client RPI --single-command --log-level 1",
        }
        if self.path in routes:
            subprocess.Popen(['sh', '-c', routes[self.path]])
            self._set_headers()
            self.wfile.write(bytes(
                "<html><body><h1>POST!</h1></body></html>",
                "utf-8"))
        else:
            self._send_not_found()


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
