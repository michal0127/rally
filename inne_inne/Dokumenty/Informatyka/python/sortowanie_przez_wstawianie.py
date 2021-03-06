#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sortowanie_przez_wstawianie.py
#  
#  Copyright 2018  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



def insertion_sort1(tab):
    for i in range(len(tab)):
    assert tab[0:i]==sorted(tab[0:i]), 'Naruszenie niezmiennika petli'
    j = i
    while j > 0 and tab[j] < tab[j-1]:
        tab[j], tab[j-1] = tab[j-1], tab[j]
        j -= 1
    return 0;

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
