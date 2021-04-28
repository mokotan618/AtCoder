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

  //A[i]B[i]はSの文字の位置を示すためデクリメント

  for(int i = 0; i < Q; i++){
    A[i]--; B[i]--;
  }

  // flag = 0 でそのまま 1 で変化する
  // (この問題では前半N文字と後半N文字を入れ替える)
  // (普通に入れ替えていたらO(NQ)でTLEなので)
  // (まるで入れ替えているかのようにふるまう必要がある)
  // (flagはそのための変数)
  // (類題でrevarseが来ても安心)

  bool flag = 0;

  for(int i = 0; i < Q; i++){
    if(flag == 0){
      if(T[i] == 1){
        swap(S[A[i]], S[B[i]]);
      }else if(T[i] == 2){
        flag = 1;
      }
    }else if(flag == 1){
      if(T[i] == 1){
        if(B[i] < N){
          swap(S[A[i]+N], S[B[i]+N]);
        }else if((A[i] < N ) && (N <= B[i])){
          swap(S[A[i]+N], S[B[i]-N]);
        }else if(N <= A[i]){
          swap(S[A[i]-N], S[B[i]-N]);
        }
      }else if(T[i] == 2){
        flag = 0;
      }
    }
  }

  string S1 = S.substr(0, N);
  string S2 = S.substr(N);

  if(flag == 1){
    swap(S1, S2);
  }

  cout << S1 + S2 << endl;

  return 0;
}
