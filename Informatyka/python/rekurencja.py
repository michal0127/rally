#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwadraty.py
# 

import turtle

def rysujKwadrat(zolw, bok, ile):
    # for i in range(4):
        zolw.forward(bok)
        zolw.right(190)
        # if ile > 0:
        if ile < ile + 1:
            rysujKwadrat(zolw, bok + 2, ile - 1,)
            
def rysuj(zolw, bok, kat, warunek):
    zolw.forward(bok)
    zolw.right(kat)
    if kat < warunek:
        rysuj


def main(args):
    turtle.title("Kwadraty")
    turtle.setup(1200, 1000)
   
    zolw = turtle.Turtle()
    zolw.color('blue')
    zolw.speed(0)
   
    rysujKwadrat(zolw, 100, 145)
   
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

