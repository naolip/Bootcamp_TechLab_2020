from sqlalchemy import Column, String, Integer
from data.database import Base

class Cameras(Base):
    __tablename__ = 'cameras'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)

    def __init__(self, name):
        self.name = name


    def to_json(self):
        fields = dict()

        for column in self.__table__.columns:
            fields[column.name] = getattr(self, column.name)

        return fields