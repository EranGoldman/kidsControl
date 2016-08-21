"""kids control python server."""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, listdir, path
from urlparse import urlparse, parse_qs
import importlib

PORT_NUMBER = 8000

DEFAULTHEADER = '''
    <!DOCTYPE html>
    <head>
    <meta charset="UTF-8">
    <title>Kids control 0.1</title>
    <link rel="stylesheet" type="text/css" href="public/css/bootstrap.min.css">
    </head>
    <body>
    '''
DEFAULTFOOTER = '''
                </body>
                <script src="public/js/jquery-3.1.0.min.js"></script>
                <script src="public/js/bootstrap.min.js"></script>
                </html>
                '''
ROWSTART = '''
    <div class="row">
    '''
ROWEND = '''
    </div>
    '''
WIDGETSTART = '''
    <div class="col-md-4">
    '''
WIDGETEND = '''</div>'''


# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):
    """standart http handler."""

    def get_module(self):
        """Build the module page."""
        # modulesDir = path.join(curdir, 'modules')
        index = DEFAULTHEADER
        modulesDir = path.join(curdir, 'modules')
        module = ((self.path[1:]).split('/')[0]).split("?")[0]
        if module in listdir(modulesDir):
            mod = importlib.import_module('modules.' + module + '.base')
            mod_class = getattr(mod, module)
            klass = mod_class()
            urlVars = parse_qs(urlparse(self.path).query)
            if 'action' in urlVars:
                index += klass.getPage(urlVars['action'][0])
            else:
                index += klass.getPage()
        else:
            index += "Unknown module.<br>"
            index += " <a href='index.html'> Return to home page </a>"
        index += DEFAULTFOOTER
        return index

    def build_index(self):
        """Build the default index."""
        widgetCounter = 0
        index = DEFAULTHEADER
        modulesList = ""
        modulesDir = path.join(curdir, 'modules')
        modulesList += ROWSTART
        for fname in listdir(modulesDir):
            fpath = path.join(modulesDir, fname)
            if not path.isdir(fpath):
                continue
            else:
                modulesList += WIDGETSTART
                modulesList += "<h2><a href='"+fname + "'>"
                modulesList += str.upper(fname) + "</a></h2>"
                mod = importlib.import_module('modules.' + fname + '.base')
                mod_class = getattr(mod, fname)
                klass = mod_class()
                urlVars = parse_qs(urlparse(self.path).query)
                modulesList += klass.getWidget(urlVars)
                modulesList += WIDGETEND
                widgetCounter += 1
                if widgetCounter == 3:
                    modulesList += ROWEND + ROWSTART
                    widgetCounter = 0
        modulesList += ROWEND
        index += modulesList
        index += DEFAULTFOOTER
        return index

    def get_mime(self):
        """Get the mime of the path."""
        if self.path.endswith(".html"):
            return 'text/html'
        if self.path.endswith(".jpg"):
            return 'image/jpg'
        if self.path.endswith(".gif"):
            return 'image/gif'
        if self.path.endswith(".js"):
            return 'application/javascript'
        if self.path.endswith(".css"):
            return 'text/css'
        else:
            return 'text/html'

    def get_public_file(self):
        """Get the file from public folder."""
        index = ""
        pubFile = "." + self.path
        pubFile = pubFile.split('?')[0]
        if path.isfile(pubFile):
            f = open(pubFile)
            index = f.read()
            f.close()
        return index

    # Handler for the GET requests
    def do_GET(self):
        """Handler for the GET requests."""
        html = 'Ooops something went wrong - \
                please contact <a href="mailto:erangoldman@gmail.com">Eran</a>'

        """Router implementation."""
        if self.path == "/" or "index.html" in self.path:
            # self.path = "/index.html"
            html = self.build_index()
        elif "/public" in self.path[:7]:
                html = self.get_public_file()
        else:
            if "action" not in self.path:
                if "?" in self.path:
                    self.path += "&action=None"
                else:
                    self.path += "?action=None"
            html = self.get_module()

        try:
            # Check the file extension required and
            # set the right mime type

            # Open the static file requested and send it
            # f = open(curdir + sep + self.path)
            mimetype = self.get_mime()
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
