// https://atcoder.jp/contests/apg4b/tasks/APG4b_cj

#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  vector<int> vec(N);
  for (int i = 0; i < N; i++) {
    cin >> vec.at(i);
  }

  int ave = 0;
  for(int i = 0; i < N; i++){
    ave += vec.at(i);
  }
  ave /= N;

  for(int i = 0; i < N; i++){
      vec.at(i) -= ave;
      if(vec.at(i) < 0){
          vec.at(i) = -1 * vec.at(i);
      }
      cout << vec.at(i) << endl;
  }
}
