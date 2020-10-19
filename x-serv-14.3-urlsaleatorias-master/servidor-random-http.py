#!/usr/bin/python3.6

import socket
import random

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
    <p><h1>Hola<h1></p>
    <p>{url}</p>
  </body>
</html>
"""

def create_answer():
    numero = str(random.randint(MIN,MAX))
    url = "<a href='http://" + socket.gethostname() + ":" + str(PORT) + "/" + str(numero) + "'>Dame otra</a>"
    page = PAGE.format(url=url)
    return(b"HTTP/1.1 200 OK\r\n\r\n" +
            bytes(page,'utf-8') +
            b"\r\n")
        
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:')
        print(recvSocket.recv(1024))
        print('Answering back...')
            
        answer = create_answer()
        recvSocket.send(answer)
            
        recvSocket.close()
except KeyboardInterrupt:
    print('\n', 'Closing server..')