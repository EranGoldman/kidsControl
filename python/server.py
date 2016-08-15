"""kids control python server."""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, listdir, path

PORT_NUMBER = 8000

DEFAULTHEADER = '''
                <!DOCTYPE html>
                <head>
                <meta charset="UTF-8">
                <title>Title of the document</title>
                </head>
                <body>
                '''
DEFAULTFOOTER = '''
                </body>
                </html>
                '''


# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):
    """standart http handler."""

    def get_module(self):
        """Build the module page."""
        return "ok"

    def build_index(self):
        """Build the default index."""
        index = DEFAULTHEADER
        modulesList = ""
        modulesDir = path.join(curdir, 'modules')
        for fname in listdir(modulesDir):
            fpath = path.join(modulesDir, fname)
            if not path.isdir(fpath):
                continue
            else:
                modulesList += "<li>" + fname + "</li>"
        index += "<ol>" + modulesList + "</ol>"
        index += DEFAULTFOOTER
        return index

    # Handler for the GET requests
    def do_GET(self):
        """Handler for the GET requests."""
        html = 'Ooops something went wrong - \
                please contact <a href="mailto:erangoldman@gmail.com">Eran</a>'
        if self.path == "/" or self.path == "/index.html":
            self.path = "/index.html"
            html = self.build_index()
        else:
            html = self.get_module()

        try:
            # Check the file extension required and
            # set the right mime type

            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True
            else:
                mimetype = 'text/html'
                sendReply = True

            if sendReply is True:
                # Open the static file requested and send it
                # f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(html)  # f.read())
                #  f.close()
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    # Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
