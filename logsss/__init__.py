#coding:utf-8

from flask import Flask
from view_logsss import content_status, Logsss, Content_tags
from model_logsss import M_Logsss
from lgs_content.lgs_index import lgs_index

def create_app(config_file):
    app = Flask(__name__)
    app.register_blueprint(lgs_index)
    return app

