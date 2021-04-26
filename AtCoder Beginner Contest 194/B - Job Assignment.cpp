// https://atcoder.jp/contests/abc194/tasks/abc194_a

#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

int main(){
  int N;
  cin >> N;

  vector<int> a(N), b(N);

  for(int i = 0; i < N; i++){
    cin >> a[i] >> b[i];
  }
  int ans = 1001001001;
  for(int i = 0; i < N; i++){
    for(int j = 0; j < N; j++){
      int now = 0;
      if (i == j){
        now = a[i] + b[j];
      }
      else{
        now = max(a[i], b[j]);
      }
      ans = min(ans, now);
    }
  }

  cout << ans << endl;

  // vector<vector<int>> zikan(N, vector<int>(2));

  // for(int i = 0; i < N; i++){
  //   for(int j = 0; j < 2; j++){
  //     cin >> zikan.at(i).at(j);
  //   }
  // }

  // for(int i = 0; i < N; i++){
  //   for(int j = 0; j < 2; j++){
  //     cout << zikan.at(i).at(j);
  //   }
  //   cout << endl;
  // }
  return 0;
}