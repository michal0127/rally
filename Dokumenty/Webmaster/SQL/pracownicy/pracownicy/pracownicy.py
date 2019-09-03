#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv
import os.path

def dane_z_pliku(nazwa_pliku, separator=','):
    dane = []  # pusta lista na dane
    
    if not os.path.isfile(nazwa_pliku):
        print("Plik {} nie istnieje.".format(nazwa_pliku))
        return dane
    
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter=separator)
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane


def ile_kolumn(cur, tab):
    """ funkcja zlicza liczbę kolum(pól) w podanej tabeli"""
    i = 0
    for kol in cur.execute("PRAGMA table_info('" + tab + "')"):
        i += 1
    return i
    

def main(args):
    baza_nazwa = 'pracownicy'
    tabele = ['pracownicy', 'kontakty', 'place', 'stanowiska']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open(baza_nazwa + '.sql', 'r') as plik:
        cur.executescript(plik.read())
        
    for tab in tabele:
        ile = ile_kolumn(cur, tab)  # ile mamy kolumn w tabeli
        dane = dane_z_pliku(tab + '.csv')
        ile_d = len(dane[0])
        
        if ile > ile_d:  # nie policzyło pimary key autoincrement
            dane2 = [] # tymczasowa lista na dane
            for r in dane:
                r.insert(0, None) # dodanie None na początku listy
                dane2.append(r)
            dane = dane2
            ile_d += 1
        
        pytajniki = ','.join(['?'] * ile_d)
        
        cur.executemany('INSERT INTO ' + tab + ' VALUES(' + pytajniki + ')', dane)
         

    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
