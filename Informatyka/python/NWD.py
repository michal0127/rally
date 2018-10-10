#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  NWD.py
#  
#  Copyright 2018  <>
#  

def nwd(a, b):
    if a == b:
    r = a % b
    if r > 0:
        a = b
        b = r
        while r==0:
            r=a%b
  else:
    r=b
        


def main(args):
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
