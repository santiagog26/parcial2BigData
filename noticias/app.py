import urllib, urllib.request
from urllib import request
import requests
import json
import boto3
import time


bucket="zappa-parcial2-descargas"

def handler(event,context):

	localtime=time.localtime()

	s3 = boto3.resource('s3')
	descargarPagina('https://www.elespectador.com/' , 'elespectador.html',localtime,bucket,s3)
    descargarPagina('https://www.eltiempo.com/' , 'eltiempo.html',localtime,bucket,s3)

	return {
			"status_code":200
		}

def descargarPagina(url,archivo,localtime,bucketname,s3):
  with urllib.request.urlopen(url) as handler:
    html = str(handler.read(), 'utf-8')
    with open(archivo,'w') as file_handler:
        file_handler.write(html)
     