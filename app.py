
#Aplicación en python que muestra información desde un servicio web de la DISCOVERY API de ticketmaster



#Importamos todo lo que vamos a necesitar de nuestro entorno
from apikey import Flask, render_template,abort,request
#Importamos la librería request
import requests
# Importamos la libreria os para  environ
import os 
# Importamos la de json
import json
#Importarmos  las fechas
from datetime import datetime

#Abrimos el fichero json donde están los paises con su codigo
#y lo guardamos en infoÇ_paises
with open("paises.json") as fichero:
    info_paises=json.load(fichero)

# Definimos la variable app por Flask
app = Flask(__name__)
#Guardamos la url base
url_base="https://app.ticketmaster.com/discovery/v2/"

