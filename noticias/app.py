import urllib, urllib.request
from urllib import request
import requests
import json
import boto3
import time

bucket="zappa-parcial2-descargas-noticias"
def handler(event,context):
    localtime=time.localtime()
    s3 = boto3.resource('s3')
    
    descargarPagina('El espectador', 'https://www.elespectador.com/', localtime, bucket, s3)
    descargarPagina('El tiempo', 'https://www.eltiempo.com/' , localtime, bucket, s3)
    
    return {
        "status_code":200
        }

def descargarPagina(name, url, localtime, bucketname, s3):	
	headers = {'User-Agent': 'Mozilla'}
	r = requests.get(url, headers=headers)
	filepath="/tmp/"+name+".txt"
	f = open(filepath,"w")
	print("Saving file from "+name)
	f.write(r.text)
	f.close()
	path = 'headlines/raw/periodico='+name+'/year='+str(localtime.tm_year)+'/month='+str(localtime.tm_mon)+'/day='+str(localtime.tm_mday)+'/'+name+'.txt'
	s3.meta.client.upload_file(filepath, bucketname, path)