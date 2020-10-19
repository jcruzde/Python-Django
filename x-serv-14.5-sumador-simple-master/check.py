#!/usr/bin/python3

"""
Script de comprobación de entrega de ejercicio

Para ejecutarlo, desde la shell:
 $ python check.py login_github

"""

import os
import random
import sys

ejercicio = 'x-serv-14.5-sumador-simple'

student_files = [
    'servidor-sumador-simple-http.py'
    ]
    
optional_files = [
    'calculadora.py'
    ]

repo_files = [
    'check.py',
    'README.md',
    '.gitignore',
    '.git'
    ]

files = student_files + repo_files

if len(sys.argv) != 2:
    print()
    sys.exit("Usage: $ python check.py login_gitlab")

repo_git = "https://gitlab.etsit.urjc.es/" + sys.argv[1] + "/" + ejercicio


aleatorio = str(int(random.random() * 1000000))

error = False

print()
print("Clonando el repositorio " + repo_git + "\n")
os.system('git clone ' + repo_git + ' /tmp/' + aleatorio + ' > /dev/null 2>&1')
try:
    gitlab_file_list = os.listdir('/tmp/' + aleatorio)
except OSError:
    error = True
    print("Error: No se ha podido acceder al repositorio " + repo_git + ".")
    print()
    sys.exit()

for filename in optional_files:
    if filename in gitlab_file_list:
        gitlab_file_list.pop(gitlab_file_list.index(filename))

if len(gitlab_file_list) != len(files):
        error = True
        print("Error: número de ficheros en el repositorio incorrecto")

for filename in files:
    if filename not in gitlab_file_list:
        error = True
        print("\tError: " + filename + " no encontrado en el repositorio.")

if not error:
    print("Parece que la entrega se ha realizado bien.")

print()
print("La salida de pep8 es: (si todo va bien, no ha de mostrar nada)")
print()
for filename in student_files:
    if filename in gitlab_file_list:
        os.system('pep8 --repeat --show-source --statistics /tmp/'
                  + aleatorio + '/' + filename)
    else:
        print("Fichero " + filename + " no encontrado en el repositorio.")
print()
