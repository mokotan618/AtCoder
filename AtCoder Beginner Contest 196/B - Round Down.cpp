// https://atcoder.jp/contests/abc196/tasks/abc196_b

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
  string s;
  cin >> s;
  
  string ss = "";

  for(int i = 0; i < s.length(); i++){
    if(s[i] == '.') break;
    ss += s[i];
  }

  cout << ss << endl;
  return 0;
}