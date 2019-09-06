#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wej-wyj.py
#
#
import random


def main(args):
    liczby = 5
    zakres = 30
    for i in range(0, liczby, 1):
        wynik = random.randint(1, zakres)
        print(wynik)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
