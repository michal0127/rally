#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
import sqlite3

def kwerenda1(cur):
    cur.execute("""
        SELECT 
    """)
        
        # SELECT klasa, COUNT(uczniowie.id) AS 
        # SELECT klasa, COUNT(*) FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa GROUP BY klasa
        # SELECT klasa, nazwisko, imie, egz_mat FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa WHERE klasa='1A'
        # SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie WHERE egz_hum > 40 AND egz_mat > 40 ORDER BY nazwisko ASC 
        # WHERE plec=1
        # SELECT imie LIKE '%a'
        # SELECT nazwisko, imie, egz_hum, egz_mat, FROM uczniowie ORDER BY egz_hum D
        # SELECT * FROM uczniowie WHERE nazwisko = 'Piasecki'
        # SELECT egz_hum, egz_mat FROM uczniowie WHERE nazwisko='Piasecki' and imie='Rafał'
        # SELECT * FROM uczniowie WHERE nazwisko='Piasecki' AND imie='Rafał'
        # SELECT COUNT(*) FROM uczniowie WHERE nazwisko LIKE 'G%'
        
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)

def main(args):
    baza_nazwa = 'uczniowie'
    tebele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    kwerenda1(cur)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
