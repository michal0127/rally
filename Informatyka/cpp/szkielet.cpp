/*
 * szkielet.cpp
 *
 */


#include <iostream>
/* io input/output czyli biblioteka wejścia/wyjścia w pythonie nie trzeba tego importować
 * zawsze musi być main bo to nazwa funkcji*/

using namespace std;

int main(int argc, char **argv)
/* int to integer, czyli to nadaje się do liczb całkowitych */
{
    int liczba;  //deklaracja zmiennej liczba typu całkowitego
    liczba = 7;
    // std::cout << liczba; // pozwala wypisać co zrobiło, coś takiego jak print


    int a, b, c; // deklaracja zmiennych
    a = b = c = d = 10; // inicjalizacja zmiennych
    a = 10; // przypisanie
    b = 2 * a; // mnożenie
    c = b + a; // dodawanie
    d = a / b; // dzielenie
    
        cout << liczba;
    cin >> a;

    cout << "\n" << a << " " << b << " " << (b - a);
    // "\n" new line, nowa linia
    cout << "\n" << d;
    return 0;
}
