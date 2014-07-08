#coding:utf-8

from datetime import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from view_logsss import content_status, Logsss
from model_logsss import M_Logsss

app = Flask(__name__)
v_logsss = Logsss()
@app.route('/', methods = ['get', 'post'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        status = request.form['status']
        new_obj = M_Logsss(id_code = 'adfjkwqeflwqelfjl', update_at = datetime.now(),\
                                   create_at = datetime.now(),\
                                   tags = 'test',\
                                   status = status,\
                                   content = 'content_test')
        return v_logsss.add_logsss(new_obj)
    return 'nothing here'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
