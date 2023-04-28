from sqlalchemy import Column, String, Integer, Text 
from data.database import Base 

class Frames(Base):
    __tablename__ = 'frames'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    frame = Column(Text(4294000000))

    
    def __init__(self, name, frame):
        self.name = name
        self.frame = frame


    def to_json(self):
        fields = dict()

        for column in self.__table__.columns:
            fields[column.name] = getattr(self, column.name)

        
        return fields