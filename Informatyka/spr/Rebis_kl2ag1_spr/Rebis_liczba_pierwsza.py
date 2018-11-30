#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    n = int(input("Podaj liczbę: "))
    x = 2
    
    for j in range(n+1):
        if not x*x <= n:
            print("To liczba pierwsza")
            return
        if not (n % x) == 0:
               x += 1
        else: 
            print("To nie liczba pierwsza")  
            return

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
