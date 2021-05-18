// https://atcoder.jp/contests/abc200/tasks/abc200_c

#include<bits/stdc++.h>
using namespace std;

int combi_2(int x){
    if((x == 1)||(x == 0)){
      return 0;
    }
    else{
      return x*(x-1)/2;
    }
}

int main(){
  int N;
  vector<int> A(N);

  cin >> N;
  for(int i = 0; i < N; i++){
    cin >> A[i];
  }

  for(int i = 0; i < N; i++){
    A[i] %= 200;
  }

  int count_combi_sum = 0;
  int count_200 = 0;


  for(int i = 0; i < N; i++){
    for(int j = 0; j < 200; j++){
      if(A[i] == j){
        count_200++;
  
      }
    }
    count_combi_sum += combi_2(count_200);
    count_200 = 0;
  }
  
  cout << count_combi_sum << endl;
  
  return 0;
}