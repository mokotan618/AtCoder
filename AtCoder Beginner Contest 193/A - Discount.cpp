// https://atcoder.jp/contests/abc193/tasks/abc193_a

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  double A, B;
  cin >> A >> B;

  cout << (1-(B/A))*100 << endl;

  return 0;
}