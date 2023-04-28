#import cv2
#import io
#import os  
#import numpy as np
#from pylab import rcParams
#import urllib.request
#from matplotlib import pyplot as plt
#from IPython.display import display, clear_output, Image

import io
import PIL.Image
import IPython
import cv2
import os
from IPython.display import Image, display, clear_output
import numpy as np
import imageio
import time
import argparse
from timeit import default_timer as timer
from queue import Queue
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model


from report import *
from crowded import *
from masked import *
from cor import *

def face_det():
   prototxt = 'deploy.prototxt'
   caffemodel = 'res10_300x300_ssd_iter_140000.caffemodel'

   net = cv2.dnn.readNetFromCaffe(prototxt,caffemodel)


   def showarray(a,fmt = 'jpeg'): # Mostra imagem
      f = io.BytesIO()
      PIL.Image.fromarray(a).save(f,fmt)
      display(Image(data=f.getvalue()))



   def detect_faces(img,conf): 
         global net
         (h,w) = img.shape[:2]
         blob = cv2.dnn.blobFromImage(cv2.resize(img,(224,224)),1.0,(224,224),(104.0,177.0,123.0))

         net.setInput(blob) # Mandando a imagem recortada pra rede
         detections = net.forward() 

         faces = []
         for i in range(detections.shape[2]):
            confidence = detections[0,0,i,2]

            if confidence < conf: # Filtrando as confiaveis
               continue

            box = detections[0,0,i,3:7]*np.array([w,h,w,h])
            (startX,startY,endX,endY) = box.astype("int")
            faces.append((startX,startY,endX,endY))

         return np.array(faces)    

   def rectangles(img,faces,dist,confMask,minDist): # Mostra a imagem com os retângulos
         size = len(faces)
         qtdMaskOff = 0
         qtdCrowded = 0
         for i in range(size): # pra cada rosto
            maskOff = 0
            crowded = 0
            startX,startY,endX,endY = faces[i]
            face = img[startY:endY,startX:endX]
            img[startY:endY,startX:endX] = cv2.GaussianBlur(face,(21,21),0)
            ## predict mask
            if hasMask(face) < confMask:
               maskOff = True
               qtdMaskOff += 1
            ## Ver aglomeração
            for d in dist[i]:
               if d < minDist and d != 0:
                     crowded = True
                     qtdCrowded += 1
                     break
            #######
            color = clr(maskOff,crowded)
            img = cv2.rectangle(img,(startX,startY),(endX,endY),color,3)
         return img,size,qtdMaskOff,qtdCrowded
   

   def show(vid):
         start = timer()
         for image in vid.iter_data():
            end = timer()
            image = cv2.medianBlur(image,3)
            faces = detect_faces(image,0.2)
            dist = distArr(faces)
            image,size,qtdMaskOff,qtdCrowded = rectangles(image,faces,dist,0.5,200)
            if end - start > 20:
               relatorio = createReport(image,size,qtdMaskOff,qtdCrowded)
               fila.put(relatorio)
               start = timer()
               end = timer()
            showarray(image)
            clear_output(wait=True)
   return getReport()