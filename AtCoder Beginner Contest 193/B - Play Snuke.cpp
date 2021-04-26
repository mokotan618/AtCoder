// https://atcoder.jp/contests/abc193/tasks/abc193_b

#include<bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;

  vector<double> A(N), P(N), X(N);
  for(int i = 0; i < N; i++){
    cin >> A[i] >> P[i] >> X[i];
  }
  
  int min = -1;
  double temp = 0;
  for(int i = 0; i < N; i++){
    //↓これは二重ループになる
    //while(0.5 < A[i]){
    //A[i] -= 1;
    //X[i] -= 1;
    if(X[i]-1-(((A[i])*60-30)/60) > 0){
      temp = P[i];
      if(min == -1){
        min = temp;
      }
      else if(temp < min){
        min = temp;
      }
      else{
        continue;
      }
    }
    else{
      continue;
    }
  }

  cout << min << endl;

  return 0;
}