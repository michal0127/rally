#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)  # losowanie liczby <1; 10>
    print("Wylosowano:", liczba)
    # pobranie typu użytkownika
    for i in range(3):
        odp = input("Podaj liczbę od 1 do 10: ")
        print("Podana liczba: ", odp)

        if liczba == odp:  # porównywanie z wylosowaną liczbą
            print("Zgadłeś!")
            break  # przerwanie działania pętli
        else:
            print("Spróbuj ponownie")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
