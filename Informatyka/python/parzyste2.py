#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parzyste.py
#  

def main(args):
    
    start = int(input("Pierwsza liczba: "))
    stop = int(input("Druga liczba: "))
    
    while start >= stop:
        stop = int(input("Podałeś większa liczbe niz pierwszą! Myśl co robisz i dawaj mi takie liczby jak się należy draniu: "))
        

    for liczba in range(start, stop + 1):
        # if liczba % 2 == 0:
        if not liczba % 2:
            print(liczba)
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
