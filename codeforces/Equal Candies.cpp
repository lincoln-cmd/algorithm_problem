//# include <bits/stdc++.h>
# include <stdio.h>
# include <vector>
# include <climits>
# include <iostream>
# include <algorithm>

//using namespace std;

using std::cin;
using std::endl;
using std::cout;
using std::min;
using std::vector;

int main(){
    int t;
    cin >> t;
    for(int test = 0; test < t; test++){
        int n;
        cin >> n;
        vector<int> a(n);
        int cnt = 0;
        int minimum = INT_MAX;
        for(int i = 0; i < n; i++){
            cin >> a[i];
            minimum = min(minimum, a[i]);
        }
        for(int i = 0; i < n; i++){
            cnt += a[i] - minimum;
        }
        cout << cnt << endl;
    }
    return 0;
}