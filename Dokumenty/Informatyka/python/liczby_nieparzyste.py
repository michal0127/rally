#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby_nieparzyste.py
#

def wersja1():
    n = int(input("Podaj liczbę naturalną: "))
    while i < n:
        print(i)
        i += 2


def wersja2():
    n = int(input("Podaj liczbę naturalną: "))
    for i in range(1, n, 2):
        print(i)
    
def main(args):
    wersja2()
    return 0

# algorytm częściowo poprawny, skończony, ma złożoność liniową O(), czyli nie zawiera rozgałęzień, nie ma instrukcji warunkowych

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
