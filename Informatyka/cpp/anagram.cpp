/*
 * anagram.cpp
 */


#include <iostream>

using namespace std;

int zlicz(char tb[]) {
    int i = 0;
    while(tb[i] != '\0') i++;
    return i;
}

void wyswietl(char tekst[], int rozmiar) {
    for(int i = 0; i < rozmiar; i++) {
        cout << tekst[i];
    }
}

int main(int argc, char **argv)
{
	const int rozmiar = 50;
    char tekst[rozmiar];
    cout << "Podaj słowo: " << endl;
    cin.getline(tekst, rozmiar);
    wyswietl(tekst, zlicz(tekst));
	return 0;
}

