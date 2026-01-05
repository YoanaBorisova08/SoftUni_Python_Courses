from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

CONNECTION_STRING = 'postgresql+psycopg2://postgres:1234@localhost:5432/lab10'
engine = create_engine(CONNECTION_STRING)
Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False, default='Yoana')