#coding:utf-8

import unittest
from sqlalchemy import *
from sqlalchemy.orm import *
mysql_engine = create_engine('mysql://root:keen@localhost/logsss', encoding = 'utf8', echo = True)

Session = sessionmaker()
session = Session(bind = mysql_engine)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class M_Logsss(Base):
    __tablename__ = 'logsss'
    id = Column(Integer, primary_key = True)
    id_code = Column(String(50), nullable = False)
    update_at = Column(DateTime(), nullable = False)
    create_at = Column(DateTime(), nullable = False)
    tags = Column(String(100), nullable = True)
    status = Column(Integer, nullable = False)
    content = Column(Text)

Base.metadata.create_all(mysql_engine)
