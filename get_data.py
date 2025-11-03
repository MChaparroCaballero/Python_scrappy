#autor : Maria Chaparro 
# git : MChaparroCaballero
import os
import sys
import requests  # Librería para hacer peticiones HTTP
from bs4 import BeautifulSoup  # Librería para analizar HTML
from bs4.element import Tag  # Tipo para elementos HTML
from typing import cast  # Función para convertir tipos

url= "http://127.0.0.1:5500/ejer__4_scrappy/periodicos.html" # URL del sitio web local
#LIMPIAR PANTALLA en windows necesitas cls para borrar la pantalla,
#  y clear para linux, por eso debemos especificar que sistema operativo es con os 
# y dependiendo de lo que nos devuelva poner uno o otro
os.system('cls' if os.name == 'nt' else 'clear')

try:

    #primero hacemos la peticion y obtenemos el contenido HTML de toda la pagina con requests y lo parseamos con BeautifulSoup
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    #luego buscamos el elemento por su id y lo casteamos para que no de error
    noticia= cast(Tag,soup.find(id="titulo-exclusiva"))
    fecha= cast(Tag,soup.find(id="fecha-exclusiva"))
    #finalmente imprimimos el texto del elemento encontrado
    print(f"Noticias del día: {fecha.get_text(strip=True)}\n{noticia.get_text(strip=True)}") #ponemos el strip true para que quite los espacios
    #en blanco al inicio y al final y los dobles saltos de linea
    
except AttributeError as e:
    print("Error al encontrar el elemento")
except requests.exceptions.ConnectionError as e:
    print("Error Live server no activado")
except requests.exceptions.HTTPError as e:
    print("Respuestas HTTP no exitosas")
except Exception as e:
    print("Error inesperado:", e)
