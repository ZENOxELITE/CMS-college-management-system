from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(String(50), primary_key=True)
    name = Column(String(100))
    department = Column(String(100))
    year = Column(Integer)
    email = Column(String(100))
    phone = Column(String(20))
