// https://atcoder.jp/contests/abc199/tasks/abc199_c

#include<bits/stdc++.h>
using namespace std;

int main(){
  int N;
  string S;
  int Q;

  cin >> N >> S >> Q;

  vector<int> T(Q), A(Q), B(Q);

  for(int i = 0; i < Q; i++){
    cin >> T[i] >> A[i] >> B[i];
  }

  for(int i = 0; i < Q; i++){
    A[i]--; B[i]--;
  }

  string S1 = S.substr(0, N);
  string S2 = S.substr(N);
 
  for(int i = 0; i < Q; i++){
    if(T[i] == 1){
      if(B[i] < N){
        swap(S1[A[i]], S1[B[i]]);
        //cout << "yaa" << endl;
      }else if((A[i] < N ) && (N <= B[i])){
        swap(S1[A[i]], S2[B[i]-N]);
        //cout << "hin" << endl;
      }else if(N <= A[i]){
        swap(S2[A[i]-N], S2[B[i]-N]);
        //cout << "owari" << endl;
      }
      //cout << S1 + S2 << endl;
    }else{
        swap(S1, S2);
      //cout << S1 + S2 << endl;
    }
  }
  cout << S1 + S2 << endl;

  return 0;
}
