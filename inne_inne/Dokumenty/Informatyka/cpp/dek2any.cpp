/*
 * dek2any.cpp
 */


#include <iostream>
#include <math.h>
using namespace std;

int dec2any(int liczba, int podstawa, int tab[]){
    int i = 0;
    do {
       tab[i] = liczba % podstawa;
       liczba = liczba / podstawa;
       i++;
    }while ( liczba != 0);
    return i-1;
}

void bin2dec(int tab[]){
        ;
}

void anytodec(int tab[]){
        int podstawa = 0;
        do {
            cout << "Podstawa [2,9]";
            cin >> podstawa;
            } while (podstawa < 2 || podstawa > 9);
            
            int ile = 0;
            cout << "Ile cyfr";
            cin >> ile;
            for (int i = 0; i < ile; i++)
                do {
                    cout << "Podaj cyfrę [0-" << podstawa -1 << "]: ";
                    while (tab[i] < 0 || tab[i] > podstawa -1);
                }
    int liczba10 = 0;
    for (int x = 0; x < ile ; ile++) {
        int wynik = pow()
        }
    cout << "Wynik: " << liczba10;
}

int main(int argc, char **argv)
{
    int tab[8];
    int liczba, podstawa;
    cout << "Podaj liczbę i podstawę systemu docelowego: ";
    cin >> liczba;
    cin >> podstawa;
    int i = dec2any(liczba, podstawa, tab);
    cout << "Wynik: ";
    while (i > -1) {
        cout << tab[i];
        i--;
        }

    return 0;
}

