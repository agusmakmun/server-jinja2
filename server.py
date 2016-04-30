# -*- coding: utf-8 -*-

import BaseHTTPServer
from jinja2 import Environment, PackageLoader

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        env = Environment(loader=PackageLoader('app', 'templates'))
        template = env.get_template('index.html')
        self.wfile.write(template.render(site='Awesome Site', name='Agus Makmun'))
        return True

print "Listening on port 8000..."
server = BaseHTTPServer.HTTPServer(('', 8000), MyHandler)
server.serve_forever()
