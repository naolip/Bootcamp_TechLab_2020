import sys 

sys.path.append('/home/bruno/cyberTech/grupo3-rep/back-end/')

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop 
from data.dao.frame_dao import Frame_dao

class GetFrameAPI(RequestHandler):

    def get(self, id):

        frame = Frame_dao.get_frame(id)

        self.write({'frame' : camera.to_json()})


def make_app():

    urls = [
        ('/api/one/([0-9]*)', GetFrameAPI)
    ]

    return Application(urls)

def start_service():

    app = make_app()
    app.listen(8000)
    IOLoop.instance().start()

if __name__ == '__main__':
    start_service()