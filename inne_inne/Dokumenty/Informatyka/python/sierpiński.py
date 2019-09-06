#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sierpiński.py
#  

import turtle

def draw_sierpinski(length,depth):
    window = turtle.Screen()
    t = turtle.Turtle()
    if depth==0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length/2,depth-1)
        t.fd(length/2)
        draw_sierpinski(length/2,depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw_sierpinski(length/2,depth-1)
    window.exitonclick()


draw_sierpinski(500,1)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
