#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alg2_rębiś.py
#  

def main(args):
    a = 0
    while a < 1 or a > 99:
        print('Podana liczba: {}'.format(a))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
