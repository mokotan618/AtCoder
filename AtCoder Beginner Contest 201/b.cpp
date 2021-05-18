#include<bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
  vector<string> S(N);
  vector<int> T(N);
  for(int i = 0; i < N; i++){
    cin >> S[i] >> T[i];
  }

  int count=0;

  vector<string> S_temp(2);
  vector<int> T_temp(2);

  S_temp[0] = "";
  S_temp[1] = "";
  T_temp[0] = 0;
  T_temp[1] = 0;

  for(int i = 0; i < N; i++){
    if(T_temp[0] < T[i]){
      S_temp[1] = S_temp[0];
      S_temp[0] = S[i];
      T_temp[0] = T[i];
      count++;
    }
  }

  if(count == 1){
    for(int i = 0; (i < N) && (T_temp[0] != T[i]); i++){
    if(T_temp[0] < T[i]){
      S_temp[1] = S_temp[0];
      S_temp[0] = S[i];
      T_temp[0] = T[i];
      count++;
      }
    }
    cout << S_temp[0] << endl;
  }

  cout << S_temp[1] << endl;

  return 0;
}