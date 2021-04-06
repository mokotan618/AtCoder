// https://atcoder.jp/contests/apg4b/tasks/APG4b_bz

#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  map<string, int> score;

  for(int i = 0; i < N; i++){
    string num;
    cin >> num;
    if(score.count(num)){
      int kosuu = score.at(num);
      kosuu++;
      score[num] = kosuu;
      // cout << "hinn";
    }else{
      score[num] = 1;
      // cout << "yaa";
    }
  }
  
  int count_n = 0;
  string count_s ="";
  for (auto p : score) {
    if(count_n < p.second){
      count_s = p.first;
      count_n = p.second;
    }
  // cout << v;
  
}
  cout << count_s << " " <<  count_n << endl;
}