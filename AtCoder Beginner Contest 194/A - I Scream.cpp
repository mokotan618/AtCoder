// https://atcoder.jp/contests/abc194/tasks/abc194_a

#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

int main(){
  int a, b;
  cin >> a >> b;

  if(15 <= a+b && 8 <= b){
    cout << "1" << endl;
  }
  else if(10 <= a+b && 3 <= b){
    cout << "2" << endl;
  }
  else if(3 <= a+b){
    cout << "3" << endl;
  }
  else{
    cout << "4" << endl;
  }
  return 0;
}