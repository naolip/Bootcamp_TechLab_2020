#from application.face_recognition.py import face_det
from data.database import session_factory
from data.model.frame_model import Frames
import urllib.request 
import base64
import sys

path = '/home/bruno/cyberTech/grupo3-rep/front-end/'
#url_path = 'https://image.freepik.com/fotos-gratis/pessoas-diversas-felizes-unidas_53876-38802.jpg'

#img = urllib.request.urlretrieve(url_path, 'pessoas.jpg')

session = session_factory()

def get_image():
    with open(path + 'exame.png', 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
        encoded_string.decode('utf-8')
        
        return encoded_string

image = get_image()


class Frame_dao():



    def create_frame(name):

#        def get_image(img):
#            with open(img, 'rb') as image_file:
#                encoded_string = base64.b64encode(image_file.read())
#                encoded_string.decode('utf-8')
#        
#                return encoded_string
#
#        image = get_image()
    
        frame_create = Frames(name=name, frame=image)


        session.add(frame_create)
        session.commit()

        session.close()

        return frame_create


    def get_frame(id):

        frame_get = session.query(Frames).filter(Frames.id == id).first()
        session.close()

        return frame_get