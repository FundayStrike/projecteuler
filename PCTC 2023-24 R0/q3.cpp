#include <bits/stdc++.h>
using namespace std;

int main(){
  ios::sync_with_stdio(false); cin.tie(0);
  string s, res;
  cin >> s;
  for (int i=2; i!=1; i=(i+1)%6){
    res += s[i];
  }
  res += s[1];
  cout << res;
}
