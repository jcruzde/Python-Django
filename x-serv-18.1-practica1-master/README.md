# X-Serv-18.1-Practica1
Práctica 1 (Ejercicio 18.1): Web acortadora de URLs


Esta práctica tendrá como objetivo la creación de una aplicación web simple para acortar URLs.

El código ha de guardarse en un fichero llamado practica1.py.
El funcionamiento de la aplicación ser ́a el siguiente:
Recurso “/”, invocado mediante GET. Devolveŕa una ́agina HTML con un
formulario. En ese formulario se podr ́a escribir una url, que se enviar ́a al
servidor mediante POST. Adem ́as, esa misma p ́agina incluir ́a un listado de
todas las URLs reales y acortadas que maneja la aplicaci ́on en este momento.
Recurso “/”, invocado mediante POST. Si el comando POST incluye una qs
(query string) que corresponda con una url enviada desde el formulario, se
devolver ́a una p ́agina HTML con la URL original y la URL acortada (ambas
como enlaces pinchables), y se apuntar ́a la correspondencia (ver m ́as abajo).
Si el POST no trae una qs que se haya podido generar en el formulario,
devolver ́a una p ́agina HTML con un mensaje de error.
Si la URL especificada en el formulario comienza por “http://” o “https://”,
se considerar ́a que  ́esa es la URL a acortar. Si no es as ́ı, se le a ̃
nadir ́a
“http://” por delante, y se considerar ́a que esa es la url a acortar. Por
ejemplo, si en el formulario se escribe “http://gsyc.es”, la URL a acor-
tar ser ́a “http://gsyc.es”. Si se escribe “gsyc.es”, la URL a acortar ser ́a
“http://gsyc.es”.
Para determinar la URL acortada, utilizar ́a un n ́
umero entero secuencial, co-
menzando por 0, para cada nueva petici ́on de acortamiento de una URL que
se reciba. Si se recibe una petici ́on para una URL ya acortada, se devolver ́a
la URL acortada que se devolvi ́o en su momento.
As ́ı, por ejemplo, si se quiere acortar
http://gsyc.urjc.es
y la aplicaci ́on est ́a en el puerto 1234 de la m ́aquina “localhost”, se invocar ́a
(mediante POST) la URL
http://localhost:1234/
67y en el cuerpo de esa petici ́on HTTP ir ́a la qs
url=http://gsyc.urjc.es
si el campo donde el usuario puede escribir en el formulario tiene el nom-
bre “URL”. Normalmente, esta invocaci ́on POST se realizar ́a rellenando el
formulario que ofrece la aplicaci ́on.
Como respuesta, la aplicaci ́on devolver ́a (en el cuerpo de la respuesta HTTP)
la URL acortada, por ejemplo
http://localhost:1234/3
Si a continuaci ́on se trata de acortar la URL
http://www.urjc.es
mediante un procedimiento similar, se recibir ́a como respuesta la URL acor-
tada
http://localhost:1234/4
Si se vuelve a intentar acortar la URL
http://gsyc.urjc.es
como ya ha sido acortada previamente, se devolver ́a la misma URL corta:
http://localhost:1234/3
Recursos correspondientes a URLs acortadas. Estos ser ́an n ́
umeros con el
prefijo “/”. Cuando la aplicaci ́on reciba un GET sobre uno de estos recursos,
si el n ́
umero corresponde a una URL acortada, devolver ́a un HTTP REDI-
RECT a la URL real. Si no la tiene, devolver ́a HTTP ERROR “Recurso no
disponible”.
Por ejemplo, si se recibe
http://localhost:1234/3
la aplicaci ́on devolver ́a un HTTP REDIRECT a la URL
http://gsyc.urjc.es
Comentario
Se recomienda utilizar dos diccionarios para almacenar las URLs reales y los
n ́
umeros de las URLs acortadas. En uno de ellos, la clave de b ́
usqueda ser ́a la URL
real, y se utilizar ́a para saber si una URL real ya est ́a acortada, y en su caso saber
cu ́al es el n ́
umero de la URL corta correspondiente.
En el otro diccionario la clave de b ́
usqueda ser ́a el n ́
umero de la URL acortada,
y se utilizar ́a para localizar las URLs reales dadas las cortas. De todas formas, son
posibles (e incluso m ́as eficientes) otras estructuras de datos.
Se recomienda realizar la aplicaci ́on en varios pasos:

Comenzar por reconocer “GET /”, y devolver el formulario correspondiente.
Reconocer “POST /”, y devolver la p ́agina HTML correspondiente (con la
URL real y la acortada).
Reconocer “GET /num” (para cualquier n ́
umero num), y realizar la redirec-
ci ́on correspondiente.
Manejar las condiciones de error y realizar el resto de la funcionalidad.