#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  min_max.py
#  

import random

def minmax1():
    a = int(input('Podaj liczbę: '))
    min = a
    max = a
    
    while True:
        a = int(input('Podaj liczbę: '))
        if a < 1:
            break
        if a < min:
            min = a
        if a > max:
            max = a
            
    return min, max
    
def minmax2(lista):

    min = max = 0
    for liczba in lista[0]:
        if liczba < min:
            min = liczba
        if liczba > max:
            max = liczba
    
    return min, max

def main(args):
    # min, max = minmax1()
    # print("Najmniejsza liczba:", min)
    # print("Największa liczba:", max)

    lista = []
    for i in range(100):
        lista.append(random.randint(1, 100))
    print(lista)
    print("Najmniejsza liczba:", min)
    print("Największa liczba:", max)
    min, max = minmax2(lista)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
