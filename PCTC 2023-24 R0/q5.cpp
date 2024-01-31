#include <bits/stdc++.h>
using namespace std;

int main(){
  ios::sync_with_stdio(false); cin.tie(0);
  char letter;
  int refills=0;
  cin >> letter;
  if (letter == 't' || letter == 'c'){
    cin >> refills;
  }
  cout << 1+refills;
}
