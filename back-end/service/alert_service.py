import sys 

sys.path.append('/home/bruno/cyberTech/grupo3-rep/back-end/')

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop 
from data.dao.alert_dao import Alert_dao

class AlertAPI(RequestHandler):

    def set_default_headers(self):
        # print("setting headers!!!")
        origin = self.request.headers.get('Origin')
        if origin:
            self.set_header('Access-Control-Allow-Origin', origin)
        # self.set_header("Access-Control-Allow-Origin", "http://localhost:9527/")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Headers",
                        "access-control-allow-origin,authorization,content-type, grant_type, client_id, client_secret")
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self, id):

        alert = Alert_dao.get_alert(id)

        self.write({'alert' : alert.to_json()})


def make_app():

    url = [
        ('/api/one/alert/([0-9]*)', AlertAPI)
    ]

    return url

def start_service():

    app = make_app()
    app.listen(8000)
    IOLoop.instance().start()


if __name__ == '__main__':
    print(start_service)
    print(make_app)