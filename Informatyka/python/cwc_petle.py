#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cwc_petle.py
#  

def main(args):
    
    a = int(input("Pierwsza liczba: "))
    b = int(input("Druga liczba: "))
    
    if a + b <= 75:
        for liczba in range(a, b):
            if liczba <= 75:
                print(liczba)
            
    else:
        print("Suma liczb przekroczyła 75")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
