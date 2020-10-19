#!/usr/bin/python3.6

import webapp

class Sumador(webapp.webApp):  
    
    def parse(self,request):
        resource = request.split()[1][1:]
        return resource.split('/')
        
    def process(self,parsedRequest):
        num1 = int(parsedRequest[0])
        num2 = int(parsedRequest[1])
        suma = num1 + num2
        return ("200 OK", "<html><body><h1>La suma es: " + str(suma) +  "</h1></body></html>")

if __name__ == "__main__":
    object_sumador = Sumador("localhost", 1234)

