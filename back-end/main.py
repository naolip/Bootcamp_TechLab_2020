from tornado.web import Application, RequestHandler

from data.database import session_factory
from data.dao.alert_dao import Alert_dao
from data.dao.camera_dao import Camera_dao
from data.dao.frame_dao import Frame_dao
from data.dao.report_dao import Report_dao
from data.dao.sala_dao import Sala_dao
from data.dao.usuario_dao import User_dao
from service.alert_service import make_app


def build_services():
    urls = list()

    urls.append(make_app)


    return Application(urls)



def start_service():

    app = build_services()
    app.listen(8000)
    IOLoop.instance().start()


if __name__ ==  '__main__':
    application = Application(make_app)
    application.listen(8888)
    IOLoop.current().start()