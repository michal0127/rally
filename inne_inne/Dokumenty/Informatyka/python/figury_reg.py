#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury_reg.py
#

import turtle

def rysuj(bok, kat, przyrost, warunek):
    turtle.forward(bok)
    turtle.right(kat)
    if kat < warunek:
        rysuj(bok + 1, kat + 1,warunek, przyrost)

def main(args):
    turtle.setup(800, 600)
    turtle.color('green', 'yellow')
    turtle.begin_fill()
    turtle.speed(0)
    
    rysuj(bok=100, kat=20, przyrost=10, warunek=180)
    
    turtle.end_fill()
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

