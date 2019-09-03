#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#
#Program pobiera trzy liczby od użytkownika, a następnie wyświetla liczbę największą.
#


def maks(maks):
    m = None
    if a > b:
        if a > c:
            m > a
    elif b > c:
        m = b
    print("Największa :" ,m)
    return m
    
def maks2(a, b, c):
    """
    Funkcja wyszukuje i zwraca największą z trzech podanych liczb
    """
    m = a # zakładamy, że pierwsza podana liczba jest największa
    if b > m:
        m = b
    if c > m:
        m = c
    return m
    
def main(args):
    assert(maks2(3, 2, 1) == 3)
    assert(maks2(3, 1, 2) == 3)
    assert(maks2(3, 3, 1) == 3)
    assert(maks2(3, 3, 2) == 3)
    assert(maks2(2, 3, 1) == 3)
    assert(maks2(2, 1, 3) == 3)
    assert(maks2(1, 2, 3) == 3)
    assert(maks2(1, 3, 2) == 3)
    assert(maks2(3, 1, 1) == 3)
    assert(maks2(1, 3, 3) == 3)
    assert(maks2(1, 3, 2) == 3)
    
    return 0
# dopisz resztę
            

def mojemaks(a, b, c):
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    c = int(input("Podaj trzecią liczbę: "))
    print(a)
    print(b)
    print(c)
    
#    if a > b:
#        print(a, "jest większe od", b)
#        print(a, "jest różne od", b)
#    elif a < b:
#        print(a, "jest mniejsze od", b)
#        print(a, "jest różne od", b)
#    else:
#        print(a, "jest równe", b)

    if a > b and a > c:
        print(a, "jest liczbą największą")
        
    elif b > a and b > c:
        print(b, "jest liczbą największą")
        
    else:
        print(c, "jest liczbą największą")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
