#include <stdio.h>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main(){
    int n, k, cnt = 0;
    cin >> n >> k;
    int li[n];
    for(int i = 0; i < n; i++){
        cin >> li[i];
    }
    
    for(int i = 0; i < n; i++){
        if(li[i] >= li[k - 1] && li[i] > 0){
            cout << li[i] << endl;
            cnt++;
        }
    }
    cout << cnt << endl;
    
    return 0;
}