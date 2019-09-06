#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby-23.py
#  

def liczby2(a, b):
    """
    Drukuje wszystki liczby dwucydrowe, którym nie powatarzają się cyfry
    np.: 11, 22, 33 ...
    Oraz zwraca ich ilość
    """

    ile = 0

    for i in range(1, 10):
        for j in range(0, 10):
            if i ! = j
                print("{}{}".format(i, j), end="")
                ile +=1
    return ile


def liczby3(c, d, e):
    
    ile3 = 0

    for i in range(100, 999):
        for j in range(0, 10):
            if i ! = j
                print("{}{}".format(i, j), end="")
                ile +=1
    return ile

    return suma


def liczby3(a, b):
    """
    Drukuje wszystkie liczby 3 cyfrowe, gdzie nie powtarzają się cyfry
    Bez 111 112 11x, 66x itd
    """

    ilosc = 0

    for x in range(a, b + 1, 1):
        c = x % 111
        ile = x % 110
        e = x % 101
        g = x % 100
        if c != 0 and ile != 0 and e != 0 and g != 0:
            z = 0
            z = int(x / 10)
            if z % 11 != 0:
                print(x)
            ilosc = ilosc + 1
    print("Ilośc takich liczb: ", ilosc)

    return "To była funkcja Liczby3"


def main(args):

    print(liczby2(10, 99))
    print(liczby3(100, 999))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
