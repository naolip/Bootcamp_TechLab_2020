from sqlalchemy import Column, String, Integer
from data.database import Base

class Reports(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    report_text = Column(String(1000))

    def __init__(self, name, report_text):
        self.name = name
        self.report_text = report_text

        