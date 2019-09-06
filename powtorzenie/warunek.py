#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunek.py
#  
#  Copyright 2019 kl3ag2 <kl3ag2@ubu16>
#  


def main(args):
    a = int(input("Wprowadź pierwszą liczę: "))
    b = int(input("Wprowadź drugą liczę: "))
    c = int(input("Wprowadź trzecią liczę: "))
    print(a)
    print(b)
    print(c)

    if a > b and a > c:
        print ("Największą liczbą to: ", a)
    elif b > a and b > c:         
        print ("Największą liczbą to: ", b)
    else:                         
        print ("Największą liczbą to: ", c)

    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
