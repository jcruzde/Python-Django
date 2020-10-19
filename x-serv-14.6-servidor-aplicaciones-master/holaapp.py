#!/usr/bin/python3.6

import webapp

class holaApp(webapp.webApp):
    def process(self,parsedRequest):
        return ("200 OK", "<html><body><h1>Hola Mundo</h1></body></html>")

if __name__ == "__main__":
    objeto_hola = holaApp("localhost", 1234)
    # Objeto = clase(parámetros)
