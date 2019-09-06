#include <iostream>
#define MAKS 100
using namespace std;




void wyswietl(char tekst[], int n){
    for(int i=0;i<n;i++){
        cout<<tekst[i];
    }
}

void szyfruj(char tekst[], int klucz, int n){


    char zaszyfrowany[n];

    int pos=0;

   for(int i = 0; i < klucz; i++){
       for(int j = i; j < n; j+=klucz){
           zaszyfrowany[pos]=tekst[j];
           pos++;
       }
   }


    for(int i=0;i<n;i++){
        tekst[i]=zaszyfrowany[i];
    }


}

void deszyfruj(char tekst[], int klucz, int n){
    char zaszyfrowany[n];
    int pos=0;

    int m=n/klucz;
    cout<<endl;
    for(int i=0;i<m;i++){
        for(int j=i;j<n;j+=m){
            zaszyfrowany[pos]=tekst[j];
            pos++;
        }

    }

    for(int i=0;i<n;i++){
        tekst[i]=zaszyfrowany[i];
    }

}


int main()
{
    // pobierz dane wejsciowe

    char tekst[MAKS];
    int klucz;
    cin.getline(tekst, MAKS);
    cin >> klucz;

    int n=cin.gcount()-1;


    //DOPELNIENIE TEKSTU

   int dop=klucz - n%klucz;

   for(int i=n;i<dop+n;i++){
       tekst[i]=',';
   }

   n+=dop;

    //lower(tekst, n);
    szyfruj(tekst, klucz, n);
    wyswietl(tekst, n);
    cout<<endl;
    deszyfruj(tekst, klucz, n);
    wyswietl(tekst, n);


	return 0;
}

