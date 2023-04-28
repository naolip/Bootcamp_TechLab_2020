import sys 
sys.path.append('/home/bruno/cyberTech/grupo3-rep/back-end/')

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop 
from api.alert.dao.alert import Alert

class AlertAPI(RequestHandler):

    def get(self, id):

        alert = Alert.get_alert(id)

        self.write({'alert' : alert.to_json()})

    def post(self, name, text)
        
        

def get_urls():

    urls = [
        ('/api/alert/([0-9]*)', CameraAPI)
    ]

    return urls