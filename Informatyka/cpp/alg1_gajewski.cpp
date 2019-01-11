/*
 * alg1_gajewski.cpp
 *
 * algorytm jest mało wydajny jeżli chodzi o liczby nieparzyste, gdyż musi osoiągnać warotść 100 żeby zakończyć działanie i podać wynik
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{   int a = 0;
    cout << "Podaj liczbę a: ";
    cin >> a;
    if (a <= 0 or a > 99) {
        cout << "Podaj liczbę a: ";
        cin >> a;
        }

    for (int i = 2; i < 101; i += 2) {
        if (a == i) {
            cout << "a jest liczbą parzystą";
            break;
            }
        if (i == 100) {
            cout << "a jest liczbą nieparzystą";
        }
    }

    return 0;
}

