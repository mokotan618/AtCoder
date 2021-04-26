// https://atcoder.jp/contests/abc198/tasks/abc198_b

#include<bits/stdc++.h>
using namespace std;

int main() {
    string N;
    cin >> N;
    
    while (N[N.length() - 1] == '0'){
      N = N.substr(0, N.length() - 1);
    } 

    string NN = N;

    reverse(NN.begin(), NN.end());
    // cout << N << endl;
    // cout << NN << endl;

    if(N == NN){
      cout << "Yes" << endl;
    }
    else{
      cout << "No" << endl;
    }

    return 0;
}