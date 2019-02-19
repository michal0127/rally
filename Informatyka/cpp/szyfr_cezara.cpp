/*
 * szyfr_cezara.cxx
 */


#include <iostream>

using namespace std;

#define MAKS 100 

void szyfruj(int klucz, char tab[]) {
   klucz = klucz % 26;
   int kod = 0;
   int i = 0;
   while (tab[i] != '\0') {
       if ((int)tab[i] == 32){
           continue;
           }
       kod = (int)tab[i] + klucz;
       cout << (char)kod;
       i++;
       } 
}

int main(int argc, char **argv)
{   
	char tekst[100];
    int klucz = 0;
    cout << "Podaj tekst: ";
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    szyfruj(klucz, tekst);
	return 0;
}
