

#include<bits/stdc++.h>
using namespace std;

int main(){
  long long N, K;
  cin >> N >> K;

  string N_moji;

  for(int i = K; i > 0; i--){
    if(N % 200 == 0){
      N /= 200;
    }
    else{
      N_moji = to_string(N) + "200";
      N = stod(N_moji);
    }
  }

  cout << N << endl;

  return 0;
}