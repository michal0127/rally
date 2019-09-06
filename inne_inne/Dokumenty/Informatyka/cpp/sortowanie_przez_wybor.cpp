/*
 * sortowanie_przez_wybor.cpp
 * 
 */

#include <cmath>
#include <iostream>
#include <iomanip>

using namespace std;

const int N = 20; // liczba liczb

int main()
{
  int d[N],i,j,k;

// Najpierw wypełniamy tablicę d[] liczbami pseudolosowymi
// a następnie wyświetlamy jej zawartość

  srand((unsigned)time(NULL));

  for(i = 0; i < N; i++) d[i] = rand() % 100;
  for(i = 0; i < N; i++) cout << setw(4) << d[i];
  cout << endl;

// Sortujemy

  for(j = 0; j < N - 1; j++)
  {
    k = j;
    for(i = j + 1; i < N; i++)
      if(d[i] < d[k]) k = i;
    swap(d[k], d[j]);
  }

// Wyświetlamy wynik sortowania

  cout << "Od najmniejszej do największej:\n";
  for(i = 0; i < N; i++) cout << setw(4) << d[i];
  cout << endl;
  return 0;
} 
