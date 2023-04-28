from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:12345678@localhost:50050/cybertech', echo=True)

_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

#tabelas
from data.model.alert_model import Alerts
from data.model.camera_model import Cameras
from data.model.frame_model import Frames
from data.model.report_model import Reports
from data.model.sala_model import Salas
from data.model.usuario_model import Usuarios 


Base.metadata.create_all(engine)

def session_factory():
    return _SessionFactory()
