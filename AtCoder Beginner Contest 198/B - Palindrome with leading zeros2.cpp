// https://atcoder.jp/contests/abc198/tasks/abc198_b

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
  string N;
  cin >> N;

  int L = N.size();

  cout << L << endl;
  // cout << N[L-1] << endl;

  while(N[L-1] == '0'){
    L--;

  }
  for(int i = 0; i < L; i++){
    cout << N[i];
  }
    cout << endl;

  return 0;
}