from sqlalchemy import Column, Integer, String
from data.database import Base

class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    usr_type = Column(String(255))

    def __init__(self, name, usr_type):
        self.name = name
        self.usr_type = usr_type
        