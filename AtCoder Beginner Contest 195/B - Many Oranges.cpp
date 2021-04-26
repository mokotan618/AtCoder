// https://atcoder.jp/contests/abc195/tasks/abc195_b

#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

int main(){
  double a, b, w;
  cin >> a >> b >> w;

  w *= 1000;

  int l, r;
  
  l = ceil(w/b);
  r = floor(w/a);  
  if (l > r){
    cout << "UNSATISFIABLE" << endl;
  }
  else{
    cout << l << " " << r << endl;
  }
  return 0;
}