# SocialBladeWebScraper

### Realizado por: Ana Blanes y Xavier Castilla

Con el objetivo de practicar como crear un web scraper decidimos hacer la parte de código por separado y luego hacer comparaciones, al final las dos propuestas son bastante distintas por lo que presentamos ambas con el fin de saber que aproximación es mejor o que comentarios de mejora exiten para cada una de las propuestas.

Dentro de los directorios "Primera Propuesta" y "Segunda Propuesta" hay un fichero README.md con los detalles



## 1. Contexto. Explicar en qué contexto se ha recolectado la información. Explique por qué el sitio web elegido proporciona dicha información.

Las redes sociales juegan cada vez más un papel más importante en nuestras vidas y con ellas se han creado figuras muy influyentes que son vistas por miles sino millones de personas. Estos “influencers” tienen la capacidad de generar tendencias y corrientes de opinión dada su alta visibilidad. En este contexto es interesante conocer cuales son las figuras más influyentes de cada una de las redes sociales más populares del momento.

SocialBlade nos presenta que plataformas sociales son más influyentes en el momento (con mayor afluencia de visitas) y nos presenta en una tabla por cada plataforma con los datos de los usuarios con mayor seguimiento.


## 2. Definir un título para el dataset. Elegir un título que sea descriptivo. 

Generamos ocho datasets, uno para cada plataforma y otro que contenga la información que tienen en común todas las plataformas, para los primeros casos el nombre es __TopInfluencers{_$nombreplataforma_}.csv__, para el caso de datos en común será __TopInfluencers.csv__.


## 3. Descripción del dataset. Desarrollar una descripción breve del conjunto de datos que se ha extraído (es necesario que esta descripción tenga sentido con el título elegido).

__TopInfluencers{_$nombreplataforma_}.csv__ contiene los datos de los usuarios más influyentes de una de las plataformas, los nombres de las variables de estos datos están ligados a las nomenclaturas de cada plataforma.

__TopInfluencers.csv__ contiene los datos de los usuarios de todas las plataformas sociales y las variables son las comunes entre todas las plataformas. 


## 4. Representación gráfica. Presentar una imagen o esquema que identifique el dataset visualmente.

A continuación mostramos la representación gráfica del dataset escogido. El formato utilizado para ello es una tabla, ya que de esta manera se puede ver fácilmente para cada una de las plataformas cuyos datos son procesados, los atributos que tienen asociados. De igual manera podemos ver dónde aparecen cada uno de los atributos.

![alt text](https://github.com/XavierCastillaCarbonell/SocialBladeWebScraper/blob/master/imagePunto4Final.png)


## 5. Contenido. Explicar los campos que incluye el dataset, el periodo de tiempo de los datos y cómo se ha recogido.

Para la propuesta escogida se generan varios datasets con sus ficheros csv correspondientes: uno por cada plataforma que es procesada más uno que contiene los datos comunes a todas ellas; aunque todos comparten una estructura parecida algunos presentan algunas particularidades, por lo que vamos a detallarlos uno a uno. De cara a facilitar la explicación de los campos que son compartidos y los que no, se van a presentar primero los campos para, a continuación, explicar el significado de cada uno de ellos.



TopInfluencers.csv: Rank, Grade, Name, Followers/Suscribers

TopInfluencersYoutube.csv: Rank, Grade, Display name, Videos, Subscribers, Views

TopInfluencersTwitchtv.csv: Rank, Grade, User name, Last game, Views, Followers

TopInfluencersTwitter.csv: Rank, Grade, User name, Display name, Tweets, Followers, Following

TopInfluencersInstagram.csv: Rank, Grade, User name, Display name, Media, Followers, Following

TopInfluencersFacebook.csv: Rank, Grade, User name, Category, Likes, Talking about

TopInfluencersDailymotion.csv: Rank, Grade, User name, Display name, Media, Followers, Vidviews

TopInfluencersMixer.csv: Rank, Grade, User name, Followers, Channel views, Level, Latest game



-	Rank: Es la posición en el ránking. Para cada una de las plataformas se indica la posición de un canal en función del número de suscriptores/seguidores.
-	Grade: según explica SocialBlade, el número de suscriptores/seguidores no es lo único que debe contar a la hora de puntuar un canal: también el número medio de visitas así como su comparación con otros sites determinan la puntuación que viene dada en esta columna y que puede tener los valores A/B/C (++/+/-/—)…
-	User name: El nombre del usuario propietario del canal
-	Display name: El nombre mostrado del usuario en el canal
-	Followers: Número de seguidores que presenta un canal en concreto.
-	Subscribers: Número de suscriptores que presenta un canal en concreto.
-	Following: Número de canales que son seguidos por un canal en concreto.
-	Una serie de campos específicos para cada plataforma donde se registran los datos correspondientes; los nombres son intuitivos y permiten saber qué datos contienen: Videos Views, Last game, Tweets, Media, Category, Likes, Talking about, Media, Vidviews, Channel views, Level.


Según indica la página SocialBlade las estadísticas las actualizan una vez al día, sin embargo si se detecta que alguna plataforma/canal está recibiendo poco tráfico estas actualizaciones pueden darse con menos frecuencia, mostrándose el resultado tras varios días. De manera que para la ejecución del código de webscraping implementado en este trabajo se puede optar por ejecutar el proceso una vez al día, y así se garantiza que los datos aparezcan sincronizados con respecto a SocialBlade.

La forma de recogerlos es mediante un conjunto de programas sencillos y específicos que son ejecutados a través de un programa principal. Cada uno de estos programas se encargan de contactar con la página web de una de las plataforma y procesar los datos contenidos en ella, para luego volcarlos en un fichero csv. Aparte, se realiza una nueva llamada sobre todas las webs de las plataformas para obtener aquellos datos que son parte del fichero común, ya que son de columnas que comparten todas las platformas.


## 6. Agradecimientos. Presentar al propietario del conjunto de datos. Es necesario incluir citas de investigación o análisis anteriores (si los hay).

SocialBlade es un website que, haciendo uso de las diferentes herramientas proporcionadas por diferentes plataformas/redes sociales a través de API’s, etc. y mediante el correspondiente acuerdo legal con las mismas y aceptación de sus condiciones y términos de uso, proporciona un valor añadido a estos datos mediante su organización y elaboración de estadísticas de interés basados en dichos datos. Por tanto los datos mostrados son propiedad de SocialBlade, al ser resultado de un procesamiento y manipulación única por su parte en la que a los datos originales se les proporciona un valor añadido.


## 7. Inspiración. Explique por qué es interesante este conjunto de datos y qué preguntas se pretenden responder.

Se han tenido en cuenta dos aspectos principales para llevar a cabo un proyecto de webscraping sobre este site:
-	Los datos obtenidos resultado del proceso son de interés.
-	La frecuencia de actualización es lo suficientemente alta como para que merezca la pena un desarrollo ad-hoc para disponer de estos datos actualizados.

Las páginas específicas que se han procesado presentan en abierto unos datos de gran interés, como son estadísticas correspondientes a las plataformas/redes sociales más importantes que existen en estos momentos; estos datos permiten por ejemplo saber cuáles son los canales más visitados, el número de visitas, etc. y permite realizar estudios sobre la evolución del ránking, suscriptores, etc. En estos tiempos en los que la subsistencia de los canales se debe en gran parte a la existencia de patrocinadores, anunciantes, etc. es fundamental saber la repercusión de los canales y su impacto en el público, por lo que el conocimiento de estadísiticas precisas sobre ellos puede ser significante en el éxito o el fracaso de un canal.

Relacionado con ello tenemos también el hecho de que estos datos solo son interesantes si se encuentran actualizados, y por tanto es fundamental que los procesos se ejecuten con la frecuencia adecuada, sin por supuesto sobrecargar los servidores, para garantizar que los datos proporcionados sean útiles de cara a un propósito  determinado.


## 8. Licencia. Seleccione una de estas licencias para su dataset y explique el motivo de su selección:

Como se ha explicado previamente, SocialBlade procesa datos proporcionados por un conjunto plataformas para mostrar estadísticas y datos relacionados de interés. Este site proporciona un acceso premium de pago donde se aportan más estadísticas de valor para el usuario.

Se han revisado los términos y condiciones legales proporcionadas por SocialBlade y en ellas menciona que los datos pueden ser utilizados, incluyendo pantallazos e imágenes, siempre y cuando se mencionen referencias al site SocialBlade. Es cierto que el site tiene una parte pública abierta con un conjunto de datos que no presentan restricciones en el fichero robots.txt y otra de acceso restringido mediante registro y pago en el que no están permitidas el botting, crawling y scraping. De manera que teniendo en cuenta que las páginas que son procesadas en este trabajo son accesibles sin restricciones pero que se trata de un site comercial que explota económicamente los datos a través de un registro con pago, se puede inferir que el tipo de licencia para los datos en abierto accedidos es Released Under CC BY-NC-SA 4.0 Licensem, ya que permite la distribución de estos datos públicos accesibles siempre y cuando se indique la referencia a la compañía y no se haga un uso comercial de ellos.
