/*
 * szkielet.cpp
 *
 */


#include <iostream>
/* io input/output czyli biblioteka wejścia/wyjścia w pythonie nie trzeba tego importować
 * zawsze musi być main bo to nazwa funkcji*/

using namespace std;

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
    
    cout << "Podaj liczbę 1: ";
    cin >> a;
    cout << a;

    cout << endl << "Podaj liczbę 2: ";
    cin >> b;
    cout << b;
    
    cout << endl << "Suma: " << a + b << endl;
    cout << "Różnica: " << a - b << endl;
    cout << "Iloczyn: "<< a * b << endl;
    cout << "Iloraz: "<< a /b << endl;

    return 0;
}

//DRY dont repeat yourself
