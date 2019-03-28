#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Función que, a partir de unos parámetros, genera un fichero csv.

# Parámetros
# filename: Nombre del fichero
# headers: Cabeceras del csv
# values: Valores a volcar en el csv

import os
import csv
def writeCSV(filename,headers,values):
    
    # Si no existe el fichero destino que contendrá los ficheros csv se crea
    path = os.path.abspath('') + '/OUT/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    with open(path + filename + '.csv', mode='w') as csvFile:
        
        # Abrimos el descriptor de fichero
        writer = csv.writer(csvFile)
        
        # Añadimos las cabeceras
        writer.writerow(headers)
        
        # Añadimos todas las filas de valores una a una
        numberRows = len(values)
        for numberRow in range (numberRows):
            writer.writerow(values[numberRow])
        
        # Cerramos el descriptor de fichero
        csvFile.close()


# In[17]:


# Función que procesa el contenido de una página web con BS y llama a la función generadora de csv
# Aparte procesa y va almacenando aquellos datos que son para el csv común

# Parámetros:
# nameSN: El nombre de la red social a procesar
# page: Objeto de BeautifulSoup que contiene la web de la red social correspondiente

# Devuelve: Los valores identificados como "comunes" (valuesCommon) que se irán acumulando para 
# constituir un csv aparte

def processPage(nameSN,page):
    # Definimos variable con aquellas cabeceras que conforman el fichero common así como otras estructuras necesarias
    # Para el caso específico de youtube, las columnas comunes de Username y Followers se rellenan con los datos de
    # Display Name y Subscribers
    rank = 'Rank'
    grade = 'Grade'
    username = 'Username'
    followers = 'Followers'
    if nameSN == 'youtube':
        username = 'Display Name'
        followers = 'Subscribers'
    
    headersCommon = ['',rank,grade,username,followers]
    valuesCommon = []
    
    # Identificamos las cabeceras propias correspondientes a los datos de la red social que vamos a procesar
    headers = []
    headersRow = page.find_all('div', class_='table-header')
    for headerRow in headersRow:
        headers.append(headerRow.string)
    
    
    # Identificamos y recuperamos del html las filas con los valores que queremos procesar
    table = page.find_all('div', class_='table-body')
    
    # Creamos las estructuras necesarias del tamaño apropiado para almacenar todos los valores
    numberRow = 0
    w, h = len(headers), len(table)
    values = [[0 for x in range(w)] for y in range(h)] 

    # Para cada una de las filas recuperadas:
    for row in table:
        
        # Creamos una estructura que almacenará aparte aquellos valores del fichero común
        valuesAux = [0 for x in range(5)]

        # En la posición 0 incluimos el nombre de la red social
        valuesAux[0] = nameSN
        
        # En el caso particular de facebook, la columna común Followers no contendrá datos y ponemos NA
        if nameSN == 'facebook':
            valuesAux[4] = 'NA'
         
        # Para cada una de las celdas, almacenamos el valor en las estructuras creadas previamente
        numberColumn = 0
        cells = row.find_all('div',class_='table-cell')
        for cell in cells:
            
            # En algunos casos la celda tiene una estructura anidada por lo que el valor es None y debemos
            # realizar un tratamiento específico. Si no, coge el valor que contiene directamente
            cellValue = ''
            if cell.string is None:
                for string in cell.strings:
                    if string != ' ':
                        cellValue = str(string)
            else:
                cellValue = cell.string
            
            
            values[numberRow][numberColumn] = cellValue
            
            # Si la celda que se procesa pertenece a una columna que debe aparecer en el fichero común, añadimos
            # ese valor aparte en la estructura de valores comunes
            if headers[numberColumn] in headersCommon:
                valuesAux[headersCommon.index(headers[numberColumn])] = cellValue
            numberColumn = numberColumn + 1
        
        valuesCommon.append(valuesAux)
        numberRow = numberRow + 1
    
    # Volcamos en formato csv los datos correspondientes a la red social
    writeCSV(nameSN,headers,values)
    
    # Devolvemos la estructura con los valores correspondientes a columnas que deben aparecer también en el 
    # fichero común
    return valuesCommon


# In[18]:


# Método main principal que:

# 1. Establece la url de la home a llamar.
# 2. Descarga y procesa el html de la home con el objetivo de identificar nuevas urls a llamar/procesar 
#    correspondientes a diferentes redes sociales.
# 3. Para cada una de ellas, llama a la función que procesa el html para luego llamar a la generadora de csv.
# 4. Para cada una de ellas, obtiene aquellos datos que conforman el fichero común common.csv con los datos comunes
#    de todas las redes sociales (exceptuando youtube).

import numpy as np
import requests
from bs4 import BeautifulSoup

# Definimos la url a llamar así como otras variables/estructuras necesarias, incluyendo los 
# headers del fichero common
url = 'https://socialblade.com'
urlSNs = [0 for x in range(5)]
headersCommon = ['Platform','Rank','Grade','Username','Followers']
valuesCommon = []


# Obtenemos la página home
page = requests.get(url)
soup = BeautifulSoup(page.content)

# Obtenemos el listado de las redes sociales que contiene
listSN = soup.find(id='top-menu-top-charts-inner')

# Para cada una de las redes sociales, llamamamos a la url y procesamos su contenido, incluyendo la generación
# del csv correspondiente. 
# La función processPage devuelve los valores comunes de la red social correspondiente para incorporarlos en el
# fichero común common.csv

for link in listSN.find_all('a'):
    urlSN = link.get('href')
    urlSNs.append(urlSN)
    urlTotalSN = url + urlSN
    pageSN = requests.get(urlTotalSN)
    valuesCommonSN = processPage(urlSN[1:],BeautifulSoup(pageSN.content))
    
    for row in range(len(valuesCommonSN)):
        valuesCommon.append(valuesCommonSN[row])

# Vuelca los valores comunes con las cabeceras comunes en el fichero csv common.csv        
writeCSV('common',headersCommon,valuesCommon)

