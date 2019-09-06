/*
 * prostokąt.cpp
 * 
 * Copyright 2018  <>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>

using namespace std;

int obwod(int a, int b){
       return 2 * a + 2 * b;
}

int pole(int a, int b){
       return a * b;
}

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
        
    cout << "Podaj długość boku 1: ";
    cin >> a;


    cout << endl << "Podaj długość boku 2: ";
    cin >> b;
    
    cout << a << endl;
    cout << b << endl;
    cout << endl << "Obwód prostokąta: " << obwod(a, b) << endl;
    cout << endl << "Pole prostokąta: " << pole(a, b) << endl;

	return 0;
}

