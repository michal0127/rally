#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
    print("Wytypuj {} z {} liczb".format(ileliczb, maksliczba))

    # losowanie liczb
    liczby = []  # lista wylosowanych liczb
    # print("Wylosowano:", liczba)
    # pobranie typu użytkownika
    for i in range(ileliczb):
        liczba = random.randint(1, maksliczba + 1)  # losowanie liczby <1; 10>
        if liczby.count(liczba) == 0:  # sprawdzenie czy wartość jest w liście
            liczby.append(liczba)
    print(liczby)
    # odp = input("Podaj liczbę od 1 do 10: ")
    # print("Podana liczba: ", odp)
    # if liczba == odp:  # porównywanie z wylosowaną liczbą
    #     print("Zgadłeś!")
    #     break  # przerwanie działania pętli
    # else:
    #     print("Spróbuj ponownie")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
