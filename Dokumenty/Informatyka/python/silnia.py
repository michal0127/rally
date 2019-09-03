#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silnia.py
#  

def silnia_it(n):
    # 0! = 1
    # n! = 1 * 2 * ... * n
    # 4! = 24
    # 5! = 120
    
    silnia = 1
    
    for i in range(1, n + 1):
        silnia = silnia * i
        print(silnia)
        
    return silnia

def main(args):
    n = int(input("Podaj liczbę: "))
    print("{}! równa się {} wynosi".format(n, silnia_it(n)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
