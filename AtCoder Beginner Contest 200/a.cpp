

#include<bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
  int count = 0;

  while(N > 0){
    count++;
    N -= 100;
  }

  cout << count << endl;
  
  return 0;
}