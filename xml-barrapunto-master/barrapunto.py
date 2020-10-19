#!/usr/bin/python3

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string
from urllib.parse import unquote
from urllib import request


class CounterHandler(ContentHandler):

    def __init__ (self):
        self.in_item = False
        self.in_content = False
        self.theContent = ""
        self.titulo = ""

    def startElement(self, name, attrs):
        if name == 'item':
            self.in_item = True
        if name == 'title' and self.in_item:
            self.in_content = True
        if name == 'link' and self.in_item:
            self.in_content = True

    def endElement(self, name):
        if name == 'item':
            self.in_item = False
        elif name == 'title' and self.in_item:
            self.titulo = self.theContent
            self.in_content = False
            self.theContent = ""
        elif name == 'link' and self.in_item:
            print("<p><a href='" + self.theContent + "'<a>" + self.titulo + "</a></p>")
            self.in_content = False
            self.theContent = ""


    def characters(self, content):
        if self.in_content:
            self.theContent = self.theContent + content

if len(sys.argv)<2:
    print("Usage: ./barrapunto.py <document>")
    print()
    print(" <URL>: url of the document to parse")
    sys.exit(1)

NewsParser = make_parser() # Parser genérico de sax
NewsHandler = CounterHandler() # Me quedo con las cosas que me interesan
NewsParser.setContentHandler(NewsHandler)

url = sys.argv[1]
# http://barrapunto.com/index.rss
xmfile = request.urlopen(url)
print('<html>')
print('<body>')
NewsParser.parse(url)
print('</body>')
print('</html>')