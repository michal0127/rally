#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  forms.py
#  

from flask_wtf import FlaskForm


class OdpForm(FlaskForm):
    id = HiddenField("Odpowiedz id")
    pytanie = HiddenField("Pytanie id")
    odpowiedz = StringField('Odpowiedź:',
                             validators)
