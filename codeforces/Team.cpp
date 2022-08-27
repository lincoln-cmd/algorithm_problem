#include <stdio.h>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main(){
    int n, p, v, t, cnt = 0;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> p >> v >> t;
        if(p + v + t >= 2){
            cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
}