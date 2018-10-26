#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
import sqlite3

def kwerenda1(cur):
    cur.execute("""
        SELECT COUNT(*) FROM uczniowie WHERE nazwisko='Piasecki' AND imie='Rafał'
        """)
        
        # SELECT 
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
