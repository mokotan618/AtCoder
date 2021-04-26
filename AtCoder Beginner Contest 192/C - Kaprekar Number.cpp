// https://atcoder.jp/contests/abc192/tasks/abc192_c

#include<bits/stdc++.h>
using namespace std;

int g1(int N){
  string S = to_string(N);
  sort(S.begin(), S.end(), greater<int>());
  return stoi(S);
}

int g2(int N){
  string S = to_string(N);
  sort(S.begin(), S.end());
  return stoi(S);
}

int f(int N){
  return g1(N) - g2(N);
}

int f_n(int N, int K){
  if(K == 0){
    return N;
  }else{
    return f_n(f(N), K-1);
  }
}

int main(){
  int N, K;
  cin >> N >> K;

  cout << f_n(N, K) << endl;

  return 0;
}
