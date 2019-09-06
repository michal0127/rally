#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parzyste.py
#  

def main(args):
    
    start = int(input("Pierwsza liczba: "))
    stop = int(input("Druga liczba: "))
    
    if start < stop:
        for liczba in range(start, stop + 1):
            # if liczba % 2 == 0:
            if not liczba % 2:
                print(liczba)
            
    else:
        print("Ziomek, kiepskie dane mi wprowadziłeś, zapodaj coś innego")
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
