from django.shortcuts import render
from django.http import HttpResponse,\
                        HttpResponseBadRequest,\
                        HttpResponseNotFound,\
                        HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote
from .models import URL

# Create your views here.

enlace_inicio = '''
<a href='http://localhost:8000/' <a><h2>Acortar otra url</h2></body></html>    
'''

page_not_found = '''
El recurso {path} no puede ser atendido''' + enlace_inicio

@csrf_exempt
def inicio(request):

    info_url = '''
    <a href='{url}' <a>{url}</a>
    ------
    <a href='http://localhost:8000/{id}' <a>localhost:8000/{id}</a>
    <br>'''

    def print_db():
        urls = URL.objects.all()
        lista = 'URLS ALMACENADAS' + '<br>'
        for url in urls:
            lista = lista + info_url.format(url=url.URL_larga,id=url.id)
        return lista

    formulario = '''
    \n\n<br>
     <form action="" method="POST">
      Introduce URL que desea acortar<br>
      <input type="text" name="url_from_formulario"<br><br>
      <input type="submit" value="Enviar">
    </form> 
   '''

    welcome_page = '''
    <h1>Acortador de urls</h1>
    ''' + formulario + print_db()

    no_url_insert = '''
    No has introducido ninguna URL''' + enlace_inicio

    already_shorcut = '''
    Esta URL ya ha sido acortada <br>''' + info_url + enlace_inicio

    new_shorcut = '''
    <h1>Has acortado una URL</h1>
    <h3>URL original: </h3>
    <a href='{url}' <a>{url}</a>
    <h3>URL acordada:</h3>
    <a href='http://localhost:8000/{id}' <a>localhost:8000/{id}</a>
     ''' + enlace_inicio


    def add_http(url):
        if url[0:4] != 'http':
            url = 'http://' + url
        return url

    if request.method == 'GET':
        return HttpResponse(welcome_page)
    elif request.method == 'POST':
        '''NOTA: request.body me devuelve el cuerpo como un byte string.
        request.POST devuelve el el valor del campo cuya clave va en [] que aparece en el formulario'''
        nueva_url = request.POST['url_from_formulario']
        if len(nueva_url) == 0:
            return HttpResponseBadRequest(no_url_insert)
        else:
            nueva_url = add_http(nueva_url)

            try:
                url_in_db = URL.objects.get(URL_larga = nueva_url)
                return HttpResponseBadRequest(already_shorcut.format(url=url_in_db.URL_larga,
                                                                    id=url_in_db.id))
            except:
                # No existe, creo una entrada nueva
                url_in_db = URL(URL_larga=nueva_url)
                url_in_db.save()
                return HttpResponse(new_shorcut.format(url=url_in_db,id=url_in_db.id))


def ya_acortada(request, id):
    try:
        url_existia = URL.objects.get(id = id).URL_larga
        print(url_existia)
        return HttpResponseRedirect(url_existia)
    except:
        return HttpResponseNotFound(page_not_found.format(path=request.path))

def not_found(request):
    return HttpResponse(page_not_found.format(path=request.path))