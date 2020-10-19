#!/usr/bin/python3.6

# JORGE CRUZ DE LA HAZA
# Doble grado en Ingeniería en Sistemas de Telecom. y ADE.

import webapp
from urllib.parse import unquote


Nº_ID = 0

FORMULARIO = """
\n\n<br>
 <form action="" method="POST">
  Introduce URL que desea acortar<br>
  <input type="text" name="url_larga"<br><br>
  <input type="submit" value="Enviar">
</form> 
"""

REDIRECCION = """
<html>
<head>
<meta http-equiv="Refresh" content="10;url={url}">
</head>

<body>
<p><h3>This resource is a shorcut of {url}.
<br>You will be automatically redirected in 10 seconds.</h3>
Otherwise, you can access by clicking <a href="{url}">here</a></p>
</body>
</html>
"""

class SHORTENER(webapp.webApp):

    urls = {}
    identificadores = {}
    
    def parse(self,request):
        method, resource, _ = request.split(' ', 2)
        body = request.split('\r\n\r\n',1)[1]
        print('Method: ', method)
        print('Resource: ', resource)
        print('Body: ', body)
        print('\n')
        return resource, method, body
        
    def process(self,parsedRequest):
        global Nº_ID
        
        resource, method, body = parsedRequest
        
        print('Voy a ver el metodo')
        if method == "GET":
            print('Detecto un GET')
            if resource == "/":
                print('Recibo barra')
                return ("200 OK", "<html><body><h1>Acortador de urls</h1>"
                + FORMULARIO
                + "URLs ya acortadas [url: ID]<br> " + str(self.urls) + "<br>"
                + "</body></html>")
            else:
                print('Recurso que no es barra')
                print('Resource: ', resource)
                try:
                    identificador = resource.split('/')[1]
                    print('Identificador: ', identificador)
                    url_redi = self.identificadores[identificador]
                    print('Redireccion: ', url_redi)
                    return ("300 OK", REDIRECCION.format(url=url_redi))
                except KeyError:
                    print('Esta clave o recurso no lo tengo identificado')
                    return ("400 Not Found", "<html><body>Sorry, resource "
                            + resource + " not found" 
                            + "<a href='http://localhost:1234/' <a><h2>Acortar otra url</h2></body></html>")
            
        if method == "POST":
            print('Detecto un POST')
            if not body:
                # Probrar estos casos con HTTP request maker
                print('El cuerpo está vacío, ignoro esta petición (Evío la página de inicio)')
                return ("404 Error", "<html><body>Sorry, we can't attend POST request without qs"
                        + "<a href='http://localhost:1234/' <a><h2>Acortar otra url</h2></body></html>")
            else:
                inicio_url = str(body.split('=')[1])[:4]
                
                url_larga = ''
                if inicio_url != "http":
                    print('Tengo que añadirle el http:// a la url')
                    url_larga = "http://"
                    
                url_larga = url_larga + unquote(body.split('=')[1])
                
                try:
                    print('Url ya cortada')
                    my_id = self.urls[url_larga]
                    return ("200 OK", "<html><body><h1>Esta URL ya ha sido cortada</h1>"
                    + "<h3>URL original: </h3>" 
                    + "<a href='" + str(url_larga) + "'<a>" + str(url_larga) + "</a>"
                    + "<h3>URL acordada:</h3>"
                    + "<a href='http://localhost:1234/" + str(my_id) + "'<a>localhost:1234/" + str(my_id) + "</a>"
                    + "<a href='http://localhost:1234/' <a><h2>Acortar otra url</h2>"
                    + "</body></html>")
                    
                except KeyError:
                    # Si no la encuentra es que esa url aún no ha sido cortada.
                    self.urls[url_larga] = Nº_ID
                    self.identificadores[str(Nº_ID)] = url_larga
                    Nº_ID += 1
                    
                    return ("200 OK", "<html><body><h1>Has acortado una URL</h1>"
                    + "<h3>URL original: </h3>" 
                    + "<a href='" + str(url_larga) + "'<a>" + str(url_larga) + "</a>"
                    + "<h3>URL acordada:</h3>"
                    + "<a href='http://localhost:1234/" + str(Nº_ID-1) + "'<a>localhost:1234/" + str(Nº_ID-1) + "</a>"
                    + "<a href='http://localhost:1234/' <a><h2>Acortar otra url</h2>"
                    + "</body></html>")

if __name__ == "__main__":
    ShortenerApp = SHORTENER("localhost", 1234)

