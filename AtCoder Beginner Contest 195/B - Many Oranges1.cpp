// https://atcoder.jp/contests/abc195/tasks/abc195_b

#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

int main(){
  int a, b, w;
  cin >> a >> b >> w;

  const int INF = 1001001001;
  int l = INF, r = -INF;
  w *= 1000;

  for(int n = 1; n <= w; ++n){
    if(a*n <= w && w <= b*n){
      l = min(l, n);
      r = max(r, n);
    }
  }
  if (l == INF){
    cout << "UNSATISFIABLE" << endl;
  }
  else{
    cout << l << " " << r << endl;
  }
  return 0;
}