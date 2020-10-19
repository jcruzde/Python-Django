#!/usr/bin/python3.6

import webapp

class adiosApp(webapp.webApp):
    def process(self,parsedRequest):
        return ("200 OK", "<html><body><h1>Adios mundo cruel</h1></body></html>")

if __name__ == "__main__":
    objeto_adios = adiosApp("localhost", 1234)
    # Objeto = clase(parámetros)
