// https://atcoder.jp/contests/abc197/tasks/abc197_b

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int h, w, x, y;
  cin >> h >> w >> x >> y;
  vector<string> s(h+2);

  // 外側に＃を配置
  for(int i = 1; i < h+1; i++) cin >> s[i];
  for(int i = 0; i < w+2; i++){
    s[0] += "#";
    s[h+1] += "#";
  }
  for(int i = 1; i < h+1; i++) s[i]= "#" + s[i] + "#";

  // for(int i = 0; i < h+2; i++){
  //  cout << s[i] << endl;
  // }

  int count = 1;
  
  // 上に
  for(int i = 1; i < h+2; i++){
    if(s[x-i][y] == '.'){
      //cout << '(' << x-i << ',' << y <<')' << endl;
      count++;
    }
    else{
      break;
    }
  }

  // 下に
  for(int i = 1; i < h+2; i++){
    if(s[x+i][y] == '.'){
      //cout << '(' << x+i << ',' << y <<')' << endl;
      count++;
    }
    else{
      break;
    }
  }

  // 左に
  for(int i = 1; i < h+2; i++){
    if(s[x][y-i] == '.'){
      //cout << '(' << x << ',' << y-i <<')' << endl;
      count++;
    }
    else{
      break;
    }
  }

  // 右に
  for(int i = 1; i < h+2; i++){
    if(s[x][y+i] == '.'){
      //cout << '(' << x << ',' << y+i <<')' << endl;
      count++;
    }
    else{
      break;
    }
  }

  cout << count << endl;

  return 0;
}