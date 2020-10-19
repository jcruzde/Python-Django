# X-Serv-14.3-Sumador-Simple
Ejercicio 14.5 - Aplicación web sumador simple

## Enunciado 

Construye una aplicación web que suma en dos fases. En la primera, invocamos una URL del tipo \url{http://sumador.edu/5}, aportando el primer sumando (el número que aparece como nombre de recurso). En la segunda, invocamos una URL similar, proporcionando el segundo sumando. La aplicación nos devuelve el resultado de la suma. En esta primera versión, suponemos que la aplicación es usada desde un solo navegador, y que las URLs siempre le llegan ``bien formadas''.

Nota:Muchos navegadores, cuando se invoca con ellos una URL, lanzan un GET para ella, y a continuación uno o varios GET para el recurso \texttt{favicon.ico} en el mismo sitio. Por ello, hace falta tener en cuenta este caso para que funcione la aplicación web con ellos.


## Forma de entrega

Has de tener un repositorio llamado X-Serv-14.5-Sumador-Simple en tu cuenta en GitLab
que incluya el fichero de nombre 'servidor-sumador-http.py' que contenga las
instrucciones en Python para solucionar el ejercicio.

Se proporciona un script, check.py, para comprobar la entrega correcta
del ejercicio. El script de comprobación se ha de ejecutar desde terminal
pasándole como parámetro tu nombre de usuario en los laboratorios docentes.
Así, un ejemplo de ejecución sería:

$ python3 check.py gregoriorobles
