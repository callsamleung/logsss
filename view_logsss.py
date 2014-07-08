#coding:utf-8

import unittest
from model_logsss import M_Logsss
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.orm import *
mysql_engine = create_engine('mysql://root:keen@localhost/logsss', encoding = 'utf8', echo = True)

Session = sessionmaker()
session = Session(bind = mysql_engine)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Content_status():
    def __init__(self):
        self.draft = 0
        self.publish = 1

class Test_Content_status(unittest.TestCase):
    def setUp(self):
        self.c = Content_status()
    def test_status(self):
        self.assertTrue(self.c.draft == 0)
        self.assertTrue(self.c.publish == 1)

content_status = Content_status()

class Logsss():
    def __init__(self):
        pass
    def get_draft(self, identity):
        identity = int(identity)
        recorder = session.query(M_Logsss).filter_by(id = identity, status = content_status).first()
        return recorder
    def get_item(self, identity):
        identity = int(identity)
        recorder = session.query(M_Logsss).filter_by(id = identity).first()
        return recorder
    def get_recorders(self):
        return session.query(M_Logsss).all()
    def add_logsss(self,logsss_model):
        is_success = False
        try:
            session.add(logsss_model)
            session.commit()
            is_success = True
        except:
            is_success = False
        return is_success
            

class Test_Logsss(unittest.TestCase):
    def setUp(self):
        self.l = Logsss()
    def test_add_logsss(self):
        new_obj = M_Logsss(id_code = 'adfjkwqeflwqelfjl', update_at = datetime.now(),\
                               create_at = datetime.now(),\
                               tags = 'test',\
                               status = content_status.draft,\
                               content = 'content_test')
        result = self.l.add_logsss(new_obj)
        self.assertTrue(result)
    def test_get_draft(self):
        ids = '0'
        obj = self.l.get_draft(ids)
        self.assertFalse(obj) # test exists
        #test content
        new_obj = M_Logsss(id_code = 'adfjkwqeflwqelfjl', update_at = datetime.now(),\
                               create_at = datetime.now(),\
                               tags = 'test',\
                               status = content_status.draft,\
                               content = 'content_test')
        session.add(new_obj)
        session.commit()
        ids = new_obj.id
        obj = self.l.get_draft(ids)
        self.assertEqual('content_test', obj.content)
    def test_get_logsss(self):
        ids = 0
        obj = self.l.get_item(ids)
        self.assertTrue(obj == None) # test exists
    def test_get_recorders(self):
        r = self.l.get_recorders()
        self.assertTrue(len(r) > 0)

if __name__ == '__main__':
    unittest.main()
