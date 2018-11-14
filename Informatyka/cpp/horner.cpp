/*
 * horner.cpp
 * 
 * w(x) = 2x^3 + 3x^2 + 5x + 4 => 6 mnożeń + 3 dodawania
 * w(x) = x (2x^2 + 3x + 5) + 4
 * w(x) = x (x (2x + 3) + 5) +4 => 3 mnożenia + 3 dodawania
 */


#include <iostream>

using namespace std;

void drukujw(int stopien, float tbwsp[]) {
    int i = 0;
    for (int i = 0; i < stopien; i++) {
    cout << tbwsp[i] << "x^" << stopien - i << " + ";
    }
    cout << tbwsp[i] << endl;
}

float horner_it(int stopien, float tbwsp[], float x) {
    float wynik = tbwsp[0];
    for (int i = 1; i < stopien + 1; i++) {
        wynik = wynik * x + tbwsp[i];
    }
    return wynik;
}

int main(int argc, char **argv)
{
	int stopien = 0;
    float x = 0;
    cout << "Podaj stopień wielomianu: ";
    cin >> stopien;
    float *tbwsp; // deklaracja wskaźnika, taka zmienna przechowująca adres komórki w pamięci
    tbwsp = new float [stopien + 1];
    for (int i = 0; i <= stopien; i++) {
        cout << "Podaj współczynnik przy potędze "
             << stopien - i << ": ";
        cin >> tbwsp[i];
    }
    
    cout << "Podaj argument: ";
    cin >> x;
    
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    cout << "\ndla x = " << x << " " << "Wynosi: ";
    cout << horner_it(stopien, tbwsp, x);
    cout << endl;
    
	return 0;
}

