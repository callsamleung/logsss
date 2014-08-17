#coding:utf-8

from logsss import create_app

if __name__ == '__main__':
    app = create_app('')
    app.config['DEBUG'] = True
    app.run(host = '0.0.0.0', debug = True)
