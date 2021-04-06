// https://atcoder.jp/contests/apg4b/tasks/APG4b_ca

#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  vector<pair<int, int>> vp(N);

  for(int i = 0; i < N; i++){
      int a;
      int b;
      cin >> a >> b;
      vp.at(i) = make_pair(b, a);
  }
  sort(vp.begin(), vp.end());
  
  for(int i = 0; i < N; i++){
      int a;
      int b;
      tie(a, b) = vp.at(i);
      vp.at(i) = make_pair(b, a);
  }

  for(auto a : vp){
      cout << a.first << " " << a.second << endl;
  }
}