#!/usr/bin/python3
"""
First state model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

user=sys.argv[1]
passwd=sys.argv[2]
db=sys.argv[3]
db_url = "mysql://{}:{}@localhost:3306/{}".format(user, passwd, db)

engine = create_engine(db_url)

Base = declarative_base()

class State(Base):
    """"Creates State class, inherits from Base"""
    
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

Base.metadata.create_all(engine)