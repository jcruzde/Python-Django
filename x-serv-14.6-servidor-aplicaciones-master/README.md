# X-Serv-14.6-ServAplicaciones
Ejercicio 14.6 - Clase servidor de aplicaciones

## Enunciado

Reescribe el programa ``Aplicación web hola mundo'' usando clases, y reutilizándolas, haz otro que devuelva ``Adiós mundo cruel'' en lugar de ``Hola mundo''. Para ello, define una clase <i>webApp</i> que sirva como clase raíz, que al especializar permitirá tener aplicaciones web que hagan distintas cosas (en nuestro caso, <i>holaApp</i> y <i>adiosApp</i>).

Esa clase <i>webApp</i> tendrá al menos:

<ul>
<li> Un método <i>Analyze</i> (o <i>Parse</i>), que devolverá un objeto con lo que ha analizado de la petición recibida del navegador (en el caso más simple, el objeto tendrá un nombre de recurso)
<li> Un método <i>Compute</i> (o <i>Process</i>), que recibirá como argumento el objeto con lo analizado por el método anterior, y devolverá una lista con el código resultante (por ejemplo, ``200 OK'') y la página HTML a devolver
<li> Código para inicializar una instancia que incluya el bucle general de atención a clientes, y la gestión de sockets necesaria para que funcione.
</ul>

Una vez la clase <i>webApp</i> esté definida, en otro módulo define la clase <i>holaApp</i>, hija de la anterior, que especializará los métodos Parse y Process como haga falta para implementar el ``Hola mundo''.

El código <i>__main__</i> de ese módulo instanciará un objeto de clase <i>holaApp</i>, con lo que tendremos una aplicación ``Hola mundo'' funcionando.

Luego, haz lo mismo para <i>adiosApp</i>.

Conviene que en el módulo donde se defina la clase <i>webApp</i> se incluya también código para, en caso de ser llamado como programa principal, se cree un objeto de ese tipo, y se ejecute una aplicación web simple.

