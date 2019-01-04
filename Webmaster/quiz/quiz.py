#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py
#  
from flask import g
from modele import *
from views import *

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='kjlsdajhksdfjkhnjksdfkjsdcjkcszd',
))

# to łączy sie z baza przed zapytaniem
@app.before_request
def before_request():
    g.db = baza
    g.db.connect()
    
# to rozłącza się z bazą po zapytaniu
@app.after_request
def after_request(response):
    g.db.close()
    return response


if __name__ == '__main__':
    app.run(debug=True)
