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
    nazwa = CharField(null=False) 
    # nie pozwala żeby klasa nie miała nazwy
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    
    class Meta:
        database = baza
        
class Uczen(Model):
    imie = CharField(null=False) 
    # nie pozwala żeby klasa nie miała nazwy
    nazwisko = CharField(null=False)
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
    if os.path.exists(baza_plik):
        os.remove(baza.plik)
    baza.connect() # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])
    
    kl2a = Klasa(nazwa="2A", roknaboru=2010, rokmatury=2013)
    kl2a.save()
    
    kl1a = Klasa(nazwa="1A", roknaboru=2011, rokmatury=2014)
    kl1a.save()
    
    u1 = Uczen(imie='Ferdynand', nazwisko='Kiepski', plec=False, klasa=kl2a)
    u1.save()
    u2 = Uczen(imie='Marian', nazwisko='Paździoch', plec=False, klasa=kl1a)
    u2.save()
    u3 = Uczen(imie='Arnold', nazwisko='Boczek', plec=False, klasa=kl1a)
    u3.save()
    
    uczniowie= Uczen.select()
    for uczen in uczniowie:
        print(uczen.id, uczen.nazwisko, uczen.klasa.nazwa)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
