/*
 * alg1_rębiś.cpp
 *
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{   int a = 0;
    cout << "Podaj liczbę: ";
    cin >> a;
    if (a <= 0 or a > 99) {
        cout << "Podaj liczbę: ";
        cin >> a;
        }
    for (int i = 2; i < 100; i += 2) {
        if (a == i) {
            cout << "Parzysta";
        }
            break;
        if (i == 100) {
            cout << "Parzysta";
        }
    }

    return 0;
}
