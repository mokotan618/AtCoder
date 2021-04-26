// https://atcoder.jp/contests/abc192/tasks/abc192_b

#include<bits/stdc++.h>
using namespace std;

int main(){
  string S;
  cin >> S;

  //bool b = 1;
  for(int i = 0; i < S.length(); i++){
    if(i%2 == 0){
      if(isupper(S[i])){
        cout << "No" << endl;
        //b = 0;
        return 0;
      }
    }else{
      if(islower(S[i])){
        cout << "No" << endl;
        //b = 0;
        return 0;
      }
    }
  }
  //if(b){
    cout << "Yes" << endl;
  //}
  return 0;
}
