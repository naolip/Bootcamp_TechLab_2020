from sqlalchemy import Column, String, Integer
from data.database import Base
import operator

class Salas(Base):
    __tablename__ = 'salas'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    max_allowed = Column(Integer)

    def __init__(self, name, max_allowed):
        self.name = name
        self.max_allowed = max_allowed


