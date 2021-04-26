// https://atcoder.jp/contests/abc195/tasks/abc195_a

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
  int m, h;
  cin >> m >> h;
  
  if(h % m == 0){
    cout << "Yes" << endl;
  }
  else{
    cout << "No" << endl;
  }

  return 0;
}