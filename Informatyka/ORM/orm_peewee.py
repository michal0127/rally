#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py
#  

import os
from peewee import *

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik)

## MODELE DANYCH

class BazaModel(Model):
    class Meta:
        database = baza

class Klasa(Model):
    nazwa = CharField(null=false) # nie pozwala żeby klasa nie miała nazwy
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    
    class Meta:
        database = baza
        
class Uczen(Model):
    imie = CharField(null=false) # nie pozwala żeby klasa nie miała nazwy
    nazwisko = CharField(null=false)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')

    class Meta:
        database = baza
        
class Wynik(BazaModel):
    egzhum = FloatField(default=0) # nie pozwala żeby klasa nie miała nazwy
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Klasa, related_name='wyniki')

def main(args):
    if os.path_exist(baza_plik):
        os.remove(baza.plik)
    baza.connect() # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
