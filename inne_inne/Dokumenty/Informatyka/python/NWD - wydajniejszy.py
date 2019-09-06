#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  NWD.py
#  
#  Copyright 2018  <>
#  

def nwd(a, b):
    licznik = 0
    while a != b:
        if a > b:
            a = a - b
            licznik += 1
        else:
            b = b - a
            licznik += 1
    return a, licznik


def main(args):
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    print("Największy wspólny dzielnik {} i {} to {} " .format(a, b, nwd(a, b)))
    print("Powtórzeń: ", licznik)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
