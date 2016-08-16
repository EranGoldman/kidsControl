"""HTML builder for the server.py."""

from os import curdir, listdir, pathfrom os import curdir, listdir, path

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
class htmlBuilder:
    def gethtml(path):
        
