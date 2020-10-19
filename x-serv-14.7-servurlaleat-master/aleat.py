#!/usr/bin/python3.6

import webapp

class Url_aleat(webapp.webApp):
        
    def process(self, parsedRequest):

        import random
        numero = str(random.randint(1,1000))
        url = "<a href='http://" + 'localhost' + ":" + str(1234) + "/" + str(numero) + "'>Dame otra</a>"
        # DUDA: No me reconoce port como variable de esta clase.
        return ("200 OK", "<html><body><h1>Hola</h1>" + url + "</body></html>" + "\r\n")
        
if __name__ == "__main__":
    objet_url_aleat = Url_aleat("localhost", 1234)
