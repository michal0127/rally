#include <iostream>
using namespace std;

int nwd_opt(int a, int b) {
    int licznik = 0;
    while(a > 0) {
        a = a % b;
        b = b - a;
        licznik++;
        }
    cout << "Powtórzeń: " << licznik << endl;
    return b;
}

int nwd_klas(int a, int b) {
    
    int licznik = 0
    while (a != b) {
        if (a > b) {
            a = b - a;
            }
        else ()
        licznik++;
        }
    cout << "Powtórzeń: " << licznik <<endl;
    return a;
}

int main(int argc, char **argv)
{
    int a, b;
    cout << "Podaj liczby: ";
    cin >> a >> b;
    cout << "Największy wspólny dzielnik: " << nwd_opt(a, b);
    
    return 0;
}
