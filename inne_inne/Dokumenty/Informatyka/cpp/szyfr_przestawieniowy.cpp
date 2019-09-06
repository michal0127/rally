/*
 * szyfr_przestawieniowy.cpp
 */


/*
#include <iostream>
#include <string>

using namespace std;

#define MAKS 100

void szyfruj(int klucz, char tab[]) {
    klucz = klucz % 26;
    int kod = 0;
    int i = 0;
    while (tab[i] != '\0') {
        if (tab[i] == ' ') {
            cout << tab[i];
            i++;
            }
        kod = (int)tab[i] + klucz;
        if (kod > 122) {
            kod = kod - 26;
            }
        cout << (char)kod;
        i++;
        }
    }

void szyfruj(char tab[], int klucz, int reszta) {
    int ile strlen(tb);
    cout << ile << endl;
    int reszta = ile % klucz;
    if (reszta > 0) {
        (klucz % tab[i]) = reszta, i++;
        if 
    }
}

int main(int argc, char **argv)
{
    char tekst[100];
    int klucz = 0;
    cout << "Podaj tekst: \n";
    cin.getline(tekst, MAKS);
    cout << cin.gcount() << endl;
    cout << strlen(tekst) << endl;
    
    cout << "Podaj klucz: ";
    cin >> klucz;
    szyfruj(klucz, tekst);
    
    return 0;
}
*/


#include<iostream>
#include<cstring>
using namespace std;

void kodowanie(char *napis)
{
    int dl = strlen(napis); //wyznaczenie liczby znaków
   
    for(int i=0; i<dl-1; i+=2) //przesuwamy się o dwa znaki
    //zamiana sąsiadujących znaków
    {
        char pom = napis[i];
        napis[i] = napis[i+1]; //dlatego w pętli i<dl-1
        napis[i+1] = pom;   
    }
}

int main()
{
    char napis[100];
   
    cout<<"Podaj napis do zaszyfrowania: ";
    cin.getline(napis, 100);
   
    cout<<"Przed szyfrowaniem: ";
    cout<<napis<<endl;
   
    //szyfrujemy
    kodowanie(napis);
   
    cout<<"Szyfrogram: ";
    cout<<napis<<endl;
   
    //deszyfrujemy
    kodowanie(napis);
   
    cout<<"Tekst jawny: ";
    cout<<napis<<endl;
   
    cin.get();
    return 0;
}


