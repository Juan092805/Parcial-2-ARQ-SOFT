## Pregunta de Analisis.
Yo lo modificaría agregando una parte que envíe los resultados al otro servicio usando una petición HTTP, por ejemplo con la librería requests.
Después de calcular el factorial, el microservicio mandaría el número, el resultado y si es par o impar al otro servicio, que se encargaría de guardarlo en la base de datos.
Así mi microservicio solo haría los cálculos y el otro manejaría el almacenamiento, cad.a uno con su función separada.
