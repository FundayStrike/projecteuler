#include <bits/stdc++.h>
using namespace std;

int main(){
  ios::sync_with_stdio(false); cin.tie(0);
  int total = 0;
  int num;
  while (total < 12){
    cin >> num;
    total += num;
  }
  cout << total-12;
}
