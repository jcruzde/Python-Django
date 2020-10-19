from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from . import calculadora

RESPONSE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <p>{n1} {oper} {n2} = {result}</p>
  </body>
</html>
"""

# Create your views here.

def saludar(request):
    return HttpResponse('Bienvenido a la calculadora')

def suma(request, n1,n2):
    resultado = calculadora.calcular('suma',n1,n2)
    print(resultado)
    return HttpResponse(bytes(RESPONSE.format(
            n1=n1,n2=n2,oper='+',result=resultado),'utf-8'))

def resta(request, n1,n2):
    resultado = calculadora.calcular('resta',n1,n2)
    return HttpResponse(bytes(RESPONSE.format(
            n1=n1,n2=n2,oper='-',result=resultado),'utf-8'))

def div(request, n1,n2):
    resultado = calculadora.calcular('div',n1,n2)
    return HttpResponse(bytes(RESPONSE.format(
            n1=n1,n2=n2,oper='/',result=resultado),'utf-8'))

def multi(request, n1,n2):
    resultado = calculadora.calcular('multi',n1,n2)
    return HttpResponse(bytes(RESPONSE.format(
            n1=n1,n2=n2,oper='*',result=resultado),'utf-8'))