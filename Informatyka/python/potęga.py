#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potęga.py
#  

def potega_it(a, n):
    # a^n = a1*a2*... an
    
    iloczyn = 1
    for i in range(n):
        iloczyn = iloczyn * a 
    return iloczyn

def main(args):
    a = int(input("Podaj podstawę: "))
    n = int(input("Podaj wykładnik: "))
    print("{} do potęgi {} wynosi {}".format(a, n, potega_it(a, n)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
