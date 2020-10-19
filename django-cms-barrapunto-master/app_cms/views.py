from django.shortcuts import render
from django.http import HttpResponse
from .models import Recurso
from django.views.decorators.csrf import csrf_exempt

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string
from urllib.parse import unquote
import urllib.request

# Create your views here.

formulario = """
<form action="" method="POST">
    Contenido:<br>
    <input type="text" name="contenido" value="{content}"><br>
    <input type="submit" value="Enviar">
</form>

"""

titulos = ""

def get_titulares():

    titulos_template = """
        <html>
        <body>
            <h2>Titulares de barrapunto</h2>
            {contenido}
        </body>
        </html>
    """

    class CounterHandler(ContentHandler):

        def __init__(self):
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
            global titulos

            if name == 'item':
                self.in_item = False
            elif name == 'title' and self.in_item:
                self.titulo = self.theContent
                self.in_content = False
                self.theContent = ""
            elif name == 'link' and self.in_item:
                titulos += "<li><a href='" + self.theContent + "'<a>" + self.titulo + "</a></li>"
                self.in_content = False
                self.theContent = ""

        def characters(self, content):
            if self.in_content:
                self.theContent = self.theContent + content

    NewsParser = make_parser()  # Parser genérico de sax
    NewsHandler = CounterHandler()  # Me quedo con las cosas que me interesan
    NewsParser.setContentHandler(NewsHandler)

    xmlFile = urllib.request.urlopen("http://barrapunto.com/index.rss")
    NewsParser.parse(xmlFile)
    todos_los_titulos = titulos_template.format(contenido=titulos)
    return todos_los_titulos

titulos_html = get_titulares()

def index(request):
    respuesta = '<h1>Recursos almacenados</h1>'
    recursos = Recurso.objects.all()
    if len(recursos) == 0:
        respuesta += 'No hay recursos almacenados en la BD'
    else:
        respuesta += '<lu>'
        for recurso in recursos:
            respuesta += '<li>' + recurso.nombre + ' -- ' \
                         + recurso.contenido + '</li>'
        respuesta += '</lu>'

        respuesta += titulos_html
    return HttpResponse(respuesta)

@csrf_exempt
def nuevo(request, recurso):
    respuesta = '<h1>Contenido para el recurso ' + recurso + '</h1>'
    if request.method == "GET":
        try:
            # Compruebo si existe para poner en el formulario el contenido que tenía.
            recurso_in_BD = Recurso.objects.get(nombre=recurso)
            respuesta += 'Ya esxistia'
            contenido = recurso_in_BD.contenido
        except Recurso.DoesNotExist:
            respuesta += 'Nuevo recurso'
            contenido = ""

    elif request.method == "POST":
        try:
            # Compruebo si el recurso ya existe para no tener duplicados.
            r = Recurso.objects.get(nombre=recurso)
        except Recurso.DoesNotExist:
            r = Recurso(nombre=recurso)

        # El contenido siempre lo actualizo
        r.contenido = request.POST['contenido']
        r.save()
        respuesta += 'Contenido actualizado'
        contenido = r.contenido

    respuesta += formulario.format(content=contenido)

    respuesta += titulos_html
    return HttpResponse(respuesta)