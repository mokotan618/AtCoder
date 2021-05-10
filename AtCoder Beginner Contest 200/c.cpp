

#include<bits/stdc++.h>
using namespace std;

int factorial(int n){
        int answer = 1;
	while(n > 1){
	    answer *= n;
	    n--;
	}
        return answer;
    }

  int calcNumOfCombination(int n, int r){
        return factorial(n) / (factorial(r) * factorial(n-r));
    }

int main(){
  int N;
  cin >> N;

  vector<int> A(N);
  for(int i = 0; i < N; i++){
    cin >> A[i];
  }
  
  int count200 = 0;



  for(int i = 0; i < N; i++){
    if(A[i] % 200 == 0){
      count200++;
    }
  }

  int count = calcNumOfCombination(count200, 2);

  cout << count << endl;

  int NN = N - count200;

  cout << NN << endl;

  vector<int> B(NN);

  int J=0;
  for(int i =0 ; i < N; i++){
    if((A[i] % 200) != 0){
      B[j] = A[i];
      J++;
    }
    
  }

  for(int i = 0; i < N; i++){
    cout << B[i] << endl;
  }

  int counta = 0;

  for(int i = 0; i < B.size(); i++){
    for(int j = i+1; j < B.size(); j++){
      if((B[i] - B[j]) % 200 == 0 ){
        count++;
        counta++;
      }
    }
  }
  
  cout << count << endl;
  cout << counta << endl;

  return 0;
}