from queue import Queue
import cv2
import time
from datetime import date
import base64

from cor import *
fila = Queue(maxsize = 10)

class Report:
    def __init__(self,img,date,people=0,maskoff=0,crowd=0,tipo = 'default'):
        self.img = img
        self.date = date
        self.people = people
        self.maskoff = maskoff
        self.crowd = crowd
        self.tipo = tipo

def getReport():
    global fila
    try:
        alerta = fila.get()
        return alerta.__dict__
    except:
        return []
        
def createReport(image,size,qtdMaskOff,qtdCrowded):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    data = str(date.today()) + ' ' + str(current_time)
    buffer = cv2.imencode('.jpg', image)[1]
    alert = tipo(qtdMaskOff,qtdCrowded)
    if alert == 'Verde': 
        imgb64 = None
    else: # Armazenar imagem para ver possiveis falsos positivos
        imgb64 = base64.b64encode(buffer)
    return Report(imgb64,data,size,qtdMaskOff,qtdCrowded,alert)   