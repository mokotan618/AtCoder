// https://atcoder.jp/contests/abc199/tasks/abc199_b

#include<bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;

  vector<int> A(N);
  vector<int> B(N);

  for(int i = 0; i < N; i++){
    cin >> A[i];
  }
   for(int i = 0; i < N; i++){
    cin >> B[i];
  }

  int maxA, minB;

  maxA = -1;
  minB = 10001;

  for(int i = 0; i < N; i++){
    maxA = max(maxA, A[i]);
    minB = min(minB, B[i]);
  }

  //for(int i = 0; i < N; i++){
  //  cout << A[i];
  //}
  //cout << endl;
  //for(int i = 0; i < N; i++){
  //  cout << B[i];
  //}
  //cout << endl;
  if(minB - maxA < 0){
    cout << 0 << endl;
  }else{
    cout << minB - maxA + 1 << endl;
  }

  return 0;
}