import json
import urllib, urllib.request
from urllib import request

def handler(event, context):
    print("hello from zappa")
    print(event)
    return {'status': 200}


def descargarPagina(event, context):
    with urllib.request.urlopen('https://www.elespectador.com/') as handler:
        html = str(handler.read(), 'utf-8')
        with open('el_espectador.html','w') as file_handler:
            file_handler.write(html)
    with urllib.request.urlopen('https://www.eltiempo.com/') as handler2:
        html2 = str(handler2.read(), 'utf-8')
        with open('eltiempo.html','w') as file_handler2:
            file_handler2.write(html2)   