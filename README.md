# SocialBladeWebScraper

__Por Xavier Castilla Carbonell y Ana Blanes Martínez.__


Para realizar la práctica hemos escogido la web https://socialblade.com/ que mantiene información actualizada de cada una de las plataformas sociales más usadas del momento. Elobjetivo es extraer la información común en un fichero .csv de los TOP 25 usuarios de cada una de las siguientes plataformas: Youtube, Twitch, Twitter, Instagram, Facebook, Dailymotion y Mixer. Además otro fichero por cada una de las plataformas con todo el detalle de los usuarios.


## Como correr el código: 
Correr con python el fichero main.py

$ py main.py

## Salida

Se generara si no existe la carpeta output con los ficheros .csv de cada plataforma

## Ficheros

### main.py

Este fichero es el lanzador de la aplicación. Tiene la función de llamar a todas las clases para extraer la información de los directorios de SocialBlade. También es el encargado de escribir el fichero .csv a partir de la información recopilada.

### socialScrapers

Esta carpeta contiene las clases de cada uno de los extractores concretos de cada plataforma. Todos tienen la misma estructura.

Estos extractores tienen la función "scrape", esta función es la responsable de recuperar el contenido web y extraer los datos requeridos, devuelve un listado con todos los elementos extraídos.


### commonScraper.py

Similar a los scrapers concretos que hay dentro la carpeta socialScrapers, "commonScraper.py" tiene la función de extraer para cada una de las plataformas la información que tienen en común entre todas ellas, estos campos son: rank, grade, name y subscriptores.

Para hacerlo, navega automáticamente entre las plataformas y busca la información.