
import BaseHTTPServer, SimpleHTTPServer
import ssl
import logging
import cgi

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            logging.error(item)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = ServerHandler

httpd = BaseHTTPServer.HTTPServer(('10.1.1.185', 443), Handler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()
