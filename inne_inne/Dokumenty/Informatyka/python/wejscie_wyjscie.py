#!/usr/bin/env python
# -*- coding: utf-8 -*-
# duck typing
#wszystko co pobierane jest z domyślnego wejścia z terminala jest znakiem

def main(args):
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    print(a) 
    print(b) 
    
    print("Suma: ", a + b)
    print("Różnica: ", a - b)
    print("Iloczyn: ", a * b)
    print("Iloraz: ", a / b)
     
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
