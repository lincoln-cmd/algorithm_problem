#include <stdio.h>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main(){
    int m, n, cnt = 0;
    cin >> m >> n;
    if(m >= 2 && n >= 1){
        cnt += (m / 2) * n;
        m -= (m / 2) * 2;
    }
    
    if(m >= 1 && n >= 2){
        cnt += (n / 2) * m;
    }
    cout << cnt << endl;
    
    return 0;
}