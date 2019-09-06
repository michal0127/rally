/*
 * algorytm.cpp
 * 
 * Copyright 2019  <>
 */


#include <iostream>
using namespace std;

int silnia_re(int n) {
    ;
}

int silnia_it(int n) {
    int silnia = 1;
    int i;
    for (i = 1; i <= n; i++)
    silnia = silnia * i;
    return silnia;
}

int main(int argc, char **argv)
{
	int n;
    cout << "Podaj liczbę: "; cin >> n;
    cout << "Wynik: " << silnia_it(n);
	return 0;
}

