#!/usr/bin/python3.6

'''
MODO DE EJECUCIÓN:
1.- localhost:PORT/numer
2.- localhost:PORT/opercación
3.- localhost:PORT/numer

Tipos de operaciones: sumar, restar, multiplicar, dividir
'''

import socket
import random
import calculadora
import sys

MIN = 0
MAX = 100000
PORT = 1234

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), PORT))

mySocket.listen(5)

PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <p><h1>{contenido}<h1></p>
  </body>
</html>
"""

PAGE_NOT_FOUND = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <p>Argument {argumento} is invalid.</p>
  </body>
</html>
"""

ANTERIOR = False
operacion = ''

def get_char(oper):
    operaciones = {'sumar': '+', 'restar': '-',
                    'multiplicar': '*', 'dividir': '/'}
    return operaciones[oper]
                
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('\n', '-'*10, '\n', 'HTTP request received:')
        request= str(recvSocket.recv(2048)) # todo el string que recibe del navegador
        request_list = request.split()
        resource = request_list[1]
        print('Resource received: ', resource)
        
        try:
            numero = str(int(resource[1:]))
        except ValueError:
            try:
                operacion = str(resource[1:])
                # Comprobamos si la operacion es valida
                resultado = calculadora.calcular(operacion,1,1)
                
                contenido = "Me has ordenado " + operacion
                page = PAGE.format(contenido=contenido)
                recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                                bytes(page,'utf-8') +
                                b"\r\n")
                recvSocket.close()
                continue
            except: # DUDA. Si pongo KeyError, no captura los KeyError de calculadora.
                print('Argumento inválido')
                page = PAGE_NOT_FOUND.format(argumento=resource)
                recvSocket.send(b"HTTP/1.1 400 \r\n\r\n" +
                            bytes(page,'utf-8') +
                            b"\r\n")
                recvSocket.close()
                continue
            
        if not ANTERIOR: # Es el primer número que envían
            primero = numero
            print('Recido un: ', primero, '[PRIMER OPERANDO]')
            ANTERIOR = True
            contenido = "Me has enviado un " + primero
        else:
            print('Recibo un: ', numero,)
            if not operacion: # Maneja el caso en el que se introducen 2 numeros consecutivos sin operación.
                primero = numero
                contenido = "Falta operacion"
                page = PAGE.format(contenido=contenido)
                recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                                bytes(page,'utf-8') +
                                b"\r\n")
                recvSocket.close()
                continue
                
                
            segundo = numero
            resultado = str(calculadora.calcular(operacion,int(primero),int(segundo)))
            char = get_char(operacion)
            contenido = primero + char + segundo + ' =' + resultado
            ANTERIOR = False
        
        
        print('Answering back...')
        page = PAGE.format(contenido=contenido)
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        bytes(page,'utf-8') +
                        b"\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print('\n', 'Closing server..')
