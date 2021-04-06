// https://atcoder.jp/contests/apg4b/tasks/APG4b_ci

#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;

  cout << max(max(A, B), C) - min(min(A, B), C) << endl;
}
