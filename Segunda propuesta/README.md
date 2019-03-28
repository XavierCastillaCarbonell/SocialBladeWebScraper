# SocialBladeWebScraper, primera propuesta

Para realizar la práctica hemos escogido la web https://socialblade.com/ que mantiene información actualizada de cada una de las plataformas sociales más usadas del momento. El objetivo es extraer la información común en un fichero .csv de los TOP 25 usuarios de cada una de las siguientes plataformas: Youtube, Twitch, Twitter, Instagram, Facebook, Dailymotion y Mixer. Además otro fichero por cada una de las plataformas con todo el detalle de los usuarios.

## Como correr el código: 

Correr con python el fichero prac1.py

$ py prac1.py

## Salida

Se generará si no existe la carpeta output con los ficheros .csv de cada plataforma más uno adicional con los datos comunes.

## Ficheros

### prac1.py

Este fichero contiene tres funciones:

- writeCSV : Función genérica que a partir de un nombre de plataforma, unas cabeceras y unos valores, genera un fichero csv en la ruta OUT/ con los datos recibidos.

- processPage : Función genérica que recibe un contenido de un html, identifica los elementos correspondientes a las cabeceras así como los correspondientes a los valores que deseamos almacenar y llama a writeCSV para volcarlos en un fichero. Este método es genérico a todas las plataformas puesto que todas tienen la misma estructura de html, sin embargo, ante unas particularidades de una plataforma en concreto, requiere diferenciación y acciones específicas. Esta función también se encarga de identificar aquellos elementos que irán en el fichero common.csv, por lo que los selecciona y los va almancenando en una estructura que devuelve al método principal

- main: El código main ejecutable recupera de la home de la página web las diferentes plataformas a procesar, y las recorre una a una llamando para cada una de ellas a la función processPage, la cual a su vez llama a writeCSV, generando el fichero csv con los datos correspondientes a la plataforma. Para cada iteración de cada plataforma recupera los elementos comunes, los almacena en una estructura y finalmente los vuelca en un csv llamado common.csv.