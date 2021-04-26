// https://atcoder.jp/contests/abc199/tasks/abc199_c

#include<bits/stdc++.h>
using namespace std;

int main(){
  int N;
  string S;
  int Q;

  cin >> N >> S >> Q;

  vector<int> T(Q);
  vector<int> A(Q);
  vector<int> B(Q);

  for(int i = 0; i < Q; i++){
    cin >> T[i] >> A[i] >> B[i];
  }

  string temp1 = "";
  string temp2 = "";

  for(int i = 0; i < Q; i++){
    if(T[i] == 1){
      temp1 = S[A[i]-1];
      temp2 = S[B[i]-1];
      S.replace(A[i]-1, 1, temp2);
      S.replace(B[i]-1, 1, temp1);
      //cout << S << endl;
    }else{
      temp1 = S.substr(0,N);
      temp2 = S.substr(N);
      S = temp2 + temp1;
      //cout << S << endl;
    }
  }
  cout << S << endl;

  //cout << S << endl;
  //for(int i = 0; i < Q; i++){
  //  cout << T[i] << " " << A[i] << " " << B[i] << endl;
  //}

  return 0;
}