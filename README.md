##Introduction

build for reading Flask, sqlalchemy.

##LICENSE

MIT


##HOW TO USE

BEFORE:

1. fix database setting at model_logsss.py

THEN:

1. git clone https://github.com/callsamleung/logsss
2. cd logsss
3. python setup.py develop (maybe permission use sudo)
4. python logsss/db.init.py (your will see ok)
4. python run.py

##CHANGLOG

2014/08/10 23:37:14:

1. add setup.py 
2. update HOW TO USE
3. use blueprint at home_index.py


20140714:

1. test blueprint for url('/l') route


20140709:

1. list data @ index.html
2. add class Content_tags @ view_logsss.py


20140708:

1. data struct: content(text), id_code(string), status(int), update_at(datetime), create_at(datetime), tags(string)
