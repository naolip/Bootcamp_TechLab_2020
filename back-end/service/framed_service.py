import sys 

sys.path.append('/home')

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop 
#from data.dao.frames_dao import Frame_dao
from application.face_recognition import face_det



class FrameAPI(RequestHandler):
     

    def get(self):

        self.write({'face_det' : face_det()})


def make_app():

    urls = [
        ('/api/one/', FrameAPI)
    ]

    return Application(urls)

def start_service():

    app = make_app()
    app.listen(8001)
    IOLoop.instance().start()

if __name__ == '__main__':
    start_service()


#    def set_default_headers(self):
#        # print("setting headers!!!")
#        origin = self.request.headers.get('Origin')
#        if origin:
#            self.set_header('Access-Control-Allow-Origin', origin)
#        # self.set_header("Access-Control-Allow-Origin", "http://localhost:9527/")
#        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
#        self.set_header("Access-Control-Allow-Headers",
#                        "access-control-allow-origin,authorization,content-type, grant_type, client_id, client_secret")
#        self.set_header('Access-Control-Allow-Credentials', 'true')
#        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
#
#    def get(self, id):
#
#        camera = Camera_dao.get_camera(id)
#
#        self.write({'camera' : camera.to_json()})
#
#
#def make_app():
#
#    urls = [
#        ('/api/one/([0-9]*)', CameraAPI)
#    ]
#
#    return Application(urls)
#
#def start_service():
#
#    app = make_app()
#    app.listen(8000)
#    IOLoop.instance().start()
#
#if __name__ == '__main__':
#    start_service()

#    def get(self):
#
#        self.write({'face_det' : face_det()})
#
#

